# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4507**
- Achados: **651**
- CRITICAL: 0 | HIGH: 11 | MEDIUM: 25 | LOW: 615

## Metadados da sessão

- Match ID: 43fc9abb-4d83-4918-8357-9f2f27f790fa
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **3743**
- Entradas posteriores à eliminação ignoradas: **764**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 77 | 7 | 8 | 3 | 47 | 4 | 2 | não/inconclusivo | 0 |
| Jogador 6 | 80 | 7 | 11 | 3 | 53 | 0 | 1 | não/inconclusivo | 0 |
| Jogador 7 | 230 | 7 | 10 | 1 | 71 | 3 | 0 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 187 | 72 | 35 | 11 | 0 | 11 | 46 | 0.1497 | 10 | 46 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::MOVE_BOARD: 1, ALL_IN::SELL: 3, FAST8::BUY: 14, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 2, FAST8::SELL: 5, STABILIZE::BUY: 54, STABILIZE::BUY_XP: 11, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 27, STABILIZE::PASS: 11, STABILIZE::SELL: 27
- Jogador 1 — recompensas por ação: BUY: média 0.4101 (n=72), BUY_XP: média -0.0282 (n=11), ITEM: média 0.1350 (n=12), MOVE_BENCH: média 0.2525 (n=16), MOVE_BOARD: média 0.0053 (n=30), PASS: média 0.0000 (n=11), SELL: média -0.2011 (n=35)
| Jogador 2 | 132 | 59 | 35 | 3 | 0 | 5 | 22 | 0.0914 | 4 | 24 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 1, ALL_IN::SELL: 6, STABILIZE::BUY: 51, STABILIZE::BUY_XP: 3, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 8, STABILIZE::MOVE_BOARD: 13, STABILIZE::PASS: 5, STABILIZE::SELL: 29
- Jogador 2 — recompensas por ação: BUY: média 0.2410 (n=59), BUY_XP: média -0.0400 (n=3), ITEM: média 0.1862 (n=8), MOVE_BENCH: média 0.2189 (n=9), MOVE_BOARD: média -0.0185 (n=13), PASS: média 0.0000 (n=5), SELL: média -0.1500 (n=35)
| Jogador 3 | 134 | 52 | 23 | 3 | 0 | 10 | 39 | 0.1324 | 5 | 26 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 3, ALL_IN::SELL: 2, STABILIZE::BUY: 44, STABILIZE::BUY_XP: 3, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 16, STABILIZE::MOVE_BOARD: 20, STABILIZE::PASS: 10, STABILIZE::SELL: 21
- Jogador 3 — recompensas por ação: BUY: média 0.3652 (n=52), BUY_XP: média -0.0467 (n=3), ITEM: média 0.2129 (n=7), MOVE_BENCH: média 0.0926 (n=19), MOVE_BOARD: média -0.0035 (n=20), PASS: média -0.0030 (n=10), SELL: média -0.1852 (n=23)
| Jogador 4 | 122 | 47 | 23 | 8 | 2 | 9 | 25 | 0.1188 | 6 | 3 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::MOVE_BENCH: 2, ALL_IN::REROLL: 2, ALL_IN::SELL: 5, STABILIZE::BUY: 41, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 12, STABILIZE::PASS: 9, STABILIZE::SELL: 18
- Jogador 4 — recompensas por ação: BUY: média 0.4626 (n=47), BUY_XP: média -0.0225 (n=8), ITEM: média 0.1562 (n=8), MOVE_BENCH: média -0.1492 (n=13), MOVE_BOARD: média 0.0042 (n=12), PASS: média 0.0000 (n=9), REROLL: média -0.0700 (n=2), SELL: média -0.2735 (n=23)
| Jogador 5 | 144 | 58 | 34 | 11 | 3 | 8 | 22 | 0.1106 | 10 | 7 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::REROLL: 1, ALL_IN::SELL: 4, STABILIZE::BUY: 55, STABILIZE::BUY_XP: 11, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 13, STABILIZE::PASS: 8, STABILIZE::REROLL: 2, STABILIZE::SELL: 30
- Jogador 5 — recompensas por ação: BUY: média 0.3421 (n=58), BUY_XP: média -0.0136 (n=11), ITEM: média 0.1613 (n=8), MOVE_BENCH: média 0.2211 (n=9), MOVE_BOARD: média 0.0154 (n=13), PASS: média -0.0063 (n=8), REROLL: média -0.1300 (n=3), SELL: média -0.2003 (n=34)
| Jogador 6 | 138 | 53 | 27 | 11 | 1 | 9 | 30 | 0.1228 | 13 | 38 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::MOVE_BENCH: 4, ALL_IN::PASS: 1, STABILIZE::BUY: 50, STABILIZE::BUY_XP: 11, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 15, STABILIZE::PASS: 8, STABILIZE::REROLL: 1, STABILIZE::SELL: 27
- Jogador 6 — recompensas por ação: BUY: média 0.3562 (n=53), BUY_XP: média -0.0418 (n=11), ITEM: média 0.1686 (n=7), MOVE_BENCH: média 0.1433 (n=15), MOVE_BOARD: média -0.0133 (n=15), PASS: média -0.0700 (n=9), REROLL: média -0.1300 (n=1), SELL: média -0.1422 (n=27)
| Jogador 7 | 183 | 71 | 32 | 10 | 0 | 12 | 39 | 0.1515 | 9 | 27 |
- Jogador 7 — ações por estratégia: FAST8::BUY: 34, FAST8::ITEM: 8, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 9, FAST8::PASS: 1, FAST8::SELL: 21, STABILIZE::BUY: 37, STABILIZE::BUY_XP: 10, STABILIZE::ITEM: 11, STABILIZE::MOVE_BENCH: 8, STABILIZE::MOVE_BOARD: 19, STABILIZE::PASS: 11, STABILIZE::SELL: 11
- Jogador 7 — recompensas por ação: BUY: média 0.4110 (n=71), BUY_XP: média -0.0260 (n=10), ITEM: média 0.1216 (n=19), MOVE_BENCH: média 0.3318 (n=11), MOVE_BOARD: média -0.0011 (n=28), PASS: média -0.0025 (n=12), SELL: média -0.2219 (n=32)
| Jogador 8 | 181 | 79 | 44 | 8 | 1 | 7 | 32 | 0.1501 | 7 | 36 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 17, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 1, ALL_IN::OTHER: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 15, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 1, STABILIZE::BUY: 62, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 15, STABILIZE::PASS: 7, STABILIZE::SELL: 29
- Jogador 8 — recompensas por ação: BUY: média 0.4462 (n=79), BUY_XP: média -0.0563 (n=8), ITEM: média 0.1322 (n=9), MOVE_BENCH: média 0.2240 (n=15), MOVE_BOARD: média -0.0141 (n=17), OTHER: média 0.0000 (n=1), PASS: média 0.0000 (n=7), REROLL: média -0.0700 (n=1), SELL: média -0.2700 (n=44)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 09:34:30 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 09:34:32 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 09:34:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 09:34:37 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 09:34:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 09:34:38 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 09:34:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 09:34:40 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 09:34:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 09:34:45 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 09:34:46 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 09:34:46 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 09:34:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 09:34:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 09:34:53 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 09:34:54 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 09:34:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 09:35:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 09:35:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 09:35:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-1 | 09:35:11 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 09:35:12 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 09:35:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 09:35:13 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 09:35:13 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 09:35:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 09:35:14 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-1 | 09:35:15 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-1 | 09:35:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 09:35:24 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 2-2 | 09:35:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 09:35:25 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 09:35:26 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 09:35:27 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 2-2 | 09:35:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 09:35:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 09:35:37 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 09:35:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 2-3 | 09:35:38 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 2-3 | 09:35:39 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.1900 |  |
| Jogador 1 | 2-3 | 09:35:40 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-3 | 09:35:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0900 |  |
| Jogador 1 | 2-3 | 09:35:41 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0100 |  |
| Jogador 1 | 2-3 | 09:35:42 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 09:35:42 | MOVE Board -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0200 |  |
| Jogador 1 | 2-4 | 09:35:53 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Ornn | 0.9700 |  |
| Jogador 1 | 2-4 | 09:35:54 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Ornn | 0.0500 |  |
| Jogador 1 | 2-4 | 09:35:55 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-4 | 09:35:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 2-4 | 09:35:56 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 09:35:57 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 2-4 | 09:35:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 2-4 | 09:35:58 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.5000 |  |
| Jogador 1 | 2-4 | 09:35:58 | MOVE Board -> Board: Shen (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 09:36:11 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.1200 |  |
| Jogador 1 | 2-5 | 09:36:12 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 2-5 | 09:36:13 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 2-5 | 09:36:13 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 2-5 | 09:36:14 | MOVE Board -> Board: Krugue (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 09:36:15 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 09:36:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 09:36:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-6 | 09:36:26 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 1 | 2-6 | 09:36:27 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 1 | 2-6 | 09:36:28 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 2-6 | 09:36:29 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 2-6 | 09:36:29 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 2-6 | 09:36:30 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-6 | 09:36:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 09:36:31 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 2-7 | 09:36:41 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 1 | 2-7 | 09:36:41 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 2-7 | 09:36:42 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 2-7 | 09:36:43 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 2-7 | 09:36:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 09:36:58 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-2 | 09:37:17 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 1 | 3-2 | 09:37:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 3-2 | 09:37:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 09:37:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 3-2 | 09:37:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 09:37:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 09:37:33 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 3-3 | 09:37:34 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-4 | 09:37:56 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 3-4 | 09:37:56 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 1 | 3-4 | 09:37:57 | MOVE Bench -> Board: Alistar (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | -0.7200 |  |
| Jogador 1 | 3-4 | 09:37:58 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 1 | 3-4 | 09:37:59 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-4 | 09:38:00 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 1 | 3-4 | 09:38:01 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.4100 |  |
| Jogador 1 | 3-5 | 09:38:13 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Inferno | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 1 | 3-6 | 09:38:36 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 3-6 | 09:38:37 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 09:38:38 | MOVE Board -> Board: Rakan (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 09:38:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-7 | 09:38:56 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 3-7 | 09:38:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_BFSword -> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 3-7 | 09:38:59 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 1 | 3-7 | 09:39:00 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 1 | 3-7 | 09:39:00 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Vi (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 3-7 | 09:39:01 | MOVE Board -> Board: Vi (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 4-1 | 09:39:16 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Inferno | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 4-1 | 09:39:17 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Inferno | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 1 | 4-1 | 09:39:18 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 4-2 | 09:39:49 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 4-2 | 09:39:50 | MOVE Board -> Board: Xayah (i:2.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 1 | 4-2 | 09:39:51 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-2 | 09:39:52 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-2 | 09:39:53 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-2 | 09:39:54 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 09:39:55 | MOVE Board -> Board: Vi (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-3 | 09:40:12 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-4 | 09:40:42 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Inferno | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 1 | 4-4 | 09:40:43 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Inferno | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 4-4 | 09:40:44 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 4-4 | 09:40:45 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-4 | 09:40:46 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 4-4 | 09:40:47 | MOVE Board -> Board: Xayah (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-4 | 09:40:48 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-5 | 09:41:05 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-6 | 09:41:40 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Inferno | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 1 | 4-6 | 09:41:41 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 4-6 | 09:41:42 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Inferno | DA_KogMaw18_AD | -0.1700 |  |
| Jogador 1 | 4-6 | 09:41:43 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-6 | 09:41:44 | MOVE Board -> Board: Xayah (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-6 | 09:41:45 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-7 | 09:42:04 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Inferno | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 4-7 | 09:42:05 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Inferno | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 5-1 | 09:42:38 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Inferno | DA_18_Rakan | -0.6000 |  |
| Jogador 1 | 5-1 | 09:42:39 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 118 | 5 | Inferno | DA_18_Rakan | 0.7700 |  |
| Jogador 1 | 5-1 | 09:42:40 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 120 | 5 | Inferno | DA_18_Rakan | -0.0100 |  |
| Jogador 1 | 5-1 | 09:42:41 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 117 | 5 | Inferno | DA_18_Rakan | 0.1900 |  |
| Jogador 1 | 5-1 | 09:42:42 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 120 | 5 | Inferno | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 5-1 | 09:42:43 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 117 | 5 | Inferno | DA_18_Rakan | 0.2200 |  |
| Jogador 1 | 5-1 | 09:42:44 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 120 | 5 | Inferno | DA_18_Rakan | -0.0600 |  |
| Jogador 1 | 5-2 | 09:43:02 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 133 | 5 | Inferno | DA_18_Rakan | 0.9100 |  |
| Jogador 1 | 5-3 | 09:43:41 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 149 | 5 | Inferno | DA_18_Rakan | -0.4700 |  |
| Jogador 1 | 5-3 | 09:43:42 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 147 | 5 | Inferno | DA_18_Rakan | 0.9100 |  |
| Jogador 1 | 5-3 | 09:43:42 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 149 | 5 | Inferno | DA_18_Rakan | -0.5100 |  |
| Jogador 1 | 5-3 | 09:43:43 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 147 | 5 | Inferno | DA_18_Rakan | 0.9000 |  |
| Jogador 1 | 5-3 | 09:43:44 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 150 | 5 | Inferno | DA_18_Rakan | -0.4600 |  |
| Jogador 1 | 5-3 | 09:43:45 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 149 | 5 | Inferno | DA_18_Rakan | 1.0200 |  |
| Jogador 1 | 5-3 | 09:43:46 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 149 | 5 | Inferno | DA_18_Rakan | 0.5500 |  |
| Jogador 1 | 5-4 | 09:44:04 | COMPROU: Lux (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 157 | 5 | Fera do Rift | DA_18_Rakan | -0.1400 |  |
| Jogador 1 | 5-5 | 09:44:40 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 169 | 5 | Fera do Rift | DA_18_Rakan | 1.0200 |  |
| Jogador 1 | 5-5 | 09:44:41 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 172 | 5 | Fera do Rift | DA_18_Rakan | -0.5900 |  |
| Jogador 1 | 5-5 | 09:44:42 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 170 | 5 | Fera do Rift | DA_18_Rakan | 1.0200 |  |
| Jogador 1 | 5-5 | 09:44:42 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 167 | 5 | Fera do Rift | DA_18_Rakan | 1.0200 |  |
| Jogador 1 | 5-5 | 09:44:44 | MOVE Bench -> Board: Grompe (i:8.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 167 | 5 | Fera do Rift | DA_18_Rakan | 0.3400 |  |
| Jogador 1 | 5-5 | 09:44:45 | MOVE Bench -> Board: Lux (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Fera do Rift | DA_18_Rakan | 0.1300 |  |
| Jogador 1 | 5-6 | 09:45:06 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 174 | 5 | Fera do Rift | DA_18_Rakan | 0.1300 |  |
| Jogador 1 | 5-6 | 09:45:07 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 171 | 5 | Fera do Rift | DA_18_Rakan | -0.1900 |  |
| Jogador 1 | 5-7 | 09:45:43 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Fera do Rift | DA_18_Rakan | 1.0100 |  |
| Jogador 1 | 5-7 | 09:45:44 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 175 | 5 | Fera do Rift | DA_18_Rakan | 0.3700 |  |
| Jogador 1 | 5-7 | 09:45:45 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Fera do Rift | DA_18_Rakan | 0.8900 |  |
| Jogador 1 | 5-7 | 09:45:47 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Aronguejo (i:4.0) (tabuleiro slot 23) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Fera do Rift | DA_18_Rakan | 0.0700 |  |
| Jogador 1 | 5-7 | 09:45:48 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Fera do Rift | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 6-1 | 09:46:11 | VENDEU: Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 191 | 5 | Fera do Rift | DA_18_Rakan | -0.5000 |  |
| Jogador 1 | 6-1 | 09:46:12 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 188 | 5 | Fera do Rift | DA_18_Rakan | 1.0100 |  |
| Jogador 1 | 6-1 | 09:46:13 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 187 | 5 | Fera do Rift | DA_18_Rakan | 1.0100 |  |
| Jogador 1 | 6-2 | 09:46:52 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 194 | 5 | Fera do Rift | DA_Krug18 | 0.5500 |  |
| Jogador 1 | 6-2 | 09:46:53 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 190 | 5 | Fera do Rift | DA_Krug18 | 0.0600 |  |
| Jogador 1 | 6-2 | 09:46:54 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Fera do Rift | DA_Krug18 | -0.0400 |  |
| Jogador 1 | 6-2 | 09:46:55 | EQUIP_FROM_INVENTORY: TFT_Item_Deathblade -> Grompe (i:8.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Fera do Rift | DA_Krug18 | 0.0900 |  |
| Jogador 1 | 6-2 | 09:46:56 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Grompe (i:8.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Fera do Rift | DA_Krug18 | 0.1600 |  |
| Jogador 1 | 6-2 | 09:46:57 | EQUIP_FROM_INVENTORY: TFT_Item_RapidFireCannon -> Grompe (i:8.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Fera do Rift | DA_Krug18 | 0.1500 |  |
| Jogador 1 | 6-3 | 09:47:23 | VENDEU: Krugue (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 208 | 5 | Fera do Rift | DA_Gromp18_AP | -0.5900 |  |
| Jogador 1 | 6-3 | 09:47:24 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 205 | 5 | Fera do Rift | DA_Gromp18_AP | 0.3500 |  |
| Jogador 1 | 6-4 | 09:48:05 | VENDEU: Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 220 | 5 | Fera do Rift | DA_Gromp18_AP | -0.5900 |  |
| Jogador 1 | 6-4 | 09:48:06 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 216 | 5 | Fera do Rift | DA_Gromp18_AP | -0.1100 |  |
| Jogador 1 | 6-4 | 09:48:07 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 217 | 5 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 1 | 6-4 | 09:48:08 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 213 | 5 | Fera do Rift | DA_Gromp18_AP | -0.1100 |  |
| Jogador 1 | 6-4 | 09:48:09 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 216 | 5 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 1 | 6-4 | 09:48:10 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 214 | 5 | Fera do Rift | DA_Gromp18_AP | -0.1100 |  |
| Jogador 1 | 6-4 | 09:48:11 | MOVE Board -> Board: Akali (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 214 | 5 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 1 | 6-5 | 09:48:33 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 226 | 5 | Fera do Rift | DA_Gromp18_AP | 0.0100 |  |
| Jogador 1 | 6-6 | 09:49:14 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 234 | 5 | Fera do Rift | DA_Gromp18_AP | 0.9700 |  |
| Jogador 1 | 6-6 | 09:49:15 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 238 | 5 | Fera do Rift | DA_Gromp18_AP | -0.0200 |  |
| Jogador 1 | 6-6 | 09:49:16 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 236 | 5 | Fera do Rift | DA_Gromp18_AP | 0.5300 |  |
| Jogador 1 | 6-6 | 09:49:17 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 240 | 5 | Fera do Rift | DA_Gromp18_AP | -0.0200 |  |
| Jogador 1 | 6-6 | 09:49:17 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 237 | 5 | Fera do Rift | DA_Gromp18_AP | -0.2600 |  |
| Jogador 1 | 6-6 | 09:49:18 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 237 | 5 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 1 | 6-6 | 09:49:19 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 240 | 5 | Fera do Rift | DA_Gromp18_AP | 0.0200 |  |
| Jogador 1 | 6-7 | 09:49:41 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 250 | 5 | Fera do Rift | DA_Gromp18_AP | 0.4000 |  |
| Jogador 2 | ? | 09:34:30 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 09:34:32 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 09:34:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 09:34:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 09:34:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 09:34:38 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 09:34:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 09:34:45 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 09:34:46 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 09:34:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 09:34:50 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 09:34:53 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 09:34:54 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 09:34:54 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 09:34:55 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 09:34:55 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 09:34:56 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 09:34:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 09:35:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 09:35:03 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 1-4 | 09:35:04 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 09:35:04 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 09:35:05 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 09:35:05 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-1 | 09:35:11 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 09:35:12 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 09:35:12 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 09:35:13 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 2-1 | 09:35:13 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 09:35:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 09:35:14 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-1 | 09:35:15 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 09:35:15 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-2 | 09:35:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 09:35:25 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-2 | 09:35:25 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 09:35:26 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-2 | 09:35:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 09:35:37 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.7700 |  |
| Jogador 2 | 2-3 | 09:35:38 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 2-3 | 09:35:38 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-3 | 09:35:39 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 09:35:40 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-3 | 09:35:40 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-3 | 09:35:41 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 2-3 | 09:35:42 | MOVE Board -> Board: Xayah (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 09:35:42 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-4 | 09:35:53 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 2-4 | 09:35:54 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-4 | 09:35:55 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 09:35:55 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.1900 |  |
| Jogador 2 | 2-4 | 09:35:56 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-4 | 09:35:57 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 2-4 | 09:35:57 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-4 | 09:35:58 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 09:35:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 09:36:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 2-5 | 09:36:12 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.2000 |  |
| Jogador 2 | 2-5 | 09:36:13 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-5 | 09:36:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 09:36:14 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 09:36:15 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 09:36:16 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-5 | 09:36:17 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-6 | 09:36:26 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 2-6 | 09:36:26 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 2-6 | 09:36:27 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-6 | 09:36:28 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Feérico | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-6 | 09:36:29 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 2-6 | 09:36:29 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-6 | 09:36:30 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 0 | Feérico | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 2-6 | 09:36:30 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 2-6 | 09:36:31 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-7 | 09:36:41 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 2-7 | 09:36:41 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 09:36:42 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 09:36:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-7 | 09:36:44 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 2-7 | 09:36:44 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-7 | 09:36:45 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | -0.3100 |  |
| Jogador 2 | 2-7 | 09:36:46 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-1 | 09:36:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Feérico | DA_18_Veigar | 0.8900 |  |
| Jogador 2 | 3-2 | 09:37:17 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Feérico | DA_18_Veigar | 0.8500 |  |
| Jogador 2 | 3-2 | 09:37:17 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-2 | 09:37:18 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 3 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 3-2 | 09:37:20 | MOVE Bench -> Board: Rammus (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 3 | Feérico | DA_18_Veigar | -0.3900 |  |
| Jogador 2 | 3-2 | 09:37:21 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 3 | Feérico | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 3-2 | 09:37:22 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 3 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-3 | 09:37:33 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-3 | 09:37:34 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-4 | 09:37:56 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Feérico | DA_18_Veigar | 0.4800 |  |
| Jogador 2 | 3-4 | 09:37:56 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-4 | 09:37:57 | MOVE Board -> Board: Veigar (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Feérico | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 3-4 | 09:37:58 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 09:37:59 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 09:38:00 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-4 | 09:38:01 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 09:38:13 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Feérico | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 3-6 | 09:38:36 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 4 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-6 | 09:38:37 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Feérico | DA_18_Tristana | 0.9300 |  |
| Jogador 2 | 3-6 | 09:38:38 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 4 | Feérico | DA_18_Tristana | -0.0700 |  |
| Jogador 2 | 3-6 | 09:38:39 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 2 | 3-6 | 09:38:40 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 4 | Feérico | DA_18_Veigar | -0.6000 |  |
| Jogador 2 | 3-6 | 09:38:40 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Feérico | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 3-6 | 09:38:41 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-6 | 09:38:42 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-7 | 09:38:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 3-7 | 09:38:57 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 3-7 | 09:38:59 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-7 | 09:39:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | 0.8700 |  |
| Jogador 2 | 3-7 | 09:39:00 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-7 | 09:39:01 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 4-1 | 09:39:16 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 09:39:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Feérico | DA_18_Veigar | 1.0000 |  |
| Jogador 2 | 4-1 | 09:39:18 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Feérico | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 4-2 | 09:39:49 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Feérico | DA_18_Veigar | 0.4600 |  |
| Jogador 2 | 4-2 | 09:39:50 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Feérico | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 4-2 | 09:39:51 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Feérico | DA_18_Veigar | -0.7000 |  |
| Jogador 2 | 4-2 | 09:39:52 | EQUIP_FROM_INVENTORY: TFT_Item_Crownguard -> Veigar (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 4-2 | 09:39:53 | EQUIP_FROM_INVENTORY: TFT_Item_RunaansHurricane -> Veigar (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Feérico | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 4-2 | 09:39:54 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Kobuko (i:2.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 4-2 | 09:39:55 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Feérico | DA_18_Veigar | -0.2200 |  |
| Jogador 2 | 4-3 | 09:40:12 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-4 | 09:40:42 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Feérico | DA_18_Veigar | 1.0100 |  |
| Jogador 2 | 4-4 | 09:40:43 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-4 | 09:40:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Veigar | 0.3800 |  |
| Jogador 2 | 4-4 | 09:40:45 | VENDEU: Ezreal (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 09:40:46 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 4-4 | 09:40:47 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 4-4 | 09:40:48 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Veigar | 0.0600 |  |
| Jogador 3 | ? | 09:34:30 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 09:34:32 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 09:34:33 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 09:34:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 09:34:37 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 09:34:38 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 09:34:38 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 09:34:40 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 09:34:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 09:34:45 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 09:34:46 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 09:34:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 09:34:47 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 09:34:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 09:34:50 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 09:34:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 09:34:54 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 09:34:54 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 09:34:55 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 09:34:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 09:35:01 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 09:35:03 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 09:35:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 09:35:04 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 09:35:05 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-4 | 09:35:05 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-1 | 09:35:11 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 09:35:12 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 09:35:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 09:35:24 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 09:35:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 09:35:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 09:35:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 09:35:37 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 09:35:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-3 | 09:35:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 09:35:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 09:35:54 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-4 | 09:35:55 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.7100 |  |
| Jogador 3 | 2-4 | 09:35:55 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.4700 |  |
| Jogador 3 | 2-4 | 09:35:56 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-4 | 09:35:57 | MOVE Bench -> Board: Akali (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 2-4 | 09:35:57 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 2-4 | 09:35:58 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.6200 |  |
| Jogador 3 | 2-4 | 09:35:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-5 | 09:36:11 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.8700 |  |
| Jogador 3 | 2-5 | 09:36:12 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.4400 |  |
| Jogador 3 | 2-5 | 09:36:13 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.3600 |  |
| Jogador 3 | 2-5 | 09:36:13 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 09:36:14 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 09:36:15 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-5 | 09:36:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 09:36:26 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 2-6 | 09:36:26 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-6 | 09:36:27 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 09:36:28 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 2-6 | 09:36:29 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 09:36:29 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 09:36:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 09:36:41 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 2-7 | 09:36:41 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | -0.5900 |  |
| Jogador 3 | 2-7 | 09:36:42 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 2-7 | 09:36:43 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.4200 |  |
| Jogador 3 | 2-7 | 09:36:44 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 2-7 | 09:36:44 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.4600 |  |
| Jogador 3 | 2-7 | 09:36:45 | MOVE Bench -> Board: Shen (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 2-7 | 09:36:46 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Devastador | DA_18_Akali_AD | -0.5300 |  |
| Jogador 3 | 3-1 | 09:36:58 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Devastador | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 3-2 | 09:37:17 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Devastador | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 3-2 | 09:37:17 | MOVE Bench -> Board: Rengar (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Devastador | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 3-2 | 09:37:18 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | -0.3300 |  |
| Jogador 3 | 3-2 | 09:37:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 3-2 | 09:37:21 | MOVE Bench -> Board: Sivir (i:8.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 09:37:22 | MOVE Bench -> Board: Rengar (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 3-3 | 09:37:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Devastador | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 3-3 | 09:37:34 | MOVE Board -> Board: Sivir (i:8.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 09:37:56 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 09:37:56 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Devastador | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 3-4 | 09:37:57 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 09:37:58 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 3-4 | 09:37:59 | MOVE Board -> Board: Rengar (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 09:38:00 | MOVE Board -> Board: Shen (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 09:38:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-5 | 09:38:13 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 3-6 | 09:38:36 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Devastador | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 3-6 | 09:38:37 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-6 | 09:38:38 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-6 | 09:38:39 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 09:38:40 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 09:38:40 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 09:38:41 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 09:38:42 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Devastador | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 3-7 | 09:38:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Devastador | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 3-7 | 09:38:57 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Devastador | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 3-7 | 09:38:59 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 09:39:00 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_Akali_AD | 0.7700 |  |
| Jogador 3 | 3-7 | 09:39:00 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Devastador | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 3-7 | 09:39:01 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_Akali_AD | -0.1100 |  |
| Jogador 3 | 4-1 | 09:39:16 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-1 | 09:39:17 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Devastador | DA_18_Akali_AD | 0.8600 |  |
| Jogador 3 | 4-1 | 09:39:18 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Devastador | DA_18_Akali_AD | -0.4400 |  |
| Jogador 3 | 4-2 | 09:39:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Devastador | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 4-2 | 09:39:50 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 09:39:51 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Devastador | DA_18_Akali_AD | -0.1500 |  |
| Jogador 3 | 4-2 | 09:39:52 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 09:39:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 09:39:54 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 09:39:55 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Devastador | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 4-3 | 09:40:12 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-4 | 09:40:42 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Devastador | DA_18_Akali_AD | 0.8800 |  |
| Jogador 3 | 4-4 | 09:40:43 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Devastador | DA_18_Akali_AD | -0.5300 |  |
| Jogador 3 | 4-4 | 09:40:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Devastador | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 3 | 4-4 | 09:40:45 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Devastador | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 3 | 4-4 | 09:40:46 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Devastador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 3 | 4-4 | 09:40:47 | MOVE Bench -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Devastador | DA_KogMaw18_AD | -1.1700 |  |
| Jogador 3 | 4-4 | 09:40:48 | MOVE Bench -> Board: Akali (i:4.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Devastador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 3 | 4-5 | 09:41:05 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Devastador | DA_18_Akali_AD | -0.1400 |  |
| Jogador 3 | 4-6 | 09:41:40 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Devastador | DA_18_Akali_AD | 1.0200 |  |
| Jogador 3 | 4-6 | 09:41:41 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Devastador | DA_18_Akali_AD | 1.0200 |  |
| Jogador 3 | 4-6 | 09:41:42 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Devastador | DA_18_Akali_AD | 0.3200 |  |
| Jogador 3 | 4-6 | 09:41:43 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Devastador | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 4-6 | 09:41:44 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Devastador | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 4-6 | 09:41:45 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Devastador | DA_18_Akali_AD | 0.4300 |  |
| Jogador 3 | 4-7 | 09:42:04 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-7 | 09:42:05 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Lobo Trevoguari (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Devastador | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 5-1 | 09:42:38 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Lobo Trevoguari (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Devastador | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 5-1 | 09:42:39 | VENDEU: Grompe (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Devastador | DA_18_Akali_AD | -0.7400 |  |
| Jogador 3 | 5-1 | 09:42:40 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Devastador | DA_18_Akali_AD | 0.9800 |  |
| Jogador 3 | 5-1 | 09:42:41 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 5-1 | 09:42:42 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Devastador | DA_18_Akali_AD | 1.0900 |  |
| Jogador 3 | 5-1 | 09:42:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Devastador | DA_18_Akali_AD | 0.3900 |  |
| Jogador 3 | 5-1 | 09:42:44 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Devastador | DA_18_Akali_AD | 0.5000 |  |
| Jogador 4 | ? | 09:34:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 09:34:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 09:34:33 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 09:34:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 09:34:37 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 09:34:38 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 09:34:38 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 09:34:40 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 09:34:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 09:34:45 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 09:34:46 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 09:34:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 09:34:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 09:34:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 09:34:53 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 09:34:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 09:34:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 09:35:01 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 09:35:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 09:35:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 09:35:11 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 09:35:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 09:35:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 09:35:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 09:35:25 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 09:35:25 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 09:35:26 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 09:35:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 09:35:27 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 09:35:28 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 09:35:28 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-2 | 09:35:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 09:35:37 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 09:35:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 09:35:38 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 09:35:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 09:35:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 09:35:40 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 09:35:41 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 09:35:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 09:35:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 4 | 2-4 | 09:35:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 09:35:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 09:35:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 09:35:55 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 2-4 | 09:35:56 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 2-4 | 09:35:57 | MOVE Bench -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-4 | 09:35:57 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 2-4 | 09:35:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 09:35:58 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 09:36:11 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 4 | 2-5 | 09:36:12 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 2-5 | 09:36:13 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 2-5 | 09:36:13 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 09:36:14 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-5 | 09:36:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-6 | 09:36:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 4 | 2-6 | 09:36:26 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 4 | 2-6 | 09:36:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 09:36:28 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 4 | 2-6 | 09:36:29 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 4 | 2-6 | 09:36:29 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 2-6 | 09:36:30 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 4 | 2-6 | 09:36:30 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-6 | 09:36:31 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 09:36:41 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 2-7 | 09:36:41 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 09:36:42 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 09:36:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 09:36:44 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 4 | 2-7 | 09:36:44 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-7 | 09:36:45 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 09:36:46 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 3-1 | 09:36:58 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-2 | 09:37:17 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-2 | 09:37:17 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Florescer | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 4 | 3-2 | 09:37:18 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Florescer | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 4 | 3-2 | 09:37:20 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Florescer | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 4 | 3-2 | 09:37:21 | MOVE Bench -> Board: Vi (i:6.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Florescer | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 4 | 3-2 | 09:37:22 | MOVE Board -> Board: Vi (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-3 | 09:37:33 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-3 | 09:37:34 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 4 | 3-4 | 09:37:56 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Florescer | DA_18_Yunara | 0.8100 |  |
| Jogador 4 | 3-4 | 09:37:56 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Florescer | DA_18_Yunara | 0.7900 |  |
| Jogador 4 | 3-4 | 09:37:57 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 3-4 | 09:37:58 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Florescer | DA_18_Yunara | -0.3800 |  |
| Jogador 4 | 3-4 | 09:37:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Florescer | DA_18_Yunara | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-5 | 09:38:13 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_18_Yunara | 0.7700 |  |
| Jogador 4 | 3-6 | 09:38:36 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_18_Yunara | 0.3000 |  |
| Jogador 4 | 3-6 | 09:38:37 | MOVE Bench -> Board: Diana (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_18_Yunara | 0.0400 |  |
| Jogador 4 | 3-6 | 09:38:38 | MOVE Bench -> Board: Vi (i:6.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_18_Yunara | -0.4300 |  |
| Jogador 4 | 3-6 | 09:38:39 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Florescer | DA_18_Yunara | -0.6300 |  |
| Jogador 4 | 3-6 | 09:38:40 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_Yunara | 0.0500 |  |
| Jogador 4 | 3-6 | 09:38:40 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Sejuani (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_Yunara | 0.0800 |  |
| Jogador 4 | 3-6 | 09:38:41 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Sejuani (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_Yunara | 0.1000 |  |
| Jogador 4 | 3-6 | 09:38:42 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Sejuani (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_Yunara | 0.0900 |  |
| Jogador 4 | 3-7 | 09:38:56 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Florescer | DA_18_Yunara | 0.5100 |  |
| Jogador 4 | 3-7 | 09:38:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Florescer | DA_18_Yunara | 0.1500 |  |
| Jogador 4 | 3-7 | 09:38:59 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Florescer | DA_18_Yunara | 0.1900 |  |
| Jogador 4 | 3-7 | 09:39:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Florescer | DA_18_Yunara | 0.1100 |  |
| Jogador 4 | 3-7 | 09:39:00 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Florescer | DA_18_Yunara | -0.7500 |  |
| Jogador 4 | 3-7 | 09:39:01 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Florescer | DA_18_Diana | -0.6200 |  |
| Jogador 4 | 4-1 | 09:39:16 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Florescer | DA_18_Diana | 0.3400 |  |
| Jogador 4 | 4-1 | 09:39:17 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Florescer | DA_18_Diana | 0.2500 |  |
| Jogador 4 | 4-1 | 09:39:18 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Florescer | DA_18_Diana | -0.0400 |  |
| Jogador 4 | 4-2 | 09:39:49 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Florescer | DA_18_Diana | 0.9400 |  |
| Jogador 4 | 4-2 | 09:39:50 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 4 | Florescer | DA_18_Diana | -0.1400 |  |
| Jogador 4 | 4-2 | 09:39:51 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Florescer | DA_18_Diana | 0.1700 |  |
| Jogador 4 | 4-2 | 09:39:52 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Diana | -0.5500 |  |
| Jogador 4 | 4-2 | 09:39:53 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Florescer | DA_18_Diana | -0.1300 |  |
| Jogador 4 | 4-2 | 09:39:54 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Florescer | DA_18_Diana | -0.6600 |  |
| Jogador 4 | 4-2 | 09:39:55 | MOVE Bench -> Board: Diana (i:6.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Florescer | DA_18_Diana | -0.3300 |  |
| Jogador 4 | 4-3 | 09:40:12 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Florescer | DA_18_Diana | -0.0200 |  |
| Jogador 4 | 4-4 | 09:40:42 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Florescer | DA_18_Diana | 0.7700 |  |
| Jogador 4 | 4-4 | 09:40:43 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Florescer | DA_18_Diana | 0.1900 |  |
| Jogador 4 | 4-4 | 09:40:44 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Florescer | DA_18_Diana | -0.0700 |  |
| Jogador 4 | 4-4 | 09:40:45 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Florescer | DA_18_Diana | -0.0100 |  |
| Jogador 4 | 4-4 | 09:40:46 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Florescer | DA_18_Diana | 0.8800 |  |
| Jogador 4 | 4-4 | 09:40:47 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Florescer | DA_18_Diana | -0.0700 |  |
| Jogador 4 | 4-4 | 09:40:48 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Florescer | DA_18_Diana | -0.0400 |  |
| Jogador 5 | ? | 09:34:30 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 09:34:32 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 09:34:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 09:34:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 09:34:38 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 09:34:38 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 09:34:40 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 09:34:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 09:34:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-2 | 09:34:45 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 09:34:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 09:34:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 09:34:54 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 09:34:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 09:35:01 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 09:35:03 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 09:35:04 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 09:35:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 09:35:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 09:35:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 09:35:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 09:35:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 09:35:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 09:35:25 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 09:35:26 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 09:35:27 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 09:35:27 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 09:35:28 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 09:35:28 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-2 | 09:35:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 09:35:37 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 09:35:38 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 09:35:38 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 09:35:39 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 09:35:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 09:35:40 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 09:35:41 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 09:35:42 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | 0.1900 |  |
| Jogador 5 | 2-3 | 09:35:42 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.1800 |  |
| Jogador 5 | 2-4 | 09:35:53 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2700 |  |
| Jogador 5 | 2-4 | 09:35:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 09:35:55 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-4 | 09:35:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 09:35:56 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-4 | 09:35:57 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.4100 |  |
| Jogador 5 | 2-4 | 09:35:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 09:35:58 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1000 |  |
| Jogador 5 | 2-4 | 09:35:58 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 09:36:11 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0200 |  |
| Jogador 5 | 2-5 | 09:36:12 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 2-5 | 09:36:13 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 09:36:13 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-5 | 09:36:14 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 2-5 | 09:36:15 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-5 | 09:36:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-5 | 09:36:17 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3300 |  |
| Jogador 5 | 2-6 | 09:36:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 2-6 | 09:36:26 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0500 |  |
| Jogador 5 | 2-6 | 09:36:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-6 | 09:36:28 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-6 | 09:36:29 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3700 |  |
| Jogador 5 | 2-6 | 09:36:29 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3300 |  |
| Jogador 5 | 2-6 | 09:36:30 | MOVE Board -> Board: Veigar (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-6 | 09:36:30 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-6 | 09:36:31 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-7 | 09:36:41 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2000 |  |
| Jogador 5 | 2-7 | 09:36:41 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1300 |  |
| Jogador 5 | 2-7 | 09:36:42 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1900 |  |
| Jogador 5 | 2-7 | 09:36:43 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-7 | 09:36:44 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-7 | 09:36:44 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-7 | 09:36:45 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-7 | 09:36:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 3-1 | 09:36:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.7100 |  |
| Jogador 5 | 3-2 | 09:37:17 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.7900 |  |
| Jogador 5 | 3-2 | 09:37:17 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2800 |  |
| Jogador 5 | 3-2 | 09:37:18 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 3-2 | 09:37:20 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2800 |  |
| Jogador 5 | 3-2 | 09:37:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 3-2 | 09:37:22 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.2000 |  |
| Jogador 5 | 3-3 | 09:37:33 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2800 |  |
| Jogador 5 | 3-3 | 09:37:34 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.2000 |  |
| Jogador 5 | 3-4 | 09:37:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.8400 |  |
| Jogador 5 | 3-4 | 09:37:56 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.6300 |  |
| Jogador 5 | 3-4 | 09:37:57 | EQUIP_FROM_INVENTORY: TFT_Item_Crownguard -> Kobuko (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1100 |  |
| Jogador 5 | 3-4 | 09:37:58 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.4900 |  |
| Jogador 5 | 3-4 | 09:37:59 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1500 |  |
| Jogador 5 | 3-4 | 09:38:00 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1200 |  |
| Jogador 5 | 3-4 | 09:38:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 3-5 | 09:38:13 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.6800 |  |
| Jogador 5 | 3-6 | 09:38:36 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3700 |  |
| Jogador 5 | 3-6 | 09:38:37 | MOVE Board -> Board: Tristana (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 3-6 | 09:38:38 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 3-6 | 09:38:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-7 | 09:38:56 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Espinhos Negros | DA_18_Cassiopeia | 0.6800 |  |
| Jogador 5 | 3-7 | 09:38:57 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Espinhos Negros | DA_18_Cassiopeia | 0.1900 |  |
| Jogador 5 | 3-7 | 09:38:59 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Espinhos Negros | DA_18_Cassiopeia | 0.4600 |  |
| Jogador 5 | 3-7 | 09:39:00 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Espinhos Negros | DA_18_Cassiopeia | 0.1800 |  |
| Jogador 5 | 3-7 | 09:39:00 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Espinhos Negros | DA_18_Cassiopeia | -0.4300 |  |
| Jogador 5 | 3-7 | 09:39:01 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Espinhos Negros | DA_18_Cassiopeia | -0.4600 |  |
| Jogador 5 | 4-1 | 09:39:16 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Espinhos Negros | DA_18_Rammus | 0.7800 |  |
| Jogador 5 | 4-1 | 09:39:17 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Espinhos Negros | DA_18_Rammus | 0.3000 |  |
| Jogador 5 | 4-1 | 09:39:18 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Espinhos Negros | DA_18_Rammus | 0.2900 |  |
| Jogador 5 | 4-2 | 09:39:49 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Espinhos Negros | DA_18_Rammus | 0.7400 |  |
| Jogador 5 | 4-2 | 09:39:50 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Espinhos Negros | DA_18_Rammus | -0.4900 |  |
| Jogador 5 | 4-2 | 09:39:51 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Espinhos Negros | DA_18_Rammus | 0.8300 |  |
| Jogador 5 | 4-2 | 09:39:52 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Espinhos Negros | DA_18_Tristana | -0.0500 |  |
| Jogador 5 | 4-2 | 09:39:53 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 1 | Espinhos Negros | DA_18_Tristana | -0.4600 |  |
| Jogador 5 | 4-2 | 09:39:54 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 1 | Espinhos Negros | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 4-2 | 09:39:55 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 1 | Espinhos Negros | DA_18_Tristana | -0.0500 |  |
| Jogador 5 | 4-3 | 09:40:12 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Espinhos Negros | DA_18_Tristana | 0.9300 |  |
| Jogador 5 | 4-4 | 09:40:42 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Vivaz | DA_18_Tristana | -0.1100 |  |
| Jogador 5 | 4-4 | 09:40:43 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Vivaz | DA_18_Tristana | -0.2800 |  |
| Jogador 5 | 4-4 | 09:40:44 | MOVE Board -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Vivaz | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 4-4 | 09:40:45 | MOVE Board -> Board: Tristana (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Vivaz | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 4-4 | 09:40:46 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Vivaz | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 4-4 | 09:40:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Vivaz | DA_18_Tristana | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-5 | 09:41:05 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Vivaz | DA_CrimsonRaptor18 | 0.9100 |  |
| Jogador 5 | 4-6 | 09:41:40 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Vivaz | DA_CrimsonRaptor18 | 0.3600 |  |
| Jogador 5 | 4-6 | 09:41:41 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Vivaz | DA_CrimsonRaptor18 | -0.2200 |  |
| Jogador 5 | 4-6 | 09:41:42 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Vivaz | DA_18_Tristana | -0.1100 |  |
| Jogador 5 | 4-6 | 09:41:43 | REROLL | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Vivaz | DA_18_Tristana | -0.1600 |  |
| Jogador 5 | 4-6 | 09:41:44 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Vivaz | DA_18_Tristana | 0.9300 |  |
| Jogador 5 | 4-6 | 09:41:45 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Vivaz | DA_18_Tristana | -0.5900 |  |
| Jogador 5 | 4-7 | 09:42:04 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Tristana | 0.9300 |  |
| Jogador 5 | 4-7 | 09:42:05 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Tristana | 0.0800 |  |
| Jogador 5 | 5-1 | 09:42:38 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Vivaz | DA_18_Tristana | 0.1300 |  |
| Jogador 5 | 5-1 | 09:42:39 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Vivaz | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 5-1 | 09:42:40 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Tristana | 0.4100 |  |
| Jogador 5 | 5-1 | 09:42:41 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Vivaz | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 5-1 | 09:42:42 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Vivaz | DA_18_Tristana | 0.1000 |  |
| Jogador 5 | 5-1 | 09:42:43 | REROLL | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Vivaz | DA_18_Tristana | -0.1600 |  |
| Jogador 5 | 5-1 | 09:42:44 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Vivaz | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 5-2 | 09:43:02 | COMPROU: Alune (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 95 | 5 | Vivaz | DA_18_Alune | 0.1900 |  |
| Jogador 5 | 5-3 | 09:43:41 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Alune | 0.0000 |  |
| Jogador 5 | 5-3 | 09:43:42 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Vivaz | DA_18_Alune | -0.1700 |  |
| Jogador 5 | 5-3 | 09:43:42 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Vivaz | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 5-3 | 09:43:43 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Vivaz | DA_18_Alune | -0.0100 |  |
| Jogador 5 | 5-3 | 09:43:44 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Vivaz | DA_18_Alune | 0.3600 |  |
| Jogador 5 | 5-3 | 09:43:45 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Vivaz | DA_18_Alune | -0.5300 |  |
| Jogador 5 | 5-3 | 09:43:46 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Vivaz | DA_18_Alune | 0.1400 |  |
| Jogador 5 | 5-4 | 09:44:04 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Vivaz | DA_18_Alune | -0.0500 |  |
| Jogador 6 | ? | 09:34:30 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 09:34:32 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 09:34:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 09:34:37 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 09:34:38 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 09:34:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-2 | 09:34:45 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 09:34:46 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 09:34:46 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 09:34:47 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 09:34:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 09:34:50 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5700 |  |
| Jogador 6 | 1-3 | 09:34:53 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0300 |  |
| Jogador 6 | 1-3 | 09:34:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 09:35:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 09:35:02 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 09:35:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 09:35:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 2-1 | 09:35:11 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 09:35:12 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 09:35:12 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 09:35:13 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 09:35:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 09:35:24 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 09:35:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 09:35:25 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 09:35:26 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-2 | 09:35:27 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 09:35:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 09:35:37 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 09:35:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 09:35:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 2-3 | 09:35:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 09:35:40 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 09:35:40 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 09:35:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 09:35:42 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-3 | 09:35:42 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-4 | 09:35:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 2-4 | 09:35:54 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-4 | 09:35:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 09:35:55 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -0.4500 |  |
| Jogador 6 | 2-4 | 09:35:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 09:35:57 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-4 | 09:35:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 2-4 | 09:35:58 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 2-4 | 09:35:58 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Yorick | -0.6300 |  |
| Jogador 6 | 2-5 | 09:36:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 09:36:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 2-5 | 09:36:13 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Yorick | -0.1900 |  |
| Jogador 6 | 2-5 | 09:36:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 2-5 | 09:36:14 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 2-5 | 09:36:15 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | -1.0200 |  |
| Jogador 6 | 2-5 | 09:36:16 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | 0.6300 |  |
| Jogador 6 | 2-5 | 09:36:17 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.1400 |  |
| Jogador 6 | 2-6 | 09:36:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-6 | 09:36:26 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 6 | 2-6 | 09:36:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 6 | 2-6 | 09:36:28 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 6 | 2-6 | 09:36:29 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Xayah | -0.1600 |  |
| Jogador 6 | 2-6 | 09:36:29 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Xayah | 0.1200 |  |
| Jogador 6 | 2-6 | 09:36:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Xayah | -0.0400 |  |
| Jogador 6 | 2-6 | 09:36:30 | MOVE Board -> Board: Xayah (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Xayah | -0.0800 |  |
| Jogador 6 | 2-6 | 09:36:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Xayah | 0.0200 |  |
| Jogador 6 | 2-7 | 09:36:41 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.2600 |  |
| Jogador 6 | 2-7 | 09:36:41 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 6 | 2-7 | 09:36:42 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 6 | 2-7 | 09:36:43 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 6 | 2-7 | 09:36:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 2-7 | 09:36:44 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 6 | 2-7 | 09:36:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 2-7 | 09:36:46 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.2900 |  |
| Jogador 6 | 3-1 | 09:36:58 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 6 | 3-2 | 09:37:17 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_Fiddlesticks18 | 0.2000 |  |
| Jogador 6 | 3-2 | 09:37:17 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 6 | 3-2 | 09:37:18 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 6 | 3-2 | 09:37:20 | MOVE Board -> Board: Rakan (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 6 | 3-2 | 09:37:21 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 6 | 3-2 | 09:37:22 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 6 | 3-3 | 09:37:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_Fiddlesticks18 | 0.7200 |  |
| Jogador 6 | 3-3 | 09:37:34 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.2800 |  |
| Jogador 6 | 3-4 | 09:37:56 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_Fiddlesticks18 | 0.8000 |  |
| Jogador 6 | 3-4 | 09:37:56 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.3400 |  |
| Jogador 6 | 3-4 | 09:37:57 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.4600 |  |
| Jogador 6 | 3-4 | 09:37:58 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 6 | 3-4 | 09:37:59 | MOVE Board -> Board: Xayah (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 6 | 3-4 | 09:38:00 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-4 | 09:38:01 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 6 | 3-5 | 09:38:13 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.5600 |  |
| Jogador 6 | 3-6 | 09:38:36 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 6 | 3-6 | 09:38:37 | COMPROU: Gnar (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_GnarSmall | -0.0600 |  |
| Jogador 6 | 3-6 | 09:38:38 | VENDEU: Gnar (i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Rakan | 0.0700 |  |
| Jogador 6 | 3-6 | 09:38:39 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Rakan | -0.2500 |  |
| Jogador 6 | 3-6 | 09:38:40 | MOVE Board -> Board: Cascalho (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-6 | 09:38:40 | MOVE Board -> Board: Xayah (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 3-6 | 09:38:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-7 | 09:38:56 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Feérico | DA_18_Rakan | 0.2500 |  |
| Jogador 6 | 3-7 | 09:38:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Feérico | DA_18_Rakan | 0.1900 |  |
| Jogador 6 | 3-7 | 09:38:59 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 3-7 | 09:39:00 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_Rakan | 0.5400 |  |
| Jogador 6 | 3-7 | 09:39:00 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Rakan | 0.0900 |  |
| Jogador 6 | 3-7 | 09:39:01 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 4-1 | 09:39:16 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Feérico | DA_18_Rakan | 0.0500 |  |
| Jogador 6 | 4-1 | 09:39:17 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Rakan | 0.1700 |  |
| Jogador 6 | 4-1 | 09:39:18 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-2 | 09:39:49 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Feérico | DA_18_Rakan | -0.0900 |  |
| Jogador 6 | 4-2 | 09:39:50 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Feérico | DA_18_Rakan | 0.0500 |  |
| Jogador 6 | 4-2 | 09:39:51 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Feérico | DA_18_Rakan | -0.0800 |  |
| Jogador 6 | 4-2 | 09:39:52 | REROLL | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Feérico | DA_18_Rakan | -0.1300 |  |
| Jogador 6 | 4-2 | 09:39:53 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-2 | 09:39:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Feérico | DA_18_Rakan | 0.3200 |  |
| Jogador 6 | 4-2 | 09:39:55 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Feérico | DA_18_Rakan | 0.0300 |  |
| Jogador 6 | 4-3 | 09:40:12 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 3 | Feérico | DA_18_Rakan | 0.0500 |  |
| Jogador 6 | 4-4 | 09:40:42 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-4 | 09:40:43 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Feérico | DA_18_Rakan | 0.3400 |  |
| Jogador 6 | 4-4 | 09:40:44 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-4 | 09:40:45 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Rakan | 0.9200 |  |
| Jogador 6 | 4-4 | 09:40:46 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Rakan | 0.1700 |  |
| Jogador 6 | 4-4 | 09:40:47 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-4 | 09:40:48 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Rakan | 0.4000 |  |
| Jogador 6 | 4-5 | 09:41:05 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Rakan | 0.8900 |  |
| Jogador 6 | 4-6 | 09:41:40 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Feérico | DA_18_Diana | 0.9600 |  |
| Jogador 6 | 4-6 | 09:41:41 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Diana | 0.9400 |  |
| Jogador 6 | 4-6 | 09:41:42 | MOVE Bench -> Board: Diana (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Diana | 0.3500 |  |
| Jogador 6 | 4-6 | 09:41:43 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Diana | 0.1700 |  |
| Jogador 6 | 4-6 | 09:41:44 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 5 | Feérico | DA_18_Diana | 0.3500 |  |
| Jogador 6 | 4-6 | 09:41:45 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 56 | 5 | Feérico | DA_18_Diana | -0.0900 |  |
| Jogador 6 | 4-7 | 09:42:04 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Diana | 0.1500 |  |
| Jogador 6 | 4-7 | 09:42:05 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Diana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Diana | 0.1300 |  |
| Jogador 6 | 5-1 | 09:42:38 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Feérico | DA_18_Diana | 1.0500 |  |
| Jogador 6 | 5-1 | 09:42:39 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Feérico | DA_18_Diana | 1.0400 |  |
| Jogador 6 | 5-1 | 09:42:40 | MOVE Bench -> Board: Mamãe Bicuda (i:12.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Feérico | DA_18_Diana | 0.0800 |  |
| Jogador 6 | 5-1 | 09:42:41 | MOVE Bench -> Board: Yorick (i:2.0) <-> Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Feérico | DA_18_Diana | -0.8500 |  |
| Jogador 6 | 5-1 | 09:42:42 | MOVE Bench -> Board: Diana (i:12.0) <-> Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Feérico | DA_18_Diana | -0.2400 |  |
| Jogador 6 | 5-1 | 09:42:43 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Feérico | DA_18_Diana | -0.6300 |  |
| Jogador 6 | 5-1 | 09:42:44 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Feérico | DA_18_Diana | 0.3400 |  |
| Jogador 6 | 5-2 | 09:43:02 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Feérico | DA_18_Diana | 0.1300 |  |
| Jogador 7 | ? | 09:34:30 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 09:34:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 09:34:37 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 09:34:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 09:34:38 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 09:34:40 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 09:34:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 09:34:41 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 09:34:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 09:34:45 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 09:34:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 09:34:46 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 09:34:47 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 09:34:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 09:34:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 09:34:53 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 09:34:54 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-3 | 09:34:54 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 09:34:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 09:34:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 09:35:01 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 09:35:03 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 09:35:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 09:35:11 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 09:35:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 09:35:12 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 09:35:13 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 09:35:13 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 09:35:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 09:35:14 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-1 | 09:35:15 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-1 | 09:35:15 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Varus (i:2.0) (tabuleiro slot 9) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1500 |  |
| Jogador 7 | 2-2 | 09:35:24 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 09:35:25 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6500 |  |
| Jogador 7 | 2-2 | 09:35:25 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-2 | 09:35:26 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 09:35:27 | VENDEU: Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | -0.6200 |  |
| Jogador 7 | 2-2 | 09:35:27 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 09:35:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.0200 |  |
| Jogador 7 | 2-2 | 09:35:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-3 | 09:35:37 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 09:35:38 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.2600 |  |
| Jogador 7 | 2-3 | 09:35:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 09:35:53 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 2-4 | 09:35:54 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.3100 |  |
| Jogador 7 | 2-4 | 09:35:55 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 09:35:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-4 | 09:35:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 09:36:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 2-5 | 09:36:12 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 2-5 | 09:36:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 09:36:13 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 09:36:14 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.4800 |  |
| Jogador 7 | 2-5 | 09:36:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 09:36:16 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 09:36:17 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-6 | 09:36:26 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 2-6 | 09:36:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 2-6 | 09:36:27 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.4600 |  |
| Jogador 7 | 2-6 | 09:36:28 | MOVE Board -> Board: Azuporã (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-6 | 09:36:29 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-6 | 09:36:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 09:36:41 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 2-7 | 09:36:41 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 2-7 | 09:36:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 09:36:43 | MOVE Board -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 09:36:44 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 09:36:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-1 | 09:36:58 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 3-2 | 09:37:17 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.8400 |  |
| Jogador 7 | 3-2 | 09:37:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 3-2 | 09:37:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 3-2 | 09:37:20 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.5600 |  |
| Jogador 7 | 3-2 | 09:37:21 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-2 | 09:37:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-3 | 09:37:33 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.8400 |  |
| Jogador 7 | 3-3 | 09:37:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 7 | 3-4 | 09:37:56 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 7 | 3-4 | 09:37:56 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 7 | 3-4 | 09:37:57 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 3-4 | 09:37:58 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Aronguejo (i:4.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 7 | 3-4 | 09:37:59 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Aronguejo (i:4.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 7 | 3-4 | 09:38:00 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 7 | 3-4 | 09:38:01 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.5100 |  |
| Jogador 7 | 3-5 | 09:38:13 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.7700 |  |
| Jogador 7 | 3-6 | 09:38:36 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.7100 |  |
| Jogador 7 | 3-6 | 09:38:37 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 7 | 3-6 | 09:38:38 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 3-6 | 09:38:39 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 0 | Colosso | DA_Sentinel18 | -0.5400 |  |
| Jogador 7 | 3-6 | 09:38:40 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Aronguejo (i:4.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 0 | Colosso | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 3-6 | 09:38:40 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-6 | 09:38:41 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 0 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 3-6 | 09:38:42 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 0 | Colosso | DA_Sentinel18 | -0.1500 |  |
| Jogador 7 | 3-7 | 09:38:56 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_Sentinel18 | 0.3100 |  |
| Jogador 7 | 3-7 | 09:38:57 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_Sentinel18 | 0.1400 |  |
| Jogador 7 | 3-7 | 09:38:59 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 3-7 | 09:39:00 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 3-7 | 09:39:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-7 | 09:39:01 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Colosso | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 4-1 | 09:39:16 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Sentinel18 | 0.8400 |  |
| Jogador 7 | 4-1 | 09:39:17 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_Sentinel18 | 0.9000 |  |
| Jogador 7 | 4-1 | 09:39:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Colosso | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 4-2 | 09:39:49 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Colosso | DA_Sentinel18 | 0.8000 |  |
| Jogador 7 | 4-2 | 09:39:50 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Colosso | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 4-2 | 09:39:51 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 4-2 | 09:39:52 | MOVE Board -> Board: Hecarim (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-2 | 09:39:53 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 09:39:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 4-3 | 09:40:12 | VENDEU: Sejuani (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 2 | Colosso | DA_Sentinel18 | -0.5000 |  |
| Jogador 7 | 4-4 | 09:40:42 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_Sentinel18 | 0.6300 |  |
| Jogador 7 | 4-4 | 09:40:43 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-4 | 09:40:44 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-4 | 09:40:45 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_Sentinel18 | 0.8500 |  |
| Jogador 7 | 4-4 | 09:40:46 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 4-4 | 09:40:47 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 4-4 | 09:40:48 | MOVE Board -> Board: Hecarim (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-5 | 09:41:05 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Colosso | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 4-6 | 09:41:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Colosso | DA_Sentinel18 | 0.9600 |  |
| Jogador 7 | 4-6 | 09:41:41 | MOVE Bench -> Board: Soraka (i:8.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Colosso | DA_Sentinel18 | 0.2300 |  |
| Jogador 7 | 4-6 | 09:41:42 | MOVE Bench -> Board: LeBlanc (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Colosso | DA_Sentinel18 | 0.1800 |  |
| Jogador 7 | 4-6 | 09:41:43 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Colosso | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 4-6 | 09:41:44 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Colosso | DA_Sentinel18 | 0.5400 |  |
| Jogador 7 | 4-6 | 09:41:45 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 4-7 | 09:42:04 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 80 | 5 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 4-7 | 09:42:05 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 80 | 5 | Colosso | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 5-1 | 09:42:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Colosso | DA_Sentinel18 | 0.5500 |  |
| Jogador 7 | 5-1 | 09:42:39 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Colosso | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 5-1 | 09:42:40 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-1 | 09:42:41 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Colosso | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 5-1 | 09:42:42 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-1 | 09:42:43 | VENDEU: Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Colosso | DA_Sentinel18 | -0.6000 |  |
| Jogador 7 | 5-1 | 09:42:44 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 97 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 5-2 | 09:43:02 | VENDEU: Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_Sentinel18 | -0.6000 |  |
| Jogador 7 | 5-3 | 09:43:41 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Colosso | DA_Sentinel18 | 0.3300 |  |
| Jogador 7 | 5-3 | 09:43:42 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> LeBlanc (i:8.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Colosso | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 5-3 | 09:43:42 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Xayah (i:2.0) (tabuleiro slot 23) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Colosso | DA_Sentinel18 | 0.1100 |  |
| Jogador 7 | 5-3 | 09:43:43 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Xayah (i:2.0) (tabuleiro slot 23) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 5-3 | 09:43:44 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-3 | 09:43:45 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Colosso | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 5-3 | 09:43:46 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-4 | 09:44:04 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Colosso | DA_Sentinel18 | 0.2700 |  |
| Jogador 7 | 5-5 | 09:44:40 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-5 | 09:44:41 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 142 | 5 | Colosso | DA_Sentinel18 | 0.2700 |  |
| Jogador 7 | 5-5 | 09:44:42 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-5 | 09:44:42 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 141 | 5 | Colosso | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 5-5 | 09:44:44 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-5 | 09:44:45 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 141 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 5-6 | 09:45:06 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-6 | 09:45:07 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 151 | 5 | Colosso | DA_Sentinel18 | 0.8700 |  |
| Jogador 7 | 5-7 | 09:45:43 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Xayah (i:2.0) (tabuleiro slot 23) | FAST8 | FAST8: composição planejada exige nível 8 | 161 | 5 | Colosso | DA_Sentinel18 | 0.1300 |  |
| Jogador 7 | 5-7 | 09:45:44 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 164 | 5 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 5-7 | 09:45:45 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 162 | 5 | Colosso | DA_Sentinel18 | 0.9300 |  |
| Jogador 7 | 5-7 | 09:45:47 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 158 | 5 | Colosso | DA_Sentinel18 | 0.1700 |  |
| Jogador 7 | 5-7 | 09:45:48 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 6-1 | 09:46:11 | VENDEU: Grompe (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 170 | 5 | Colosso | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-1 | 09:46:12 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Colosso | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 6-1 | 09:46:13 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 171 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 6-2 | 09:46:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Colosso | DA_CrimsonRaptor18 | 1.0100 |  |
| Jogador 7 | 6-2 | 09:46:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 175 | 5 | Colosso | DA_CrimsonRaptor18 | 1.0100 |  |
| Jogador 7 | 6-2 | 09:46:54 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 175 | 5 | Colosso | DA_CrimsonRaptor18 | 0.4200 |  |
| Jogador 7 | 6-2 | 09:46:55 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Colosso | DA_CrimsonRaptor18 | -0.2400 |  |
| Jogador 7 | 6-2 | 09:46:56 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 170 | 5 | Colosso | DA_CrimsonRaptor18 | -0.2000 |  |
| Jogador 7 | 6-2 | 09:46:57 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 169 | 5 | Colosso | DA_CrimsonRaptor18 | -0.2100 |  |
| Jogador 7 | 6-3 | 09:47:23 | VENDEU: Mamãe Bicuda (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 187 | 5 | Sabugueiro | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 7 | 6-3 | 09:47:24 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 184 | 5 | Sabugueiro | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 7 | 6-4 | 09:48:05 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Soraka (i:8.0) (tabuleiro slot 11) | FAST8 | FAST8: composição planejada exige nível 8 | 194 | 5 | Sabugueiro | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 6-4 | 09:48:06 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Soraka (i:8.0) (tabuleiro slot 11) | FAST8 | FAST8: composição planejada exige nível 8 | 194 | 5 | Sabugueiro | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 6-4 | 09:48:07 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 195 | 5 | Sabugueiro | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 6-4 | 09:48:08 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 194 | 5 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 6-4 | 09:48:09 | VENDEU: Fiddlesticks (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 202 | 5 | Sabugueiro | DA_Sentinel18 | -0.6000 |  |
| Jogador 7 | 6-4 | 09:48:10 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 199 | 5 | Sabugueiro | DA_Sentinel18 | -0.2300 |  |
| Jogador 7 | 6-4 | 09:48:11 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 200 | 5 | Sabugueiro | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 6-5 | 09:48:33 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 208 | 5 | Sabugueiro | DA_Sentinel18 | 0.3200 |  |
| Jogador 7 | 6-6 | 09:49:14 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 222 | 5 | Sabugueiro | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 6-6 | 09:49:15 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 219 | 5 | Sabugueiro | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 6-6 | 09:49:16 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 222 | 5 | Sabugueiro | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 6-6 | 09:49:17 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 219 | 5 | Sabugueiro | DA_Sentinel18 | -0.1700 |  |
| Jogador 7 | 6-6 | 09:49:17 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 222 | 5 | Sabugueiro | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 6-6 | 09:49:18 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 220 | 5 | Sabugueiro | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 6-6 | 09:49:19 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 222 | 5 | Sabugueiro | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-7 | 09:49:41 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 230 | 5 | Sabugueiro | DA_Sentinel18 | 0.9400 |  |
| Jogador 8 | ? | 09:34:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 09:34:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 09:34:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 09:34:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 09:34:38 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 09:34:38 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 09:34:40 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 09:34:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 09:34:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-2 | 09:34:45 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 09:34:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 09:34:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 09:34:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 09:34:54 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 09:34:54 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 09:34:55 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 09:34:55 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 09:34:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 09:35:01 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 09:35:02 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 09:35:03 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 09:35:04 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 09:35:04 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 09:35:05 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 1-4 | 09:35:05 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.3200 |  |
| Jogador 8 | 2-1 | 09:35:11 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 09:35:12 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 2-1 | 09:35:12 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1900 |  |
| Jogador 8 | 2-1 | 09:35:13 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 2-1 | 09:35:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-1 | 09:35:14 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-1 | 09:35:14 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-1 | 09:35:15 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.1700 |  |
| Jogador 8 | 2-1 | 09:35:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-2 | 09:35:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.9900 |  |
| Jogador 8 | 2-2 | 09:35:25 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.3600 |  |
| Jogador 8 | 2-2 | 09:35:25 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 2-2 | 09:35:26 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-2 | 09:35:27 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 2-2 | 09:35:27 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 2-2 | 09:35:28 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.1500 |  |
| Jogador 8 | 2-2 | 09:35:28 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Karma18 | -0.3300 |  |
| Jogador 8 | 2-2 | 09:35:29 | MOVE Bench -> Board: Veigar (i:2.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 2-3 | 09:35:37 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-3 | 09:35:38 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-3 | 09:35:38 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-3 | 09:35:39 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_Karma18 | 0.3500 |  |
| Jogador 8 | 2-3 | 09:35:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | — | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-3 | 09:35:40 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | — | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 2-3 | 09:35:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | — | DA_Karma18 | -0.1200 |  |
| Jogador 8 | 2-3 | 09:35:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-3 | 09:35:42 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | — | DA_18_MasterYi_AD | -0.6300 |  |
| Jogador 8 | 2-4 | 09:35:53 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 1.0300 |  |
| Jogador 8 | 2-4 | 09:35:54 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 8 | 2-4 | 09:35:55 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.3200 |  |
| Jogador 8 | 2-4 | 09:35:55 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 8 | 2-4 | 09:35:56 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.4300 |  |
| Jogador 8 | 2-4 | 09:35:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 8 | 2-4 | 09:35:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 8 | 2-4 | 09:35:58 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.3800 |  |
| Jogador 8 | 2-4 | 09:35:58 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 8 | 2-5 | 09:36:11 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.2500 |  |
| Jogador 8 | 2-5 | 09:36:12 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.4800 |  |
| Jogador 8 | 2-5 | 09:36:13 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 8 | 2-5 | 09:36:13 | MOVE Board -> Board: Diana (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.2000 |  |
| Jogador 8 | 2-5 | 09:36:14 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 8 | 2-5 | 09:36:15 | MOVE Bench -> Board: Soraka (i:8.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.2600 |  |
| Jogador 8 | 2-5 | 09:36:16 | MOVE Board -> Board: Rakan (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 2-5 | 09:36:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 2-6 | 09:36:26 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.3500 |  |
| Jogador 8 | 2-6 | 09:36:26 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.2900 |  |
| Jogador 8 | 2-6 | 09:36:27 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.1800 |  |
| Jogador 8 | 2-6 | 09:36:28 | MOVE Board -> Board: Diana (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 2-6 | 09:36:29 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 2-6 | 09:36:29 | MOVE Board -> Board: Soraka (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 2-6 | 09:36:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 2-7 | 09:36:41 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 8 | 2-7 | 09:36:41 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_SparringGloves -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.1700 |  |
| Jogador 8 | 2-7 | 09:36:42 | MOVE Board -> Board: Diana (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 8 | 2-7 | 09:36:43 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 8 | 2-7 | 09:36:44 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 8 | 2-7 | 09:36:44 | MOVE Board -> Board: Teemo (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0200 |  |
| Jogador 8 | 2-7 | 09:36:45 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 8 | 2-7 | 09:36:46 | MOVE Board -> Board: Veigar (i:2.0) <-> Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 3-1 | 09:36:58 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 8 | 3-2 | 09:37:17 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_18_MasterYi_AD | 0.2800 |  |
| Jogador 8 | 3-2 | 09:37:17 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 8 | 3-2 | 09:37:18 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_MasterYi_AD | 0.2500 |  |
| Jogador 8 | 3-2 | 09:37:20 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 3-2 | 09:37:21 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_MasterYi_AD | 0.2200 |  |
| Jogador 8 | 3-2 | 09:37:22 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 8 | 3-3 | 09:37:33 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Enfeitiçador | DA_18_MasterYi_AD | 0.8500 |  |
| Jogador 8 | 3-3 | 09:37:34 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Enfeitiçador | DA_18_MasterYi_AD | 0.1400 |  |
| Jogador 8 | 3-4 | 09:37:56 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.8200 |  |
| Jogador 8 | 3-4 | 09:37:56 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.5800 |  |
| Jogador 8 | 3-4 | 09:37:57 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_18_LeBlanc | 0.8700 |  |
| Jogador 8 | 3-4 | 09:37:58 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_LeBlanc | 0.2900 |  |
| Jogador 8 | 3-4 | 09:37:59 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_18_LeBlanc | -0.0100 |  |
| Jogador 8 | 3-4 | 09:38:00 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_Soraka | -0.5000 |  |
| Jogador 8 | 3-4 | 09:38:01 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_18_Soraka | -0.0700 |  |
| Jogador 8 | 3-5 | 09:38:13 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_18_Soraka | 0.8200 |  |
| Jogador 8 | 3-6 | 09:38:36 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Soraka | 0.9000 |  |
| Jogador 8 | 3-6 | 09:38:37 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Soraka | 0.2000 |  |
| Jogador 8 | 3-6 | 09:38:38 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Soraka | -0.5900 |  |
| Jogador 8 | 3-6 | 09:38:39 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Soraka | 0.0400 |  |
| Jogador 8 | 3-6 | 09:38:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 4 | Enfeitiçador | DA_18_Soraka | -0.0700 |  |
| Jogador 8 | 3-6 | 09:38:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 4 | Enfeitiçador | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-6 | 09:38:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 4 | Enfeitiçador | DA_18_Soraka | -0.0900 |  |
| Jogador 8 | 3-6 | 09:38:42 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 4 | Enfeitiçador | DA_18_Soraka | 0.5500 |  |
| Jogador 8 | 3-7 | 09:38:56 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Soraka | 0.2900 |  |
| Jogador 8 | 3-7 | 09:38:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Soraka | 0.1300 |  |
| Jogador 8 | 3-7 | 09:38:59 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Soraka | 0.0800 |  |
| Jogador 8 | 3-7 | 09:39:00 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Enfeitiçador | DA_18_Soraka | 0.0800 |  |
| Jogador 8 | 3-7 | 09:39:00 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Enfeitiçador | DA_18_Soraka | 0.1000 |  |
| Jogador 8 | 3-7 | 09:39:01 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Enfeitiçador | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 4-1 | 09:39:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Soraka | 0.8600 |  |
| Jogador 8 | 4-1 | 09:39:17 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Enfeitiçador | DA_18_Soraka | -0.0300 |  |
| Jogador 8 | 4-1 | 09:39:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Soraka | 0.1000 |  |
| Jogador 8 | 4-2 | 09:39:49 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Soraka | -0.0300 |  |
| Jogador 8 | 4-2 | 09:39:50 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Enfeitiçador | DA_18_Soraka | 0.8500 |  |
| Jogador 8 | 4-2 | 09:39:51 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Enfeitiçador | DA_18_Soraka | -0.0300 |  |
| Jogador 8 | 4-2 | 09:39:52 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Enfeitiçador | DA_18_Soraka | 0.7800 |  |
| Jogador 8 | 4-2 | 09:39:53 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Enfeitiçador | DA_18_Soraka | -0.0700 |  |
| Jogador 8 | 4-2 | 09:39:54 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Enfeitiçador | DA_18_Soraka | 0.3600 |  |
| Jogador 8 | 4-2 | 09:39:55 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Enfeitiçador | DA_18_Soraka | -0.5400 |  |
| Jogador 8 | 4-3 | 09:40:12 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 89 | 5 | Enfeitiçador | DA_18_Soraka | 0.8800 |  |
| Jogador 8 | 4-4 | 09:40:42 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 98 | 5 | Enfeitiçador | DA_18_Soraka | 0.9600 |  |
| Jogador 8 | 4-4 | 09:40:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Enfeitiçador | DA_18_Soraka | 0.9600 |  |
| Jogador 8 | 4-4 | 09:40:44 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Enfeitiçador | DA_18_Soraka | 0.3100 |  |
| Jogador 8 | 4-4 | 09:40:45 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 94 | 5 | Enfeitiçador | DA_18_Soraka | 0.1300 |  |
| Jogador 8 | 4-4 | 09:40:46 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 94 | 5 | Enfeitiçador | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 4-4 | 09:40:47 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Enfeitiçador | DA_18_Soraka | 0.4000 |  |
| Jogador 8 | 4-4 | 09:40:48 | MOVE Board -> Board: Tristana (i:6.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Enfeitiçador | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 4-5 | 09:41:05 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 103 | 5 | Enfeitiçador | DA_18_Soraka | 0.8900 |  |
| Jogador 8 | 4-6 | 09:41:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Enfeitiçador | DA_18_Soraka | 0.6200 |  |
| Jogador 8 | 4-6 | 09:41:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.8400 |  |
| Jogador 8 | 4-6 | 09:41:42 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.5000 |  |
| Jogador 8 | 4-6 | 09:41:43 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.0200 |  |
| Jogador 8 | 4-6 | 09:41:44 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 8 | 4-6 | 09:41:45 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.2100 |  |
| Jogador 8 | 4-7 | 09:42:04 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Teemo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.1300 |  |
| Jogador 8 | 4-7 | 09:42:05 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.1300 |  |
| Jogador 8 | 5-1 | 09:42:38 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.6800 |  |
| Jogador 8 | 5-1 | 09:42:39 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.8100 |  |
| Jogador 8 | 5-1 | 09:42:40 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Master Yi (i:12.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 8 | 5-1 | 09:42:41 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Master Yi (i:12.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 8 | 5-1 | 09:42:42 | VENDEU: LeBlanc (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.6800 |  |
| Jogador 8 | 5-1 | 09:42:43 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.5800 |  |
| Jogador 8 | 5-1 | 09:42:44 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 5-2 | 09:43:02 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 8 | 5-3 | 09:43:41 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 1.0500 |  |
| Jogador 8 | 5-3 | 09:43:42 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.4700 |  |
| Jogador 8 | 5-3 | 09:43:42 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 8 | 5-3 | 09:43:43 | VENDEU: Cassiopeia (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.1500 |  |
| Jogador 8 | 5-3 | 09:43:44 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.3800 |  |
| Jogador 8 | 5-3 | 09:43:45 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 8 | 5-3 | 09:43:46 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.4100 |  |
| Jogador 8 | 5-4 | 09:44:04 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.9800 |  |
| Jogador 8 | 5-5 | 09:44:40 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.9000 |  |
| Jogador 8 | 5-5 | 09:44:41 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 169 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.5200 |  |
| Jogador 8 | 5-5 | 09:44:42 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 167 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.4200 |  |
| Jogador 8 | 5-5 | 09:44:42 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 169 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.6800 |  |
| Jogador 8 | 5-5 | 09:44:44 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 167 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.4200 |  |
| Jogador 8 | 5-5 | 09:44:45 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 169 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.6800 |  |
| Jogador 8 | 5-6 | 09:45:06 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.8100 |  |
| Jogador 8 | 5-6 | 09:45:07 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 181 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.5400 |  |
| Jogador 8 | 5-7 | 09:45:43 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 191 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.4600 |  |
| Jogador 8 | 5-7 | 09:45:44 | EQUIP_FROM_INVENTORY: DA_18_EmblemHunter -> Veigar (i:2.0) (tabuleiro slot 23) | ALL_IN | HP crítico: gastar para sobreviver | 191 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 5-7 | 09:45:45 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 194 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.6000 |  |
| Jogador 8 | 5-7 | 09:45:47 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 192 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 8 | 5-7 | 09:45:48 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 194 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 8 | 6-1 | 09:46:11 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 202 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.4500 |  |
| Jogador 8 | 6-1 | 09:46:12 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 204 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.7200 |  |
| Jogador 8 | 6-1 | 09:46:13 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 201 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.4100 |  |
| Jogador 8 | 6-2 | 09:46:52 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.1000 |  |
| Jogador 8 | 6-2 | 09:46:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 212 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 1.0300 |  |
| Jogador 8 | 6-2 | 09:46:54 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.6700 |  |
| Jogador 8 | 6-2 | 09:46:55 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 212 | 5 | Enfeitiçador | DA_18_MasterYi_AD | 0.4300 |  |
| Jogador 8 | 6-2 | 09:46:56 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.5500 |  |
| Jogador 8 | 6-2 | 09:46:57 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Enfeitiçador | DA_18_MasterYi_AD | -0.1800 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 39 | 39 | 195 | 39 | 19 | 187 | 10 | 46 |
| Jogador 2 | 23 | 23 | 115 | 23 | 14 | 132 | 4 | 24 |
| Jogador 3 | 27 | 27 | 135 | 27 | 17 | 134 | 5 | 26 |
| Jogador 4 | 23 | 25 | 125 | 23 | 14 | 122 | 6 | 3 |
| Jogador 5 | 30 | 33 | 165 | 30 | 17 | 144 | 10 | 7 |
| Jogador 6 | 28 | 29 | 145 | 28 | 16 | 138 | 13 | 38 |
| Jogador 7 | 39 | 39 | 195 | 39 | 21 | 183 | 9 | 27 |
| Jogador 8 | 35 | 36 | 180 | 35 | 17 | 181 | 7 | 36 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 187 | 187 | 187 | 0 | 175 | 0 | 187 | 187 | 187 | 72/57 |
| Jogador 2 | 132 | 132 | 132 | 0 | 124 | 0 | 132 | 132 | 132 | 59/45 |
| Jogador 3 | 134 | 134 | 134 | 0 | 127 | 0 | 134 | 134 | 134 | 52/39 |
| Jogador 4 | 122 | 122 | 122 | 0 | 114 | 0 | 122 | 122 | 122 | 47/33 |
| Jogador 5 | 144 | 144 | 144 | 0 | 136 | 0 | 144 | 144 | 144 | 58/44 |
| Jogador 6 | 138 | 138 | 138 | 0 | 131 | 0 | 138 | 138 | 138 | 53/41 |
| Jogador 7 | 183 | 183 | 183 | 0 | 164 | 0 | 183 | 183 | 183 | 71/56 |
| Jogador 8 | 181 | 181 | 181 | 0 | 171 | 0 | 181 | 181 | 181 | 79/64 |

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
| Jogador 1 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.34722596406936646 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2512100040912628 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387595891952515 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.031553864479065 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 46 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 47 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3354947865009308 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 53 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13024558126926422 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 54 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05997481942176819 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2757837474346161 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 58 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17242395877838135 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-2 | 59 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3278871178627014 | 0.0 | 0.0 | +e76c0caf-1c3d-493f-9a21-659dd8587fc2 / -— |
| Jogador 1 | 2-2 | 60 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35286957025527954 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 63 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 64 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33430856466293335 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 65 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1780567616224289 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 66 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15131524205207825 | 0.0 | 0.0 | +— / -e76c0caf-1c3d-493f-9a21-659dd8587fc2 |
| Jogador 1 | 2-3 | 67 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 68 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 72 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.11699378490448 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 73 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3641240894794464 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4286927282810211 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 75 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19477969408035278 | 0.0 | 0.0 | +7d8f4f6b-4eba-4c31-9834-bd81a3765520 / -— |
| Jogador 1 | 2-4 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002366695087403059 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09324062615633011 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01360281277447939 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 79 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014595994725823402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 80 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015672916546463966 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 82 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9662604928016663 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 83 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.054117608815431595 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 84 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-5 | 85 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 86 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00031991899595595896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 87 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899999871850014 | 0.0 | 0.0 | +— / -7d8f4f6b-4eba-4c31-9834-bd81a3765520 |
| Jogador 1 | 2-5 | 88 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 89 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5041336417198181 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014980697073042393 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 92 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.117992639541626 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 93 | BUY | STABILIZE | 100.0 | 6 | 6 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28147950768470764 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 94 | BUY | STABILIZE | 100.0 | 6 | 3 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28170570731163025 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.400149405002594 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01498666126281023 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 98 | PASS | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 101 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0476287603378296 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 102 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9423136115074158 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 103 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 5 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3429839611053467 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 104 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05123848840594292 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 2-7 | 105 | BUY | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018735121935606003 | 0.0 | 0.0 | +acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce / -— |
| Jogador 1 | 2-7 | 106 | BUY | STABILIZE | 100.0 | 6 | 2 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27295875549316406 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -— |
| Jogador 1 | 2-7 | 107 | SELL | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 2-7 | 108 | PASS | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40026146173477173 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 111 | BUY | STABILIZE | 100.0 | 6 | 10 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11613920331001282 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 112 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.018427761271595955 | 0.0 | 0.0 | +dca8bf82-80ac-4054-9a77-3891a7de23e2 / -— |
| Jogador 1 | 3-1 | 113 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16741271317005157 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 114 | BUY | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.054386284202337265 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 115 | PASS | STABILIZE | 100.0 | 6 | 3 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 120 | SELL | STABILIZE | 100.0 | 6 | 12 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024117838591337204 | 0.0 | 0.0 | +— / -acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce |
| Jogador 1 | 3-3 | 122 | BUY | STABILIZE | 100.0 | 6 | 23 | 2 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4771985411643982 | 0.0 | 0.0 | +66b5ed5e-7fdf-4135-a334-e693715e302d / -— |
| Jogador 1 | 3-3 | 123 | BUY_XP | STABILIZE | 100.0 | 6 | 21 | 2 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 124 | BUY_XP | STABILIZE | 100.0 | 6 | 17 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 125 | BUY_XP | STABILIZE | 100.0 | 6 | 13 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 126 | BUY_XP | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 127 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 129 | SELL | STABILIZE | 90.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 1 | 3-4 | 130 | BUY | STABILIZE | 90.0 | 6 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09852606058120728 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 1 | 3-5 | 132 | SELL | STABILIZE | 90.0 | 7 | 12 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02537880651652813 | 0.0 | 0.0 | +— / -7a60e1b2-fc20-4070-b163-2f9fb6f93264 |
| Jogador 1 | 3-5 | 133 | BUY | STABILIZE | 90.0 | 7 | 13 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8357812166213989 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 134 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 11 | 1 | 16.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7226929664611816 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 135 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 11 | 1 | 16.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33483073115348816 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 136 | BUY | STABILIZE | 90.0 | 7 | 11 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01295043807476759 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 137 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 8 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15508869290351868 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 138 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 8 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4055947959423065 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 140 | BUY | STABILIZE | 90.0 | 7 | 14 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28564292192459106 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-7 | 142 | BUY | STABILIZE | 81.0 | 7 | 18 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8034525513648987 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 143 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 15 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 144 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 15 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 145 | PASS | STABILIZE | 81.0 | 7 | 15 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 151 | CRAFT_AND_EQUIP | STABILIZE | 81.0 | 7 | 21 | 2 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1538250744342804 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 81.0 | 7 | 21 | 2 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07078087329864502 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 153 | SELL | STABILIZE | 81.0 | 7 | 21 | 2 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 |
| Jogador 1 | 4-1 | 154 | BUY | STABILIZE | 81.0 | 7 | 26 | 2 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7358748912811279 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 155 | EQUIP_FROM_INVENTORY | STABILIZE | 81.0 | 7 | 23 | 2 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12519675493240356 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 156 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 23 | 2 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037000760436058044 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 158 | SELL | STABILIZE | 81.0 | 7 | 31 | 3 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 1 | 4-2 | 159 | BUY | STABILIZE | 81.0 | 7 | 34 | 3 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3268892467021942 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 1 | 4-2 | 160 | SELL | STABILIZE | 81.0 | 7 | 33 | 3 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010262285359203815 | 0.0 | 0.0 | +— / -7c218f01-e884-46da-8a1a-2d2db27a5ff1 |
| Jogador 1 | 4-3 | 162 | BUY | STABILIZE | 81.0 | 7 | 46 | 4 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1359744817018509 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -— |
| Jogador 1 | 4-3 | 163 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 45 | 4 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0370020791888237 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 164 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 45 | 4 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000122599303722 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 165 | SELL | STABILIZE | 81.0 | 7 | 45 | 4 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028562556952238083 | 0.0 | 0.0 | +— / -ea460790-b046-451d-9174-8b613e476241 |
| Jogador 1 | 4-3 | 166 | BUY | STABILIZE | 81.0 | 7 | 46 | 4 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019831692799925804 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 1 | 4-3 | 167 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 43 | 4 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.507465978851542e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 168 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 43 | 4 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015517809428274632 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 170 | SELL | STABILIZE | 81.0 | 7 | 54 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00032192820799537003 | 0.0 | 0.0 | +— / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 |
| Jogador 1 | 4-5 | 172 | BUY | STABILIZE | 81.0 | 7 | 68 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23110240697860718 | 0.0 | 0.0 | +1022f12a-84e9-4eeb-81dc-706092de3728 / -— |
| Jogador 1 | 4-5 | 173 | SELL | STABILIZE | 81.0 | 7 | 65 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -1022f12a-84e9-4eeb-81dc-706092de3728 |
| Jogador 1 | 4-5 | 174 | BUY | STABILIZE | 81.0 | 7 | 68 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0802111104130745 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 1 | 4-5 | 175 | SELL | STABILIZE | 81.0 | 7 | 64 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 |
| Jogador 1 | 4-5 | 176 | BUY | STABILIZE | 81.0 | 7 | 68 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08021186292171478 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 1 | 4-5 | 177 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 64 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005176424165256321 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 178 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 64 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997368678450584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 180 | SELL | STABILIZE | 81.0 | 7 | 76 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 1 | 4-7 | 182 | BUY | STABILIZE | 81.0 | 7 | 93 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9636412262916565 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -227dbcdb-af5c-4318-94d1-f01a7847d100,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 4-7 | 183 | BUY | STABILIZE | 81.0 | 7 | 90 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07397344708442688 | 0.0 | 0.0 | +b9b38183-663e-43a4-9f9d-02f1bd4d2d24 / -— |
| Jogador 1 | 4-7 | 184 | BUY | STABILIZE | 81.0 | 7 | 88 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17277567088603973 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 1 | 4-7 | 185 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 85 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.786463258213189e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 186 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 85 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000997111201286 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 187 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 85 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999955892562866 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 189 | CRAFT_AND_EQUIP | STABILIZE | 81.0 | 7 | 97 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1334250420331955 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 190 | CRAFT_AND_EQUIP | STABILIZE | 81.0 | 7 | 97 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12747755646705627 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 192 | SELL | STABILIZE | 81.0 | 7 | 111 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -d1bc6c5b-74a5-46db-b00f-e91265546f5d |
| Jogador 1 | 5-2 | 193 | BUY | STABILIZE | 81.0 | 7 | 119 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7650455832481384 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 1 | 5-2 | 194 | SELL | STABILIZE | 81.0 | 7 | 118 | 5 | 30.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -b9b38183-663e-43a4-9f9d-02f1bd4d2d24 |
| Jogador 1 | 5-2 | 195 | BUY | STABILIZE | 81.0 | 7 | 120 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1876557171344757 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 1 | 5-2 | 196 | SELL | STABILIZE | 81.0 | 7 | 117 | 5 | 30.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -f8a93323-530e-4f9c-99d7-a5ec83b78992 |
| Jogador 1 | 5-2 | 197 | BUY | STABILIZE | 81.0 | 7 | 120 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2205112874507904 | 0.0 | 0.0 | +e270a6b1-23dd-49a0-8694-ba911eae4c71 / -— |
| Jogador 1 | 5-2 | 198 | SELL | STABILIZE | 81.0 | 7 | 117 | 5 | 30.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -e270a6b1-23dd-49a0-8694-ba911eae4c71 |
| Jogador 1 | 5-3 | 200 | BUY | STABILIZE | 81.0 | 7 | 134 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9124572277069092 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -— |
| Jogador 1 | 5-4 | 202 | SELL | STABILIZE | 81.0 | 7 | 147 | 5 | 30.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47344276309013367 | 0.0 | 0.0 | +— / -66b5ed5e-7fdf-4135-a334-e693715e302d |
| Jogador 1 | 5-4 | 203 | BUY | STABILIZE | 81.0 | 7 | 149 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9126400947570801 | 0.0 | 0.0 | +1512b230-15a6-405f-9b6b-4387a3091648 / -— |
| Jogador 1 | 5-4 | 204 | SELL | STABILIZE | 81.0 | 7 | 147 | 5 | 30.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5075919032096863 | 0.0 | 0.0 | +— / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 |
| Jogador 1 | 5-4 | 205 | BUY | STABILIZE | 81.0 | 7 | 149 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8976821899414062 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 1 | 5-4 | 206 | SELL | STABILIZE | 81.0 | 7 | 147 | 5 | 30.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4584110975265503 | 0.0 | 0.0 | +— / -9af900db-c181-448a-9736-30f08f062a00 |
| Jogador 1 | 5-4 | 207 | BUY | STABILIZE | 81.0 | 7 | 150 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0194885730743408 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -89ef75a2-6ac2-4c6c-b2b8-492aec985a01,cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 5-4 | 208 | MOVE_BENCH | STABILIZE | 81.0 | 7 | 149 | 5 | 28.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5486538410186768 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 210 | BUY | STABILIZE | 81.0 | 7 | 162 | 5 | 32.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13587701320648193 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -— |
| Jogador 1 | 5-6 | 212 | BUY | STABILIZE | 81.0 | 7 | 171 | 5 | 32.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0223535299301147 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -3fc2815d-c456-47c3-bb27-783336b3cdfa,64d87de4-68df-4a72-8b8d-f78039ae4ce5 |
| Jogador 1 | 5-6 | 213 | SELL | STABILIZE | 81.0 | 7 | 169 | 5 | 24.0 | Fera do Rift/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -b2517873-8317-401b-8461-1d86969edbd7 |
| Jogador 1 | 5-6 | 214 | BUY | STABILIZE | 81.0 | 7 | 172 | 5 | 24.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0223572254180908 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -760d5bee-7d64-4f03-abf0-6357c914a1ed,b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 5-6 | 215 | BUY | STABILIZE | 81.0 | 7 | 170 | 5 | 24.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0184640884399414 | 0.0 | 0.0 | +d3fddd9d-ee81-418d-9c58-0baa4ed99f61 / -727765c8-7f02-491e-a6da-12b0dab59f6d,844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 1 | 5-6 | 216 | MOVE_BENCH | STABILIZE | 81.0 | 7 | 167 | 5 | 18.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3381456136703491 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 217 | MOVE_BENCH | STABILIZE | 81.0 | 7 | 167 | 5 | 26.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13309314846992493 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 219 | BUY | FAST8 | 65.0 | 7 | 177 | 5 | 36.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12671861052513123 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 1 | 5-7 | 220 | BUY | FAST8 | 65.0 | 7 | 174 | 5 | 36.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1873011589050293 | 0.0 | 0.0 | +864f332a-0446-4995-b7fb-76d48d293501 / -— |
| Jogador 1 | 6-1 | 222 | BUY | FAST8 | 65.0 | 7 | 181 | 5 | 42.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0059071779251099 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -— |
| Jogador 1 | 6-1 | 223 | BUY | FAST8 | 65.0 | 7 | 178 | 5 | 42.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.36895087361335754 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 1 | 6-1 | 224 | BUY | FAST8 | 65.0 | 7 | 175 | 5 | 42.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8887606263160706 | 0.0 | 0.0 | +9c3b3b78-e99c-4947-b958-cce156ecccb1 / -— |
| Jogador 1 | 6-1 | 225 | EQUIP_FROM_INVENTORY | FAST8 | 65.0 | 7 | 172 | 5 | 42.0 | Fera do Rift/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06617221236228943 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 226 | MOVE_BOARD | FAST8 | 65.0 | 7 | 172 | 5 | 42.0 | Fera do Rift/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002236936241388321 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 228 | SELL | FAST8 | 65.0 | 7 | 183 | 5 | 42.0 | Fera do Rift/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5049759149551392 | 0.0 | 0.0 | +— / -d3fddd9d-ee81-418d-9c58-0baa4ed99f61 |
| Jogador 1 | 6-2 | 229 | BUY | FAST8 | 65.0 | 7 | 191 | 5 | 42.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0137888193130493 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad,68a0405b-6231-471f-98a5-1661d32f4ac4 |
| Jogador 1 | 6-2 | 230 | BUY | FAST8 | 65.0 | 7 | 188 | 5 | 36.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0107123851776123 | 0.0 | 0.0 | +e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 / -22f3c707-2635-41cb-a228-10d5ed1883b3,6fa83356-562b-4a26-a77d-3e989089e70a |
| Jogador 1 | 6-3 | 232 | BUY | FAST8 | 48.0 | 7 | 197 | 5 | 40.0 | Fera do Rift/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5500807166099548 | 0.0 | 0.0 | +63c47a3f-6712-4cfa-9376-6140da170089 / -— |
| Jogador 1 | 6-3 | 233 | BUY | FAST8 | 48.0 | 7 | 194 | 5 | 40.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.06174410134553909 | 0.0 | 0.0 | +78adfe0a-b6d8-4cc4-a482-26451f95e788 / -— |
| Jogador 1 | 6-3 | 234 | BUY | FAST8 | 48.0 | 7 | 190 | 5 | 40.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.03709704801440239 | 0.0 | 0.0 | +e7c18780-1d70-4a15-ad72-2eaa0f81df8d / -— |
| Jogador 1 | 6-3 | 235 | EQUIP_FROM_INVENTORY | FAST8 | 48.0 | 7 | 189 | 5 | 40.0 | Fera do Rift/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08936666697263718 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 236 | EQUIP_FROM_INVENTORY | FAST8 | 48.0 | 7 | 189 | 5 | 40.0 | Fera do Rift/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1636965572834015 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 237 | EQUIP_FROM_INVENTORY | FAST8 | 48.0 | 7 | 189 | 5 | 40.0 | Fera do Rift/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15167170763015747 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 239 | SELL | FAST8 | 48.0 | 7 | 200 | 5 | 40.0 | Fera do Rift/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5899999737739563 | 0.0 | 0.0 | +— / -8538e488-6f36-433a-b261-73626f24bb07 |
| Jogador 1 | 6-4 | 240 | BUY | FAST8 | 48.0 | 7 | 208 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34819790720939636 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -— |
| Jogador 1 | 6-5 | 242 | SELL | FAST8 | 48.0 | 7 | 215 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5899999737739563 | 0.0 | 0.0 | +— / -3c5f5211-f30d-44e7-ac68-0ce513a3d614 |
| Jogador 1 | 6-5 | 243 | BUY | FAST8 | 48.0 | 7 | 220 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1108972579240799 | 0.0 | 0.0 | +0f186e00-6f9d-4a22-a1ed-5ccd1b14613d / -— |
| Jogador 1 | 6-5 | 244 | SELL | FAST8 | 48.0 | 7 | 216 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009033333510160446 | 0.0 | 0.0 | +— / -e7c18780-1d70-4a15-ad72-2eaa0f81df8d |
| Jogador 1 | 6-5 | 245 | BUY | FAST8 | 48.0 | 7 | 217 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11088288575410843 | 0.0 | 0.0 | +d4e5375b-6b8c-4492-b9cc-ded108270798 / -— |
| Jogador 1 | 6-5 | 246 | SELL | FAST8 | 48.0 | 7 | 213 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003100000089034438 | 0.0 | 0.0 | +— / -864f332a-0446-4995-b7fb-76d48d293501 |
| Jogador 1 | 6-5 | 247 | BUY | FAST8 | 48.0 | 7 | 216 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10938514024019241 | 0.0 | 0.0 | +d47034a1-8b51-4b82-b1b4-5f2aee8f959a / -— |
| Jogador 1 | 6-5 | 248 | MOVE_BOARD | FAST8 | 48.0 | 7 | 214 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0011282030027359724 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-6 | 250 | SELL | STABILIZE | 30.0 | 7 | 224 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005910780280828476 | 0.0 | 0.0 | +— / -d47034a1-8b51-4b82-b1b4-5f2aee8f959a |
| Jogador 1 | 6-7 | 252 | BUY | ALL_IN | 12.0 | 7 | 237 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9679305553436279 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -— |
| Jogador 1 | 6-7 | 253 | SELL | ALL_IN | 12.0 | 7 | 234 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015533333644270897 | 0.0 | 0.0 | +— / -d4e5375b-6b8c-4492-b9cc-ded108270798 |
| Jogador 1 | 6-7 | 254 | BUY | ALL_IN | 12.0 | 7 | 238 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5255787372589111 | 0.0 | 0.0 | +b053a0fd-0f0b-4343-a920-f0a36d36e771 / -— |
| Jogador 1 | 6-7 | 255 | SELL | ALL_IN | 12.0 | 7 | 236 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015533333644270897 | 0.0 | 0.0 | +— / -0f186e00-6f9d-4a22-a1ed-5ccd1b14613d |
| Jogador 1 | 6-7 | 256 | BUY | ALL_IN | 12.0 | 7 | 240 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26279449462890625 | 0.0 | 0.0 | +a5247b50-831c-4600-bac0-e9bcdfa3ce1c / -— |
| Jogador 1 | 6-7 | 257 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 237 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-7 | 258 | SELL | ALL_IN | 12.0 | 7 | 237 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019999999552965164 | 0.0 | 0.0 | +— / -a5247b50-831c-4600-bac0-e9bcdfa3ce1c |
| Jogador 1 | 7-1 | 260 | BUY | ALL_IN | 12.0 | 7 | 251 | 5 | 40.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.40048882365226746 | 0.0 | 0.0 | +80241b75-9eb3-4b89-a754-8df65ec59786 / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178070306777954 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12192989885807037 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3096804618835449 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4080016613006592 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0723165273666382 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20116683840751648 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.400331974029541 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 40 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0378973484039307 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1819940060377121 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2737523019313812 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 46 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2639981210231781 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 47 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1472880095243454 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 48 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049025435000658035 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 49 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19665487110614777 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-1 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028999745845794678 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 52 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479705333709717 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 53 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2333821803331375 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 54 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15019755065441132 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 55 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2306191772222519 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 56 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 57 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 58 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19457465410232544 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 59 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01434213388711214 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 60 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011931832879781723 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 62 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29713717103004456 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 63 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03785359486937523 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 64 | BUY | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006640653009526432 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 2 | 2-3 | 65 | SELL | STABILIZE | 90.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-3 | 66 | PASS | STABILIZE | 90.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 72 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7671193480491638 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 73 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2947474420070648 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 74 | BUY | STABILIZE | 85.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07471544295549393 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 75 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00026666666963137686 | 0.0 | 0.0 | +— / -e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 2 | 2-4 | 76 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15264467895030975 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-4 | 77 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40151524543762207 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 78 | BUY | STABILIZE | 85.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15986567735671997 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 2 | 2-4 | 79 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008618667721748352 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 80 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032048508524894714 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 82 | BUY | STABILIZE | 85.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3183997571468353 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 83 | BUY | STABILIZE | 85.0 | 5 | 5 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026614589616656303 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 84 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03909999877214432 | 0.0 | 0.0 | +— / -ce928be1-b3ba-4640-b93c-d15c8a92833e |
| Jogador 2 | 2-5 | 85 | BUY | STABILIZE | 85.0 | 5 | 3 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19138279557228088 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 2 | 2-5 | 86 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 12.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010600143112242222 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-5 | 87 | BUY | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2809448838233948 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 2 | 2-5 | 88 | SELL | STABILIZE | 85.0 | 5 | 1 | 0 | 12.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010300000198185444 | 0.0 | 0.0 | +— / -eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 2 | 2-5 | 89 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043666668236255646 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 2-5 | 90 | BUY_XP | STABILIZE | 85.0 | 5 | 5 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 92 | BUY | STABILIZE | 79.0 | 5 | 7 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13221433758735657 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 93 | BUY | STABILIZE | 79.0 | 5 | 4 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19613097608089447 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 94 | SELL | STABILIZE | 79.0 | 5 | 2 | 0 | 12.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010105923749506474 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 2-6 | 95 | BUY_XP | STABILIZE | 79.0 | 5 | 4 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 96 | SELL | STABILIZE | 79.0 | 5 | 0 | 0 | 12.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -6a071ec5-c3f4-41b3-a0d8-c1aee62cffee |
| Jogador 2 | 2-6 | 97 | SELL | STABILIZE | 79.0 | 5 | 3 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -d1840f93-35b0-4e88-b58e-eea7267beedc |
| Jogador 2 | 2-6 | 98 | SELL | STABILIZE | 79.0 | 5 | 6 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42233332991600037 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 99 | BUY | STABILIZE | 79.0 | 5 | 9 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05966707691550255 | 0.0 | 0.0 | +8ea1c095-e10b-46d0-8097-a70a211e2881 / -— |
| Jogador 2 | 2-7 | 101 | BUY | STABILIZE | 79.0 | 5 | 14 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31323349475860596 | 0.0 | 0.0 | +0067f61f-504d-440a-b071-de7f18886e3d / -— |
| Jogador 2 | 2-7 | 102 | BUY | STABILIZE | 79.0 | 5 | 13 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11959386616945267 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 103 | SELL | STABILIZE | 79.0 | 5 | 11 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034699998795986176 | 0.0 | 0.0 | +— / -8ea1c095-e10b-46d0-8097-a70a211e2881 |
| Jogador 2 | 2-7 | 104 | SELL | STABILIZE | 79.0 | 5 | 12 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42165786027908325 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 2-7 | 105 | SELL | STABILIZE | 79.0 | 5 | 14 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09431054443120956 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-7 | 106 | SELL | STABILIZE | 79.0 | 5 | 17 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06839446723461151 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-7 | 107 | SELL | STABILIZE | 79.0 | 5 | 20 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5514836311340332 | 0.0 | 0.0 | +— / -0067f61f-504d-440a-b071-de7f18886e3d |
| Jogador 2 | 2-7 | 108 | BUY | STABILIZE | 79.0 | 5 | 21 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05172496289014816 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 109 | BUY | STABILIZE | 79.0 | 5 | 18 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05912971496582031 | 0.0 | 0.0 | +c96b6357-8134-4e68-af0b-f5695a815597 / -— |
| Jogador 2 | 3-1 | 111 | BUY | STABILIZE | 79.0 | 5 | 22 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.015629589557647705 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 112 | BUY | STABILIZE | 79.0 | 5 | 19 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0007668762700632215 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 2 | 3-1 | 113 | CRAFT_AND_EQUIP | STABILIZE | 79.0 | 5 | 17 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2577109634876251 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 114 | BUY | STABILIZE | 79.0 | 5 | 17 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07574202120304108 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 115 | SELL | STABILIZE | 79.0 | 5 | 16 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36528536677360535 | 0.0 | 0.0 | +— / -a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 3-1 | 116 | SELL | STABILIZE | 79.0 | 5 | 17 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -c96b6357-8134-4e68-af0b-f5695a815597 |
| Jogador 2 | 3-1 | 117 | SELL | STABILIZE | 79.0 | 5 | 19 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3147091865539551 | 0.0 | 0.0 | +— / -4312fba1-1471-4fb3-af6f-257248fa1437 |
| Jogador 2 | 3-1 | 118 | SELL | STABILIZE | 79.0 | 5 | 21 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 3-2 | 120 | BUY | STABILIZE | 67.0 | 5 | 31 | 3 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8865454196929932 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -7ca9b803-76eb-4283-9648-7f98bfd81149,d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 3-3 | 122 | BUY | STABILIZE | 56.0 | 6 | 39 | 3 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8533738851547241 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 123 | BUY | STABILIZE | 56.0 | 6 | 36 | 3 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06335725635290146 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 124 | BUY | STABILIZE | 56.0 | 6 | 33 | 3 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3647169768810272 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 125 | MOVE_BENCH | STABILIZE | 56.0 | 6 | 29 | 2 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39237385988235474 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 126 | MOVE_BENCH | STABILIZE | 56.0 | 6 | 29 | 2 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5037189722061157 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 127 | MOVE_BOARD | STABILIZE | 56.0 | 6 | 29 | 2 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08738195896148682 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 129 | BUY | STABILIZE | 56.0 | 6 | 38 | 3 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03324412927031517 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 130 | BUY | STABILIZE | 56.0 | 6 | 36 | 3 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03211761638522148 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-5 | 132 | BUY | STABILIZE | 56.0 | 6 | 42 | 4 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4848627746105194 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 133 | BUY | STABILIZE | 56.0 | 6 | 39 | 3 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05120393633842468 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 134 | MOVE_BOARD | STABILIZE | 56.0 | 6 | 37 | 3 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1303342878818512 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 135 | MOVE_BOARD | STABILIZE | 56.0 | 6 | 37 | 3 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015167057514190674 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 136 | SELL | STABILIZE | 56.0 | 6 | 37 | 3 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005873027257621288 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-5 | 137 | BUY | STABILIZE | 56.0 | 6 | 39 | 3 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04363517463207245 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 2 | 3-5 | 138 | SELL | STABILIZE | 56.0 | 6 | 38 | 3 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -c5a8f36d-74b1-4944-a3db-bfb601a89b59 |
| Jogador 2 | 3-6 | 140 | BUY | STABILIZE | 45.0 | 6 | 47 | 4 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3269408643245697 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-7 | 142 | SELL | STABILIZE | 35.0 | 6 | 56 | 5 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-7 | 143 | BUY | STABILIZE | 35.0 | 6 | 58 | 5 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9310394525527954 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 144 | BUY | STABILIZE | 35.0 | 6 | 55 | 5 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06630782783031464 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 3-7 | 145 | BUY | STABILIZE | 35.0 | 6 | 52 | 5 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02852000668644905 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 146 | SELL | STABILIZE | 35.0 | 6 | 50 | 5 | 20.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 147 | BUY | STABILIZE | 35.0 | 6 | 58 | 5 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24549154937267303 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 148 | SELL | STABILIZE | 35.0 | 6 | 55 | 5 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 2 | 3-7 | 149 | BUY | STABILIZE | 35.0 | 6 | 57 | 5 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03848344832658768 | 0.0 | 0.0 | +813260b6-a1b8-4a5c-978e-acd60b6b1082 / -— |
| Jogador 2 | 4-1 | 151 | CRAFT_AND_EQUIP | STABILIZE | 35.0 | 6 | 67 | 5 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18463928997516632 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 35.0 | 6 | 67 | 5 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19737716019153595 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 153 | SELL | STABILIZE | 35.0 | 6 | 67 | 5 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -813260b6-a1b8-4a5c-978e-acd60b6b1082 |
| Jogador 2 | 4-1 | 154 | BUY | STABILIZE | 35.0 | 6 | 68 | 5 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8746018409729004 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 2 | 4-1 | 155 | SELL | STABILIZE | 35.0 | 6 | 67 | 5 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 4-1 | 156 | BUY | STABILIZE | 35.0 | 6 | 69 | 5 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2539634704589844 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-2 | 158 | SELL | ALL_IN | 25.0 | 6 | 76 | 5 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 2 | 4-2 | 159 | BUY | ALL_IN | 25.0 | 6 | 79 | 5 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0013196468353271 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-2 | 160 | MOVE_BENCH | ALL_IN | 25.0 | 6 | 78 | 5 | 16.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0710027813911438 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 162 | BUY | ALL_IN | 14.0 | 6 | 89 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.455005407333374 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 2 | 4-3 | 163 | BUY | ALL_IN | 14.0 | 6 | 86 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20916388928890228 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -— |
| Jogador 2 | 4-3 | 164 | SELL | ALL_IN | 14.0 | 6 | 84 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7046999931335449 | 0.0 | 0.0 | +— / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-3 | 165 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 6 | 87 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10923496633768082 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 166 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 6 | 87 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1408347487449646 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 167 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 6 | 87 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14925213158130646 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 168 | BUY | ALL_IN | 14.0 | 6 | 87 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21910612285137177 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 2 | 4-4 | 170 | SELL | ALL_IN | 3.0 | 6 | 97 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006866666488349438 | 0.0 | 0.0 | +— / -6538f28f-845f-4f45-92bf-120931553bec |
| Jogador 2 | 4-5 | 172 | BUY | ALL_IN | 3.0 | 6 | 111 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0078327655792236 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -— |
| Jogador 2 | 4-5 | 173 | SELL | ALL_IN | 3.0 | 6 | 108 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -caf1c554-2223-4090-9f96-b551e5c579ce |
| Jogador 2 | 4-5 | 174 | BUY | ALL_IN | 3.0 | 6 | 110 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37833666801452637 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 2 | 4-5 | 175 | SELL | ALL_IN | 3.0 | 6 | 109 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-5 | 176 | BUY | ALL_IN | 3.0 | 6 | 113 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.156073659658432 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 2 | 4-5 | 177 | SELL | ALL_IN | 3.0 | 6 | 110 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04846666753292084 | 0.0 | 0.0 | +— / -734c25e1-eddf-4452-a04a-1b39db3b94d0 |
| Jogador 2 | 4-5 | 178 | BUY | ALL_IN | 3.0 | 6 | 113 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058196648955345154 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.039663553237915 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179777383804321 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5899207592010498 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22747288644313812 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2126249372959137 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.266706258058548 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39558371901512146 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 47 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21767717599868774 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 48 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007223713677376509 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012296375818550587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015378622338175774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9588384032249451 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 53 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3373487591743469 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 54 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33263662457466125 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 63 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2669682204723358 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 65 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8901210427284241 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 73 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 74 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 82 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8980467915534973 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 83 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9475502371788025 | 0.0 | 0.0 | +492fa74a-22b8-4f7d-a4f9-346fdcf565be / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-5 | 84 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 12.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7087385654449463 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 85 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47410523891448975 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020538339391350746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09967894107103348 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 88 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049516402184963226 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 89 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -492fa74a-22b8-4f7d-a4f9-346fdcf565be |
| Jogador 3 | 2-5 | 90 | BUY_XP | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 92 | BUY | STABILIZE | 89.0 | 5 | 10 | 1 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8683999180793762 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 93 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 9 | 0 | 16.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43676409125328064 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 94 | BUY | STABILIZE | 89.0 | 5 | 9 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3551364541053772 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 95 | BUY | STABILIZE | 89.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0026255708653479815 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 3 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012297529028728604 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 97 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02490667812526226 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 98 | PASS | STABILIZE | 89.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 101 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8204439878463745 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 102 | BUY | STABILIZE | 84.0 | 5 | 8 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8879010677337646 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 103 | SELL | STABILIZE | 84.0 | 5 | 6 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00286666676402092 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 3 | 2-7 | 104 | BUY | STABILIZE | 84.0 | 5 | 8 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16178391873836517 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 105 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.551115123125783e-17 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 106 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007911337539553642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 107 | PASS | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 111 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23802268505096436 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 112 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 3-1 | 113 | BUY | STABILIZE | 84.0 | 5 | 14 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8144732713699341 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-1 | 114 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 13 | 1 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4214261770248413 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 115 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0329902246594429 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 116 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4607555568218231 | 0.0 | 0.0 | +— / -2fa86b11-4e28-4652-890e-f00a79068223 |
| Jogador 3 | 3-1 | 117 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6446284055709839 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 118 | SELL | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5277026295661926 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-2 | 120 | BUY | STABILIZE | 74.0 | 5 | 26 | 2 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25897687673568726 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-3 | 122 | BUY | STABILIZE | 63.0 | 6 | 32 | 3 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024839282035827637 | 0.0 | 0.0 | +ffdee27e-2d30-40b5-9937-92be68ab1390 / -— |
| Jogador 3 | 3-3 | 123 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 30 | 3 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4067915081977844 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 124 | BUY | STABILIZE | 63.0 | 6 | 30 | 3 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3262421190738678 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 125 | BUY | STABILIZE | 63.0 | 6 | 26 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24005933105945587 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 3 | 3-3 | 126 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 23 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01095667015761137 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 127 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 23 | 2 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4146521985530853 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 129 | BUY | STABILIZE | 63.0 | 6 | 31 | 3 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12278641760349274 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 130 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 28 | 2 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 132 | SELL | STABILIZE | 63.0 | 6 | 35 | 3 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008933333680033684 | 0.0 | 0.0 | +— / -ffdee27e-2d30-40b5-9937-92be68ab1390 |
| Jogador 3 | 3-5 | 133 | BUY | STABILIZE | 63.0 | 6 | 37 | 3 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23900844156742096 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 134 | SELL | STABILIZE | 63.0 | 6 | 34 | 3 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010833333246409893 | 0.0 | 0.0 | +— / -e8b0d22c-35bc-459e-a90c-7db13fcbe34f |
| Jogador 3 | 3-5 | 135 | BUY | STABILIZE | 63.0 | 6 | 37 | 3 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20935049653053284 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 136 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 33 | 3 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 137 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 33 | 3 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 138 | PASS | STABILIZE | 63.0 | 6 | 33 | 3 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 140 | SELL | STABILIZE | 54.0 | 6 | 41 | 4 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045499999076128006 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 3 | 3-7 | 142 | BUY | STABILIZE | 44.0 | 6 | 54 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04503970965743065 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 143 | SELL | STABILIZE | 44.0 | 6 | 51 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 3-7 | 144 | BUY | STABILIZE | 44.0 | 6 | 54 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02268756926059723 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 145 | MOVE_BOARD | STABILIZE | 44.0 | 6 | 51 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008157125557772815 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 146 | SELL | STABILIZE | 44.0 | 6 | 51 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002744639292359352 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 3-7 | 147 | BUY | STABILIZE | 44.0 | 6 | 54 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00435944739729166 | 0.0 | 0.0 | +cbcde5b6-8f03-4d96-ade5-1ef113ab25bc / -— |
| Jogador 3 | 3-7 | 148 | SELL | STABILIZE | 44.0 | 6 | 53 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0047465115785598755 | 0.0 | 0.0 | +— / -cbcde5b6-8f03-4d96-ade5-1ef113ab25bc |
| Jogador 3 | 3-7 | 149 | BUY | STABILIZE | 44.0 | 6 | 54 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03510645404458046 | 0.0 | 0.0 | +f5ae964e-f157-48d1-8088-8b8a45a398b6 / -— |
| Jogador 3 | 4-1 | 151 | CRAFT_AND_EQUIP | STABILIZE | 44.0 | 6 | 64 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17167207598686218 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 44.0 | 6 | 64 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23402009904384613 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 153 | SELL | STABILIZE | 44.0 | 6 | 64 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -f5ae964e-f157-48d1-8088-8b8a45a398b6 |
| Jogador 3 | 4-1 | 154 | BUY | STABILIZE | 44.0 | 6 | 65 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7697648406028748 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 3 | 4-1 | 155 | SELL | STABILIZE | 44.0 | 6 | 62 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.062335263937711716 | 0.0 | 0.0 | +— / -ccdd8153-af58-4fe7-994c-d49f0a7a17f8 |
| Jogador 3 | 4-1 | 156 | BUY | STABILIZE | 44.0 | 6 | 66 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1118832528591156 | 0.0 | 0.0 | +48be5cb2-e7b3-41f8-b212-79e21249fa6a / -— |
| Jogador 3 | 4-2 | 158 | SELL | STABILIZE | 44.0 | 6 | 73 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -48be5cb2-e7b3-41f8-b212-79e21249fa6a |
| Jogador 3 | 4-2 | 159 | BUY | STABILIZE | 44.0 | 6 | 77 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8620596528053284 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 3 | 4-2 | 160 | SELL | STABILIZE | 44.0 | 6 | 75 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44092223048210144 | 0.0 | 0.0 | +— / -99511886-d1a7-4910-b099-5072e5385c63 |
| Jogador 3 | 4-3 | 162 | BUY | STABILIZE | 44.0 | 6 | 88 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06717903167009354 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 3 | 4-3 | 163 | SELL | STABILIZE | 44.0 | 6 | 85 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024341443553566933 | 0.0 | 0.0 | +— / -235510e3-df54-4de9-9bcf-bff6d47e364a |
| Jogador 3 | 4-3 | 164 | BUY | STABILIZE | 44.0 | 6 | 88 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15299873054027557 | 0.0 | 0.0 | +2001a193-3868-4a3f-8a71-3a9f95c04a02 / -— |
| Jogador 3 | 4-3 | 165 | SELL | STABILIZE | 44.0 | 6 | 85 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -2001a193-3868-4a3f-8a71-3a9f95c04a02 |
| Jogador 3 | 4-3 | 166 | BUY | STABILIZE | 44.0 | 6 | 88 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017933199182152748 | 0.0 | 0.0 | +3f488391-7117-4e28-b6cc-7416722351d4 / -— |
| Jogador 3 | 4-3 | 167 | SELL | STABILIZE | 44.0 | 6 | 85 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -3f488391-7117-4e28-b6cc-7416722351d4 |
| Jogador 3 | 4-3 | 168 | BUY | STABILIZE | 44.0 | 6 | 88 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25180014967918396 | 0.0 | 0.0 | +395ae945-c8a2-4d80-98a4-5eb6887b8f78 / -— |
| Jogador 3 | 4-4 | 170 | SELL | STABILIZE | 32.0 | 6 | 94 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -395ae945-c8a2-4d80-98a4-5eb6887b8f78 |
| Jogador 3 | 4-5 | 172 | BUY | STABILIZE | 32.0 | 6 | 108 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8831384778022766 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 3 | 4-5 | 173 | SELL | STABILIZE | 32.0 | 6 | 106 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5272777676582336 | 0.0 | 0.0 | +— / -5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 4-5 | 174 | BUY | STABILIZE | 32.0 | 6 | 107 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9448550939559937 | 0.0 | 0.0 | +fcc4f620-7b85-40ed-a42c-2eadd37a82fd / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9,f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 3 | 4-5 | 175 | BUY | STABILIZE | 32.0 | 6 | 104 | 5 | 32.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32677242159843445 | 0.0 | 0.0 | +226f36b1-cb9a-464a-a10a-3f21ebd41f24 / -— |
| Jogador 3 | 4-5 | 176 | BUY | STABILIZE | 32.0 | 6 | 102 | 5 | 32.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09974390268325806 | 0.0 | 0.0 | +9d2d95f2-c079-43eb-a4cd-37b224a473a8 / -— |
| Jogador 3 | 4-5 | 177 | MOVE_BENCH | STABILIZE | 32.0 | 6 | 99 | 5 | 32.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1711357831954956 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 178 | MOVE_BENCH | STABILIZE | 32.0 | 6 | 99 | 5 | 32.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10485180467367172 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 180 | SELL | STABILIZE | 32.0 | 6 | 110 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13967765867710114 | 0.0 | 0.0 | +— / -fcc4f620-7b85-40ed-a42c-2eadd37a82fd |
| Jogador 3 | 4-7 | 182 | BUY | ALL_IN | 20.0 | 6 | 128 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.023398756980896 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -111acae7-a889-409f-a15e-419d250fccd0,41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 4-7 | 183 | BUY | ALL_IN | 20.0 | 6 | 126 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0225447416305542 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -9bd6852a-b7a4-468c-a8cc-5318f7906eae,ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 3 | 4-7 | 184 | MOVE_BENCH | ALL_IN | 20.0 | 6 | 124 | 5 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31572648882865906 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 185 | BUY | ALL_IN | 20.0 | 6 | 124 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2536812722682953 | 0.0 | 0.0 | +5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 / -— |
| Jogador 3 | 4-7 | 186 | BUY | ALL_IN | 20.0 | 6 | 121 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26182064414024353 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -— |
| Jogador 3 | 4-7 | 187 | MOVE_BENCH | ALL_IN | 20.0 | 6 | 118 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4292844831943512 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 189 | BUY | ALL_IN | 20.0 | 6 | 128 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.006970560643821955 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -— |
| Jogador 3 | 5-1 | 190 | CRAFT_AND_EQUIP | ALL_IN | 20.0 | 6 | 126 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21772852540016174 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 192 | CRAFT_AND_EQUIP | ALL_IN | 4.0 | 6 | 137 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15361742675304413 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 193 | SELL | ALL_IN | 4.0 | 6 | 137 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7353000044822693 | 0.0 | 0.0 | +— / -3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 |
| Jogador 3 | 5-2 | 194 | BUY | ALL_IN | 4.0 | 6 | 142 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.977027177810669 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -— |
| Jogador 3 | 5-2 | 195 | SELL | ALL_IN | 4.0 | 6 | 140 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0166898462921381 | 0.0 | 0.0 | +— / -02e125a0-3563-47ec-a82a-cba5178731dd |
| Jogador 3 | 5-2 | 196 | BUY | ALL_IN | 4.0 | 6 | 142 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0932121276855469 | 0.0 | 0.0 | +6594349f-ecaa-4212-b063-815acae6d0bb / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0,bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 3 | 5-2 | 197 | BUY | ALL_IN | 4.0 | 6 | 140 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38801443576812744 | 0.0 | 0.0 | +8d75ef64-e2c3-47b6-a336-c9e5867158e5 / -— |
| Jogador 3 | 5-2 | 198 | MOVE_BENCH | ALL_IN | 4.0 | 6 | 139 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4958826005458832 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16303955018520355 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06030172109603882 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.012860894203186 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3393029570579529 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9801025390625 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18318334221839905 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21557970345020294 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 46 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 47 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 52 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9551578760147095 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 53 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 54 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 62 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9439310431480408 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 63 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0434552431106567 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 64 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30425798892974854 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 65 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 66 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 67 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10035383701324463 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 69 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 70 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1374218463897705 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23768481612205505 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 74 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 75 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 76 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 78 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 79 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2502065896987915 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 80 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9551072120666504 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 82 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0012191534042358 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 83 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3844655156135559 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 84 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 85 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20775465667247772 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 86 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21663010120391846 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3975071310997009 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 88 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5793925523757935 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-5 | 89 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 90 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01303389947861433 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 92 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3260316550731659 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 93 | BUY | STABILIZE | 90.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2837255001068115 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 94 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008337188512086868 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 95 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014826050959527493 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01666545867919922 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 97 | PASS | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 101 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9447794556617737 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 102 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36226481199264526 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 103 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 104 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2590000033378601 | 0.0 | 0.0 | +— / -5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 2-7 | 105 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935961008071899 | 0.0 | 0.0 | +— / -814d07bd-0296-44af-9626-26a8a224d86f |
| Jogador 4 | 2-7 | 106 | BUY | STABILIZE | 84.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13419343531131744 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 4 | 2-7 | 107 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1528579443693161 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 2-7 | 108 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3983556926250458 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 109 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 111 | BUY | STABILIZE | 84.0 | 6 | 9 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8030167818069458 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 112 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2434326559305191 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 113 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04589236527681351 | 0.0 | 0.0 | +31aa0a5f-4d66-48c2-b6d4-b76ac220c752 / -— |
| Jogador 4 | 3-1 | 114 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 115 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 4 | 3-1 | 116 | BUY | STABILIZE | 84.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0412907712161541 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 117 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899999871850014 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-1 | 118 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -31aa0a5f-4d66-48c2-b6d4-b76ac220c752 |
| Jogador 4 | 3-2 | 120 | BUY | STABILIZE | 84.0 | 6 | 11 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.837992787361145 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-3 | 122 | BUY | STABILIZE | 73.0 | 6 | 16 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8356239795684814 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -8052731e-e34c-4de7-84b1-2b986cfeddaa,c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 3-3 | 123 | BUY | STABILIZE | 73.0 | 6 | 14 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22904834151268005 | 0.0 | 0.0 | +e2ed7625-f3aa-43f0-936b-7322cb9d16f1 / -— |
| Jogador 4 | 3-3 | 124 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 12 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3394795060157776 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 125 | BUY | STABILIZE | 73.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03642524406313896 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 126 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 9 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31615185737609863 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 127 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 129 | BUY | STABILIZE | 64.0 | 6 | 15 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28586453199386597 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 130 | BUY | STABILIZE | 64.0 | 6 | 13 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7532307505607605 | 0.0 | 0.0 | +e01be6cf-34fe-4057-aef3-c08c504794cf / -— |
| Jogador 4 | 3-5 | 132 | BUY | STABILIZE | 64.0 | 6 | 18 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8058398962020874 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 133 | BUY | STABILIZE | 64.0 | 6 | 16 | 1 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7888544201850891 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 134 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 14 | 1 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013919712044298649 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 135 | MOVE_BENCH | STABILIZE | 64.0 | 6 | 14 | 1 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3752615451812744 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 136 | PASS | STABILIZE | 64.0 | 6 | 14 | 1 | 24.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 140 | BUY | STABILIZE | 52.0 | 6 | 21 | 2 | 24.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.770846962928772 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -7fd03119-ac82-49e1-b3bb-3a0caa31011f,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 3-7 | 142 | BUY | STABILIZE | 42.0 | 6 | 26 | 2 | 24.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2967117130756378 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -— |
| Jogador 4 | 3-7 | 143 | MOVE_BENCH | STABILIZE | 42.0 | 6 | 23 | 2 | 24.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.043210145086050034 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 144 | MOVE_BENCH | STABILIZE | 42.0 | 6 | 23 | 2 | 24.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4256809651851654 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 145 | SELL | STABILIZE | 42.0 | 6 | 23 | 2 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 3-7 | 146 | BUY | STABILIZE | 42.0 | 6 | 26 | 2 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.04828339070081711 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 4 | 3-7 | 147 | EQUIP_FROM_INVENTORY | STABILIZE | 42.0 | 6 | 24 | 2 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07987800985574722 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 148 | EQUIP_FROM_INVENTORY | STABILIZE | 42.0 | 6 | 24 | 2 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09562834352254868 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 149 | EQUIP_FROM_INVENTORY | STABILIZE | 42.0 | 6 | 24 | 2 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0949343666434288 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 151 | BUY | STABILIZE | 42.0 | 6 | 32 | 3 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.507036030292511 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 4 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 42.0 | 6 | 30 | 3 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15370483696460724 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 153 | CRAFT_AND_EQUIP | STABILIZE | 42.0 | 6 | 30 | 3 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18738634884357452 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 154 | BUY | STABILIZE | 42.0 | 6 | 30 | 3 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11336269974708557 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 155 | SELL | STABILIZE | 42.0 | 6 | 29 | 2 | 26.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7534999847412109 | 0.0 | 0.0 | +— / -52018505-08c9-471f-83b9-fd5066efe55a |
| Jogador 4 | 4-1 | 156 | SELL | STABILIZE | 42.0 | 6 | 34 | 3 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -23f4d10f-2614-47b2-bfb2-4fb276764b5e |
| Jogador 4 | 4-2 | 158 | BUY | STABILIZE | 31.0 | 6 | 49 | 4 | 26.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33847475051879883 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 4 | 4-2 | 159 | BUY | STABILIZE | 31.0 | 6 | 47 | 4 | 26.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24918052554130554 | 0.0 | 0.0 | +55944609-f4df-4e53-a1d1-31c79a148b22 / -— |
| Jogador 4 | 4-2 | 160 | SELL | STABILIZE | 31.0 | 6 | 46 | 4 | 26.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043855998665094376 | 0.0 | 0.0 | +— / -465ecc70-f5da-47f4-a7c0-2005a8ed24c1 |
| Jogador 4 | 4-3 | 162 | BUY | ALL_IN | 19.0 | 6 | 59 | 5 | 26.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9371217489242554 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 4 | 4-3 | 163 | SELL | ALL_IN | 19.0 | 6 | 57 | 5 | 26.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13989999890327454 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 4-3 | 164 | BUY | ALL_IN | 19.0 | 6 | 60 | 5 | 26.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16665920615196228 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -— |
| Jogador 4 | 4-3 | 165 | SELL | ALL_IN | 19.0 | 6 | 57 | 5 | 26.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5458406209945679 | 0.0 | 0.0 | +— / -eab06dbd-05d4-43b6-88f0-e6abb0e83d34 |
| Jogador 4 | 4-3 | 166 | BUY | ALL_IN | 19.0 | 6 | 59 | 5 | 26.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1343425065279007 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-3 | 167 | MOVE_BENCH | ALL_IN | 19.0 | 6 | 56 | 5 | 26.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6642044186592102 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 168 | MOVE_BENCH | ALL_IN | 19.0 | 6 | 56 | 5 | 24.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3303241729736328 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 170 | SELL | ALL_IN | 7.0 | 7 | 69 | 5 | 24.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015155120752751827 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 4 | 4-5 | 172 | BUY | ALL_IN | 7.0 | 7 | 84 | 5 | 28.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7688178420066833 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 4 | 4-5 | 173 | BUY | ALL_IN | 7.0 | 7 | 81 | 5 | 28.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18904170393943787 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 4 | 4-5 | 174 | REROLL | ALL_IN | 7.0 | 7 | 77 | 5 | 28.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 175 | SELL | ALL_IN | 7.0 | 7 | 75 | 5 | 28.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -60138930-82d5-4f1c-a5fe-a22ea4b70d36 |
| Jogador 4 | 4-5 | 176 | BUY | ALL_IN | 7.0 | 7 | 78 | 5 | 28.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8848503828048706 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 4 | 4-5 | 177 | REROLL | ALL_IN | 7.0 | 7 | 75 | 5 | 28.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 178 | SELL | ALL_IN | 7.0 | 7 | 73 | 5 | 28.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04365444555878639 | 0.0 | 0.0 | +— / -b1efce8c-0cb0-47fc-a361-c50a76c0f9de |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2185916006565094 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 23 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33173495531082153 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29088297486305237 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0322877168655396 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1994202435016632 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21338270604610443 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4090534746646881 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 47 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22639957070350647 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9719731211662292 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 54 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441535711288452 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12276306003332138 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 65 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24617168307304382 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4363538920879364 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 67 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16284826397895813 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 69 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25792863965034485 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 70 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 72 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3106982707977295 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 73 | BUY | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2186538279056549 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 74 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 75 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08824509382247925 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 76 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 77 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09730804711580276 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 78 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10479776561260223 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-4 | 79 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18894968926906586 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 80 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17966967821121216 | 0.0 | 0.0 | +32b7b452-7702-43a3-b3c4-8eda786225b9 / -— |
| Jogador 5 | 2-5 | 82 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2671852707862854 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 83 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32465773820877075 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 5 | 2-5 | 84 | SELL | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030366666615009308 | 0.0 | 0.0 | +— / -32b7b452-7702-43a3-b3c4-8eda786225b9 |
| Jogador 5 | 2-5 | 85 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 86 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030533334240317345 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-5 | 87 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40817776322364807 | 0.0 | 0.0 | +— / -de78e1b7-ed58-42dd-8374-76b578543e94 |
| Jogador 5 | 2-5 | 88 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 89 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0983823761343956 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 90 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3566199839115143 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 92 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015697868540883064 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 93 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021104255691170692 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 94 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05602027103304863 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 95 | SELL | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 96 | SELL | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3451807200908661 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 2-6 | 97 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005923189222812653 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 98 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 99 | SELL | STABILIZE | 100.0 | 6 | 2 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3343333303928375 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-7 | 101 | BUY | STABILIZE | 94.0 | 6 | 8 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20675867795944214 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 102 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05196301266551018 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 103 | BUY_XP | STABILIZE | 94.0 | 6 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 104 | BUY | STABILIZE | 94.0 | 6 | 1 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027100319042801857 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 2-7 | 105 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 0 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.372784286737442 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 106 | SELL | STABILIZE | 94.0 | 6 | 0 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3343333303928375 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 2-7 | 107 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005703182541765273 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 108 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 109 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 111 | BUY | STABILIZE | 94.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20223550498485565 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 112 | BUY | STABILIZE | 94.0 | 6 | 3 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13203604519367218 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 113 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19029124081134796 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 114 | SELL | STABILIZE | 94.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08575989305973053 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 3-1 | 115 | BUY | STABILIZE | 94.0 | 6 | 2 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04237848520278931 | 0.0 | 0.0 | +79ed9815-7667-4e50-86a3-420599ce8c79 / -— |
| Jogador 5 | 3-1 | 116 | SELL | STABILIZE | 94.0 | 6 | 0 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -79ed9815-7667-4e50-86a3-420599ce8c79 |
| Jogador 5 | 3-1 | 117 | SELL | STABILIZE | 94.0 | 6 | 2 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09482568502426147 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-1 | 118 | BUY_XP | STABILIZE | 94.0 | 6 | 4 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 120 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.712977409362793 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-3 | 122 | BUY | STABILIZE | 84.0 | 6 | 9 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7940902709960938 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 123 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2837259769439697 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 124 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09566666930913925 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 3-3 | 125 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2755972445011139 | 0.0 | 0.0 | +a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a / -— |
| Jogador 5 | 3-3 | 126 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 127 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19566667079925537 | 0.0 | 0.0 | +— / -a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a |
| Jogador 5 | 3-4 | 129 | BUY | STABILIZE | 75.0 | 6 | 7 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2755308747291565 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 130 | SELL | STABILIZE | 75.0 | 6 | 5 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19566667079925537 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-5 | 132 | BUY | STABILIZE | 75.0 | 6 | 12 | 1 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379454612731934 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 3-5 | 133 | SELL | STABILIZE | 75.0 | 6 | 11 | 1 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-5 | 134 | EQUIP_FROM_INVENTORY | STABILIZE | 75.0 | 6 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10891102999448776 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 135 | MOVE_BENCH | STABILIZE | 75.0 | 6 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4882439970970154 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 136 | BUY | STABILIZE | 75.0 | 6 | 14 | 1 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14635102450847626 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 137 | BUY | STABILIZE | 75.0 | 6 | 11 | 1 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11527377367019653 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 138 | BUY_XP | STABILIZE | 75.0 | 6 | 8 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 140 | BUY | STABILIZE | 64.0 | 7 | 10 | 1 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6768472194671631 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-7 | 142 | BUY | STABILIZE | 64.0 | 7 | 13 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3699609339237213 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 143 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 144 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017082568258047104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 145 | PASS | STABILIZE | 64.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 151 | BUY | STABILIZE | 64.0 | 7 | 16 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6781622767448425 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -— |
| Jogador 5 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 64.0 | 7 | 13 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18872882425785065 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 153 | BUY | STABILIZE | 64.0 | 7 | 13 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4599930942058563 | 0.0 | 0.0 | +6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 / -— |
| Jogador 5 | 4-1 | 154 | CRAFT_AND_EQUIP | STABILIZE | 64.0 | 7 | 11 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1786121129989624 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 155 | SELL | STABILIZE | 64.0 | 7 | 11 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4335755407810211 | 0.0 | 0.0 | +— / -6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 |
| Jogador 5 | 4-1 | 156 | SELL | STABILIZE | 64.0 | 7 | 13 | 1 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46034079790115356 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 4-2 | 158 | BUY | STABILIZE | 52.0 | 7 | 22 | 2 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7825928926467896 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -486e92ad-4dcf-4c0e-a470-e0b87777d380,a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 4-2 | 159 | BUY | STABILIZE | 52.0 | 7 | 19 | 1 | 28.0 | Espinhos Negros/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2958930432796478 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 5 | 4-2 | 160 | BUY | STABILIZE | 52.0 | 7 | 16 | 1 | 28.0 | Espinhos Negros/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28749191761016846 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 5 | 4-3 | 162 | BUY | STABILIZE | 52.0 | 7 | 22 | 2 | 28.0 | Espinhos Negros/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7448094487190247 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 5 | 4-3 | 163 | SELL | STABILIZE | 52.0 | 7 | 19 | 1 | 28.0 | Espinhos Negros/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -dde5ed69-0fc4-4d15-b12c-a5252a239040 |
| Jogador 5 | 4-3 | 164 | BUY | STABILIZE | 52.0 | 7 | 27 | 2 | 28.0 | Espinhos Negros/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8261206150054932 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -— |
| Jogador 5 | 4-3 | 165 | SELL | STABILIZE | 52.0 | 7 | 26 | 2 | 28.0 | Espinhos Negros/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049425382167100906 | 0.0 | 0.0 | +— / -fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 5 | 4-3 | 166 | SELL | STABILIZE | 52.0 | 7 | 29 | 2 | 28.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.455313503742218 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 4-3 | 167 | SELL | STABILIZE | 52.0 | 7 | 32 | 3 | 28.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09650184214115143 | 0.0 | 0.0 | +— / -0c07379e-5dd1-42e9-aa7a-a764f949deee |
| Jogador 5 | 4-3 | 168 | BUY | STABILIZE | 52.0 | 7 | 35 | 3 | 28.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045225247740745544 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-4 | 170 | BUY | STABILIZE | 52.0 | 7 | 42 | 4 | 28.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9276249408721924 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -333b0a0b-8868-40b2-96e9-71e468c5dd1f,9593a62e-442f-410a-8a0c-7d781e2487cc |
| Jogador 5 | 4-5 | 172 | BUY | STABILIZE | 52.0 | 7 | 51 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11278754472732544 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 5 | 4-5 | 173 | BUY | STABILIZE | 52.0 | 7 | 50 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27576744556427 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -— |
| Jogador 5 | 4-5 | 174 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 49 | 4 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0051783607341349125 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 175 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 49 | 4 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 176 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 49 | 4 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01597990281879902 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 177 | PASS | STABILIZE | 52.0 | 7 | 49 | 4 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04928571358323097 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 180 | BUY | STABILIZE | 38.0 | 7 | 58 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9099467992782593 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -1457cd1e-c240-4ce5-9217-a91bddfc8807,4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 4-7 | 182 | BUY | STABILIZE | 28.0 | 7 | 66 | 5 | 28.0 | Vivaz/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36099451780319214 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 5 | 4-7 | 183 | BUY | STABILIZE | 28.0 | 7 | 65 | 5 | 28.0 | Vivaz/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22066693007946014 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 5 | 4-7 | 184 | SELL | STABILIZE | 28.0 | 7 | 61 | 5 | 28.0 | Vivaz/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11129999905824661 | 0.0 | 0.0 | +— / -023f01af-91d0-4e07-8229-2b7cded83151 |
| Jogador 5 | 4-7 | 185 | REROLL | STABILIZE | 28.0 | 7 | 69 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 186 | BUY | STABILIZE | 28.0 | 7 | 67 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9312934875488281 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 5 | 4-7 | 187 | SELL | STABILIZE | 28.0 | 7 | 66 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -b755a0c5-f515-4f95-8f58-1e05f40ad302 |
| Jogador 5 | 5-1 | 189 | BUY | STABILIZE | 28.0 | 7 | 80 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9346380233764648 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 5 | 5-1 | 190 | CRAFT_AND_EQUIP | STABILIZE | 28.0 | 7 | 79 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07759271562099457 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 192 | CRAFT_AND_EQUIP | STABILIZE | 28.0 | 7 | 90 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12636250257492065 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 193 | SELL | STABILIZE | 28.0 | 7 | 90 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005511346738785505 | 0.0 | 0.0 | +— / -61362365-2cf7-40e4-95f9-98e28728fd39 |
| Jogador 5 | 5-2 | 194 | BUY | STABILIZE | 28.0 | 7 | 91 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4116579294204712 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 5 | 5-2 | 195 | SELL | STABILIZE | 28.0 | 7 | 89 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -a72137b3-498b-40e1-938a-639f56745f08 |
| Jogador 5 | 5-2 | 196 | BUY | STABILIZE | 28.0 | 7 | 90 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09830468893051147 | 0.0 | 0.0 | +da6c9f59-1fc3-467d-8845-bf7b38b4232c / -— |
| Jogador 5 | 5-2 | 197 | REROLL | STABILIZE | 28.0 | 7 | 87 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 198 | SELL | STABILIZE | 28.0 | 7 | 85 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -da6c9f59-1fc3-467d-8845-bf7b38b4232c |
| Jogador 5 | 5-3 | 200 | BUY | STABILIZE | 28.0 | 7 | 100 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1942950338125229 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 5 | 5-4 | 202 | SELL | ALL_IN | 13.0 | 7 | 105 | 5 | 28.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -3b934078-806c-40f0-b102-e9131220f70e |
| Jogador 5 | 5-4 | 203 | BUY | ALL_IN | 13.0 | 7 | 109 | 5 | 28.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17446820437908173 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -— |
| Jogador 5 | 5-4 | 204 | REROLL | ALL_IN | 13.0 | 7 | 108 | 5 | 28.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 205 | SELL | ALL_IN | 13.0 | 7 | 106 | 5 | 28.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009160428307950497 | 0.0 | 0.0 | +— / -7f9f3188-2482-4518-9fd2-34f0ea1527a9 |
| Jogador 5 | 5-4 | 206 | BUY | ALL_IN | 13.0 | 7 | 107 | 5 | 28.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3647025227546692 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -— |
| Jogador 5 | 5-4 | 207 | SELL | ALL_IN | 13.0 | 7 | 105 | 5 | 28.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5306144952774048 | 0.0 | 0.0 | +— / -f2dbe099-e518-4261-b120-9f327b112dcb |
| Jogador 5 | 5-4 | 208 | BUY | ALL_IN | 13.0 | 7 | 107 | 5 | 28.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1363856941461563 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 5 | 5-5 | 210 | SELL | ALL_IN | 13.0 | 7 | 114 | 5 | 28.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04846666753292084 | 0.0 | 0.0 | +— / -3faf4ab2-44b3-4779-985b-658c64791c28 |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0372674465179443 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5739498138427734 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.025650978088379 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 35 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 43 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1292608678340912 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15291057527065277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2878401279449463 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 46 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 47 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 52 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2621338963508606 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 53 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2463040053844452 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 54 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 55 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 56 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 62 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28902435302734375 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 63 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1803932934999466 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 64 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841120302677155 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 65 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14495904743671417 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 66 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1517755091190338 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 67 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 72 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18289299309253693 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 73 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24050183594226837 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 74 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8068224787712097 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 75 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 76 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 77 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10961306095123291 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 78 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 79 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14381426572799683 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-4 | 80 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14380952715873718 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 82 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8596822023391724 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 83 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28841620683670044 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 84 | BUY_XP | STABILIZE | 83.0 | 5 | 7 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 85 | SELL | STABILIZE | 83.0 | 5 | 3 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45226582884788513 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 86 | BUY_XP | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 87 | SELL | STABILIZE | 83.0 | 5 | 1 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4931742250919342 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-5 | 88 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 89 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 8.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21166107058525085 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 90 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-6 | 92 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32035815715789795 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 93 | BUY_XP | STABILIZE | 76.0 | 6 | 6 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 94 | SELL | STABILIZE | 76.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18617047369480133 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 95 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006841098889708519 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 97 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-6 | 98 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6276098489761353 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 99 | BUY | STABILIZE | 76.0 | 6 | 2 | 0 | 12.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1366092711687088 | 0.0 | 0.0 | +53bbd605-d60b-4555-b5e8-29f1cfbb83b4 / -— |
| Jogador 6 | 2-7 | 101 | BUY | STABILIZE | 70.0 | 6 | 7 | 0 | 12.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.317169725894928 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 102 | BUY | STABILIZE | 70.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3625761568546295 | 0.0 | 0.0 | +dc83202b-476c-4438-90aa-a615b764b7e4 / -— |
| Jogador 6 | 2-7 | 103 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13620233535766602 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 104 | SELL | STABILIZE | 70.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07491586357355118 | 0.0 | 0.0 | +— / -53bbd605-d60b-4555-b5e8-29f1cfbb83b4 |
| Jogador 6 | 2-7 | 105 | SELL | STABILIZE | 70.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1630827933549881 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 106 | BUY | STABILIZE | 70.0 | 6 | 8 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11710625886917114 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 107 | BUY_XP | STABILIZE | 70.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 108 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 1 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07568792998790741 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 109 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 1 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02214992046356201 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 111 | BUY | STABILIZE | 70.0 | 6 | 8 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26031696796417236 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 112 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17849762737751007 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 113 | BUY | STABILIZE | 70.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09548237919807434 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 114 | SELL | STABILIZE | 70.0 | 6 | 1 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05032064765691757 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-1 | 115 | BUY_XP | STABILIZE | 70.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 116 | SELL | STABILIZE | 70.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038333334028720856 | 0.0 | 0.0 | +— / -4eedd873-e4ec-41e5-9f5e-48e443e80f86 |
| Jogador 6 | 3-1 | 117 | BUY_XP | STABILIZE | 70.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 118 | MOVE_BENCH | STABILIZE | 70.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2874350845813751 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 120 | BUY | STABILIZE | 70.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379754424095154 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-3 | 122 | BUY | STABILIZE | 60.0 | 6 | 10 | 1 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.202566459774971 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 123 | BUY | STABILIZE | 60.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0841454565525055 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 124 | BUY | STABILIZE | 60.0 | 6 | 4 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04471971467137337 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 6 | 3-3 | 125 | MOVE_BOARD | STABILIZE | 60.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10031282156705856 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 126 | MOVE_BOARD | STABILIZE | 60.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07774132490158081 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 127 | SELL | STABILIZE | 60.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -25b16126-6e41-4649-a47f-42656ffc7a08 |
| Jogador 6 | 3-4 | 129 | BUY | STABILIZE | 60.0 | 6 | 10 | 1 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7222812175750732 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 130 | BUY | STABILIZE | 60.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2795027792453766 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 6 | 3-5 | 132 | BUY | STABILIZE | 60.0 | 7 | 9 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7997981905937195 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 133 | BUY | STABILIZE | 60.0 | 7 | 6 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3437627851963043 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 6 | 3-5 | 134 | MOVE_BENCH | STABILIZE | 60.0 | 7 | 3 | 0 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45502936840057373 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 135 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 3 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1626417338848114 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 136 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 3 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1040763184428215 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 137 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 3 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012763437815010548 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 138 | BUY | STABILIZE | 60.0 | 7 | 3 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06908068805932999 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-6 | 140 | BUY | STABILIZE | 60.0 | 7 | 7 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5607436895370483 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-7 | 142 | SELL | STABILIZE | 60.0 | 7 | 11 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026684843003749847 | 0.0 | 0.0 | +— / -dc83202b-476c-4438-90aa-a615b764b7e4 |
| Jogador 6 | 3-7 | 143 | BUY | STABILIZE | 60.0 | 7 | 12 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05771389231085777 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 144 | SELL | STABILIZE | 60.0 | 7 | 7 | 0 | 24.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06883333623409271 | 0.0 | 0.0 | +— / -891aea62-e06a-46d4-8250-a3d4a56e847d |
| Jogador 6 | 3-7 | 145 | BUY | STABILIZE | 60.0 | 7 | 12 | 1 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25270557403564453 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 146 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 147 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01232683751732111 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 148 | PASS | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 151 | CRAFT_AND_EQUIP | STABILIZE | 60.0 | 7 | 14 | 1 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2543240189552307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 60.0 | 7 | 14 | 1 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18881899118423462 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 153 | SELL | STABILIZE | 60.0 | 7 | 14 | 1 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 6 | 4-1 | 154 | BUY | STABILIZE | 60.0 | 7 | 18 | 1 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5364910960197449 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -06db3a99-d008-406a-ac86-30884335d7c2,50f9a30c-27db-4ed0-804e-548f87950b17 |
| Jogador 6 | 4-1 | 155 | BUY | STABILIZE | 60.0 | 7 | 15 | 1 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09069458395242691 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 6 | 4-1 | 156 | BUY | STABILIZE | 60.0 | 7 | 12 | 1 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0386100672185421 | 0.0 | 0.0 | +3d7ba32f-3349-479e-bb6f-9cd1f2006149 / -— |
| Jogador 6 | 4-2 | 158 | SELL | STABILIZE | 49.0 | 7 | 17 | 1 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0459546335041523 | 0.0 | 0.0 | +— / -f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-2 | 159 | BUY | STABILIZE | 49.0 | 7 | 25 | 2 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16662244498729706 | 0.0 | 0.0 | +6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb / -— |
| Jogador 6 | 4-2 | 160 | SELL | STABILIZE | 49.0 | 7 | 22 | 2 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024611936882138252 | 0.0 | 0.0 | +— / -3d7ba32f-3349-479e-bb6f-9cd1f2006149 |
| Jogador 6 | 4-3 | 162 | BUY | STABILIZE | 38.0 | 7 | 31 | 3 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08683845400810242 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-3 | 163 | SELL | STABILIZE | 38.0 | 7 | 27 | 2 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050966665148735046 | 0.0 | 0.0 | +— / -a8a8381a-f3a8-45ec-9106-293d73fca0c8 |
| Jogador 6 | 4-3 | 164 | BUY | STABILIZE | 38.0 | 7 | 30 | 3 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0813400000333786 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 6 | 4-3 | 165 | REROLL | STABILIZE | 38.0 | 7 | 28 | 2 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1340000033378601 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 166 | SELL | STABILIZE | 38.0 | 7 | 26 | 2 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011938636191189289 | 0.0 | 0.0 | +— / -badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 6 | 4-3 | 167 | BUY | STABILIZE | 38.0 | 7 | 28 | 2 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31636470556259155 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 6 | 4-3 | 168 | SELL | STABILIZE | 38.0 | 7 | 27 | 2 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032595906406641006 | 0.0 | 0.0 | +— / -6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb |
| Jogador 6 | 4-4 | 170 | BUY | STABILIZE | 38.0 | 7 | 39 | 3 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04676888510584831 | 0.0 | 0.0 | +1f7f2a48-1318-4fc6-87cc-03d557bf69ea / -— |
| Jogador 6 | 4-5 | 172 | SELL | STABILIZE | 38.0 | 7 | 45 | 4 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -1f7f2a48-1318-4fc6-87cc-03d557bf69ea |
| Jogador 6 | 4-5 | 173 | BUY | STABILIZE | 38.0 | 7 | 47 | 4 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3432065546512604 | 0.0 | 0.0 | +31ea6d79-501d-4f2a-821d-7058334be82f / -— |
| Jogador 6 | 4-5 | 174 | SELL | STABILIZE | 38.0 | 7 | 43 | 4 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 |
| Jogador 6 | 4-5 | 175 | BUY | STABILIZE | 38.0 | 7 | 47 | 4 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9163951873779297 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 4-5 | 176 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 46 | 4 | 20.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17031481862068176 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 177 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 46 | 4 | 26.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01641288585960865 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 178 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 46 | 4 | 26.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4014253318309784 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 180 | BUY | STABILIZE | 38.0 | 7 | 57 | 5 | 32.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8873287439346313 | 0.0 | 0.0 | +5c43307a-6d61-4493-a1ed-cb428d79a254 / -— |
| Jogador 6 | 4-7 | 182 | BUY | STABILIZE | 38.0 | 7 | 66 | 5 | 32.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9622785449028015 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -5b95b64a-b46a-4827-8613-307c8dadc072,cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 4-7 | 183 | BUY | STABILIZE | 38.0 | 7 | 63 | 5 | 26.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9427335858345032 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 4-7 | 184 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 60 | 5 | 14.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3499591648578644 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 185 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 60 | 5 | 26.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1657467484474182 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 186 | BUY | STABILIZE | 38.0 | 7 | 60 | 5 | 28.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3475368916988373 | 0.0 | 0.0 | +943437ce-e190-4790-986b-4e66e49637a7 / -— |
| Jogador 6 | 4-7 | 187 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 56 | 5 | 28.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08617914468050003 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 189 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 67 | 5 | 34.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1467576026916504 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 190 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 67 | 5 | 34.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13482241332530975 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 192 | BUY | ALL_IN | 24.0 | 7 | 77 | 5 | 34.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0504348278045654 | 0.0 | 0.0 | +4432f76a-94cc-4a96-b72b-1cf35b310dca / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 5-2 | 193 | BUY | ALL_IN | 24.0 | 7 | 76 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0421302318572998 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4,ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c |
| Jogador 6 | 5-2 | 194 | MOVE_BENCH | ALL_IN | 24.0 | 7 | 73 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08105594664812088 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 195 | MOVE_BENCH | ALL_IN | 24.0 | 7 | 73 | 5 | 40.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8492336869239807 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 196 | MOVE_BENCH | ALL_IN | 24.0 | 7 | 73 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23712016642093658 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 197 | PASS | ALL_IN | 24.0 | 7 | 73 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6282188892364502 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 198 | MOVE_BENCH | ALL_IN | 24.0 | 7 | 73 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3434959352016449 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 200 | BUY | ALL_IN | 10.0 | 7 | 84 | 5 | 34.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12868358194828033 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0485279560089111 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23092935979366302 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368268489837646 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24681922793388367 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 38 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.826633632183075 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19990859925746918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24556782841682434 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 46 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3008885979652405 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 47 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047570824623108 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15447205305099487 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 55 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17901837825775146 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 56 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 58 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 59 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11028668284416199 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 60 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1539463847875595 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 62 | BUY | STABILIZE | 94.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475420951843262 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 63 | BUY | STABILIZE | 94.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6461395025253296 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17267221212387085 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 65 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09771741181612015 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 66 | SELL | STABILIZE | 94.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6186314821243286 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 2-3 | 67 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.142038494348526 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 68 | BUY_XP | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 69 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 72 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31499430537223816 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 73 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2572064995765686 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 74 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 82 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28892770409584045 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 83 | BUY | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31405338644981384 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 84 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005171899683773518 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 85 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0160977803170681 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 86 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 92 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9129268527030945 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 93 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8861379027366638 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 94 | BUY_XP | STABILIZE | 94.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 95 | SELL | STABILIZE | 94.0 | 5 | 1 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00286666676402092 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-6 | 96 | SELL | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48007455468177795 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-6 | 97 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 98 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0022987904958426952 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 99 | SELL | STABILIZE | 94.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06310796737670898 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-7 | 101 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2672550082206726 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 102 | BUY_XP | STABILIZE | 94.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03353499993681908 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 103 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46332263946533203 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 104 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015011870302259922 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 105 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01493695005774498 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 106 | PASS | STABILIZE | 94.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 111 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2845257520675659 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 112 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15369176864624023 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 113 | BUY_XP | STABILIZE | 94.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 114 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004193209169898182 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 115 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014673740603029728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 116 | PASS | STABILIZE | 94.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 120 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28169578313827515 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-3 | 122 | BUY | STABILIZE | 84.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.837782084941864 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -242805ca-f275-4e04-a2f5-81e0b6680dd1,7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 3-3 | 123 | BUY_XP | STABILIZE | 84.0 | 6 | 8 | 0 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 124 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 125 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5583645105361938 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 126 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497933641076088 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 127 | PASS | STABILIZE | 84.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 129 | BUY | STABILIZE | 74.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379953503608704 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -4e206e09-40e3-4699-81cb-8aaf01109dea,a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 3-4 | 130 | BUY | STABILIZE | 74.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8311177492141724 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-5 | 132 | BUY | STABILIZE | 74.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7953240871429443 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 133 | BUY | STABILIZE | 74.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2214668095111847 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 134 | SELL | STABILIZE | 74.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -1ff50c59-5133-459e-8bf1-d449c26efabf |
| Jogador 7 | 3-5 | 135 | EQUIP_FROM_INVENTORY | STABILIZE | 74.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12827123701572418 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 136 | EQUIP_FROM_INVENTORY | STABILIZE | 74.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11077457666397095 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 137 | BUY | STABILIZE | 74.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1251903921365738 | 0.0 | 0.0 | +2074e6ec-81e7-41c9-be7e-a0d9310fbafa / -— |
| Jogador 7 | 3-5 | 138 | MOVE_BENCH | STABILIZE | 74.0 | 6 | 3 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5088528990745544 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 140 | BUY | STABILIZE | 74.0 | 6 | 9 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7727383375167847 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-7 | 142 | BUY | STABILIZE | 74.0 | 6 | 13 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7116923332214355 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 143 | SELL | STABILIZE | 74.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 7 | 3-7 | 144 | MOVE_BOARD | STABILIZE | 74.0 | 6 | 13 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01030804868787527 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 145 | SELL | STABILIZE | 74.0 | 6 | 13 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5389999747276306 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 3-7 | 146 | EQUIP_FROM_INVENTORY | STABILIZE | 74.0 | 6 | 21 | 2 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08216829597949982 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 147 | SELL | STABILIZE | 74.0 | 6 | 21 | 2 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 3-7 | 148 | BUY | STABILIZE | 74.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11977413296699524 | 0.0 | 0.0 | +328e1a7d-391c-48e0-b268-64d26b4db788 / -— |
| Jogador 7 | 3-7 | 149 | SELL | STABILIZE | 74.0 | 6 | 23 | 2 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15159764885902405 | 0.0 | 0.0 | +— / -2074e6ec-81e7-41c9-be7e-a0d9310fbafa |
| Jogador 7 | 4-1 | 151 | BUY | STABILIZE | 74.0 | 6 | 33 | 3 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3069342374801636 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -— |
| Jogador 7 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 74.0 | 6 | 31 | 3 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13860468566417694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 153 | CRAFT_AND_EQUIP | STABILIZE | 74.0 | 6 | 31 | 3 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.121343694627285 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 154 | BUY | STABILIZE | 74.0 | 6 | 31 | 3 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023802559822797775 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-1 | 155 | BUY_XP | STABILIZE | 74.0 | 6 | 29 | 2 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004301874898374081 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 156 | SELL | STABILIZE | 74.0 | 6 | 25 | 2 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07223844528198242 | 0.0 | 0.0 | +— / -328e1a7d-391c-48e0-b268-64d26b4db788 |
| Jogador 7 | 4-2 | 158 | BUY | STABILIZE | 74.0 | 7 | 35 | 3 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8353672623634338 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -— |
| Jogador 7 | 4-2 | 159 | BUY | STABILIZE | 74.0 | 7 | 33 | 3 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8951887488365173 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -0803068a-0141-4e75-ab81-12bb13986025,cc56fedc-f555-4075-af15-6b5fb93a156f |
| Jogador 7 | 4-2 | 160 | BUY_XP | STABILIZE | 74.0 | 7 | 31 | 3 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10206499695777893 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 162 | BUY | FAST8 | 74.0 | 7 | 36 | 3 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7955577969551086 | 0.0 | 0.0 | +17d5d3f2-999d-4788-852b-bda84adb4350 / -— |
| Jogador 7 | 4-3 | 163 | BUY | FAST8 | 74.0 | 7 | 34 | 3 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1258738487958908 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 7 | 4-3 | 164 | BUY | FAST8 | 74.0 | 7 | 30 | 3 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024734070524573326 | 0.0 | 0.0 | +f5cca112-4fa0-4ee6-a863-20a5d49ab7ef / -— |
| Jogador 7 | 4-3 | 165 | MOVE_BOARD | FAST8 | 74.0 | 7 | 28 | 2 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 166 | MOVE_BOARD | FAST8 | 74.0 | 7 | 28 | 2 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 167 | PASS | FAST8 | 74.0 | 7 | 28 | 2 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034285712987184525 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 170 | SELL | FAST8 | 74.0 | 7 | 38 | 3 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 7 | 4-5 | 172 | BUY | FAST8 | 74.0 | 7 | 54 | 5 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6286681294441223 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 7 | 4-5 | 173 | MOVE_BOARD | FAST8 | 74.0 | 7 | 52 | 5 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0029365343507379293 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 174 | SELL | FAST8 | 74.0 | 7 | 52 | 5 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012233865447342396 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-5 | 175 | BUY | FAST8 | 74.0 | 7 | 54 | 5 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8453454971313477 | 0.0 | 0.0 | +84981e98-bfb7-4c49-a020-51cf6d864881 / -262702a6-b710-4129-9dc6-0c1a04514ff9,f5cca112-4fa0-4ee6-a863-20a5d49ab7ef |
| Jogador 7 | 4-5 | 176 | BUY | FAST8 | 74.0 | 7 | 52 | 5 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015742167830467224 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 7 | 4-5 | 177 | MOVE_BOARD | FAST8 | 74.0 | 7 | 49 | 4 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005593472626060247 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 178 | MOVE_BOARD | FAST8 | 74.0 | 7 | 49 | 4 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 180 | BUY | FAST8 | 74.0 | 7 | 63 | 5 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8877860307693481 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,d69fa0dc-74b6-4ee7-90f7-aaca5405c59c |
| Jogador 7 | 4-7 | 182 | BUY | STABILIZE | 74.0 | 7 | 74 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9623469114303589 | 0.0 | 0.0 | +deb56311-9843-48be-9a22-3529305d04e5 / -033a84d9-70f6-46a8-a6eb-a2f03be70400,17d5d3f2-999d-4788-852b-bda84adb4350 |
| Jogador 7 | 4-7 | 183 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 72 | 5 | 22.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23216861486434937 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 184 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 72 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17563995718955994 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 185 | BUY | FAST8 | 74.0 | 7 | 72 | 5 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2860424816608429 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 7 | 4-7 | 186 | MOVE_BENCH | FAST8 | 74.0 | 7 | 69 | 5 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.536328136920929 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 187 | MOVE_BOARD | FAST8 | 74.0 | 7 | 69 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0151974493637681 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 189 | BUY | FAST8 | 74.0 | 7 | 82 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05213019624352455 | 0.0 | 0.0 | +af98a89b-ee97-45ce-972a-3f41e280b6b2 / -— |
| Jogador 7 | 5-1 | 190 | CRAFT_AND_EQUIP | FAST8 | 74.0 | 7 | 80 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09745728224515915 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 192 | BUY | FAST8 | 74.0 | 7 | 94 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.549710214138031 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -— |
| Jogador 7 | 5-2 | 193 | CRAFT_AND_EQUIP | FAST8 | 74.0 | 7 | 92 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07082228362560272 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 194 | MOVE_BOARD | FAST8 | 74.0 | 7 | 92 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08072081953287125 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 195 | MOVE_BOARD | FAST8 | 74.0 | 7 | 92 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06298771500587463 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 196 | MOVE_BOARD | FAST8 | 74.0 | 7 | 92 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012989170849323273 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 197 | SELL | FAST8 | 74.0 | 7 | 92 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -4aa5d560-d9d3-45f9-802a-bdbe95788762 |
| Jogador 7 | 5-2 | 198 | BUY | FAST8 | 74.0 | 7 | 100 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021048005670309067 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -— |
| Jogador 7 | 5-3 | 200 | SELL | FAST8 | 59.0 | 7 | 107 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -deb56311-9843-48be-9a22-3529305d04e5 |
| Jogador 7 | 5-4 | 202 | BUY | FAST8 | 59.0 | 7 | 123 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.32988566160202026 | 0.0 | 0.0 | +f00a538c-0607-4d8b-babe-7c13daf80c42 / -— |
| Jogador 7 | 5-4 | 203 | EQUIP_FROM_INVENTORY | FAST8 | 59.0 | 7 | 121 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04253118485212326 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 204 | EQUIP_FROM_INVENTORY | FAST8 | 59.0 | 7 | 121 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11230472475290298 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 205 | EQUIP_FROM_INVENTORY | FAST8 | 59.0 | 7 | 121 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14549151062965393 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 206 | SELL | FAST8 | 59.0 | 7 | 121 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -8aa832ec-4c09-43bd-ae21-baf7268e468d |
| Jogador 7 | 5-4 | 207 | BUY | FAST8 | 59.0 | 7 | 124 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15688660740852356 | 0.0 | 0.0 | +d2afd490-f89f-47c9-8279-a88acde5b1b6 / -— |
| Jogador 7 | 5-4 | 208 | SELL | FAST8 | 59.0 | 7 | 121 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -9f445115-49cc-4647-91a0-a80e347e9c62 |
| Jogador 7 | 5-5 | 210 | BUY | FAST8 | 59.0 | 7 | 134 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27336007356643677 | 0.0 | 0.0 | +407092ea-3a14-4555-9ebd-64a36c41d1d0 / -— |
| Jogador 7 | 5-6 | 212 | SELL | FAST8 | 45.0 | 7 | 142 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08166062086820602 | 0.0 | 0.0 | +— / -407092ea-3a14-4555-9ebd-64a36c41d1d0 |
| Jogador 7 | 5-6 | 213 | BUY | FAST8 | 45.0 | 7 | 144 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27341029047966003 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 7 | 5-6 | 214 | SELL | FAST8 | 45.0 | 7 | 142 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0816049724817276 | 0.0 | 0.0 | +— / -2d5214b0-3e0c-4e71-8664-2459bf616650 |
| Jogador 7 | 5-6 | 215 | BUY | FAST8 | 45.0 | 7 | 144 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08358228951692581 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 7 | 5-6 | 216 | SELL | FAST8 | 45.0 | 7 | 141 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034270450472831726 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 7 | 5-6 | 217 | BUY | FAST8 | 45.0 | 7 | 144 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016716038808226585 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 7 | 5-7 | 219 | SELL | FAST8 | 45.0 | 7 | 151 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -0a29573e-2a7b-4719-9b6e-49c2f476bc04 |
| Jogador 7 | 5-7 | 220 | BUY | FAST8 | 45.0 | 7 | 154 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8681042194366455 | 0.0 | 0.0 | +3c46b699-2b56-48d0-820c-b523c5153b9f / -— |
| Jogador 7 | 6-1 | 222 | EQUIP_FROM_INVENTORY | FAST8 | 45.0 | 7 | 161 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13405558466911316 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 223 | SELL | FAST8 | 45.0 | 7 | 161 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -d2afd490-f89f-47c9-8279-a88acde5b1b6 |
| Jogador 7 | 6-1 | 224 | BUY | FAST8 | 45.0 | 7 | 164 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9287751317024231 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -af98a89b-ee97-45ce-972a-3f41e280b6b2,b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 7 | 6-1 | 225 | BUY | FAST8 | 45.0 | 7 | 162 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1693120300769806 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -— |
| Jogador 7 | 6-1 | 226 | BUY | FAST8 | 45.0 | 7 | 158 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016939952969551086 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 7 | 6-2 | 228 | SELL | FAST8 | 45.0 | 7 | 165 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09140308946371078 | 0.0 | 0.0 | +— / -0a0e7d41-96bf-404f-a3bf-98df0a182b63 |
| Jogador 7 | 6-2 | 229 | BUY | FAST8 | 45.0 | 7 | 170 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8858439326286316 | 0.0 | 0.0 | +e89905aa-6564-4e15-bc3a-c281646446bc / -— |
| Jogador 7 | 6-2 | 230 | SELL | FAST8 | 45.0 | 7 | 168 | 5 | 44.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -5de51369-647a-45bd-95b7-c8efe44c5484 |
| Jogador 7 | 6-3 | 232 | BUY | FAST8 | 45.0 | 7 | 181 | 5 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0137667655944824 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -3c46b699-2b56-48d0-820c-b523c5153b9f,599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 6-3 | 233 | BUY | FAST8 | 45.0 | 7 | 178 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.01247239112854 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -8a52858d-da47-4de9-8e91-8612788cb8fd,f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 6-3 | 234 | MOVE_BENCH | FAST8 | 45.0 | 7 | 175 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4187144339084625 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 235 | BUY | FAST8 | 45.0 | 7 | 175 | 5 | 46.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24017949402332306 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -— |
| Jogador 7 | 6-3 | 236 | BUY | FAST8 | 45.0 | 7 | 172 | 5 | 46.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20128148794174194 | 0.0 | 0.0 | +d79de824-d9b2-4dfb-a7be-a359b416aea1 / -— |
| Jogador 7 | 6-3 | 237 | BUY | FAST8 | 45.0 | 7 | 170 | 5 | 46.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2144964337348938 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -— |
| Jogador 7 | 6-4 | 239 | SELL | FAST8 | 45.0 | 7 | 179 | 5 | 46.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -2b10436d-ccfe-4329-aef8-2769899b3787 |
| Jogador 7 | 6-4 | 240 | BUY | FAST8 | 45.0 | 7 | 187 | 5 | 46.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.1169314906001091 | 0.0 | 0.0 | +46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 / -— |
| Jogador 7 | 6-5 | 242 | EQUIP_FROM_INVENTORY | FAST8 | 45.0 | 7 | 194 | 5 | 46.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07172752916812897 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 243 | EQUIP_FROM_INVENTORY | FAST8 | 45.0 | 7 | 194 | 5 | 46.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05843983218073845 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 244 | SELL | FAST8 | 45.0 | 7 | 194 | 5 | 46.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -aa803972-8af8-46d7-b430-079819730c36 |
| Jogador 7 | 6-5 | 245 | BUY | FAST8 | 45.0 | 7 | 195 | 5 | 46.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014276154339313507 | 0.0 | 0.0 | +9f271ee0-c506-40b7-b3f3-bac209974ba2 / -— |
| Jogador 7 | 6-5 | 246 | SELL | FAST8 | 45.0 | 7 | 194 | 5 | 46.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5978000164031982 | 0.0 | 0.0 | +— / -dc423197-9320-4651-b71d-a62086416f9d |
| Jogador 7 | 6-5 | 247 | BUY | FAST8 | 45.0 | 7 | 202 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23313723504543304 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 7 | 6-5 | 248 | SELL | FAST8 | 45.0 | 7 | 199 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039799999445676804 | 0.0 | 0.0 | +— / -9f271ee0-c506-40b7-b3f3-bac209974ba2 |
| Jogador 7 | 6-6 | 250 | BUY | FAST8 | 45.0 | 7 | 211 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32411637902259827 | 0.0 | 0.0 | +e1be174a-f112-4e1b-8bf6-738af52f27e8 / -— |
| Jogador 7 | 6-7 | 252 | SELL | FAST8 | 45.0 | 7 | 220 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010466666892170906 | 0.0 | 0.0 | +— / -d79de824-d9b2-4dfb-a7be-a359b416aea1 |
| Jogador 7 | 6-7 | 253 | BUY | FAST8 | 45.0 | 7 | 222 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29416999220848083 | 0.0 | 0.0 | +13169f05-0cd0-4012-89a6-7b47246b475e / -— |
| Jogador 7 | 6-7 | 254 | SELL | FAST8 | 45.0 | 7 | 219 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019999999552965164 | 0.0 | 0.0 | +— / -92bac611-1820-42eb-8243-499f20058673 |
| Jogador 7 | 6-7 | 255 | BUY | FAST8 | 45.0 | 7 | 222 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17258240282535553 | 0.0 | 0.0 | +94e47e85-54f4-4546-af6a-3700e3c325a8 / -— |
| Jogador 7 | 6-7 | 256 | SELL | FAST8 | 45.0 | 7 | 219 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008299999870359898 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 6-7 | 257 | BUY | FAST8 | 45.0 | 7 | 222 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06204009801149368 | 0.0 | 0.0 | +158c7931-f8db-44bd-a279-53dd6e59b352 / -— |
| Jogador 7 | 6-7 | 258 | SELL | FAST8 | 45.0 | 7 | 220 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0148415956646204 | 0.0 | 0.0 | +— / -158c7931-f8db-44bd-a279-53dd6e59b352 |
| Jogador 7 | 7-1 | 260 | BUY | FAST8 | 45.0 | 7 | 233 | 5 | 46.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9414641261100769 | 0.0 | 0.0 | +f55e2447-5d65-4f95-9f26-5b9017efefe0 / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0133585929870605 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.360882431268692 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28385138511657715 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9778589010238647 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 36 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17383559048175812 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2516370713710785 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 38 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11586668342351913 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 39 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1140061616897583 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20173077285289764 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18002638220787048 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055928610265254974 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 47 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1035438776016235 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12470517307519913 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 49 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03448481857776642 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 50 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3210981488227844 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 52 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2616599202156067 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 53 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29660776257514954 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 54 | BUY | STABILIZE | 94.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1904657483100891 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 55 | SELL | STABILIZE | 94.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21293824911117554 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-2 | 56 | BUY_XP | STABILIZE | 94.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09122847020626068 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 58 | SELL | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 59 | BUY | STABILIZE | 94.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17306874692440033 | 0.0 | 0.0 | +3c6ac558-6b59-4a97-814e-bff0ff895232 / -— |
| Jogador 8 | 2-2 | 60 | PASS | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 62 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9861928820610046 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 63 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36460915207862854 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 64 | SELL | STABILIZE | 89.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0667666643857956 | 0.0 | 0.0 | +— / -3c6ac558-6b59-4a97-814e-bff0ff895232 |
| Jogador 8 | 2-3 | 65 | SELL | STABILIZE | 89.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-3 | 66 | SELL | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13300000131130219 | 0.0 | 0.0 | +— / -ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 2-3 | 67 | BUY | STABILIZE | 89.0 | 4 | 8 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24791376292705536 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 68 | SELL | STABILIZE | 89.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14536243677139282 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-3 | 69 | SELL | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3335987627506256 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-3 | 70 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 10 | 1 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08348704874515533 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 72 | BUY | STABILIZE | 83.0 | 5 | 17 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18306276202201843 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 73 | BUY | STABILIZE | 83.0 | 5 | 14 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21323414146900177 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05875431001186371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 75 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3469600975513458 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 76 | BUY | STABILIZE | 83.0 | 5 | 13 | 1 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08827269077301025 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 77 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 10 | 1 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06682410836219788 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 78 | BUY_XP | STABILIZE | 83.0 | 5 | 10 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 79 | BUY_XP | STABILIZE | 83.0 | 5 | 6 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 80 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 2-5 | 82 | BUY | STABILIZE | 83.0 | 5 | 11 | 1 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0271296501159668 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 83 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07614735513925552 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 84 | BUY | STABILIZE | 83.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32313933968544006 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 85 | SELL | STABILIZE | 83.0 | 5 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09146422892808914 | 0.0 | 0.0 | +— / -3644801e-2247-403d-8b81-d2d3f15c2f55 |
| Jogador 8 | 2-5 | 86 | SELL | STABILIZE | 83.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42540407180786133 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 2-5 | 87 | BUY_XP | STABILIZE | 83.0 | 5 | 8 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 88 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 89 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.380355566740036 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-5 | 90 | BUY | STABILIZE | 83.0 | 5 | 3 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12230964004993439 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-6 | 92 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24916398525238037 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 93 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4757331907749176 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 94 | BUY | STABILIZE | 83.0 | 6 | 4 | 0 | 22.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20352338254451752 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 95 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 22.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1992843896150589 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 22.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0856911912560463 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 97 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 22.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2648916244506836 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 98 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 99 | PASS | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 101 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34505388140678406 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 102 | BUY | STABILIZE | 83.0 | 6 | 4 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2872447371482849 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 103 | BUY | STABILIZE | 83.0 | 6 | 3 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18002302944660187 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 104 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00013956762268207967 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 105 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497931033372879 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 106 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 107 | PASS | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 111 | BUY | STABILIZE | 83.0 | 6 | 6 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1995263397693634 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 112 | CRAFT_AND_EQUIP | STABILIZE | 83.0 | 6 | 2 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16532255709171295 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 113 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 2 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01823311857879162 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 114 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0625 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 3-1 | 115 | BUY | STABILIZE | 83.0 | 6 | 3 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07347973436117172 | 0.0 | 0.0 | +7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 / -— |
| Jogador 8 | 3-1 | 116 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 1 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01824404112994671 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 117 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 1 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015022363513708115 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 118 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 1 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014749253168702126 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 120 | SELL | STABILIZE | 83.0 | 6 | 8 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 3-3 | 122 | BUY | STABILIZE | 83.0 | 6 | 18 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2849152088165283 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 8 | 3-3 | 123 | SELL | STABILIZE | 83.0 | 6 | 16 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 |
| Jogador 8 | 3-3 | 124 | BUY | STABILIZE | 83.0 | 6 | 18 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24821089208126068 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 125 | SELL | STABILIZE | 83.0 | 6 | 15 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007366666570305824 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 3-3 | 126 | BUY | STABILIZE | 83.0 | 6 | 18 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21797482669353485 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 127 | SELL | STABILIZE | 83.0 | 6 | 17 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04516666755080223 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-4 | 129 | BUY | STABILIZE | 83.0 | 6 | 27 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8529797196388245 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -5de56114-806a-4f58-8241-b3b8434a2154,b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 3-4 | 130 | BUY | STABILIZE | 83.0 | 6 | 26 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1445753574371338 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -— |
| Jogador 8 | 3-5 | 132 | BUY | STABILIZE | 83.0 | 6 | 34 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8218961358070374 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 133 | SELL | STABILIZE | 83.0 | 6 | 32 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -eb7e36f0-cef9-4a2e-979a-f8a357da73e8 |
| Jogador 8 | 3-5 | 134 | BUY | STABILIZE | 83.0 | 6 | 35 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8654693365097046 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -1af578c1-57cf-4752-93e7-d0eebc6e8ae5,9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-5 | 135 | BUY | STABILIZE | 83.0 | 6 | 33 | 3 | 28.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29091334342956543 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 136 | BUY | STABILIZE | 83.0 | 6 | 30 | 3 | 28.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013913317583501339 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 137 | SELL | STABILIZE | 83.0 | 6 | 27 | 2 | 28.0 | Enfeitiçador/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 |
| Jogador 8 | 3-5 | 138 | SELL | STABILIZE | 83.0 | 6 | 32 | 3 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07152316719293594 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 3-6 | 140 | BUY | STABILIZE | 83.0 | 6 | 45 | 4 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8165111541748047 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -— |
| Jogador 8 | 3-7 | 142 | BUY | STABILIZE | 83.0 | 6 | 55 | 5 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9012988805770874 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce,f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 3-7 | 143 | BUY | STABILIZE | 83.0 | 6 | 54 | 5 | 26.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1959044635295868 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 144 | SELL | STABILIZE | 83.0 | 6 | 51 | 5 | 26.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 3-7 | 145 | BUY | STABILIZE | 83.0 | 6 | 54 | 5 | 26.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04064874351024628 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 146 | BUY_XP | STABILIZE | 83.0 | 6 | 51 | 5 | 26.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06504400074481964 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 147 | BUY_XP | STABILIZE | 83.0 | 6 | 47 | 4 | 26.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013344000093638897 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 148 | BUY_XP | STABILIZE | 83.0 | 6 | 43 | 4 | 26.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09334400296211243 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 149 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 39 | 3 | 26.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5511583089828491 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 151 | BUY | STABILIZE | 83.0 | 6 | 50 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.29446107149124146 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 8 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 83.0 | 6 | 49 | 4 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1305084079504013 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 153 | CRAFT_AND_EQUIP | STABILIZE | 83.0 | 6 | 49 | 4 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08391999453306198 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 154 | SELL | STABILIZE | 83.0 | 6 | 49 | 4 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08250000327825546 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 4-1 | 155 | BUY | STABILIZE | 83.0 | 6 | 52 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10183132439851761 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 156 | SELL | STABILIZE | 83.0 | 6 | 50 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 8 | 4-2 | 158 | BUY | STABILIZE | 83.0 | 6 | 66 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8622646927833557 | 0.0 | 0.0 | +7e0c9595-0ca2-44d4-bfe9-3752c7a89e0d / -— |
| Jogador 8 | 4-2 | 159 | SELL | STABILIZE | 83.0 | 6 | 65 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 4-2 | 160 | BUY | STABILIZE | 83.0 | 6 | 68 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10446920245885849 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 8 | 4-3 | 162 | SELL | STABILIZE | 72.0 | 6 | 75 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 8 | 4-3 | 163 | BUY | STABILIZE | 72.0 | 6 | 78 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8519383668899536 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 8 | 4-3 | 164 | SELL | STABILIZE | 72.0 | 6 | 76 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 4-3 | 165 | BUY | STABILIZE | 72.0 | 6 | 79 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7842722535133362 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 166 | SELL | STABILIZE | 72.0 | 6 | 76 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06710382550954819 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-3 | 167 | BUY | STABILIZE | 72.0 | 6 | 79 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35939234495162964 | 0.0 | 0.0 | +579b987a-fedf-45d8-92fc-634a041d3d4f / -— |
| Jogador 8 | 4-3 | 168 | SELL | STABILIZE | 72.0 | 6 | 77 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5398423671722412 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 8 | 4-4 | 170 | BUY | STABILIZE | 60.0 | 7 | 91 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.879124104976654 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 8 | 4-5 | 172 | BUY | STABILIZE | 60.0 | 7 | 100 | 5 | 34.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9610311985015869 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865,e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 8 | 4-5 | 173 | BUY | STABILIZE | 60.0 | 7 | 98 | 5 | 30.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9602680802345276 | 0.0 | 0.0 | +fe12befc-b473-4f91-9e51-558a03efa3ad / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,7e0c9595-0ca2-44d4-bfe9-3752c7a89e0d |
| Jogador 8 | 4-5 | 174 | MOVE_BENCH | STABILIZE | 60.0 | 7 | 97 | 5 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3062226176261902 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 175 | BUY | STABILIZE | 60.0 | 7 | 97 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13024988770484924 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -— |
| Jogador 8 | 4-5 | 176 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 94 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008405588567256927 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 177 | MOVE_BENCH | STABILIZE | 60.0 | 7 | 94 | 5 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3970223069190979 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 178 | MOVE_BOARD | FAST8 | 60.0 | 7 | 94 | 5 | 38.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 180 | BUY | FAST8 | 49.0 | 7 | 105 | 5 | 38.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8922951817512512 | 0.0 | 0.0 | +590d07db-5e90-4705-a7ae-96f84fd06382 / -579b987a-fedf-45d8-92fc-634a041d3d4f,d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 8 | 4-7 | 182 | BUY | STABILIZE | 38.0 | 7 | 114 | 5 | 42.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6181950569152832 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 8 | 4-7 | 183 | BUY | STABILIZE | 38.0 | 7 | 111 | 5 | 42.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8372631669044495 | 0.0 | 0.0 | +0fd34229-b814-4580-8651-59e712d5657f / -3c59d736-011d-480c-a9af-1df7a3b4caab,5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 4-7 | 184 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 108 | 5 | 36.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4964735209941864 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 185 | BUY | STABILIZE | 38.0 | 7 | 108 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01975378952920437 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 8 | 4-7 | 186 | BUY | STABILIZE | 38.0 | 7 | 105 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07333342730998993 | 0.0 | 0.0 | +bcd06176-e1d7-43fb-abd4-b6faea8c7927 / -— |
| Jogador 8 | 4-7 | 187 | BUY | STABILIZE | 38.0 | 7 | 103 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2137620598077774 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -— |
| Jogador 8 | 5-1 | 189 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 113 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12710759043693542 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 190 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 113 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12743917107582092 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 192 | SELL | ALL_IN | 24.0 | 7 | 125 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6766999959945679 | 0.0 | 0.0 | +— / -fe12befc-b473-4f91-9e51-558a03efa3ad |
| Jogador 8 | 5-2 | 193 | BUY | ALL_IN | 24.0 | 7 | 128 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8118206858634949 | 0.0 | 0.0 | +c7762d7d-bcfa-4694-a3fc-038d7242207f / -— |
| Jogador 8 | 5-2 | 194 | EQUIP_FROM_INVENTORY | ALL_IN | 24.0 | 7 | 125 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0782037153840065 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 195 | EQUIP_FROM_INVENTORY | ALL_IN | 24.0 | 7 | 125 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09479667991399765 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 196 | SELL | ALL_IN | 24.0 | 7 | 125 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6793000102043152 | 0.0 | 0.0 | +— / -590d07db-5e90-4705-a7ae-96f84fd06382 |
| Jogador 8 | 5-2 | 197 | BUY | ALL_IN | 24.0 | 7 | 130 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5800192356109619 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 8 | 5-2 | 198 | MOVE_BOARD | ALL_IN | 24.0 | 7 | 127 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006326940841972828 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 200 | SELL | ALL_IN | 24.0 | 7 | 138 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -aaebedb3-18bf-4ae6-948e-7b326b573f1c |
| Jogador 8 | 5-4 | 202 | BUY | ALL_IN | 24.0 | 7 | 149 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0467591285705566 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -9af097e2-729d-474a-9a7e-b266c665c606,b55260cd-3c6a-4cb8-99d0-b7c6471103ad |
| Jogador 8 | 5-4 | 203 | BUY | ALL_IN | 24.0 | 7 | 146 | 5 | 42.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46508705615997314 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 8 | 5-4 | 204 | REROLL | ALL_IN | 24.0 | 7 | 143 | 5 | 42.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 205 | SELL | ALL_IN | 24.0 | 7 | 141 | 5 | 42.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14640000462532043 | 0.0 | 0.0 | +— / -aea521ef-8511-4b98-9c6d-e83b814777df |
| Jogador 8 | 5-4 | 206 | BUY | ALL_IN | 24.0 | 7 | 149 | 5 | 42.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37942102551460266 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 8 | 5-4 | 207 | SELL | ALL_IN | 24.0 | 7 | 146 | 5 | 42.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018835417926311493 | 0.0 | 0.0 | +— / -bcd06176-e1d7-43fb-abd4-b6faea8c7927 |
| Jogador 8 | 5-4 | 208 | MOVE_BENCH | ALL_IN | 24.0 | 7 | 148 | 5 | 42.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40547895431518555 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 210 | BUY | ALL_IN | 24.0 | 7 | 158 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9839540719985962 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -— |
| Jogador 8 | 5-6 | 212 | BUY | ALL_IN | 24.0 | 7 | 169 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9002825021743774 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -— |
| Jogador 8 | 5-6 | 213 | SELL | ALL_IN | 24.0 | 7 | 166 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5233444571495056 | 0.0 | 0.0 | +— / -d30c92eb-1279-4532-b763-7c30826c8430 |
| Jogador 8 | 5-6 | 214 | BUY | ALL_IN | 24.0 | 7 | 169 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4171806573867798 | 0.0 | 0.0 | +caeaaabc-213a-4018-97f3-8797a0711863 / -— |
| Jogador 8 | 5-6 | 215 | SELL | ALL_IN | 24.0 | 7 | 167 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6754000186920166 | 0.0 | 0.0 | +— / -caeaaabc-213a-4018-97f3-8797a0711863 |
| Jogador 8 | 5-6 | 216 | BUY | ALL_IN | 24.0 | 7 | 169 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41721946001052856 | 0.0 | 0.0 | +3ae84928-bc2a-4c1e-8663-b7ad05da4501 / -— |
| Jogador 8 | 5-6 | 217 | SELL | ALL_IN | 24.0 | 7 | 167 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6754000186920166 | 0.0 | 0.0 | +— / -3ae84928-bc2a-4c1e-8663-b7ad05da4501 |
| Jogador 8 | 5-7 | 219 | BUY | ALL_IN | 24.0 | 7 | 181 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8107268214225769 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 8 | 5-7 | 220 | SELL | ALL_IN | 24.0 | 7 | 178 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5354431867599487 | 0.0 | 0.0 | +— / -4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 8 | 6-1 | 222 | BUY | ALL_IN | 24.0 | 7 | 192 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.46217256784439087 | 0.0 | 0.0 | +7d8564c6-8151-4e04-b028-2121cb064215 / -— |
| Jogador 8 | 6-1 | 223 | EQUIP_FROM_INVENTORY | ALL_IN | 24.0 | 7 | 191 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.0011613118695095181 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 224 | SELL | ALL_IN | 24.0 | 7 | 191 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6009261608123779 | 0.0 | 0.0 | +— / -c7762d7d-bcfa-4694-a3fc-038d7242207f |
| Jogador 8 | 6-1 | 225 | BUY | ALL_IN | 24.0 | 7 | 194 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20382097363471985 | 0.0 | 0.0 | +2a2b613e-8850-4c70-ab66-bc18356178e8 / -— |
| Jogador 8 | 6-1 | 226 | SELL | ALL_IN | 24.0 | 7 | 192 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -2a2b613e-8850-4c70-ab66-bc18356178e8 |
| Jogador 8 | 6-2 | 228 | BUY | ALL_IN | 6.0 | 7 | 204 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45279449224472046 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 8 | 6-2 | 229 | SELL | ALL_IN | 6.0 | 7 | 202 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7156345844268799 | 0.0 | 0.0 | +— / -bfe7ca8a-6e89-4673-b142-262e012398a9 |
| Jogador 8 | 6-2 | 230 | BUY | ALL_IN | 6.0 | 7 | 204 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41437020897865295 | 0.0 | 0.0 | +85d35881-ba70-4310-8d5f-bae796309eed / -— |
| Jogador 8 | 6-3 | 232 | SELL | ALL_IN | 6.0 | 7 | 212 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10413026809692383 | 0.0 | 0.0 | +— / -85d35881-ba70-4310-8d5f-bae796309eed |
| Jogador 8 | 6-3 | 233 | BUY | ALL_IN | 6.0 | 7 | 215 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0348149538040161 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 8 | 6-3 | 234 | SELL | ALL_IN | 6.0 | 7 | 212 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6725596785545349 | 0.0 | 0.0 | +— / -40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 8 | 6-3 | 235 | BUY | ALL_IN | 6.0 | 7 | 215 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4307108223438263 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -— |
| Jogador 8 | 6-3 | 236 | SELL | ALL_IN | 6.0 | 7 | 212 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5514706969261169 | 0.0 | 0.0 | +— / -a810e10d-e7ef-4ece-8fb2-8b6471b557ec |
| Jogador 8 | 6-3 | 237 | BUY | ALL_IN | 6.0 | 7 | 215 | 5 | 48.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17918339371681213 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 187 | 205 | 109 | 4 | 9 | 0 | 0 | 0 | 250 | 40.0 |
- Jogador 1 — gasto por ação: BUY: 161g, BUY_XP: 44g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 40g, stage 4: 27g, stage 5: 31g, stage 6: 42g, stage 7: 1g
| Jogador 2 | 132 | 127 | 79 | 4 | 3 | 0 | 0 | 0 | 112 | 28.0 |
- Jogador 2 — gasto por ação: BUY: 115g, BUY_XP: 12g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 59g, stage 3: 40g, stage 4: 21g
| Jogador 3 | 134 | 126 | 68 | 4 | 3 | 0 | 0 | 0 | 139 | 36.0 |
- Jogador 3 — gasto por ação: BUY: 114g, BUY_XP: 12g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 39g, stage 3: 31g, stage 4: 42g, stage 5: 7g
| Jogador 4 | 122 | 126 | 56 | 4 | 6 | 1 | 2 | 0 | 77 | 28.0 |
- Jogador 4 — gasto por ação: BUY: 90g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 34g, stage 4: 28g
| Jogador 5 | 144 | 167 | 83 | 5 | 8 | 1 | 3 | 0 | 117 | 28.0 |
- Jogador 5 — gasto por ação: BUY: 117g, BUY_XP: 44g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 6g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 61g, stage 3: 45g, stage 4: 33g, stage 5: 21g
| Jogador 6 | 138 | 172 | 70 | 7 | 10 | 0 | 1 | 0 | 80 | 34.0 |
- Jogador 6 — gasto por ação: BUY: 126g, BUY_XP: 44g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 69g, stage 3: 51g, stage 4: 39g, stage 5: 8g
| Jogador 7 | 183 | 199 | 105 | 4 | 8 | 1 | 0 | 0 | 230 | 46.0 |
- Jogador 7 — gasto por ação: BUY: 159g, BUY_XP: 40g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 50g, stage 3: 35g, stage 4: 39g, stage 5: 25g, stage 6: 41g, stage 7: 3g
| Jogador 8 | 181 | 199 | 109 | 6 | 8 | 0 | 1 | 0 | 211 | 48.0 |
- Jogador 8 — gasto por ação: BUY: 165g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 64g, stage 3: 46g, stage 4: 36g, stage 5: 28g, stage 6: 18g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 11 | 1 |
- Jogador 1 · 3-7 · step 145: PASS com 15g, HP 81, nível 7/8 (STABILIZE).
| Jogador 2 | 3 | 0 |
| Jogador 3 | 3 | 3 |
- Jogador 3 · 2-6 · step 98: PASS com 5g, HP 89, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 107: PASS com 7g, HP 84, nível 5/8 (STABILIZE).
- Jogador 3 · 3-5 · step 138: PASS com 33g, HP 63, nível 6/8 (STABILIZE).
| Jogador 4 | 8 | 3 |
- Jogador 4 · 3-5 · step 136: PASS com 14g, HP 64, nível 6/8 (STABILIZE).
- Jogador 4 · 4-5 · step 174: REROLL com 77g, HP 7, nível 7/8 (ALL_IN).
- Jogador 4 · 4-5 · step 177: REROLL com 75g, HP 7, nível 7/8 (ALL_IN).
| Jogador 5 | 11 | 5 |
- Jogador 5 · 3-7 · step 145: PASS com 10g, HP 64, nível 7/8 (STABILIZE).
- Jogador 5 · 4-5 · step 177: PASS com 49g, HP 52, nível 7/8 (STABILIZE).
- Jogador 5 · 4-7 · step 185: REROLL com 69g, HP 28, nível 7/8 (STABILIZE).
- Jogador 5 · 5-2 · step 197: REROLL com 87g, HP 28, nível 7/8 (STABILIZE).
- Jogador 5 · 5-4 · step 204: REROLL com 108g, HP 13, nível 7/8 (ALL_IN).
| Jogador 6 | 11 | 3 |
- Jogador 6 · 3-7 · step 148: PASS com 8g, HP 60, nível 7/8 (STABILIZE).
- Jogador 6 · 4-3 · step 165: REROLL com 28g, HP 38, nível 7/8 (STABILIZE).
- Jogador 6 · 5-2 · step 197: PASS com 73g, HP 24, nível 7/8 (ALL_IN).
| Jogador 7 | 10 | 1 |
- Jogador 7 · 4-3 · step 167: PASS com 28g, HP 74, nível 7/8 (FAST8).
| Jogador 8 | 8 | 1 |
- Jogador 8 · 5-4 · step 204: REROLL com 143g, HP 24, nível 7/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 2 | 1 | 1 | 50.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 187 | 37 | 35 | 115 | 0.0018 | 0.4047 | 0.0002 | 0.2841 | 0.0016 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0228 (72 ações), BUY_XP: Δ 0.0089 (11 ações), CRAFT_AND_EQUIP: Δ 0.0020 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (5 ações), MOVE_BENCH: Δ -0.0202 (16 ações), MOVE_BOARD: Δ 0.0565 (30 ações), PASS: Δ 0.0000 (11 ações), SELL: Δ 0.0141 (35 ações)
| Jogador 2 | 132 | 14 | 20 | 98 | -0.0000 | 0.0114 | -0.0011 | 0.3238 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0051 (59 ações), BUY_XP: Δ 0.0000 (3 ações), CRAFT_AND_EQUIP: Δ 0.0014 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0139 (9 ações), MOVE_BOARD: Δ -0.0010 (13 ações), PASS: Δ 0.0000 (5 ações), SELL: Δ 0.0051 (35 ações)
| Jogador 3 | 134 | 26 | 26 | 82 | 0.0024 | 0.1698 | 0.0013 | 0.2443 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0067 (52 ações), BUY_XP: Δ 0.0000 (3 ações), CRAFT_AND_EQUIP: Δ 0.0149 (7 ações), MOVE_BENCH: Δ 0.0165 (19 ações), MOVE_BOARD: Δ -0.0027 (20 ações), PASS: Δ 0.0000 (10 ações), SELL: Δ 0.0131 (23 ações)
| Jogador 4 | 122 | 23 | 21 | 78 | 0.0039 | -0.0196 | 0.0014 | 0.4187 | 0.0025 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0079 (47 ações), BUY_XP: Δ 0.0135 (8 ações), CRAFT_AND_EQUIP: Δ 0.0028 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0111 (13 ações), MOVE_BOARD: Δ 0.0238 (12 ações), PASS: Δ 0.0000 (9 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0127 (23 ações)
| Jogador 5 | 144 | 21 | 19 | 104 | 0.0065 | 0.0758 | 0.0043 | 0.4012 | 0.0022 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0115 (58 ações), BUY_XP: Δ 0.0128 (11 ações), CRAFT_AND_EQUIP: Δ 0.0205 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0095 (9 ações), MOVE_BOARD: Δ 0.0628 (13 ações), PASS: Δ 0.0000 (8 ações), REROLL: Δ 0.0000 (3 ações), SELL: Δ 0.0124 (34 ações)
| Jogador 6 | 138 | 30 | 30 | 78 | 0.0003 | -0.5974 | -0.0014 | 0.4772 | 0.0016 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0281 (53 ações), BUY_XP: Δ 0.0024 (11 ações), CRAFT_AND_EQUIP: Δ 0.0830 (7 ações), MOVE_BENCH: Δ 0.0863 (15 ações), MOVE_BOARD: Δ -0.0491 (15 ações), PASS: Δ 0.0000 (9 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0134 (27 ações)
| Jogador 7 | 183 | 37 | 28 | 118 | 0.0064 | 0.1748 | 0.0041 | 0.4270 | 0.0023 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0247 (71 ações), BUY_XP: Δ 0.0096 (10 ações), CRAFT_AND_EQUIP: Δ -0.0470 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0288 (12 ações), MOVE_BENCH: Δ 0.1004 (11 ações), MOVE_BOARD: Δ 0.0373 (28 ações), PASS: Δ 0.0000 (12 ações), SELL: Δ 0.0207 (32 ações)
| Jogador 8 | 181 | 34 | 24 | 123 | 0.0018 | 0.0242 | 0.0010 | 0.4072 | 0.0008 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0134 (79 ações), BUY_XP: Δ 0.0000 (8 ações), CRAFT_AND_EQUIP: Δ 0.0030 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0487 (15 ações), MOVE_BOARD: Δ 0.0059 (17 ações), PASS: Δ 0.0000 (7 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0120 (44 ações)
- Jogador 1 — rounds avaliados: 39; correlação estrutural/combate: 0.217; posicional/combate: 0.026.
- Jogador 1 — combate positive: score estrutural prévio 0.477
  score posicional prévio 0.286
- Jogador 1 — combate negative: score estrutural prévio 0.292
  score posicional prévio 0.291
- Jogador 2 — rounds avaliados: 23; correlação estrutural/combate: -0.366; posicional/combate: 0.010.
- Jogador 2 — combate positive: score estrutural prévio -0.150
  score posicional prévio 0.301
- Jogador 2 — combate negative: score estrutural prévio 0.101
  score posicional prévio 0.315
- Jogador 3 — rounds avaliados: 27; correlação estrutural/combate: -0.002; posicional/combate: 0.032.
- Jogador 3 — combate positive: score estrutural prévio 0.131
  score posicional prévio 0.260
- Jogador 3 — combate negative: score estrutural prévio 0.143
  score posicional prévio 0.248
- Jogador 4 — rounds avaliados: 23; correlação estrutural/combate: 0.459; posicional/combate: -0.403.
- Jogador 4 — combate positive: score estrutural prévio 0.101
  score posicional prévio 0.372
- Jogador 4 — combate negative: score estrutural prévio -0.085
  score posicional prévio 0.498
- Jogador 5 — rounds avaliados: 30; correlação estrutural/combate: -0.214; posicional/combate: -0.165.
- Jogador 5 — combate positive: score estrutural prévio 0.056
  score posicional prévio 0.415
- Jogador 5 — combate negative: score estrutural prévio 0.156
  score posicional prévio 0.463
- Jogador 6 — rounds avaliados: 28; correlação estrutural/combate: 0.194; posicional/combate: -0.210.
- Jogador 6 — combate positive: score estrutural prévio -0.198
  score posicional prévio 0.425
- Jogador 6 — combate negative: score estrutural prévio -0.502
  score posicional prévio 0.479
- Jogador 7 — rounds avaliados: 39; correlação estrutural/combate: -0.044; posicional/combate: -0.013.
- Jogador 7 — combate positive: score estrutural prévio 0.160
  score posicional prévio 0.446
- Jogador 7 — combate negative: score estrutural prévio 0.143
  score posicional prévio 0.478
- Jogador 8 — rounds avaliados: 35; correlação estrutural/combate: 0.444; posicional/combate: -0.169.
- Jogador 8 — combate positive: score estrutural prévio 0.444
  score posicional prévio 0.402
- Jogador 8 — combate negative: score estrutural prévio -0.096
  score posicional prévio 0.428

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 226 | OK (226) | 8 | 0 | 1 | 0 | 8 | 3 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Crownguard, TFT_Item_Deathblade, TFT_Item_JeweledGauntlet, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_SpectralGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 154 | OK (154) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 2 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_Crownguard, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RunaansHurricane; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 160 | OK (160) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_RedBuff, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 144 | OK (144) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 173 | OK (173) | 7 | 0 | 0 | 0 | 7 | 1 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_GuinsoosRageblade, TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 165 | OK (165) | 4 | 3 | 0 | 0 | 7 | 0 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 222 | OK (222) | 8 | 0 | 1 | 0 | 8 | 3 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 215 | OK (215) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 8 — IDs equipados observados: DA_18_EmblemHunter, TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_InfinityEdge, TFT_Item_LastWhisper, TFT_Item_Morellonomicon, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.002 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.014 | 0.427 |
| Jogador 1 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 8 | 9 | 4 → 5 | -0.027 | 0.269 |
| Jogador 1 | 2-3 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 18% | 8 → 7 | 11 | 5 → 5 | 0.000 | 0.320 |
| Jogador 1 | 2-4 | 10 | 2.000 | 8.000 | 0 → 0 | 3 → 2 | 18% → 18% | 7 → 7 | 6 | 5 → 5 | 0.057 | 0.000 |
| Jogador 1 | 2-5 | 10 | 4.000 | -4.000 | 0 → 0 | 2 → 3 | 18% → 21% | 7 → 7 | 12 | 5 → 6 | 0.042 | 0.285 |
| Jogador 1 | 2-6 | 8 | 4.000 | 8.000 | 0 → 0 | 3 → 2 | 21% → 21% | 7 → 8 | 7 | 6 → 6 | -0.000 | 0.330 |
| Jogador 1 | 2-7 | 10 | 4.000 | 6.000 | 0 → 1 | 2 → 2 | 21% → 21% | 8 → 10 | 8 | 6 → 6 | 0.004 | 0.000 |
| Jogador 1 | 3-1 | 6 | 0.000 | 14.000 | 1 → 1 | 2 → 2 | 21% → 21% | 10 → 12 | 7 | 6 → 6 | 0.000 | 0.460 |
| Jogador 1 | 3-2 | 2 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 12 → 23 | 0 | 6 → 6 | 0.000 | 1.450 |
| Jogador 1 | 3-3 | 7 | 0.000 | 4.000 | 1 → 1 | 2 → 3 | 21% → 21% | 23 → 6 | 22 | 6 → 6 | 0.000 | -0.383 |
| Jogador 1 | 3-4 | 3 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 6 → 12 | 1 | 6 → 7 | 0.016 | 0.000 |
| Jogador 1 | 3-5 | 8 | 6.000 | -2.000 | 1 → 1 | 3 → 2 | 21% → 25% | 12 → 14 | 5 | 7 → 7 | -0.003 | 0.385 |
| Jogador 1 | 3-6 | 2 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 25% → 25% | 14 → 18 | 2 | 7 → 7 | 0.000 | -1.269 |
| Jogador 1 | 3-7 | 5 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 18 → 21 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-1 | 7 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 25% → 25% | 21 → 31 | 3 | 7 → 7 | -0.129 | 0.414 |
| Jogador 1 | 4-2 | 4 | 0.000 | -10.000 | 1 → 1 | 4 → 4 | 25% → 25% | 31 → 46 | 1 | 7 → 7 | 0.000 | 0.713 |
| Jogador 1 | 4-3 | 8 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 25% → 25% | 46 → 54 | 4 | 7 → 7 | 0.055 | 0.367 |
| Jogador 1 | 4-4 | 2 | 0.000 | -6.000 | 1 → 1 | 4 → 4 | 25% → 25% | 54 → 68 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 8 | 0.000 | 8.000 | 1 → 1 | 4 → 4 | 25% → 25% | 68 → 76 | 11 | 7 → 7 | 0.072 | 0.376 |
| Jogador 1 | 4-6 | 2 | 0.000 | -8.000 | 1 → 1 | 4 → 4 | 25% → 25% | 76 → 93 | 0 | 7 → 7 | 0.000 | 1.492 |
| Jogador 1 | 4-7 | 7 | 0.000 | 10.000 | 1 → 1 | 4 → 3 | 25% → 25% | 93 → 97 | 8 | 7 → 7 | -0.004 | 0.000 |
| Jogador 1 | 5-1 | 3 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 97 → 111 | 0 | 7 → 7 | 0.000 | 1.024 |
| Jogador 1 | 5-2 | 8 | 0.000 | -14.000 | 1 → 1 | 3 → 4 | 25% → 25% | 111 → 134 | 7 | 7 → 7 | 0.008 | 0.384 |
| Jogador 1 | 5-3 | 2 | 0.000 | 2.000 | 1 → 1 | 4 → 5 | 25% → 25% | 134 → 147 | 1 | 7 → 7 | 0.000 | 1.528 |
| Jogador 1 | 5-4 | 8 | 2.000 | -8.000 | 1 → 1 | 5 → 5 | 25% → 25% | 147 → 162 | 5 | 7 → 7 | -0.078 | 0.000 |
| Jogador 1 | 5-5 | 2 | 0.000 | 10.000 | 1 → 1 | 5 → 5 | 25% → 25% | 162 → 171 | 5 | 7 → 7 | 0.000 | 1.493 |
| Jogador 1 | 5-6 | 7 | 4.000 | -8.000 | 1 → 2 | 5 → 2 | 25% → 21% | 171 → 177 | 7 | 7 → 7 | -0.035 | -0.407 |
| Jogador 1 | 5-7 | 3 | 6.000 | 6.000 | 2 → 2 | 2 → 2 | 21% → 25% | 177 → 181 | 6 | 7 → 7 | -0.007 | 0.000 |
| Jogador 1 | 6-1 | 6 | 0.000 | 18.000 | 2 → 2 | 2 → 4 | 25% → 25% | 181 → 183 | 9 | 7 → 7 | 0.005 | 0.499 |
| Jogador 1 | 6-2 | 4 | -2.000 | -10.000 | 2 → 3 | 4 → 2 | 25% → 25% | 183 → 197 | 4 | 7 → 7 | -0.040 | -0.700 |
| Jogador 1 | 6-3 | 7 | 0.000 | 16.000 | 3 → 3 | 2 → 2 | 25% → 25% | 197 → 200 | 8 | 7 → 7 | 0.000 | 0.434 |
| Jogador 1 | 6-4 | 3 | 0.000 | -6.000 | 3 → 3 | 2 → 2 | 25% → 25% | 200 → 215 | 3 | 7 → 7 | 0.020 | 0.000 |
| Jogador 1 | 6-5 | 8 | 0.000 | 4.000 | 3 → 3 | 2 → 2 | 25% → 25% | 215 → 224 | 10 | 7 → 7 | 0.006 | -0.363 |
| Jogador 1 | 6-6 | 2 | 0.000 | -4.000 | 3 → 3 | 2 → 2 | 25% → 25% | 224 → 237 | 0 | 7 → 7 | 0.000 | -1.450 |
| Jogador 1 | 6-7 | 8 | 0.000 | -6.000 | 3 → 3 | 2 → 4 | 25% → 25% | 237 → 251 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 7-1 | 1 | 0.000 | 2.000 | 3 → 3 | 4 → 4 | 25% → 25% | 251 → 250 | 1 | 7 → 7 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 22, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 16; mudanças de composição: 1; posicionamento melhorou em 41 ações e piorou em 38.
- Jogador 1 — estado final: ouro 250, nível 7, vida 12.0, colocação None.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.131 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 9 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | -0.003 | -0.257 |
| Jogador 2 | 2-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.023 | -0.253 |
| Jogador 2 | 2-3 | 6 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 14% → 14% | 6 → 7 | 6 | 4 → 5 | 0.008 | -0.404 |
| Jogador 2 | 2-4 | 10 | 2.000 | 8.000 | 1 → 1 | 1 → 2 | 14% → 18% | 7 → 8 | 8 | 5 → 5 | -0.037 | 0.000 |
| Jogador 2 | 2-5 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 8 → 7 | 14 | 5 → 5 | -0.000 | -0.253 |
| Jogador 2 | 2-6 | 9 | 0.000 | -10.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 14 | 10 | 5 → 5 | 0.000 | 0.279 |
| Jogador 2 | 2-7 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 14 → 22 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 2 | 3-1 | 9 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 22 → 31 | 6 | 5 → 5 | 0.000 | -0.324 |
| Jogador 2 | 3-2 | 2 | 2.000 | -2.000 | 1 → 2 | 2 → 1 | 18% → 18% | 31 → 39 | 1 | 5 → 6 | 0.038 | -1.438 |
| Jogador 2 | 3-3 | 7 | 6.000 | 14.000 | 2 → 2 | 1 → 2 | 18% → 21% | 39 → 38 | 10 | 6 → 6 | -0.039 | 0.395 |
| Jogador 2 | 3-4 | 3 | 0.000 | 8.000 | 2 → 2 | 2 → 2 | 21% → 21% | 38 → 42 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-5 | 8 | 0.000 | 6.000 | 2 → 2 | 2 → 3 | 21% → 21% | 42 → 47 | 6 | 6 → 6 | 0.087 | -0.341 |
| Jogador 2 | 3-6 | 2 | 0.000 | 2.000 | 2 → 2 | 3 → 3 | 21% → 21% | 47 → 56 | 1 | 6 → 6 | -0.001 | -1.341 |
| Jogador 2 | 3-7 | 9 | 0.000 | -2.000 | 2 → 2 | 3 → 2 | 21% → 21% | 56 → 67 | 12 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 7 | 0.000 | 4.000 | 2 → 2 | 2 → 3 | 21% → 21% | 67 → 76 | 5 | 6 → 6 | 0.001 | -0.369 |
| Jogador 2 | 4-2 | 4 | 8.000 | -14.000 | 2 → 2 | 3 → 2 | 21% → 21% | 76 → 89 | 1 | 6 → 6 | -0.144 | -0.656 |
| Jogador 2 | 4-3 | 8 | 0.000 | 10.000 | 2 → 2 | 2 → 2 | 21% → 21% | 89 → 97 | 7 | 6 → 6 | 0.007 | -0.341 |
| Jogador 2 | 4-4 | 2 | 0.000 | -4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 97 → 111 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 8 | -28.000 | -42.000 | 2 → 0 | 2 → 0 | 21% → 0% | 111 → 112 | 8 | 6 → 6 | -0.030 | -0.356 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 8; mudanças de composição: 0; posicionamento melhorou em 19 ações e piorou em 22.
- Jogador 2 — estado final: ouro 112, nível 6, vida 3.0, colocação 8.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.070 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 9 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.004 | 0.290 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.684 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 6 | 7 | 4 → 5 | 0.006 | -0.484 |
| Jogador 3 | 2-4 | 4 | 4.000 | -2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 6 → 6 | 5 | 5 → 5 | 0.026 | 0.000 |
| Jogador 3 | 2-5 | 10 | 2.000 | -8.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 10 | 7 | 5 → 5 | -0.027 | -0.253 |
| Jogador 3 | 2-6 | 8 | 2.000 | 6.000 | 1 → 2 | 2 → 1 | 18% → 18% | 10 → 11 | 5 | 5 → 5 | 0.002 | -0.296 |
| Jogador 3 | 2-7 | 8 | 0.000 | 8.000 | 2 → 2 | 1 → 3 | 18% → 18% | 11 → 13 | 6 | 5 → 5 | 0.006 | 0.000 |
| Jogador 3 | 3-1 | 9 | 0.000 | -10.000 | 2 → 1 | 3 → 2 | 18% → 18% | 13 → 26 | 1 | 5 → 5 | -0.001 | -0.293 |
| Jogador 3 | 3-2 | 2 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 26 → 32 | 3 | 5 → 6 | 0.024 | -1.363 |
| Jogador 3 | 3-3 | 7 | 12.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 21% | 32 → 31 | 9 | 6 → 6 | 0.038 | 0.388 |
| Jogador 3 | 3-4 | 3 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 31 → 35 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 3-5 | 8 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 35 → 41 | 7 | 6 → 6 | 0.000 | -0.317 |
| Jogador 3 | 3-6 | 2 | 0.000 | -6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 41 → 54 | 0 | 6 → 6 | 0.000 | -1.316 |
| Jogador 3 | 3-7 | 9 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 54 → 64 | 8 | 6 → 6 | -0.010 | 0.000 |
| Jogador 3 | 4-1 | 7 | 0.000 | 4.000 | 1 → 1 | 2 → 3 | 21% → 21% | 64 → 73 | 7 | 6 → 6 | 0.000 | 0.395 |
| Jogador 3 | 4-2 | 4 | 0.000 | -6.000 | 1 → 1 | 3 → 4 | 21% → 21% | 73 → 88 | 2 | 6 → 6 | 0.000 | 0.733 |
| Jogador 3 | 4-3 | 8 | 0.000 | 8.000 | 1 → 1 | 4 → 4 | 21% → 21% | 88 → 94 | 13 | 6 → 6 | 0.000 | -0.339 |
| Jogador 3 | 4-4 | 2 | 0.000 | -8.000 | 1 → 1 | 4 → 4 | 21% → 21% | 94 → 108 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 8 | -4.000 | 16.000 | 1 → 1 | 4 → 4 | 21% → 21% | 108 → 110 | 10 | 6 → 6 | -0.100 | 0.367 |
| Jogador 3 | 4-6 | 2 | 0.000 | -12.000 | 1 → 1 | 4 → 4 | 21% → 21% | 110 → 128 | 0 | 6 → 6 | 0.030 | -1.407 |
| Jogador 3 | 4-7 | 7 | 4.000 | 8.000 | 1 → 2 | 4 → 2 | 21% → 21% | 128 → 128 | 10 | 6 → 6 | 0.085 | 0.000 |
| Jogador 3 | 5-1 | 3 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 128 → 137 | 2 | 6 → 6 | 0.010 | -0.967 |
| Jogador 3 | 5-2 | 8 | -32.000 | -52.000 | 2 → 0 | 2 → 0 | 21% → 0% | 137 → 139 | 5 | 6 → 6 | -0.055 | -0.363 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 10; mudanças de composição: 1; posicionamento melhorou em 31 ações e piorou em 28.
- Jogador 3 — estado final: ouro 139, nível 6, vida 4.0, colocação 6.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.076 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.021 | -0.404 |
| Jogador 4 | 2-2 | 4 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.034 | 0.684 |
| Jogador 4 | 2-3 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 6 → 9 | 9 | 5 → 5 | 0.005 | 0.269 |
| Jogador 4 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 10 | 12 | 5 → 5 | -0.013 | 0.000 |
| Jogador 4 | 2-5 | 10 | 6.000 | -2.000 | 0 → 0 | 3 → 2 | 18% → 21% | 10 → 5 | 14 | 5 → 6 | -0.003 | -0.232 |
| Jogador 4 | 2-6 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 5 → 8 | 3 | 6 → 6 | 0.019 | -0.354 |
| Jogador 4 | 2-7 | 10 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 9 | 10 | 6 → 6 | 0.009 | 0.000 |
| Jogador 4 | 3-1 | 9 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 11 | 11 | 6 → 6 | -0.000 | 0.312 |
| Jogador 4 | 3-2 | 2 | 2.000 | -2.000 | 0 → 0 | 3 → 2 | 21% → 21% | 11 → 16 | 1 | 6 → 6 | -0.149 | -1.388 |
| Jogador 4 | 3-3 | 7 | 2.000 | 8.000 | 0 → 0 | 2 → 1 | 21% → 21% | 16 → 15 | 7 | 6 → 6 | 0.031 | -0.370 |
| Jogador 4 | 3-4 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 2 | 21% → 21% | 15 → 18 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 3-5 | 6 | -2.000 | 10.000 | 0 → 0 | 2 → 4 | 21% → 21% | 18 → 21 | 4 | 6 → 6 | -0.019 | -0.486 |
| Jogador 4 | 3-6 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 3 | 21% → 21% | 21 → 26 | 2 | 6 → 6 | -0.030 | -1.316 |
| Jogador 4 | 3-7 | 9 | 2.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 26 → 32 | 5 | 6 → 6 | -0.002 | 0.000 |
| Jogador 4 | 4-1 | 7 | 0.000 | -10.000 | 0 → 0 | 3 → 4 | 21% → 21% | 32 → 49 | 3 | 6 → 6 | 0.017 | -0.389 |
| Jogador 4 | 4-2 | 4 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 49 → 59 | 3 | 6 → 6 | -0.001 | -0.691 |
| Jogador 4 | 4-3 | 8 | -2.000 | 8.000 | 0 → 0 | 4 → 4 | 21% → 21% | 59 → 69 | 8 | 6 → 7 | 0.002 | -0.346 |
| Jogador 4 | 4-4 | 2 | 4.000 | -8.000 | 0 → 0 | 4 → 4 | 21% → 25% | 69 → 84 | 0 | 7 → 7 | -0.052 | 0.000 |
| Jogador 4 | 4-5 | 8 | -28.000 | -32.000 | 0 → 0 | 4 → 0 | 25% → 0% | 84 → 77 | 14 | 7 → 7 | -0.043 | -0.346 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 12, COMPOSITION_COMPATIBILITY: 16, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 28 ações e piorou em 26.
- Jogador 4 — estado final: ouro 77, nível 7, vida 7.0, colocação 7.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.021 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.347 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 5 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 7 | 11 | 4 → 5 | -0.007 | 0.256 |
| Jogador 5 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 8 | 12 | 5 → 5 | 0.006 | 0.000 |
| Jogador 5 | 2-5 | 10 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 8 → 7 | 12 | 5 → 6 | -0.010 | 0.269 |
| Jogador 5 | 2-6 | 9 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 8 | 9 | 6 → 6 | 0.015 | -0.281 |
| Jogador 5 | 2-7 | 10 | -2.000 | 8.000 | 0 → 0 | 1 → 1 | 21% → 21% | 8 → 6 | 8 | 6 → 6 | 0.042 | 0.000 |
| Jogador 5 | 3-1 | 9 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 6 | 11 | 6 → 6 | 0.000 | -0.287 |
| Jogador 5 | 3-2 | 2 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 6 → 9 | 3 | 6 → 6 | 0.000 | 1.475 |
| Jogador 5 | 3-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 7 | 12 | 6 → 6 | 0.000 | -0.362 |
| Jogador 5 | 3-4 | 3 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 12 | 2 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 8 | 4.000 | 4.000 | 0 → 0 | 3 → 2 | 21% → 21% | 12 → 10 | 11 | 6 → 7 | -0.007 | -0.353 |
| Jogador 5 | 3-6 | 2 | 6.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 25% | 10 → 13 | 3 | 7 → 7 | -0.068 | 1.358 |
| Jogador 5 | 3-7 | 5 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 13 → 16 | 3 | 7 → 7 | -0.016 | 0.000 |
| Jogador 5 | 4-1 | 7 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 16 → 22 | 5 | 7 → 7 | 0.004 | -0.395 |
| Jogador 5 | 4-2 | 4 | 0.000 | 8.000 | 0 → 0 | 4 → 3 | 25% → 25% | 22 → 22 | 7 | 7 → 7 | -0.015 | 0.700 |
| Jogador 5 | 4-3 | 8 | 0.000 | -16.000 | 0 → 0 | 3 → 4 | 25% → 25% | 22 → 42 | 7 | 7 → 7 | 0.007 | 0.360 |
| Jogador 5 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 3 | 25% → 25% | 42 → 51 | 1 | 7 → 7 | -0.030 | 0.000 |
| Jogador 5 | 4-5 | 7 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 51 → 58 | 2 | 7 → 7 | 0.023 | -0.419 |
| Jogador 5 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 2 | 25% → 25% | 58 → 66 | 3 | 7 → 7 | -0.030 | -1.291 |
| Jogador 5 | 4-7 | 7 | 0.000 | -4.000 | 0 → 0 | 2 → 3 | 25% → 25% | 66 → 80 | 8 | 7 → 7 | 0.017 | 0.000 |
| Jogador 5 | 5-1 | 3 | 0.000 | 2.000 | 0 → 0 | 3 → 4 | 25% → 25% | 80 → 90 | 1 | 7 → 7 | 0.000 | 0.995 |
| Jogador 5 | 5-2 | 8 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 90 → 100 | 7 | 7 → 7 | 0.015 | 0.376 |
| Jogador 5 | 5-3 | 2 | 0.000 | 10.000 | 0 → 0 | 4 → 4 | 25% → 25% | 100 → 105 | 5 | 7 → 7 | 0.000 | -1.450 |
| Jogador 5 | 5-4 | 8 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 105 → 114 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 2 | -28.000 | -44.000 | 0 → 0 | 4 → 0 | 25% → 0% | 114 → 117 | 0 | 7 → 7 | -0.382 | -1.416 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 18, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 13; mudanças de composição: 1; posicionamento melhorou em 23 ações e piorou em 22.
- Jogador 5 — estado final: ouro 117, nível 7, vida 13.0, colocação 4.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 4 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.084 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.021 | -0.412 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 14% → 14% | 9 → 10 | 13 | 5 → 5 | 0.006 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | -12.000 | 0 → 0 | 3 → 4 | 14% → 18% | 10 → 9 | 15 | 5 → 6 | 0.052 | -0.269 |
| Jogador 6 | 2-6 | 9 | 2.000 | 0.000 | 0 → 0 | 4 → 3 | 18% → 21% | 9 → 7 | 13 | 6 → 6 | 0.019 | -0.281 |
| Jogador 6 | 2-7 | 10 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 8 | 11 | 6 → 6 | 0.007 | 0.000 |
| Jogador 6 | 3-1 | 9 | 4.000 | -4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 6 | 15 | 6 → 6 | 0.018 | 0.343 |
| Jogador 6 | 3-2 | 2 | 2.000 | -2.000 | 0 → 1 | 3 → 2 | 21% → 21% | 6 → 10 | 1 | 6 → 6 | 0.012 | -1.341 |
| Jogador 6 | 3-3 | 7 | 0.000 | 12.000 | 1 → 1 | 2 → 2 | 21% → 21% | 10 → 10 | 8 | 6 → 6 | -0.003 | 0.409 |
| Jogador 6 | 3-4 | 3 | 0.000 | 12.000 | 1 → 1 | 2 → 3 | 21% → 21% | 10 → 9 | 6 | 6 → 7 | 0.012 | 0.000 |
| Jogador 6 | 3-5 | 8 | 6.000 | 12.000 | 1 → 1 | 3 → 5 | 21% → 25% | 9 → 7 | 9 | 7 → 7 | -0.004 | 0.375 |
| Jogador 6 | 3-6 | 2 | 0.000 | 6.000 | 1 → 1 | 5 → 6 | 25% → 25% | 7 → 11 | 3 | 7 → 7 | 0.000 | 1.406 |
| Jogador 6 | 3-7 | 8 | 0.000 | 6.000 | 1 → 1 | 6 → 6 | 25% → 25% | 11 → 14 | 9 | 7 → 7 | 0.001 | 0.000 |
| Jogador 6 | 4-1 | 7 | 0.000 | 0.000 | 1 → 1 | 6 → 5 | 25% → 25% | 14 → 17 | 7 | 7 → 7 | -0.009 | -0.389 |
| Jogador 6 | 4-2 | 4 | 0.000 | -8.000 | 1 → 1 | 5 → 5 | 25% → 25% | 17 → 31 | 3 | 7 → 7 | 0.016 | -0.681 |
| Jogador 6 | 4-3 | 8 | 0.000 | -2.000 | 1 → 1 | 5 → 5 | 25% → 25% | 31 → 39 | 9 | 7 → 7 | 0.000 | 0.363 |
| Jogador 6 | 4-4 | 2 | 0.000 | 4.000 | 1 → 1 | 5 → 5 | 25% → 25% | 39 → 45 | 2 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 8 | 8.000 | -12.000 | 1 → 1 | 5 → 4 | 25% → 25% | 45 → 57 | 5 | 7 → 7 | 0.009 | 0.356 |
| Jogador 6 | 4-6 | 2 | 0.000 | 6.000 | 1 → 1 | 4 → 5 | 25% → 25% | 57 → 66 | 3 | 7 → 7 | 0.000 | 1.450 |
| Jogador 6 | 4-7 | 7 | 2.000 | 6.000 | 1 → 2 | 5 → 3 | 25% → 25% | 66 → 67 | 10 | 7 → 7 | -0.040 | 0.000 |
| Jogador 6 | 5-1 | 3 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 67 → 77 | 0 | 7 → 7 | 0.194 | -0.944 |
| Jogador 6 | 5-2 | 8 | 0.000 | 0.000 | 2 → 3 | 3 → 1 | 25% → 21% | 77 → 84 | 4 | 7 → 7 | -0.004 | -0.348 |
| Jogador 6 | 5-3 | 2 | -34.000 | -46.000 | 3 → 0 | 1 → 0 | 21% → 0% | 84 → 80 | 4 | 7 → 7 | -0.279 | -1.366 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 14, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 9; mudanças de composição: 0; posicionamento melhorou em 37 ações e piorou em 32.
- Jogador 6 — estado final: ouro 80, nível 7, vida 10.0, colocação 5.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.048 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 6 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.016 | 0.456 |
| Jogador 7 | 2-2 | 10 | -2.000 | 4.000 | 0 → 0 | 3 → 2 | 14% → 11% | 8 → 8 | 8 | 4 → 4 | 0.015 | -0.258 |
| Jogador 7 | 2-3 | 9 | 10.000 | -6.000 | 0 → 0 | 2 → 2 | 11% → 14% | 8 → 8 | 9 | 4 → 5 | 0.056 | 0.304 |
| Jogador 7 | 2-4 | 4 | 6.000 | 8.000 | 0 → 0 | 2 → 2 | 14% → 18% | 8 → 6 | 7 | 5 → 5 | -0.013 | 0.000 |
| Jogador 7 | 2-5 | 6 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 9 | 4 | 5 → 5 | -0.012 | 0.410 |
| Jogador 7 | 2-6 | 9 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 8 | 12 | 5 → 5 | 0.015 | 0.299 |
| Jogador 7 | 2-7 | 7 | 8.000 | -2.000 | 0 → 0 | 3 → 3 | 18% → 21% | 8 → 7 | 7 | 5 → 6 | 0.028 | 0.000 |
| Jogador 7 | 3-1 | 7 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 6 | 6 | 6 → 6 | -0.009 | -0.369 |
| Jogador 7 | 3-2 | 2 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 9 | 3 | 6 → 6 | 0.000 | 1.431 |
| Jogador 7 | 3-3 | 7 | 2.000 | -2.000 | 0 → 0 | 3 → 2 | 21% → 21% | 9 → 5 | 9 | 6 → 6 | -0.000 | -0.376 |
| Jogador 7 | 3-4 | 3 | -2.000 | 2.000 | 0 → 0 | 2 → 0 | 21% → 18% | 5 → 6 | 4 | 6 → 6 | -0.136 | 0.000 |
| Jogador 7 | 3-5 | 8 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 18% → 21% | 6 → 9 | 6 | 6 → 6 | -0.006 | 0.340 |
| Jogador 7 | 3-6 | 2 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 9 → 13 | 3 | 6 → 6 | 0.000 | 1.431 |
| Jogador 7 | 3-7 | 9 | 0.000 | -18.000 | 0 → 0 | 2 → 3 | 21% → 21% | 13 → 33 | 4 | 6 → 6 | 0.065 | 0.000 |
| Jogador 7 | 4-1 | 7 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 33 → 35 | 8 | 6 → 7 | -0.049 | 0.414 |
| Jogador 7 | 4-2 | 4 | 6.000 | -2.000 | 0 → 0 | 3 → 3 | 21% → 25% | 35 → 36 | 8 | 7 → 7 | 0.041 | 0.725 |
| Jogador 7 | 4-3 | 7 | 0.000 | 16.000 | 0 → 0 | 3 → 4 | 25% → 25% | 36 → 38 | 8 | 7 → 7 | 0.000 | 0.441 |
| Jogador 7 | 4-4 | 2 | 0.000 | -8.000 | 0 → 0 | 4 → 4 | 25% → 25% | 38 → 54 | 0 | 7 → 7 | 0.030 | 0.000 |
| Jogador 7 | 4-5 | 8 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 25% → 25% | 54 → 63 | 7 | 7 → 7 | 0.019 | 0.386 |
| Jogador 7 | 4-6 | 2 | -8.000 | 8.000 | 0 → 0 | 4 → 3 | 25% → 21% | 63 → 74 | 3 | 7 → 7 | -0.262 | 1.381 |
| Jogador 7 | 4-7 | 7 | 14.000 | -8.000 | 0 → 1 | 3 → 2 | 21% → 25% | 74 → 82 | 5 | 7 → 7 | 0.048 | 0.000 |
| Jogador 7 | 5-1 | 3 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 25% → 25% | 82 → 94 | 2 | 7 → 7 | 0.000 | 0.995 |
| Jogador 7 | 5-2 | 8 | 0.000 | -2.000 | 1 → 1 | 2 → 3 | 25% → 25% | 94 → 107 | 5 | 7 → 7 | -0.009 | -0.356 |
| Jogador 7 | 5-3 | 2 | 0.000 | -8.000 | 1 → 1 | 3 → 3 | 25% → 25% | 107 → 123 | 0 | 7 → 7 | 0.030 | 1.443 |
| Jogador 7 | 5-4 | 8 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 123 → 134 | 5 | 7 → 7 | 0.021 | 0.000 |
| Jogador 7 | 5-5 | 2 | 0.000 | 4.000 | 1 → 1 | 3 → 3 | 25% → 25% | 134 → 142 | 2 | 7 → 7 | 0.000 | -1.366 |
| Jogador 7 | 5-6 | 7 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 142 → 151 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-7 | 3 | 0.000 | 0.000 | 1 → 1 | 3 → 4 | 25% → 25% | 151 → 161 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 6 | 0.000 | 8.000 | 1 → 1 | 4 → 3 | 25% → 25% | 161 → 165 | 9 | 7 → 7 | -0.010 | 0.000 |
| Jogador 7 | 6-2 | 4 | 0.000 | -10.000 | 1 → 1 | 3 → 4 | 25% → 25% | 165 → 181 | 2 | 7 → 7 | 0.015 | 0.000 |
| Jogador 7 | 6-3 | 7 | 2.000 | 10.000 | 1 → 1 | 4 → 2 | 25% → 25% | 181 → 179 | 12 | 7 → 7 | 0.005 | 0.000 |
| Jogador 7 | 6-4 | 3 | 0.000 | -6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 179 → 194 | 3 | 7 → 7 | 0.020 | 0.000 |
| Jogador 7 | 6-5 | 8 | 0.000 | -8.000 | 1 → 1 | 2 → 2 | 25% → 25% | 194 → 211 | 4 | 7 → 7 | 0.007 | 0.387 |
| Jogador 7 | 6-6 | 2 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 211 → 220 | 3 | 7 → 7 | 0.000 | 1.548 |
| Jogador 7 | 6-7 | 8 | 0.000 | -4.000 | 1 → 1 | 2 → 3 | 25% → 25% | 220 → 233 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 7-1 | 1 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 25% → 25% | 233 → 230 | 3 | 7 → 7 | 0.000 | 0.000 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 18, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 17; mudanças de composição: 1; posicionamento melhorou em 42 ações e piorou em 33.
- Jogador 7 — estado final: ouro 230, nível 7, vida 45.0, colocação None.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.084 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 9 | 6.000 | 0.000 | 0 → 1 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.016 | -0.287 |
| Jogador 8 | 2-2 | 10 | 0.000 | 4.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 7 | 9 | 4 → 4 | 0.019 | -0.242 |
| Jogador 8 | 2-3 | 10 | -2.000 | -4.000 | 1 → 0 | 0 → 1 | 14% → 14% | 7 → 17 | 5 | 4 → 5 | -0.032 | -0.253 |
| Jogador 8 | 2-4 | 10 | 6.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 18% | 17 → 11 | 15 | 5 → 5 | 0.036 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 18% → 18% | 11 → 7 | 16 | 5 → 6 | 0.005 | 0.269 |
| Jogador 8 | 2-6 | 9 | 12.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 21% | 7 → 7 | 7 | 6 → 6 | 0.069 | 0.299 |
| Jogador 8 | 2-7 | 8 | 0.000 | 14.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 6 | 7 | 6 → 6 | 0.006 | 0.000 |
| Jogador 8 | 3-1 | 9 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 21% → 21% | 6 → 8 | 6 | 6 → 6 | 0.052 | 0.307 |
| Jogador 8 | 3-2 | 2 | 0.000 | -4.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 18 | 0 | 6 → 6 | 0.000 | 1.525 |
| Jogador 8 | 3-3 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 18 → 27 | 6 | 6 → 6 | 0.000 | 0.402 |
| Jogador 8 | 3-4 | 3 | 0.000 | 2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 27 → 34 | 2 | 6 → 6 | -0.020 | 0.000 |
| Jogador 8 | 3-5 | 8 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 34 → 45 | 10 | 6 → 6 | 0.008 | 0.363 |
| Jogador 8 | 3-6 | 2 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 45 → 55 | 3 | 6 → 6 | 0.000 | 1.406 |
| Jogador 8 | 3-7 | 9 | 4.000 | 4.000 | 0 → 0 | 2 → 1 | 21% → 21% | 55 → 50 | 19 | 6 → 6 | -0.043 | 0.000 |
| Jogador 8 | 4-1 | 7 | 0.000 | -4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 50 → 66 | 3 | 6 → 6 | 0.000 | 0.419 |
| Jogador 8 | 4-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 66 → 75 | 4 | 6 → 6 | 0.000 | -0.669 |
| Jogador 8 | 4-3 | 8 | 0.000 | -10.000 | 0 → 0 | 2 → 3 | 21% → 21% | 75 → 91 | 7 | 6 → 7 | 0.006 | -0.364 |
| Jogador 8 | 4-4 | 2 | 2.000 | 2.000 | 0 → 0 | 3 → 4 | 21% → 25% | 91 → 100 | 2 | 7 → 7 | -0.062 | 0.000 |
| Jogador 8 | 4-5 | 8 | 4.000 | 2.000 | 0 → 0 | 4 → 2 | 25% → 25% | 100 → 105 | 6 | 7 → 7 | -0.064 | -0.334 |
| Jogador 8 | 4-6 | 2 | 4.000 | -4.000 | 0 → 1 | 2 → 1 | 25% → 25% | 105 → 114 | 2 | 7 → 7 | 0.070 | -1.363 |
| Jogador 8 | 4-7 | 7 | 6.000 | 12.000 | 1 → 2 | 1 → 1 | 25% → 25% | 114 → 113 | 12 | 7 → 7 | -0.002 | 0.000 |
| Jogador 8 | 5-1 | 3 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 113 → 125 | 0 | 7 → 7 | 0.000 | -0.944 |
| Jogador 8 | 5-2 | 8 | 0.000 | 0.000 | 2 → 2 | 1 → 3 | 25% → 25% | 125 → 138 | 6 | 7 → 7 | 0.003 | 0.367 |
| Jogador 8 | 5-3 | 2 | 0.000 | -2.000 | 2 → 2 | 3 → 3 | 25% → 25% | 138 → 149 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 5-4 | 8 | 0.000 | -4.000 | 2 → 2 | 3 → 2 | 25% → 25% | 149 → 158 | 11 | 7 → 7 | 0.048 | 0.000 |
| Jogador 8 | 5-5 | 2 | 0.000 | 2.000 | 2 → 2 | 2 → 3 | 25% → 25% | 158 → 169 | 1 | 7 → 7 | 0.000 | 1.443 |
| Jogador 8 | 5-6 | 7 | 0.000 | 0.000 | 2 → 2 | 3 → 4 | 25% → 25% | 169 → 181 | 7 | 7 → 7 | 0.000 | 0.432 |
| Jogador 8 | 5-7 | 3 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 25% → 25% | 181 → 192 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 6 | 0.000 | -4.000 | 2 → 2 | 4 → 3 | 25% → 25% | 192 → 204 | 3 | 7 → 7 | 0.000 | -0.467 |
| Jogador 8 | 6-2 | 4 | 0.000 | 6.000 | 2 → 2 | 3 → 3 | 25% → 25% | 204 → 212 | 5 | 7 → 7 | 0.000 | 0.746 |
| Jogador 8 | 6-3 | 7 | -48.000 | -48.000 | 2 → 0 | 3 → 0 | 25% → 0% | 212 → 211 | 10 | 7 → 7 | -0.109 | -0.407 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 23, COMPOSITION_COMPATIBILITY: 28, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 41 ações e piorou em 26.
- Jogador 8 — estado final: ouro 211, nível 7, vida 6.0, colocação 3.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 72 | 35 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 1 | 0 |
| Jogador 2 | 59 | 35 | 0 | 1 | 1 | 0 | 1 | 0 | 8 | 1 | 1 | 0 |
| Jogador 3 | 52 | 23 | 0 | 0 | 0 | 1 | 0 | 0 | 9 | 0 | 0 | 0 |
| Jogador 4 | 47 | 23 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| Jogador 5 | 58 | 34 | 1 | 3 | 4 | 1 | 1 | 1 | 6 | 2 | 2 | 0 |
| Jogador 6 | 53 | 27 | 0 | 0 | 1 | 0 | 0 | 0 | 5 | 3 | 2 | 0 |
| Jogador 7 | 71 | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 1 | 0 | 0 |
| Jogador 8 | 79 | 44 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 3 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 84): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Akali_AD (2-7, step 107): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 1 — venda DA_KogMaw18_AD (5-2, step 192): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Alistar (5-4, step 202): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Vi18 (6-2, step 228): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Rakan (4-3, step 164): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (3-1, step 116): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Yorick (3-1, step 118): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Rakan (2-5, step 88): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Rakan (2-7, step 105): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Yorick (3-7, step 145): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Yunara (4-1, step 155): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Yunara (4-1, step 156): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Warwick (4-3, step 165): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-5, step 133): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_Scuttlecrab18 (4-1, step 155): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Cassiopeia (4-1, step 156): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Krug18 (4-3, step 166): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Scuttlecrab18 (5-4, step 207): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-6, step 97): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_Camille (2-6, step 96): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rakan (3-5, step 134): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (3-7, step 145): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Karma18 (3-5, step 133): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Veigar (3-7, step 144): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Diana (4-3, step 168): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (5-2, step 192): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Hecarim (5-7, step 220): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Diana (6-1, step 224): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (6-3, step 234): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Hecarim (6-3, step 236): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **6**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 2-3 | 65 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 1 | 2-5 | 84 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 5-2 | 192 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 5-4 | 202 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 2-2 | 52 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 53 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 54 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 55 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 57 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 515 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 622 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 759 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-5 | 891 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 1002 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1263 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1357 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1524 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1561 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 1739 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 1740 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 1803 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 1804 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 1922 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 1960 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2075 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 2210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-1 | 2261 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 2375 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 2415 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-4 | 2530 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-5 | 2568 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-6 | 2669 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-6 | 2670 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-7 | 2720 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-7 | 2721 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-1 | 2810 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-1 | 2811 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-2 | 2877 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-2 | 2878 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-3 | 2980 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-3 | 2981 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-4 | 3031 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-4 | 3032 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-5 | 3145 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-5 | 3146 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-6 | 3184 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-6 | 3185 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-7 | 3297 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-7 | 3298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| MEDIUM | Jogador 1 | 3-6 | 1612 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-7 | 104 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Warwick) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 2 | 3-1 | 115 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yorick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 2 | 4-3 | 164 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-4 | 798 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-5 | 932 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-6 | 1052 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-7 | 1188 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-1 | 1312 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-3 | 1453 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-3 | 1454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-4 | 1505 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-4 | 1506 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1619 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1658 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 1783 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 1886 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 1951 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 1952 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2070 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 2071 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2109 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 2110 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2222 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 4-5 | 2223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| HIGH | Jogador 3 | 3-1 | 116 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 3-1 | 118 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 4-5 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-5 | 781 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-6 | 891 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-7 | 999 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-1 | 1120 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1121 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-2 | 1158 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-3 | 1256 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-3 | 1257 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1306 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1417 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1579 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1678 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 1741 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 1854 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 1891 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2008 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-5 | 2009 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2046 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-6 | 2047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-7 | 2148 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 2198 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-2 | 2314 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-2 | 2315 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 3-4 | 1394 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-1 | 117 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 4 | 3-7 | 145 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-1 | 155 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 4-1 | 156 | SOLD_CORE_UNIT | Venda de 'DA_18_Yunara' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-3 | 165 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 3-5 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-6 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-6 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-5 | 2050 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-5 | 2051 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 3-4 | 1437 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-6 | 96 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 99 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-1 | 116 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-3 | 127 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 5 | 3-4 | 130 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 4-1 | 155 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-1 | 156 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-3 | 166 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Krug18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-4 | 207 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 47 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 48 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 51 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 52 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 53 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 54 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 61 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 2-7 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 109 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-3 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-3 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 546 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 679 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 810 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 931 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-5 | 2506 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-5 | 2507 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 3-6 | 1573 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-4 | 1989 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-3 | 66 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-7 | 105 | PURCHASE_SALE_REVIEW | Compra de DA_KogMaw18_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 3-3 | 127 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 6 | 2-2 | 52 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 53 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 54 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 55 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 61 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 2-7 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 116 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-3 | 211 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-4 | 258 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 427 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 525 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 660 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 793 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 914 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1166 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1203 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1301 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1351 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1461 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1462 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 1499 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1500 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1611 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1612 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 1712 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 1713 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 1776 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 1777 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 1889 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 1890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 1928 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 1929 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2043 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2044 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 2081 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2082 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 2180 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 2231 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-3 | 2390 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-3 | 2391 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 2-6 | 96 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-5 | 134 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-7 | 145 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-3 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-3 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-3 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-3 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-3 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-3 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-3 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-4 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-4 | 240 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-4 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-5 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-5 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-5 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 6-5 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 331 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 417 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 555 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-5 | 829 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 950 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-7 | 1046 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-3 | 1280 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1335 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1492 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1619 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 1717 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 1777 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 1879 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 1916 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2030 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2067 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2167 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2168 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2218 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 2219 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-3 | 2935 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-4 | 2988 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 3103 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-6 | 3142 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-7 | 3254 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 1-4 | 38 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-3 | 69 | PURCHASE_SALE_REVIEW | Compra de DA_18_Cassiopeia foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-5 | 86 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 8 | 3-7 | 144 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-3 | 168 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 5-2 | 192 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-7 | 220 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 6-1 | 224 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 6-3 | 234 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 6-3 | 236 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 2-4 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-4 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 151 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 212 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 309 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 433 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 564 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 699 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 831 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 964 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1193 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-1 | 1321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1359 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1507 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1617 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 1654 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 1773 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 1875 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 1941 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2052 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2090 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2207 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2208 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2246 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 2347 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 2399 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 2517 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-3 | 2556 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-4 | 2671 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-5 | 2710 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-6 | 2809 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-7 | 2860 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-1 | 2950 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-2 | 3013 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-3 | 3118 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-3 | 3119 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
