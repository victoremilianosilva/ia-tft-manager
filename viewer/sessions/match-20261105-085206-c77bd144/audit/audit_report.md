# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4874**
- Achados: **362**
- CRITICAL: 0 | HIGH: 30 | MEDIUM: 59 | LOW: 273

## Metadados da sessão

- Match ID: c77bd144-057a-4fab-9f0f-1c9c429a0b95
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 75f85fcc863dec3a3ed733875b445fc41eabec9c8d0a4e5eb23247049009b7fd
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4237**
- Entradas posteriores à eliminação ignoradas: **637**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 9 | 9 | 43 | 8 | 71 | 5 | 7 | não/inconclusivo | 0 |
| Jogador 6 | 3 | 9 | 40 | 7 | 56 | 7 | 2 | não/inconclusivo | 0 |
| Jogador 7 | 47 | 8 | 23 | 10 | 40 | 8 | 1 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 189 | 46 | 14 | 26 | 0 | 19 | 72 | 0.1055 | 16 | 31 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::MOVE_BOARD: 5, ALL_IN::PASS: 2, FAST8::BUY: 13, FAST8::BUY_XP: 15, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 12, FAST8::MOVE_BOARD: 18, FAST8::PASS: 7, FAST8::SELL: 6, STABILIZE::BUY: 29, STABILIZE::BUY_XP: 11, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 19, STABILIZE::MOVE_BOARD: 18, STABILIZE::PASS: 10, STABILIZE::SELL: 8
- Jogador 1 — recompensas por ação: BUY: média 0.4215 (n=46), BUY_XP: média -0.0242 (n=26), ITEM: média 0.1350 (n=12), MOVE_BENCH: média 0.0287 (n=31), MOVE_BOARD: média -0.0073 (n=41), PASS: média -0.0053 (n=19), SELL: média -0.0664 (n=14)
| Jogador 2 | 230 | 65 | 34 | 20 | 0 | 13 | 90 | 0.1134 | 7 | 31 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 11, ALL_IN::MOVE_BOARD: 16, ALL_IN::PASS: 2, ALL_IN::SELL: 6, STABILIZE::BUY: 54, STABILIZE::BUY_XP: 20, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 16, STABILIZE::MOVE_BOARD: 58, STABILIZE::PASS: 11, STABILIZE::SELL: 28
- Jogador 2 — recompensas por ação: BUY: média 0.4074 (n=65), BUY_XP: média -0.0190 (n=20), ITEM: média 0.1537 (n=8), MOVE_BENCH: média 0.2162 (n=16), MOVE_BOARD: média -0.0061 (n=74), PASS: média -0.0338 (n=13), SELL: média -0.1127 (n=34)
| Jogador 3 | 204 | 58 | 31 | 17 | 0 | 19 | 70 | 0.0925 | 18 | 34 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::MOVE_BOARD: 3, ALL_IN::PASS: 1, ALL_IN::SELL: 2, FAST8::BUY: 16, FAST8::BUY_XP: 9, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 20, FAST8::PASS: 8, FAST8::SELL: 12, STABILIZE::BUY: 40, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 32, STABILIZE::PASS: 10, STABILIZE::SELL: 17
- Jogador 3 — recompensas por ação: BUY: média 0.3372 (n=58), BUY_XP: média -0.0118 (n=17), ITEM: média 0.1367 (n=9), MOVE_BENCH: média 0.0787 (n=15), MOVE_BOARD: média -0.0058 (n=55), PASS: média -0.0158 (n=19), SELL: média -0.0736 (n=31)
| Jogador 4 | 274 | 71 | 30 | 43 | 0 | 19 | 98 | 0.1077 | 28 | 40 |
- Jogador 4 — ações por estratégia: FAST8::BUY: 14, FAST8::BUY_XP: 16, FAST8::ITEM: 5, FAST8::MOVE_BENCH: 16, FAST8::MOVE_BOARD: 19, FAST8::PASS: 8, FAST8::SELL: 6, STABILIZE::BUY: 57, STABILIZE::BUY_XP: 27, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 45, STABILIZE::PASS: 11, STABILIZE::SELL: 24
- Jogador 4 — recompensas por ação: BUY: média 0.4252 (n=71), BUY_XP: média 0.0028 (n=43), ITEM: média 0.1515 (n=13), MOVE_BENCH: média 0.0359 (n=34), MOVE_BOARD: média -0.0080 (n=64), PASS: média -0.0237 (n=19), SELL: média -0.1007 (n=30)
| Jogador 5 | 271 | 75 | 42 | 32 | 0 | 18 | 93 | 0.0969 | 16 | 50 |
- Jogador 5 — ações por estratégia: ECON::BUY: 4, ECON::BUY_XP: 5, ECON::ITEM: 2, ECON::MOVE_BENCH: 2, ECON::MOVE_BOARD: 3, ECON::SELL: 3, FAST8::BUY: 17, FAST8::BUY_XP: 6, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 22, FAST8::PASS: 7, FAST8::SELL: 8, STABILIZE::BUY: 54, STABILIZE::BUY_XP: 21, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 54, STABILIZE::PASS: 11, STABILIZE::SELL: 31
- Jogador 5 — recompensas por ação: BUY: média 0.3613 (n=75), BUY_XP: média -0.0013 (n=32), ITEM: média 0.1454 (n=11), MOVE_BENCH: média 0.1664 (n=14), MOVE_BOARD: média -0.0109 (n=79), PASS: média -0.0272 (n=18), SELL: média -0.0807 (n=42)
| Jogador 6 | 242 | 56 | 21 | 40 | 0 | 18 | 94 | 0.0797 | 14 | 38 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::MOVE_BENCH: 6, ALL_IN::MOVE_BOARD: 1, ECON::BUY: 1, ECON::BUY_XP: 9, ECON::MOVE_BENCH: 1, FAST8::BUY: 17, FAST8::BUY_XP: 9, FAST8::ITEM: 7, FAST8::MOVE_BENCH: 14, FAST8::MOVE_BOARD: 27, FAST8::PASS: 12, FAST8::SELL: 6, STABILIZE::BUY: 36, STABILIZE::BUY_XP: 22, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 24, STABILIZE::MOVE_BOARD: 21, STABILIZE::OTHER: 1, STABILIZE::PASS: 6, STABILIZE::SELL: 15
- Jogador 6 — recompensas por ação: BUY: média 0.4184 (n=56), BUY_XP: média -0.0092 (n=40), ITEM: média 0.1008 (n=12), MOVE_BENCH: média -0.0380 (n=45), MOVE_BOARD: média 0.0008 (n=49), OTHER: média -0.0300 (n=1), PASS: média -0.0289 (n=18), SELL: média -0.1319 (n=21)
| Jogador 7 | 161 | 40 | 17 | 23 | 0 | 14 | 59 | 0.1259 | 12 | 27 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::BUY_XP: 5, ALL_IN::SELL: 2, STABILIZE::BUY: 38, STABILIZE::BUY_XP: 18, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 32, STABILIZE::MOVE_BOARD: 27, STABILIZE::PASS: 14, STABILIZE::SELL: 15
- Jogador 7 — recompensas por ação: BUY: média 0.5065 (n=40), BUY_XP: média 0.0778 (n=23), ITEM: média 0.1787 (n=8), MOVE_BENCH: média 0.0147 (n=32), MOVE_BOARD: média -0.0244 (n=27), PASS: média -0.0336 (n=14), SELL: média -0.1500 (n=17)
| Jogador 8 | 173 | 47 | 22 | 22 | 0 | 14 | 59 | 0.1108 | 13 | 22 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::BUY_XP: 5, ALL_IN::SELL: 2, STABILIZE::BUY: 45, STABILIZE::BUY_XP: 17, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 45, STABILIZE::PASS: 14, STABILIZE::SELL: 20
- Jogador 8 — recompensas por ação: BUY: média 0.4209 (n=47), BUY_XP: média -0.0077 (n=22), ITEM: média 0.1744 (n=9), MOVE_BENCH: média 0.0664 (n=14), MOVE_BOARD: média -0.0113 (n=45), PASS: média 0.0000 (n=14), SELL: média -0.1105 (n=22)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 08:52:18 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2600 |  |
| Jogador 1 | ? | 08:52:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 08:52:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 1-1 | 08:52:25 | MOVE Bench -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.3200 |  |
| Jogador 1 | 1-1 | 08:52:26 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3100 |  |
| Jogador 1 | 1-1 | 08:52:28 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 1 | 1-1 | 08:52:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-1 | 08:52:29 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4200 |  |
| Jogador 1 | 1-2 | 08:52:32 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 1-2 | 08:52:33 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 1 | 1-2 | 08:52:33 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-2 | 08:52:35 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0700 |  |
| Jogador 1 | 1-2 | 08:52:37 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 1 | 1-3 | 08:52:41 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 08:52:42 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 08:52:43 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-3 | 08:52:43 | MOVE Board -> Board: Ornn (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 1-3 | 08:52:44 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 1-3 | 08:52:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 08:52:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 1 | 1-4 | 08:52:53 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1900 |  |
| Jogador 1 | 1-4 | 08:52:54 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 1 | 1-4 | 08:52:55 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.5400 |  |
| Jogador 1 | 1-4 | 08:52:55 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 1 | 1-4 | 08:52:56 | MOVE Board -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-4 | 08:52:57 | MOVE Board -> Board: Ornn (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 1 | 1-4 | 08:52:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-1 | 08:53:03 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.3000 |  |
| Jogador 1 | 2-1 | 08:53:04 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.1900 |  |
| Jogador 1 | 2-1 | 08:53:05 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Diana | 0.1200 |  |
| Jogador 1 | 2-1 | 08:53:06 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-1 | 08:53:06 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Diana | -0.0600 |  |
| Jogador 1 | 2-1 | 08:53:07 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.0500 |  |
| Jogador 1 | 2-1 | 08:53:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-1 | 08:53:08 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Diana | -0.1000 |  |
| Jogador 1 | 2-2 | 08:53:15 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-3 | 08:53:29 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | 0.7700 |  |
| Jogador 1 | 2-3 | 08:53:30 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Diana | 0.2200 |  |
| Jogador 1 | 2-3 | 08:53:31 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Diana | 0.4000 |  |
| Jogador 1 | 2-3 | 08:53:32 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Diana | 0.1700 |  |
| Jogador 1 | 2-3 | 08:53:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-3 | 08:53:34 | MOVE Board -> Board: Leona (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 08:53:34 | MOVE Board -> Board: Akali (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-3 | 08:53:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 08:53:40 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Diana | 0.8700 |  |
| Jogador 1 | 2-4 | 08:53:41 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Defendente | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 08:53:41 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-4 | 08:53:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-4 | 08:53:42 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 08:53:42 | MOVE Bench -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Diana | -0.5300 |  |
| Jogador 1 | 2-4 | 08:53:43 | MOVE Bench -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Diana | 0.0800 |  |
| Jogador 1 | 2-4 | 08:53:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Diana | -0.3100 |  |
| Jogador 1 | 2-4 | 08:53:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Diana | -0.5000 |  |
| Jogador 1 | 2-4 | 08:53:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-5 | 08:54:00 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Defendente | DA_18_Diana | 0.0800 |  |
| Jogador 1 | 2-5 | 08:54:01 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Defendente | DA_18_Akali_AD | 0.8700 |  |
| Jogador 1 | 2-5 | 08:54:02 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Defendente | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 2-5 | 08:54:02 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Akali_AD | 0.2500 |  |
| Jogador 1 | 2-5 | 08:54:03 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | -0.2400 |  |
| Jogador 1 | 2-5 | 08:54:04 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 08:54:04 | MOVE Bench -> Board: Krugue (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | -0.1100 |  |
| Jogador 1 | 2-5 | 08:54:05 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 08:54:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 08:54:22 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Defendente | DA_18_Diana | -0.2900 |  |
| Jogador 1 | 2-6 | 08:54:23 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Defendente | DA_18_Rakan | 0.9400 |  |
| Jogador 1 | 2-6 | 08:54:23 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Defendente | DA_18_Rakan | 0.4200 |  |
| Jogador 1 | 2-6 | 08:54:24 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Defendente | DA_18_Rakan | 0.0700 |  |
| Jogador 1 | 2-6 | 08:54:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Rakan | -0.1200 |  |
| Jogador 1 | 2-6 | 08:54:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Rakan | 0.0500 |  |
| Jogador 1 | 2-6 | 08:54:26 | MOVE Bench -> Board: Grompe (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Rakan | -0.3900 |  |
| Jogador 1 | 2-6 | 08:54:28 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Rakan | 0.5800 |  |
| Jogador 1 | 2-7 | 08:54:37 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Rakan | 0.2100 |  |
| Jogador 1 | 2-7 | 08:54:38 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Rakan | 0.1600 |  |
| Jogador 1 | 2-7 | 08:54:38 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rakan | -0.0400 |  |
| Jogador 1 | 2-7 | 08:54:39 | MOVE Bench -> Board: Grompe (i:4.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Rakan | -0.2100 |  |
| Jogador 1 | 2-7 | 08:54:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 3-1 | 08:55:00 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Defendente | DA_18_Rakan | 0.1100 |  |
| Jogador 1 | 3-1 | 08:55:00 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Defendente | DA_18_Rakan | -0.3300 |  |
| Jogador 1 | 3-1 | 08:55:01 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Defendente | DA_18_Rakan | -0.0500 |  |
| Jogador 1 | 3-1 | 08:55:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Defendente | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 3-2 | 08:55:22 | VENDEU: Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Defendente | DA_CrimsonRaptor18 | -0.2200 |  |
| Jogador 1 | 3-2 | 08:55:22 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Vi (i:6.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Defendente | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 1 | 3-2 | 08:55:23 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Vi (i:6.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Defendente | DA_CrimsonRaptor18 | 0.0800 |  |
| Jogador 1 | 3-2 | 08:55:23 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Defendente | DA_CrimsonRaptor18 | 0.5800 |  |
| Jogador 1 | 3-2 | 08:55:24 | MOVE Bench -> Board: Krugue (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Defendente | DA_CrimsonRaptor18 | -0.9500 |  |
| Jogador 1 | 3-2 | 08:55:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Defendente | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 1 | 3-2 | 08:55:25 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Defendente | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 1 | 3-2 | 08:55:25 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Defendente | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 1 | 3-2 | 08:55:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 1 | Defendente | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 1 | 3-3 | 08:55:44 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Defendente | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 1 | 3-3 | 08:55:45 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Defendente | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 1 | 3-3 | 08:55:45 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 1 | 3-3 | 08:55:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 1 | 3-3 | 08:55:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_CrimsonRaptor18 | 0.0800 |  |
| Jogador 1 | 3-3 | 08:55:47 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_CrimsonRaptor18 | 0.4500 |  |
| Jogador 1 | 3-3 | 08:55:47 | MOVE Board -> Board: Grompe (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 1 | 3-3 | 08:55:48 | MOVE Board -> Board: Vi (i:6.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_CrimsonRaptor18 | 0.0300 |  |
| Jogador 1 | 3-3 | 08:55:48 | MOVE Board -> Board: Ornn (i:2.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 1 | 3-4 | 08:56:08 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Shen | 0.6900 |  |
| Jogador 1 | 3-4 | 08:56:08 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 3-4 | 08:56:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 3-4 | 08:56:09 | MOVE Bench -> Board: Shen (i:8.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Shen | 0.2300 |  |
| Jogador 1 | 3-4 | 08:56:10 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Shen | 0.0300 |  |
| Jogador 1 | 3-4 | 08:56:11 | MOVE Board -> Board: Krugue (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-4 | 08:56:11 | MOVE Board -> Board: Grompe (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Shen | -0.0400 |  |
| Jogador 1 | 3-4 | 08:56:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-5 | 08:56:33 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_18_Shen | 0.2200 |  |
| Jogador 1 | 3-5 | 08:56:34 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Shen | 0.1600 |  |
| Jogador 1 | 3-5 | 08:56:34 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-5 | 08:56:35 | MOVE Board -> Board: Krugue (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 3-5 | 08:56:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-6 | 08:57:01 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Shen | -0.2700 |  |
| Jogador 1 | 3-6 | 08:57:01 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_18_Shen | 0.6500 |  |
| Jogador 1 | 3-6 | 08:57:01 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Shen | 0.0800 |  |
| Jogador 1 | 3-6 | 08:57:02 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_18_Shen | 0.1300 |  |
| Jogador 1 | 3-6 | 08:57:03 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 3-6 | 08:57:03 | COMPROU: Lux (Feérica) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_18_Lux_Fae | -0.1400 |  |
| Jogador 1 | 3-6 | 08:57:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Lux_Fae | -0.0100 |  |
| Jogador 1 | 3-6 | 08:57:04 | MOVE Board -> Board: Grompe (i:4.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Lux_Fae | 0.0500 |  |
| Jogador 1 | 3-6 | 08:57:05 | MOVE Board -> Board: Ornn (i:2.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Lux_Fae | -0.0200 |  |
| Jogador 1 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Lux_Fae | 0.1900 |  |
| Jogador 1 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Lux_Fae | 0.2000 |  |
| Jogador 1 | 3-7 | 08:57:31 | VENDEU: Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Lux_Fae | 0.0700 |  |
| Jogador 1 | 3-7 | 08:57:31 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_Vi18 | 0.6200 |  |
| Jogador 1 | 3-7 | 08:57:32 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_Vi18 | 0.5700 |  |
| Jogador 1 | 3-7 | 08:57:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 3-7 | 08:57:32 | MOVE Bench -> Board: Leona (i:2.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_Vi18 | -0.4000 |  |
| Jogador 1 | 3-7 | 08:57:33 | MOVE Bench -> Board: Leona (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_Vi18 | 0.1000 |  |
| Jogador 1 | 3-7 | 08:57:34 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_Vi18 | -0.4100 |  |
| Jogador 1 | 4-1 | 08:58:03 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_Vi18 | 0.2200 |  |
| Jogador 1 | 4-1 | 08:58:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-1 | 08:58:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-1 | 08:58:05 | MOVE Board -> Board: Shen (i:8.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-1 | 08:58:05 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-1 | 08:58:06 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-2 | 08:58:37 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_Vi18 | 0.7700 |  |
| Jogador 1 | 4-2 | 08:58:37 | MOVE Bench -> Board: Leona (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_Vi18 | 0.0900 |  |
| Jogador 1 | 4-2 | 08:58:38 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_Vi18 | 0.3900 |  |
| Jogador 1 | 4-2 | 08:58:38 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-2 | 08:58:40 | MOVE Board -> Board: Shen (i:8.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-2 | 08:58:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-3 | 08:59:11 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_Vi18 | 0.6500 |  |
| Jogador 1 | 4-3 | 08:59:11 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-3 | 08:59:12 | MOVE Board -> Board: Grompe (i:4.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_Vi18 | -0.0200 |  |
| Jogador 1 | 4-3 | 08:59:12 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-3 | 08:59:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-4 | 08:59:46 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Defendente | DA_Vi18 | 0.2100 |  |
| Jogador 1 | 4-4 | 08:59:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_Vi18 | -0.0900 |  |
| Jogador 1 | 4-4 | 08:59:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-4 | 08:59:47 | MOVE Bench -> Board: Rammus (i:6.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_Vi18 | -0.3800 |  |
| Jogador 1 | 4-4 | 08:59:47 | MOVE Board -> Board: Krugue (i:6.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_Vi18 | -0.0700 |  |
| Jogador 1 | 4-4 | 08:59:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-5 | 09:00:25 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Defendente | DA_18_Lux_Fae | -0.1800 |  |
| Jogador 1 | 4-5 | 09:00:26 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Krugue (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Defendente | DA_18_Lux_Fae | 0.0600 |  |
| Jogador 1 | 4-5 | 09:00:26 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Krugue (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Defendente | DA_18_Lux_Fae | 0.0800 |  |
| Jogador 1 | 4-5 | 09:00:27 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Krugue (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Defendente | DA_18_Lux_Fae | 0.1100 |  |
| Jogador 1 | 4-5 | 09:00:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 0 | Defendente | DA_18_Lux_Fae | 0.7000 |  |
| Jogador 1 | 4-5 | 09:00:28 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Defendente | DA_18_Lux_Fae | 0.0700 |  |
| Jogador 1 | 4-5 | 09:00:28 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Defendente | DA_18_Lux_Fae | 0.5900 |  |
| Jogador 1 | 4-5 | 09:00:29 | MOVE Board -> Board: Leona (i:2.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Defendente | DA_18_Lux_Fae | -0.0100 |  |
| Jogador 1 | 4-5 | 09:00:29 | MOVE Board -> Board: Krugue (i:6.0) <-> Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Defendente | DA_18_Lux_Fae | -0.0100 |  |
| Jogador 1 | 4-6 | 09:01:03 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Defendente | DA_18_Lux_Fae | 0.7500 |  |
| Jogador 1 | 4-6 | 09:01:03 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Defendente | DA_18_Lux_Fae | -0.0100 |  |
| Jogador 1 | 4-6 | 09:01:04 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 11 | 1 | Defendente | DA_18_Lux_Fae | -0.0100 |  |
| Jogador 1 | 4-6 | 09:01:04 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 7 | 1 | Defendente | DA_18_Lux_Fae | -0.0900 |  |
| Jogador 1 | 4-6 | 09:01:05 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Defendente | DA_18_Lux_Fae | -0.0100 |  |
| Jogador 1 | 4-6 | 09:01:05 | MOVE Board -> Board: Shen (i:8.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Defendente | DA_18_Lux_Fae | 0.0000 |  |
| Jogador 1 | 4-6 | 09:01:06 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Defendente | DA_18_Lux_Fae | -0.0100 |  |
| Jogador 1 | 4-6 | 09:01:06 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Defendente | DA_18_Lux_Fae | 0.0000 |  |
| Jogador 1 | 4-7 | 09:01:42 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Defendente | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 1 | 4-7 | 09:01:42 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Defendente | DA_KogMaw18_AD | 0.7100 |  |
| Jogador 1 | 4-7 | 09:01:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Defendente | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 4-7 | 09:01:43 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Defendente | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 1 | 4-7 | 09:01:43 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Defendente | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 4-7 | 09:01:44 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Defendente | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-7 | 09:01:44 | MOVE Board -> Board: Leona (i:2.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Defendente | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-7 | 09:01:45 | MOVE Board -> Board: Krugue (i:6.0) <-> Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Defendente | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-7 | 09:01:45 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Defendente | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 5-1 | 09:02:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Defendente | DA_KogMaw18_AD | 0.8200 |  |
| Jogador 1 | 5-1 | 09:02:22 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Defendente | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 1 | 5-1 | 09:02:23 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 5-1 | 09:02:23 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 5-1 | 09:02:24 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 5-1 | 09:02:24 | MOVE Board -> Board: Leona (i:2.0) <-> Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 5-1 | 09:02:24 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 5-2 | 09:03:02 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Defendente | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 5-2 | 09:03:02 | MOVE Board -> Board: Krugue (i:6.0) <-> Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Defendente | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 5-2 | 09:03:03 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Defendente | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 5-2 | 09:03:03 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Defendente | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 2 | ? | 08:52:18 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | ? | 08:52:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 08:52:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 08:52:25 | MOVE Bench -> Board: Veigar (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 1-1 | 08:52:26 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 1-1 | 08:52:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 08:52:32 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 08:52:33 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-2 | 08:52:33 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 1-2 | 08:52:35 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 1-2 | 08:52:37 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 1-3 | 08:52:41 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 08:52:42 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 1.0900 |  |
| Jogador 2 | 1-3 | 08:52:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 1-3 | 08:52:43 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 1-3 | 08:52:44 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 1-3 | 08:52:44 | MOVE Board -> Board: Xayah (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 1-3 | 08:52:45 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 1-3 | 08:52:46 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 1-3 | 08:52:46 | MOVE Board -> Board: Veigar (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 1-4 | 08:52:52 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 1-4 | 08:52:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 08:52:54 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 08:52:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 1-4 | 08:52:55 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 1-4 | 08:52:56 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-4 | 08:52:57 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 1-4 | 08:52:58 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.3100 |  |
| Jogador 2 | 2-1 | 08:53:03 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.9700 |  |
| Jogador 2 | 2-1 | 08:53:04 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 2-1 | 08:53:05 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 08:53:06 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 2-1 | 08:53:06 | MOVE Board -> Board: Xayah (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 08:53:07 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 2-1 | 08:53:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 08:53:08 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 2-2 | 08:53:15 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 2-3 | 08:53:29 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-3 | 08:53:30 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Veigar | 0.9500 |  |
| Jogador 2 | 2-3 | 08:53:31 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Veigar | 0.5900 |  |
| Jogador 2 | 2-3 | 08:53:32 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Veigar | 0.3800 |  |
| Jogador 2 | 2-3 | 08:53:33 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 2-3 | 08:53:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-3 | 08:53:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-3 | 08:53:34 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.5600 |  |
| Jogador 2 | 2-4 | 08:53:40 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 2-4 | 08:53:41 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Veigar | -0.2400 |  |
| Jogador 2 | 2-4 | 08:53:41 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 2-4 | 08:53:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 08:53:42 | MOVE Board -> Board: Varus (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-4 | 08:53:42 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 08:53:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-5 | 08:54:00 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 2-5 | 08:54:01 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Veigar | 0.7100 |  |
| Jogador 2 | 2-5 | 08:54:02 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 2-5 | 08:54:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-5 | 08:54:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 08:54:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-5 | 08:54:04 | MOVE Bench -> Board: Kayle (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 2-5 | 08:54:05 | MOVE Board -> Board: Kayle (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-5 | 08:54:06 | MOVE Board -> Board: Veigar (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 08:54:22 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Veigar | 0.9000 |  |
| Jogador 2 | 2-6 | 08:54:23 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 2-6 | 08:54:23 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 2-6 | 08:54:24 | MOVE Board -> Board: Varus (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 2-6 | 08:54:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 08:54:25 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 2-6 | 08:54:26 | MOVE Board -> Board: Veigar (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-6 | 08:54:28 | MOVE Board -> Board: Veigar (i:4.0) <-> Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-7 | 08:54:37 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_SparringGloves -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 2-7 | 08:54:38 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-7 | 08:54:38 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 2-7 | 08:54:39 | MOVE Board -> Board: Kayle (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 08:54:40 | MOVE Board -> Board: Varus (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 2-7 | 08:54:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 08:55:00 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 3-1 | 08:55:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-1 | 08:55:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 08:55:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Espinhos Negros | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-1 | 08:55:02 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 08:55:02 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Espinhos Negros | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 3-1 | 08:55:03 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Espinhos Negros | DA_18_Veigar | -0.2000 |  |
| Jogador 2 | 3-1 | 08:55:04 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Espinhos Negros | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 3-1 | 08:55:04 | MOVE Board -> Board: Varus (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 08:55:22 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 08:55:22 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 3-2 | 08:55:23 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 3-2 | 08:55:23 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 3-2 | 08:55:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-2 | 08:55:24 | MOVE Board -> Board: Tristana (i:6.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 08:55:25 | MOVE Board -> Board: Varus (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-2 | 08:55:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 08:55:44 | VENDEU: Kayle (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Espinhos Negros | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 3-3 | 08:55:45 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Espinhos Negros | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 3-3 | 08:55:45 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Espinhos Negros | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-3 | 08:55:46 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Espinhos Negros | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 3-3 | 08:55:46 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Espinhos Negros | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-3 | 08:55:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 08:55:47 | MOVE Board -> Board: Veigar (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 08:55:48 | MOVE Board -> Board: Varus (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 08:55:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-4 | 08:56:08 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Espinhos Negros | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 3-4 | 08:56:08 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_18_Veigar | 0.6300 |  |
| Jogador 2 | 3-4 | 08:56:09 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Espinhos Negros | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 3-4 | 08:56:09 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 3-4 | 08:56:10 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 08:56:11 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 3-4 | 08:56:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Veigar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-5 | 08:56:33 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 08:56:34 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Espinhos Negros | DA_18_Veigar | 0.8500 |  |
| Jogador 2 | 3-5 | 08:56:34 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Espinhos Negros | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-5 | 08:56:35 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Espinhos Negros | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 3-5 | 08:56:35 | MOVE Bench -> Board: Leona (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Espinhos Negros | DA_18_Veigar | -0.3300 |  |
| Jogador 2 | 3-5 | 08:56:36 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Espinhos Negros | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 3-5 | 08:56:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Espinhos Negros | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-5 | 08:56:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 08:56:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Espinhos Negros | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 3-6 | 08:57:01 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_18_Veigar | -0.4600 |  |
| Jogador 2 | 3-6 | 08:57:01 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_18_Veigar | 0.7400 |  |
| Jogador 2 | 3-6 | 08:57:01 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Kobuko (i:2.0) (tabuleiro slot 6) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 3-6 | 08:57:02 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 3-6 | 08:57:03 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_18_Veigar | 0.7100 |  |
| Jogador 2 | 3-6 | 08:57:03 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 3-6 | 08:57:04 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Espinhos Negros | DA_18_Veigar | 0.6600 |  |
| Jogador 2 | 3-6 | 08:57:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-6 | 08:57:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Espinhos Negros | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 3-7 | 08:57:31 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Espinhos Negros | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 3-7 | 08:57:31 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Espinhos Negros | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 3-7 | 08:57:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-7 | 08:57:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-7 | 08:57:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-7 | 08:57:33 | MOVE Board -> Board: Yunara (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-7 | 08:57:34 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 4-1 | 08:58:03 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 4-1 | 08:58:04 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 4-1 | 08:58:04 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 4-1 | 08:58:05 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 4-1 | 08:58:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-1 | 08:58:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-1 | 08:58:06 | MOVE Board -> Board: Yunara (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-1 | 08:58:07 | MOVE Board -> Board: Varus (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-1 | 08:58:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 08:58:37 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 4-2 | 08:58:37 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 4-2 | 08:58:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-2 | 08:58:38 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-2 | 08:58:40 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 4-2 | 08:58:40 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-2 | 08:58:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 08:59:11 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Espinhos Negros | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-3 | 08:59:11 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Espinhos Negros | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 4-3 | 08:59:12 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-3 | 08:59:12 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Espinhos Negros | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-3 | 08:59:13 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 08:59:13 | MOVE Board -> Board: Rakan (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Espinhos Negros | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 4-3 | 08:59:14 | MOVE Board -> Board: Yunara (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-3 | 08:59:14 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Espinhos Negros | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-3 | 08:59:15 | MOVE Board -> Board: Varus (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Espinhos Negros | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 4-4 | 08:59:46 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Espinhos Negros | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 4-4 | 08:59:46 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Espinhos Negros | DA_18_Azir | 0.7500 |  |
| Jogador 2 | 4-4 | 08:59:47 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Azir | 0.7900 |  |
| Jogador 2 | 4-4 | 08:59:47 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Azir | 0.0400 |  |
| Jogador 2 | 4-4 | 08:59:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Azir | 0.0300 |  |
| Jogador 2 | 4-4 | 08:59:48 | MOVE Board -> Board: Yunara (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 2 | 4-4 | 08:59:48 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Azir | 0.1900 |  |
| Jogador 2 | 4-4 | 08:59:49 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Azir | -0.0900 |  |
| Jogador 2 | 4-4 | 08:59:49 | MOVE Board -> Board: Veigar (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Azir | 0.0800 |  |
| Jogador 2 | 4-5 | 09:00:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Espinhos Negros | DA_18_Azir | 0.7800 |  |
| Jogador 2 | 4-5 | 09:00:26 | VENDEU: Azir (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Espinhos Negros | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 4-5 | 09:00:26 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Espinhos Negros | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 4-5 | 09:00:27 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Espinhos Negros | DA_18_Veigar | -0.3300 |  |
| Jogador 2 | 4-5 | 09:00:27 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Espinhos Negros | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 4-5 | 09:00:28 | MOVE Board -> Board: Varus (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Espinhos Negros | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 4-5 | 09:00:28 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Espinhos Negros | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-5 | 09:00:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Espinhos Negros | DA_18_Veigar | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-6 | 09:01:03 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 1 | Espinhos Negros | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 4-6 | 09:01:03 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Espinhos Negros | DA_18_Veigar | 0.6500 |  |
| Jogador 2 | 4-6 | 09:01:04 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 1 | Espinhos Negros | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-6 | 09:01:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Espinhos Negros | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 4-6 | 09:01:05 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Espinhos Negros | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 09:01:05 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Espinhos Negros | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 4-6 | 09:01:06 | MOVE Board -> Board: Veigar (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Espinhos Negros | DA_18_Veigar | -0.2400 |  |
| Jogador 2 | 4-6 | 09:01:06 | MOVE Board -> Board: Varus (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Espinhos Negros | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-6 | 09:01:07 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Espinhos Negros | DA_18_Veigar | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Espinhos Negros | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NeedlesslyLargeRod -> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Espinhos Negros | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 4-7 | 09:01:43 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Espinhos Negros | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 4-7 | 09:01:43 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0900 |  |
| Jogador 2 | 4-7 | 09:01:43 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.2200 |  |
| Jogador 2 | 4-7 | 09:01:44 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.1700 |  |
| Jogador 2 | 4-7 | 09:01:44 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.5600 |  |
| Jogador 2 | 4-7 | 09:01:45 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 4-7 | 09:01:45 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.1300 |  |
| Jogador 2 | 5-1 | 09:02:22 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-1 | 09:02:22 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.2100 |  |
| Jogador 2 | 5-1 | 09:02:23 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-1 | 09:02:23 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.1500 |  |
| Jogador 2 | 5-1 | 09:02:24 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.1700 |  |
| Jogador 2 | 5-1 | 09:02:24 | MOVE Board -> Board: Veigar (i:4.0) <-> Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-1 | 09:02:24 | MOVE Board -> Board: Varus (i:2.0) <-> Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0300 |  |
| Jogador 2 | 5-1 | 09:02:25 | MOVE Board -> Board: Kobuko (i:2.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.1100 |  |
| Jogador 2 | 5-1 | 09:02:25 | MOVE Board -> Board: Tristana (i:6.0) <-> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-2 | 09:03:02 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-2 | 09:03:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.9600 |  |
| Jogador 2 | 5-2 | 09:03:03 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0500 |  |
| Jogador 2 | 5-2 | 09:03:03 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.1300 |  |
| Jogador 2 | 5-2 | 09:03:04 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0200 |  |
| Jogador 2 | 5-2 | 09:03:04 | MOVE Board -> Board: Yunara (i:4.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-2 | 09:03:05 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-2 | 09:03:05 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-2 | 09:03:05 | MOVE Board -> Board: Veigar (i:4.0) <-> Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-3 | 09:03:43 | VENDEU: Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.2000 |  |
| Jogador 2 | 5-3 | 09:03:44 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.9300 |  |
| Jogador 2 | 5-3 | 09:03:44 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 48 | 3 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.4100 |  |
| Jogador 2 | 5-3 | 09:03:44 | COMPROU: Alune (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Espinhos Negros | DA_18_Alune | 0.2200 |  |
| Jogador 2 | 5-3 | 09:03:45 | MOVE Board -> Board: Varus (i:2.0) <-> Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Espinhos Negros | DA_18_Alune | -0.2400 |  |
| Jogador 2 | 5-3 | 09:03:45 | MOVE Board -> Board: Kobuko (i:2.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Espinhos Negros | DA_18_Alune | 0.2200 |  |
| Jogador 2 | 5-3 | 09:03:46 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Espinhos Negros | DA_18_Alune | -0.0200 |  |
| Jogador 2 | 5-3 | 09:03:46 | MOVE Board -> Board: Veigar (i:4.0) <-> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Espinhos Negros | DA_18_Alune | -0.0700 |  |
| Jogador 2 | 5-3 | 09:03:46 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Espinhos Negros | DA_18_Alune | -0.1600 |  |
| Jogador 2 | 5-4 | 09:04:26 | VENDEU: Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Espinhos Negros | DA_18_Alune | -0.2700 |  |
| Jogador 2 | 5-4 | 09:04:26 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Espinhos Negros | DA_18_Alune | 0.7000 |  |
| Jogador 2 | 5-4 | 09:04:26 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Espinhos Negros | DA_18_Alune | -0.0200 |  |
| Jogador 2 | 5-4 | 09:04:27 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 54 | 4 | Espinhos Negros | DA_CrimsonRaptor18 | 0.9700 |  |
| Jogador 2 | 5-4 | 09:04:27 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 2 | 5-4 | 09:04:28 | MOVE Board -> Board: Yunara (i:4.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 2 | 5-4 | 09:04:28 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0600 |  |
| Jogador 2 | 5-4 | 09:04:28 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_CrimsonRaptor18 | -0.2000 |  |
| Jogador 3 | ? | 08:52:18 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | ? | 08:52:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 08:52:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 08:52:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.7200 |  |
| Jogador 3 | 1-1 | 08:52:26 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-1 | 08:52:28 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 1-1 | 08:52:28 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 08:52:29 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3900 |  |
| Jogador 3 | 1-2 | 08:52:32 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 08:52:33 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 08:52:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 08:52:41 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 08:52:42 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 08:52:43 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1300 |  |
| Jogador 3 | 1-3 | 08:52:43 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 08:52:44 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 08:52:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 08:52:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 1-4 | 08:52:53 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | 1-4 | 08:52:54 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 1-4 | 08:52:55 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.1300 |  |
| Jogador 3 | 1-4 | 08:52:55 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 1-4 | 08:52:56 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 3 | 1-4 | 08:52:57 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 08:52:58 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-1 | 08:53:03 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 08:53:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 2-1 | 08:53:05 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.6600 |  |
| Jogador 3 | 2-1 | 08:53:06 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | -0.3400 |  |
| Jogador 3 | 2-1 | 08:53:06 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.0500 |  |
| Jogador 3 | 2-1 | 08:53:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 2-1 | 08:53:07 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 2-1 | 08:53:08 | MOVE Bench -> Board: Shen (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0600 |  |
| Jogador 3 | 2-2 | 08:53:15 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.3200 |  |
| Jogador 3 | 2-3 | 08:53:29 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | 1.0100 |  |
| Jogador 3 | 2-3 | 08:53:30 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | 0.1500 |  |
| Jogador 3 | 2-3 | 08:53:31 | MOVE Bench -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | -0.1000 |  |
| Jogador 3 | 2-3 | 08:53:32 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Diana | 0.1100 |  |
| Jogador 3 | 2-3 | 08:53:33 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 3 | 2-3 | 08:53:34 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Diana | 0.1500 |  |
| Jogador 3 | 2-3 | 08:53:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.0600 |  |
| Jogador 3 | 2-3 | 08:53:34 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | 0.4000 |  |
| Jogador 3 | 2-4 | 08:53:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Diana | 0.8500 |  |
| Jogador 3 | 2-4 | 08:53:41 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Diana | 0.9800 |  |
| Jogador 3 | 2-4 | 08:53:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 2-4 | 08:53:42 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 3 | 2-4 | 08:53:42 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 2-4 | 08:53:42 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 2-4 | 08:53:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 2-5 | 08:54:00 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Scuttlecrab18 | 0.8700 |  |
| Jogador 3 | 2-5 | 08:54:01 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_Scuttlecrab18 | 1.0500 |  |
| Jogador 3 | 2-5 | 08:54:02 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-5 | 08:54:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 2-5 | 08:54:03 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-5 | 08:54:04 | MOVE Board -> Board: Camille (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-5 | 08:54:04 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Scuttlecrab18 | -0.1900 |  |
| Jogador 3 | 2-5 | 08:54:05 | MOVE Board -> Board: Grompe (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Scuttlecrab18 | 0.1600 |  |
| Jogador 3 | 2-5 | 08:54:06 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-6 | 08:54:22 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Scuttlecrab18 | 0.9000 |  |
| Jogador 3 | 2-6 | 08:54:23 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yorick | 0.3400 |  |
| Jogador 3 | 2-6 | 08:54:23 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yorick | 0.5200 |  |
| Jogador 3 | 2-6 | 08:54:24 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-6 | 08:54:25 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 3 | 2-6 | 08:54:25 | MOVE Board -> Board: Camille (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 3 | 2-6 | 08:54:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-7 | 08:54:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Yorick | 0.2200 |  |
| Jogador 3 | 2-7 | 08:54:38 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 3 | 2-7 | 08:54:38 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Diana (i:6.0) (tabuleiro slot 6) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Yorick | 0.1200 |  |
| Jogador 3 | 2-7 | 08:54:39 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Diana (i:6.0) (tabuleiro slot 6) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Yorick | 0.1400 |  |
| Jogador 3 | 2-7 | 08:54:40 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Yorick | 0.2800 |  |
| Jogador 3 | 2-7 | 08:54:40 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Yorick | -0.2700 |  |
| Jogador 3 | 2-7 | 08:54:40 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Yorick | 0.0800 |  |
| Jogador 3 | 2-7 | 08:54:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 3 | 2-7 | 08:54:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 3 | 2-7 | 08:54:42 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yorick | 0.4100 |  |
| Jogador 3 | 3-1 | 08:55:00 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Yorick | 0.0500 |  |
| Jogador 3 | 3-1 | 08:55:00 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Diana | -0.3700 |  |
| Jogador 3 | 3-1 | 08:55:01 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Diana | 0.0500 |  |
| Jogador 3 | 3-1 | 08:55:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-1 | 08:55:02 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 3 | 3-1 | 08:55:02 | MOVE Bench -> Board: Rengar (i:6.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Diana | -0.0800 |  |
| Jogador 3 | 3-1 | 08:55:03 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.1600 |  |
| Jogador 3 | 3-1 | 08:55:04 | MOVE Board -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-1 | 08:55:04 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 3-2 | 08:55:22 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Diana | 0.0200 |  |
| Jogador 3 | 3-2 | 08:55:22 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | -0.1300 |  |
| Jogador 3 | 3-2 | 08:55:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-2 | 08:55:23 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Diana | 0.0200 |  |
| Jogador 3 | 3-2 | 08:55:24 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-2 | 08:55:24 | MOVE Board -> Board: Grompe (i:4.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-2 | 08:55:25 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 3-2 | 08:55:25 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-2 | 08:55:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-3 | 08:55:44 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 3 | 3-3 | 08:55:45 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | 0.7300 |  |
| Jogador 3 | 3-3 | 08:55:45 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-3 | 08:55:46 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-3 | 08:55:46 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | 0.1800 |  |
| Jogador 3 | 3-3 | 08:55:47 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-3 | 08:55:47 | MOVE Board -> Board: Shen (i:4.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-3 | 08:55:48 | MOVE Board -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-3 | 08:55:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-4 | 08:56:08 | VENDEU: Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Diana | -0.2400 |  |
| Jogador 3 | 3-4 | 08:56:08 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | 0.7600 |  |
| Jogador 3 | 3-4 | 08:56:09 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.1800 |  |
| Jogador 3 | 3-4 | 08:56:09 | VENDEU: Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Diana | -0.3100 |  |
| Jogador 3 | 3-4 | 08:56:10 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | 0.0800 |  |
| Jogador 3 | 3-4 | 08:56:11 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-4 | 08:56:11 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-4 | 08:56:12 | MOVE Board -> Board: Grompe (i:4.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0600 |  |
| Jogador 3 | 3-4 | 08:56:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-5 | 08:56:33 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Diana | 0.5100 |  |
| Jogador 3 | 3-5 | 08:56:34 | VENDEU: Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Diana | 0.0200 |  |
| Jogador 3 | 3-5 | 08:56:34 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | 0.2200 |  |
| Jogador 3 | 3-5 | 08:56:35 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.1000 |  |
| Jogador 3 | 3-5 | 08:56:35 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.5800 |  |
| Jogador 3 | 3-5 | 08:56:36 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-5 | 08:56:37 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 3-5 | 08:56:37 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Nidalee18_AP | -0.0200 |  |
| Jogador 3 | 3-5 | 08:56:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 3-6 | 08:57:01 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Nidalee18_AP | 0.0100 |  |
| Jogador 3 | 3-6 | 08:57:01 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Nidalee18_AP | 0.2100 |  |
| Jogador 3 | 3-6 | 08:57:01 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 3 | 3-6 | 08:57:02 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Nidalee18_AP | -0.1400 |  |
| Jogador 3 | 3-6 | 08:57:03 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-6 | 08:57:03 | MOVE Board -> Board: Shen (i:4.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-6 | 08:57:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Diana | 0.1200 |  |
| Jogador 3 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Diana | 0.1000 |  |
| Jogador 3 | 3-7 | 08:57:31 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Diana | 0.0500 |  |
| Jogador 3 | 3-7 | 08:57:31 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Diana | 0.6500 |  |
| Jogador 3 | 3-7 | 08:57:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-7 | 08:57:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-7 | 08:57:32 | MOVE Board -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-7 | 08:57:33 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-7 | 08:57:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-1 | 08:58:03 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Diana | -0.2300 |  |
| Jogador 3 | 4-1 | 08:58:04 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | -0.0300 |  |
| Jogador 3 | 4-1 | 08:58:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-1 | 08:58:05 | MOVE Board -> Board: Grompe (i:4.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 4-1 | 08:58:05 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-1 | 08:58:06 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-2 | 08:58:37 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_18_Diana | 0.0900 |  |
| Jogador 3 | 4-2 | 08:58:37 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Diana | -0.0700 |  |
| Jogador 3 | 4-2 | 08:58:38 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-2 | 08:58:38 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-2 | 08:58:40 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 4-2 | 08:58:40 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-2 | 08:58:41 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-3 | 08:59:11 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 3 | 4-3 | 08:59:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Diana | 0.2500 |  |
| Jogador 3 | 4-3 | 08:59:12 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Diana | 0.0300 |  |
| Jogador 3 | 4-3 | 08:59:12 | MOVE Board -> Board: Shen (i:4.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-3 | 08:59:13 | MOVE Board -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-3 | 08:59:13 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-4 | 08:59:46 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Diana | 0.0700 |  |
| Jogador 3 | 4-4 | 08:59:46 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_Vi18 | 0.7500 |  |
| Jogador 3 | 4-4 | 08:59:47 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_Vi18 | 0.2500 |  |
| Jogador 3 | 4-4 | 08:59:47 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_Vi18 | 0.1700 |  |
| Jogador 3 | 4-4 | 08:59:47 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_Vi18 | 0.0300 |  |
| Jogador 3 | 4-4 | 08:59:48 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 3 | 4-4 | 08:59:48 | MOVE Board -> Board: Grompe (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 3 | 4-4 | 08:59:49 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 3 | 4-5 | 09:00:25 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 0 | Colosso | DA_18_Diana | -0.2200 |  |
| Jogador 3 | 4-5 | 09:00:26 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Colosso | DA_18_Diana | 0.2900 |  |
| Jogador 3 | 4-5 | 09:00:26 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-5 | 09:00:27 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_18_Diana | -0.2500 |  |
| Jogador 3 | 4-5 | 09:00:27 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 4-5 | 09:00:28 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 3 | 4-5 | 09:00:28 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_Nidalee18_AP | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-6 | 09:01:03 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Colosso | DA_Nidalee18_AP | -0.0300 |  |
| Jogador 3 | 4-6 | 09:01:03 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Colosso | DA_Nidalee18_AP | 0.3000 |  |
| Jogador 3 | 4-6 | 09:01:04 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Colosso | DA_Nidalee18_AP | -0.2400 |  |
| Jogador 3 | 4-6 | 09:01:04 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Colosso | DA_Nidalee18_AP | 0.1700 |  |
| Jogador 3 | 4-6 | 09:01:05 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 4-6 | 09:01:05 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_Nidalee18_AP | -0.1100 |  |
| Jogador 3 | 4-6 | 09:01:06 | MOVE Board -> Board: Shen (i:4.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 4-6 | 09:01:06 | MOVE Board -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 3 | 4-6 | 09:01:07 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_Nidalee18_AP | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Colosso | DA_Nidalee18_AP | 0.1400 |  |
| Jogador 3 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Colosso | DA_Nidalee18_AP | 0.1100 |  |
| Jogador 3 | 4-7 | 09:01:43 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 1 | Colosso | DA_Nidalee18_AP | 0.0100 |  |
| Jogador 3 | 4-7 | 09:01:43 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 1 | Colosso | DA_Nidalee18_AP | 0.1800 |  |
| Jogador 3 | 4-7 | 09:01:43 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 1 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 4-7 | 09:01:44 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Colosso | DA_Nidalee18_AP | 0.0500 |  |
| Jogador 3 | 4-7 | 09:01:44 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 4-7 | 09:01:45 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Colosso | DA_Nidalee18_AP | -0.0200 |  |
| Jogador 3 | 4-7 | 09:01:45 | MOVE Board -> Board: Grompe (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Colosso | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 3 | 5-1 | 09:02:22 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Colosso | DA_Nidalee18_AP | 0.0100 |  |
| Jogador 3 | 5-1 | 09:02:22 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Colosso | DA_Nidalee18_AP | 0.8700 |  |
| Jogador 3 | 5-1 | 09:02:23 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 2 | Colosso | DA_Nidalee18_AP | -0.0400 |  |
| Jogador 3 | 5-1 | 09:02:23 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Colosso | DA_Nidalee18_AP | 0.1200 |  |
| Jogador 3 | 5-1 | 09:02:24 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Colosso | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 3 | 5-1 | 09:02:24 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Colosso | DA_Nidalee18_AP | -0.0200 |  |
| Jogador 3 | 5-1 | 09:02:24 | MOVE Board -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 5-1 | 09:02:25 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Colosso | DA_18_Diana | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 5-2 | 09:03:02 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 3 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 3 | 5-2 | 09:03:02 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 3 | Colosso | DA_18_Diana | 0.8600 |  |
| Jogador 3 | 5-2 | 09:03:03 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Colosso | DA_18_Diana | -0.2600 |  |
| Jogador 3 | 5-2 | 09:03:03 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_18_Diana | 0.3300 |  |
| Jogador 3 | 5-2 | 09:03:04 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-2 | 09:03:04 | MOVE Board -> Board: Grompe (i:4.0) <-> Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 5-2 | 09:03:05 | MOVE Board -> Board: Camille (i:2.0) <-> Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 5-2 | 09:03:05 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_18_Diana | -0.1700 |  |
| Jogador 4 | ? | 08:52:18 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3500 |  |
| Jogador 4 | ? | 08:52:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 08:52:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 08:52:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.7100 |  |
| Jogador 4 | 1-1 | 08:52:26 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 4 | 1-1 | 08:52:28 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 1-1 | 08:52:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 08:52:29 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4000 |  |
| Jogador 4 | 1-2 | 08:52:32 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 08:52:33 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 08:52:33 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 08:52:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 1-2 | 08:52:37 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 1-3 | 08:52:41 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 1.0100 |  |
| Jogador 4 | 1-3 | 08:52:42 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.3000 |  |
| Jogador 4 | 1-3 | 08:52:43 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 4 | 1-3 | 08:52:43 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-3 | 08:52:44 | MOVE Board -> Board: Camille (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 1-3 | 08:52:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-4 | 08:52:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.9800 |  |
| Jogador 4 | 1-4 | 08:52:53 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.1900 |  |
| Jogador 4 | 1-4 | 08:52:54 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.1400 |  |
| Jogador 4 | 1-4 | 08:52:55 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.5100 |  |
| Jogador 4 | 1-4 | 08:52:55 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.4800 |  |
| Jogador 4 | 1-4 | 08:52:56 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1900 |  |
| Jogador 4 | 1-4 | 08:52:57 | MOVE Board -> Board: Akali (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 1-4 | 08:52:58 | MOVE Board -> Board: Camille (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 2-1 | 08:53:03 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 0.7500 |  |
| Jogador 4 | 2-1 | 08:53:04 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.0500 |  |
| Jogador 4 | 2-1 | 08:53:05 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 2-1 | 08:53:06 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | -0.1200 |  |
| Jogador 4 | 2-1 | 08:53:06 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Krug18 | -0.0100 |  |
| Jogador 4 | 2-1 | 08:53:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | -0.0400 |  |
| Jogador 4 | 2-1 | 08:53:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 4 | 2-1 | 08:53:08 | MOVE Board -> Board: Camille (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | -0.0100 |  |
| Jogador 4 | 2-2 | 08:53:15 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.9500 |  |
| Jogador 4 | 2-3 | 08:53:29 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 4 | 2-3 | 08:53:30 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Akali_AD | 0.5300 |  |
| Jogador 4 | 2-3 | 08:53:31 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 08:53:32 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.8100 |  |
| Jogador 4 | 2-3 | 08:53:33 | MOVE Board -> Board: Karma (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 4 | 2-3 | 08:53:34 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 4 | 2-3 | 08:53:34 | MOVE Board -> Board: Krugue (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 4 | 2-3 | 08:53:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 4 | 2-4 | 08:53:40 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Aphelios | -0.2400 |  |
| Jogador 4 | 2-4 | 08:53:41 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Aphelios | 0.8200 |  |
| Jogador 4 | 2-4 | 08:53:41 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Aphelios | -0.2500 |  |
| Jogador 4 | 2-4 | 08:53:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Xayah | 0.9500 |  |
| Jogador 4 | 2-4 | 08:53:42 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Xayah | 0.3200 |  |
| Jogador 4 | 2-4 | 08:53:42 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Xayah | 0.0400 |  |
| Jogador 4 | 2-4 | 08:53:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Xayah | -0.0400 |  |
| Jogador 4 | 2-4 | 08:53:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Xayah | -0.0400 |  |
| Jogador 4 | 2-4 | 08:53:44 | MOVE Board -> Board: Karma (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Xayah | -0.0100 |  |
| Jogador 4 | 2-4 | 08:53:45 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Xayah | -0.0100 |  |
| Jogador 4 | 2-5 | 08:54:00 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Aphelios | -0.2100 |  |
| Jogador 4 | 2-5 | 08:54:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Aphelios | 0.9000 |  |
| Jogador 4 | 2-5 | 08:54:02 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Aphelios | 0.0200 |  |
| Jogador 4 | 2-5 | 08:54:02 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Aphelios | 0.0700 |  |
| Jogador 4 | 2-5 | 08:54:03 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Aphelios | -0.2800 |  |
| Jogador 4 | 2-5 | 08:54:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-5 | 08:54:04 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Aphelios | 0.1400 |  |
| Jogador 4 | 2-5 | 08:54:05 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-5 | 08:54:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-6 | 08:54:22 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Aphelios | 0.0500 |  |
| Jogador 4 | 2-6 | 08:54:23 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | 0.8700 |  |
| Jogador 4 | 2-6 | 08:54:23 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.8700 |  |
| Jogador 4 | 2-6 | 08:54:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | 0.1300 |  |
| Jogador 4 | 2-6 | 08:54:25 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 2-6 | 08:54:25 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.0800 |  |
| Jogador 4 | 2-6 | 08:54:26 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | -0.7000 |  |
| Jogador 4 | 2-6 | 08:54:28 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.5500 |  |
| Jogador 4 | 2-7 | 08:54:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | 2-7 | 08:54:38 | MOVE Bench -> Board: Akali (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 2-7 | 08:54:38 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Rakan | 0.4700 |  |
| Jogador 4 | 2-7 | 08:54:39 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 2-7 | 08:54:40 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 2-7 | 08:54:40 | MOVE Board -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-7 | 08:54:40 | MOVE Board -> Board: Karma (i:2.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 2-7 | 08:54:41 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 3-1 | 08:55:00 | VENDEU: Camille (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_18_Rakan | -0.1700 |  |
| Jogador 4 | 3-1 | 08:55:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Yorick | 0.7700 |  |
| Jogador 4 | 3-1 | 08:55:01 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Yorick | 0.2900 |  |
| Jogador 4 | 3-1 | 08:55:01 | MOVE Bench -> Board: Yunara (i:4.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_18_Yorick | -0.7700 |  |
| Jogador 4 | 3-1 | 08:55:02 | MOVE Bench -> Board: Varus (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Yorick | 0.1700 |  |
| Jogador 4 | 3-1 | 08:55:02 | MOVE Bench -> Board: Yunara (i:4.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-1 | 08:55:03 | MOVE Bench -> Board: Krugue (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_18_Yorick | -0.8000 |  |
| Jogador 4 | 3-1 | 08:55:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-2 | 08:55:22 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Colosso | DA_18_Yorick | 0.7300 |  |
| Jogador 4 | 3-2 | 08:55:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-2 | 08:55:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 3-2 | 08:55:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 1 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-2 | 08:55:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-2 | 08:55:24 | MOVE Board -> Board: Yunara (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Yorick | 0.0300 |  |
| Jogador 4 | 3-2 | 08:55:25 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Yorick | -0.1100 |  |
| Jogador 4 | 3-2 | 08:55:25 | MOVE Board -> Board: Aphelios (i:8.0) <-> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Yorick | -0.0800 |  |
| Jogador 4 | 3-2 | 08:55:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-3 | 08:55:44 | VENDEU: Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Rakan | -0.2900 |  |
| Jogador 4 | 3-3 | 08:55:45 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Rakan | 0.6500 |  |
| Jogador 4 | 3-3 | 08:55:45 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Aphelios (i:8.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 3-3 | 08:55:46 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Aphelios (i:8.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Rakan | 0.1400 |  |
| Jogador 4 | 3-3 | 08:55:46 | EQUIP_FROM_INVENTORY: TFT_Item_RunaansHurricane -> Aphelios (i:8.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Rakan | 0.1300 |  |
| Jogador 4 | 3-3 | 08:55:47 | VENDEU: Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Aphelios | -0.2600 |  |
| Jogador 4 | 3-3 | 08:55:47 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Akali_AD | 0.6900 |  |
| Jogador 4 | 3-3 | 08:55:48 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Akali_AD | 0.0900 |  |
| Jogador 4 | 3-3 | 08:55:48 | MOVE Bench -> Board: Varus (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Akali_AD | -0.3100 |  |
| Jogador 4 | 3-4 | 08:56:08 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Akali_AD | 0.6600 |  |
| Jogador 4 | 3-4 | 08:56:08 | MOVE Bench -> Board: Krugue (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Akali_AD | -0.7300 |  |
| Jogador 4 | 3-4 | 08:56:09 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 4 | 3-4 | 08:56:09 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Akali_AD | 0.1500 |  |
| Jogador 4 | 3-4 | 08:56:10 | MOVE Bench -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Akali_AD | -0.7400 |  |
| Jogador 4 | 3-4 | 08:56:11 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Akali_AD | -0.3100 |  |
| Jogador 4 | 3-4 | 08:56:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 08:56:33 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Akali_AD | -0.8100 |  |
| Jogador 4 | 3-5 | 08:56:34 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Akali_AD | 0.1600 |  |
| Jogador 4 | 3-5 | 08:56:34 | MOVE Bench -> Board: Krugue (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Akali_AD | -0.1000 |  |
| Jogador 4 | 3-5 | 08:56:35 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Akali_AD | -0.8300 |  |
| Jogador 4 | 3-5 | 08:56:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 08:57:01 | VENDEU: Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Colosso | DA_18_Aphelios | -0.3100 |  |
| Jogador 4 | 3-6 | 08:57:01 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_18_MasterYi_AD | 0.7800 |  |
| Jogador 4 | 3-6 | 08:57:01 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 4 | 3-6 | 08:57:02 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_18_MasterYi_AD | 0.5000 |  |
| Jogador 4 | 3-6 | 08:57:03 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Colosso | DA_18_MasterYi_AD | 0.2200 |  |
| Jogador 4 | 3-6 | 08:57:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 3-6 | 08:57:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Colosso | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 4 | 3-6 | 08:57:04 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Colosso | DA_18_MasterYi_AD | 0.7900 |  |
| Jogador 4 | 3-6 | 08:57:05 | MOVE Board -> Board: Diana (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Colosso | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-7 | 08:57:30 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_MasterYi_AD | 0.6800 |  |
| Jogador 4 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_MasterYi_AD | 0.2300 |  |
| Jogador 4 | 3-7 | 08:57:31 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 4 | 3-7 | 08:57:31 | MOVE Board -> Board: Sejuani (i:4.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-7 | 08:57:32 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 08:57:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_MasterYi_AD | -0.1100 |  |
| Jogador 4 | 4-1 | 08:58:03 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Colosso | DA_18_MasterYi_AD | 0.7800 |  |
| Jogador 4 | 4-1 | 08:58:04 | MOVE Bench -> Board: Yunara (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Colosso | DA_18_MasterYi_AD | 0.5600 |  |
| Jogador 4 | 4-1 | 08:58:04 | MOVE Board -> Board: Yunara (i:8.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Colosso | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-1 | 08:58:05 | MOVE Board -> Board: Karma (i:2.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Colosso | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 4 | 4-1 | 08:58:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Colosso | DA_18_MasterYi_AD | -0.1100 |  |
| Jogador 4 | 4-2 | 08:58:37 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Colosso | DA_18_MasterYi_AD | 0.6900 |  |
| Jogador 4 | 4-2 | 08:58:37 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Colosso | DA_18_MasterYi_AD | 0.2300 |  |
| Jogador 4 | 4-2 | 08:58:38 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 08:58:38 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Colosso | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 4 | 4-2 | 08:58:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 2 | Colosso | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 4 | 4-2 | 08:58:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Colosso | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 4 | 4-2 | 08:58:41 | MOVE Board -> Board: Krugue (i:6.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 08:58:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 2 | Colosso | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 4 | 4-2 | 08:58:41 | MOVE Board -> Board: Karma (i:2.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 2 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-3 | 08:59:11 | VENDEU: Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Colosso | DA_18_Yunara | -0.2400 |  |
| Jogador 4 | 4-3 | 08:59:11 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Yunara | 0.7500 |  |
| Jogador 4 | 4-3 | 08:59:12 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yunara (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Yunara | -0.0600 |  |
| Jogador 4 | 4-3 | 08:59:12 | MOVE Board -> Board: Yunara (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Yunara | 0.0400 |  |
| Jogador 4 | 4-3 | 08:59:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-3 | 08:59:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Colosso | DA_18_Yunara | -0.0700 |  |
| Jogador 4 | 4-3 | 08:59:14 | MOVE Board -> Board: Yunara (i:8.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-3 | 08:59:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Colosso | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-3 | 08:59:15 | MOVE Board -> Board: Krugue (i:6.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-4 | 08:59:46 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_18_Yunara | 0.0200 |  |
| Jogador 4 | 4-4 | 08:59:46 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Colosso | DA_18_Yunara | 0.0200 |  |
| Jogador 4 | 4-4 | 08:59:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Colosso | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-4 | 08:59:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Colosso | DA_18_Yunara | -0.0900 |  |
| Jogador 4 | 4-4 | 08:59:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 1 | Colosso | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 4-4 | 08:59:48 | MOVE Board -> Board: Karma (i:2.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 1 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-4 | 08:59:48 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 1 | Colosso | DA_18_Yunara | -0.0200 |  |
| Jogador 4 | 4-4 | 08:59:49 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 1 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-5 | 09:00:25 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Colosso | DA_18_Yunara | 0.0700 |  |
| Jogador 4 | 4-5 | 09:00:26 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Colosso | DA_18_Yunara | 0.2800 |  |
| Jogador 4 | 4-5 | 09:00:26 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Colosso | DA_18_Yunara | -0.0600 |  |
| Jogador 4 | 4-5 | 09:00:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Yunara | 0.2200 |  |
| Jogador 4 | 4-5 | 09:00:27 | MOVE Board -> Board: Aphelios (i:8.0) <-> Yunara (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-5 | 09:00:28 | MOVE Board -> Board: Yunara (i:8.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Yunara | -0.0200 |  |
| Jogador 4 | 4-5 | 09:00:28 | MOVE Board -> Board: Krugue (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Yunara | -0.0200 |  |
| Jogador 4 | 4-5 | 09:00:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Yunara | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-6 | 09:01:03 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Colosso | DA_18_Yunara | 0.0700 |  |
| Jogador 4 | 4-6 | 09:01:03 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_18_Diana | 0.7800 |  |
| Jogador 4 | 4-6 | 09:01:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Colosso | DA_18_Diana | 0.2900 |  |
| Jogador 4 | 4-6 | 09:01:04 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Colosso | DA_18_Diana | 0.5700 |  |
| Jogador 4 | 4-6 | 09:01:05 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_18_Diana | 0.2800 |  |
| Jogador 4 | 4-6 | 09:01:05 | MOVE Board -> Board: Yunara (i:4.0) <-> Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 4 | 4-6 | 09:01:06 | MOVE Board -> Board: Aphelios (i:8.0) <-> Yunara (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 4 | 4-6 | 09:01:06 | MOVE Board -> Board: Yunara (i:8.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 4 | 4-6 | 09:01:07 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 4 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_18_Diana | 0.1500 |  |
| Jogador 4 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_18_Diana | 0.0900 |  |
| Jogador 4 | 4-7 | 09:01:43 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 1 | Colosso | DA_18_Yunara | -0.2000 |  |
| Jogador 4 | 4-7 | 09:01:43 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 24 | 1 | Colosso | DA_CrimsonRaptor18 | 0.8800 |  |
| Jogador 4 | 4-7 | 09:01:43 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Sejuani (i:4.0) (tabuleiro slot 6) | STABILIZE | STABILIZE: pressão de vida | 24 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 4 | 4-7 | 09:01:44 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Yunara (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 24 | 1 | Colosso | DA_CrimsonRaptor18 | 0.1400 |  |
| Jogador 4 | 4-7 | 09:01:44 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Colosso | DA_CrimsonRaptor18 | 0.3000 |  |
| Jogador 4 | 4-7 | 09:01:45 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 4 | 4-7 | 09:01:45 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 4 | 5-1 | 09:02:22 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_CrimsonRaptor18 | 0.1600 |  |
| Jogador 4 | 5-1 | 09:02:22 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_CrimsonRaptor18 | 0.5100 |  |
| Jogador 4 | 5-1 | 09:02:23 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_CrimsonRaptor18 | 0.1900 |  |
| Jogador 4 | 5-1 | 09:02:23 | MOVE Board -> Board: Vi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 5-1 | 09:02:24 | MOVE Board -> Board: Sejuani (i:4.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 4 | 5-1 | 09:02:24 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 5-2 | 09:03:02 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 1 | Colosso | DA_18_Yunara | -0.3400 |  |
| Jogador 4 | 5-2 | 09:03:02 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Colosso | DA_18_Yunara | 0.0700 |  |
| Jogador 4 | 5-2 | 09:03:03 | MOVE Board -> Board: Krugue (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 5-2 | 09:03:03 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Colosso | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 5-2 | 09:03:04 | MOVE Board -> Board: Yunara (i:4.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Florescer | DA_18_Yunara | -0.0200 |  |
| Jogador 4 | 5-2 | 09:03:04 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Florescer | DA_18_Yunara | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 5-3 | 09:03:43 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 5-3 | 09:03:44 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_18_Yunara | 0.2300 |  |
| Jogador 4 | 5-3 | 09:03:44 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 5-3 | 09:03:44 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Florescer | DA_18_Yunara | 0.0700 |  |
| Jogador 4 | 5-3 | 09:03:45 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Florescer | DA_18_Yunara | -0.0500 |  |
| Jogador 4 | 5-3 | 09:03:45 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 25 | 2 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 5-3 | 09:03:46 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 21 | 2 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 5-3 | 09:03:46 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 17 | 2 | Florescer | DA_18_Yunara | -0.0500 |  |
| Jogador 4 | 5-3 | 09:03:46 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 13 | 2 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 5-4 | 09:04:26 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 5-4 | 09:04:26 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Florescer | DA_18_Yunara | 0.1300 |  |
| Jogador 4 | 5-4 | 09:04:26 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Florescer | DA_18_Yunara | 0.0600 |  |
| Jogador 4 | 5-4 | 09:04:27 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Florescer | DA_18_Yunara | 0.7300 |  |
| Jogador 4 | 5-4 | 09:04:27 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 5-4 | 09:04:28 | MOVE Board -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 5-4 | 09:04:28 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Florescer | DA_18_Yunara | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 5-5 | 09:05:10 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 1 | Florescer | DA_18_Yunara | -0.0500 |  |
| Jogador 4 | 5-5 | 09:05:10 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Florescer | DA_18_Yunara | 0.8400 |  |
| Jogador 4 | 5-5 | 09:05:11 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 1 | Florescer | DA_18_Yunara | -0.1300 |  |
| Jogador 4 | 5-5 | 09:05:11 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Florescer | DA_Krug18 | 0.8800 |  |
| Jogador 4 | 5-5 | 09:05:11 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Florescer | DA_Krug18 | 0.6000 |  |
| Jogador 4 | 5-5 | 09:05:12 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Florescer | DA_Krug18 | -0.0200 |  |
| Jogador 4 | 5-5 | 09:05:12 | MOVE Board -> Board: Aphelios (i:8.0) <-> Yunara (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Florescer | DA_Krug18 | -0.0100 |  |
| Jogador 4 | 5-5 | 09:05:12 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Florescer | DA_Krug18 | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 5-6 | 09:05:53 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Florescer | DA_Krug18 | 0.8500 |  |
| Jogador 4 | 5-6 | 09:05:55 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Florescer | DA_Krug18 | 0.7600 |  |
| Jogador 4 | 5-6 | 09:05:55 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 22 | 2 | Florescer | DA_Krug18 | 0.0300 |  |
| Jogador 4 | 5-6 | 09:05:56 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 18 | 2 | Florescer | DA_Krug18 | -0.0500 |  |
| Jogador 4 | 5-6 | 09:05:56 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 14 | 2 | Florescer | DA_Krug18 | 0.0300 |  |
| Jogador 4 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 10 | 2 | Florescer | DA_Krug18 | 0.0300 |  |
| Jogador 4 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 6 | 2 | Florescer | DA_Krug18 | -0.0500 |  |
| Jogador 4 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 2 | Florescer | DA_Krug18 | 0.0300 |  |
| Jogador 4 | 5-6 | 09:05:58 | MOVE Board -> Board: Yunara (i:8.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 2 | Florescer | DA_Krug18 | -0.0400 |  |
| Jogador 4 | 5-7 | 09:06:41 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Yunara (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Florescer | DA_Krug18 | 0.1400 |  |
| Jogador 4 | 5-7 | 09:06:41 | VENDEU: Krugue (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Florescer | DA_18_Yunara | -0.2800 |  |
| Jogador 4 | 5-7 | 09:06:42 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Florescer | DA_Nidalee18_AP | 0.8300 |  |
| Jogador 4 | 5-7 | 09:06:42 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Florescer | DA_Nidalee18_AP | 0.1800 |  |
| Jogador 4 | 5-7 | 09:06:43 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Florescer | DA_Nidalee18_AP | 0.5800 |  |
| Jogador 4 | 5-7 | 09:06:43 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Florescer | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 4 | 5-7 | 09:06:43 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Florescer | DA_Nidalee18_AP | 0.0300 |  |
| Jogador 4 | 5-7 | 09:06:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Florescer | DA_Nidalee18_AP | 0.4200 |  |
| Jogador 4 | 5-7 | 09:06:44 | MOVE Board -> Board: Rakan (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Florescer | DA_Nidalee18_AP | -0.1200 |  |
| Jogador 4 | 6-1 | 09:07:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Florescer | DA_Nidalee18_AP | 0.2800 |  |
| Jogador 4 | 6-1 | 09:07:27 | MOVE Board -> Board: Yunara (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Florescer | DA_Nidalee18_AP | 0.1000 |  |
| Jogador 4 | 6-1 | 09:07:28 | COMPROU: Lux (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Florescer | DA_Nidalee18_AP | -0.1800 |  |
| Jogador 4 | 6-1 | 09:07:28 | MOVE Board -> Board: Master Yi (i:6.0) <-> Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Florescer | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 4 | 6-1 | 09:07:28 | MOVE Board -> Board: Aphelios (i:8.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Florescer | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 4 | 6-1 | 09:07:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Florescer | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 4 | 6-2 | 09:08:13 | VENDEU: Nidalee (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 0 | Florescer | DA_18_Yunara | -0.2200 |  |
| Jogador 4 | 6-2 | 09:08:13 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 0 | Florescer | DA_18_Yunara | 0.1300 |  |
| Jogador 4 | 6-2 | 09:08:14 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 0 | Florescer | DA_18_Yunara | 0.0600 |  |
| Jogador 4 | 6-2 | 09:08:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 0 | Florescer | DA_18_Yunara | 0.1300 |  |
| Jogador 4 | 6-2 | 09:08:14 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 6-2 | 09:08:15 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 6-2 | 09:08:15 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Florescer | DA_18_Yunara | -0.0500 |  |
| Jogador 4 | 6-2 | 09:08:16 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 6-2 | 09:08:16 | MOVE Board -> Board: Vi (i:6.0) <-> Yunara (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Florescer | DA_18_Yunara | 0.0200 |  |
| Jogador 4 | 6-3 | 09:09:00 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Florescer | DA_18_Yunara | -0.0500 |  |
| Jogador 4 | 6-3 | 09:09:00 | MOVE Board -> Board: Yunara (i:8.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 6-3 | 09:09:01 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 6-3 | 09:09:01 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 6-3 | 09:09:01 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 6-3 | 09:09:02 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 6-3 | 09:09:02 | MOVE Board -> Board: Rakan (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Florescer | DA_18_Yunara | -0.0200 |  |
| Jogador 4 | 6-3 | 09:09:03 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 6-4 | 09:09:47 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Florescer | DA_18_Yunara | 0.0600 |  |
| Jogador 4 | 6-4 | 09:09:48 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Florescer | DA_18_Yunara | 0.2000 |  |
| Jogador 4 | 6-4 | 09:09:48 | VENDEU: Lux (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Florescer | DA_18_Yunara | 0.1000 |  |
| Jogador 4 | 6-4 | 09:09:48 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Florescer | DA_18_Yunara | 0.1800 |  |
| Jogador 4 | 6-4 | 09:09:49 | MOVE Board -> Board: Yunara (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 6-4 | 09:09:49 | MOVE Board -> Board: Master Yi (i:6.0) <-> Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 6-4 | 09:09:50 | MOVE Board -> Board: Aphelios (i:8.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 6-4 | 09:09:50 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | ? | 08:52:18 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.3200 |  |
| Jogador 5 | ? | 08:52:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 08:52:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 08:52:25 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.6400 |  |
| Jogador 5 | 1-1 | 08:52:26 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.4200 |  |
| Jogador 5 | 1-1 | 08:52:28 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | 1-1 | 08:52:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 08:52:29 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4200 |  |
| Jogador 5 | 1-2 | 08:52:32 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | 1-2 | 08:52:33 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0600 |  |
| Jogador 5 | 1-2 | 08:52:33 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.3200 |  |
| Jogador 5 | 1-2 | 08:52:35 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.3000 |  |
| Jogador 5 | 1-2 | 08:52:37 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 08:52:41 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 08:52:42 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.3100 |  |
| Jogador 5 | 1-3 | 08:52:43 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0100 |  |
| Jogador 5 | 1-3 | 08:52:43 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | -0.1900 |  |
| Jogador 5 | 1-3 | 08:52:44 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.1600 |  |
| Jogador 5 | 1-3 | 08:52:44 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | -0.0100 |  |
| Jogador 5 | 1-3 | 08:52:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | -0.0100 |  |
| Jogador 5 | 1-3 | 08:52:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 1-4 | 08:52:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | 0.9600 |  |
| Jogador 5 | 1-4 | 08:52:53 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | 0.2100 |  |
| Jogador 5 | 1-4 | 08:52:54 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | 0.1800 |  |
| Jogador 5 | 1-4 | 08:52:55 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | 0.4200 |  |
| Jogador 5 | 1-4 | 08:52:55 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2000 |  |
| Jogador 5 | 1-4 | 08:52:56 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 1-4 | 08:52:57 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 1-4 | 08:52:58 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.1800 |  |
| Jogador 5 | 2-1 | 08:53:03 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Cassiopeia | 1.0300 |  |
| Jogador 5 | 2-1 | 08:53:04 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.3200 |  |
| Jogador 5 | 2-1 | 08:53:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 2-1 | 08:53:06 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.3400 |  |
| Jogador 5 | 2-1 | 08:53:06 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.0900 |  |
| Jogador 5 | 2-1 | 08:53:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-1 | 08:53:07 | MOVE Board -> Board: Veigar (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 2-1 | 08:53:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-2 | 08:53:15 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | 1.0500 |  |
| Jogador 5 | 2-3 | 08:53:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-3 | 08:53:30 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | -0.5300 |  |
| Jogador 5 | 2-3 | 08:53:31 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 5 | 2-3 | 08:53:32 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 5 | 2-3 | 08:53:33 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.1700 |  |
| Jogador 5 | 2-3 | 08:53:34 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | -0.0200 |  |
| Jogador 5 | 2-3 | 08:53:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0400 |  |
| Jogador 5 | 2-3 | 08:53:34 | MOVE Board -> Board: Tristana (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 5 | 2-4 | 08:53:40 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Rakan | 0.2800 |  |
| Jogador 5 | 2-4 | 08:53:41 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Rakan | 0.2900 |  |
| Jogador 5 | 2-4 | 08:53:41 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Rakan | 0.0300 |  |
| Jogador 5 | 2-4 | 08:53:42 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-4 | 08:53:42 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | -0.3200 |  |
| Jogador 5 | 2-4 | 08:53:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 2-4 | 08:53:43 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.1200 |  |
| Jogador 5 | 2-4 | 08:53:44 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-4 | 08:53:44 | MOVE Board -> Board: Tristana (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 2-4 | 08:53:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-5 | 08:54:00 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Tristana | 0.6900 |  |
| Jogador 5 | 2-5 | 08:54:01 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Tristana | -0.1500 |  |
| Jogador 5 | 2-5 | 08:54:02 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 2-5 | 08:54:02 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_Tristana | -0.0500 |  |
| Jogador 5 | 2-5 | 08:54:03 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-5 | 08:54:04 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Tristana | -0.2300 |  |
| Jogador 5 | 2-5 | 08:54:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 2-5 | 08:54:05 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-5 | 08:54:06 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | -0.3600 |  |
| Jogador 5 | 2-6 | 08:54:22 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | 0.0200 |  |
| Jogador 5 | 2-6 | 08:54:23 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | 0.8500 |  |
| Jogador 5 | 2-6 | 08:54:23 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-6 | 08:54:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | 0.6900 |  |
| Jogador 5 | 2-6 | 08:54:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 2-6 | 08:54:25 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 2-6 | 08:54:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | -0.0600 |  |
| Jogador 5 | 2-6 | 08:54:28 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.4000 |  |
| Jogador 5 | 2-7 | 08:54:37 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_Tristana | 0.8000 |  |
| Jogador 5 | 2-7 | 08:54:38 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | 0.2400 |  |
| Jogador 5 | 2-7 | 08:54:38 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | 0.1400 |  |
| Jogador 5 | 2-7 | 08:54:39 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-7 | 08:54:40 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 2-7 | 08:54:40 | MOVE Board -> Board: Tristana (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 2-7 | 08:54:40 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | 0.3000 |  |
| Jogador 5 | 2-7 | 08:54:41 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 2-7 | 08:54:41 | MOVE Board -> Board: Veigar (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-7 | 08:54:42 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-1 | 08:55:00 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | 0.0600 |  |
| Jogador 5 | 3-1 | 08:55:00 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | -0.3000 |  |
| Jogador 5 | 3-1 | 08:55:01 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | 0.1000 |  |
| Jogador 5 | 3-1 | 08:55:01 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | -0.1500 |  |
| Jogador 5 | 3-1 | 08:55:02 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-1 | 08:55:02 | MOVE Board -> Board: Tristana (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | -0.3600 |  |
| Jogador 5 | 3-1 | 08:55:03 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | 0.0700 |  |
| Jogador 5 | 3-1 | 08:55:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | 0.1100 |  |
| Jogador 5 | 3-1 | 08:55:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-2 | 08:55:22 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 3-2 | 08:55:22 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | 0.7900 |  |
| Jogador 5 | 3-2 | 08:55:23 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-2 | 08:55:23 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | 0.2000 |  |
| Jogador 5 | 3-2 | 08:55:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-2 | 08:55:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-2 | 08:55:25 | MOVE Board -> Board: Veigar (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-2 | 08:55:25 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-2 | 08:55:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-3 | 08:55:44 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | -0.2600 |  |
| Jogador 5 | 3-3 | 08:55:45 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | 0.8100 |  |
| Jogador 5 | 3-3 | 08:55:45 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 3-3 | 08:55:46 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | 0.8400 |  |
| Jogador 5 | 3-3 | 08:55:46 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Tristana | -0.0500 |  |
| Jogador 5 | 3-3 | 08:55:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-3 | 08:55:47 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Tristana | -0.1200 |  |
| Jogador 5 | 3-3 | 08:55:48 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-3 | 08:55:48 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 3-4 | 08:56:08 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.7700 |  |
| Jogador 5 | 3-4 | 08:56:08 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 5 | 3-4 | 08:56:09 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 5 | 3-4 | 08:56:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 5 | 3-4 | 08:56:10 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 5 | 3-4 | 08:56:11 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 3-4 | 08:56:11 | MOVE Board -> Board: Tristana (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-4 | 08:56:12 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Enfeitiçador | DA_18_Tristana | 0.0400 |  |
| Jogador 5 | 3-4 | 08:56:12 | MOVE Board -> Board: Veigar (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-5 | 08:56:33 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_18_Rammus | 0.7600 |  |
| Jogador 5 | 3-5 | 08:56:34 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_18_Rammus | 0.5300 |  |
| Jogador 5 | 3-5 | 08:56:34 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Enfeitiçador | DA_18_Rammus | -0.0500 |  |
| Jogador 5 | 3-5 | 08:56:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Enfeitiçador | DA_18_Rammus | -0.0400 |  |
| Jogador 5 | 3-5 | 08:56:35 | MOVE Board -> Board: Tristana (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Enfeitiçador | DA_18_Rammus | -0.3100 |  |
| Jogador 5 | 3-5 | 08:56:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Enfeitiçador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-6 | 08:57:01 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | 0.7300 |  |
| Jogador 5 | 3-6 | 08:57:01 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_18_Rammus | 0.1900 |  |
| Jogador 5 | 3-6 | 08:57:01 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-6 | 08:57:02 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 3-6 | 08:57:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-7 | 08:57:30 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | 0.1800 |  |
| Jogador 5 | 3-7 | 08:57:31 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 3-7 | 08:57:31 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-7 | 08:57:32 | VENDEU: Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Enfeitiçador | DA_18_Rammus | -0.0300 |  |
| Jogador 5 | 3-7 | 08:57:32 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | -0.2300 |  |
| Jogador 5 | 3-7 | 08:57:32 | MOVE Board -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-7 | 08:57:33 | MOVE Board -> Board: Tristana (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 3-7 | 08:57:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-1 | 08:58:03 | VENDEU: Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 5 | 4-1 | 08:58:04 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 5 | 4-1 | 08:58:04 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-1 | 08:58:05 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 5 | 4-1 | 08:58:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 4-1 | 08:58:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 4-1 | 08:58:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-1 | 08:58:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-1 | 08:58:08 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 4-2 | 08:58:37 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 4-2 | 08:58:37 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.5500 |  |
| Jogador 5 | 4-2 | 08:58:38 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 5 | 4-2 | 08:58:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 5 | 4-2 | 08:58:40 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 5 | 4-2 | 08:58:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 4-2 | 08:58:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 4-2 | 08:58:41 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-2 | 08:58:41 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 5 | 4-3 | 08:59:11 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 5 | 4-3 | 08:59:11 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 4-3 | 08:59:12 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-3 | 08:59:12 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-3 | 08:59:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-4 | 08:59:46 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 5 | 4-4 | 08:59:46 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 4-4 | 08:59:47 | MOVE Board -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-4 | 08:59:47 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-4 | 08:59:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-5 | 09:00:25 | VENDEU: Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.1400 |  |
| Jogador 5 | 4-5 | 09:00:26 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.5200 |  |
| Jogador 5 | 4-5 | 09:00:26 | MOVE Board -> Board: Tristana (i:6.0) <-> Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 0 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-5 | 09:00:27 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 4-5 | 09:00:27 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 0 | Enfeitiçador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 4-6 | 09:01:03 | VENDEU: Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-6 | 09:01:03 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.2300 |  |
| Jogador 5 | 4-6 | 09:01:04 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-6 | 09:01:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-6 | 09:01:05 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 4-6 | 09:01:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 5 | 4-7 | 09:01:43 | VENDEU: Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 4-7 | 09:01:43 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.9000 |  |
| Jogador 5 | 4-7 | 09:01:43 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 4-7 | 09:01:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 4-7 | 09:01:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 4-7 | 09:01:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-7 | 09:01:45 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 26 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-1 | 09:02:22 | VENDEU: Tristana (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 41 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 5 | 5-1 | 09:02:22 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Yorick (i:2.0) (tabuleiro slot 6) | ECON | ECON: acumular até o limite de juros de 50 | 41 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 5-1 | 09:02:23 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Yorick (i:2.0) (tabuleiro slot 6) | ECON | ECON: acumular até o limite de juros de 50 | 41 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 5 | 5-1 | 09:02:23 | COMPROU: Teemo (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 5-1 | 09:02:24 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 39 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 5 | 5-1 | 09:02:24 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 35 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 5-1 | 09:02:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-1 | 09:02:25 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 27 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.1000 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-1 | 09:02:25 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 23 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-2 | 09:03:02 | VENDEU: Teemo (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 33 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-2 | 09:03:02 | COMPROU: Zyra (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 29 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-2 | 09:03:03 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Karma (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 29 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 5 | 5-2 | 09:03:03 | VENDEU: Zyra (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 33 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 5 | 5-2 | 09:03:04 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 30 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 5 | 5-2 | 09:03:04 | MOVE Board -> Board: Azuporã (i:8.0) <-> Yorick (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 30 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-2 | 09:03:05 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 26 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.1000 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-2 | 09:03:05 | MOVE Board -> Board: Yorick (i:2.0) <-> Kog'Maw (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 26 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-2 | 09:03:05 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Veigar (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 26 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-3 | 09:03:43 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 5 | 5-3 | 09:03:44 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-3 | 09:03:44 | MOVE Board -> Board: Nidalee (i:8.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 5-3 | 09:03:44 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-4 | 09:04:26 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 5 | 5-4 | 09:04:26 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 5 | 5-4 | 09:04:26 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-4 | 09:04:27 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 5 | 5-4 | 09:04:27 | MOVE Board -> Board: Azuporã (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-4 | 09:04:28 | MOVE Board -> Board: Yorick (i:2.0) <-> Kog'Maw (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 5-4 | 09:04:28 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-4 | 09:04:28 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 33 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-5 | 09:05:10 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 5 | 5-5 | 09:05:10 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 5 | 5-5 | 09:05:11 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-5 | 09:05:11 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-5 | 09:05:11 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-5 | 09:05:12 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Enfeitiçador | DA_KogMaw18_AD | -0.0700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-6 | 09:05:53 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-6 | 09:05:55 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Enfeitiçador | DA_Nidalee18_AP | 0.9500 |  |
| Jogador 5 | 5-6 | 09:05:55 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Enfeitiçador | DA_Nidalee18_AP | -0.0600 |  |
| Jogador 5 | 5-6 | 09:05:56 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Enfeitiçador | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 5 | 5-6 | 09:05:56 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 44 | 4 | Enfeitiçador | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 5 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 40 | 4 | Enfeitiçador | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 5 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 36 | 4 | Enfeitiçador | DA_Nidalee18_AP | -0.0800 |  |
| Jogador 5 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 32 | 4 | Enfeitiçador | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 5 | 5-6 | 09:05:58 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 28 | 4 | Enfeitiçador | DA_Nidalee18_AP | -0.0800 |  |
| Jogador 5 | 5-7 | 09:06:41 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Cassiopeia (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Enfeitiçador | DA_Nidalee18_AP | 0.1400 |  |
| Jogador 5 | 5-7 | 09:06:41 | VENDEU: Nidalee (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 5-7 | 09:06:42 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.9300 |  |
| Jogador 5 | 5-7 | 09:06:42 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 5-7 | 09:06:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.8800 |  |
| Jogador 5 | 5-7 | 09:06:43 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 5-7 | 09:06:43 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 5 | 5-7 | 09:06:44 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 2 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-7 | 09:06:44 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 2 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 6-1 | 09:07:27 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Enfeitiçador | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 5 | 6-1 | 09:07:27 | MOVE Board -> Board: Ashe (i:10.0) <-> Kog'Maw (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 6-1 | 09:07:28 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 6-1 | 09:07:28 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Enfeitiçador | DA_KogMaw18_AD | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 6-2 | 09:08:13 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 6-2 | 09:08:13 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 5 | 6-2 | 09:08:14 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 6-2 | 09:08:14 | COMPROU: Maokai (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 5 | 6-2 | 09:08:14 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 6-2 | 09:08:15 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 6-2 | 09:08:15 | MOVE Board -> Board: Veigar (i:2.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 6-2 | 09:08:16 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 6-3 | 09:09:00 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 5 | 6-3 | 09:09:00 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 5 | 6-3 | 09:09:01 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 5 | 6-3 | 09:09:01 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.4100 |  |
| Jogador 5 | 6-3 | 09:09:01 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 5 | 6-3 | 09:09:02 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 5 | 6-3 | 09:09:02 | MOVE Board -> Board: Azuporã (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 6-3 | 09:09:03 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 6-3 | 09:09:03 | MOVE Board -> Board: Yorick (i:2.0) <-> Ashe (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 6-4 | 09:09:47 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 6-4 | 09:09:48 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Enfeitiçador | DA_KogMaw18_AD | 1.0800 |  |
| Jogador 5 | 6-4 | 09:09:48 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.6600 |  |
| Jogador 5 | 6-4 | 09:09:48 | VENDEU: Cassiopeia (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.3500 |  |
| Jogador 5 | 6-4 | 09:09:49 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Ashe (i:10.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 5 | 6-4 | 09:09:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 5 | 6-4 | 09:09:50 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 5 | 6-4 | 09:09:50 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 5 | 6-4 | 09:09:50 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.6600 |  |
| Jogador 6 | ? | 08:52:18 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | ? | 08:52:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 08:52:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 6 | 1-1 | 08:52:25 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.9900 |  |
| Jogador 6 | 1-1 | 08:52:26 | MOVE Bench -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.1300 |  |
| Jogador 6 | 1-1 | 08:52:28 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0200 |  |
| Jogador 6 | 1-1 | 08:52:28 | MOVE Bench -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.4100 |  |
| Jogador 6 | 1-1 | 08:52:29 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5500 |  |
| Jogador 6 | 1-2 | 08:52:32 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2300 |  |
| Jogador 6 | 1-2 | 08:52:33 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.2200 |  |
| Jogador 6 | 1-2 | 08:52:33 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 6 | 1-2 | 08:52:35 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0300 |  |
| Jogador 6 | 1-2 | 08:52:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0200 |  |
| Jogador 6 | 1-3 | 08:52:41 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 6 | 1-3 | 08:52:42 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2400 |  |
| Jogador 6 | 1-3 | 08:52:43 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-3 | 08:52:43 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1000 |  |
| Jogador 6 | 1-3 | 08:52:44 | MOVE Board -> Board: Cascalho (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 6 | 1-3 | 08:52:44 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 6 | 1-3 | 08:52:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 1-3 | 08:52:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-4 | 08:52:52 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3000 |  |
| Jogador 6 | 1-4 | 08:52:53 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 6 | 1-4 | 08:52:54 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.1400 |  |
| Jogador 6 | 1-4 | 08:52:55 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.0900 |  |
| Jogador 6 | 1-4 | 08:52:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 6 | 1-4 | 08:52:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.9000 |  |
| Jogador 6 | 1-4 | 08:52:57 | MOVE Board -> Board: Cascalho (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0500 |  |
| Jogador 6 | 1-4 | 08:52:58 | MOVE Board -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-1 | 08:53:03 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | 0.2200 |  |
| Jogador 6 | 2-1 | 08:53:04 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Vi18 | -0.0500 |  |
| Jogador 6 | 2-1 | 08:53:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 2-1 | 08:53:06 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 2-1 | 08:53:06 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | -0.0800 |  |
| Jogador 6 | 2-1 | 08:53:07 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | 0.1100 |  |
| Jogador 6 | 2-1 | 08:53:07 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | -0.0700 |  |
| Jogador 6 | 2-1 | 08:53:08 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | -0.1700 |  |
| Jogador 6 | 2-2 | 08:53:15 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Vi18 | 0.2700 |  |
| Jogador 6 | 2-3 | 08:53:29 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_Vi18 | 0.2800 |  |
| Jogador 6 | 2-3 | 08:53:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Vi18 | 0.1800 |  |
| Jogador 6 | 2-3 | 08:53:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Vi18 | -0.1400 |  |
| Jogador 6 | 2-3 | 08:53:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Vi18 | -0.0600 |  |
| Jogador 6 | 2-3 | 08:53:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Vi18 | -0.0600 |  |
| Jogador 6 | 2-3 | 08:53:34 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | -0.0900 |  |
| Jogador 6 | 2-3 | 08:53:34 | MOVE Bench -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | -0.0300 |  |
| Jogador 6 | 2-3 | 08:53:34 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | 0.3900 |  |
| Jogador 6 | 2-4 | 08:53:40 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Yorick | 1.0500 |  |
| Jogador 6 | 2-4 | 08:53:41 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Yorick | -0.8200 |  |
| Jogador 6 | 2-4 | 08:53:41 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Yorick | 0.3300 |  |
| Jogador 6 | 2-4 | 08:53:42 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Yorick | 0.1200 |  |
| Jogador 6 | 2-4 | 08:53:42 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Yorick | 0.0400 |  |
| Jogador 6 | 2-4 | 08:53:42 | MOVE Bench -> Board: Shen (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Yorick | -0.2100 |  |
| Jogador 6 | 2-4 | 08:53:43 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Yorick | 0.0600 |  |
| Jogador 6 | 2-4 | 08:53:44 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Yorick | -0.0500 |  |
| Jogador 6 | 2-4 | 08:53:44 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Vi18 | -0.3800 |  |
| Jogador 6 | 2-4 | 08:53:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Vi18 | -0.0600 |  |
| Jogador 6 | 2-5 | 08:54:00 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_Vi18 | 0.8300 |  |
| Jogador 6 | 2-5 | 08:54:01 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 08:54:02 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 6 | 2-5 | 08:54:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 08:54:03 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 6 | 2-5 | 08:54:04 | MOVE Board -> Board: Sejuani (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-5 | 08:54:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-5 | 08:54:06 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 6 | 2-6 | 08:54:22 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.9000 |  |
| Jogador 6 | 2-6 | 08:54:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.9000 |  |
| Jogador 6 | 2-6 | 08:54:23 | MOVE Board -> Board: Rubrivirim (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 6 | 2-6 | 08:54:24 | MOVE Board -> Board: Sejuani (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 2-6 | 08:54:25 | MOVE Board -> Board: Cascalho (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-6 | 08:54:25 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-6 | 08:54:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-7 | 08:54:37 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 6 | 2-7 | 08:54:38 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 6 | 2-7 | 08:54:38 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 6 | 2-7 | 08:54:39 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 6 | 2-7 | 08:54:40 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-7 | 08:54:40 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-7 | 08:54:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-1 | 08:55:00 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 6 | 3-1 | 08:55:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | 0.7600 |  |
| Jogador 6 | 3-1 | 08:55:01 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.8400 |  |
| Jogador 6 | 3-1 | 08:55:01 | MOVE Bench -> Board: Rakan (i:4.0) <-> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.1000 |  |
| Jogador 6 | 3-1 | 08:55:02 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.1300 |  |
| Jogador 6 | 3-1 | 08:55:02 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | -0.0600 |  |
| Jogador 6 | 3-1 | 08:55:03 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | -0.7600 |  |
| Jogador 6 | 3-1 | 08:55:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 3-1 | 08:55:04 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | -0.3500 |  |
| Jogador 6 | 3-2 | 08:55:22 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Rubrivirim (i:2.0) (tabuleiro slot 22) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Rakan | 0.0800 |  |
| Jogador 6 | 3-2 | 08:55:22 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Rubrivirim (i:2.0) (tabuleiro slot 22) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Rakan | 0.0700 |  |
| Jogador 6 | 3-2 | 08:55:23 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.1800 |  |
| Jogador 6 | 3-2 | 08:55:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 3-2 | 08:55:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 3-2 | 08:55:24 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 6 | 3-2 | 08:55:25 | MOVE Bench -> Board: Grompe (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 6 | 3-2 | 08:55:25 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 6 | 3-2 | 08:55:26 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 3-3 | 08:55:44 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Vi18 | 0.8300 |  |
| Jogador 6 | 3-3 | 08:55:45 | MOVE Board -> Board: Rubrivirim (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-3 | 08:55:45 | MOVE Board -> Board: Sejuani (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-3 | 08:55:46 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-3 | 08:55:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-4 | 08:56:08 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Vi18 | 0.8100 |  |
| Jogador 6 | 3-4 | 08:56:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-4 | 08:56:09 | MOVE Bench -> Board: Vi (i:12.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.1000 |  |
| Jogador 6 | 3-4 | 08:56:09 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | -0.0500 |  |
| Jogador 6 | 3-4 | 08:56:10 | MOVE Board -> Board: Rubrivirim (i:2.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.0200 |  |
| Jogador 6 | 3-4 | 08:56:11 | MOVE Board -> Board: Sejuani (i:4.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-4 | 08:56:11 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-4 | 08:56:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-5 | 08:56:33 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | -0.1500 |  |
| Jogador 6 | 3-5 | 08:56:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-5 | 08:56:34 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-5 | 08:56:35 | MOVE Board -> Board: Vi (i:12.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-5 | 08:56:35 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-5 | 08:56:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-6 | 08:57:01 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Vi18 | 0.1000 |  |
| Jogador 6 | 3-6 | 08:57:01 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Vi18 | 0.3900 |  |
| Jogador 6 | 3-6 | 08:57:01 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Vi18 | -0.1000 |  |
| Jogador 6 | 3-6 | 08:57:02 | MOVE Bench -> Board: Zyra (i:8.0) <-> Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Vi18 | 0.0600 |  |
| Jogador 6 | 3-6 | 08:57:03 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | -0.0300 |  |
| Jogador 6 | 3-6 | 08:57:03 | MOVE Board -> Board: Zyra (i:8.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-6 | 08:57:04 | MOVE Board -> Board: Vi (i:12.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-6 | 08:57:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Vi18 | 0.1100 |  |
| Jogador 6 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Vi18 | 0.1100 |  |
| Jogador 6 | 3-7 | 08:57:31 | VENDEU: Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-7 | 08:57:31 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Zyra (i:8.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Vi18 | 0.0900 |  |
| Jogador 6 | 3-7 | 08:57:32 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Master Yi (i:6.0) (tabuleiro slot 22) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Vi18 | 0.0400 |  |
| Jogador 6 | 3-7 | 08:57:32 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Vi18 | 0.4600 |  |
| Jogador 6 | 3-7 | 08:57:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-7 | 08:57:33 | MOVE Bench -> Board: Rammus (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | 0.0100 |  |
| Jogador 6 | 3-7 | 08:57:34 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | -0.7600 |  |
| Jogador 6 | 4-1 | 08:58:03 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_Vi18 | 0.0900 |  |
| Jogador 6 | 4-1 | 08:58:04 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 6 | 4-1 | 08:58:04 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.5700 |  |
| Jogador 6 | 4-1 | 08:58:05 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.6900 |  |
| Jogador 6 | 4-1 | 08:58:05 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 6 | 4-1 | 08:58:06 | MOVE Board -> Board: Rammus (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-1 | 08:58:06 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-2 | 08:58:37 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 6 | 4-2 | 08:58:37 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-2 | 08:58:38 | MOVE Board -> Board: Sejuani (i:4.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-2 | 08:58:38 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-2 | 08:58:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-3 | 08:59:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 6 | 4-3 | 08:59:11 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-3 | 08:59:12 | VENDEU: Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 6 | 4-3 | 08:59:12 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Shen (i:4.0) (tabuleiro slot 22) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | 4-3 | 08:59:13 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 6 | 4-3 | 08:59:13 | MOVE Bench -> Board: Amumu (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 6 | 4-3 | 08:59:14 | MOVE Board -> Board: Shen (i:4.0) <-> Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-3 | 08:59:14 | MOVE Board -> Board: Zyra (i:8.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-3 | 08:59:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-4 | 08:59:46 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 4-4 | 08:59:46 | MOVE Board -> Board: Vi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-4 | 08:59:47 | COMPROU: Varus (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 4-4 | 08:59:47 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-4 | 08:59:47 | MOVE Board -> Board: Shen (i:4.0) <-> Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-4 | 08:59:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-5 | 09:00:25 | VENDEU: Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 1 | Colosso | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 6 | 4-5 | 09:00:26 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Colosso | DA_KogMaw18_AD | 0.6900 |  |
| Jogador 6 | 4-5 | 09:00:26 | MOVE Board -> Board: Zyra (i:8.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-5 | 09:00:27 | MOVE Board -> Board: Vi (i:12.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-5 | 09:00:27 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 4-6 | 09:01:03 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-6 | 09:01:03 | MOVE Board -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-6 | 09:01:04 | MOVE Board -> Board: Shen (i:4.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-6 | 09:01:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 3 | Colosso | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 6 | 4-7 | 09:01:42 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 3 | Colosso | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 6 | 4-7 | 09:01:43 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 3 | Colosso | DA_Vi18 | -0.3100 |  |
| Jogador 6 | 4-7 | 09:01:43 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 3 | Colosso | DA_Vi18 | 0.6200 |  |
| Jogador 6 | 4-7 | 09:01:43 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 3 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 4-7 | 09:01:44 | MOVE Board -> Board: Zyra (i:8.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 3 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 4-7 | 09:01:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 3 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 6 | 5-1 | 09:02:22 | VENDEU: Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 5-1 | 09:02:22 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Colosso | DA_Vi18 | 0.9500 |  |
| Jogador 6 | 5-1 | 09:02:23 | MOVE Bench -> Board: Grompe (i:4.0) <-> Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Colosso | DA_Vi18 | -0.4000 |  |
| Jogador 6 | 5-1 | 09:02:23 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Colosso | DA_Vi18 | 0.0800 |  |
| Jogador 6 | 5-1 | 09:02:24 | MOVE Bench -> Board: Rakan (i:2.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Colosso | DA_Vi18 | -0.4100 |  |
| Jogador 6 | 5-1 | 09:02:24 | MOVE Bench -> Board: Amumu (i:8.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Colosso | DA_Vi18 | -0.3500 |  |
| Jogador 6 | 5-1 | 09:02:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Colosso | DA_Vi18 | -0.1000 |  |
| Jogador 6 | 5-2 | 09:03:02 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_Fiddlesticks18 | 0.9300 |  |
| Jogador 6 | 5-2 | 09:03:02 | MOVE Bench -> Board: Grompe (i:4.0) <-> Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 6 | 5-2 | 09:03:03 | MOVE Bench -> Board: Amumu (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_Fiddlesticks18 | 0.5800 |  |
| Jogador 6 | 5-2 | 09:03:03 | MOVE Board -> Board: Amumu (i:8.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 5-2 | 09:03:04 | MOVE Board -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 5-2 | 09:03:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 6 | 5-3 | 09:03:43 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Colosso | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 6 | 5-3 | 09:03:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 5-3 | 09:03:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 74 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 5-3 | 09:03:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 5-3 | 09:03:45 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 5-3 | 09:03:45 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 5-3 | 09:03:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 5-3 | 09:03:46 | BUY XP | ECON | ECON: manter reserva de 50 e gastar excedente útil | 58 | 5 | Colosso | DA_Fiddlesticks18 | 0.7300 |  |
| Jogador 6 | 5-3 | 09:03:46 | MOVE Bench -> Board: Zyra (i:8.0) <-> Grompe (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 58 | 5 | Colosso | DA_Fiddlesticks18 | -0.7800 |  |
| Jogador 6 | 5-4 | 09:04:26 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 65 | 5 | Colosso | DA_Fiddlesticks18 | 0.6200 |  |
| Jogador 6 | 5-4 | 09:04:26 | BUY XP | ECON | ECON: manter reserva de 50 e gastar excedente útil | 61 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 5-4 | 09:04:26 | BUY XP | ECON | ECON: manter reserva de 50 e gastar excedente útil | 57 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 5-4 | 09:04:27 | BUY XP | ECON | ECON: manter reserva de 50 e gastar excedente útil | 53 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 5-4 | 09:04:27 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 49 | 5 | Colosso | DA_Fiddlesticks18 | -0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 6 | 5-4 | 09:04:28 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 45 | 5 | Colosso | DA_Fiddlesticks18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 6 | 5-4 | 09:04:28 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 41 | 5 | Colosso | DA_Fiddlesticks18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 6 | 5-4 | 09:04:28 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 37 | 5 | Colosso | DA_Fiddlesticks18 | -0.1100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 6 | 5-4 | 09:04:29 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 33 | 5 | Colosso | DA_Fiddlesticks18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 6 | 5-5 | 09:05:10 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 3 | Colosso | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 6 | 5-5 | 09:05:10 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 33 | 3 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 5-5 | 09:05:11 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 29 | 3 | Colosso | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 6 | 5-5 | 09:05:11 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 25 | 3 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 5-5 | 09:05:11 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 21 | 3 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 5-5 | 09:05:12 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 17 | 3 | Colosso | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 6 | 5-5 | 09:05:12 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 13 | 3 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 5-5 | 09:05:12 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 9 | 3 | Colosso | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 6 | 5-5 | 09:05:13 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 3 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 5-6 | 09:05:53 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 0 | Colosso | DA_Vi18 | -0.1400 |  |
| Jogador 6 | 5-6 | 09:05:55 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 0 | Colosso | DA_Vi18 | 0.7500 |  |
| Jogador 6 | 5-6 | 09:05:55 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 24 | 0 | Colosso | DA_Vi18 | -0.2900 |  |
| Jogador 6 | 5-6 | 09:05:56 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 0 | Colosso | DA_Vi18 | 0.3300 |  |
| Jogador 6 | 5-6 | 09:05:56 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Colosso | DA_Vi18 | -0.0500 |  |
| Jogador 6 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Colosso | DA_Vi18 | 0.0300 |  |
| Jogador 6 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_Vi18 | -0.0500 |  |
| Jogador 6 | 5-6 | 09:05:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_Vi18 | 0.0300 |  |
| Jogador 6 | 5-6 | 09:05:58 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | 0.0300 |  |
| Jogador 6 | 5-7 | 09:06:41 | EQUIP_FROM_INVENTORY: DA_18_EmblemSpellweaver -> Lobo Trevoguari (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_Vi18 | -0.0300 |  |
| Jogador 6 | 5-7 | 09:06:41 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Colosso | DA_Vi18 | 0.0700 |  |
| Jogador 6 | 5-7 | 09:06:42 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_Amumu18 | 0.7500 |  |
| Jogador 6 | 5-7 | 09:06:42 | MOVE Bench -> Board: Rakan (i:2.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_Amumu18 | 0.1000 |  |
| Jogador 6 | 5-7 | 09:06:43 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_Amumu18 | -0.4100 |  |
| Jogador 6 | 5-7 | 09:06:43 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_Amumu18 | 0.2900 |  |
| Jogador 6 | 5-7 | 09:06:43 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_Amumu18 | 0.0600 |  |
| Jogador 6 | 5-7 | 09:06:44 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 6 | 5-7 | 09:06:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_Amumu18 | 0.0700 |  |
| Jogador 6 | 6-1 | 09:07:27 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_Amumu18 | 0.2700 |  |
| Jogador 6 | 6-1 | 09:07:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Amumu18 | 0.2700 |  |
| Jogador 6 | 6-1 | 09:07:28 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Amumu18 | -0.4000 |  |
| Jogador 6 | 6-1 | 09:07:28 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Amumu18 | 0.0600 |  |
| Jogador 6 | 6-1 | 09:07:28 | MOVE Bench -> Board: Rakan (i:2.0) <-> Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Amumu18 | 0.0600 |  |
| Jogador 6 | 6-1 | 09:07:29 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Amumu18 | -0.4100 |  |
| Jogador 6 | 6-1 | 09:07:29 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Amumu18 | 0.0600 |  |
| Jogador 6 | 6-1 | 09:07:29 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Amumu18 | 0.3100 |  |
| Jogador 6 | 6-1 | 09:07:30 | MOVE Board -> Board: Vi (i:6.0) <-> Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 7 | ? | 08:52:18 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 7 | ? | 08:52:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 08:52:24 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 08:52:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 08:52:26 | MOVE Bench -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.6400 |  |
| Jogador 7 | 1-1 | 08:52:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-1 | 08:52:29 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2300 |  |
| Jogador 7 | 1-2 | 08:52:32 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-2 | 08:52:33 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 7 | 1-2 | 08:52:33 | MOVE Bench -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 7 | 1-2 | 08:52:35 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 7 | 1-2 | 08:52:37 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 08:52:41 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 7 | 1-3 | 08:52:42 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-3 | 08:52:43 | MOVE Board -> Board: Akali (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-3 | 08:52:43 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 7 | 1-3 | 08:52:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 08:52:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9700 |  |
| Jogador 7 | 1-4 | 08:52:53 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 7 | 1-4 | 08:52:54 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 7 | 1-4 | 08:52:55 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3100 |  |
| Jogador 7 | 1-4 | 08:52:55 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.5000 |  |
| Jogador 7 | 1-4 | 08:52:56 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-4 | 08:52:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0500 |  |
| Jogador 7 | 1-4 | 08:52:58 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 7 | 2-1 | 08:53:03 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9500 |  |
| Jogador 7 | 2-1 | 08:53:04 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.4200 |  |
| Jogador 7 | 2-1 | 08:53:05 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 2-1 | 08:53:06 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1300 |  |
| Jogador 7 | 2-1 | 08:53:06 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 08:53:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.3500 |  |
| Jogador 7 | 2-1 | 08:53:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-2 | 08:53:15 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.9500 |  |
| Jogador 7 | 2-3 | 08:53:29 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 7 | 2-3 | 08:53:30 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 7 | 2-3 | 08:53:31 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | -0.4400 |  |
| Jogador 7 | 2-3 | 08:53:32 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | -0.0300 |  |
| Jogador 7 | 2-3 | 08:53:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-4 | 08:53:40 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.0700 |  |
| Jogador 7 | 2-4 | 08:53:41 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 7 | 2-4 | 08:53:41 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | -0.4500 |  |
| Jogador 7 | 2-4 | 08:53:42 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 7 | 2-4 | 08:53:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-5 | 08:54:00 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | 0.4700 |  |
| Jogador 7 | 2-5 | 08:54:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.8800 |  |
| Jogador 7 | 2-5 | 08:54:02 | VENDEU: Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.2600 |  |
| Jogador 7 | 2-5 | 08:54:02 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | 0.8700 |  |
| Jogador 7 | 2-5 | 08:54:03 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | 0.0400 |  |
| Jogador 7 | 2-5 | 08:54:04 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 7 | 2-5 | 08:54:04 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | -0.1200 |  |
| Jogador 7 | 2-5 | 08:54:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-6 | 08:54:22 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Devastador | DA_Fiddlesticks18 | -0.3700 |  |
| Jogador 7 | 2-6 | 08:54:23 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | 0.9000 |  |
| Jogador 7 | 2-6 | 08:54:23 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Yorick (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 7 | 2-6 | 08:54:24 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Yorick (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 7 | 2-6 | 08:54:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | -0.2900 |  |
| Jogador 7 | 2-6 | 08:54:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | -0.3800 |  |
| Jogador 7 | 2-6 | 08:54:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-7 | 08:54:37 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Fiddlesticks18 | 0.2000 |  |
| Jogador 7 | 2-7 | 08:54:38 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 7 | 2-7 | 08:54:38 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 7 | 2-7 | 08:54:39 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Fiddlesticks18 | -0.3900 |  |
| Jogador 7 | 2-7 | 08:54:40 | MOVE Bench -> Board: Rakan (i:2.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 7 | 2-7 | 08:54:40 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 7 | 2-7 | 08:54:40 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Fiddlesticks18 | -0.4400 |  |
| Jogador 7 | 2-7 | 08:54:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Fiddlesticks18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-1 | 08:55:00 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 7 | 3-1 | 08:55:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Rakan | 0.8000 |  |
| Jogador 7 | 3-1 | 08:55:01 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Rakan | -0.7100 |  |
| Jogador 7 | 3-1 | 08:55:01 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Rakan | 0.3400 |  |
| Jogador 7 | 3-1 | 08:55:02 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | 0.8100 |  |
| Jogador 7 | 3-1 | 08:55:02 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | 0.0800 |  |
| Jogador 7 | 3-1 | 08:55:03 | MOVE Bench -> Board: Yorick (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | 0.0600 |  |
| Jogador 7 | 3-1 | 08:55:04 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | 0.4900 |  |
| Jogador 7 | 3-1 | 08:55:04 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 7 | 3-2 | 08:55:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Rakan | 0.8300 |  |
| Jogador 7 | 3-2 | 08:55:22 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Colosso | DA_Fiddlesticks18 | -0.3700 |  |
| Jogador 7 | 3-2 | 08:55:23 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Colosso | DA_Fiddlesticks18 | 0.6100 |  |
| Jogador 7 | 3-2 | 08:55:23 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Yorick (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Colosso | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 7 | 3-2 | 08:55:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 3-2 | 08:55:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 7 | 3-2 | 08:55:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Colosso | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 7 | 3-2 | 08:55:25 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Colosso | DA_Fiddlesticks18 | 0.5400 |  |
| Jogador 7 | 3-2 | 08:55:26 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 3 | Colosso | DA_Fiddlesticks18 | 0.2400 |  |
| Jogador 7 | 3-3 | 08:55:44 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_Fiddlesticks18 | -0.2800 |  |
| Jogador 7 | 3-3 | 08:55:45 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_Fiddlesticks18 | 0.7600 |  |
| Jogador 7 | 3-3 | 08:55:45 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 7 | 3-3 | 08:55:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | 0.3200 |  |
| Jogador 7 | 3-3 | 08:55:46 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-3 | 08:55:47 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-3 | 08:55:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-4 | 08:56:08 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 7 | 3-4 | 08:56:08 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_Fiddlesticks18 | 0.2400 |  |
| Jogador 7 | 3-4 | 08:56:09 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-4 | 08:56:09 | MOVE Board -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-4 | 08:56:10 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-4 | 08:56:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_Fiddlesticks18 | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-5 | 08:56:33 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Colosso | DA_Fiddlesticks18 | -0.2700 |  |
| Jogador 7 | 3-5 | 08:56:34 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Colosso | DA_Fiddlesticks18 | 0.7100 |  |
| Jogador 7 | 3-5 | 08:56:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 3-5 | 08:56:35 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-5 | 08:56:35 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-5 | 08:56:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Colosso | DA_Fiddlesticks18 | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-6 | 08:57:01 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-6 | 08:57:01 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Colosso | DA_Fiddlesticks18 | 0.9000 |  |
| Jogador 7 | 3-6 | 08:57:01 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_Fiddlesticks18 | 0.7500 |  |
| Jogador 7 | 3-6 | 08:57:02 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_Fiddlesticks18 | 0.5600 |  |
| Jogador 7 | 3-6 | 08:57:03 | MOVE Board -> Board: Grompe (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-6 | 08:57:03 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 7 | 3-6 | 08:57:04 | MOVE Board -> Board: Hecarim (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 7 | 3-6 | 08:57:04 | MOVE Board -> Board: Grompe (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_Fiddlesticks18 | -0.2200 |  |
| Jogador 7 | 3-6 | 08:57:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_Fiddlesticks18 | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-7 | 08:57:30 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.3600 |  |
| Jogador 7 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.1700 |  |
| Jogador 7 | 3-7 | 08:57:31 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.1700 |  |
| Jogador 7 | 3-7 | 08:57:31 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Colosso | DA_18_Hecarim | -0.3000 |  |
| Jogador 7 | 3-7 | 08:57:32 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Colosso | DA_18_Hecarim | 0.0500 |  |
| Jogador 7 | 3-7 | 08:57:32 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Colosso | DA_18_Hecarim | 0.0300 |  |
| Jogador 7 | 3-7 | 08:57:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Colosso | DA_18_Hecarim | 0.0300 |  |
| Jogador 7 | 3-7 | 08:57:33 | MOVE Board -> Board: Yorick (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Colosso | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 3-7 | 08:57:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Colosso | DA_18_Hecarim | 0.0300 |  |
| Jogador 7 | 4-1 | 08:58:03 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Colosso | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-1 | 08:58:04 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_18_Hecarim | 0.8800 |  |
| Jogador 7 | 4-1 | 08:58:04 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Colosso | DA_18_Hecarim | -0.2600 |  |
| Jogador 7 | 4-1 | 08:58:05 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_18_Hecarim | 0.0500 |  |
| Jogador 7 | 4-1 | 08:58:05 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_18_Hecarim | 0.0300 |  |
| Jogador 7 | 4-1 | 08:58:06 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Colosso | DA_18_Hecarim | 0.3600 |  |
| Jogador 7 | 4-1 | 08:58:06 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Colosso | DA_18_Hecarim | 0.4500 |  |
| Jogador 7 | 4-1 | 08:58:07 | MOVE Board -> Board: Sejuani (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Colosso | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 4-1 | 08:58:08 | MOVE Board -> Board: Grompe (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Colosso | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-2 | 08:58:37 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Colosso | DA_18_Soraka | -0.1600 |  |
| Jogador 7 | 4-2 | 08:58:37 | MOVE Board -> Board: Hecarim (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 7 | 4-2 | 08:58:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 7 | 4-2 | 08:58:38 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Colosso | DA_18_Soraka | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-3 | 08:59:11 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 7 | 4-3 | 08:59:11 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_18_Soraka | 0.3700 |  |
| Jogador 7 | 4-3 | 08:59:12 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 7 | 4-3 | 08:59:12 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Colosso | DA_18_Soraka | 0.1900 |  |
| Jogador 7 | 4-3 | 08:59:13 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-3 | 08:59:13 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-3 | 08:59:14 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-3 | 08:59:14 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 7 | 4-3 | 08:59:15 | MOVE Board -> Board: Grompe (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 7 | 4-4 | 08:59:46 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_18_Soraka | -0.0200 |  |
| Jogador 7 | 4-4 | 08:59:46 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Colosso | DA_18_Soraka | 0.1100 |  |
| Jogador 7 | 4-4 | 08:59:47 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-4 | 08:59:47 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-4 | 08:59:47 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-4 | 08:59:48 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-4 | 08:59:48 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-4 | 08:59:49 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 57 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-4 | 08:59:49 | MOVE Board -> Board: Sejuani (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 5 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 7 | 4-5 | 09:00:25 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_18_Soraka | -0.2700 |  |
| Jogador 7 | 4-5 | 09:00:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 69 | 5 | Colosso | DA_18_Soraka | 0.9300 |  |
| Jogador 7 | 4-5 | 09:00:26 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_18_Soraka | -0.1400 |  |
| Jogador 7 | 4-5 | 09:00:27 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Colosso | DA_18_Soraka | 0.6000 |  |
| Jogador 7 | 4-5 | 09:00:27 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-5 | 09:00:28 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 59 | 5 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-5 | 09:00:28 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 55 | 5 | Colosso | DA_18_Soraka | 0.5500 |  |
| Jogador 7 | 4-5 | 09:00:29 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Colosso | DA_18_Soraka | 0.0400 |  |
| Jogador 7 | 4-5 | 09:00:29 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 47 | 5 | Colosso | DA_18_Soraka | -0.0500 |  |
| Jogador 8 | ? | 08:52:18 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3500 |  |
| Jogador 8 | ? | 08:52:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 08:52:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 08:52:25 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0100 |  |
| Jogador 8 | 1-1 | 08:52:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 08:52:29 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2100 |  |
| Jogador 8 | 1-2 | 08:52:32 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | 1-2 | 08:52:33 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | 1-2 | 08:52:33 | MOVE Bench -> Board: Xayah (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.9200 |  |
| Jogador 8 | 1-2 | 08:52:35 | MOVE Bench -> Board: Leona (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.3500 |  |
| Jogador 8 | 1-2 | 08:52:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 1-3 | 08:52:41 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0300 |  |
| Jogador 8 | 1-3 | 08:52:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.1200 |  |
| Jogador 8 | 1-3 | 08:52:43 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.9200 |  |
| Jogador 8 | 1-3 | 08:52:43 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0400 |  |
| Jogador 8 | 1-3 | 08:52:44 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0200 |  |
| Jogador 8 | 1-3 | 08:52:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 1-4 | 08:52:52 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 1.1000 |  |
| Jogador 8 | 1-4 | 08:52:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.3900 |  |
| Jogador 8 | 1-4 | 08:52:54 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.3000 |  |
| Jogador 8 | 1-4 | 08:52:55 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.3700 |  |
| Jogador 8 | 1-4 | 08:52:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.1900 |  |
| Jogador 8 | 1-4 | 08:52:56 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.1100 |  |
| Jogador 8 | 1-4 | 08:52:57 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0500 |  |
| Jogador 8 | 1-4 | 08:52:58 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.5400 |  |
| Jogador 8 | 2-1 | 08:53:03 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2700 |  |
| Jogador 8 | 2-1 | 08:53:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0400 |  |
| Jogador 8 | 2-1 | 08:53:05 | MOVE Board -> Board: Xayah (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-1 | 08:53:06 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0700 |  |
| Jogador 8 | 2-1 | 08:53:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-2 | 08:53:15 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.9700 |  |
| Jogador 8 | 2-3 | 08:53:29 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Xayah | 0.9800 |  |
| Jogador 8 | 2-3 | 08:53:30 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 8 | 2-3 | 08:53:31 | MOVE Bench -> Board: Veigar (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Xayah | -0.6300 |  |
| Jogador 8 | 2-3 | 08:53:32 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Xayah | 0.4800 |  |
| Jogador 8 | 2-3 | 08:53:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | -0.0400 |  |
| Jogador 8 | 2-3 | 08:53:34 | MOVE Board -> Board: Leona (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | -0.0400 |  |
| Jogador 8 | 2-3 | 08:53:34 | MOVE Board -> Board: Xayah (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 2-3 | 08:53:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-4 | 08:53:40 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Xayah | 0.7900 |  |
| Jogador 8 | 2-4 | 08:53:41 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Xayah | 0.2300 |  |
| Jogador 8 | 2-4 | 08:53:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Xayah | -0.0400 |  |
| Jogador 8 | 2-4 | 08:53:42 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Xayah | 0.0100 |  |
| Jogador 8 | 2-4 | 08:53:42 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Leona | -0.3200 |  |
| Jogador 8 | 2-4 | 08:53:42 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Leona | 0.2900 |  |
| Jogador 8 | 2-4 | 08:53:43 | MOVE Board -> Board: Yorick (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-4 | 08:53:44 | MOVE Board -> Board: Leona (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Leona | 0.2600 |  |
| Jogador 8 | 2-4 | 08:53:44 | MOVE Board -> Board: Xayah (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 2-4 | 08:53:45 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Leona | -0.3400 |  |
| Jogador 8 | 2-5 | 08:54:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Leona | 0.8500 |  |
| Jogador 8 | 2-5 | 08:54:01 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Rammus | -0.2300 |  |
| Jogador 8 | 2-5 | 08:54:02 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Tristana | 0.0500 |  |
| Jogador 8 | 2-5 | 08:54:02 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 2-5 | 08:54:03 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Tristana | 0.1600 |  |
| Jogador 8 | 2-5 | 08:54:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Tristana | -0.0400 |  |
| Jogador 8 | 2-5 | 08:54:04 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 2-5 | 08:54:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | 0.0500 |  |
| Jogador 8 | 2-5 | 08:54:06 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | 0.7000 |  |
| Jogador 8 | 2-6 | 08:54:22 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.9000 |  |
| Jogador 8 | 2-6 | 08:54:23 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.0400 |  |
| Jogador 8 | 2-6 | 08:54:23 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Tristana | -0.2700 |  |
| Jogador 8 | 2-6 | 08:54:24 | MOVE Bench -> Board: Warwick (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Tristana | -0.5800 |  |
| Jogador 8 | 2-6 | 08:54:25 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Tristana | 0.1100 |  |
| Jogador 8 | 2-6 | 08:54:25 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 2-6 | 08:54:26 | MOVE Board -> Board: Warwick (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 2-6 | 08:54:28 | MOVE Board -> Board: Yorick (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 2-7 | 08:54:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Tristana | 0.2100 |  |
| Jogador 8 | 2-7 | 08:54:38 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 2-7 | 08:54:38 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.2200 |  |
| Jogador 8 | 2-7 | 08:54:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 2-7 | 08:54:40 | MOVE Board -> Board: Leona (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.0600 |  |
| Jogador 8 | 2-7 | 08:54:40 | MOVE Board -> Board: Xayah (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | 0.2300 |  |
| Jogador 8 | 2-7 | 08:54:40 | MOVE Board -> Board: Veigar (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.3700 |  |
| Jogador 8 | 2-7 | 08:54:41 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 2-7 | 08:54:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-1 | 08:55:00 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Tristana | 0.0800 |  |
| Jogador 8 | 3-1 | 08:55:00 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Tristana | 0.2700 |  |
| Jogador 8 | 3-1 | 08:55:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Tristana | -0.0900 |  |
| Jogador 8 | 3-1 | 08:55:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-1 | 08:55:02 | MOVE Board -> Board: Warwick (i:4.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-1 | 08:55:02 | MOVE Board -> Board: Warwick (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-1 | 08:55:03 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-2 | 08:55:22 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Tristana | -0.1600 |  |
| Jogador 8 | 3-2 | 08:55:22 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Tristana | 0.7600 |  |
| Jogador 8 | 3-2 | 08:55:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-2 | 08:55:23 | MOVE Board -> Board: Yorick (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-2 | 08:55:24 | MOVE Board -> Board: Leona (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Tristana | 0.3400 |  |
| Jogador 8 | 3-2 | 08:55:24 | MOVE Board -> Board: Veigar (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Tristana | -0.1700 |  |
| Jogador 8 | 3-2 | 08:55:25 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Tristana | -0.0600 |  |
| Jogador 8 | 3-2 | 08:55:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-3 | 08:55:44 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Tristana | -0.2100 |  |
| Jogador 8 | 3-3 | 08:55:45 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Tristana | 0.0900 |  |
| Jogador 8 | 3-3 | 08:55:45 | MOVE Board -> Board: Xayah (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 3-3 | 08:55:46 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Tristana | 0.0900 |  |
| Jogador 8 | 3-3 | 08:55:46 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-3 | 08:55:47 | MOVE Board -> Board: Warwick (i:4.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-3 | 08:55:47 | MOVE Board -> Board: Warwick (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-3 | 08:55:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-4 | 08:56:08 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 3-4 | 08:56:08 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Espinhos Negros | DA_18_Tristana | 0.0500 |  |
| Jogador 8 | 3-4 | 08:56:09 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 3-4 | 08:56:09 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Tristana | 0.0400 |  |
| Jogador 8 | 3-4 | 08:56:10 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 3-4 | 08:56:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-4 | 08:56:11 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-4 | 08:56:12 | MOVE Board -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Tristana | 0.0300 |  |
| Jogador 8 | 3-4 | 08:56:12 | MOVE Board -> Board: Xayah (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Tristana | -0.1500 |  |
| Jogador 8 | 3-5 | 08:56:33 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Espinhos Negros | DA_18_Tristana | 0.2800 |  |
| Jogador 8 | 3-5 | 08:56:34 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-5 | 08:56:34 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Espinhos Negros | DA_18_Tristana | 0.2800 |  |
| Jogador 8 | 3-5 | 08:56:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Espinhos Negros | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 3-5 | 08:56:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | Espinhos Negros | DA_18_Tristana | -0.1100 |  |
| Jogador 8 | 3-5 | 08:56:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Espinhos Negros | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-5 | 08:56:37 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Espinhos Negros | DA_18_Tristana | 0.5800 |  |
| Jogador 8 | 3-5 | 08:56:37 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Espinhos Negros | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 3-5 | 08:56:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 3-6 | 08:57:01 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Tristana | 0.7500 |  |
| Jogador 8 | 3-6 | 08:57:01 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Tristana | -0.2900 |  |
| Jogador 8 | 3-6 | 08:57:01 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.2800 |  |
| Jogador 8 | 3-6 | 08:57:02 | MOVE Board -> Board: Xayah (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.0500 |  |
| Jogador 8 | 3-6 | 08:57:03 | MOVE Board -> Board: Warwick (i:4.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-6 | 08:57:03 | MOVE Board -> Board: Warwick (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-6 | 08:57:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Tristana | 0.2400 |  |
| Jogador 8 | 3-7 | 08:57:30 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Tristana | 0.2300 |  |
| Jogador 8 | 3-7 | 08:57:31 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_18_Tristana | -0.2100 |  |
| Jogador 8 | 3-7 | 08:57:31 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Espinhos Negros | DA_18_Tristana | 0.8100 |  |
| Jogador 8 | 3-7 | 08:57:32 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Espinhos Negros | DA_18_Tristana | -0.1600 |  |
| Jogador 8 | 3-7 | 08:57:32 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_18_Veigar | 0.8400 |  |
| Jogador 8 | 3-7 | 08:57:32 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Warwick (i:4.0) (tabuleiro slot 6) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_18_Veigar | 0.1400 |  |
| Jogador 8 | 3-7 | 08:57:33 | MOVE Bench -> Board: Azir (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_18_Veigar | 0.1500 |  |
| Jogador 8 | 3-7 | 08:57:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Veigar | -0.0200 |  |
| Jogador 8 | 4-1 | 08:58:03 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Espinhos Negros | DA_18_Tristana | -0.2900 |  |
| Jogador 8 | 4-1 | 08:58:04 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Warwick (i:4.0) (tabuleiro slot 6) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Espinhos Negros | DA_18_Tristana | 0.0900 |  |
| Jogador 8 | 4-1 | 08:58:04 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Azir (i:6.0) (tabuleiro slot 22) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Espinhos Negros | DA_18_Tristana | 0.1800 |  |
| Jogador 8 | 4-1 | 08:58:05 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Azir (i:6.0) (tabuleiro slot 22) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Espinhos Negros | DA_18_Tristana | 0.1800 |  |
| Jogador 8 | 4-1 | 08:58:05 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Espinhos Negros | DA_18_Tristana | 0.7600 |  |
| Jogador 8 | 4-1 | 08:58:06 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Espinhos Negros | DA_18_Tristana | 0.1500 |  |
| Jogador 8 | 4-1 | 08:58:06 | MOVE Board -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-1 | 08:58:07 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Espinhos Negros | DA_18_Tristana | -0.2300 |  |
| Jogador 8 | 4-1 | 08:58:08 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 9 | 1 | Espinhos Negros | DA_18_Tristana | -0.1100 |  |
| Jogador 8 | 4-2 | 08:58:37 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Espinhos Negros | DA_18_Tristana | 0.1500 |  |
| Jogador 8 | 4-2 | 08:58:37 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 1 | Espinhos Negros | DA_18_Tristana | -0.0600 |  |
| Jogador 8 | 4-2 | 08:58:38 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 5 | 1 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-2 | 08:58:38 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 1 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-2 | 08:58:40 | MOVE Board -> Board: Warwick (i:4.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 1 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-2 | 08:58:40 | MOVE Board -> Board: Azir (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 1 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 4-2 | 08:58:41 | MOVE Board -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 1 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 4-2 | 08:58:41 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 1 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-3 | 08:59:11 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.7500 |  |
| Jogador 8 | 4-3 | 08:59:11 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Espinhos Negros | DA_18_Sivir | -0.1500 |  |
| Jogador 8 | 4-3 | 08:59:12 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Espinhos Negros | DA_18_Sivir | 0.2800 |  |
| Jogador 8 | 4-3 | 08:59:12 | MOVE Board -> Board: Sivir (i:8.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Espinhos Negros | DA_18_Sivir | 0.0000 |  |
| Jogador 8 | 4-3 | 08:59:13 | MOVE Board -> Board: Warwick (i:4.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Espinhos Negros | DA_18_Sivir | -0.0200 |  |
| Jogador 8 | 4-3 | 08:59:13 | MOVE Board -> Board: Azir (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Espinhos Negros | DA_18_Sivir | -0.0100 |  |
| Jogador 8 | 4-3 | 08:59:14 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Espinhos Negros | DA_18_Sivir | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-4 | 08:59:46 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Espinhos Negros | DA_18_Sivir | 0.0000 |  |
| Jogador 8 | 4-4 | 08:59:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Espinhos Negros | DA_18_Rakan | 0.8400 |  |
| Jogador 8 | 4-4 | 08:59:47 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Espinhos Negros | DA_18_Rakan | 0.4800 |  |
| Jogador 8 | 4-4 | 08:59:47 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Espinhos Negros | DA_18_Rakan | 0.2200 |  |
| Jogador 8 | 4-4 | 08:59:47 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Espinhos Negros | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 4-4 | 08:59:48 | MOVE Board -> Board: Xayah (i:2.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Espinhos Negros | DA_18_Rakan | -0.0200 |  |
| Jogador 8 | 4-4 | 08:59:48 | MOVE Board -> Board: Sivir (i:8.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Espinhos Negros | DA_18_Rakan | -0.0200 |  |
| Jogador 8 | 4-4 | 08:59:49 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Espinhos Negros | DA_18_Rakan | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-5 | 09:00:25 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Espinhos Negros | DA_18_Sivir | -0.3300 |  |
| Jogador 8 | 4-5 | 09:00:26 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Espinhos Negros | DA_18_Sivir | 0.8300 |  |
| Jogador 8 | 4-5 | 09:00:26 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Espinhos Negros | DA_18_Sivir | -0.0200 |  |
| Jogador 8 | 4-5 | 09:00:27 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Espinhos Negros | DA_18_Sivir | 0.0300 |  |
| Jogador 8 | 4-5 | 09:00:27 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Espinhos Negros | DA_18_Sivir | -0.0500 |  |
| Jogador 8 | 4-5 | 09:00:28 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 14 | 1 | Espinhos Negros | DA_18_Sivir | 0.0300 |  |
| Jogador 8 | 4-5 | 09:00:28 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 10 | 1 | Espinhos Negros | DA_18_Sivir | 0.0300 |  |
| Jogador 8 | 4-5 | 09:00:29 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 6 | 1 | Espinhos Negros | DA_18_Sivir | 0.2400 |  |
| Jogador 8 | 4-5 | 09:00:29 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 2 | 1 | Espinhos Negros | DA_18_Sivir | 0.0300 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 28 | 28 | 140 | 28 | 16 | 189 | 16 | 31 |
| Jogador 2 | 30 | 30 | 150 | 30 | 16 | 230 | 7 | 31 |
| Jogador 3 | 28 | 28 | 140 | 28 | 16 | 204 | 18 | 34 |
| Jogador 4 | 37 | 37 | 185 | 37 | 17 | 274 | 28 | 40 |
| Jogador 5 | 37 | 37 | 185 | 37 | 17 | 271 | 16 | 50 |
| Jogador 6 | 34 | 34 | 170 | 34 | 18 | 242 | 14 | 38 |
| Jogador 7 | 24 | 24 | 120 | 24 | 15 | 161 | 12 | 27 |
| Jogador 8 | 24 | 24 | 120 | 24 | 15 | 173 | 13 | 22 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 189 | 189 | 189 | 0 | 177 | 0 | 189 | 189 | 189 | 46/30 |
| Jogador 2 | 230 | 230 | 230 | 0 | 222 | 0 | 230 | 230 | 230 | 65/50 |
| Jogador 3 | 204 | 204 | 204 | 0 | 195 | 0 | 204 | 204 | 204 | 58/43 |
| Jogador 4 | 274 | 274 | 274 | 0 | 261 | 0 | 274 | 274 | 274 | 71/54 |
| Jogador 5 | 271 | 271 | 271 | 0 | 260 | 0 | 271 | 271 | 271 | 75/60 |
| Jogador 6 | 242 | 242 | 242 | 0 | 229 | 0 | 242 | 242 | 242 | 56/41 |
| Jogador 7 | 161 | 161 | 161 | 0 | 153 | 0 | 161 | 161 | 161 | 40/25 |
| Jogador 8 | 173 | 173 | 173 | 0 | 164 | 0 | 173 | 173 | 173 | 47/32 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.2637415826320648 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 9 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 10 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32052889466285706 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3127656579017639 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.2252703607082367 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41529834270477295 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3505658805370331 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.273463636636734 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004667711444199085 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 19 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06544619053602219 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2713334262371063 | 0.0 | 0.0 | +8189d616-2d10-437f-86ce-218e11038acc / -— |
| Jogador 1 | 1-4 | 22 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.038723349571228 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0284360647201538 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00036364729749038815 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014718701131641865 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 27 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 32 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9809544086456299 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 33 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 34 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5444155335426331 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 36 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23630492389202118 | 0.0 | 0.0 | +57652644-f861-47bc-addd-90760a272b22 / -— |
| Jogador 1 | 2-1 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 39 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 41 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30292966961860657 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 42 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1912430375814438 | 0.0 | 0.0 | +4fc25524-9d8f-46f0-a145-ba3de2642229 / -— |
| Jogador 1 | 2-2 | 43 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11892064660787582 | 0.0 | 0.0 | +56a8c7e1-c6a6-47e0-9a00-6416cf6f068f / -— |
| Jogador 1 | 2-2 | 44 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.000850911601446569 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 45 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0598708912730217 | 0.0 | 0.0 | +— / -57652644-f861-47bc-addd-90760a272b22 |
| Jogador 1 | 2-2 | 46 | SELL | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05460000038146973 | 0.0 | 0.0 | +— / -4fc25524-9d8f-46f0-a145-ba3de2642229 |
| Jogador 1 | 2-2 | 47 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 48 | SELL | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10441899299621582 | 0.0 | 0.0 | +— / -cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 2-3 | 50 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34382200241088867 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-4 | 52 | BUY | STABILIZE | 95.0 | 5 | 12 | 1 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7680054306983948 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -— |
| Jogador 1 | 2-4 | 53 | BUY | STABILIZE | 95.0 | 5 | 11 | 1 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22274035215377808 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 54 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 8 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40332719683647156 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 55 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1652096062898636 | 0.0 | 0.0 | +8c5a0cda-86da-4f36-bee3-c2eae934e263 / -— |
| Jogador 1 | 2-4 | 56 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 57 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 58 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 59 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 61 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8676918745040894 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 62 | SELL | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | Defendente/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00431999983265996 | 0.0 | 0.0 | +— / -8c5a0cda-86da-4f36-bee3-c2eae934e263 |
| Jogador 1 | 2-5 | 63 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 10.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03923351317644119 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 1 | 2-5 | 64 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | Defendente/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 65 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 10.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0030882167629897594 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 66 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 10.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5305770635604858 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 67 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 10.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08068020641803741 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 68 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 10.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31238651275634766 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 69 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 10.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5036733150482178 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 70 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 10.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 72 | SELL | STABILIZE | 95.0 | 5 | 8 | 0 | 10.0 | Defendente/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0771893858909607 | 0.0 | 0.0 | +— / -56a8c7e1-c6a6-47e0-9a00-6416cf6f068f |
| Jogador 1 | 2-6 | 73 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 10.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8698399066925049 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 74 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 9 | 0 | 8.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40309447050094604 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 75 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24925634264945984 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 76 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24221791326999664 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 77 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Defendente/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000540256267413497 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 78 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Defendente/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11227526515722275 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 79 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013381599448621273 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 80 | PASS | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 82 | SELL | STABILIZE | 95.0 | 5 | 10 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29115018248558044 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 2-7 | 83 | BUY | STABILIZE | 95.0 | 5 | 13 | 1 | 18.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9429717063903809 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 84 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 12 | 1 | 16.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42472371459007263 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 85 | BUY | STABILIZE | 95.0 | 5 | 12 | 1 | 22.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07376838475465775 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 86 | BUY_XP | STABILIZE | 95.0 | 5 | 10 | 1 | 22.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 87 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 22.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 88 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Defendente/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38937145471572876 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 89 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 2 | 0 | 20.0 | Defendente/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5784426331520081 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 91 | BUY | STABILIZE | 95.0 | 6 | 8 | 0 | 24.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21140806376934052 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 92 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 6 | 0 | 24.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16086164116859436 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 93 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 6 | 0 | 24.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036460548639297485 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 94 | MOVE_BENCH | FAST8 | 95.0 | 6 | 6 | 0 | 26.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21271781623363495 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 95 | PASS | STABILIZE | 95.0 | 6 | 6 | 0 | 24.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 102 | BUY | STABILIZE | 95.0 | 6 | 14 | 1 | 24.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11061423271894455 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 103 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 11 | 1 | 24.0 | Defendente/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3278883099555969 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 104 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 11 | 1 | 24.0 | Defendente/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05150771141052246 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 105 | PASS | FAST8 | 95.0 | 6 | 11 | 1 | 26.0 | Defendente/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 112 | SELL | FAST8 | 95.0 | 6 | 21 | 2 | 26.0 | Defendente/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22276046872138977 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 1 | 3-3 | 113 | EQUIP_FROM_INVENTORY | FAST8 | 95.0 | 6 | 24 | 2 | 26.0 | Defendente/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0661289244890213 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 114 | EQUIP_FROM_INVENTORY | FAST8 | 95.0 | 6 | 24 | 2 | 26.0 | Defendente/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07875145226716995 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 115 | BUY | FAST8 | 95.0 | 6 | 24 | 2 | 26.0 | Defendente/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5801188349723816 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 116 | MOVE_BENCH | FAST8 | 95.0 | 6 | 21 | 2 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9464221000671387 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 117 | BUY_XP | FAST8 | 95.0 | 6 | 21 | 2 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 118 | BUY_XP | FAST8 | 95.0 | 6 | 17 | 1 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 119 | BUY_XP | FAST8 | 95.0 | 6 | 13 | 1 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 120 | BUY_XP | FAST8 | 95.0 | 6 | 9 | 0 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 122 | SELL | FAST8 | 95.0 | 6 | 14 | 1 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011089249514043331 | 0.0 | 0.0 | +— / -8e819ba6-a356-4d9b-a8c9-7493332900fb |
| Jogador 1 | 3-4 | 123 | BUY | FAST8 | 95.0 | 6 | 16 | 1 | 26.0 | Defendente/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06095769628882408 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 124 | BUY_XP | FAST8 | 95.0 | 6 | 14 | 1 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 125 | BUY_XP | FAST8 | 95.0 | 6 | 10 | 1 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 126 | BUY_XP | FAST8 | 95.0 | 6 | 6 | 0 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 127 | MOVE_BENCH | FAST8 | 95.0 | 7 | 2 | 0 | 26.0 | Defendente/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4547438323497772 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 128 | MOVE_BOARD | FAST8 | 95.0 | 7 | 2 | 0 | 30.0 | Defendente/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033786043524742126 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 129 | MOVE_BOARD | FAST8 | 95.0 | 7 | 2 | 0 | 30.0 | Defendente/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03476547449827194 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 130 | MOVE_BOARD | FAST8 | 95.0 | 7 | 2 | 0 | 30.0 | Defendente/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 132 | BUY | FAST8 | 95.0 | 7 | 10 | 1 | 30.0 | Defendente/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6859418153762817 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 133 | BUY_XP | FAST8 | 95.0 | 7 | 8 | 0 | 26.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 134 | BUY_XP | FAST8 | 95.0 | 7 | 4 | 0 | 26.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 135 | MOVE_BENCH | FAST8 | 95.0 | 7 | 0 | 0 | 26.0 | Defendente/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23024789988994598 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 136 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 32.0 | Defendente/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02921849489212036 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 137 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 32.0 | Defendente/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015079354867339134 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 138 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 32.0 | Defendente/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03836371377110481 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 139 | PASS | FAST8 | 95.0 | 7 | 0 | 0 | 32.0 | Defendente/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 142 | BUY | FAST8 | 95.0 | 7 | 9 | 0 | 36.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21599221229553223 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 143 | BUY | FAST8 | 95.0 | 7 | 7 | 0 | 36.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15987342596054077 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 144 | MOVE_BOARD | FAST8 | 95.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_18_Shen | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 145 | MOVE_BOARD | FAST8 | 95.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_18_Shen | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03181485831737518 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 146 | PASS | FAST8 | 95.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_18_Shen | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 152 | SELL | FAST8 | 84.0 | 7 | 8 | 0 | 36.0 | Defendente/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.272132009267807 | 0.0 | 0.0 | +— / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 |
| Jogador 1 | 3-7 | 153 | BUY | FAST8 | 84.0 | 7 | 10 | 1 | 36.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6523072123527527 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 154 | SELL | FAST8 | 84.0 | 7 | 7 | 0 | 36.0 | Defendente/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08040188252925873 | 0.0 | 0.0 | +— / -9fe58106-e0c4-4ecc-b152-13c8c0eb564e |
| Jogador 1 | 3-7 | 155 | BUY | FAST8 | 84.0 | 7 | 10 | 1 | 36.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13395801186561584 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 156 | SELL | FAST8 | 84.0 | 7 | 7 | 0 | 36.0 | Defendente/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09040000289678574 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 3-7 | 157 | BUY | FAST8 | 84.0 | 7 | 10 | 1 | 36.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13615484535694122 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 158 | BUY_XP | FAST8 | 84.0 | 7 | 5 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 159 | MOVE_BOARD | FAST8 | 84.0 | 7 | 1 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.046959683299064636 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 160 | MOVE_BOARD | FAST8 | 84.0 | 7 | 1 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019126372411847115 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 162 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1949012130498886 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 163 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19561122357845306 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 164 | SELL | FAST8 | 84.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06740722805261612 | 0.0 | 0.0 | +— / -4518ad1d-87e7-4110-830a-96183c533201 |
| Jogador 1 | 4-1 | 165 | BUY | FAST8 | 84.0 | 7 | 10 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6231364607810974 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -0c9ac713-08bd-4fa7-a94a-2ab70d7815ff,c30e7bdb-41d6-423c-9d7d-2e146472e724 |
| Jogador 1 | 4-1 | 166 | MOVE_BENCH | FAST8 | 84.0 | 7 | 7 | 0 | 30.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5676336884498596 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 167 | BUY_XP | FAST8 | 84.0 | 7 | 7 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 168 | MOVE_BENCH | FAST8 | 84.0 | 7 | 3 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 169 | MOVE_BENCH | FAST8 | 84.0 | 7 | 3 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1031745970249176 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 170 | MOVE_BENCH | FAST8 | 84.0 | 7 | 3 | 0 | 28.0 | Defendente/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41376715898513794 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 172 | BUY | FAST8 | 71.0 | 7 | 9 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21567568182945251 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 1 | 4-2 | 173 | BUY_XP | FAST8 | 71.0 | 7 | 8 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 174 | BUY_XP | FAST8 | 71.0 | 7 | 4 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 175 | MOVE_BOARD | FAST8 | 71.0 | 7 | 0 | 0 | 32.0 | Defendente/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 176 | MOVE_BOARD | FAST8 | 71.0 | 7 | 0 | 0 | 32.0 | Defendente/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 177 | PASS | FAST8 | 71.0 | 7 | 0 | 0 | 32.0 | Defendente/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 182 | BUY | FAST8 | 58.0 | 7 | 6 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7676438689231873 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 4-3 | 183 | MOVE_BENCH | FAST8 | 58.0 | 7 | 5 | 0 | 30.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08506026118993759 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 184 | MOVE_BENCH | FAST8 | 58.0 | 7 | 5 | 0 | 26.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3897877037525177 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 185 | MOVE_BOARD | FAST8 | 58.0 | 7 | 5 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014822624623775482 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 186 | MOVE_BOARD | FAST8 | 58.0 | 7 | 5 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 187 | PASS | FAST8 | 58.0 | 7 | 5 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 192 | BUY | FAST8 | 46.0 | 7 | 11 | 1 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6539726853370667 | 0.0 | 0.0 | +3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 / -— |
| Jogador 1 | 4-4 | 193 | MOVE_BOARD | FAST8 | 46.0 | 7 | 8 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.174306609958876e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 194 | MOVE_BOARD | FAST8 | 46.0 | 7 | 8 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015592733398079872 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 195 | MOVE_BOARD | FAST8 | 46.0 | 7 | 8 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 196 | PASS | FAST8 | 46.0 | 7 | 8 | 0 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 202 | BUY | FAST8 | 46.0 | 7 | 14 | 1 | 32.0 | Defendente/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2127961665391922 | 0.0 | 0.0 | +5477420d-3b98-4863-b2e7-f414d3fa1f01 / -— |
| Jogador 1 | 4-5 | 203 | BUY_XP | FAST8 | 46.0 | 7 | 11 | 1 | 32.0 | Defendente/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 204 | BUY_XP | FAST8 | 46.0 | 7 | 7 | 0 | 32.0 | Defendente/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 205 | MOVE_BENCH | FAST8 | 46.0 | 7 | 3 | 0 | 32.0 | Defendente/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3797233998775482 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 206 | MOVE_BOARD | FAST8 | 46.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06869202852249146 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 207 | PASS | FAST8 | 46.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 212 | SELL | STABILIZE | 33.0 | 7 | 10 | 1 | 36.0 | Defendente/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1781180202960968 | 0.0 | 0.0 | +— / -844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 1 | 4-6 | 213 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 7 | 18 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.061472851783037186 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 214 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 7 | 18 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07645796984434128 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 215 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 7 | 18 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11322228610515594 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 216 | BUY | STABILIZE | 33.0 | 7 | 18 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7029296159744263 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -— |
| Jogador 1 | 4-6 | 217 | BUY_XP | STABILIZE | 33.0 | 7 | 16 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06923499703407288 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 218 | MOVE_BENCH | STABILIZE | 33.0 | 8 | 12 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5938974618911743 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 219 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 12 | 1 | 38.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01197079662233591 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 220 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 12 | 1 | 38.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 222 | BUY | STABILIZE | 20.0 | 8 | 21 | 2 | 38.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7486355900764465 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -0f5471bd-1451-4979-adc9-aced6bb63610,b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 4-7 | 223 | BUY_XP | STABILIZE | 20.0 | 8 | 19 | 1 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 224 | BUY_XP | STABILIZE | 20.0 | 8 | 15 | 1 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 225 | BUY_XP | STABILIZE | 20.0 | 8 | 11 | 1 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 226 | BUY_XP | STABILIZE | 20.0 | 8 | 7 | 0 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 227 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 3 | 0 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 228 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 3 | 0 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01360772829502821 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 229 | PASS | STABILIZE | 20.0 | 8 | 3 | 0 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 232 | BUY | STABILIZE | 20.0 | 8 | 11 | 1 | 40.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7520732283592224 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -227dbcdb-af5c-4318-94d1-f01a7847d100,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 5-1 | 233 | BUY | STABILIZE | 20.0 | 8 | 8 | 0 | 34.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7138605117797852 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 1 | 5-1 | 234 | CRAFT_AND_EQUIP | STABILIZE | 20.0 | 8 | 5 | 0 | 34.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1447203904390335 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 235 | CRAFT_AND_EQUIP | STABILIZE | 20.0 | 8 | 5 | 0 | 34.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16480271518230438 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 236 | BUY_XP | STABILIZE | 20.0 | 8 | 5 | 0 | 34.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 237 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 1 | 0 | 34.0 | Defendente/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020787750836461782 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 238 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 1 | 0 | 34.0 | Defendente/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 239 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 1 | 0 | 34.0 | Defendente/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 240 | PASS | STABILIZE | 20.0 | 8 | 1 | 0 | 34.0 | Defendente/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 242 | BUY | ALL_IN | 4.0 | 8 | 9 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.823968231678009 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58,c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 5-2 | 243 | BUY | ALL_IN | 4.0 | 8 | 6 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2319367676973343 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -— |
| Jogador 1 | 5-2 | 244 | BUY | ALL_IN | 4.0 | 8 | 2 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012898898683488369 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -— |
| Jogador 1 | 5-2 | 245 | MOVE_BOARD | ALL_IN | 4.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00018735321646090597 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 246 | MOVE_BOARD | ALL_IN | 4.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016254369169473648 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 247 | MOVE_BOARD | ALL_IN | 4.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 248 | PASS | ALL_IN | 4.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 252 | BUY | ALL_IN | 4.0 | 8 | 6 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7962920069694519 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 1 | 5-3 | 253 | MOVE_BOARD | ALL_IN | 4.0 | 8 | 5 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 254 | MOVE_BOARD | ALL_IN | 4.0 | 8 | 5 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013975177891552448 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 255 | PASS | ALL_IN | 4.0 | 8 | 5 | 0 | 46.0 | Defendente/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.22566726803779602 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 9 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 10 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03396162390708923 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1177810430526733 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 0.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, SELL, PASS | True | True | 0.2713311016559601 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 18 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09783928096294403 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31940197944641113 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26135382056236267 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 22 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.41249367594718933 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 23 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.086754322052002 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06976480782032013 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03286576271057129 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38602614402770996 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03503049537539482 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015770578756928444 | 0.0 | 0.0 | +780538e0-4319-45d7-9d96-ace3e3d95c3d / -— |
| Jogador 2 | 1-4 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24481070041656494 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07229120284318924 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 32 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.31559547781944275 | 0.0 | 0.0 | +18082e05-51e8-4142-b541-c3d7d781b878 / -— |
| Jogador 2 | 2-1 | 33 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2694930136203766 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 34 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.27077800035476685 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 35 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21610568463802338 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 36 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1654183715581894 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-1 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40118643641471863 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039426691830158234 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3087616562843323 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 41 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9718188047409058 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 42 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18432709574699402 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -— |
| Jogador 2 | 2-2 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003950363490730524 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 44 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08553752303123474 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31686931848526 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2294555902481079 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 50 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1164923831820488 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-4 | 52 | SELL | STABILIZE | 91.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009759999811649323 | 0.0 | 0.0 | +— / -780538e0-4319-45d7-9d96-ace3e3d95c3d |
| Jogador 2 | 2-4 | 53 | BUY | STABILIZE | 91.0 | 4 | 13 | 1 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9466838240623474 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -0023ba20-d605-41fb-8002-3b6920635c59,7ca9b803-76eb-4283-9648-7f98bfd81149 |
| Jogador 2 | 2-4 | 54 | BUY | STABILIZE | 91.0 | 4 | 12 | 1 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5852516293525696 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 2 | 2-4 | 55 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 11 | 1 | 8.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37614938616752625 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 56 | BUY | STABILIZE | 91.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11193448305130005 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 57 | BUY_XP | STABILIZE | 91.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 58 | BUY_XP | STABILIZE | 91.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 59 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.561423659324646 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 61 | BUY | STABILIZE | 91.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0994071215391159 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 62 | SELL | STABILIZE | 91.0 | 5 | 4 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24034938216209412 | 0.0 | 0.0 | +— / -d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 2-5 | 63 | BUY | STABILIZE | 91.0 | 5 | 7 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08414217084646225 | 0.0 | 0.0 | +be53a299-cc3e-4af3-94f6-343f9de1e0a0 / -— |
| Jogador 2 | 2-5 | 64 | BUY_XP | STABILIZE | 91.0 | 5 | 6 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 65 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 2 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007919380441308022 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 66 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 2 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03975530341267586 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 67 | PASS | STABILIZE | 91.0 | 5 | 2 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 72 | SELL | STABILIZE | 85.0 | 5 | 8 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07583877444267273 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-6 | 73 | BUY | STABILIZE | 85.0 | 5 | 10 | 1 | 12.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7122898101806641 | 0.0 | 0.0 | +032b5960-ec2a-4a26-ad67-862a20f30523 / -— |
| Jogador 2 | 2-6 | 74 | SELL | STABILIZE | 85.0 | 5 | 9 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06629980355501175 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-6 | 75 | BUY | STABILIZE | 85.0 | 5 | 10 | 1 | 12.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04761474207043648 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 76 | BUY_XP | STABILIZE | 85.0 | 5 | 8 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 77 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 78 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 0 | 0 | 12.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41413503885269165 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 79 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008781423792243004 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 80 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0065312194637954235 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 82 | BUY | STABILIZE | 85.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8968361020088196 | 0.0 | 0.0 | +068d0768-4134-4a5f-a132-0642c23d91e1 / -— |
| Jogador 2 | 2-7 | 83 | SELL | STABILIZE | 85.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05157696455717087 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-7 | 84 | BUY | STABILIZE | 85.0 | 6 | 5 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12302586436271667 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 85 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0733591616153717 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 86 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 87 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20037604868412018 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 88 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02509838528931141 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 89 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013252520002424717 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 91 | CRAFT_AND_EQUIP | STABILIZE | 85.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2442774921655655 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 92 | SELL | STABILIZE | 85.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04120239242911339 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 3-1 | 93 | BUY | STABILIZE | 85.0 | 6 | 10 | 1 | 16.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19949108362197876 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 94 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 95 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05265260115265846 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 96 | PASS | STABILIZE | 85.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 102 | SELL | STABILIZE | 85.0 | 6 | 17 | 1 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28225404024124146 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 3-2 | 103 | BUY | STABILIZE | 85.0 | 6 | 18 | 1 | 16.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7988122701644897 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 104 | BUY_XP | STABILIZE | 85.0 | 6 | 17 | 1 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 105 | BUY_XP | STABILIZE | 85.0 | 6 | 13 | 1 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 107 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029722435399889946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 108 | SELL | STABILIZE | 85.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1991766393184662 | 0.0 | 0.0 | +— / -032b5960-ec2a-4a26-ad67-862a20f30523 |
| Jogador 2 | 3-2 | 109 | BUY | STABILIZE | 85.0 | 6 | 10 | 1 | 16.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.140499547123909 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -— |
| Jogador 2 | 3-2 | 110 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 112 | SELL | STABILIZE | 76.0 | 6 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009634207934141159 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-3 | 113 | BUY | STABILIZE | 76.0 | 6 | 15 | 1 | 16.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8352958559989929 | 0.0 | 0.0 | +e08cb89b-8a77-44fe-be4c-46c2b45cbe9b / -068d0768-4134-4a5f-a132-0642c23d91e1,d1840f93-35b0-4e88-b58e-eea7267beedc |
| Jogador 2 | 3-3 | 114 | BUY | STABILIZE | 76.0 | 6 | 13 | 1 | 12.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20782427489757538 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 115 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 10 | 1 | 12.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33563166856765747 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 116 | BUY | STABILIZE | 76.0 | 6 | 10 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022705964744091034 | 0.0 | 0.0 | +c30a99f5-ce2d-4bbf-9aab-93017ad40255 / -— |
| Jogador 2 | 3-3 | 117 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 118 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038652244955301285 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 119 | PASS | STABILIZE | 76.0 | 6 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 122 | SELL | STABILIZE | 76.0 | 6 | 14 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2640128433704376 | 0.0 | 0.0 | +— / -e08cb89b-8a77-44fe-be4c-46c2b45cbe9b |
| Jogador 2 | 3-4 | 123 | BUY | STABILIZE | 76.0 | 6 | 19 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2741737365722656 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 124 | SELL | STABILIZE | 76.0 | 6 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03831459581851959 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 3-4 | 125 | BUY | STABILIZE | 76.0 | 6 | 19 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27417463064193726 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 126 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013878819532692432 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 127 | BUY_XP | STABILIZE | 76.0 | 6 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 128 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 13 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004218944814056158 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 129 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 13 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 130 | PASS | STABILIZE | 76.0 | 6 | 13 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 132 | SELL | STABILIZE | 76.0 | 6 | 19 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041120000183582306 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-5 | 133 | BUY | STABILIZE | 76.0 | 6 | 21 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6310895085334778 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 2 | 3-5 | 134 | SELL | STABILIZE | 76.0 | 6 | 20 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2691799998283386 | 0.0 | 0.0 | +— / -c5a8f36d-74b1-4944-a3db-bfb601a89b59 |
| Jogador 2 | 3-5 | 135 | BUY | STABILIZE | 76.0 | 6 | 21 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06795753538608551 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 136 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 18 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 137 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 18 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28058576583862305 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 138 | PASS | STABILIZE | 76.0 | 6 | 18 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 142 | SELL | STABILIZE | 76.0 | 6 | 26 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003744816640391946 | 0.0 | 0.0 | +— / -cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 2 | 3-6 | 143 | BUY | STABILIZE | 76.0 | 6 | 29 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8529876470565796 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 3-6 | 144 | BUY | STABILIZE | 76.0 | 6 | 28 | 2 | 16.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8015148043632507 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -— |
| Jogador 2 | 3-6 | 145 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 26 | 2 | 16.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42559361457824707 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 146 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 26 | 2 | 20.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32943689823150635 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 147 | BUY | STABILIZE | 76.0 | 6 | 26 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16250543296337128 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 148 | BUY_XP | STABILIZE | 76.0 | 6 | 23 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 149 | BUY_XP | STABILIZE | 76.0 | 6 | 19 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 150 | BUY_XP | STABILIZE | 76.0 | 6 | 15 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 152 | SELL | STABILIZE | 65.0 | 7 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4552749991416931 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 3-7 | 153 | BUY | STABILIZE | 65.0 | 7 | 20 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7361212968826294 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 154 | EQUIP_FROM_INVENTORY | STABILIZE | 65.0 | 7 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09728043526411057 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 155 | SELL | STABILIZE | 65.0 | 7 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07742876559495926 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 3-7 | 156 | BUY | STABILIZE | 65.0 | 7 | 20 | 2 | 18.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.712333619594574 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -— |
| Jogador 2 | 3-7 | 157 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30748337507247925 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 158 | BUY | STABILIZE | 65.0 | 7 | 17 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6607603430747986 | 0.0 | 0.0 | +813260b6-a1b8-4a5c-978e-acd60b6b1082 / -— |
| Jogador 2 | 3-7 | 159 | BUY_XP | STABILIZE | 65.0 | 7 | 16 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 160 | BUY_XP | STABILIZE | 65.0 | 7 | 12 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 162 | CRAFT_AND_EQUIP | STABILIZE | 65.0 | 7 | 13 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11447227746248245 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 163 | CRAFT_AND_EQUIP | STABILIZE | 65.0 | 7 | 13 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07010996341705322 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 164 | SELL | STABILIZE | 65.0 | 7 | 13 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2691799998283386 | 0.0 | 0.0 | +— / -813260b6-a1b8-4a5c-978e-acd60b6b1082 |
| Jogador 2 | 4-1 | 165 | BUY | STABILIZE | 65.0 | 7 | 14 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2760758399963379 | 0.0 | 0.0 | +f00503d7-4e8f-4514-acc1-d3206151acc2 / -— |
| Jogador 2 | 4-1 | 166 | BUY_XP | STABILIZE | 65.0 | 7 | 12 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 167 | BUY_XP | STABILIZE | 65.0 | 7 | 8 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 168 | BUY_XP | STABILIZE | 65.0 | 7 | 4 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 169 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 170 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06014770269393921 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 172 | SELL | STABILIZE | 52.0 | 7 | 6 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1291559934616089 | 0.0 | 0.0 | +— / -18082e05-51e8-4142-b541-c3d7d781b878 |
| Jogador 2 | 4-2 | 173 | BUY | STABILIZE | 52.0 | 7 | 8 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2768949568271637 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 2 | 4-2 | 174 | SELL | STABILIZE | 52.0 | 7 | 7 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1627800017595291 | 0.0 | 0.0 | +— / -c617e958-b482-40ce-ab24-acff4dc48bc0 |
| Jogador 2 | 4-2 | 175 | BUY | STABILIZE | 52.0 | 7 | 8 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.254244863986969 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -— |
| Jogador 2 | 4-2 | 176 | BUY_XP | STABILIZE | 52.0 | 7 | 6 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 177 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026621220633387566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 178 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 179 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 180 | PASS | STABILIZE | 52.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 182 | SELL | STABILIZE | 40.0 | 7 | 8 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04915599897503853 | 0.0 | 0.0 | +— / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-3 | 183 | BUY | STABILIZE | 40.0 | 7 | 10 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06088314577937126 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 2 | 4-3 | 184 | BUY_XP | STABILIZE | 40.0 | 7 | 7 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 185 | MOVE_BOARD | STABILIZE | 40.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01393103040754795 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 186 | MOVE_BOARD | STABILIZE | 40.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37154459953308105 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 187 | MOVE_BOARD | STABILIZE | 40.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014425798319280148 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 188 | PASS | STABILIZE | 40.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 192 | SELL | STABILIZE | 28.0 | 7 | 9 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09471999853849411 | 0.0 | 0.0 | +— / -caf1c554-2223-4090-9f96-b551e5c579ce |
| Jogador 2 | 4-4 | 193 | BUY | STABILIZE | 28.0 | 7 | 12 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10504517704248428 | 0.0 | 0.0 | +e1867f53-f97a-4c7a-bce3-24aa037ce27f / -— |
| Jogador 2 | 4-4 | 194 | BUY_XP | STABILIZE | 28.0 | 7 | 9 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 195 | BUY_XP | STABILIZE | 28.0 | 7 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 196 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00032233039382845163 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 197 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039857469499111176 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 198 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 199 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08620905876159668 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 200 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0799487754702568 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 202 | SELL | STABILIZE | 28.0 | 7 | 7 | 0 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07464039325714111 | 0.0 | 0.0 | +— / -e1867f53-f97a-4c7a-bce3-24aa037ce27f |
| Jogador 2 | 4-5 | 203 | BUY | STABILIZE | 28.0 | 7 | 10 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7539940476417542 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -081b684f-5d42-45c5-9a68-12127e5330a7,74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 2 | 4-5 | 204 | BUY | STABILIZE | 28.0 | 7 | 7 | 0 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7949244379997253 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 2 | 4-5 | 205 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04172440245747566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 206 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03437122702598572 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 207 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 208 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1917034536600113 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 209 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09026406705379486 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 210 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07579173892736435 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 212 | BUY | STABILIZE | 28.0 | 7 | 11 | 1 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7771294116973877 | 0.0 | 0.0 | +a11208a9-96bf-468e-ab92-2ead6308be26 / -— |
| Jogador 2 | 4-6 | 213 | SELL | STABILIZE | 28.0 | 7 | 10 | 1 | 22.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3605000078678131 | 0.0 | 0.0 | +— / -5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 2 | 4-6 | 214 | BUY | STABILIZE | 28.0 | 7 | 18 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879699766635895 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 2 | 4-6 | 215 | SELL | STABILIZE | 28.0 | 7 | 17 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.334766685962677 | 0.0 | 0.0 | +— / -7fb0217d-521c-42b5-995c-81e299b3b934 |
| Jogador 2 | 4-6 | 216 | BUY | STABILIZE | 28.0 | 7 | 18 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2768595218658447 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 2 | 4-6 | 217 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 17 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3446449339389801 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 218 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 17 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01526702381670475 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 219 | PASS | STABILIZE | 28.0 | 7 | 17 | 1 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03348042443394661 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 222 | SELL | STABILIZE | 28.0 | 7 | 25 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1627800017595291 | 0.0 | 0.0 | +— / -42aa4dc8-e388-40dd-a210-4c59e358afcd |
| Jogador 2 | 4-7 | 223 | BUY | STABILIZE | 28.0 | 7 | 26 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6548735499382019 | 0.0 | 0.0 | +d366508d-f33b-485a-8ff3-e5d0a248ae3e / -— |
| Jogador 2 | 4-7 | 224 | SELL | STABILIZE | 28.0 | 7 | 25 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2691799998283386 | 0.0 | 0.0 | +— / -d366508d-f33b-485a-8ff3-e5d0a248ae3e |
| Jogador 2 | 4-7 | 225 | BUY | STABILIZE | 28.0 | 7 | 26 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2934207022190094 | 0.0 | 0.0 | +b9b38183-663e-43a4-9f9d-02f1bd4d2d24 / -— |
| Jogador 2 | 4-7 | 226 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 25 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015031705843284726 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 227 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 25 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19672098755836487 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 228 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 25 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2358425110578537 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 229 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 25 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014869878068566322 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 230 | PASS | STABILIZE | 28.0 | 7 | 25 | 2 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04725397005677223 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 232 | CRAFT_AND_EQUIP | STABILIZE | 28.0 | 8 | 33 | 3 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09278181195259094 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 233 | CRAFT_AND_EQUIP | STABILIZE | 28.0 | 8 | 33 | 3 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13374854624271393 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 234 | SELL | STABILIZE | 28.0 | 8 | 33 | 3 | 22.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.046723201870918274 | 0.0 | 0.0 | +— / -b9b38183-663e-43a4-9f9d-02f1bd4d2d24 |
| Jogador 2 | 5-1 | 235 | BUY | STABILIZE | 28.0 | 8 | 34 | 3 | 22.0 | Espinhos Negros/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08601276576519012 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -— |
| Jogador 2 | 5-1 | 236 | SELL | STABILIZE | 28.0 | 8 | 29 | 2 | 22.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21856191754341125 | 0.0 | 0.0 | +— / -a11208a9-96bf-468e-ab92-2ead6308be26 |
| Jogador 2 | 5-1 | 237 | BUY | STABILIZE | 28.0 | 8 | 30 | 3 | 22.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17229127883911133 | 0.0 | 0.0 | +2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 / -— |
| Jogador 2 | 5-1 | 238 | MOVE_BENCH | STABILIZE | 28.0 | 8 | 28 | 2 | 22.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.557499885559082 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 239 | MOVE_BOARD | STABILIZE | 28.0 | 8 | 28 | 2 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0137204984202981 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 240 | BUY | STABILIZE | 28.0 | 8 | 28 | 2 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13062968850135803 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 2 | 5-2 | 242 | SELL | ALL_IN | 15.0 | 8 | 32 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015999999595806003 | 0.0 | 0.0 | +— / -ee67f5c6-559f-492e-9cc0-6bc19a203d6a |
| Jogador 2 | 5-2 | 243 | BUY | ALL_IN | 15.0 | 8 | 35 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20660138130187988 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -— |
| Jogador 2 | 5-2 | 244 | SELL | ALL_IN | 15.0 | 8 | 31 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013307119719684124 | 0.0 | 0.0 | +— / -0d120db3-34e2-47e3-a57c-0d65dcc56342 |
| Jogador 2 | 5-2 | 245 | BUY | ALL_IN | 15.0 | 8 | 35 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15077653527259827 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 2 | 5-2 | 246 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 31 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1697830855846405 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 247 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 31 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 248 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 31 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030710186809301376 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 249 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 31 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11212075501680374 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 250 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 31 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 252 | SELL | ALL_IN | 15.0 | 8 | 40 | 4 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0036800000816583633 | 0.0 | 0.0 | +— / -c69a2be1-356a-4576-9887-6d1790221a5e |
| Jogador 2 | 5-3 | 253 | BUY | ALL_IN | 15.0 | 8 | 44 | 4 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9586949348449707 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -63304cf5-4aa7-473e-9bfb-ec04cd68ebbd,6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 5-3 | 254 | BUY | ALL_IN | 15.0 | 8 | 42 | 4 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045184176415205 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 2 | 5-3 | 255 | BUY | ALL_IN | 15.0 | 8 | 38 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13064827024936676 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 2 | 5-3 | 256 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 35 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015651781111955643 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 257 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 35 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 258 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 35 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005169999203644693 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 259 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 35 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013981005176901817 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 260 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 35 | 3 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0058635808527469635 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 262 | SELL | ALL_IN | 15.0 | 8 | 45 | 4 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2042311728000641 | 0.0 | 0.0 | +— / -7313188a-ce84-4a52-b2d0-a94b2c420cdb |
| Jogador 2 | 5-4 | 263 | BUY | ALL_IN | 15.0 | 8 | 50 | 5 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9263842105865479 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -584e7960-a541-4d45-8ea1-8a75e288c387,a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 5-4 | 264 | BUY | ALL_IN | 15.0 | 8 | 49 | 4 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4088361859321594 | 0.0 | 0.0 | +499f10b9-47ba-4cab-add1-31b452acae6d / -— |
| Jogador 2 | 5-4 | 265 | BUY | ALL_IN | 15.0 | 8 | 48 | 4 | 28.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2154281735420227 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 2 | 5-4 | 266 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 43 | 4 | 28.0 | Espinhos Negros/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23647063970565796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 267 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 43 | 4 | 28.0 | Espinhos Negros/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22146892547607422 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 268 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 43 | 4 | 28.0 | Espinhos Negros/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018017640337347984 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 269 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 43 | 4 | 28.0 | Espinhos Negros/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07094559818506241 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 270 | PASS | ALL_IN | 15.0 | 8 | 43 | 4 | 28.0 | Espinhos Negros/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15816666185855865 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 272 | SELL | ALL_IN | 15.0 | 8 | 53 | 5 | 28.0 | Espinhos Negros/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2687639892101288 | 0.0 | 0.0 | +— / -908d49c8-626c-44b5-9b03-6a85442f358b |
| Jogador 2 | 5-5 | 273 | BUY | ALL_IN | 15.0 | 8 | 56 | 5 | 28.0 | Espinhos Negros/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6964865326881409 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 2 | 5-5 | 274 | SELL | ALL_IN | 15.0 | 8 | 53 | 5 | 28.0 | Espinhos Negros/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016153112053871155 | 0.0 | 0.0 | +— / -4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 2 | 5-5 | 275 | BUY | ALL_IN | 15.0 | 8 | 57 | 5 | 28.0 | Espinhos Negros/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9690801501274109 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -a267d973-f857-4dda-89e1-209bff42ab6f,b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 2 | 5-5 | 276 | BUY | ALL_IN | 15.0 | 8 | 54 | 5 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02237539552152157 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 2 | 5-5 | 277 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 50 | 5 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 278 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 50 | 5 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055723901838064194 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 279 | PASS | ALL_IN | 15.0 | 8 | 50 | 5 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1966666728258133 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3500058054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 9 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 10 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7215380668640137 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.409182608127594 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.11721326410770416 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001950824080267921 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38700923323631287 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0408989191055298 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179802417755127 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 22 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23208801448345184 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23397980630397797 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1273825615644455 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011461431160569191 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012287451885640621 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 32 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9622392654418945 | 0.0 | 0.0 | +584812e9-d314-4de0-97e2-604c5c69466c / -— |
| Jogador 3 | 2-1 | 33 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2946026027202606 | 0.0 | 0.0 | +4274fbd9-759f-48e5-ae6b-c9e3ffed1bd1 / -— |
| Jogador 3 | 2-1 | 34 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1504356414079666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 35 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1286839246749878 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09713888168334961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 37 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30206525325775146 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007186502916738391 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01100125815719366 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 41 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3431656062602997 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 42 | BUY | STABILIZE | 96.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.212688609957695 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 43 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.656371533870697 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 44 | SELL | STABILIZE | 96.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3428778648376465 | 0.0 | 0.0 | +— / -8a384047-bcc4-4d79-8896-30170e9313cd |
| Jogador 3 | 2-2 | 45 | SELL | STABILIZE | 96.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05251999944448471 | 0.0 | 0.0 | +— / -4274fbd9-759f-48e5-ae6b-c9e3ffed1bd1 |
| Jogador 3 | 2-2 | 46 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 47 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003112484235316515 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 48 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.061402130872011185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 50 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31679773330688477 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-4 | 52 | BUY | STABILIZE | 96.0 | 5 | 12 | 1 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0119227170944214 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -584812e9-d314-4de0-97e2-604c5c69466c,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 2-4 | 53 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 11 | 1 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15112829208374023 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 54 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 11 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09673880785703659 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 55 | BUY | STABILIZE | 96.0 | 5 | 11 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11499127745628357 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 56 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06329010426998138 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 57 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14975963532924652 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 58 | BUY_XP | STABILIZE | 96.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 59 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40106719732284546 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 61 | BUY | STABILIZE | 96.0 | 5 | 10 | 1 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8493598103523254 | 0.0 | 0.0 | +492fa74a-22b8-4f7d-a4f9-346fdcf565be / -— |
| Jogador 3 | 2-5 | 62 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9793956875801086 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 63 | BUY_XP | STABILIZE | 96.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 64 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006873304955661297 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 65 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017126522958278656 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 66 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012935616075992584 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 67 | PASS | STABILIZE | 96.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 72 | BUY | STABILIZE | 96.0 | 5 | 10 | 1 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8677358627319336 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -492fa74a-22b8-4f7d-a4f9-346fdcf565be,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 73 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475068092346191 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 74 | BUY | STABILIZE | 96.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003696596249938011 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 3 | 2-6 | 75 | BUY_XP | STABILIZE | 96.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 76 | BUY | STABILIZE | 96.0 | 5 | 1 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015915047843009233 | 0.0 | 0.0 | +924e5b6b-e429-4c01-9241-bd06cb88464d / -— |
| Jogador 3 | 2-6 | 77 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00022256546071730554 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 78 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18661312758922577 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 79 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1576080024242401 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 80 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 82 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.89736407995224 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 83 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3374349772930145 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 84 | BUY | STABILIZE | 90.0 | 5 | 1 | 0 | 22.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5232951045036316 | 0.0 | 0.0 | +432bc6b0-03a8-42f3-a147-d165f4172a8f / -— |
| Jogador 3 | 2-7 | 85 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.2959035302628763e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 86 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01498415321111679 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 87 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01563272252678871 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 88 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 91 | CRAFT_AND_EQUIP | STABILIZE | 90.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22495634853839874 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 92 | SELL | STABILIZE | 90.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009279999881982803 | 0.0 | 0.0 | +— / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63 |
| Jogador 3 | 3-1 | 93 | EQUIP_FROM_INVENTORY | STABILIZE | 90.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12437887489795685 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 94 | EQUIP_FROM_INVENTORY | STABILIZE | 90.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1362699419260025 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 95 | BUY | STABILIZE | 90.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27841803431510925 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 96 | SELL | STABILIZE | 90.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2661319971084595 | 0.0 | 0.0 | +— / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 |
| Jogador 3 | 3-1 | 97 | BUY | STABILIZE | 90.0 | 6 | 10 | 1 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07743137329816818 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-1 | 98 | BUY_XP | STABILIZE | 90.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 99 | BUY_XP | STABILIZE | 90.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 100 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41301849484443665 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 102 | BUY | STABILIZE | 78.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05460195243358612 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 103 | SELL | STABILIZE | 78.0 | 6 | 3 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37049999833106995 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-2 | 104 | BUY | STABILIZE | 78.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05246580019593239 | 0.0 | 0.0 | +f2020469-2f4e-4b95-96e4-1e7d091f1ab0 / -— |
| Jogador 3 | 3-2 | 105 | BUY_XP | STABILIZE | 78.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 106 | SELL | STABILIZE | 78.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01071999967098236 | 0.0 | 0.0 | +— / -f2020469-2f4e-4b95-96e4-1e7d091f1ab0 |
| Jogador 3 | 3-2 | 107 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07686915993690491 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 108 | BUY | FAST8 | 78.0 | 6 | 2 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1579924374818802 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -— |
| Jogador 3 | 3-2 | 109 | MOVE_BOARD | FAST8 | 78.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 110 | MOVE_BOARD | FAST8 | 78.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01520299818366766 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 112 | SELL | FAST8 | 68.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016735566779971123 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 3 | 3-3 | 113 | BUY | FAST8 | 68.0 | 6 | 9 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13314707577228546 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 114 | BUY_XP | FAST8 | 68.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 115 | SELL | FAST8 | 68.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017920000478625298 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 3-3 | 116 | BUY | FAST8 | 68.0 | 6 | 2 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005451633594930172 | 0.0 | 0.0 | +2b23e695-35cf-41dd-8a1d-b99fca421777 / -— |
| Jogador 3 | 3-3 | 117 | MOVE_BOARD | FAST8 | 68.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0010331054218113422 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 118 | MOVE_BOARD | FAST8 | 68.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015001729130744934 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 119 | MOVE_BOARD | FAST8 | 68.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 120 | PASS | FAST8 | 68.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 122 | SELL | FAST8 | 57.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013120000250637531 | 0.0 | 0.0 | +— / -2b23e695-35cf-41dd-8a1d-b99fca421777 |
| Jogador 3 | 3-4 | 123 | BUY | FAST8 | 57.0 | 6 | 8 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7328414916992188 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 124 | BUY_XP | FAST8 | 57.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 125 | SELL | FAST8 | 57.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005424880655482411 | 0.0 | 0.0 | +— / -2fa86b11-4e28-4652-890e-f00a79068223 |
| Jogador 3 | 3-4 | 126 | BUY | FAST8 | 57.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18106406927108765 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 127 | MOVE_BOARD | FAST8 | 57.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.986677357825101e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 128 | MOVE_BOARD | FAST8 | 57.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 129 | MOVE_BOARD | FAST8 | 57.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 130 | PASS | FAST8 | 57.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 132 | SELL | FAST8 | 57.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.238661527633667 | 0.0 | 0.0 | +— / -924e5b6b-e429-4c01-9241-bd06cb88464d |
| Jogador 3 | 3-5 | 133 | BUY | FAST8 | 57.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7608826160430908 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-5 | 134 | BUY | FAST8 | 57.0 | 6 | 4 | 0 | 28.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18152426183223724 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 135 | SELL | FAST8 | 57.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3121570646762848 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-5 | 136 | BUY | FAST8 | 57.0 | 6 | 9 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07932187616825104 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 137 | BUY_XP | FAST8 | 57.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 138 | MOVE_BOARD | FAST8 | 57.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002600926090963185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 139 | MOVE_BOARD | FAST8 | 57.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05987953394651413 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 140 | PASS | FAST8 | 57.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 142 | BUY | FAST8 | 57.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5098950266838074 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 143 | SELL | FAST8 | 57.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02199999988079071 | 0.0 | 0.0 | +— / -432bc6b0-03a8-42f3-a147-d165f4172a8f |
| Jogador 3 | 3-6 | 144 | BUY | FAST8 | 57.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21513953804969788 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 3 | 3-6 | 145 | BUY_XP | FAST8 | 57.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10029999911785126 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 146 | MOVE_BENCH | FAST8 | 57.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5770779252052307 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 147 | BUY | FAST8 | 57.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0012065427144989371 | 0.0 | 0.0 | +daad4576-7a5d-4154-9b81-963d092a7207 / -— |
| Jogador 3 | 3-6 | 148 | MOVE_BOARD | FAST8 | 57.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019823398906737566 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 149 | MOVE_BOARD | FAST8 | 57.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01624227501451969 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 150 | PASS | FAST8 | 57.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 152 | SELL | FAST8 | 45.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009759999811649323 | 0.0 | 0.0 | +— / -daad4576-7a5d-4154-9b81-963d092a7207 |
| Jogador 3 | 3-7 | 153 | BUY | FAST8 | 45.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21036794781684875 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 154 | SELL | FAST8 | 45.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01360000018030405 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 3 | 3-7 | 155 | BUY | FAST8 | 45.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14480619132518768 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 156 | MOVE_BOARD | FAST8 | 45.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 157 | MOVE_BOARD | FAST8 | 45.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 158 | PASS | FAST8 | 45.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 162 | CRAFT_AND_EQUIP | FAST8 | 45.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11575362831354141 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 163 | CRAFT_AND_EQUIP | FAST8 | 45.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09588617086410522 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 164 | SELL | FAST8 | 45.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05486612394452095 | 0.0 | 0.0 | +— / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9 |
| Jogador 3 | 4-1 | 165 | BUY | FAST8 | 45.0 | 7 | 11 | 1 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6506001353263855 | 0.0 | 0.0 | +15d93457-0760-419e-87db-74223c1cb7f4 / -— |
| Jogador 3 | 4-1 | 166 | BUY_XP | FAST8 | 45.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 167 | BUY_XP | FAST8 | 45.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 168 | MOVE_BOARD | FAST8 | 45.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 169 | MOVE_BOARD | FAST8 | 45.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007308301981538534 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 170 | PASS | FAST8 | 45.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 172 | SELL | FAST8 | 45.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.230068176984787 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 4-2 | 173 | BUY | FAST8 | 45.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027462709695100784 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 3 | 4-2 | 174 | BUY_XP | FAST8 | 45.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 175 | MOVE_BOARD | FAST8 | 45.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017311863601207733 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 176 | MOVE_BOARD | FAST8 | 45.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013140343129634857 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 177 | PASS | FAST8 | 45.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 182 | SELL | FAST8 | 45.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08832000195980072 | 0.0 | 0.0 | +— / -0534477f-2ff8-47a7-b71b-1a1d5430589e |
| Jogador 3 | 4-3 | 183 | BUY | FAST8 | 45.0 | 7 | 12 | 1 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06639368832111359 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 3 | 4-3 | 184 | BUY_XP | FAST8 | 45.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 185 | BUY_XP | FAST8 | 45.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 186 | MOVE_BOARD | FAST8 | 45.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012172937858849764 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 187 | MOVE_BOARD | FAST8 | 45.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 188 | PASS | FAST8 | 45.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 192 | SELL | STABILIZE | 34.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013417650014162064 | 0.0 | 0.0 | +— / -235510e3-df54-4de9-9bcf-bff6d47e364a |
| Jogador 3 | 4-4 | 193 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25136125087738037 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -— |
| Jogador 3 | 4-4 | 194 | BUY_XP | STABILIZE | 34.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 195 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 196 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 197 | PASS | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 202 | SELL | STABILIZE | 34.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06518569588661194 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 3 | 4-5 | 203 | BUY | STABILIZE | 34.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7535115480422974 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -15d93457-0760-419e-87db-74223c1cb7f4,bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-5 | 204 | BUY | STABILIZE | 34.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2512929141521454 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -— |
| Jogador 3 | 4-5 | 205 | BUY | STABILIZE | 34.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1726803183555603 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 3 | 4-5 | 206 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02921343222260475 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 207 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014953307807445526 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 208 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000575222074986 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 209 | PASS | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 212 | SELL | STABILIZE | 34.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.218634694814682 | 0.0 | 0.0 | +— / -3a1de7b3-af72-4024-8105-588fa4ec946b |
| Jogador 3 | 4-6 | 213 | BUY | STABILIZE | 34.0 | 7 | 16 | 1 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2873879671096802 | 0.0 | 0.0 | +738fea60-6b44-40f1-9936-43accf852bd7 / -— |
| Jogador 3 | 4-6 | 214 | SELL | STABILIZE | 34.0 | 7 | 15 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006694305338896811 | 0.0 | 0.0 | +— / -5f9e16e2-0766-403f-a85a-f6a735c04261 |
| Jogador 3 | 4-6 | 215 | BUY | STABILIZE | 34.0 | 7 | 17 | 1 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24655748903751373 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -— |
| Jogador 3 | 4-6 | 216 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 14 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.474083319408237e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 217 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 14 | 1 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 218 | PASS | STABILIZE | 34.0 | 7 | 14 | 1 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 222 | SELL | STABILIZE | 22.0 | 7 | 20 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02525317668914795 | 0.0 | 0.0 | +— / -a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 3 | 4-7 | 223 | BUY | STABILIZE | 22.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.297573983669281 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -— |
| Jogador 3 | 4-7 | 224 | SELL | STABILIZE | 22.0 | 7 | 20 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23871195316314697 | 0.0 | 0.0 | +— / -cba152f4-af54-4d82-a35d-67aa165174be |
| Jogador 3 | 4-7 | 225 | BUY | STABILIZE | 22.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17148858308792114 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 3 | 4-7 | 226 | SELL | STABILIZE | 22.0 | 7 | 21 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013154776534065604 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 3 | 4-7 | 227 | BUY | STABILIZE | 22.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10906817018985748 | 0.0 | 0.0 | +5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 / -— |
| Jogador 3 | 4-7 | 228 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 19 | 1 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 229 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 19 | 1 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 230 | PASS | STABILIZE | 22.0 | 7 | 19 | 1 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04012380912899971 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 232 | CRAFT_AND_EQUIP | STABILIZE | 22.0 | 7 | 25 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14289534091949463 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 233 | CRAFT_AND_EQUIP | STABILIZE | 22.0 | 7 | 25 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10911522060632706 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 234 | SELL | STABILIZE | 22.0 | 7 | 25 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008320000022649765 | 0.0 | 0.0 | +— / -5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 |
| Jogador 3 | 5-1 | 235 | BUY | STABILIZE | 22.0 | 7 | 29 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17804524302482605 | 0.0 | 0.0 | +a64cf09b-42bf-494e-9603-d387b6740200 / -— |
| Jogador 3 | 5-1 | 236 | SELL | STABILIZE | 22.0 | 7 | 27 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00024303812824655324 | 0.0 | 0.0 | +— / -a64cf09b-42bf-494e-9603-d387b6740200 |
| Jogador 3 | 5-1 | 237 | BUY | STABILIZE | 22.0 | 7 | 29 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.049992647022008896 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 3 | 5-1 | 238 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 28 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.3870395554913557e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 239 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 28 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015026901848614216 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 240 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 28 | 2 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014983288943767548 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 242 | SELL | STABILIZE | 22.0 | 7 | 36 | 3 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013120000250637531 | 0.0 | 0.0 | +— / -91966802-adc2-46d2-9e7e-194283bca85c |
| Jogador 3 | 5-2 | 243 | BUY | STABILIZE | 22.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8657649755477905 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 3 | 5-2 | 244 | SELL | STABILIZE | 22.0 | 7 | 36 | 3 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04457089304924011 | 0.0 | 0.0 | +— / -6eecc806-dcf8-47df-bc1d-bc5bc5f07099 |
| Jogador 3 | 5-2 | 245 | BUY | STABILIZE | 22.0 | 7 | 39 | 3 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11718221008777618 | 0.0 | 0.0 | +678a6f43-ca48-46c9-8c5b-6790493f4841 / -— |
| Jogador 3 | 5-2 | 246 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.3887631073193916e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 247 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015002050437033176 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 248 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 249 | PASS | STABILIZE | 22.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08526571094989777 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 252 | SELL | ALL_IN | 7.0 | 7 | 45 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007858012802898884 | 0.0 | 0.0 | +— / -678a6f43-ca48-46c9-8c5b-6790493f4841 |
| Jogador 3 | 5-3 | 253 | BUY | ALL_IN | 7.0 | 7 | 47 | 4 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8552052974700928 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -— |
| Jogador 3 | 5-3 | 254 | SELL | ALL_IN | 7.0 | 7 | 45 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2559891641139984 | 0.0 | 0.0 | +— / -1489b596-9339-407a-b49f-d01ecfdd6f78 |
| Jogador 3 | 5-3 | 255 | BUY | ALL_IN | 7.0 | 7 | 46 | 4 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32665520906448364 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 3 | 5-3 | 256 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 43 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.350238744635135e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 257 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 43 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499997265636921 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 258 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 43 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000177547335625 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 259 | PASS | ALL_IN | 7.0 | 7 | 43 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17381110787391663 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3500058054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 9 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 10 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7106347680091858 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42640984058380127 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.040587835013866425 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40096789598464966 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1557593047618866 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059818435460329056 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0033620113972574472 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013552410528063774 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 22 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128636360168457 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3008732199668884 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9755599498748779 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0010096327168866992 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 32 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9810962080955505 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 33 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19102546572685242 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 34 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13936883211135864 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 35 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5145199298858643 | 0.0 | 0.0 | +838eb81f-88a4-41a2-b2e5-7d6784d86773 / -— |
| Jogador 4 | 2-1 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.483184814453125 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 37 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19199572503566742 | 0.0 | 0.0 | +b166276e-305e-4945-8398-7c8b4b86ca9e / -— |
| Jogador 4 | 2-1 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7496787309646606 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 42 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05074823647737503 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 43 | SELL | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009440000168979168 | 0.0 | 0.0 | +— / -b166276e-305e-4945-8398-7c8b4b86ca9e |
| Jogador 4 | 2-2 | 44 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11855386197566986 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 45 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Krug18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011837850324809551 | 0.0 | 0.0 | +— / -e989a0cc-848a-4c45-b153-315877aee8f7 |
| Jogador 4 | 2-2 | 46 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0003655832551885396 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 50 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9491148591041565 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793,eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 52 | BUY | STABILIZE | 100.0 | 5 | 13 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048976924270391464 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5327237248420715 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 54 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24609076976776123 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 55 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8069702386856079 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-4 | 56 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08465605229139328 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05006884038448334 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015081020072102547 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015026106499135494 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 61 | SELL | STABILIZE | 100.0 | 5 | 13 | 1 | 14.0 | —/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23596400022506714 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-5 | 62 | BUY | STABILIZE | 100.0 | 5 | 16 | 1 | 14.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8216132521629333 | 0.0 | 0.0 | +3825a7ba-319f-48f8-ad2d-8c24eabbc1cc / -— |
| Jogador 4 | 2-5 | 63 | SELL | STABILIZE | 100.0 | 5 | 13 | 1 | 14.0 | Colosso/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2461400032043457 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-5 | 64 | BUY | STABILIZE | 100.0 | 5 | 14 | 1 | 14.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9466398358345032 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 65 | BUY | STABILIZE | 100.0 | 5 | 13 | 1 | 14.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3220364451408386 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 66 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038337983191013336 | 0.0 | 0.0 | +a72d427f-f2f7-46dd-97bf-d28999772db0 / -— |
| Jogador 4 | 2-5 | 67 | BUY_XP | STABILIZE | 100.0 | 5 | 9 | 0 | 14.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 68 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005852746777236462 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 70 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009367742575705051 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 72 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2057529091835022 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-6 | 73 | BUY | STABILIZE | 100.0 | 5 | 11 | 1 | 14.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9041892886161804 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 74 | SELL | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | Colosso/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02199999988079071 | 0.0 | 0.0 | +— / -838eb81f-88a4-41a2-b2e5-7d6784d86773 |
| Jogador 4 | 2-6 | 75 | BUY | STABILIZE | 100.0 | 5 | 11 | 1 | 14.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07340697199106216 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 76 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27812135219573975 | 0.0 | 0.0 | +— / -8a006243-4508-4a6c-97ae-a0ce807cee54 |
| Jogador 4 | 2-6 | 77 | BUY_XP | STABILIZE | 100.0 | 5 | 9 | 0 | 14.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 78 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13652674853801727 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 79 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Aphelios | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005231653340160847 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 80 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Aphelios | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014951765537261963 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 82 | SELL | STABILIZE | 93.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04831999912858009 | 0.0 | 0.0 | +— / -f71a7192-663d-46a0-93ef-b900c59c3bde |
| Jogador 4 | 2-7 | 83 | BUY | STABILIZE | 93.0 | 5 | 10 | 1 | 14.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8699724674224854 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -814d07bd-0296-44af-9626-26a8a224d86f,9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-7 | 84 | BUY | STABILIZE | 93.0 | 5 | 9 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8694776296615601 | 0.0 | 0.0 | +3d4fca52-8f58-4464-8cec-752fa99dbb3c / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-7 | 85 | BUY | STABILIZE | 93.0 | 5 | 8 | 0 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12758783996105194 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -— |
| Jogador 4 | 2-7 | 86 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 7 | 0 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1755344420671463 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 87 | BUY | STABILIZE | 93.0 | 5 | 7 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08298156410455704 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 88 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 4 | 0 | 12.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6996042132377625 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 89 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 4 | 0 | 16.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5526755452156067 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 91 | CRAFT_AND_EQUIP | STABILIZE | 93.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23514491319656372 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 92 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0881875604391098 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 93 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 9 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4696565568447113 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 94 | BUY | FAST8 | 93.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010862134397029877 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 95 | BUY | FAST8 | 93.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012866659089922905 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 96 | MOVE_BOARD | FAST8 | 93.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015939527656883001 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 97 | MOVE_BOARD | FAST8 | 93.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014290152117609978 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 98 | PASS | FAST8 | 93.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 102 | SELL | FAST8 | 93.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1652120053768158 | 0.0 | 0.0 | +— / -3d4fca52-8f58-4464-8cec-752fa99dbb3c |
| Jogador 4 | 3-2 | 103 | BUY | FAST8 | 93.0 | 6 | 14 | 1 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7679757475852966 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 104 | BUY | STABILIZE | 93.0 | 6 | 13 | 1 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28799504041671753 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 105 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 12 | 1 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7721575498580933 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 106 | MOVE_BENCH | FAST8 | 93.0 | 6 | 12 | 1 | 26.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1701848804950714 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 107 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 12 | 1 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002654604148119688 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 108 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 12 | 1 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8008933067321777 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 109 | PASS | FAST8 | 93.0 | 6 | 12 | 1 | 26.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 112 | BUY | FAST8 | 82.0 | 6 | 18 | 1 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7335878610610962 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 113 | BUY_XP | FAST8 | 82.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 114 | BUY_XP | FAST8 | 82.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 115 | BUY_XP | FAST8 | 82.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 116 | BUY_XP | FAST8 | 82.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 117 | MOVE_BOARD | FAST8 | 82.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032343607395887375 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 118 | MOVE_BOARD | FAST8 | 82.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11456101387739182 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 119 | MOVE_BOARD | FAST8 | 82.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08198538422584534 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 120 | PASS | FAST8 | 82.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 122 | SELL | FAST8 | 73.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2881186604499817 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 3-4 | 123 | BUY | FAST8 | 73.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.6516715884208679 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 124 | EQUIP_FROM_INVENTORY | FAST8 | 73.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0908835157752037 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 125 | EQUIP_FROM_INVENTORY | FAST8 | 73.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1381242275238037 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 126 | EQUIP_FROM_INVENTORY | FAST8 | 73.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12764011323451996 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 127 | SELL | FAST8 | 73.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2624461054801941 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 3-4 | 128 | BUY | FAST8 | 73.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6863888502120972 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -764470bb-9820-4e49-98f9-5a5f0ce5ca8f,ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 3-4 | 129 | MOVE_BENCH | FAST8 | 73.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08695398271083832 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 130 | MOVE_BENCH | FAST8 | 73.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3106057047843933 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 132 | BUY | FAST8 | 73.0 | 6 | 15 | 1 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6571490168571472 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 133 | MOVE_BENCH | FAST8 | 73.0 | 6 | 13 | 1 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7336617708206177 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 134 | MOVE_BENCH | FAST8 | 73.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0726490244269371 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 135 | BUY | FAST8 | 73.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14550137519836426 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 136 | MOVE_BENCH | FAST8 | 73.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7440159320831299 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 137 | MOVE_BENCH | FAST8 | 73.0 | 6 | 11 | 1 | 28.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3084304928779602 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 138 | PASS | FAST8 | 73.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 142 | MOVE_BENCH | FAST8 | 63.0 | 6 | 18 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.814163863658905 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 143 | MOVE_BENCH | FAST8 | 63.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15804040431976318 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 144 | MOVE_BENCH | FAST8 | 63.0 | 6 | 18 | 1 | 28.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09988460689783096 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 145 | MOVE_BENCH | FAST8 | 63.0 | 6 | 18 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8279592394828796 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 146 | PASS | FAST8 | 63.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 152 | SELL | FAST8 | 53.0 | 6 | 25 | 2 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30848047137260437 | 0.0 | 0.0 | +— / -d754fcfc-6d22-4bc0-8643-8f4bef9afda5 |
| Jogador 4 | 3-7 | 153 | BUY | FAST8 | 53.0 | 6 | 28 | 2 | 26.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7786370515823364 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-7 | 154 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 25 | 2 | 20.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1161767840385437 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 155 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 25 | 2 | 22.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5024871826171875 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 156 | BUY | FAST8 | 53.0 | 6 | 25 | 2 | 28.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2234591692686081 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -— |
| Jogador 4 | 3-7 | 157 | BUY_XP | FAST8 | 53.0 | 6 | 23 | 2 | 28.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 158 | BUY_XP | FAST8 | 53.0 | 6 | 19 | 1 | 28.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10570000112056732 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 159 | MOVE_BENCH | FAST8 | 53.0 | 7 | 15 | 1 | 28.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7874122262001038 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 160 | MOVE_BOARD | FAST8 | 53.0 | 7 | 15 | 1 | 34.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 162 | BUY | FAST8 | 53.0 | 7 | 22 | 2 | 34.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6756886839866638 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 4 | 4-1 | 163 | CRAFT_AND_EQUIP | FAST8 | 53.0 | 7 | 19 | 1 | 34.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22924651205539703 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 164 | CRAFT_AND_EQUIP | FAST8 | 53.0 | 7 | 19 | 1 | 34.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.196312814950943 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 165 | MOVE_BOARD | FAST8 | 53.0 | 7 | 19 | 1 | 34.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013569860719144344 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 166 | MOVE_BOARD | FAST8 | 53.0 | 7 | 19 | 1 | 34.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002875273348763585 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 167 | PASS | FAST8 | 53.0 | 7 | 19 | 1 | 34.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10785714536905289 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 172 | BUY | FAST8 | 53.0 | 7 | 27 | 2 | 34.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7795911431312561 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -8052731e-e34c-4de7-84b1-2b986cfeddaa,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 4-2 | 173 | MOVE_BENCH | FAST8 | 53.0 | 7 | 25 | 2 | 30.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5578544735908508 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 174 | MOVE_BOARD | FAST8 | 53.0 | 7 | 25 | 2 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01428554393351078 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 175 | MOVE_BOARD | FAST8 | 53.0 | 7 | 25 | 2 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015350385569036007 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 176 | PASS | FAST8 | 53.0 | 7 | 25 | 2 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11214285343885422 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 182 | BUY | FAST8 | 41.0 | 7 | 32 | 3 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6893558502197266 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-3 | 183 | BUY | FAST8 | 41.0 | 7 | 29 | 2 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23216243088245392 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 4 | 4-3 | 184 | MOVE_BOARD | FAST8 | 41.0 | 7 | 27 | 2 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00023010732547845691 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 185 | BUY_XP | FAST8 | 41.0 | 7 | 27 | 2 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 186 | BUY_XP | FAST8 | 41.0 | 7 | 23 | 2 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07395999878644943 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 187 | BUY_XP | FAST8 | 41.0 | 7 | 19 | 1 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 188 | MOVE_BOARD | FAST8 | 41.0 | 7 | 15 | 1 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005685765063390136 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 189 | BUY_XP | FAST8 | 41.0 | 7 | 15 | 1 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 190 | MOVE_BOARD | FAST8 | 41.0 | 7 | 11 | 1 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.360196776862722e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 192 | SELL | FAST8 | 41.0 | 7 | 18 | 1 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24491482973098755 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 4-4 | 193 | BUY | FAST8 | 41.0 | 7 | 26 | 2 | 38.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.752828061580658 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 4 | 4-4 | 194 | MOVE_BOARD | FAST8 | 41.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059628166258335114 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 195 | MOVE_BOARD | FAST8 | 41.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04461394622921944 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 196 | BUY_XP | FAST8 | 41.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 197 | BUY_XP | FAST8 | 41.0 | 7 | 20 | 2 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07395999878644943 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 198 | MOVE_BOARD | FAST8 | 41.0 | 7 | 16 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001340053859166801 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 199 | BUY_XP | FAST8 | 41.0 | 7 | 16 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 200 | MOVE_BOARD | FAST8 | 41.0 | 7 | 12 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013540750369429588 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 202 | SELL | FAST8 | 41.0 | 7 | 18 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018999576568603516 | 0.0 | 0.0 | +— / -59f588eb-e3f3-4907-ab23-af073a26bd6a |
| Jogador 4 | 4-5 | 203 | BUY | FAST8 | 41.0 | 7 | 20 | 2 | 38.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01874954253435135 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 4 | 4-5 | 204 | BUY_XP | FAST8 | 41.0 | 7 | 16 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 205 | BUY_XP | FAST8 | 41.0 | 7 | 12 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 206 | BUY_XP | FAST8 | 41.0 | 7 | 8 | 0 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 207 | MOVE_BOARD | FAST8 | 41.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.915594331578177e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 208 | MOVE_BOARD | FAST8 | 41.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015002451837062836 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 209 | PASS | FAST8 | 41.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 212 | SELL | STABILIZE | 29.0 | 7 | 9 | 0 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06815999746322632 | 0.0 | 0.0 | +— / -c49cf468-6fa4-4d94-bc3a-9dc8f7111626 |
| Jogador 4 | 4-6 | 213 | BUY | STABILIZE | 29.0 | 7 | 13 | 1 | 38.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28416067361831665 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -— |
| Jogador 4 | 4-6 | 214 | SELL | STABILIZE | 29.0 | 7 | 11 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06452082842588425 | 0.0 | 0.0 | +— / -4a885bc0-41b4-43f1-94d3-8e755a10645c |
| Jogador 4 | 4-6 | 215 | BUY | STABILIZE | 29.0 | 7 | 13 | 1 | 38.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2164733111858368 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -— |
| Jogador 4 | 4-6 | 216 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 10 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.664710559154628e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 217 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 10 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015017213299870491 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 218 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 10 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01502432581037283 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 219 | PASS | STABILIZE | 29.0 | 7 | 10 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 222 | SELL | STABILIZE | 29.0 | 7 | 17 | 1 | 38.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06639999896287918 | 0.0 | 0.0 | +— / -772bccc4-15f4-4de2-95f8-82d0ed9a72d2 |
| Jogador 4 | 4-7 | 223 | BUY | STABILIZE | 29.0 | 7 | 20 | 2 | 38.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.783932089805603 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -42733dbd-0bc3-461b-95ab-76daf5ad6296,a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 4-7 | 224 | BUY | STABILIZE | 29.0 | 7 | 17 | 1 | 32.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28719526529312134 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 4 | 4-7 | 225 | MOVE_BENCH | STABILIZE | 29.0 | 7 | 16 | 1 | 32.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5670577883720398 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 226 | BUY | STABILIZE | 29.0 | 7 | 16 | 1 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.275261789560318 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 4 | 4-7 | 227 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0054552615620195866 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 228 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03631764277815819 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 229 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002701713237911463 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 230 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011530437506735325 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 232 | CRAFT_AND_EQUIP | STABILIZE | 29.0 | 8 | 19 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15038816630840302 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 233 | CRAFT_AND_EQUIP | STABILIZE | 29.0 | 8 | 19 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08783780038356781 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 234 | SELL | STABILIZE | 29.0 | 8 | 19 | 1 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19956399500370026 | 0.0 | 0.0 | +— / -6722b147-c2a7-4fd0-a943-5036adb3e3a1 |
| Jogador 4 | 5-1 | 235 | BUY | STABILIZE | 29.0 | 8 | 27 | 2 | 36.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8789567351341248 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -60138930-82d5-4f1c-a5fe-a22ea4b70d36,b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 5-1 | 236 | EQUIP_FROM_INVENTORY | STABILIZE | 29.0 | 8 | 24 | 2 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0920119360089302 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 237 | EQUIP_FROM_INVENTORY | STABILIZE | 29.0 | 8 | 24 | 2 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13742400705814362 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 238 | BUY | STABILIZE | 29.0 | 8 | 24 | 2 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.301940381526947 | 0.0 | 0.0 | +0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c / -— |
| Jogador 4 | 5-1 | 239 | BUY_XP | STABILIZE | 29.0 | 8 | 21 | 2 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 240 | BUY_XP | STABILIZE | 29.0 | 8 | 17 | 1 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 242 | BUY | STABILIZE | 29.0 | 8 | 21 | 2 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15504570305347443 | 0.0 | 0.0 | +8d75ef64-e2c3-47b6-a336-c9e5867158e5 / -— |
| Jogador 4 | 5-2 | 243 | MOVE_BENCH | STABILIZE | 29.0 | 8 | 17 | 1 | 36.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5088773965835571 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 244 | BUY | STABILIZE | 29.0 | 8 | 17 | 1 | 42.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1857842057943344 | 0.0 | 0.0 | +6594349f-ecaa-4212-b063-815acae6d0bb / -— |
| Jogador 4 | 5-2 | 245 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 13 | 1 | 42.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 246 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 13 | 1 | 42.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 247 | PASS | STABILIZE | 29.0 | 8 | 13 | 1 | 42.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 252 | SELL | STABILIZE | 29.0 | 8 | 21 | 2 | 42.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34428730607032776 | 0.0 | 0.0 | +— / -02e125a0-3563-47ec-a82a-cba5178731dd |
| Jogador 4 | 5-3 | 253 | BUY | STABILIZE | 29.0 | 8 | 29 | 2 | 42.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06514774262905121 | 0.0 | 0.0 | +d22aa2b7-7c7c-4d47-89be-0f1b8755971c / -— |
| Jogador 4 | 5-3 | 254 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 28 | 2 | 42.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004338648577686399 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 255 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 28 | 2 | 42.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014981765300035477 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 256 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 28 | 2 | 42.0 | Colosso/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015452099964022636 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 257 | PASS | STABILIZE | 29.0 | 8 | 28 | 2 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05648761987686157 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 262 | SELL | STABILIZE | 29.0 | 8 | 37 | 3 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005232116207480431 | 0.0 | 0.0 | +— / -a72d427f-f2f7-46dd-97bf-d28999772db0 |
| Jogador 4 | 5-4 | 263 | BUY | STABILIZE | 29.0 | 8 | 38 | 3 | 42.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2264101207256317 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -— |
| Jogador 4 | 5-4 | 264 | SELL | STABILIZE | 29.0 | 8 | 35 | 3 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005919999908655882 | 0.0 | 0.0 | +— / -d22aa2b7-7c7c-4d47-89be-0f1b8755971c |
| Jogador 4 | 5-4 | 265 | BUY | STABILIZE | 29.0 | 8 | 36 | 3 | 42.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07467702031135559 | 0.0 | 0.0 | +438ec27b-d901-437b-82b5-64e6d46fccb1 / -— |
| Jogador 4 | 5-4 | 266 | BUY_XP | STABILIZE | 29.0 | 8 | 33 | 3 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 267 | BUY_XP | STABILIZE | 29.0 | 8 | 29 | 2 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 268 | BUY_XP | STABILIZE | 29.0 | 8 | 25 | 2 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 269 | BUY_XP | STABILIZE | 29.0 | 8 | 21 | 2 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 270 | BUY_XP | STABILIZE | 29.0 | 8 | 17 | 1 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 272 | SELL | STABILIZE | 29.0 | 8 | 20 | 2 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00044472108129411936 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 4 | 5-5 | 273 | BUY | STABILIZE | 29.0 | 8 | 21 | 2 | 42.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12849077582359314 | 0.0 | 0.0 | +3329c812-11fa-4335-a982-f03e6ab28ee0 / -— |
| Jogador 4 | 5-5 | 274 | SELL | STABILIZE | 29.0 | 8 | 17 | 1 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0568314865231514 | 0.0 | 0.0 | +— / -d8392323-28e4-4e98-a466-5958bf400729 |
| Jogador 4 | 5-5 | 275 | BUY | STABILIZE | 29.0 | 8 | 20 | 2 | 42.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7263466715812683 | 0.0 | 0.0 | +d9097eba-c1b2-4df8-9e5d-a9134dbfe52f / -— |
| Jogador 4 | 5-5 | 276 | MOVE_BENCH | STABILIZE | 29.0 | 8 | 16 | 1 | 42.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009749856777489185 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 277 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 16 | 1 | 48.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 278 | PASS | STABILIZE | 29.0 | 8 | 16 | 1 | 48.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034543491899967194 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 282 | SELL | STABILIZE | 29.0 | 8 | 25 | 2 | 48.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0503748320043087 | 0.0 | 0.0 | +— / -57f213f7-34b1-4a4a-8047-afa5e404e5c4 |
| Jogador 4 | 5-6 | 283 | BUY | STABILIZE | 29.0 | 8 | 26 | 2 | 48.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8377942442893982 | 0.0 | 0.0 | +edd2748e-d629-4a8a-8174-4c1ef3f5f852 / -— |
| Jogador 4 | 5-6 | 284 | SELL | STABILIZE | 29.0 | 8 | 23 | 2 | 48.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12554800510406494 | 0.0 | 0.0 | +— / -438ec27b-d901-437b-82b5-64e6d46fccb1 |
| Jogador 4 | 5-6 | 285 | BUY | STABILIZE | 29.0 | 8 | 26 | 2 | 48.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8752802610397339 | 0.0 | 0.0 | +95a2e19e-619f-4497-ba52-e9bbf06b364f / -3825a7ba-319f-48f8-ad2d-8c24eabbc1cc,4e00fb2f-75c1-4580-bd09-cb73c31af01f |
| Jogador 4 | 5-6 | 286 | MOVE_BENCH | STABILIZE | 29.0 | 8 | 23 | 2 | 42.0 | Florescer/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5976377725601196 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 287 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 23 | 2 | 48.0 | Florescer/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015067793428897858 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 288 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 23 | 2 | 48.0 | Florescer/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01489179115742445 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 289 | PASS | STABILIZE | 29.0 | 8 | 23 | 2 | 48.0 | Florescer/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1353442370891571 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 292 | BUY | STABILIZE | 29.0 | 8 | 34 | 3 | 48.0 | Florescer/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8503196239471436 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -— |
| Jogador 4 | 5-7 | 293 | BUY | STABILIZE | 29.0 | 8 | 30 | 3 | 48.0 | Florescer/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7632126212120056 | 0.0 | 0.0 | +9c07608c-00e1-40f1-9671-6d8bc584a6c9 / -— |
| Jogador 4 | 5-7 | 294 | BUY_XP | STABILIZE | 29.0 | 8 | 26 | 2 | 48.0 | Florescer/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 295 | BUY_XP | STABILIZE | 29.0 | 8 | 22 | 2 | 48.0 | Florescer/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 296 | BUY_XP | STABILIZE | 29.0 | 8 | 18 | 1 | 48.0 | Florescer/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 297 | BUY_XP | STABILIZE | 29.0 | 8 | 14 | 1 | 48.0 | Florescer/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 298 | BUY_XP | STABILIZE | 29.0 | 8 | 10 | 1 | 48.0 | Florescer/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 299 | BUY_XP | STABILIZE | 29.0 | 8 | 6 | 0 | 48.0 | Florescer/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 300 | MOVE_BOARD | STABILIZE | 29.0 | 8 | 2 | 0 | 48.0 | Florescer/DA_Krug18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0434069000184536 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 302 | EQUIP_FROM_INVENTORY | STABILIZE | 29.0 | 8 | 10 | 1 | 48.0 | Florescer/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14050978422164917 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 303 | SELL | STABILIZE | 29.0 | 8 | 10 | 1 | 48.0 | Florescer/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2790652811527252 | 0.0 | 0.0 | +— / -95a2e19e-619f-4497-ba52-e9bbf06b364f |
| Jogador 4 | 6-1 | 304 | BUY | STABILIZE | 29.0 | 8 | 18 | 1 | 48.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8305146098136902 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -6594349f-ecaa-4212-b063-815acae6d0bb,9c07608c-00e1-40f1-9671-6d8bc584a6c9 |
| Jogador 4 | 6-1 | 305 | BUY | STABILIZE | 29.0 | 8 | 14 | 1 | 48.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1843397319316864 | 0.0 | 0.0 | +3eccad10-cc50-4695-852e-0809356dd33b / -— |
| Jogador 4 | 6-1 | 306 | BUY_XP | STABILIZE | 29.0 | 8 | 13 | 1 | 48.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5806871652603149 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 307 | BUY_XP | STABILIZE | 29.0 | 9 | 9 | 0 | 48.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 308 | BUY_XP | STABILIZE | 29.0 | 9 | 5 | 0 | 48.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 309 | MOVE_BENCH | STABILIZE | 29.0 | 9 | 1 | 0 | 48.0 | Florescer/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42485272884368896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 310 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 1 | 0 | 50.0 | Florescer/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11963996291160583 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 312 | BUY | STABILIZE | 29.0 | 9 | 9 | 0 | 50.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.283348023891449 | 0.0 | 0.0 | +d58ebcea-d18b-42f8-a6ca-984d15656662 / -— |
| Jogador 4 | 6-2 | 313 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 6 | 0 | 50.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09733777493238449 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 314 | BUY | STABILIZE | 29.0 | 9 | 6 | 0 | 50.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17958150804042816 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 4 | 6-2 | 315 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 1 | 0 | 50.0 | Florescer/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 316 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 1 | 0 | 50.0 | Florescer/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 317 | PASS | STABILIZE | 29.0 | 9 | 1 | 0 | 50.0 | Florescer/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 322 | SELL | STABILIZE | 29.0 | 9 | 10 | 1 | 50.0 | Florescer/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22353902459144592 | 0.0 | 0.0 | +— / -b250e22d-7193-4ea5-879d-5c7b41145719 |
| Jogador 4 | 6-3 | 323 | BUY | STABILIZE | 29.0 | 9 | 21 | 2 | 50.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13068722188472748 | 0.0 | 0.0 | +194da7dc-39b4-40e3-869d-326ace65137b / -— |
| Jogador 4 | 6-3 | 324 | SELL | STABILIZE | 29.0 | 9 | 19 | 1 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05716106295585632 | 0.0 | 0.0 | +— / -194da7dc-39b4-40e3-869d-326ace65137b |
| Jogador 4 | 6-3 | 325 | BUY | STABILIZE | 29.0 | 9 | 21 | 2 | 50.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13071101903915405 | 0.0 | 0.0 | +1ad1f705-7e6b-4c1f-811c-2863dbf2db9e / -— |
| Jogador 4 | 6-3 | 326 | BUY_XP | STABILIZE | 29.0 | 9 | 19 | 1 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 327 | BUY_XP | STABILIZE | 29.0 | 9 | 15 | 1 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 328 | BUY_XP | STABILIZE | 29.0 | 9 | 11 | 1 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 329 | BUY_XP | STABILIZE | 29.0 | 9 | 7 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 330 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 3 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016457654535770416 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 332 | BUY_XP | STABILIZE | 29.0 | 9 | 12 | 1 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 333 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 8 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000611285213381052 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 334 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 8 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999914914369583 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 335 | BUY_XP | STABILIZE | 29.0 | 9 | 8 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 336 | BUY_XP | STABILIZE | 29.0 | 9 | 4 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 337 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 0 | 0 | 50.0 | Florescer/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.189751112131489e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 338 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 0 | 0 | 50.0 | Florescer/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500018686056137 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 339 | PASS | STABILIZE | 29.0 | 9 | 0 | 0 | 50.0 | Florescer/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 342 | SELL | STABILIZE | 29.0 | 9 | 8 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057153861969709396 | 0.0 | 0.0 | +— / -1ad1f705-7e6b-4c1f-811c-2863dbf2db9e |
| Jogador 4 | 6-5 | 343 | BUY | STABILIZE | 29.0 | 9 | 10 | 1 | 50.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1985919028520584 | 0.0 | 0.0 | +5098782d-1ec1-4a5b-a435-f3c84ab1be0d / -— |
| Jogador 4 | 6-5 | 344 | SELL | STABILIZE | 29.0 | 9 | 6 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09824000298976898 | 0.0 | 0.0 | +— / -7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 |
| Jogador 4 | 6-5 | 345 | BUY | STABILIZE | 29.0 | 9 | 11 | 1 | 50.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.182831808924675 | 0.0 | 0.0 | +78adfe0a-b6d8-4cc4-a482-26451f95e788 / -— |
| Jogador 4 | 6-5 | 346 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 8 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.845441357152595e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 347 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 8 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 348 | MOVE_BOARD | STABILIZE | 29.0 | 9 | 8 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 349 | PASS | STABILIZE | 29.0 | 9 | 8 | 0 | 50.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3222387135028839 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 9 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10612095892429352 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 10 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6402381062507629 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41820284724235535 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.2695513963699341 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42235812544822693 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2650448977947235 | 0.0 | 0.0 | +3002832d-1e66-428b-a25e-007c716764a3 / -— |
| Jogador 5 | 1-3 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05846039578318596 | 0.0 | 0.0 | +9c93476e-a7be-457d-8543-8802507a8d3f / -— |
| Jogador 5 | 1-3 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3193610906600952 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30265548825263977 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0035226289182901382 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 22 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3338584899902344 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3080614507198334 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007323022000491619 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19058199226856232 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15546055138111115 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00985430832952261 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 32 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9622774720191956 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 33 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21232406795024872 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 34 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18147805333137512 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4180606007575989 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 36 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2005729079246521 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 37 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041830770671367645 | 0.0 | 0.0 | +— / -9c93476e-a7be-457d-8543-8802507a8d3f |
| Jogador 5 | 2-1 | 38 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06628739088773727 | 0.0 | 0.0 | +— / -3002832d-1e66-428b-a25e-007c716764a3 |
| Jogador 5 | 2-1 | 39 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18498533964157104 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-2 | 41 | BUY | STABILIZE | 96.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0311145782470703 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 42 | BUY | STABILIZE | 96.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32410913705825806 | 0.0 | 0.0 | +0debca82-3a2a-44ba-af48-83211d5e5243 / -— |
| Jogador 5 | 2-2 | 43 | BUY_XP | STABILIZE | 96.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 44 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33767586946487427 | 0.0 | 0.0 | +— / -eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-2 | 45 | BUY | STABILIZE | 96.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09116382896900177 | 0.0 | 0.0 | +96f1450d-00f3-4aa2-a7fb-05db55904eb1 / -— |
| Jogador 5 | 2-2 | 46 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.1526371710933745e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 47 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025131700560450554 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 48 | PASS | STABILIZE | 96.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 50 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0478142499923706 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-4 | 52 | BUY | STABILIZE | 91.0 | 5 | 11 | 1 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24679310619831085 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 53 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5252889394760132 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 54 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6122501492500305 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 55 | BUY | STABILIZE | 91.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2920839786529541 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 56 | BUY | STABILIZE | 91.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17242304980754852 | 0.0 | 0.0 | +32b7b452-7702-43a3-b3c4-8eda786225b9 / -— |
| Jogador 5 | 2-4 | 57 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02372053638100624 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 58 | BUY_XP | STABILIZE | 91.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 59 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08486001938581467 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 61 | BUY | STABILIZE | 91.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2761622965335846 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 62 | BUY | STABILIZE | 91.0 | 5 | 3 | 0 | 18.0 | Espinhos Negros/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29496893286705017 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 5 | 2-5 | 63 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 2 | 0 | 18.0 | Espinhos Negros/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029493888840079308 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 64 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 2 | 0 | 18.0 | Espinhos Negros/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012395799160003662 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 65 | SELL | STABILIZE | 91.0 | 5 | 2 | 0 | 18.0 | Espinhos Negros/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.316942423582077 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-5 | 66 | BUY_XP | STABILIZE | 91.0 | 5 | 5 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 67 | BUY | STABILIZE | 91.0 | 5 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1200113296508789 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 68 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 0 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 69 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 0 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018638858571648598 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 70 | PASS | STABILIZE | 91.0 | 5 | 0 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 72 | BUY | STABILIZE | 91.0 | 5 | 6 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6891586780548096 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 5 | 2-6 | 73 | BUY | STABILIZE | 91.0 | 5 | 5 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14959940314292908 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 74 | SELL | STABILIZE | 91.0 | 5 | 4 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008320000022649765 | 0.0 | 0.0 | +— / -32b7b452-7702-43a3-b3c4-8eda786225b9 |
| Jogador 5 | 2-6 | 75 | BUY | STABILIZE | 91.0 | 5 | 5 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.054468050599098206 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 76 | SELL | STABILIZE | 91.0 | 5 | 3 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00020899185619782656 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 77 | BUY | STABILIZE | 91.0 | 5 | 5 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22741806507110596 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 78 | BUY_XP | STABILIZE | 91.0 | 5 | 4 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 79 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 0 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003370677586644888 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 80 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 0 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36062633991241455 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 82 | SELL | STABILIZE | 91.0 | 5 | 7 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015519999898970127 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 2-7 | 83 | BUY | STABILIZE | 91.0 | 5 | 8 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8452611565589905 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 84 | SELL | STABILIZE | 91.0 | 5 | 7 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -de78e1b7-ed58-42dd-8374-76b578543e94 |
| Jogador 5 | 2-7 | 85 | BUY | STABILIZE | 91.0 | 5 | 8 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.68904048204422 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 86 | BUY_XP | STABILIZE | 91.0 | 5 | 7 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 87 | SELL | STABILIZE | 91.0 | 6 | 3 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007003643084317446 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-7 | 88 | BUY_XP | STABILIZE | 91.0 | 6 | 4 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 89 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 0 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40038299560546875 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 91 | BUY | STABILIZE | 91.0 | 6 | 6 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8039467930793762 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 92 | BUY | STABILIZE | 91.0 | 6 | 3 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.23641043901443481 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 93 | CRAFT_AND_EQUIP | STABILIZE | 91.0 | 6 | 1 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13903380930423737 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 94 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 1 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 95 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 1 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009801722131669521 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 96 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 1 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02110769972205162 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 97 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 1 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.297992080450058 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 98 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 1 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0070305392146110535 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 99 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 1 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 100 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 1 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 102 | SELL | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06449787318706512 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-2 | 103 | BUY | STABILIZE | 91.0 | 6 | 10 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.297750324010849 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 104 | SELL | STABILIZE | 91.0 | 6 | 7 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09663999825716019 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-2 | 105 | BUY | STABILIZE | 91.0 | 6 | 10 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1506444364786148 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002783566014841199 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 107 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3628711700439453 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 108 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07165811955928802 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 109 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10953289270401001 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 110 | BUY_XP | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 112 | SELL | STABILIZE | 91.0 | 6 | 11 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01056000031530857 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 3-3 | 113 | BUY | STABILIZE | 91.0 | 6 | 13 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7902068495750427 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 114 | SELL | STABILIZE | 91.0 | 6 | 10 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0024834726937115192 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 3-3 | 115 | BUY | STABILIZE | 91.0 | 6 | 12 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19990815222263336 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 116 | BUY_XP | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 117 | BUY_XP | STABILIZE | 91.0 | 6 | 4 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 118 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 0 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 119 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 0 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 120 | PASS | STABILIZE | 91.0 | 6 | 0 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 122 | SELL | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.258892297744751 | 0.0 | 0.0 | +— / -96f1450d-00f3-4aa2-a7fb-05db55904eb1 |
| Jogador 5 | 3-4 | 123 | BUY | STABILIZE | 91.0 | 6 | 9 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8065943121910095 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 124 | SELL | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01239034067839384 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 5 | 3-4 | 125 | BUY | STABILIZE | 91.0 | 6 | 9 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.83743816614151 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -2e4ab22c-62d7-425c-9528-2e1315655c24,6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 3-4 | 126 | BUY | STABILIZE | 91.0 | 6 | 8 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05372786521911621 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 127 | BUY_XP | STABILIZE | 91.0 | 6 | 6 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 128 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 2 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11816881597042084 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 129 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 2 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2798096239566803 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 130 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 2 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048447780311107635 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 132 | BUY | STABILIZE | 91.0 | 6 | 9 | 0 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7747209072113037 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 133 | SELL | STABILIZE | 91.0 | 6 | 6 | 0 | 24.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2938520014286041 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-5 | 134 | BUY | STABILIZE | 91.0 | 6 | 9 | 0 | 24.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7257041335105896 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -02c39b42-90d5-4e01-9380-460b6c1cb993,21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 3-5 | 135 | BUY_XP | STABILIZE | 91.0 | 6 | 8 | 0 | 22.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 136 | MOVE_BENCH | STABILIZE | 91.0 | 7 | 4 | 0 | 22.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10479714721441269 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 137 | BUY_XP | FAST8 | 91.0 | 7 | 4 | 0 | 28.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 138 | MOVE_BOARD | FAST8 | 91.0 | 7 | 0 | 0 | 28.0 | Enfeitiçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0016469021793454885 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 139 | MOVE_BOARD | FAST8 | 91.0 | 7 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036735761910676956 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 140 | MOVE_BOARD | FAST8 | 91.0 | 7 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 142 | BUY | FAST8 | 82.0 | 7 | 5 | 0 | 28.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7579349279403687 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -486e92ad-4dcf-4c0e-a470-e0b87777d380,a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 3-6 | 143 | MOVE_BENCH | FAST8 | 82.0 | 7 | 2 | 0 | 28.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5252510905265808 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 144 | BUY | FAST8 | 82.0 | 7 | 2 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05271376669406891 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 145 | MOVE_BOARD | FAST8 | 82.0 | 7 | 1 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03983283042907715 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 146 | MOVE_BOARD | FAST8 | 82.0 | 7 | 1 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3072626292705536 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 147 | PASS | FAST8 | 82.0 | 7 | 1 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 152 | BUY | FAST8 | 82.0 | 7 | 7 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7312276363372803 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 153 | BUY | FAST8 | 82.0 | 7 | 4 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18634676933288574 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 5 | 3-7 | 154 | MOVE_BOARD | FAST8 | 82.0 | 7 | 2 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012071347795426846 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 155 | MOVE_BOARD | FAST8 | 82.0 | 7 | 2 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016970612108707428 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 156 | PASS | FAST8 | 82.0 | 7 | 2 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 162 | BUY | FAST8 | 82.0 | 7 | 7 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21355125308036804 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 163 | CRAFT_AND_EQUIP | FAST8 | 82.0 | 7 | 4 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18197238445281982 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 164 | CRAFT_AND_EQUIP | FAST8 | 82.0 | 7 | 4 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20932528376579285 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 165 | MOVE_BOARD | FAST8 | 82.0 | 7 | 4 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0023523513227701187 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 166 | SELL | FAST8 | 82.0 | 7 | 4 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029440000653266907 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 4-1 | 167 | BUY | FAST8 | 82.0 | 7 | 7 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22648784518241882 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 5 | 4-1 | 168 | MOVE_BOARD | FAST8 | 82.0 | 7 | 4 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017761836061254144 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 169 | MOVE_BOARD | FAST8 | 82.0 | 7 | 4 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015513354912400246 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 170 | PASS | FAST8 | 82.0 | 7 | 4 | 0 | 30.0 | Enfeitiçador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 172 | SELL | FAST8 | 82.0 | 7 | 11 | 1 | 30.0 | Enfeitiçador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2774200141429901 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 4-2 | 173 | BUY | FAST8 | 82.0 | 7 | 19 | 1 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19843867421150208 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 5 | 4-2 | 174 | SELL | FAST8 | 82.0 | 7 | 16 | 1 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004000000189989805 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 4-2 | 175 | BUY | FAST8 | 82.0 | 7 | 17 | 1 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12106069922447205 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -— |
| Jogador 5 | 4-2 | 176 | BUY_XP | FAST8 | 82.0 | 7 | 14 | 1 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 177 | BUY_XP | FAST8 | 82.0 | 7 | 10 | 1 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 178 | BUY_XP | FAST8 | 82.0 | 7 | 6 | 0 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 179 | MOVE_BOARD | FAST8 | 82.0 | 7 | 2 | 0 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0027796379290521145 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 180 | MOVE_BOARD | FAST8 | 82.0 | 7 | 2 | 0 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015466546639800072 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 182 | SELL | FAST8 | 82.0 | 7 | 9 | 0 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09663999825716019 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 5 | 4-3 | 183 | BUY | FAST8 | 82.0 | 7 | 12 | 1 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5499067902565002 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 5 | 4-3 | 184 | SELL | FAST8 | 82.0 | 7 | 9 | 0 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08671999722719193 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 4-3 | 185 | BUY | FAST8 | 82.0 | 7 | 11 | 1 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6775158643722534 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -0f1b15a2-9978-4691-a15e-483ccd03db7f,9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 4-3 | 186 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 8 | 0 | 18.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15622974932193756 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 187 | BUY_XP | STABILIZE | 82.0 | 7 | 8 | 0 | 24.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 188 | BUY_XP | STABILIZE | 82.0 | 7 | 4 | 0 | 24.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 189 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 0 | 0 | 24.0 | Enfeitiçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020168686751276255 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 190 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 0 | 0 | 24.0 | Enfeitiçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4311358630657196 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 192 | BUY | FAST8 | 82.0 | 7 | 7 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.715872585773468 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -d8ecc66e-097d-4caa-a657-90fcd1286c2b,dde5ed69-0fc4-4d15-b12c-a5252a239040 |
| Jogador 5 | 4-4 | 193 | BUY | FAST8 | 82.0 | 7 | 4 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022209059447050095 | 0.0 | 0.0 | +b26a039f-581c-4de2-8a75-f7e8a4ef0e4a / -— |
| Jogador 5 | 4-4 | 194 | MOVE_BOARD | FAST8 | 82.0 | 7 | 2 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0039941915310919285 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 195 | MOVE_BOARD | FAST8 | 82.0 | 7 | 2 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014212465845048428 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 196 | PASS | FAST8 | 82.0 | 7 | 2 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 202 | BUY | FAST8 | 82.0 | 7 | 8 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21755750477313995 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 5 | 4-5 | 203 | BUY | FAST8 | 82.0 | 7 | 7 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021760782226920128 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 5 | 4-5 | 204 | MOVE_BOARD | FAST8 | 82.0 | 7 | 6 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007697618566453457 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 205 | MOVE_BOARD | FAST8 | 82.0 | 7 | 6 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014923815615475178 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 206 | PASS | FAST8 | 82.0 | 7 | 6 | 0 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 212 | SELL | FAST8 | 82.0 | 7 | 14 | 1 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14338932931423187 | 0.0 | 0.0 | +— / -ad19ac66-9f86-4c29-8ae7-7222164aece1 |
| Jogador 5 | 4-6 | 213 | BUY | FAST8 | 82.0 | 7 | 22 | 2 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5175477862358093 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 5 | 4-6 | 214 | MOVE_BOARD | FAST8 | 82.0 | 7 | 21 | 2 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 215 | MOVE_BOARD | FAST8 | 82.0 | 7 | 21 | 2 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022741276770830154 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 216 | PASS | FAST8 | 82.0 | 7 | 21 | 2 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029285714030265808 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 222 | SELL | FAST8 | 82.0 | 7 | 32 | 3 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004394684452563524 | 0.0 | 0.0 | +— / -b26a039f-581c-4de2-8a75-f7e8a4ef0e4a |
| Jogador 5 | 4-7 | 223 | BUY | FAST8 | 82.0 | 7 | 34 | 3 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2294645458459854 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 5 | 4-7 | 224 | MOVE_BOARD | FAST8 | 82.0 | 7 | 30 | 3 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.856460095150396e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 225 | MOVE_BOARD | FAST8 | 82.0 | 7 | 30 | 3 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011570129543542862 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 226 | MOVE_BOARD | FAST8 | 82.0 | 7 | 30 | 3 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018349334597587585 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 227 | PASS | FAST8 | 82.0 | 7 | 30 | 3 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0357142873108387 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 232 | CRAFT_AND_EQUIP | FAST8 | 82.0 | 7 | 41 | 4 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09651949256658554 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 233 | CRAFT_AND_EQUIP | FAST8 | 82.0 | 7 | 41 | 4 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13919241726398468 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 234 | SELL | FAST8 | 82.0 | 7 | 41 | 4 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020320000126957893 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 5 | 5-1 | 235 | BUY | FAST8 | 82.0 | 7 | 45 | 4 | 36.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8960802555084229 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -0debca82-3a2a-44ba-af48-83211d5e5243,e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 5-1 | 236 | BUY | FAST8 | 82.0 | 7 | 42 | 4 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0269971564412117 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 5 | 5-1 | 237 | BUY_XP | FAST8 | 82.0 | 7 | 38 | 3 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017400000244379044 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 238 | BUY_XP | FAST8 | 82.0 | 7 | 34 | 3 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017400000244379044 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 239 | MOVE_BOARD | FAST8 | 82.0 | 7 | 30 | 3 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00194306462071836 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 240 | BUY_XP | FAST8 | 82.0 | 7 | 30 | 3 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016625000163912773 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 242 | SELL | ECON | 67.0 | 8 | 33 | 3 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2156440019607544 | 0.0 | 0.0 | +— / -b0c8ce74-5ce1-4ed0-82ac-f95013475f3c |
| Jogador 5 | 5-2 | 243 | EQUIP_FROM_INVENTORY | ECON | 67.0 | 8 | 41 | 4 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10444852709770203 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 244 | EQUIP_FROM_INVENTORY | ECON | 67.0 | 8 | 41 | 4 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07414307445287704 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 245 | BUY | ECON | 67.0 | 8 | 41 | 4 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020763495936989784 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 5 | 5-2 | 246 | MOVE_BENCH | ECON | 67.0 | 8 | 39 | 3 | 30.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27512332797050476 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 247 | BUY | ECON | 67.0 | 8 | 39 | 3 | 32.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03312066197395325 | 0.0 | 0.0 | +da6c9f59-1fc3-467d-8845-bf7b38b4232c / -— |
| Jogador 5 | 5-2 | 248 | BUY_XP | ECON | 67.0 | 8 | 35 | 3 | 32.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019999999552965164 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 249 | BUY_XP | ECON | 67.0 | 8 | 31 | 3 | 32.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 250 | BUY_XP | ECON | 67.0 | 8 | 27 | 2 | 32.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019999999552965164 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 252 | SELL | ECON | 50.0 | 8 | 31 | 3 | 32.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012480000033974648 | 0.0 | 0.0 | +— / -986fbe1e-1826-4be7-a5d6-410a4c0a3f2f |
| Jogador 5 | 5-3 | 253 | BUY | ECON | 50.0 | 8 | 33 | 3 | 32.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014498285949230194 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 5 | 5-3 | 254 | MOVE_BENCH | ECON | 50.0 | 8 | 29 | 2 | 32.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3914988338947296 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 255 | SELL | ECON | 50.0 | 8 | 29 | 2 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0751403272151947 | 0.0 | 0.0 | +— / -e1055913-2340-4af0-8527-e175c8bc1ccb |
| Jogador 5 | 5-3 | 256 | BUY | ECON | 50.0 | 8 | 33 | 3 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036260832101106644 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 5 | 5-3 | 257 | MOVE_BOARD | ECON | 50.0 | 8 | 30 | 3 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002421566314296797 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 258 | BUY_XP | ECON | 50.0 | 8 | 30 | 3 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 259 | MOVE_BOARD | ECON | 50.0 | 8 | 26 | 2 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003039394738152623 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 260 | MOVE_BOARD | ECON | 50.0 | 8 | 26 | 2 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010051451623439789 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 262 | BUY | STABILIZE | 35.0 | 8 | 34 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6044726967811584 | 0.0 | 0.0 | +7a419783-907e-47e2-bf69-29a54ee18a02 / -— |
| Jogador 5 | 5-4 | 263 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 31 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 264 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 31 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015030529350042343 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 265 | PASS | STABILIZE | 35.0 | 8 | 31 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05376031622290611 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 272 | SELL | STABILIZE | 35.0 | 8 | 40 | 4 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27445998787879944 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 5 | 5-5 | 273 | BUY | STABILIZE | 35.0 | 8 | 41 | 4 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7625263929367065 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -— |
| Jogador 5 | 5-5 | 274 | SELL | STABILIZE | 35.0 | 8 | 37 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011359999887645245 | 0.0 | 0.0 | +— / -f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 |
| Jogador 5 | 5-5 | 275 | BUY | STABILIZE | 35.0 | 8 | 38 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11943727731704712 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 5 | 5-5 | 276 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 33 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.535201570542995e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 277 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 33 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02026149071753025 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 278 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 33 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009717167355120182 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 279 | PASS | STABILIZE | 35.0 | 8 | 33 | 3 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.056635450571775436 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 282 | SELL | STABILIZE | 35.0 | 8 | 42 | 4 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27285999059677124 | 0.0 | 0.0 | +— / -7a419783-907e-47e2-bf69-29a54ee18a02 |
| Jogador 5 | 5-6 | 283 | BUY | STABILIZE | 35.0 | 8 | 45 | 4 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0443330779671669 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -— |
| Jogador 5 | 5-6 | 284 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 42 | 4 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.322276138031157e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 285 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 42 | 4 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014987052418291569 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 286 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 42 | 4 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998882077634335 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 287 | PASS | STABILIZE | 35.0 | 8 | 42 | 4 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06826984137296677 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 292 | SELL | STABILIZE | 35.0 | 8 | 51 | 5 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007600000128149986 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 5 | 5-7 | 293 | BUY | STABILIZE | 35.0 | 8 | 54 | 5 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9482781887054443 | 0.0 | 0.0 | +08731924-b808-4070-8c85-2c747847d835 / -d381c462-a17f-4192-b694-66a7c3aaee4f,f2dbe099-e518-4261-b120-9f327b112dcb |
| Jogador 5 | 5-7 | 294 | BUY | STABILIZE | 35.0 | 8 | 50 | 5 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060076840221881866 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 5 | 5-7 | 295 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 48 | 4 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.885780562815853e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 296 | BUY_XP | STABILIZE | 35.0 | 8 | 48 | 4 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 297 | BUY_XP | STABILIZE | 35.0 | 8 | 44 | 4 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 298 | BUY_XP | STABILIZE | 35.0 | 8 | 40 | 4 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 299 | BUY_XP | STABILIZE | 35.0 | 8 | 36 | 3 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 300 | BUY_XP | STABILIZE | 35.0 | 8 | 32 | 3 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 302 | EQUIP_FROM_INVENTORY | STABILIZE | 35.0 | 8 | 35 | 3 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13882261514663696 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 303 | SELL | STABILIZE | 35.0 | 8 | 35 | 3 | 38.0 | Enfeitiçador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09333200007677078 | 0.0 | 0.0 | +— / -08731924-b808-4070-8c85-2c747847d835 |
| Jogador 5 | 6-1 | 304 | BUY | STABILIZE | 35.0 | 8 | 46 | 4 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9267449378967285 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 5 | 6-1 | 305 | SELL | STABILIZE | 35.0 | 8 | 45 | 4 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006719999946653843 | 0.0 | 0.0 | +— / -3c5f5211-f30d-44e7-ac68-0ce513a3d614 |
| Jogador 5 | 6-1 | 306 | BUY | STABILIZE | 35.0 | 8 | 47 | 4 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8834882974624634 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 5 | 6-1 | 307 | SELL | STABILIZE | 35.0 | 8 | 44 | 4 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010283898562192917 | 0.0 | 0.0 | +— / -c07a17cf-e9e7-42be-b925-cb4f699593de |
| Jogador 5 | 6-1 | 308 | BUY | STABILIZE | 35.0 | 8 | 47 | 4 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7626962661743164 | 0.0 | 0.0 | +be1e11e4-dc58-4e75-a402-3a2d831ac7b3 / -— |
| Jogador 5 | 6-1 | 309 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 42 | 4 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 310 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 42 | 4 | 38.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015042217448353767 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 312 | BUY | STABILIZE | 35.0 | 8 | 53 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21531370282173157 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -— |
| Jogador 5 | 6-2 | 313 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 50 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00011921434634132311 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 314 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 50 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014868342317640781 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 315 | PASS | STABILIZE | 35.0 | 8 | 50 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11733333021402359 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 322 | SELL | STABILIZE | 35.0 | 8 | 61 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028878379613161087 | 0.0 | 0.0 | +— / -a37d8478-8a98-4099-bb18-3602d68764f5 |
| Jogador 5 | 6-3 | 323 | BUY | STABILIZE | 35.0 | 8 | 64 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21543049812316895 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 5 | 6-3 | 324 | SELL | STABILIZE | 35.0 | 8 | 61 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028856249526143074 | 0.0 | 0.0 | +— / -8538e488-6f36-433a-b261-73626f24bb07 |
| Jogador 5 | 6-3 | 325 | BUY | STABILIZE | 35.0 | 8 | 64 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07287435978651047 | 0.0 | 0.0 | +d632ff66-a7c4-43d3-afb3-b83c174cda35 / -— |
| Jogador 5 | 6-3 | 326 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 59 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.8199876396683976e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 327 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 59 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015010456554591656 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 328 | MOVE_BOARD | STABILIZE | 35.0 | 8 | 59 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 329 | PASS | STABILIZE | 35.0 | 8 | 59 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12369995564222336 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 332 | SELL | STABILIZE | 19.0 | 8 | 69 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20069199800491333 | 0.0 | 0.0 | +— / -691cde76-cf1b-4a60-b818-65f790e312ec |
| Jogador 5 | 6-4 | 333 | BUY | STABILIZE | 19.0 | 8 | 71 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.960098147392273 | 0.0 | 0.0 | +b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 / -— |
| Jogador 5 | 6-4 | 334 | SELL | STABILIZE | 19.0 | 8 | 67 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27358001470565796 | 0.0 | 0.0 | +— / -1bf15a91-4832-4245-9b48-382a27410263 |
| Jogador 5 | 6-4 | 335 | BUY | STABILIZE | 19.0 | 8 | 70 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40536704659461975 | 0.0 | 0.0 | +17279599-f3fc-4cf2-874f-da62a23ac238 / -— |
| Jogador 5 | 6-4 | 336 | SELL | STABILIZE | 19.0 | 8 | 68 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20069199800491333 | 0.0 | 0.0 | +— / -17279599-f3fc-4cf2-874f-da62a23ac238 |
| Jogador 5 | 6-4 | 337 | BUY | STABILIZE | 19.0 | 8 | 70 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14192625880241394 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 5 | 6-4 | 338 | MOVE_BOARD | STABILIZE | 19.0 | 8 | 67 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.054448148352094e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 339 | MOVE_BOARD | STABILIZE | 19.0 | 8 | 67 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999272301793098 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 340 | MOVE_BOARD | STABILIZE | 19.0 | 8 | 67 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500030979514122 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 342 | SELL | STABILIZE | 19.0 | 8 | 77 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007600000128149986 | 0.0 | 0.0 | +— / -bfe7ca8a-6e89-4673-b142-262e012398a9 |
| Jogador 5 | 6-5 | 343 | BUY | STABILIZE | 19.0 | 8 | 80 | 5 | 48.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.079216718673706 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c,df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 6-5 | 344 | BUY | STABILIZE | 19.0 | 8 | 77 | 5 | 42.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6614770889282227 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -— |
| Jogador 5 | 6-5 | 345 | SELL | STABILIZE | 19.0 | 8 | 74 | 5 | 42.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35345199704170227 | 0.0 | 0.0 | +— / -dc423197-9320-4651-b71d-a62086416f9d |
| Jogador 5 | 6-5 | 346 | EQUIP_FROM_INVENTORY | STABILIZE | 19.0 | 8 | 82 | 5 | 42.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13053138554096222 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 347 | BUY | STABILIZE | 19.0 | 8 | 82 | 5 | 42.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15922360122203827 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -— |
| Jogador 5 | 6-5 | 348 | BUY_XP | STABILIZE | 19.0 | 8 | 79 | 5 | 42.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05813249945640564 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 349 | BUY_XP | STABILIZE | 19.0 | 8 | 75 | 5 | 42.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05756250023841858 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 350 | BUY_XP | STABILIZE | 19.0 | 8 | 71 | 5 | 42.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6561112403869629 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.17109805345535278 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 9 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9946255087852478 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12545929849147797 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021449394524097443 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5458027720451355 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23212078213691711 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 17 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21634778380393982 | 0.0 | 0.0 | +— / -c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 1-3 | 18 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.11618693172931671 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 19 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025510579347610474 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020172372460365295 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 22 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0262550115585327 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2409178465604782 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10219843685626984 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2175285667181015 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015096897259354591 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 32 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3039020001888275 | 0.0 | 0.0 | +c8b72b14-11a4-48e6-8135-41efdbc347cb / -— |
| Jogador 6 | 2-1 | 33 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11227715015411377 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 34 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13590148091316223 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0933062732219696 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 36 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28756484389305115 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 37 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9024146199226379 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05075222998857498 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01688888669013977 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 41 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21953928470611572 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 42 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05251999944448471 | 0.0 | 0.0 | +— / -3cb4d077-df9a-4fd2-9a68-7301aff1b657 |
| Jogador 6 | 2-2 | 43 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 44 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041830770671367645 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 45 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08131002634763718 | 0.0 | 0.0 | +— / -c8b72b14-11a4-48e6-8135-41efdbc347cb |
| Jogador 6 | 2-2 | 46 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10604330897331238 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 47 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06590262800455093 | 0.0 | 0.0 | +— / -c19cf6a8-c66e-4670-b0fc-fb83453f22e7 |
| Jogador 6 | 2-2 | 48 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16879600286483765 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-3 | 50 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26563748717308044 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-4 | 52 | BUY | STABILIZE | 91.0 | 5 | 14 | 1 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2794783413410187 | 0.0 | 0.0 | +77d51a33-bfc7-4b8b-b460-8a4a45391474 / -— |
| Jogador 6 | 2-4 | 53 | BUY | STABILIZE | 91.0 | 5 | 13 | 1 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18169005215168 | 0.0 | 0.0 | +2c497125-ca06-46b1-a3b3-9a59d904705b / -— |
| Jogador 6 | 2-4 | 54 | BUY_XP | STABILIZE | 91.0 | 5 | 12 | 1 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14300000667572021 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 55 | BUY_XP | STABILIZE | 91.0 | 5 | 8 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 56 | BUY_XP | STABILIZE | 91.0 | 5 | 4 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 57 | SELL | STABILIZE | 91.0 | 5 | 0 | 0 | 8.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08787620067596436 | 0.0 | 0.0 | +— / -77d51a33-bfc7-4b8b-b460-8a4a45391474 |
| Jogador 6 | 2-4 | 58 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 1 | 0 | 8.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200184181332588 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 59 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 1 | 0 | 8.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3906112313270569 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 61 | BUY | STABILIZE | 91.0 | 5 | 7 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0478413105010986 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -425b1e77-5887-40b3-875e-c1f60dc6c513,908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-5 | 62 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 6 | 0 | 8.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8165738582611084 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 63 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 6 | 0 | 8.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33415767550468445 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 64 | BUY | STABILIZE | 91.0 | 5 | 6 | 0 | 10.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11991972476243973 | 0.0 | 0.0 | +f957e607-dd51-492b-9186-252da4e0c12f / -— |
| Jogador 6 | 2-5 | 65 | BUY | STABILIZE | 91.0 | 5 | 5 | 0 | 10.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03502865508198738 | 0.0 | 0.0 | +0023f061-5310-4e39-849a-22ad49993d8c / -— |
| Jogador 6 | 2-5 | 66 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 3 | 0 | 10.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20653797686100006 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 67 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 3 | 0 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05528907850384712 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 68 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 3 | 0 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05318755656480789 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 69 | SELL | STABILIZE | 91.0 | 5 | 3 | 0 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38377273082733154 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-5 | 70 | BUY_XP | STABILIZE | 91.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 72 | BUY | STABILIZE | 86.0 | 6 | 8 | 0 | 12.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8254032135009766 | 0.0 | 0.0 | +f5511428-5be8-475d-949c-1d840a0aed4d / -— |
| Jogador 6 | 2-6 | 73 | BUY | STABILIZE | 86.0 | 6 | 7 | 0 | 12.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3239762783050537 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 74 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 4 | 0 | 12.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24418911337852478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 75 | BUY | STABILIZE | 86.0 | 6 | 4 | 0 | 14.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32314884662628174 | 0.0 | 0.0 | +2a7dd07f-3b48-489c-8822-9ec2434a01cf / -— |
| Jogador 6 | 2-6 | 76 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 2 | 0 | 14.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3184139132499695 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 77 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 2 | 0 | 16.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 78 | PASS | STABILIZE | 86.0 | 6 | 2 | 0 | 16.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 80 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 2 | 0 | 16.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37955477833747864 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 82 | BUY | STABILIZE | 86.0 | 6 | 8 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9017952680587769 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 83 | BUY | STABILIZE | 86.0 | 6 | 5 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8970971703529358 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 84 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02674074098467827 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 85 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005050791427493095 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 86 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014831552281975746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 87 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014503015205264091 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 88 | PASS | STABILIZE | 86.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 91 | BUY | STABILIZE | 86.0 | 6 | 7 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24178707599639893 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 92 | CRAFT_AND_EQUIP | STABILIZE | 86.0 | 6 | 4 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15035226941108704 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 93 | SELL | STABILIZE | 86.0 | 6 | 4 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26846304535865784 | 0.0 | 0.0 | +— / -f957e607-dd51-492b-9186-252da4e0c12f |
| Jogador 6 | 3-1 | 94 | BUY | STABILIZE | 86.0 | 6 | 5 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023902159184217453 | 0.0 | 0.0 | +ab127012-83d7-46f0-a16c-b20582d1179b / -— |
| Jogador 6 | 3-1 | 95 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 96 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01475666556507349 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 97 | PASS | STABILIZE | 86.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 102 | SELL | STABILIZE | 76.0 | 6 | 8 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08754255622625351 | 0.0 | 0.0 | +— / -ab127012-83d7-46f0-a16c-b20582d1179b |
| Jogador 6 | 3-2 | 103 | BUY | STABILIZE | 76.0 | 6 | 10 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7579777836799622 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -185ee377-0917-4209-905b-9486d5be0193,646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 3-2 | 104 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8363221883773804 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 105 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 8 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09784018993377686 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 106 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 8 | 0 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13444362580776215 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 107 | BUY | STABILIZE | 76.0 | 6 | 8 | 0 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059068500995635986 | 0.0 | 0.0 | +6e096b30-0b49-4a98-8596-8b05089793ae / -— |
| Jogador 6 | 3-2 | 108 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 5 | 0 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7591925859451294 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 109 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 110 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34651559591293335 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-3 | 112 | EQUIP_FROM_INVENTORY | STABILIZE | 76.0 | 6 | 10 | 1 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07785514742136002 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 113 | EQUIP_FROM_INVENTORY | STABILIZE | 76.0 | 6 | 10 | 1 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06670695543289185 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 114 | BUY | STABILIZE | 76.0 | 6 | 10 | 1 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17628952860832214 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 6 | 3-3 | 115 | BUY_XP | STABILIZE | 76.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 116 | BUY_XP | STABILIZE | 76.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 117 | SELL | STABILIZE | 76.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39673998951911926 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-3 | 118 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11070595681667328 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 119 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3918149173259735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 120 | BUY | STABILIZE | 76.0 | 6 | 3 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04595084488391876 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-4 | 122 | BUY | STABILIZE | 65.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8339301347732544 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -43da0d73-facd-488b-b856-94e9496a97f9,9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-4 | 123 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0850528269656934e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 124 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 125 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999525621533394 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 126 | PASS | STABILIZE | 65.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 132 | BUY | STABILIZE | 65.0 | 6 | 7 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8052309155464172 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-5 | 133 | BUY_XP | STABILIZE | 65.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 134 | MOVE_BENCH | STABILIZE | 65.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0992005243897438 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 135 | MOVE_BOARD | FAST8 | 65.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05182303488254547 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 136 | MOVE_BOARD | FAST8 | 65.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02177966758608818 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 137 | MOVE_BOARD | FAST8 | 65.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 138 | MOVE_BOARD | FAST8 | 65.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 139 | PASS | FAST8 | 65.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 142 | BUY | FAST8 | 65.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1472744196653366 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 143 | BUY_XP | FAST8 | 65.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 144 | MOVE_BOARD | FAST8 | 65.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.4204310900822747e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 145 | MOVE_BOARD | FAST8 | 65.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 146 | MOVE_BOARD | FAST8 | 65.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014970062300562859 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 147 | PASS | FAST8 | 65.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 152 | MOVE_BENCH | FAST8 | 65.0 | 7 | 7 | 0 | 32.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0962090939283371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 153 | MOVE_BENCH | FAST8 | 65.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.386025995016098 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 154 | BUY | FAST8 | 65.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10218852013349533 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 155 | MOVE_BENCH | FAST8 | 65.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06086684390902519 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 156 | BUY | FAST8 | 65.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034032728523015976 | 0.0 | 0.0 | +3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 / -— |
| Jogador 6 | 3-7 | 157 | MOVE_BOARD | FAST8 | 65.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 158 | MOVE_BOARD | FAST8 | 65.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 159 | PASS | FAST8 | 65.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 162 | CRAFT_AND_EQUIP | FAST8 | 65.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11132178455591202 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 163 | CRAFT_AND_EQUIP | FAST8 | 65.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10936260968446732 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 164 | SELL | FAST8 | 65.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003034308087080717 | 0.0 | 0.0 | +— / -f5511428-5be8-475d-949c-1d840a0aed4d |
| Jogador 6 | 4-1 | 165 | EQUIP_FROM_INVENTORY | FAST8 | 65.0 | 7 | 9 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08810387551784515 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 166 | EQUIP_FROM_INVENTORY | FAST8 | 65.0 | 7 | 9 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.03694969788193703 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 167 | BUY | FAST8 | 65.0 | 7 | 9 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46064436435699463 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 168 | BUY_XP | FAST8 | 65.0 | 7 | 6 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 169 | MOVE_BENCH | FAST8 | 65.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005686796735972166 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 170 | MOVE_BENCH | FAST8 | 65.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7584561109542847 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 172 | SELL | FAST8 | 65.0 | 7 | 9 | 0 | 44.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08806877583265305 | 0.0 | 0.0 | +— / -3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 |
| Jogador 6 | 4-2 | 173 | BUY | FAST8 | 65.0 | 7 | 10 | 1 | 44.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6839128136634827 | 0.0 | 0.0 | +6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede,fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 4-2 | 174 | BUY | FAST8 | 65.0 | 7 | 7 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.572699785232544 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -— |
| Jogador 6 | 4-2 | 175 | BUY | FAST8 | 65.0 | 7 | 4 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.693667471408844 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -6e096b30-0b49-4a98-8596-8b05089793ae,7fd8b302-97aa-4373-94f4-adfcad477ed2 |
| Jogador 6 | 4-2 | 176 | MOVE_BENCH | FAST8 | 65.0 | 7 | 1 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09635909646749496 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 177 | MOVE_BOARD | FAST8 | 65.0 | 7 | 1 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 178 | PASS | FAST8 | 65.0 | 7 | 1 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 182 | BUY | FAST8 | 65.0 | 7 | 8 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21077322959899902 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-3 | 183 | BUY_XP | FAST8 | 65.0 | 7 | 4 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 184 | MOVE_BOARD | FAST8 | 65.0 | 7 | 0 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 185 | MOVE_BOARD | FAST8 | 65.0 | 7 | 0 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 186 | PASS | FAST8 | 65.0 | 7 | 0 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 192 | BUY | FAST8 | 65.0 | 7 | 8 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21765190362930298 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 6 | 4-4 | 193 | BUY_XP | FAST8 | 65.0 | 7 | 7 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 194 | SELL | FAST8 | 65.0 | 7 | 3 | 0 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07341594994068146 | 0.0 | 0.0 | +— / -93f7279f-b03b-407b-b623-c0a2bd88f877 |
| Jogador 6 | 4-4 | 195 | EQUIP_FROM_INVENTORY | FAST8 | 65.0 | 7 | 11 | 1 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04188872501254082 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 196 | BUY | FAST8 | 65.0 | 7 | 11 | 1 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6501179337501526 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -50f9a30c-27db-4ed0-804e-548f87950b17,f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-4 | 197 | MOVE_BENCH | FAST8 | 65.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33887404203414917 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 198 | MOVE_BOARD | FAST8 | 65.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 199 | MOVE_BOARD | FAST8 | 65.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 200 | PASS | FAST8 | 65.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 202 | BUY | FAST8 | 65.0 | 7 | 15 | 1 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011194487102329731 | 0.0 | 0.0 | +652568b9-7093-4e77-8b9c-7ed286cf7f4c / -— |
| Jogador 6 | 4-5 | 203 | MOVE_BOARD | FAST8 | 65.0 | 7 | 13 | 1 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.8209329937235452e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 204 | BUY | FAST8 | 65.0 | 7 | 13 | 1 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0050054313614964485 | 0.0 | 0.0 | +1ff42607-ccac-4d3f-8277-bccddf08862f / -— |
| Jogador 6 | 4-5 | 205 | MOVE_BOARD | FAST8 | 65.0 | 7 | 12 | 1 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 206 | MOVE_BOARD | FAST8 | 65.0 | 7 | 12 | 1 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 207 | PASS | FAST8 | 65.0 | 7 | 12 | 1 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 212 | SELL | FAST8 | 65.0 | 7 | 22 | 2 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08195926249027252 | 0.0 | 0.0 | +— / -b755a0c5-f515-4f95-8f58-1e05f40ad302 |
| Jogador 6 | 4-6 | 213 | BUY | FAST8 | 65.0 | 7 | 30 | 3 | 44.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6918365955352783 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 6 | 4-6 | 214 | MOVE_BOARD | FAST8 | 65.0 | 7 | 28 | 2 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 215 | MOVE_BOARD | FAST8 | 65.0 | 7 | 28 | 2 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 216 | PASS | FAST8 | 65.0 | 7 | 28 | 2 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034285712987184525 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 222 | MOVE_BOARD | FAST8 | 65.0 | 7 | 39 | 3 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.682164474914316e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 223 | MOVE_BOARD | FAST8 | 65.0 | 7 | 39 | 3 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 224 | MOVE_BOARD | FAST8 | 65.0 | 7 | 39 | 3 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 225 | PASS | FAST8 | 65.0 | 7 | 39 | 3 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04214285686612129 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 232 | CRAFT_AND_EQUIP | FAST8 | 65.0 | 7 | 50 | 5 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10607542097568512 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 233 | CRAFT_AND_EQUIP | FAST8 | 65.0 | 7 | 50 | 5 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15775145590305328 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 234 | SELL | FAST8 | 65.0 | 7 | 50 | 5 | 44.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3116439878940582 | 0.0 | 0.0 | +— / -6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb |
| Jogador 6 | 5-1 | 235 | BUY | FAST8 | 65.0 | 7 | 58 | 5 | 44.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6226821541786194 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -— |
| Jogador 6 | 5-1 | 236 | MOVE_BOARD | FAST8 | 65.0 | 7 | 55 | 5 | 44.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 237 | MOVE_BOARD | FAST8 | 65.0 | 7 | 55 | 5 | 44.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 238 | PASS | FAST8 | 65.0 | 7 | 55 | 5 | 44.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0910571813583374 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 242 | SELL | FAST8 | 65.0 | 7 | 69 | 5 | 44.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005249014589935541 | 0.0 | 0.0 | +— / -1ff42607-ccac-4d3f-8277-bccddf08862f |
| Jogador 6 | 5-2 | 243 | BUY | FAST8 | 65.0 | 7 | 70 | 5 | 44.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9498977065086365 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -0fff7760-179f-4d7c-8267-08d70cb6c1bd,5b95b64a-b46a-4827-8613-307c8dadc072 |
| Jogador 6 | 5-2 | 244 | MOVE_BENCH | FAST8 | 65.0 | 7 | 68 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39889246225357056 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 245 | MOVE_BENCH | FAST8 | 65.0 | 7 | 68 | 5 | 32.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08434081077575684 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 246 | MOVE_BENCH | FAST8 | 65.0 | 7 | 68 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41356372833251953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 247 | MOVE_BENCH | FAST8 | 65.0 | 7 | 68 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34917089343070984 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 248 | PASS | FAST8 | 65.0 | 7 | 68 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1005098968744278 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 252 | BUY | FAST8 | 50.0 | 7 | 78 | 5 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9311267137527466 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9,a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 5-3 | 253 | MOVE_BENCH | FAST8 | 50.0 | 7 | 75 | 5 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39701685309410095 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 254 | MOVE_BENCH | FAST8 | 50.0 | 7 | 75 | 5 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5771533846855164 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 255 | MOVE_BOARD | FAST8 | 50.0 | 7 | 75 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 256 | MOVE_BOARD | FAST8 | 50.0 | 7 | 75 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 257 | PASS | FAST8 | 50.0 | 7 | 75 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25995510816574097 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 262 | BUY | FAST8 | 50.0 | 7 | 86 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4027846157550812 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -— |
| Jogador 6 | 5-4 | 263 | BUY_XP | FAST8 | 50.0 | 7 | 82 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008999999612569809 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 264 | BUY_XP | FAST8 | 50.0 | 7 | 78 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008999999612569809 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 265 | BUY_XP | FAST8 | 50.0 | 7 | 74 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008999999612569809 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 266 | BUY_XP | FAST8 | 50.0 | 7 | 70 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008999999612569809 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 267 | MOVE_BOARD | FAST8 | 50.0 | 7 | 66 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.4777218893868849e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 268 | BUY_XP | FAST8 | 50.0 | 7 | 66 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008999999612569809 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 269 | BUY_XP | FAST8 | 50.0 | 7 | 62 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7284500002861023 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 270 | MOVE_BENCH | ECON | 50.0 | 8 | 58 | 5 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7844057083129883 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 272 | BUY | ECON | 50.0 | 8 | 68 | 5 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6158546805381775 | 0.0 | 0.0 | +91eb044c-6989-4b6a-a9fa-a59f75b56743 / -— |
| Jogador 6 | 5-5 | 273 | BUY_XP | ECON | 50.0 | 8 | 65 | 5 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 274 | BUY_XP | ECON | 50.0 | 8 | 61 | 5 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 275 | BUY_XP | ECON | 50.0 | 8 | 57 | 5 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 276 | BUY_XP | ECON | 50.0 | 8 | 53 | 5 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07637500017881393 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 277 | BUY_XP | ECON | 50.0 | 8 | 49 | 4 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027374999597668648 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 278 | BUY_XP | ECON | 50.0 | 8 | 45 | 4 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027374999597668648 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 279 | BUY_XP | ECON | 50.0 | 8 | 41 | 4 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10737500339746475 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 280 | BUY_XP | ECON | 50.0 | 8 | 37 | 3 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027374999597668648 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 282 | BUY | STABILIZE | 36.0 | 8 | 41 | 4 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11980462074279785 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 6 | 5-6 | 283 | BUY_XP | STABILIZE | 36.0 | 8 | 37 | 3 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021299999207258224 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 284 | BUY_XP | STABILIZE | 36.0 | 8 | 33 | 3 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10130000114440918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 285 | BUY_XP | STABILIZE | 36.0 | 8 | 29 | 2 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021299999207258224 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 286 | BUY_XP | STABILIZE | 36.0 | 8 | 25 | 2 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021299999207258224 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 287 | BUY_XP | STABILIZE | 36.0 | 8 | 21 | 2 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10130000114440918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 288 | BUY_XP | STABILIZE | 36.0 | 8 | 17 | 1 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021299999207258224 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 289 | BUY_XP | STABILIZE | 36.0 | 8 | 13 | 1 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10130000114440918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 290 | MOVE_BOARD | STABILIZE | 36.0 | 8 | 9 | 0 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00030763173708692193 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 292 | SELL | STABILIZE | 20.0 | 9 | 15 | 1 | 48.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14382000267505646 | 0.0 | 0.0 | +— / -39b89fbe-9520-4eaa-80f9-81e03232c83c |
| Jogador 6 | 5-7 | 293 | BUY | STABILIZE | 20.0 | 9 | 23 | 2 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7541088461875916 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -— |
| Jogador 6 | 5-7 | 294 | SELL | STABILIZE | 20.0 | 9 | 19 | 1 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2865000069141388 | 0.0 | 0.0 | +— / -3658b5d8-450f-451a-8487-5b3bdd7c385b |
| Jogador 6 | 5-7 | 295 | BUY | STABILIZE | 20.0 | 9 | 24 | 2 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3280925750732422 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 6 | 5-7 | 296 | BUY_XP | STABILIZE | 20.0 | 9 | 21 | 2 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 297 | BUY_XP | STABILIZE | 20.0 | 9 | 17 | 1 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 298 | BUY_XP | STABILIZE | 20.0 | 9 | 13 | 1 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 299 | BUY_XP | STABILIZE | 20.0 | 9 | 9 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 300 | BUY_XP | STABILIZE | 20.0 | 9 | 5 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 302 | EQUIP_FROM_INVENTORY | STABILIZE | 20.0 | 9 | 7 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 303 | SELL | STABILIZE | 20.0 | 9 | 7 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07229071110486984 | 0.0 | 0.0 | +— / -7de5aac5-85d7-4add-b5a7-1c89be9d7e40 |
| Jogador 6 | 6-1 | 304 | BUY | STABILIZE | 20.0 | 9 | 11 | 1 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7519931197166443 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -03e5f6e4-e80d-49c1-b5bb-e5b158d96f51,d4c27edc-9b7e-4a31-a967-3aa80766b470 |
| Jogador 6 | 6-1 | 305 | MOVE_BENCH | STABILIZE | 20.0 | 9 | 7 | 0 | 40.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09606477618217468 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 306 | MOVE_BENCH | STABILIZE | 20.0 | 9 | 7 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41350114345550537 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 307 | MOVE_BENCH | STABILIZE | 20.0 | 9 | 7 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29385828971862793 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 308 | MOVE_BENCH | STABILIZE | 20.0 | 9 | 7 | 0 | 38.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06198246777057648 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 309 | BUY_XP | STABILIZE | 20.0 | 9 | 7 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 310 | MOVE_BENCH | STABILIZE | 20.0 | 9 | 3 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07403423637151718 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 312 | BUY | ALL_IN | 2.0 | 9 | 9 | 0 | 40.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27199095487594604 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -— |
| Jogador 6 | 6-2 | 313 | BUY | ALL_IN | 2.0 | 9 | 5 | 0 | 40.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27474889159202576 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 6 | 6-2 | 314 | MOVE_BENCH | ALL_IN | 2.0 | 9 | 3 | 0 | 40.0 | Colosso/DA_Amumu18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39912140369415283 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 315 | MOVE_BENCH | ALL_IN | 2.0 | 9 | 3 | 0 | 38.0 | Colosso/DA_Amumu18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06295207142829895 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 316 | MOVE_BENCH | ALL_IN | 2.0 | 9 | 3 | 0 | 42.0 | Colosso/DA_Amumu18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06080595403909683 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 317 | MOVE_BENCH | ALL_IN | 2.0 | 9 | 3 | 0 | 40.0 | Colosso/DA_Amumu18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4130060374736786 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 318 | MOVE_BENCH | ALL_IN | 2.0 | 9 | 3 | 0 | 38.0 | Colosso/DA_Amumu18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06320436298847198 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 319 | MOVE_BENCH | ALL_IN | 2.0 | 9 | 3 | 0 | 42.0 | Colosso/DA_Amumu18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3113899827003479 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 320 | MOVE_BOARD | ALL_IN | 2.0 | 9 | 3 | 0 | 44.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.903760787376086e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3500058054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 9 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6420197486877441 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22610600292682648 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0388437509536743 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2662448287010193 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08020386844873428 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.601165771484375 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013105367543175817 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 22 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0184402465820312 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2021738439798355 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008631253615021706 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11501160264015198 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 26 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 32 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9689698219299316 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 33 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24282772839069366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 34 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21041633188724518 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 35 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30724674463272095 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.501498281955719 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 37 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2637510597705841 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 7 | 2-1 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04902606084942818 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499971654266119 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 41 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.949948251247406 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 42 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4218553602695465 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 43 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20367467403411865 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 44 | BUY | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12571392953395844 | 0.0 | 0.0 | +98558a52-389f-46fc-b370-6345603f4103 / -— |
| Jogador 7 | 2-2 | 45 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00022559908393304795 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 46 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34902089834213257 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 47 | PASS | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 50 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9450998306274414 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-4 | 52 | BUY | STABILIZE | 90.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20758356153964996 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 53 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27321285009384155 | 0.0 | 0.0 | +3280b28e-bd8f-494b-a78d-111744e2178b / -— |
| Jogador 7 | 2-4 | 54 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44355490803718567 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 55 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030277984216809273 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 56 | PASS | STABILIZE | 90.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 61 | BUY | STABILIZE | 90.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06657764315605164 | 0.0 | 0.0 | +1d709136-338f-4fef-90fc-b2aa1b83d879 / -— |
| Jogador 7 | 2-5 | 62 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 9 | 0 | 14.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08065937459468842 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 63 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 9 | 0 | 14.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4495653808116913 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 64 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 9 | 0 | 14.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03154537081718445 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 65 | PASS | STABILIZE | 90.0 | 4 | 9 | 0 | 14.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 72 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 14 | 1 | 14.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4676904082298279 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 73 | BUY | STABILIZE | 85.0 | 5 | 14 | 1 | 16.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8763675689697266 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 74 | SELL | STABILIZE | 85.0 | 5 | 13 | 1 | 16.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25642287731170654 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 2-6 | 75 | BUY | STABILIZE | 85.0 | 5 | 16 | 1 | 16.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.869625985622406 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 7 | 2-6 | 76 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 14 | 1 | 16.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037376705557107925 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 77 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 14 | 1 | 16.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09579690545797348 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 78 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 14 | 1 | 16.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 79 | PASS | STABILIZE | 85.0 | 5 | 14 | 1 | 16.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 82 | SELL | STABILIZE | 80.0 | 5 | 21 | 2 | 16.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37049999833106995 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-7 | 83 | BUY | STABILIZE | 80.0 | 5 | 24 | 2 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9002790451049805 | 0.0 | 0.0 | +1e0a3ead-540d-4169-a1fc-3e79592564a0 / -— |
| Jogador 7 | 2-7 | 84 | EQUIP_FROM_INVENTORY | STABILIZE | 80.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13101720809936523 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 85 | EQUIP_FROM_INVENTORY | STABILIZE | 80.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15678326785564423 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 86 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29230424761772156 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 87 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38372868299484253 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 88 | PASS | STABILIZE | 80.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 91 | CRAFT_AND_EQUIP | STABILIZE | 80.0 | 5 | 30 | 3 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19504305720329285 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 92 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 30 | 3 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 93 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 30 | 3 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019594142213463783 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 94 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 30 | 3 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3944702744483948 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 95 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 30 | 3 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08164005726575851 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 96 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 30 | 3 | 14.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5028784871101379 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 97 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 30 | 3 | 14.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43826961517333984 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 98 | PASS | STABILIZE | 80.0 | 5 | 30 | 3 | 14.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 102 | SELL | STABILIZE | 69.0 | 5 | 39 | 3 | 14.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09696000069379807 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 3-2 | 103 | BUY | STABILIZE | 69.0 | 5 | 40 | 4 | 14.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8029770255088806 | 0.0 | 0.0 | +fa331d8d-1e0c-49b4-848e-8ad58859331c / -4e206e09-40e3-4699-81cb-8aaf01109dea,a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 3-2 | 104 | MOVE_BENCH | STABILIZE | 69.0 | 5 | 39 | 3 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7069274187088013 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 105 | MOVE_BENCH | STABILIZE | 69.0 | 5 | 39 | 3 | 12.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3394421935081482 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 106 | BUY | STABILIZE | 69.0 | 5 | 39 | 3 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8128501772880554 | 0.0 | 0.0 | +96bf8f0a-9fe1-4182-95dc-903c1e623983 / -— |
| Jogador 7 | 3-2 | 107 | MOVE_BENCH | STABILIZE | 69.0 | 5 | 37 | 3 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07776959240436554 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 108 | MOVE_BENCH | STABILIZE | 69.0 | 5 | 37 | 3 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05544522777199745 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 109 | MOVE_BENCH | STABILIZE | 69.0 | 5 | 37 | 3 | 12.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49183082580566406 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 110 | MOVE_BOARD | STABILIZE | 69.0 | 5 | 37 | 3 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014084752649068832 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 112 | BUY | STABILIZE | 59.0 | 5 | 46 | 4 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8273546695709229 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 113 | SELL | STABILIZE | 59.0 | 5 | 43 | 4 | 16.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37049999833106995 | 0.0 | 0.0 | +— / -fa331d8d-1e0c-49b4-848e-8ad58859331c |
| Jogador 7 | 3-3 | 114 | BUY | STABILIZE | 59.0 | 5 | 46 | 4 | 16.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.609520673751831 | 0.0 | 0.0 | +2399a42a-332c-42ee-9bd8-5f52bb921ffa / -— |
| Jogador 7 | 3-3 | 115 | EQUIP_FROM_INVENTORY | STABILIZE | 59.0 | 5 | 45 | 4 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1530645191669464 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 116 | BUY_XP | STABILIZE | 59.0 | 5 | 45 | 4 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008379999548196793 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 117 | BUY_XP | STABILIZE | 59.0 | 5 | 41 | 4 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07162000238895416 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 118 | BUY_XP | STABILIZE | 59.0 | 5 | 37 | 3 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15501999855041504 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 119 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 33 | 3 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5382927060127258 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 120 | BUY | STABILIZE | 59.0 | 6 | 33 | 3 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23565413057804108 | 0.0 | 0.0 | +4d03897d-0113-4a29-a864-75305c142d97 / -— |
| Jogador 7 | 3-4 | 122 | SELL | STABILIZE | 59.0 | 6 | 40 | 4 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27812203764915466 | 0.0 | 0.0 | +— / -2399a42a-332c-42ee-9bd8-5f52bb921ffa |
| Jogador 7 | 3-4 | 123 | BUY | STABILIZE | 59.0 | 6 | 41 | 4 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.755480945110321 | 0.0 | 0.0 | +7e545d27-1847-4016-b42b-e7db1960ae89 / -— |
| Jogador 7 | 3-4 | 124 | SELL | STABILIZE | 59.0 | 6 | 39 | 3 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.173963263630867 | 0.0 | 0.0 | +— / -42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 7 | 3-4 | 125 | BUY | STABILIZE | 59.0 | 6 | 41 | 4 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3213331699371338 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 7 | 3-4 | 126 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 40 | 4 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 127 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 40 | 4 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014809026382863522 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 128 | PASS | STABILIZE | 59.0 | 6 | 40 | 4 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 132 | SELL | STABILIZE | 59.0 | 6 | 49 | 4 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08785992860794067 | 0.0 | 0.0 | +— / -96bf8f0a-9fe1-4182-95dc-903c1e623983 |
| Jogador 7 | 3-5 | 133 | BUY | STABILIZE | 59.0 | 6 | 51 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23650041222572327 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 134 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 50 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.03231232566759e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 135 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 50 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014855067245662212 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 136 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 50 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 137 | PASS | STABILIZE | 59.0 | 6 | 50 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0560000017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 142 | SELL | STABILIZE | 48.0 | 6 | 60 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26853999495506287 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 3-6 | 143 | BUY | STABILIZE | 48.0 | 6 | 62 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7095991373062134 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 144 | BUY_XP | STABILIZE | 48.0 | 6 | 59 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01092000026255846 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 145 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 55 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002819667279254645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 146 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 55 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020279059186577797 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 147 | PASS | STABILIZE | 48.0 | 6 | 55 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057945478707551956 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 152 | SELL | STABILIZE | 48.0 | 6 | 66 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005439999978989363 | 0.0 | 0.0 | +— / -a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 7 | 3-7 | 153 | BUY | STABILIZE | 48.0 | 6 | 68 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8998544812202454 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -f116ca4e-dbe8-457e-83a5-958525aa384a,fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 3-7 | 154 | BUY | STABILIZE | 48.0 | 6 | 65 | 5 | 16.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7517315745353699 | 0.0 | 0.0 | +1cba4955-961e-4efd-a291-e0a70bf72841 / -— |
| Jogador 7 | 3-7 | 155 | MOVE_BENCH | STABILIZE | 48.0 | 6 | 63 | 5 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5609466433525085 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 156 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 63 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02364867739379406 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 157 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 63 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04067301005125046 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 158 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 63 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03783676028251648 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 159 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 63 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2190239429473877 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 160 | PASS | STABILIZE | 48.0 | 6 | 63 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15956540405750275 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 162 | BUY | STABILIZE | 48.0 | 6 | 73 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.35647639632225037 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -— |
| Jogador 7 | 4-1 | 163 | CRAFT_AND_EQUIP | STABILIZE | 48.0 | 6 | 71 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17477990686893463 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 164 | CRAFT_AND_EQUIP | STABILIZE | 48.0 | 6 | 71 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17463064193725586 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 165 | SELL | STABILIZE | 48.0 | 6 | 71 | 5 | 20.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2955639958381653 | 0.0 | 0.0 | +— / -8a52858d-da47-4de9-8e91-8612788cb8fd |
| Jogador 7 | 4-1 | 166 | BUY | STABILIZE | 48.0 | 6 | 79 | 5 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05046190321445465 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-1 | 167 | BUY_XP | STABILIZE | 48.0 | 6 | 77 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02807999961078167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 168 | BUY_XP | STABILIZE | 48.0 | 6 | 73 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02807999961078167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 169 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 69 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 170 | BUY_XP | STABILIZE | 48.0 | 6 | 69 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02807999961078167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 172 | SELL | STABILIZE | 37.0 | 6 | 75 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006136750802397728 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-2 | 173 | BUY | STABILIZE | 37.0 | 6 | 77 | 5 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8757734894752502 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 7 | 4-2 | 174 | SELL | STABILIZE | 37.0 | 6 | 75 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26105645298957825 | 0.0 | 0.0 | +— / -1e0a3ead-540d-4169-a1fc-3e79592564a0 |
| Jogador 7 | 4-2 | 175 | BUY | STABILIZE | 37.0 | 6 | 77 | 5 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05131146311759949 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -— |
| Jogador 7 | 4-2 | 176 | BUY_XP | STABILIZE | 37.0 | 6 | 75 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02807999961078167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 177 | BUY_XP | STABILIZE | 37.0 | 6 | 71 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3636687397956848 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 178 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 67 | 5 | 20.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4498874545097351 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 179 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 67 | 5 | 24.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11185404658317566 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 180 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 67 | 5 | 24.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013300148770213127 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 182 | BUY | STABILIZE | 24.0 | 7 | 78 | 5 | 24.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15926454961299896 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 7 | 4-3 | 183 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 74 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 184 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 74 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014956027269363403 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 185 | PASS | STABILIZE | 24.0 | 7 | 74 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.132939413189888 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 192 | SELL | STABILIZE | 24.0 | 7 | 85 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0021078167483210564 | 0.0 | 0.0 | +— / -1d709136-338f-4fef-90fc-b2aa1b83d879 |
| Jogador 7 | 4-4 | 193 | BUY | STABILIZE | 24.0 | 7 | 87 | 5 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3696611821651459 | 0.0 | 0.0 | +bb51728e-fcc5-4950-ad03-c864c51c2371 / -— |
| Jogador 7 | 4-4 | 194 | SELL | STABILIZE | 24.0 | 7 | 84 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006145707331597805 | 0.0 | 0.0 | +— / -0803068a-0141-4e75-ab81-12bb13986025 |
| Jogador 7 | 4-4 | 195 | BUY | STABILIZE | 24.0 | 7 | 86 | 5 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19205473363399506 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 7 | 4-4 | 196 | BUY_XP | STABILIZE | 24.0 | 7 | 83 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0587024986743927 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 197 | BUY_XP | STABILIZE | 24.0 | 7 | 79 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05813249945640564 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 198 | BUY_XP | STABILIZE | 24.0 | 7 | 75 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05756250023841858 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 199 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 71 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008578982669860125 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 200 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 71 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014451518654823303 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 202 | SELL | STABILIZE | 24.0 | 7 | 81 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019396960735321045 | 0.0 | 0.0 | +— / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 |
| Jogador 7 | 4-5 | 203 | BUY | STABILIZE | 24.0 | 7 | 84 | 5 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10506929457187653 | 0.0 | 0.0 | +d6a00f0c-4823-44d6-b326-67595876998d / -— |
| Jogador 7 | 4-5 | 204 | BUY_XP | STABILIZE | 24.0 | 7 | 81 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05841749906539917 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 205 | BUY_XP | STABILIZE | 24.0 | 7 | 77 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05784749984741211 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 206 | BUY_XP | STABILIZE | 24.0 | 7 | 73 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05727750062942505 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 207 | BUY_XP | STABILIZE | 24.0 | 7 | 69 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05670750141143799 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 208 | BUY_XP | STABILIZE | 24.0 | 7 | 65 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05613749846816063 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 209 | BUY_XP | STABILIZE | 24.0 | 7 | 61 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05556749925017357 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 210 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 57 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 212 | SELL | ALL_IN | 12.0 | 7 | 67 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2710045576095581 | 0.0 | 0.0 | +— / -d69fa0dc-74b6-4ee7-90f7-aaca5405c59c |
| Jogador 7 | 4-6 | 213 | BUY | ALL_IN | 12.0 | 7 | 70 | 5 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9258872866630554 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 7 | 4-6 | 214 | SELL | ALL_IN | 12.0 | 7 | 69 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1414915770292282 | 0.0 | 0.0 | +— / -42f739bb-e676-4a27-a96f-c09d09d592bb |
| Jogador 7 | 4-6 | 215 | BUY | ALL_IN | 12.0 | 7 | 70 | 5 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.597386360168457 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 7 | 4-6 | 216 | BUY_XP | ALL_IN | 12.0 | 7 | 67 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05754999816417694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 217 | BUY_XP | ALL_IN | 12.0 | 7 | 63 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05694999918341637 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 218 | BUY_XP | ALL_IN | 12.0 | 7 | 59 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5489727258682251 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 219 | BUY_XP | ALL_IN | 12.0 | 8 | 55 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 220 | BUY_XP | ALL_IN | 12.0 | 8 | 51 | 5 | 24.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050999999046325684 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3500058054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 9 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01241401955485344 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 11 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21455475687980652 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2947953939437866 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28815770149230957 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9236916303634644 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3468432128429413 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 22 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0265331268310547 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.115348219871521 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -4ea4d9af-5729-414b-a102-b7fc80667118,74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 1-4 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9170761108398438 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -— |
| Jogador 8 | 1-4 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04184781759977341 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020744144916534424 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 32 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1005061864852905 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -64f24363-3325-4538-972e-a6d8260b3787,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-1 | 33 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.39130663871765137 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -— |
| Jogador 8 | 2-1 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 4.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2961447238922119 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 35 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3667529821395874 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 36 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19415126740932465 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 37 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11158259212970734 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04723525047302246 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.543745756149292 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26907122135162354 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 42 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07421910762786865 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 45 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 50 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9715962409973145 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-4 | 52 | BUY | STABILIZE | 90.0 | 5 | 11 | 1 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9759326577186584 | 0.0 | 0.0 | +fb186a97-59a4-4b3a-be2f-dadd2670dc95 / -— |
| Jogador 8 | 2-4 | 53 | BUY | STABILIZE | 90.0 | 5 | 10 | 1 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.043878667056560516 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 54 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 7 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6278991103172302 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 55 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 7 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4791252613067627 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 56 | BUY_XP | STABILIZE | 90.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 57 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03742942214012146 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 58 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 59 | PASS | STABILIZE | 90.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 61 | BUY | STABILIZE | 90.0 | 5 | 9 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7863238453865051 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 62 | BUY | STABILIZE | 90.0 | 5 | 7 | 0 | 10.0 | Espinhos Negros/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23065535724163055 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 63 | BUY_XP | STABILIZE | 90.0 | 5 | 4 | 0 | 10.0 | Espinhos Negros/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 64 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 10.0 | Espinhos Negros/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014872713945806026 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 65 | SELL | STABILIZE | 90.0 | 5 | 0 | 0 | 10.0 | Espinhos Negros/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31675300002098083 | 0.0 | 0.0 | +— / -322e9047-623a-4fec-a0f9-d21d2fbcd88a |
| Jogador 8 | 2-5 | 66 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 10.0 | Espinhos Negros/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2899016737937927 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 67 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 2 | 0 | 10.0 | Espinhos Negros/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 68 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 2 | 0 | 10.0 | Espinhos Negros/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2594025135040283 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 69 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 2 | 0 | 10.0 | Espinhos Negros/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 70 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 2 | 0 | 10.0 | Espinhos Negros/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3442973792552948 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 72 | BUY | STABILIZE | 83.0 | 5 | 8 | 0 | 10.0 | Espinhos Negros/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8452685475349426 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 73 | SELL | STABILIZE | 83.0 | 5 | 7 | 0 | 10.0 | Espinhos Negros/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22631199657917023 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-6 | 74 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 10.0 | Espinhos Negros/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.053902655839920044 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 75 | SELL | STABILIZE | 83.0 | 5 | 7 | 0 | 10.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005244092550128698 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-6 | 76 | BUY | STABILIZE | 83.0 | 5 | 8 | 0 | 10.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15849754214286804 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 8 | 2-6 | 77 | BUY_XP | STABILIZE | 83.0 | 5 | 7 | 0 | 10.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 78 | SELL | STABILIZE | 83.0 | 5 | 3 | 0 | 10.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007040000054985285 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-6 | 79 | BUY_XP | STABILIZE | 83.0 | 5 | 6 | 0 | 10.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 80 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 2 | 0 | 10.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7017394304275513 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 82 | BUY | STABILIZE | 76.0 | 6 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9013971090316772 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 83 | BUY | STABILIZE | 76.0 | 6 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04098188877105713 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 84 | SELL | STABILIZE | 76.0 | 6 | 2 | 0 | 14.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26677998900413513 | 0.0 | 0.0 | +— / -fb186a97-59a4-4b3a-be2f-dadd2670dc95 |
| Jogador 8 | 2-7 | 85 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5753622055053711 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 86 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1132572591304779 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 87 | BUY | STABILIZE | 76.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024741074070334435 | 0.0 | 0.0 | +60b0249f-e02f-4aca-b90d-75e9bcc822b8 / -— |
| Jogador 8 | 2-7 | 88 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 2 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 89 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 2 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 91 | CRAFT_AND_EQUIP | STABILIZE | 76.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21499629318714142 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 92 | SELL | STABILIZE | 76.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0036800000816583633 | 0.0 | 0.0 | +— / -60b0249f-e02f-4aca-b90d-75e9bcc822b8 |
| Jogador 8 | 3-1 | 93 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21759173274040222 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 94 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 95 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055550336837768555 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 96 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2266991287469864 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 97 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3678778111934662 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 98 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015429484657943249 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 99 | PASS | STABILIZE | 76.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 102 | SELL | STABILIZE | 65.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.077844999730587 | 0.0 | 0.0 | +— / -2e656a3d-eed0-40bb-a831-443d972d6588 |
| Jogador 8 | 3-2 | 103 | BUY | STABILIZE | 65.0 | 6 | 11 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26944494247436523 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 104 | BUY_XP | STABILIZE | 65.0 | 6 | 10 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 105 | BUY_XP | STABILIZE | 65.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 2 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 107 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 2 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 108 | PASS | STABILIZE | 65.0 | 6 | 2 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 112 | SELL | STABILIZE | 65.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15665242075920105 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-3 | 113 | BUY | STABILIZE | 65.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7588751316070557 | 0.0 | 0.0 | +8df39648-f588-452a-b234-32da76c43aff / -— |
| Jogador 8 | 3-3 | 114 | BUY_XP | STABILIZE | 65.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 115 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 116 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3390048146247864 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 117 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17081038653850555 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 118 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06375118345022202 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 119 | PASS | STABILIZE | 65.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 122 | SELL | STABILIZE | 55.0 | 6 | 9 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20821113884449005 | 0.0 | 0.0 | +— / -8df39648-f588-452a-b234-32da76c43aff |
| Jogador 8 | 3-4 | 123 | BUY | STABILIZE | 55.0 | 6 | 10 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08662322163581848 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 124 | MOVE_BOARD | STABILIZE | 55.0 | 6 | 7 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01140470802783966 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 125 | SELL | STABILIZE | 55.0 | 6 | 7 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08681990951299667 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 3-4 | 126 | BUY | STABILIZE | 55.0 | 6 | 10 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0349685437977314 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 127 | MOVE_BOARD | STABILIZE | 55.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 128 | MOVE_BOARD | STABILIZE | 55.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 129 | PASS | STABILIZE | 55.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 132 | SELL | STABILIZE | 55.0 | 6 | 13 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0060198549181222916 | 0.0 | 0.0 | +— / -d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 3-5 | 133 | BUY | STABILIZE | 55.0 | 6 | 15 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05397583544254303 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 134 | SELL | STABILIZE | 55.0 | 6 | 12 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006824934855103493 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 3-5 | 135 | BUY | STABILIZE | 55.0 | 6 | 15 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03845081850886345 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 136 | SELL | STABILIZE | 55.0 | 6 | 13 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006719999946653843 | 0.0 | 0.0 | +— / -9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-5 | 137 | BUY_XP | STABILIZE | 55.0 | 6 | 15 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 138 | MOVE_BOARD | STABILIZE | 55.0 | 6 | 11 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012327036820352077 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 139 | MOVE_BOARD | STABILIZE | 55.0 | 6 | 11 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03467351198196411 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 140 | MOVE_BOARD | STABILIZE | 55.0 | 6 | 11 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15485188364982605 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 142 | BUY | STABILIZE | 45.0 | 6 | 18 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28175634145736694 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 143 | SELL | STABILIZE | 45.0 | 6 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006399999838322401 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-6 | 144 | BUY | STABILIZE | 45.0 | 6 | 17 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2831423580646515 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 145 | BUY_XP | STABILIZE | 45.0 | 6 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06353499740362167 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 146 | BUY_XP | STABILIZE | 45.0 | 7 | 10 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 147 | BUY_XP | STABILIZE | 45.0 | 7 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 148 | MOVE_BENCH | STABILIZE | 45.0 | 7 | 2 | 0 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.575190544128418 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 149 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 2 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0066079553216695786 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 150 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 2 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019021784886717796 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 152 | BUY | STABILIZE | 45.0 | 7 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7516887784004211 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 153 | SELL | STABILIZE | 45.0 | 7 | 7 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2877958118915558 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 3-7 | 154 | BUY | STABILIZE | 45.0 | 7 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28364717960357666 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 155 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 5 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04760038107633591 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 156 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 5 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 157 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 5 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 158 | PASS | STABILIZE | 45.0 | 7 | 5 | 0 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 162 | CRAFT_AND_EQUIP | STABILIZE | 45.0 | 7 | 10 | 1 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23570360243320465 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 163 | CRAFT_AND_EQUIP | STABILIZE | 45.0 | 7 | 10 | 1 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23109005391597748 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 164 | SELL | STABILIZE | 45.0 | 7 | 10 | 1 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21141844987869263 | 0.0 | 0.0 | +— / -23366968-ed3f-43d0-9f24-bb7691bf5d45 |
| Jogador 8 | 4-1 | 165 | BUY | STABILIZE | 45.0 | 7 | 13 | 1 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8052000999450684 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 8 | 4-1 | 166 | SELL | STABILIZE | 45.0 | 7 | 12 | 1 | 18.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16423870623111725 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 8 | 4-1 | 167 | BUY | STABILIZE | 45.0 | 7 | 16 | 1 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379526138305664 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -01f4a73c-7202-4ee3-964e-d32370c3c547,64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 4-1 | 168 | EQUIP_FROM_INVENTORY | STABILIZE | 45.0 | 7 | 15 | 1 | 14.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14080600440502167 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 169 | MOVE_BENCH | STABILIZE | 45.0 | 7 | 15 | 1 | 14.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15463685989379883 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 170 | BUY_XP | STABILIZE | 45.0 | 7 | 15 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02246999926865101 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 172 | SELL | STABILIZE | 31.0 | 7 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2904999852180481 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 8 | 4-2 | 173 | EQUIP_FROM_INVENTORY | STABILIZE | 31.0 | 7 | 20 | 2 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09032516926527023 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 174 | EQUIP_FROM_INVENTORY | STABILIZE | 31.0 | 7 | 20 | 2 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1816600263118744 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 175 | EQUIP_FROM_INVENTORY | STABILIZE | 31.0 | 7 | 20 | 2 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.17677892744541168 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 176 | BUY | STABILIZE | 31.0 | 7 | 20 | 2 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7649672627449036 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -87600495-fe90-4832-ab42-9a5cb0ebe3f4,d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-2 | 177 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 17 | 1 | 18.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1486230343580246 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 178 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 17 | 1 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010752023197710514 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 179 | BUY | STABILIZE | 31.0 | 7 | 17 | 1 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22643296420574188 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 8 | 4-2 | 180 | BUY_XP | STABILIZE | 31.0 | 7 | 13 | 1 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 182 | BUY | STABILIZE | 31.0 | 7 | 16 | 1 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15297651290893555 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 8 | 4-3 | 183 | BUY | STABILIZE | 31.0 | 7 | 12 | 1 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0569293387234211 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 184 | BUY_XP | STABILIZE | 31.0 | 7 | 9 | 0 | 20.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 185 | BUY_XP | STABILIZE | 31.0 | 7 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 186 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 1 | 0 | 20.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.0992821090621874e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 187 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 1 | 0 | 20.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015296123921871185 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 188 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 1 | 0 | 20.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015023100189864635 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 189 | PASS | STABILIZE | 31.0 | 7 | 1 | 0 | 20.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 192 | BUY | STABILIZE | 18.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7549346089363098 | 0.0 | 0.0 | +cc9b5fff-2223-4721-a8b2-4f70e196b851 / -— |
| Jogador 8 | 4-4 | 193 | SELL | STABILIZE | 18.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14764738082885742 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 8 | 4-4 | 194 | BUY | STABILIZE | 18.0 | 7 | 13 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2817114591598511 | 0.0 | 0.0 | +167110eb-b0d0-4873-9ffe-38286dcc5ca2 / -— |
| Jogador 8 | 4-4 | 195 | MOVE_BOARD | STABILIZE | 18.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.33091698444332e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 196 | MOVE_BOARD | STABILIZE | 18.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015940915793180466 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 197 | MOVE_BOARD | STABILIZE | 18.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01397324912250042 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 198 | PASS | STABILIZE | 18.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 202 | SELL | STABILIZE | 18.0 | 7 | 16 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0010286651086062193 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 8 | 4-5 | 203 | BUY | STABILIZE | 18.0 | 7 | 19 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8374866247177124 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 4-5 | 204 | BUY | STABILIZE | 18.0 | 7 | 18 | 1 | 28.0 | Espinhos Negros/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4795059263706207 | 0.0 | 0.0 | +ac547bcb-d285-480d-b50e-3cfba572db5a / -— |
| Jogador 8 | 4-5 | 205 | BUY | STABILIZE | 18.0 | 7 | 17 | 1 | 28.0 | Espinhos Negros/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2164122462272644 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 8 | 4-5 | 206 | MOVE_BOARD | STABILIZE | 18.0 | 7 | 14 | 1 | 28.0 | Espinhos Negros/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.4027118494559545e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 207 | MOVE_BOARD | STABILIZE | 18.0 | 7 | 14 | 1 | 28.0 | Espinhos Negros/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015098783187568188 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 208 | MOVE_BOARD | STABILIZE | 18.0 | 7 | 14 | 1 | 28.0 | Espinhos Negros/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015027642250061035 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 209 | PASS | STABILIZE | 18.0 | 7 | 14 | 1 | 28.0 | Espinhos Negros/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 212 | SELL | ALL_IN | 4.0 | 7 | 21 | 2 | 28.0 | Espinhos Negros/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33224785327911377 | 0.0 | 0.0 | +— / -262702a6-b710-4129-9dc6-0c1a04514ff9 |
| Jogador 8 | 4-6 | 213 | BUY | ALL_IN | 4.0 | 7 | 24 | 2 | 28.0 | Espinhos Negros/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8257546424865723 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -— |
| Jogador 8 | 4-6 | 214 | SELL | ALL_IN | 4.0 | 7 | 21 | 2 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015239374712109566 | 0.0 | 0.0 | +— / -715d5bfc-c8c3-4dec-a247-9e07ee2755e8 |
| Jogador 8 | 4-6 | 215 | BUY | ALL_IN | 4.0 | 7 | 24 | 2 | 28.0 | Espinhos Negros/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026770688593387604 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 8 | 4-6 | 216 | BUY_XP | ALL_IN | 4.0 | 7 | 22 | 2 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 217 | BUY_XP | ALL_IN | 4.0 | 7 | 18 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 218 | BUY_XP | ALL_IN | 4.0 | 7 | 14 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 219 | BUY_XP | ALL_IN | 4.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24457499384880066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 220 | BUY_XP | ALL_IN | 4.0 | 8 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 189 | 203 | 37 | 16 | 23 | 0 | 0 | 0 | 5 | 46.0 |
- Jogador 1 — gasto por ação: BUY: 99g, BUY_XP: 104g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 7g, stage 2: 52g, stage 3: 69g, stage 4: 55g, stage 5: 20g
| Jogador 2 | 230 | 207 | 80 | 20 | 17 | 1 | 0 | 0 | 50 | 28.0 |
- Jogador 2 — gasto por ação: BUY: 127g, BUY_XP: 80g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 44g, stage 3: 63g, stage 4: 49g, stage 5: 44g
| Jogador 3 | 204 | 189 | 83 | 8 | 16 | 0 | 0 | 0 | 43 | 36.0 |
- Jogador 3 — gasto por ação: BUY: 121g, BUY_XP: 68g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 44g, stage 3: 69g, stage 4: 58g, stage 5: 11g
| Jogador 4 | 274 | 330 | 99 | 31 | 41 | 0 | 0 | 0 | 8 | 50.0 |
- Jogador 4 — gasto por ação: BUY: 158g, BUY_XP: 172g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 7g, stage 2: 52g, stage 3: 44g, stage 4: 68g, stage 5: 95g, stage 6: 64g
| Jogador 5 | 271 | 306 | 121 | 17 | 28 | 2 | 0 | 0 | 67 | 42.0 |
- Jogador 5 — gasto por ação: BUY: 178g, BUY_XP: 128g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 52g, stage 3: 58g, stage 4: 50g, stage 5: 89g, stage 6: 50g
| Jogador 6 | 242 | 287 | 67 | 17 | 39 | 1 | 0 | 0 | 3 | 44.0 |
- Jogador 6 — gasto por ação: BUY: 127g, BUY_XP: 160g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 9g, stage 2: 49g, stage 3: 48g, stage 4: 37g, stage 5: 130g, stage 6: 14g
| Jogador 7 | 161 | 167 | 42 | 6 | 20 | 1 | 0 | 0 | 47 | 24.0 |
- Jogador 7 — gasto por ação: BUY: 75g, BUY_XP: 92g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 23g, stage 3: 37g, stage 4: 101g
| Jogador 8 | 173 | 180 | 58 | 11 | 19 | 1 | 0 | 0 | 2 | 28.0 |
- Jogador 8 — gasto por ação: BUY: 92g, BUY_XP: 88g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 48g, stage 3: 59g, stage 4: 66g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 26 | 4 |
- Jogador 1 · 3-1 · step 95: PASS com 6g, HP 95, nível 6/8 (STABILIZE).
- Jogador 1 · 3-2 · step 105: PASS com 11g, HP 95, nível 6/8 (FAST8).
- Jogador 1 · 4-3 · step 187: PASS com 5g, HP 58, nível 7/8 (FAST8).
- Jogador 1 · 4-4 · step 196: PASS com 8g, HP 46, nível 7/8 (FAST8).
| Jogador 2 | 20 | 6 |
- Jogador 2 · 3-1 · step 96: PASS com 9g, HP 85, nível 6/8 (STABILIZE).
- Jogador 2 · 3-3 · step 119: PASS com 8g, HP 76, nível 6/8 (STABILIZE).
- Jogador 2 · 3-4 · step 130: PASS com 13g, HP 76, nível 6/8 (STABILIZE).
- Jogador 2 · 3-5 · step 138: PASS com 18g, HP 76, nível 6/8 (STABILIZE).
- Jogador 2 · 4-6 · step 219: PASS com 17g, HP 28, nível 7/8 (STABILIZE).
- Jogador 2 · 4-7 · step 230: PASS com 25g, HP 28, nível 7/8 (STABILIZE).
| Jogador 3 | 17 | 4 |
- Jogador 3 · 4-6 · step 218: PASS com 14g, HP 34, nível 7/8 (STABILIZE).
- Jogador 3 · 4-7 · step 230: PASS com 19g, HP 22, nível 7/8 (STABILIZE).
- Jogador 3 · 5-2 · step 249: PASS com 37g, HP 22, nível 7/8 (STABILIZE).
- Jogador 3 · 5-3 · step 259: PASS com 43g, HP 7, nível 7/8 (ALL_IN).
| Jogador 4 | 43 | 8 |
- Jogador 4 · 3-1 · step 98: PASS com 5g, HP 93, nível 6/8 (FAST8).
- Jogador 4 · 3-2 · step 109: PASS com 12g, HP 93, nível 6/8 (FAST8).
- Jogador 4 · 3-5 · step 138: PASS com 11g, HP 73, nível 6/8 (FAST8).
- Jogador 4 · 3-6 · step 146: PASS com 18g, HP 63, nível 6/8 (FAST8).
- Jogador 4 · 4-1 · step 167: PASS com 19g, HP 53, nível 7/8 (FAST8).
- Jogador 4 · 4-2 · step 176: PASS com 25g, HP 53, nível 7/8 (FAST8).
- Jogador 4 · 4-5 · step 209: PASS com 4g, HP 41, nível 7/8 (FAST8).
- Jogador 4 · 4-6 · step 219: PASS com 10g, HP 29, nível 7/8 (STABILIZE).
| Jogador 5 | 32 | 4 |
- Jogador 5 · 4-1 · step 170: PASS com 4g, HP 82, nível 7/8 (FAST8).
- Jogador 5 · 4-5 · step 206: PASS com 6g, HP 82, nível 7/8 (FAST8).
- Jogador 5 · 4-6 · step 216: PASS com 21g, HP 82, nível 7/8 (FAST8).
- Jogador 5 · 4-7 · step 227: PASS com 30g, HP 82, nível 7/8 (FAST8).
| Jogador 6 | 40 | 7 |
- Jogador 6 · 4-4 · step 200: PASS com 8g, HP 65, nível 7/8 (FAST8).
- Jogador 6 · 4-5 · step 207: PASS com 12g, HP 65, nível 7/8 (FAST8).
- Jogador 6 · 4-6 · step 216: PASS com 28g, HP 65, nível 7/8 (FAST8).
- Jogador 6 · 4-7 · step 225: PASS com 39g, HP 65, nível 7/8 (FAST8).
- Jogador 6 · 5-1 · step 238: PASS com 55g, HP 65, nível 7/8 (FAST8).
- Jogador 6 · 5-2 · step 248: PASS com 68g, HP 65, nível 7/8 (FAST8).
- Jogador 6 · 5-3 · step 257: PASS com 75g, HP 50, nível 7/8 (FAST8).
| Jogador 7 | 23 | 10 |
- Jogador 7 · 2-4 · step 56: PASS com 6g, HP 90, nível 4/8 (STABILIZE).
- Jogador 7 · 2-5 · step 65: PASS com 9g, HP 90, nível 4/8 (STABILIZE).
- Jogador 7 · 2-6 · step 79: PASS com 14g, HP 85, nível 5/8 (STABILIZE).
- Jogador 7 · 2-7 · step 88: PASS com 22g, HP 80, nível 5/8 (STABILIZE).
- Jogador 7 · 3-1 · step 98: PASS com 30g, HP 80, nível 5/8 (STABILIZE).
- Jogador 7 · 3-4 · step 128: PASS com 40g, HP 59, nível 6/8 (STABILIZE).
- Jogador 7 · 3-5 · step 137: PASS com 50g, HP 59, nível 6/8 (STABILIZE).
- Jogador 7 · 3-6 · step 147: PASS com 55g, HP 48, nível 6/8 (STABILIZE).
- Jogador 7 · 3-7 · step 160: PASS com 63g, HP 48, nível 6/8 (STABILIZE).
- Jogador 7 · 4-3 · step 185: PASS com 74g, HP 24, nível 7/8 (STABILIZE).
| Jogador 8 | 22 | 5 |
- Jogador 8 · 3-3 · step 119: PASS com 4g, HP 65, nível 6/8 (STABILIZE).
- Jogador 8 · 3-4 · step 129: PASS com 8g, HP 55, nível 6/8 (STABILIZE).
- Jogador 8 · 3-7 · step 158: PASS com 5g, HP 45, nível 7/8 (STABILIZE).
- Jogador 8 · 4-4 · step 198: PASS com 10g, HP 18, nível 7/8 (STABILIZE).
- Jogador 8 · 4-5 · step 209: PASS com 14g, HP 18, nível 7/8 (STABILIZE).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 2 | 2 | 0 | 0.0% |
| Jogador 5 | 2 | 2 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 2 | 2 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 189 | 48 | 32 | 109 | 0.0048 | 0.2001 | 0.0037 | 0.2798 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0192 (46 ações), BUY_XP: Δ 0.0053 (26 ações), CRAFT_AND_EQUIP: Δ 0.0145 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0196 (31 ações), MOVE_BOARD: Δ 0.0119 (41 ações), PASS: Δ 0.0000 (19 ações), SELL: Δ 0.0332 (14 ações)
| Jogador 2 | 230 | 55 | 49 | 126 | -0.0010 | -0.3301 | -0.0024 | 0.3371 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0068 (65 ações), BUY_XP: Δ 0.0041 (20 ações), CRAFT_AND_EQUIP: Δ 0.0289 (7 ações), EQUIP_FROM_INVENTORY: Δ -0.0019 (1 ações), MOVE_BENCH: Δ -0.0808 (16 ações), MOVE_BOARD: Δ 0.0094 (74 ações), PASS: Δ 0.0000 (13 ações), SELL: Δ 0.0155 (34 ações)
| Jogador 3 | 204 | 41 | 39 | 124 | 0.0053 | 0.3631 | 0.0032 | 0.3386 | 0.0021 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0233 (58 ações), BUY_XP: Δ 0.0017 (17 ações), CRAFT_AND_EQUIP: Δ 0.0063 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0360 (15 ações), MOVE_BOARD: Δ 0.0225 (55 ações), PASS: Δ 0.0005 (19 ações), SELL: Δ 0.0185 (31 ações)
| Jogador 4 | 274 | 66 | 63 | 145 | 0.0052 | 0.1631 | 0.0039 | 0.4058 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0388 (71 ações), BUY_XP: Δ 0.0001 (43 ações), CRAFT_AND_EQUIP: Δ -0.0066 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0544 (34 ações), MOVE_BOARD: Δ 0.0207 (64 ações), PASS: Δ 0.0000 (19 ações), SELL: Δ 0.0345 (30 ações)
| Jogador 5 | 271 | 62 | 61 | 148 | 0.0039 | 0.1650 | 0.0029 | 0.3271 | 0.0010 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0230 (75 ações), BUY_XP: Δ 0.0050 (32 ações), CRAFT_AND_EQUIP: Δ 0.1721 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (4 ações), MOVE_BENCH: Δ 0.0103 (14 ações), MOVE_BOARD: Δ 0.0064 (79 ações), PASS: Δ -0.0045 (18 ações), SELL: Δ 0.0206 (42 ações)
| Jogador 6 | 242 | 53 | 43 | 146 | 0.0047 | 0.2795 | 0.0030 | 0.3340 | 0.0017 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0362 (56 ações), BUY_XP: Δ 0.0012 (40 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0108 (45 ações), MOVE_BOARD: Δ 0.0392 (49 ações), PASS: Δ 0.0000 (18 ações), SELL: Δ 0.0339 (21 ações)
| Jogador 7 | 161 | 44 | 33 | 84 | 0.0034 | 0.2132 | 0.0017 | 0.2055 | 0.0017 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0277 (40 ações), BUY_XP: Δ 0.0049 (23 ações), CRAFT_AND_EQUIP: Δ 0.0157 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0065 (3 ações), MOVE_BENCH: Δ 0.0294 (32 ações), MOVE_BOARD: Δ -0.0007 (27 ações), PASS: Δ 0.0009 (14 ações), SELL: Δ 0.0304 (17 ações)
| Jogador 8 | 173 | 42 | 39 | 92 | 0.0035 | -0.2023 | 0.0002 | 0.2907 | 0.0034 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0179 (47 ações), BUY_XP: Δ 0.0052 (22 ações), CRAFT_AND_EQUIP: Δ 0.0000 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0275 (4 ações), MOVE_BENCH: Δ 0.0203 (14 ações), MOVE_BOARD: Δ 0.0050 (45 ações), PASS: Δ 0.0000 (14 ações), SELL: Δ 0.0327 (22 ações)
- Jogador 1 — rounds avaliados: 28; correlação estrutural/combate: -0.326; posicional/combate: -0.290.
- Jogador 1 — combate positive: score estrutural prévio 0.162
  score posicional prévio 0.263
- Jogador 1 — combate negative: score estrutural prévio 0.387
  score posicional prévio 0.313
- Jogador 2 — rounds avaliados: 30; correlação estrutural/combate: 0.204; posicional/combate: 0.199.
- Jogador 2 — combate positive: score estrutural prévio -0.241
  score posicional prévio 0.346
- Jogador 2 — combate negative: score estrutural prévio -0.388
  score posicional prévio 0.300
- Jogador 3 — rounds avaliados: 28; correlação estrutural/combate: -0.038; posicional/combate: -0.157.
- Jogador 3 — combate positive: score estrutural prévio 0.401
  score posicional prévio 0.339
- Jogador 3 — combate negative: score estrutural prévio 0.414
  score posicional prévio 0.375
- Jogador 4 — rounds avaliados: 37; correlação estrutural/combate: 0.340; posicional/combate: 0.130.
- Jogador 4 — combate positive: score estrutural prévio 0.272
  score posicional prévio 0.424
- Jogador 4 — combate negative: score estrutural prévio -0.067
  score posicional prévio 0.404
- Jogador 5 — rounds avaliados: 37; correlação estrutural/combate: -0.173; posicional/combate: 0.114.
- Jogador 5 — combate positive: score estrutural prévio 0.092
  score posicional prévio 0.324
- Jogador 5 — combate negative: score estrutural prévio 0.321
  score posicional prévio 0.298
- Jogador 6 — rounds avaliados: 34; correlação estrutural/combate: 0.038; posicional/combate: 0.193.
- Jogador 6 — combate positive: score estrutural prévio 0.337
  score posicional prévio 0.358
- Jogador 6 — combate negative: score estrutural prévio 0.309
  score posicional prévio 0.319
- Jogador 7 — rounds avaliados: 24; correlação estrutural/combate: -0.001; posicional/combate: 0.069.
- Jogador 7 — combate positive: score estrutural prévio 0.332
  score posicional prévio 0.207
- Jogador 7 — combate negative: score estrutural prévio 0.255
  score posicional prévio 0.202
- Jogador 8 — rounds avaliados: 24; correlação estrutural/combate: -0.116; posicional/combate: -0.086.
- Jogador 8 — combate positive: score estrutural prévio -0.255
  score posicional prévio 0.279
- Jogador 8 — combate negative: score estrutural prévio -0.158
  score posicional prévio 0.295

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 216 | OK (216) | 5 | 2 | 0 | 0 | 7 | 3 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_Crownguard, TFT_Item_JeweledGauntlet, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 259 | OK (259) | 7 | 0 | 0 | 0 | 7 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_BrambleVest, TFT_Item_GargoyleStoneplate, TFT_Item_GuinsoosRageblade, TFT_Item_LastWhisper, TFT_Item_Quicksilver, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 231 | OK (231) | 7 | 0 | 0 | 0 | 7 | 2 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 311 | OK (311) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_BlueBuff, TFT_Item_JeweledGauntlet, TFT_Item_PowerGauntlet, TFT_Item_Quicksilver, TFT_Item_Redemption, TFT_Item_RunaansHurricane, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 307 | OK (307) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 5 — IDs equipados observados: TFT_Item_GargoyleStoneplate, TFT_Item_GuinsoosRageblade, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_MadredsBloodrazor, TFT_Item_Morellonomicon, TFT_Item_NightHarvester, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 275 | OK (275) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 6 — IDs equipados observados: DA_18_EmblemSpellweaver, TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_Crownguard, TFT_Item_HextechGunblade, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 184 | OK (184) | 5 | 0 | 0 | 1 | 5 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_NightHarvester, TFT_Item_RabadonsDeathcap, TFT_Item_SpectralGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 196 | OK (196) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 8 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_LastWhisper, TFT_Item_Redemption; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.003 | 0.000 |
| Jogador 1 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.063 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 3 | 3 → 3 | 0.006 | 0.000 |
| Jogador 1 | 1-4 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.011 | 0.000 |
| Jogador 1 | 2-1 | 9 | 2.000 | 2.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 2 | 4 → 4 | -0.017 | -0.269 |
| Jogador 1 | 2-2 | 9 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 14% → 14% | 8 → 7 | 11 | 4 → 4 | 0.012 | 0.264 |
| Jogador 1 | 2-3 | 2 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 14% → 14% | 7 → 12 | 2 | 4 → 5 | 0.015 | 1.281 |
| Jogador 1 | 2-4 | 9 | 2.000 | 10.000 | 0 → 0 | 3 → 4 | 14% → 18% | 12 → 8 | 10 | 5 → 5 | -0.027 | 0.000 |
| Jogador 1 | 2-5 | 11 | 0.000 | 6.000 | 0 → 0 | 4 → 5 | 18% → 18% | 8 → 8 | 9 | 5 → 5 | 0.028 | 0.224 |
| Jogador 1 | 2-6 | 10 | 8.000 | 0.000 | 0 → 0 | 5 → 4 | 18% → 18% | 8 → 10 | 7 | 5 → 5 | -0.011 | 0.275 |
| Jogador 1 | 2-7 | 9 | 6.000 | -6.000 | 0 → 0 | 4 → 3 | 18% → 21% | 10 → 8 | 11 | 5 → 6 | 0.039 | 0.000 |
| Jogador 1 | 3-1 | 6 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 14 | 2 | 6 → 6 | -0.065 | 0.475 |
| Jogador 1 | 3-2 | 5 | 2.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 14 → 21 | 3 | 6 → 6 | 0.002 | 0.562 |
| Jogador 1 | 3-3 | 10 | 0.000 | 2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 21 → 14 | 19 | 6 → 6 | -0.050 | 0.285 |
| Jogador 1 | 3-4 | 10 | 4.000 | -4.000 | 0 → 0 | 4 → 4 | 21% → 25% | 14 → 10 | 14 | 6 → 7 | 0.016 | 0.000 |
| Jogador 1 | 3-5 | 9 | 6.000 | -6.000 | 0 → 1 | 4 → 3 | 25% → 25% | 10 → 9 | 10 | 7 → 7 | 0.009 | 0.312 |
| Jogador 1 | 3-6 | 6 | 0.000 | 12.000 | 1 → 1 | 3 → 3 | 25% → 25% | 9 → 8 | 6 | 7 → 7 | -0.007 | -0.454 |
| Jogador 1 | 3-7 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 25% → 25% | 8 → 6 | 15 | 7 → 7 | 0.015 | 0.000 |
| Jogador 1 | 4-1 | 10 | -4.000 | -4.000 | 1 → 1 | 4 → 3 | 25% → 25% | 6 → 9 | 7 | 7 → 7 | 0.092 | -0.275 |
| Jogador 1 | 4-2 | 7 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 9 → 6 | 9 | 7 → 7 | -0.000 | -0.393 |
| Jogador 1 | 4-3 | 7 | 0.000 | 0.000 | 1 → 1 | 3 → 2 | 25% → 25% | 6 → 11 | 1 | 7 → 7 | -0.043 | -0.402 |
| Jogador 1 | 4-4 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 11 → 14 | 3 | 7 → 7 | -0.053 | 0.000 |
| Jogador 1 | 4-5 | 7 | 4.000 | 2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 14 → 10 | 11 | 7 → 7 | -0.063 | -0.407 |
| Jogador 1 | 4-6 | 10 | 2.000 | -10.000 | 1 → 1 | 3 → 4 | 25% → 29% | 10 → 21 | 6 | 7 → 8 | 0.022 | -0.270 |
| Jogador 1 | 4-7 | 9 | 2.000 | -2.000 | 1 → 1 | 4 → 3 | 29% → 29% | 21 → 11 | 18 | 8 → 8 | 0.016 | 0.000 |
| Jogador 1 | 5-1 | 10 | 6.000 | 0.000 | 1 → 2 | 3 → 3 | 29% → 29% | 11 → 9 | 10 | 8 → 8 | 0.028 | -0.275 |
| Jogador 1 | 5-2 | 8 | 0.000 | 12.000 | 2 → 2 | 3 → 2 | 29% → 29% | 9 → 6 | 9 | 8 → 8 | -0.031 | 0.369 |
| Jogador 1 | 5-3 | 5 | -46.000 | -54.000 | 2 → 0 | 2 → 0 | 29% → 0% | 6 → 5 | 1 | 8 → 8 | -0.113 | -0.550 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 52 ações e piorou em 37.
- Jogador 1 — estado final: ouro 5, nível 8, vida 4.0, colocação 6.
| Jogador 2 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.096 | 0.000 |
| Jogador 2 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.085 | 0.000 |
| Jogador 2 | 1-3 | 6 | 2.000 | 0.000 | 0 → 1 | 1 → 0 | 7% → 7% | 3 → 4 | 2 | 3 → 3 | 0.069 | 0.000 |
| Jogador 2 | 1-4 | 10 | 2.000 | 6.000 | 1 → 1 | 0 → 1 | 7% → 11% | 4 → 4 | 4 | 3 → 4 | 0.098 | 0.000 |
| Jogador 2 | 2-1 | 9 | 2.000 | 6.000 | 1 → 1 | 1 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.099 | 0.270 |
| Jogador 2 | 2-2 | 9 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 14% → 14% | 6 → 7 | 4 | 4 → 4 | 0.018 | -0.251 |
| Jogador 2 | 2-3 | 2 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 14% → 14% | 7 → 12 | 1 | 4 → 4 | -0.001 | -1.211 |
| Jogador 2 | 2-4 | 9 | 2.000 | 2.000 | 1 → 1 | 2 → 2 | 14% → 18% | 12 → 7 | 12 | 4 → 5 | -0.021 | 0.000 |
| Jogador 2 | 2-5 | 8 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 8 | 8 | 5 → 5 | -0.039 | -0.316 |
| Jogador 2 | 2-6 | 10 | 4.000 | -4.000 | 1 → 1 | 2 → 3 | 18% → 21% | 8 → 6 | 11 | 5 → 6 | 0.033 | 0.254 |
| Jogador 2 | 2-7 | 9 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.058 | 0.000 |
| Jogador 2 | 3-1 | 7 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 8 → 17 | 1 | 6 → 6 | -0.019 | 0.409 |
| Jogador 2 | 3-2 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 3 | 21% → 21% | 17 → 14 | 10 | 6 → 6 | 0.019 | -0.259 |
| Jogador 2 | 3-3 | 9 | 2.000 | 6.000 | 1 → 1 | 3 → 2 | 21% → 21% | 14 → 14 | 7 | 6 → 6 | -0.019 | 0.302 |
| Jogador 2 | 3-4 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 14 → 19 | 8 | 6 → 6 | 0.010 | 0.000 |
| Jogador 2 | 3-5 | 8 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 19 → 26 | 4 | 6 → 6 | -0.056 | 0.345 |
| Jogador 2 | 3-6 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 26 → 17 | 18 | 6 → 7 | 0.011 | -0.268 |
| Jogador 2 | 3-7 | 10 | 4.000 | 0.000 | 1 → 1 | 2 → 5 | 21% → 25% | 17 → 13 | 15 | 7 → 7 | -0.009 | 0.000 |
| Jogador 2 | 4-1 | 10 | 0.000 | 2.000 | 1 → 1 | 5 → 4 | 25% → 25% | 13 → 6 | 14 | 7 → 7 | 0.033 | -0.275 |
| Jogador 2 | 4-2 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 6 → 8 | 7 | 7 → 7 | 0.011 | -0.281 |
| Jogador 2 | 4-3 | 8 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 8 → 9 | 7 | 7 → 7 | -0.096 | -0.346 |
| Jogador 2 | 4-4 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 9 → 7 | 11 | 7 → 7 | 0.035 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 7 → 11 | 5 | 7 → 7 | 0.061 | 0.301 |
| Jogador 2 | 4-6 | 9 | 0.000 | -8.000 | 1 → 1 | 4 → 5 | 25% → 25% | 11 → 25 | 3 | 7 → 7 | -0.092 | 0.317 |
| Jogador 2 | 4-7 | 10 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 25% → 25% | 25 → 33 | 2 | 7 → 8 | -0.011 | 0.000 |
| Jogador 2 | 5-1 | 10 | 6.000 | 10.000 | 1 → 1 | 5 → 4 | 25% → 29% | 33 → 32 | 10 | 8 → 8 | -0.008 | -0.270 |
| Jogador 2 | 5-2 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 29% → 29% | 32 → 40 | 8 | 8 → 8 | 0.082 | 0.301 |
| Jogador 2 | 5-3 | 10 | 0.000 | 6.000 | 1 → 1 | 4 → 3 | 29% → 29% | 40 → 45 | 9 | 8 → 8 | 0.035 | 0.302 |
| Jogador 2 | 5-4 | 10 | 0.000 | 4.000 | 1 → 1 | 3 → 2 | 29% → 29% | 45 → 53 | 7 | 8 → 8 | -0.050 | 0.000 |
| Jogador 2 | 5-5 | 9 | -28.000 | -52.000 | 1 → 0 | 2 → 0 | 29% → 0% | 53 → 50 | 10 | 8 → 8 | -0.018 | -0.317 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 20, COMPOSITION_COMPATIBILITY: 21, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 59 ações e piorou em 49.
- Jogador 2 — estado final: ouro 50, nível 8, vida 15.0, colocação 4.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.007 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.058 | 0.000 |
| Jogador 3 | 1-3 | 4 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.078 | 0.000 |
| Jogador 3 | 1-4 | 7 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.067 | 0.000 |
| Jogador 3 | 2-1 | 9 | 2.000 | 6.000 | 1 → 1 | 0 → 1 | 11% → 14% | 4 → 5 | 4 | 4 → 4 | -0.032 | -0.257 |
| Jogador 3 | 2-2 | 9 | 4.000 | 0.000 | 1 → 0 | 1 → 1 | 14% → 14% | 5 → 6 | 9 | 4 → 4 | 0.025 | 0.299 |
| Jogador 3 | 2-3 | 2 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 6 → 12 | 1 | 4 → 5 | 0.016 | 1.256 |
| Jogador 3 | 2-4 | 9 | 8.000 | -2.000 | 0 → 0 | 1 → 0 | 14% → 18% | 12 → 10 | 8 | 5 → 5 | -0.018 | 0.000 |
| Jogador 3 | 2-5 | 8 | 0.000 | 6.000 | 0 → 0 | 0 → 2 | 18% → 18% | 10 → 10 | 7 | 5 → 5 | 0.051 | 0.338 |
| Jogador 3 | 2-6 | 10 | 0.000 | 6.000 | 0 → 0 | 2 → 0 | 18% → 18% | 10 → 5 | 10 | 5 → 5 | 0.010 | -0.238 |
| Jogador 3 | 2-7 | 8 | 0.000 | 10.000 | 0 → 0 | 0 → 2 | 18% → 18% | 5 → 5 | 5 | 5 → 6 | -0.029 | 0.000 |
| Jogador 3 | 3-1 | 11 | 2.000 | -4.000 | 0 → 0 | 2 → 2 | 18% → 21% | 5 → 6 | 13 | 6 → 6 | -0.001 | -0.256 |
| Jogador 3 | 3-2 | 10 | 4.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 6 → 7 | 9 | 6 → 6 | 0.009 | -0.263 |
| Jogador 3 | 3-3 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 7 | 9 | 6 → 6 | 0.038 | -0.273 |
| Jogador 3 | 3-4 | 10 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 21% → 21% | 7 → 6 | 10 | 6 → 6 | 0.002 | 0.000 |
| Jogador 3 | 3-5 | 10 | 0.000 | 0.000 | 0 → 0 | 3 → 1 | 21% → 21% | 6 → 7 | 14 | 6 → 6 | -0.094 | 0.290 |
| Jogador 3 | 3-6 | 10 | 8.000 | -2.000 | 0 → 0 | 1 → 2 | 21% → 25% | 7 → 5 | 8 | 6 → 7 | 0.018 | -0.266 |
| Jogador 3 | 3-7 | 8 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 25% → 25% | 5 → 8 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 10 | 0.000 | 0.000 | 0 → 0 | 3 → 4 | 25% → 25% | 8 → 6 | 11 | 7 → 7 | 0.095 | 0.291 |
| Jogador 3 | 4-2 | 7 | 0.000 | 2.000 | 0 → 0 | 4 → 3 | 25% → 25% | 6 → 8 | 8 | 7 → 7 | -0.144 | 0.412 |
| Jogador 3 | 4-3 | 8 | 0.000 | -2.000 | 0 → 0 | 3 → 3 | 25% → 25% | 8 → 6 | 11 | 7 → 7 | -0.001 | -0.328 |
| Jogador 3 | 4-4 | 7 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 7 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 9 | 0.000 | 4.000 | 0 → 0 | 3 → 2 | 25% → 25% | 7 → 8 | 8 | 7 → 7 | 0.104 | 0.320 |
| Jogador 3 | 4-6 | 8 | 0.000 | -8.000 | 0 → 0 | 2 → 3 | 25% → 25% | 8 → 20 | 4 | 7 → 7 | -0.005 | -0.339 |
| Jogador 3 | 4-7 | 10 | 0.000 | 2.000 | 0 → 0 | 3 → 2 | 25% → 25% | 20 → 25 | 9 | 7 → 7 | -0.000 | 0.000 |
| Jogador 3 | 5-1 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 25 → 36 | 3 | 7 → 7 | -0.017 | 0.292 |
| Jogador 3 | 5-2 | 9 | 0.000 | -2.000 | 0 → 0 | 2 → 3 | 25% → 25% | 36 → 45 | 3 | 7 → 7 | -0.002 | -0.317 |
| Jogador 3 | 5-3 | 9 | -36.000 | -32.000 | 0 → 0 | 3 → 0 | 25% → 0% | 45 → 43 | 5 | 7 → 7 | -0.113 | -0.317 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 13, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 46 ações e piorou em 40.
- Jogador 3 — estado final: ouro 43, nível 7, vida 7.0, colocação 5.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.007 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 4 | 1-4 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.008 | 0.000 |
| Jogador 4 | 2-1 | 9 | 2.000 | 4.000 | 0 → 0 | 2 → 4 | 11% → 14% | 4 → 7 | 3 | 4 → 4 | -0.010 | 0.285 |
| Jogador 4 | 2-2 | 9 | 0.000 | 6.000 | 0 → 0 | 4 → 5 | 14% → 14% | 7 → 7 | 10 | 4 → 4 | -0.002 | 0.285 |
| Jogador 4 | 2-3 | 2 | 0.000 | 0.000 | 0 → 0 | 5 → 4 | 14% → 14% | 7 → 13 | 1 | 4 → 5 | -0.222 | 1.231 |
| Jogador 4 | 2-4 | 9 | 6.000 | 6.000 | 0 → 0 | 4 → 5 | 14% → 18% | 13 → 13 | 6 | 5 → 5 | 0.064 | 0.000 |
| Jogador 4 | 2-5 | 11 | 0.000 | 8.000 | 0 → 0 | 5 → 4 | 18% → 18% | 13 → 8 | 16 | 5 → 5 | -0.003 | 0.233 |
| Jogador 4 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 18% → 18% | 8 → 8 | 10 | 5 → 5 | 0.038 | -0.259 |
| Jogador 4 | 2-7 | 9 | 10.000 | -6.000 | 0 → 0 | 4 → 2 | 18% → 18% | 8 → 9 | 6 | 5 → 6 | -0.008 | 0.000 |
| Jogador 4 | 3-1 | 9 | 2.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 21% | 9 → 11 | 4 | 6 → 6 | -0.033 | 0.332 |
| Jogador 4 | 3-2 | 9 | 4.000 | -6.000 | 0 → 0 | 2 → 1 | 21% → 21% | 11 → 18 | 2 | 6 → 6 | -0.062 | -0.314 |
| Jogador 4 | 3-3 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 18 → 7 | 17 | 6 → 6 | -0.017 | -0.254 |
| Jogador 4 | 3-4 | 10 | -4.000 | 2.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 15 | 4 | 6 → 6 | 0.017 | 0.000 |
| Jogador 4 | 3-5 | 8 | 4.000 | 4.000 | 0 → 0 | 2 → 3 | 21% → 21% | 15 → 18 | 4 | 6 → 6 | -0.013 | -0.329 |
| Jogador 4 | 3-6 | 6 | -4.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 18 → 25 | 0 | 6 → 6 | -0.034 | -0.439 |
| Jogador 4 | 3-7 | 10 | 8.000 | -8.000 | 0 → 0 | 3 → 2 | 21% → 25% | 25 → 22 | 13 | 6 → 7 | 0.075 | 0.000 |
| Jogador 4 | 4-1 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 25% → 25% | 22 → 27 | 3 | 7 → 7 | -0.005 | 0.414 |
| Jogador 4 | 4-2 | 6 | 4.000 | -4.000 | 0 → 1 | 3 → 2 | 25% → 25% | 27 → 32 | 2 | 7 → 7 | 0.043 | -0.452 |
| Jogador 4 | 4-3 | 10 | 0.000 | 10.000 | 1 → 1 | 2 → 3 | 25% → 25% | 32 → 18 | 21 | 7 → 7 | 0.044 | 0.298 |
| Jogador 4 | 4-4 | 10 | 0.000 | -8.000 | 1 → 1 | 3 → 4 | 25% → 25% | 18 → 18 | 14 | 7 → 7 | 0.005 | 0.000 |
| Jogador 4 | 4-5 | 9 | 0.000 | 4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 18 → 9 | 16 | 7 → 7 | -0.008 | -0.302 |
| Jogador 4 | 4-6 | 9 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 9 → 17 | 5 | 7 → 7 | -0.022 | 0.332 |
| Jogador 4 | 4-7 | 10 | -2.000 | 4.000 | 1 → 1 | 4 → 3 | 25% → 25% | 17 → 19 | 7 | 7 → 8 | -0.041 | 0.000 |
| Jogador 4 | 5-1 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 2 | 25% → 25% | 19 → 21 | 14 | 8 → 8 | 0.000 | 0.286 |
| Jogador 4 | 5-2 | 7 | 6.000 | 10.000 | 1 → 1 | 2 → 2 | 25% → 29% | 21 → 21 | 8 | 8 → 8 | 0.016 | 0.448 |
| Jogador 4 | 5-3 | 7 | 0.000 | -10.000 | 1 → 1 | 2 → 2 | 29% → 29% | 21 → 37 | 1 | 8 → 8 | 0.028 | 0.415 |
| Jogador 4 | 5-4 | 10 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 29% → 29% | 37 → 20 | 26 | 8 → 8 | -0.000 | 0.000 |
| Jogador 4 | 5-5 | 8 | 6.000 | 2.000 | 1 → 1 | 2 → 3 | 29% → 29% | 20 → 25 | 8 | 8 → 8 | 0.008 | 0.361 |
| Jogador 4 | 5-6 | 9 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 29% → 29% | 25 → 34 | 6 | 8 → 8 | 0.038 | 0.325 |
| Jogador 4 | 5-7 | 10 | 0.000 | 16.000 | 1 → 1 | 3 → 5 | 29% → 29% | 34 → 10 | 32 | 8 → 8 | -0.101 | 0.000 |
| Jogador 4 | 6-1 | 10 | 2.000 | -12.000 | 1 → 1 | 5 → 4 | 29% → 32% | 10 → 9 | 17 | 8 → 9 | -0.014 | 0.000 |
| Jogador 4 | 6-2 | 7 | 0.000 | 16.000 | 1 → 1 | 4 → 4 | 32% → 32% | 9 → 10 | 8 | 9 → 9 | 0.026 | 0.419 |
| Jogador 4 | 6-3 | 10 | 0.000 | -12.000 | 1 → 1 | 4 → 4 | 32% → 32% | 10 → 12 | 20 | 9 → 9 | 0.040 | 0.302 |
| Jogador 4 | 6-4 | 9 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 32% → 32% | 12 → 8 | 12 | 9 → 9 | 0.070 | 0.000 |
| Jogador 4 | 6-5 | 9 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 32% → 32% | 8 → 9 | 7 | 9 → 9 | 0.016 | 0.346 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 18; mudanças de composição: 1; posicionamento melhorou em 70 ações e piorou em 65.
- Jogador 4 — estado final: ouro 9, nível 9, vida 29.0, colocação 1.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.006 | 0.000 |
| Jogador 5 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 5 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.021 | 0.000 |
| Jogador 5 | 1-4 | 9 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.039 | 0.000 |
| Jogador 5 | 2-1 | 9 | 2.000 | -2.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 9 | 4 | 4 → 4 | -0.003 | -0.257 |
| Jogador 5 | 2-2 | 9 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 7 | 9 | 4 → 4 | -0.048 | 0.279 |
| Jogador 5 | 2-3 | 2 | 4.000 | -4.000 | 0 → 0 | 1 → 0 | 14% → 14% | 7 → 11 | 1 | 4 → 5 | -0.106 | -1.186 |
| Jogador 5 | 2-4 | 9 | 6.000 | 6.000 | 0 → 0 | 0 → 0 | 14% → 18% | 11 → 6 | 10 | 5 → 5 | -0.012 | 0.000 |
| Jogador 5 | 2-5 | 11 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 6 | 9 | 5 → 5 | 0.038 | 0.244 |
| Jogador 5 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 18% → 18% | 6 → 7 | 9 | 5 → 5 | -0.084 | 0.251 |
| Jogador 5 | 2-7 | 9 | 6.000 | -8.000 | 0 → 0 | 1 → 3 | 18% → 21% | 7 → 6 | 10 | 5 → 6 | -0.008 | 0.000 |
| Jogador 5 | 3-1 | 11 | 0.000 | 10.000 | 0 → 0 | 3 → 4 | 21% → 21% | 6 → 8 | 5 | 6 → 6 | 0.086 | 0.273 |
| Jogador 5 | 3-2 | 10 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 8 → 11 | 9 | 6 → 6 | -0.043 | 0.300 |
| Jogador 5 | 3-3 | 10 | 0.000 | 6.000 | 0 → 0 | 4 → 5 | 21% → 21% | 11 → 8 | 15 | 6 → 6 | -0.006 | 0.290 |
| Jogador 5 | 3-4 | 10 | 0.000 | 2.000 | 0 → 0 | 5 → 4 | 21% → 21% | 8 → 9 | 8 | 6 → 6 | 0.057 | 0.000 |
| Jogador 5 | 3-5 | 10 | 4.000 | -2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 9 → 5 | 12 | 6 → 7 | -0.044 | -0.254 |
| Jogador 5 | 3-6 | 7 | 2.000 | 0.000 | 0 → 0 | 4 → 3 | 21% → 25% | 5 → 7 | 4 | 7 → 7 | -0.063 | 0.414 |
| Jogador 5 | 3-7 | 6 | 0.000 | 10.000 | 0 → 0 | 3 → 4 | 25% → 25% | 7 → 7 | 5 | 7 → 7 | -0.063 | 0.000 |
| Jogador 5 | 4-1 | 10 | 0.000 | 8.000 | 0 → 0 | 4 → 4 | 25% → 25% | 7 → 11 | 6 | 7 → 7 | 0.111 | 0.314 |
| Jogador 5 | 4-2 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 11 → 9 | 18 | 7 → 7 | 0.019 | 0.298 |
| Jogador 5 | 4-3 | 10 | 6.000 | -10.000 | 0 → 1 | 4 → 4 | 25% → 25% | 9 → 7 | 14 | 7 → 7 | 0.033 | 0.280 |
| Jogador 5 | 4-4 | 6 | 0.000 | 4.000 | 1 → 1 | 4 → 3 | 25% → 25% | 7 → 8 | 5 | 7 → 7 | -0.077 | 0.000 |
| Jogador 5 | 4-5 | 6 | 0.000 | 4.000 | 1 → 1 | 3 → 3 | 25% → 25% | 8 → 14 | 2 | 7 → 7 | 0.090 | 0.481 |
| Jogador 5 | 4-6 | 6 | 0.000 | -10.000 | 1 → 1 | 3 → 4 | 25% → 25% | 14 → 32 | 1 | 7 → 7 | -0.104 | 0.481 |
| Jogador 5 | 4-7 | 7 | 0.000 | 4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 32 → 41 | 4 | 7 → 7 | 0.012 | 0.000 |
| Jogador 5 | 5-1 | 10 | -6.000 | 6.000 | 1 → 1 | 4 → 3 | 25% → 21% | 41 → 33 | 19 | 7 → 8 | -0.002 | -0.285 |
| Jogador 5 | 5-2 | 10 | 2.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 25% | 33 → 31 | 18 | 8 → 8 | -0.008 | -0.295 |
| Jogador 5 | 5-3 | 10 | 14.000 | -12.000 | 1 → 1 | 3 → 3 | 25% → 29% | 31 → 34 | 11 | 8 → 8 | 0.061 | -0.275 |
| Jogador 5 | 5-4 | 5 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 29% → 29% | 34 → 40 | 3 | 8 → 8 | -0.018 | 0.000 |
| Jogador 5 | 5-5 | 9 | 0.000 | 14.000 | 1 → 1 | 4 → 4 | 29% → 29% | 40 → 42 | 9 | 8 → 8 | 0.010 | 0.334 |
| Jogador 5 | 5-6 | 7 | 0.000 | 0.000 | 1 → 1 | 4 → 3 | 29% → 29% | 42 → 51 | 3 | 8 → 8 | 0.054 | 0.000 |
| Jogador 5 | 5-7 | 10 | -8.000 | 6.000 | 1 → 1 | 3 → 2 | 29% → 25% | 51 → 35 | 26 | 8 → 8 | -0.002 | 0.000 |
| Jogador 5 | 6-1 | 10 | 10.000 | -18.000 | 1 → 1 | 2 → 5 | 25% → 29% | 35 → 53 | 9 | 8 → 8 | -0.045 | 0.305 |
| Jogador 5 | 6-2 | 5 | 0.000 | 6.000 | 1 → 1 | 5 → 5 | 29% → 29% | 53 → 61 | 3 | 8 → 8 | 0.006 | 0.000 |
| Jogador 5 | 6-3 | 9 | 0.000 | 4.000 | 1 → 1 | 5 → 5 | 29% → 29% | 61 → 69 | 8 | 8 → 8 | 0.008 | -0.317 |
| Jogador 5 | 6-4 | 10 | 0.000 | 4.000 | 1 → 1 | 5 → 5 | 29% → 29% | 69 → 77 | 9 | 8 → 8 | 0.012 | 0.000 |
| Jogador 5 | 6-5 | 10 | -48.000 | -58.000 | 1 → 0 | 5 → 0 | 29% → 0% | 77 → 67 | 21 | 8 → 9 | -0.113 | -0.290 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 19, COMPOSITION_COMPATIBILITY: 28, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 19; mudanças de composição: 1; posicionamento melhorou em 64 ações e piorou em 66.
- Jogador 5 — estado final: ouro 67, nível 9, vida 19.0, colocação 2.
| Jogador 6 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.098 | 0.000 |
| Jogador 6 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.017 | 0.000 |
| Jogador 6 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 4 | 3 → 3 | 0.026 | 0.000 |
| Jogador 6 | 1-4 | 9 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.104 | 0.000 |
| Jogador 6 | 2-1 | 9 | 2.000 | 6.000 | 0 → 0 | 2 → 3 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.056 | 0.270 |
| Jogador 6 | 2-2 | 9 | 0.000 | -6.000 | 0 → 0 | 3 → 3 | 14% → 14% | 6 → 10 | 9 | 4 → 4 | 0.007 | -0.269 |
| Jogador 6 | 2-3 | 2 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 14% → 14% | 10 → 14 | 2 | 4 → 5 | -0.018 | -1.130 |
| Jogador 6 | 2-4 | 9 | 4.000 | -2.000 | 0 → 0 | 3 → 3 | 14% → 18% | 14 → 7 | 14 | 5 → 5 | 0.026 | 0.000 |
| Jogador 6 | 2-5 | 11 | 0.000 | 2.000 | 0 → 0 | 3 → 2 | 18% → 14% | 7 → 8 | 8 | 5 → 6 | -0.020 | -0.211 |
| Jogador 6 | 2-6 | 9 | 6.000 | 6.000 | 0 → 0 | 2 → 3 | 14% → 21% | 8 → 8 | 6 | 6 → 6 | -0.003 | 0.295 |
| Jogador 6 | 2-7 | 8 | 0.000 | 12.000 | 0 → 0 | 3 → 5 | 21% → 21% | 8 → 7 | 6 | 6 → 6 | 0.068 | 0.000 |
| Jogador 6 | 3-1 | 8 | 0.000 | 8.000 | 0 → 0 | 5 → 4 | 21% → 21% | 7 → 8 | 5 | 6 → 6 | 0.068 | -0.335 |
| Jogador 6 | 3-2 | 10 | 2.000 | -4.000 | 0 → 0 | 4 → 2 | 21% → 18% | 8 → 10 | 9 | 6 → 6 | -0.100 | 0.281 |
| Jogador 6 | 3-3 | 10 | 4.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 21% | 10 → 5 | 13 | 6 → 6 | 0.079 | -0.268 |
| Jogador 6 | 3-4 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 1 | 21% → 21% | 5 → 7 | 3 | 6 → 6 | 0.010 | 0.000 |
| Jogador 6 | 3-5 | 9 | 8.000 | -4.000 | 0 → 1 | 1 → 2 | 21% → 21% | 7 → 7 | 6 | 6 → 6 | -0.025 | 0.302 |
| Jogador 6 | 3-6 | 7 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 7 | 7 | 6 → 7 | 0.053 | 0.405 |
| Jogador 6 | 3-7 | 9 | 10.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 25% | 7 → 8 | 5 | 7 → 7 | 0.007 | 0.000 |
| Jogador 6 | 4-1 | 10 | 2.000 | 2.000 | 1 → 1 | 2 → 3 | 25% → 25% | 8 → 9 | 7 | 7 → 7 | -0.057 | 0.291 |
| Jogador 6 | 4-2 | 8 | 0.000 | 4.000 | 1 → 1 | 3 → 2 | 25% → 25% | 9 → 8 | 9 | 7 → 7 | -0.005 | 0.358 |
| Jogador 6 | 4-3 | 6 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 8 | 8 | 7 → 7 | -0.000 | 0.489 |
| Jogador 6 | 4-4 | 10 | 0.000 | -10.000 | 1 → 1 | 2 → 1 | 25% → 25% | 8 → 15 | 8 | 7 → 7 | 0.001 | 0.000 |
| Jogador 6 | 4-5 | 7 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 15 → 22 | 3 | 7 → 7 | -0.007 | 0.426 |
| Jogador 6 | 4-6 | 6 | 0.000 | -8.000 | 1 → 1 | 1 → 2 | 25% → 25% | 22 → 39 | 2 | 7 → 7 | 0.010 | 0.477 |
| Jogador 6 | 4-7 | 5 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 39 → 50 | 0 | 7 → 7 | 0.002 | 0.000 |
| Jogador 6 | 5-1 | 8 | 0.000 | -6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 50 → 69 | 3 | 7 → 7 | 0.008 | 0.376 |
| Jogador 6 | 5-2 | 8 | -4.000 | 2.000 | 1 → 1 | 3 → 2 | 25% → 21% | 69 → 78 | 2 | 7 → 7 | -0.025 | -0.350 |
| Jogador 6 | 5-3 | 7 | 4.000 | -4.000 | 1 → 1 | 2 → 1 | 21% → 25% | 78 → 86 | 3 | 7 → 7 | 0.080 | 0.415 |
| Jogador 6 | 5-4 | 10 | 4.000 | 4.000 | 1 → 1 | 1 → 2 | 25% → 25% | 86 → 68 | 28 | 7 → 8 | -0.065 | 0.000 |
| Jogador 6 | 5-5 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 68 → 41 | 35 | 8 → 8 | 0.000 | -0.273 |
| Jogador 6 | 5-6 | 10 | 0.000 | 8.000 | 1 → 1 | 3 → 3 | 25% → 25% | 41 → 15 | 32 | 8 → 9 | -0.001 | -0.275 |
| Jogador 6 | 5-7 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 4 | 25% → 25% | 15 → 7 | 27 | 9 → 9 | 0.014 | 0.000 |
| Jogador 6 | 6-1 | 10 | -8.000 | 0.000 | 1 → 1 | 4 → 3 | 25% → 25% | 7 → 9 | 8 | 9 → 9 | -0.011 | -0.285 |
| Jogador 6 | 6-2 | 10 | -40.000 | -46.000 | 1 → 0 | 3 → 0 | 25% → 0% | 9 → 3 | 6 | 9 → 9 | -0.053 | -0.275 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 58 ações e piorou em 46.
- Jogador 6 — estado final: ouro 3, nível 9, vida 2.0, colocação 3.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.007 | 0.000 |
| Jogador 7 | 1-2 | 6 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 7 | 1-3 | 6 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | 0.124 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.104 | 0.000 |
| Jogador 7 | 2-1 | 9 | 2.000 | 8.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | 0.086 | -0.251 |
| Jogador 7 | 2-2 | 8 | 2.000 | 6.000 | 0 → 0 | 3 → 2 | 14% → 14% | 5 → 6 | 5 | 4 → 4 | -0.146 | -0.316 |
| Jogador 7 | 2-3 | 2 | 4.000 | -4.000 | 0 → 0 | 2 → 1 | 14% → 14% | 6 → 11 | 1 | 4 → 4 | 0.224 | 1.190 |
| Jogador 7 | 2-4 | 6 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 14% → 14% | 11 → 11 | 5 | 4 → 4 | -0.027 | 0.000 |
| Jogador 7 | 2-5 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 14% | 11 → 14 | 2 | 4 → 5 | 0.007 | -0.404 |
| Jogador 7 | 2-6 | 9 | 2.000 | 0.000 | 0 → 0 | 1 → 3 | 14% → 18% | 14 → 21 | 3 | 5 → 5 | 0.036 | -0.264 |
| Jogador 7 | 2-7 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 4 | 18% → 18% | 21 → 30 | 2 | 5 → 5 | 0.010 | 0.000 |
| Jogador 7 | 3-1 | 9 | -2.000 | 2.000 | 0 → 0 | 4 → 4 | 18% → 18% | 30 → 39 | 0 | 5 → 5 | -0.005 | -0.297 |
| Jogador 7 | 3-2 | 10 | 2.000 | 0.000 | 0 → 0 | 4 → 4 | 18% → 18% | 39 → 46 | 3 | 5 → 5 | 0.011 | -0.263 |
| Jogador 7 | 3-3 | 10 | 6.000 | 2.000 | 0 → 0 | 4 → 6 | 18% → 21% | 46 → 40 | 18 | 5 → 6 | 0.007 | 0.281 |
| Jogador 7 | 3-4 | 8 | 0.000 | 0.000 | 0 → 0 | 6 → 5 | 21% → 21% | 40 → 49 | 3 | 6 → 6 | 0.003 | 0.000 |
| Jogador 7 | 3-5 | 7 | 0.000 | -2.000 | 0 → 0 | 5 → 5 | 21% → 21% | 49 → 60 | 1 | 6 → 6 | -0.006 | -0.389 |
| Jogador 7 | 3-6 | 7 | 0.000 | 2.000 | 0 → 0 | 5 → 5 | 21% → 21% | 60 → 66 | 7 | 6 → 6 | -0.027 | 0.407 |
| Jogador 7 | 3-7 | 10 | -2.000 | 2.000 | 0 → 0 | 5 → 5 | 21% → 21% | 66 → 73 | 5 | 6 → 6 | -0.045 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | -4.000 | 0 → 0 | 5 → 5 | 21% → 21% | 73 → 75 | 16 | 6 → 6 | 0.006 | -0.273 |
| Jogador 7 | 4-2 | 10 | 4.000 | -4.000 | 0 → 0 | 5 → 5 | 21% → 25% | 75 → 78 | 12 | 6 → 7 | 0.088 | -0.270 |
| Jogador 7 | 4-3 | 5 | 0.000 | 8.000 | 0 → 0 | 5 → 5 | 25% → 25% | 78 → 85 | 4 | 7 → 7 | 0.043 | 0.572 |
| Jogador 7 | 4-4 | 10 | 0.000 | 4.000 | 0 → 0 | 5 → 5 | 25% → 25% | 85 → 81 | 18 | 7 → 7 | -0.040 | 0.000 |
| Jogador 7 | 4-5 | 10 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 81 → 67 | 27 | 7 → 7 | 0.000 | -0.271 |
| Jogador 7 | 4-6 | 10 | -24.000 | -42.000 | 0 → 0 | 5 → 0 | 25% → 0% | 67 → 47 | 24 | 7 → 8 | -0.070 | -0.281 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 15; mudanças de composição: 1; posicionamento melhorou em 47 ações e piorou em 35.
- Jogador 7 — estado final: ouro 47, nível 8, vida 12.0, colocação 8.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.007 | 0.000 |
| Jogador 8 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-3 | 6 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.010 | 0.000 |
| Jogador 8 | 2-1 | 9 | 2.000 | 2.000 | 0 → 0 | 1 → 0 | 11% → 14% | 4 → 7 | 3 | 4 → 4 | 0.000 | 0.264 |
| Jogador 8 | 2-2 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 14% → 14% | 7 → 6 | 6 | 4 → 4 | -0.015 | -0.395 |
| Jogador 8 | 2-3 | 2 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 14% → 14% | 6 → 11 | 1 | 4 → 5 | 0.027 | -1.161 |
| Jogador 8 | 2-4 | 9 | 2.000 | 6.000 | 0 → 0 | 1 → 2 | 14% → 18% | 11 → 9 | 8 | 5 → 5 | -0.051 | 0.000 |
| Jogador 8 | 2-5 | 11 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 8 | 10 | 5 → 5 | 0.026 | -0.231 |
| Jogador 8 | 2-6 | 10 | 4.000 | -6.000 | 0 → 0 | 3 → 4 | 18% → 21% | 8 → 8 | 13 | 5 → 6 | 0.024 | -0.249 |
| Jogador 8 | 2-7 | 9 | 2.000 | 10.000 | 0 → 0 | 4 → 4 | 21% → 21% | 8 → 8 | 7 | 6 → 6 | 0.007 | 0.000 |
| Jogador 8 | 3-1 | 10 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 21% → 21% | 8 → 8 | 8 | 6 → 6 | -0.055 | -0.283 |
| Jogador 8 | 3-2 | 8 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 8 → 8 | 9 | 6 → 6 | 0.008 | 0.346 |
| Jogador 8 | 3-3 | 9 | 0.000 | 0.000 | 0 → 0 | 4 → 5 | 21% → 21% | 8 → 9 | 5 | 6 → 6 | 0.045 | -0.293 |
| Jogador 8 | 3-4 | 9 | 0.000 | 2.000 | 0 → 0 | 5 → 4 | 21% → 21% | 9 → 13 | 5 | 6 → 6 | -0.005 | 0.000 |
| Jogador 8 | 3-5 | 10 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 13 → 18 | 9 | 6 → 6 | -0.008 | -0.258 |
| Jogador 8 | 3-6 | 10 | 2.000 | 6.000 | 0 → 0 | 4 → 4 | 21% → 25% | 18 → 8 | 19 | 6 → 7 | -0.010 | 0.281 |
| Jogador 8 | 3-7 | 8 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 25% → 25% | 8 → 10 | 4 | 7 → 7 | 0.015 | 0.000 |
| Jogador 8 | 4-1 | 10 | 0.000 | -12.000 | 0 → 0 | 4 → 4 | 25% → 18% | 10 → 17 | 6 | 7 → 7 | 0.046 | -0.298 |
| Jogador 8 | 4-2 | 10 | 2.000 | 2.000 | 0 → 0 | 4 → 3 | 18% → 21% | 17 → 16 | 11 | 7 → 7 | 0.051 | 0.291 |
| Jogador 8 | 4-3 | 9 | 8.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 25% | 16 → 6 | 15 | 7 → 7 | -0.009 | -0.300 |
| Jogador 8 | 4-4 | 8 | 0.000 | -4.000 | 0 → 0 | 3 → 4 | 25% → 25% | 6 → 16 | 4 | 7 → 7 | 0.050 | 0.000 |
| Jogador 8 | 4-5 | 9 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 16 → 21 | 5 | 7 → 7 | -0.040 | -0.315 |
| Jogador 8 | 4-6 | 10 | -28.000 | -40.000 | 0 → 0 | 4 → 0 | 25% → 0% | 21 → 2 | 25 | 7 → 8 | -0.079 | -0.268 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 48 ações e piorou em 41.
- Jogador 8 — estado final: ouro 2, nível 8, vida 4.0, colocação 7.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 46 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| Jogador 2 | 65 | 34 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 |
| Jogador 3 | 58 | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 0 | 0 |
| Jogador 4 | 71 | 30 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 |
| Jogador 5 | 75 | 42 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 |
| Jogador 6 | 56 | 21 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Jogador 7 | 40 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 8 | 47 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
- Jogador 1 — venda DA_18_Akali_AD (2-7, step 82): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 1 — venda DA_18_Rakan (3-3, step 112): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Vi18 (4-6, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Xayah (2-5, step 62): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Varus (3-2, step 102): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Kobuko (3-2, step 108): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Kayle (3-4, step 122): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Varus (3-5, step 134): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Veigar (3-7, step 152): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Varus (4-1, step 164): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Azir (4-6, step 213): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Varus (4-7, step 224): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (5-1, step 236): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_Sejuani (5-4, step 262): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_Scuttlecrab18 (3-1, step 96): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Karma18 (3-5, step 132): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 3 — venda DA_Vi18 (3-5, step 135): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_KhaZix (4-2, step 172): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Vi18 (4-6, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Rengar (4-7, step 224): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Camille (5-3, step 254): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Akali_AD (2-5, step 61): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Ornn (2-5, step 63): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Xayah (2-6, step 72): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Karma18 (2-6, step 76): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Camille (3-2, step 102): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Rakan (3-4, step 127): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Akali_AD (3-7, step 152): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_MasterYi_AD (4-4, step 192): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Diana (5-1, step 234): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_CrimsonRaptor18 (5-3, step 252): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Krug18 (6-1, step 303): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_Nidalee18_AP (6-3, step 322): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Rakan (2-5, step 65): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Cinderling18 (3-4, step 122): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_18_Rammus (4-2, step 172): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_MasterYi_AD (4-6, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (5-2, step 242): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Akali_AD (5-5, step 272): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Diana (5-6, step 282): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Nidalee18_AP (6-1, step 303): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Rammus (6-4, step 334): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Cassiopeia (6-5, step 345): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-5, step 69): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Cinderling18 (3-1, step 93): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Sentry (3-2, step 110): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Rakan (3-3, step 117): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_MasterYi_AD (4-4, step 194): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Rammus (4-6, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (5-1, step 234): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Fiddlesticks18 (5-7, step 292): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Scuttlecrab18 (5-7, step 294): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Varus (2-6, step 74): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=True, compensações posteriores=0.
- Jogador 7 — venda DA_18_Akali_AD (2-7, step 82): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rakan (3-3, step 113): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_RekSai (3-4, step 122): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_Murkwolf18 (3-4, step 124): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Shen (3-6, step 142): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_Fiddlesticks18 (4-1, step 165): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Warwick (4-2, step 174): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (4-6, step 212): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Leona (2-7, step 84): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Xayah (3-4, step 122): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Xayah (3-7, step 153): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Lillia (4-1, step 166): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Veigar (4-2, step 172): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (4-4, step 193): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (4-6, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **5**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 3-3 | 112 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 4-6 | 212 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 2-7 | 1133 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1219 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1220 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1292 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1293 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1428 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-3 | 1429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1564 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1565 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1685 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-5 | 1686 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1772 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1773 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1906 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 1907 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 2044 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 2138 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 2237 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2323 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 2324 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2418 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2419 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2560 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-6 | 2561 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 2677 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-1 | 2816 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 2931 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-2 | 2932 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 3009 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-3 | 3010 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| HIGH | Jogador 2 | 2-5 | 62 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-2 | 102 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Varus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-2 | 108 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 3-4 | 122 | SOLD_CORE_UNIT | Venda de 'DA_18_Kayle' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-5 | 134 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Varus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-7 | 152 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Veigar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-1 | 164 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Varus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-6 | 213 | SOLD_CORE_UNIT | Venda de 'DA_18_Azir' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-7 | 224 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Varus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 1-2 | 115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-3 | 199 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-4 | 334 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-1 | 460 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-2 | 588 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-3 | 624 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-4 | 746 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 2-5 | 856 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-6 | 993 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-7 | 1119 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-1 | 1216 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-2 | 1350 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-3 | 1474 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-4 | 1610 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-5 | 1723 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-6 | 1858 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-7 | 1998 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-1 | 2130 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 2261 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 2374 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 2509 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 2653 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-6 | 2779 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 2917 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-1 | 3054 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-2 | 3200 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-3 | 3341 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-4 | 3484 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-5 | 3607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 5-5 | 3608 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 3-3 | 1587 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-4 | 1700 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-5 | 2756 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-6 | 2894 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 3 | 3-1 | 96 | SOLD_CORE_UNIT | Venda de 'DA_Scuttlecrab18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 3-5 | 135 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 4-2 | 172 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 4-6 | 212 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 4-7 | 224 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-3 | 254 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 1-3 | 199 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-4 | 701 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 808 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 2-5 | 809 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1051 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 2-7 | 1052 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1199 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-1 | 1200 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1333 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1467 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1599 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1734 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-5 | 1735 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1871 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-6 | 1872 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1984 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-7 | 1985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 2117 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2213 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-2 | 2214 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 2325 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-3 | 2326 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 2423 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-4 | 2424 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2547 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2664 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-7 | 2802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 2945 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-1 | 2946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-2 | 3075 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-2 | 3076 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-3 | 3204 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-3 | 3205 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 4-5 | 2641 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-6 | 2779 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-1 | 3052 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 4 | 2-6 | 72 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 2-6 | 76 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Karma18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 4-4 | 192 | SOLD_CORE_UNIT | Venda de 'DA_18_MasterYi_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 5-3 | 252 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 6-3 | 322 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 2-5 | 873 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-7 | 1132 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-1 | 1253 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-1 | 1254 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-2 | 1380 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-2 | 1381 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-3 | 1510 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1511 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 1652 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1653 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 1765 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1766 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1855 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 1856 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1991 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 1992 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2309 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2440 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 2685 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-7 | 2826 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-1 | 2965 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-2 | 3068 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-3 | 3172 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-4 | 3301 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-5 | 3412 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-6 | 3536 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-7 | 3668 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-7 | 3669 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-1 | 3806 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-1 | 3807 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-2 | 3911 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-2 | 3912 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-3 | 4042 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-3 | 4043 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-4 | 4169 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-4 | 4170 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-5 | 4298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-5 | 4299 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| MEDIUM | Jogador 4 | 4-5 | 2662 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-1 | 3045 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-2 | 3149 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-4 | 3389 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-5 | 3513 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 5 | 2-5 | 65 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 4-2 | 172 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 4-6 | 212 | SOLD_CORE_UNIT | Venda de 'DA_18_MasterYi_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 5-2 | 242 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-5 | 272 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-6 | 282 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 6-1 | 303 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-4 | 334 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 6-5 | 345 | SOLD_CORE_UNIT | Venda de 'DA_18_Cassiopeia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 2-2 | 590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-3 | 628 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 748 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 892 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 1026 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 1147 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 1298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1432 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1564 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1697 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1834 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1933 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 2021 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 2159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2295 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2428 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2518 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 2519 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 2604 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2605 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2693 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 2694 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2794 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-7 | 2795 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 2931 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 2932 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 3070 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 3071 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 3215 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-3 | 3216 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3292 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-4 | 3293 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3421 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-5 | 3422 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3526 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-6 | 3527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 3658 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-7 | 3659 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 3802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-1 | 3803 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-2 | 3880 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-2 | 3881 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-3 | 4013 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-3 | 4014 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-4 | 4159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-4 | 4160 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-5 | 4301 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-5 | 4302 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 4-7 | 2908 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 3025 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 3036 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 3047 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-2 | 3164 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-3 | 3269 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-4 | 3398 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-5 | 3503 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 6-1 | 3857 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 6-2 | 3990 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-2 | 48 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 2-5 | 69 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 3-1 | 93 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Cinderling18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 3-2 | 110 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-6 | 212 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-1 | 234 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-7 | 292 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-7 | 294 | SOLD_CORE_UNIT | Venda de 'DA_Scuttlecrab18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 470 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 631 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 752 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 753 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-5 | 901 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 902 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-6 | 1026 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 1027 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-7 | 1136 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-1 | 1244 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-2 | 1383 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-3 | 1517 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1603 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1728 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1729 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 1828 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1954 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 2096 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2207 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2294 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2434 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2535 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 2622 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 2698 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 2814 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 2923 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 3025 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-4 | 3153 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-5 | 3280 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-6 | 3407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-7 | 3536 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-1 | 3671 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-2 | 3810 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-2 | 3811 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 5-4 | 3213 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 5-4 | 3224 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 5-4 | 3235 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 5-4 | 3246 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 5-4 | 3257 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 7 | 2-7 | 82 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-3 | 113 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-4 | 122 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-4 | 124 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Murkwolf18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-6 | 142 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-1 | 165 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-2 | 174 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-6 | 212 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 296 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 530 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-3 | 566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-4 | 649 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-5 | 732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 855 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 972 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1102 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1241 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1374 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1482 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1581 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1678 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1817 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 1818 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 1953 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-1 | 1954 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2086 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2162 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2296 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-4 | 2297 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2425 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2426 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-6 | 2559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 2-5 | 832 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-6 | 949 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-7 | 1079 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-3 | 1459 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-4 | 1558 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-5 | 1655 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-6 | 1794 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-2 | 2139 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-4 | 122 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Xayah' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-7 | 153 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Xayah' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-2 | 172 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-4 | 193 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-6 | 212 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 1-2 | 115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 1-3 | 198 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 1-4 | 295 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 2-1 | 418 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 2-2 | 504 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 541 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 663 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 815 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 949 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1071 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1211 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1445 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1569 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1705 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 1838 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 1950 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2354 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-6 | 2723 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 4-6 | 2724 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 4-3 | 2443 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-4 | 2567 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
