# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5243**
- Achados: **892**
- CRITICAL: 0 | HIGH: 14 | MEDIUM: 72 | LOW: 806

## Metadados da sessão

- Match ID: 3cfff16b-6164-4184-bb7e-73e2bcc13d2d
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4693**
- Entradas posteriores à eliminação ignoradas: **550**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 117 | 7 | 8 | 8 | 78 | 3 | 2 | não/inconclusivo | 0 |
| Jogador 6 | 119 | 7 | 11 | 8 | 87 | 4 | 1 | não/inconclusivo | 0 |
| Jogador 7 | 173 | 7 | 12 | 10 | 100 | 1 | 3 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 256 | 93 | 54 | 12 | 0 | 17 | 67 | 0.1013 | 12 | 47 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 14, ALL_IN::ITEM: 1, ALL_IN::MOVE_BOARD: 2, ALL_IN::SELL: 10, FAST8::BUY: 4, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 3, FAST8::SELL: 3, STABILIZE::BUY: 75, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 12, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 46, STABILIZE::PASS: 17, STABILIZE::SELL: 41
- Jogador 1 — recompensas por ação: BUY: média 0.3386 (n=93), BUY_XP: média -0.0158 (n=12), ITEM: média 0.1285 (n=13), MOVE_BENCH: média 0.2656 (n=16), MOVE_BOARD: média -0.0024 (n=51), PASS: média -0.0188 (n=17), SELL: média -0.2007 (n=54)
| Jogador 2 | 298 | 105 | 69 | 28 | 0 | 15 | 73 | 0.0711 | 7 | 45 |
- Jogador 2 — ações por estratégia: FAST8::BUY: 21, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 8, FAST8::PASS: 1, FAST8::SELL: 18, STABILIZE::BUY: 84, STABILIZE::BUY_XP: 28, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 22, STABILIZE::MOVE_BOARD: 42, STABILIZE::PASS: 14, STABILIZE::SELL: 51
- Jogador 2 — recompensas por ação: BUY: média 0.2612 (n=105), BUY_XP: média 0.0068 (n=28), ITEM: média 0.1762 (n=8), MOVE_BENCH: média 0.1752 (n=23), MOVE_BOARD: média -0.0110 (n=50), PASS: média -0.0233 (n=15), SELL: média -0.1591 (n=69)
| Jogador 3 | 179 | 56 | 22 | 9 | 2 | 20 | 62 | 0.1146 | 7 | 12 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 4, ALL_IN::PASS: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 5, STABILIZE::BUY: 47, STABILIZE::BUY_XP: 9, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 39, STABILIZE::PASS: 19, STABILIZE::SELL: 17
- Jogador 3 — recompensas por ação: BUY: média 0.4191 (n=56), BUY_XP: média -0.0400 (n=9), ITEM: média 0.1713 (n=8), MOVE_BENCH: média 0.0926 (n=19), MOVE_BOARD: média -0.0058 (n=43), PASS: média -0.0375 (n=20), REROLL: média -0.0700 (n=2), SELL: média -0.2086 (n=22)
| Jogador 4 | 208 | 78 | 45 | 8 | 0 | 16 | 52 | 0.0936 | 7 | 18 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 26, ALL_IN::ITEM: 4, ALL_IN::MOVE_BENCH: 7, ALL_IN::MOVE_BOARD: 4, ALL_IN::PASS: 3, ALL_IN::SELL: 19, STABILIZE::BUY: 52, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 29, STABILIZE::PASS: 13, STABILIZE::SELL: 26
- Jogador 4 — recompensas por ação: BUY: média 0.3719 (n=78), BUY_XP: média -0.0225 (n=8), ITEM: média 0.1533 (n=9), MOVE_BENCH: média 0.0089 (n=19), MOVE_BOARD: média -0.0027 (n=33), PASS: média -0.1113 (n=16), SELL: média -0.2011 (n=45)
| Jogador 5 | 279 | 110 | 77 | 12 | 3 | 12 | 50 | 0.0747 | 17 | 29 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 2, ALL_IN::REROLL: 2, ALL_IN::SELL: 5, STABILIZE::BUY: 103, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 13, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 30, STABILIZE::PASS: 12, STABILIZE::REROLL: 1, STABILIZE::SELL: 72
- Jogador 5 — recompensas por ação: BUY: média 0.2450 (n=110), BUY_XP: média -0.0150 (n=12), ITEM: média 0.1340 (n=15), MOVE_BENCH: média 0.2710 (n=20), MOVE_BOARD: média 0.0067 (n=30), PASS: média -0.0325 (n=12), REROLL: média -0.1133 (n=3), SELL: média -0.1666 (n=77)
| Jogador 6 | 255 | 87 | 58 | 11 | 2 | 16 | 71 | 0.0725 | 11 | 55 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 25, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 8, ALL_IN::MOVE_BOARD: 7, ALL_IN::OTHER: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 18, FAST8::BUY: 5, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 9, FAST8::PASS: 3, FAST8::SELL: 4, STABILIZE::BUY: 57, STABILIZE::BUY_XP: 11, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 33, STABILIZE::PASS: 13, STABILIZE::SELL: 36
- Jogador 6 — recompensas por ação: BUY: média 0.2768 (n=87), BUY_XP: média -0.0518 (n=11), ITEM: média 0.1556 (n=9), MOVE_BENCH: média 0.1827 (n=22), MOVE_BOARD: média -0.0061 (n=49), OTHER: média 0.0100 (n=1), PASS: média -0.0131 (n=16), REROLL: média -0.0700 (n=2), SELL: média -0.1690 (n=58)
| Jogador 7 | 289 | 100 | 62 | 12 | 0 | 20 | 77 | 0.0857 | 8 | 49 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 32, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 2, ALL_IN::MOVE_BOARD: 3, ALL_IN::SELL: 25, STABILIZE::BUY: 68, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 17, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 58, STABILIZE::PASS: 20, STABILIZE::SELL: 37
- Jogador 7 — recompensas por ação: BUY: média 0.3082 (n=100), BUY_XP: média -0.0342 (n=12), ITEM: média 0.1300 (n=18), MOVE_BENCH: média 0.2681 (n=16), MOVE_BOARD: média -0.0061 (n=61), PASS: média -0.0300 (n=20), SELL: média -0.1821 (n=62)
| Jogador 8 | 165 | 67 | 36 | 3 | 1 | 8 | 42 | 0.1147 | 5 | 25 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 2, ALL_IN::REROLL: 1, ALL_IN::SELL: 4, STABILIZE::BUY: 60, STABILIZE::BUY_XP: 3, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 31, STABILIZE::MOVE_BOARD: 8, STABILIZE::PASS: 8, STABILIZE::SELL: 32
- Jogador 8 — recompensas por ação: BUY: média 0.3385 (n=67), BUY_XP: média -0.0200 (n=3), ITEM: média 0.1775 (n=8), MOVE_BENCH: média 0.0078 (n=32), MOVE_BOARD: média -0.0120 (n=10), PASS: média -0.0213 (n=8), REROLL: média -0.0700 (n=1), SELL: média -0.1389 (n=36)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 12:59:32 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 12:59:34 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 12:59:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 12:59:39 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 12:59:40 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 12:59:40 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 12:59:41 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 12:59:42 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 12:59:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 12:59:45 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 12:59:47 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 12:59:47 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 12:59:48 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 12:59:48 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 12:59:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 12:59:56 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 12:59:56 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 12:59:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 13:00:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 13:00:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 13:00:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 13:00:10 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 2-1 | 13:00:13 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 13:00:14 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 13:00:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 13:00:15 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 13:00:15 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 13:00:16 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 13:00:16 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-2 | 13:00:24 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 1 | 2-2 | 13:00:24 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.3600 |  |
| Jogador 1 | 2-2 | 13:00:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 13:00:25 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 13:00:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 13:00:26 | MOVE Board -> Board: Ornn (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 13:00:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-2 | 13:00:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 13:00:36 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 13:00:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0600 |  |
| Jogador 1 | 2-3 | 13:00:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-4 | 13:00:52 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Ornn | 1.0200 |  |
| Jogador 1 | 2-4 | 13:00:53 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Shen | -0.6300 |  |
| Jogador 1 | 2-4 | 13:00:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Shen | 0.3000 |  |
| Jogador 1 | 2-4 | 13:00:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0300 |  |
| Jogador 1 | 2-4 | 13:00:54 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 2-4 | 13:00:55 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.4000 |  |
| Jogador 1 | 2-4 | 13:00:55 | MOVE Board -> Board: Grompe (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 2-4 | 13:00:56 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 2-4 | 13:00:56 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 2-5 | 13:01:08 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | 1.1200 |  |
| Jogador 1 | 2-5 | 13:01:08 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.0700 |  |
| Jogador 1 | 2-5 | 13:01:09 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | 0.0700 |  |
| Jogador 1 | 2-5 | 13:01:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | 0.0400 |  |
| Jogador 1 | 2-5 | 13:01:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 13:01:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | 1.1200 |  |
| Jogador 1 | 2-6 | 13:01:25 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.9400 |  |
| Jogador 1 | 2-6 | 13:01:25 | MOVE Bench -> Board: Akali (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.2600 |  |
| Jogador 1 | 2-6 | 13:01:26 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.1400 |  |
| Jogador 1 | 2-6 | 13:01:26 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.0700 |  |
| Jogador 1 | 2-6 | 13:01:27 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 13:01:27 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | -0.6300 |  |
| Jogador 1 | 2-6 | 13:01:27 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Xayah (i:2.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | 0.1100 |  |
| Jogador 1 | 2-6 | 13:01:28 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Xayah (i:2.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | 0.1000 |  |
| Jogador 1 | 2-7 | 13:01:43 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 13:01:43 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 2-7 | 13:01:44 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 2-7 | 13:01:44 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 2-7 | 13:01:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-7 | 13:01:45 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | -0.0700 |  |
| Jogador 1 | 2-7 | 13:01:46 | MOVE Board -> Board: Cascalho (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 13:01:46 | MOVE Board -> Board: Grompe (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | -0.1600 |  |
| Jogador 1 | 2-7 | 13:01:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 13:02:03 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.6600 |  |
| Jogador 1 | 3-1 | 13:02:04 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | 0.3600 |  |
| Jogador 1 | 3-1 | 13:02:04 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 3-1 | 13:02:05 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.1400 |  |
| Jogador 1 | 3-1 | 13:02:05 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 13:02:06 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.2300 |  |
| Jogador 1 | 3-1 | 13:02:06 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 13:02:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 13:02:07 | MOVE Board -> Board: Shen (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 13:02:26 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | -0.2100 |  |
| Jogador 1 | 3-2 | 13:02:27 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 13:02:27 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | -0.2500 |  |
| Jogador 1 | 3-2 | 13:02:28 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | 0.0100 |  |
| Jogador 1 | 3-2 | 13:02:29 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_18_Akali_AD | -0.1000 |  |
| Jogador 1 | 3-2 | 13:02:29 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Akali_AD | -0.4300 |  |
| Jogador 1 | 3-2 | 13:02:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_18_Akali_AD | -0.0900 |  |
| Jogador 1 | 3-2 | 13:02:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 13:02:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 13:02:52 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | 0.2900 |  |
| Jogador 1 | 3-3 | 13:02:52 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 3-3 | 13:02:53 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | -0.0700 |  |
| Jogador 1 | 3-3 | 13:02:54 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.0100 |  |
| Jogador 1 | 3-3 | 13:02:54 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 13:02:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 3-3 | 13:02:55 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | 0.4100 |  |
| Jogador 1 | 3-3 | 13:02:56 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 13:02:56 | MOVE Board -> Board: Cascalho (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-4 | 13:03:18 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.8400 |  |
| Jogador 1 | 3-4 | 13:03:19 | MOVE Bench -> Board: Shen (i:8.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | -0.3900 |  |
| Jogador 1 | 3-4 | 13:03:20 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.7600 |  |
| Jogador 1 | 3-4 | 13:03:20 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 3-4 | 13:03:21 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | -0.0300 |  |
| Jogador 1 | 3-4 | 13:03:21 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | 0.1500 |  |
| Jogador 1 | 3-4 | 13:03:22 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-4 | 13:03:22 | MOVE Board -> Board: Xayah (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 13:03:23 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-5 | 13:03:47 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | 0.8000 |  |
| Jogador 1 | 3-5 | 13:03:48 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Akali_AD | 0.2900 |  |
| Jogador 1 | 3-5 | 13:03:48 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 3-5 | 13:03:49 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-5 | 13:03:49 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-5 | 13:03:50 | MOVE Board -> Board: Akali (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 3-5 | 13:03:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 13:04:18 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.2800 |  |
| Jogador 1 | 3-6 | 13:04:18 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | -0.0800 |  |
| Jogador 1 | 3-6 | 13:04:18 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.8000 |  |
| Jogador 1 | 3-6 | 13:04:19 | MOVE Board -> Board: Varus (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 3-6 | 13:04:20 | MOVE Board -> Board: Vi (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-6 | 13:04:20 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 13:04:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 13:04:50 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_BFSword -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 3-7 | 13:04:51 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Akali_AD | 0.0700 |  |
| Jogador 1 | 3-7 | 13:04:52 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.4100 |  |
| Jogador 1 | 3-7 | 13:04:52 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_18_Akali_AD | -0.4500 |  |
| Jogador 1 | 3-7 | 13:04:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | 0.0300 |  |
| Jogador 1 | 3-7 | 13:04:55 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 13:04:55 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | 0.5000 |  |
| Jogador 1 | 3-7 | 13:04:55 | MOVE Board -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 13:05:27 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Akali_AD | -0.5900 |  |
| Jogador 1 | 4-1 | 13:05:28 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Inferno | DA_18_Akali_AD | 0.2900 |  |
| Jogador 1 | 4-1 | 13:05:28 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Akali_AD | -0.5900 |  |
| Jogador 1 | 4-1 | 13:05:29 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Akali_AD | 0.2300 |  |
| Jogador 1 | 4-1 | 13:05:30 | MOVE Board -> Board: Akali (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 13:05:30 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Akali_AD | -0.0800 |  |
| Jogador 1 | 4-1 | 13:05:31 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 4-1 | 13:05:31 | MOVE Board -> Board: Varus (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 13:05:32 | MOVE Board -> Board: Xayah (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 4-2 | 13:06:05 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_18_Akali_AD | 0.0700 |  |
| Jogador 1 | 4-2 | 13:06:05 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Inferno | DA_18_Akali_AD | -0.0700 |  |
| Jogador 1 | 4-2 | 13:06:06 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_18_Akali_AD | 0.0700 |  |
| Jogador 1 | 4-2 | 13:06:07 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Akali_AD | 0.0700 |  |
| Jogador 1 | 4-2 | 13:06:07 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 4-2 | 13:06:08 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 4-2 | 13:06:08 | MOVE Board -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 13:06:09 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 4-2 | 13:06:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Akali_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-3 | 13:06:44 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 4-3 | 13:06:44 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Inferno | DA_Fiddlesticks18 | 0.8100 |  |
| Jogador 1 | 4-3 | 13:06:45 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Inferno | DA_Fiddlesticks18 | 0.7600 |  |
| Jogador 1 | 4-3 | 13:06:46 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Inferno | DA_Fiddlesticks18 | -0.1800 |  |
| Jogador 1 | 4-3 | 13:06:47 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 2 | Inferno | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 1 | 4-3 | 13:06:47 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 2 | Inferno | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 1 | 4-3 | 13:06:48 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 2 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 4-3 | 13:06:48 | MOVE Board -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 2 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 4-3 | 13:06:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 2 | Inferno | DA_Fiddlesticks18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-4 | 13:07:27 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 1 | Inferno | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 1 | 4-4 | 13:07:28 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Inferno | DA_Fiddlesticks18 | 0.2100 |  |
| Jogador 1 | 4-4 | 13:07:28 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 1 | Inferno | DA_18_Shen | -0.4900 |  |
| Jogador 1 | 4-4 | 13:07:29 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 1 | Inferno | DA_18_Shen | -0.1600 |  |
| Jogador 1 | 4-4 | 13:07:29 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 1 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-4 | 13:07:30 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 1 | Inferno | DA_18_Shen | -0.1600 |  |
| Jogador 1 | 4-4 | 13:07:30 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 1 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-4 | 13:07:31 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Inferno | DA_18_Shen | -0.0500 |  |
| Jogador 1 | 4-4 | 13:07:32 | MOVE Board -> Board: Akali (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-5 | 13:08:11 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 4-5 | 13:08:12 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Inferno | DA_18_Shen | 0.9200 |  |
| Jogador 1 | 4-5 | 13:08:12 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Inferno | DA_18_Shen | 0.2400 |  |
| Jogador 1 | 4-5 | 13:08:12 | MOVE Bench -> Board: Malphite (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Inferno | DA_18_Shen | 0.4000 |  |
| Jogador 1 | 4-5 | 13:08:13 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Inferno | DA_18_Shen | -0.2300 |  |
| Jogador 1 | 4-5 | 13:08:14 | MOVE Board -> Board: Malphite (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-5 | 13:08:14 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-5 | 13:08:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Inferno | DA_18_Shen | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-6 | 13:08:53 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Inferno | DA_18_Shen | -0.5000 |  |
| Jogador 1 | 4-6 | 13:08:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Inferno | DA_18_Shen | 0.2700 |  |
| Jogador 1 | 4-6 | 13:08:54 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 4-6 | 13:08:55 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 4-6 | 13:08:55 | MOVE Board -> Board: Vi (i:6.0) <-> Malphite (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-6 | 13:08:55 | MOVE Board -> Board: Malphite (i:8.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-6 | 13:08:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Inferno | DA_18_Shen | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Malphite (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Malphite (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Inferno | DA_18_Shen | 0.0800 |  |
| Jogador 1 | 4-7 | 13:09:38 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 4 | Inferno | DA_18_Shen | -0.0500 |  |
| Jogador 1 | 4-7 | 13:09:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 4 | Inferno | DA_18_Shen | 0.9100 |  |
| Jogador 1 | 4-7 | 13:09:39 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 4 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 4-7 | 13:09:39 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 4 | Inferno | DA_18_Shen | 0.6600 |  |
| Jogador 1 | 4-7 | 13:09:40 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 4 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-7 | 13:09:40 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Inferno | DA_18_Shen | 0.9900 |  |
| Jogador 1 | 4-7 | 13:09:41 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Inferno | DA_18_Shen | -0.1900 |  |
| Jogador 1 | 5-1 | 13:10:23 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Inferno | DA_18_Shen | 1.0200 |  |
| Jogador 1 | 5-1 | 13:10:24 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Inferno | DA_18_Shen | 0.3800 |  |
| Jogador 1 | 5-1 | 13:10:24 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Inferno | DA_18_Shen | -0.5900 |  |
| Jogador 1 | 5-1 | 13:10:25 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Inferno | DA_18_Shen | 0.1200 |  |
| Jogador 1 | 5-1 | 13:10:25 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Akali (i:4.0) (tabuleiro slot 6) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Inferno | DA_18_Shen | 0.1100 |  |
| Jogador 1 | 5-1 | 13:10:26 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Aronguejo (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 5-1 | 13:10:26 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Aronguejo (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 5-1 | 13:10:27 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Inferno | DA_18_Shen | 0.5300 |  |
| Jogador 1 | 5-1 | 13:10:27 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Inferno | DA_18_Shen | -0.2500 |  |
| Jogador 1 | 5-2 | 13:11:15 | VENDEU: Krugue (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Inferno | DA_18_Shen | -0.5000 |  |
| Jogador 1 | 5-2 | 13:11:15 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Inferno | DA_18_Shen | 0.3800 |  |
| Jogador 1 | 5-2 | 13:11:16 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-2 | 13:11:16 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Inferno | DA_18_Shen | 0.4000 |  |
| Jogador 1 | 5-2 | 13:11:17 | VENDEU: Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 5-2 | 13:11:17 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Inferno | DA_18_Shen | 0.2900 |  |
| Jogador 1 | 5-2 | 13:11:18 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-2 | 13:11:19 | MOVE Board -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-2 | 13:11:19 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-3 | 13:12:10 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Inferno | DA_18_Shen | -0.1200 |  |
| Jogador 1 | 5-3 | 13:12:11 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Inferno | DA_18_Shen | 0.9700 |  |
| Jogador 1 | 5-3 | 13:12:13 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Inferno | DA_18_Shen | -0.5900 |  |
| Jogador 1 | 5-3 | 13:12:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_18_Shen | 0.3500 |  |
| Jogador 1 | 5-3 | 13:12:14 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Inferno | DA_18_Shen | -0.4400 |  |
| Jogador 1 | 5-3 | 13:12:15 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_18_Shen | 0.1000 |  |
| Jogador 1 | 5-3 | 13:12:15 | MOVE Board -> Board: Malphite (i:8.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-3 | 13:12:15 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 5-3 | 13:12:16 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_18_Shen | -0.1700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 5-4 | 13:13:05 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 5-4 | 13:13:05 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Inferno | DA_18_Shen | 0.1900 |  |
| Jogador 1 | 5-4 | 13:13:06 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Inferno | DA_18_Shen | -0.0600 |  |
| Jogador 1 | 5-4 | 13:13:06 | COMPROU: Lux (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Inferno | DA_18_Shen | -0.1800 |  |
| Jogador 1 | 5-4 | 13:13:07 | VENDEU: Lux (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-4 | 13:13:07 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Inferno | DA_18_Shen | 0.0300 |  |
| Jogador 1 | 5-4 | 13:13:08 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-4 | 13:13:08 | MOVE Board -> Board: Akali (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 5-4 | 13:13:08 | MOVE Board -> Board: Vi (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Inferno | DA_18_Shen | -0.0500 |  |
| Jogador 1 | 5-5 | 13:13:57 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-5 | 13:13:57 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Inferno | DA_18_Shen | 0.9200 |  |
| Jogador 1 | 5-5 | 13:13:58 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Inferno | DA_18_Shen | -0.5800 |  |
| Jogador 1 | 5-5 | 13:13:58 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Inferno | DA_18_Shen | 0.5500 |  |
| Jogador 1 | 5-5 | 13:13:59 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Inferno | DA_18_Shen | -0.5800 |  |
| Jogador 1 | 5-5 | 13:13:59 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Inferno | DA_18_Shen | 0.1500 |  |
| Jogador 1 | 5-5 | 13:14:00 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 5-5 | 13:14:00 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Inferno | DA_18_Shen | 0.1300 |  |
| Jogador 1 | 5-5 | 13:14:01 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-6 | 13:15:16 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 5-6 | 13:15:17 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Inferno | DA_18_Shen | 1.0600 |  |
| Jogador 1 | 5-6 | 13:15:18 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Inferno | DA_18_Shen | -0.2000 |  |
| Jogador 1 | 5-6 | 13:15:18 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 5-6 | 13:15:19 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Inferno | DA_18_Shen | -0.7200 |  |
| Jogador 1 | 5-6 | 13:15:19 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Inferno | DA_18_Shen | 0.0500 |  |
| Jogador 1 | 5-6 | 13:15:20 | MOVE Board -> Board: Malphite (i:8.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-6 | 13:15:21 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-6 | 13:15:21 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Inferno | DA_18_Shen | -0.2700 |  |
| Jogador 1 | 5-7 | 13:16:24 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Malphite (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Inferno | DA_18_Shen | 0.0500 |  |
| Jogador 1 | 5-7 | 13:16:25 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Inferno | DA_18_Shen | 0.0200 |  |
| Jogador 1 | 5-7 | 13:16:25 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Inferno | DA_18_Shen | 1.1100 |  |
| Jogador 1 | 5-7 | 13:16:26 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Inferno | DA_18_Shen | 0.9500 |  |
| Jogador 1 | 5-7 | 13:16:26 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Inferno | DA_18_Shen | 1.1100 |  |
| Jogador 1 | 5-7 | 13:16:27 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Inferno | DA_18_Shen | 0.0800 |  |
| Jogador 1 | 5-7 | 13:16:27 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Inferno | DA_18_Shen | -0.2700 |  |
| Jogador 1 | 5-7 | 13:16:28 | VENDEU: Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Inferno | DA_CrimsonRaptor18 | -0.9700 |  |
| Jogador 1 | 5-7 | 13:16:29 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Inferno | DA_18_Shen | -0.7700 |  |
| Jogador 2 | ? | 12:59:32 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 12:59:34 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 12:59:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 12:59:39 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 12:59:40 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 12:59:40 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 12:59:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 12:59:45 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 12:59:47 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 12:59:47 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 12:59:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 12:59:52 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 12:59:56 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 12:59:56 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 12:59:57 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 12:59:57 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 12:59:58 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 12:59:58 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 12:59:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 13:00:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 13:00:06 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 13:00:06 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 13:00:06 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 13:00:07 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 13:00:10 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 1-4 | 13:00:10 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 13:00:13 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 13:00:14 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 13:00:14 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 13:00:15 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 13:00:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 13:00:16 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 13:00:16 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-2 | 13:00:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 13:00:24 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-2 | 13:00:25 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-2 | 13:00:25 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-2 | 13:00:26 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-2 | 13:00:26 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-2 | 13:00:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 13:00:27 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-2 | 13:00:28 | MOVE Board -> Board: Vi (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 13:00:36 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 2-3 | 13:00:37 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 2-3 | 13:00:37 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 13:00:38 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 13:00:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-4 | 13:00:52 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 2-4 | 13:00:53 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-4 | 13:00:53 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-4 | 13:00:54 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 2-4 | 13:00:54 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 2-4 | 13:00:55 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 13:00:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-5 | 13:01:08 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.8900 |  |
| Jogador 2 | 2-5 | 13:01:08 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 2-5 | 13:01:09 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 2-5 | 13:01:09 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 13:01:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 13:01:10 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-5 | 13:01:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 13:01:11 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-5 | 13:01:12 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 2-6 | 13:01:24 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.6500 |  |
| Jogador 2 | 2-6 | 13:01:25 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 2-6 | 13:01:25 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 2-6 | 13:01:26 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-6 | 13:01:26 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-6 | 13:01:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-6 | 13:01:27 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.6000 |  |
| Jogador 2 | 2-6 | 13:01:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 13:01:28 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 13:01:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 2-7 | 13:01:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 2-7 | 13:01:44 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 13:01:44 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.4600 |  |
| Jogador 2 | 2-7 | 13:01:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 13:01:45 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 2-7 | 13:01:46 | MOVE Bench -> Board: Tristana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 2-7 | 13:01:46 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 2-7 | 13:01:47 | MOVE Board -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 13:02:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 3-1 | 13:02:04 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-1 | 13:02:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 13:02:05 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-1 | 13:02:05 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-1 | 13:02:06 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-1 | 13:02:06 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 13:02:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 13:02:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 13:02:26 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | 0.7200 |  |
| Jogador 2 | 3-2 | 13:02:27 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 3-2 | 13:02:27 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-2 | 13:02:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 13:02:29 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-2 | 13:02:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 13:02:30 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.4300 |  |
| Jogador 2 | 3-2 | 13:02:30 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-2 | 13:02:31 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 13:02:52 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-3 | 13:02:52 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 3-3 | 13:02:53 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-3 | 13:02:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 13:02:54 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.5700 |  |
| Jogador 2 | 3-3 | 13:02:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 13:02:55 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-3 | 13:02:56 | MOVE Board -> Board: Veigar (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 13:02:56 | MOVE Board -> Board: Vi (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 13:03:18 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 3-4 | 13:03:19 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-4 | 13:03:20 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 3-4 | 13:03:20 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 3-4 | 13:03:21 | MOVE Board -> Board: Rammus (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 13:03:21 | MOVE Board -> Board: Veigar (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 13:03:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 13:03:47 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | 0.8300 |  |
| Jogador 2 | 3-5 | 13:03:48 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 3-5 | 13:03:48 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 3-5 | 13:03:49 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 13:03:49 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 13:03:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 13:04:18 | VENDEU: Sejuani (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_18_Veigar | -0.5800 |  |
| Jogador 2 | 3-6 | 13:04:18 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Tristana | 0.8300 |  |
| Jogador 2 | 3-6 | 13:04:18 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Tristana | 0.1400 |  |
| Jogador 2 | 3-6 | 13:04:19 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 3-6 | 13:04:20 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 3-6 | 13:04:20 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 13:04:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-6 | 13:04:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 3-6 | 13:04:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-7 | 13:04:50 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 3-7 | 13:04:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-7 | 13:04:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-7 | 13:04:54 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 3-7 | 13:04:55 | MOVE Board -> Board: Krugue (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-7 | 13:04:55 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-7 | 13:04:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 13:05:27 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 4-1 | 13:05:28 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 4-1 | 13:05:28 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 13:05:29 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.5800 |  |
| Jogador 2 | 4-1 | 13:05:30 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-1 | 13:05:30 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-1 | 13:05:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-1 | 13:05:31 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 4-1 | 13:05:32 | MOVE Board -> Board: Krugue (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-2 | 13:06:05 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.7400 |  |
| Jogador 2 | 4-2 | 13:06:05 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 4-2 | 13:06:06 | MOVE Bench -> Board: Krugue (i:12.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-2 | 13:06:07 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.6100 |  |
| Jogador 2 | 4-2 | 13:06:07 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Krugue (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Vivaz | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 4-2 | 13:06:08 | VENDEU: Krugue (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Vivaz | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 4-2 | 13:06:08 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Vivaz | DA_18_Veigar | -0.1700 |  |
| Jogador 2 | 4-2 | 13:06:09 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-2 | 13:06:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Vivaz | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-3 | 13:06:44 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Vivaz | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 4-3 | 13:06:44 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Vivaz | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-3 | 13:06:45 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-3 | 13:06:46 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 4-3 | 13:06:47 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 4-3 | 13:06:47 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Vivaz | DA_18_Veigar | -0.1900 |  |
| Jogador 2 | 4-3 | 13:06:48 | MOVE Board -> Board: Rammus (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 13:06:48 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-3 | 13:06:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 13:07:27 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_Veigar | 0.7300 |  |
| Jogador 2 | 4-4 | 13:07:28 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 13:07:28 | MOVE Board -> Board: Rammus (i:6.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 4-4 | 13:07:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-5 | 13:08:11 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-5 | 13:08:12 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vivaz | DA_18_Veigar | 0.7400 |  |
| Jogador 2 | 4-5 | 13:08:12 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vivaz | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 4-5 | 13:08:12 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Vivaz | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 4-5 | 13:08:13 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Vivaz | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 4-5 | 13:08:14 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-5 | 13:08:14 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Vivaz | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 4-5 | 13:08:15 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-5 | 13:08:15 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Vivaz | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 4-6 | 13:08:53 | VENDEU: Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-6 | 13:08:54 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Vivaz | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 4-6 | 13:08:54 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Vivaz | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 4-6 | 13:08:55 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Vivaz | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 4-6 | 13:08:55 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-6 | 13:08:55 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Vivaz | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-6 | 13:08:56 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Vivaz | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-6 | 13:08:56 | COMPROU: Varus (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Vivaz | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 4-6 | 13:08:57 | MOVE Board -> Board: Vi (i:6.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Vivaz | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Vivaz | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 4-7 | 13:09:38 | VENDEU: Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-7 | 13:09:38 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Vivaz | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 4-7 | 13:09:39 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Vivaz | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 4-7 | 13:09:39 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Vivaz | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 4-7 | 13:09:40 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-7 | 13:09:40 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 2 | Vivaz | DA_18_Veigar | -0.1700 |  |
| Jogador 2 | 4-7 | 13:09:41 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 2 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-1 | 13:10:23 | VENDEU: Lux (Sabugueiro) (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-1 | 13:10:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Vivaz | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 5-1 | 13:10:24 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Vivaz | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 5-1 | 13:10:25 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Vivaz | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 5-1 | 13:10:25 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-1 | 13:10:26 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-1 | 13:10:26 | VENDEU: Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-1 | 13:10:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Vivaz | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 5-1 | 13:10:27 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Vivaz | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 5-2 | 13:11:15 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Vivaz | DA_18_Veigar | 0.9000 |  |
| Jogador 2 | 5-2 | 13:11:15 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Vivaz | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 5-2 | 13:11:16 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Vivaz | DA_18_Veigar | -0.1700 |  |
| Jogador 2 | 5-2 | 13:11:16 | VENDEU: Azir (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Vivaz | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 5-2 | 13:11:17 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Vivaz | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 5-2 | 13:11:17 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-2 | 13:11:18 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Vivaz | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 5-2 | 13:11:19 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-2 | 13:11:19 | MOVE Board -> Board: Rammus (i:6.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-3 | 13:12:10 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 13:12:11 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Vivaz | DA_18_Veigar | 1.0200 |  |
| Jogador 2 | 5-3 | 13:12:13 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Vivaz | DA_18_Veigar | 0.4700 |  |
| Jogador 2 | 5-3 | 13:12:14 | COMPROU: Alune (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 4 | Vivaz | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 5-3 | 13:12:14 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Vivaz | DA_18_Veigar | -0.8400 |  |
| Jogador 2 | 5-3 | 13:12:15 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 4 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 13:12:15 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 13:12:15 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 4 | Vivaz | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 5-3 | 13:12:16 | MOVE Board -> Board: Vi (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 4 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-4 | 13:13:05 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-4 | 13:13:05 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Vivaz | DA_18_Veigar | 0.8600 |  |
| Jogador 2 | 5-4 | 13:13:06 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-4 | 13:13:06 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Vivaz | DA_18_Veigar | 0.3500 |  |
| Jogador 2 | 5-4 | 13:13:07 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Vivaz | DA_18_Veigar | 0.4200 |  |
| Jogador 2 | 5-4 | 13:13:07 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Vivaz | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 5-4 | 13:13:08 | MOVE Board -> Board: Diana (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-4 | 13:13:08 | MOVE Board -> Board: Vi (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-4 | 13:13:08 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Vivaz | DA_18_Veigar | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-5 | 13:13:57 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 13:13:57 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Vivaz | DA_18_Veigar | 0.3700 |  |
| Jogador 2 | 5-5 | 13:13:58 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Vivaz | DA_18_Veigar | -0.4300 |  |
| Jogador 2 | 5-5 | 13:13:58 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 5 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-5 | 13:13:59 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 13:13:59 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Vivaz | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-5 | 13:14:00 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 13:14:00 | MOVE Board -> Board: Veigar (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-5 | 13:14:01 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Vivaz | DA_18_Veigar | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-6 | 13:15:16 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-6 | 13:15:17 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Vivaz | DA_18_Veigar | 1.0200 |  |
| Jogador 2 | 5-6 | 13:15:18 | MOVE Bench -> Board: Malphite (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Vivaz | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 5-6 | 13:15:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Vivaz | DA_18_Veigar | 0.8800 |  |
| Jogador 2 | 5-6 | 13:15:19 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Vivaz | DA_18_Veigar | 0.5100 |  |
| Jogador 2 | 5-6 | 13:15:19 | COMPROU: Lux (Lunar) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Vivaz | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 5-6 | 13:15:20 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-6 | 13:15:21 | MOVE Board -> Board: Malphite (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-6 | 13:15:21 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Vivaz | DA_18_Veigar | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-7 | 13:16:24 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Vi (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 5-7 | 13:16:25 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Vivaz | DA_18_Veigar | -0.6000 |  |
| Jogador 2 | 5-7 | 13:16:25 | COMPROU: Morgana (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 5-7 | 13:16:26 | VENDEU: Morgana (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Vivaz | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 5-7 | 13:16:26 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 5-7 | 13:16:27 | MOVE Board -> Board: Diana (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 5-7 | 13:16:27 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 5-7 | 13:16:28 | MOVE Bench -> Board: Lux (Lunar) (i:10.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 5-7 | 13:16:29 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 6-1 | 13:17:21 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 6-1 | 13:17:22 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Vivaz | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 6-1 | 13:17:22 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Vivaz | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 6-1 | 13:17:23 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Vivaz | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 6-1 | 13:17:23 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 6-1 | 13:17:23 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Vivaz | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 6-1 | 13:17:24 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Vivaz | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 6-1 | 13:17:25 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Vivaz | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 6-1 | 13:17:25 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Vivaz | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 6-2 | 13:18:18 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 6-2 | 13:18:18 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Vivaz | DA_18_Zyra | 0.9500 |  |
| Jogador 2 | 6-2 | 13:18:19 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Vivaz | DA_18_Zyra | 0.1000 |  |
| Jogador 2 | 6-2 | 13:18:19 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Vivaz | DA_18_Zyra | 0.0700 |  |
| Jogador 2 | 6-2 | 13:18:19 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Vivaz | DA_18_Zyra | 0.0600 |  |
| Jogador 2 | 6-2 | 13:18:20 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Vivaz | DA_18_Zyra | 0.0600 |  |
| Jogador 2 | 6-2 | 13:18:20 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 56 | 5 | Vivaz | DA_18_Zyra | 0.0600 |  |
| Jogador 2 | 6-2 | 13:18:21 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 52 | 5 | Vivaz | DA_18_Zyra | 0.0400 |  |
| Jogador 2 | 6-2 | 13:18:21 | MOVE Board -> Board: Vi (i:6.0) <-> Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 5 | Vivaz | DA_18_Zyra | 0.0000 |  |
| Jogador 2 | 6-3 | 13:19:15 | VENDEU: Zyra (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Vivaz | DA_18_Alune | -0.0900 |  |
| Jogador 2 | 6-3 | 13:19:15 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_18_Alune | 0.6300 |  |
| Jogador 2 | 6-3 | 13:19:16 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Alune | -0.0100 |  |
| Jogador 2 | 6-3 | 13:19:16 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_18_Alune | 0.1800 |  |
| Jogador 2 | 6-3 | 13:19:17 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Alune | -0.0300 |  |
| Jogador 2 | 6-3 | 13:19:19 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_18_Alune | 0.0800 |  |
| Jogador 2 | 6-3 | 13:19:19 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Alune | -0.0200 |  |
| Jogador 2 | 6-3 | 13:19:20 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_18_Alune | -0.0900 |  |
| Jogador 2 | 6-3 | 13:19:20 | MOVE Board -> Board: Malphite (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_18_Alune | 0.0000 |  |
| Jogador 2 | 6-4 | 13:20:16 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Vivaz | DA_18_Alune | -0.0200 |  |
| Jogador 2 | 6-4 | 13:20:16 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Vivaz | DA_18_Alune | 0.9400 |  |
| Jogador 2 | 6-4 | 13:20:17 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Vivaz | DA_18_Alune | -0.0400 |  |
| Jogador 2 | 6-4 | 13:20:17 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Vivaz | DA_18_Alune | 0.4200 |  |
| Jogador 2 | 6-4 | 13:20:18 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Vivaz | DA_18_Alune | -0.4300 |  |
| Jogador 2 | 6-4 | 13:20:18 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Vivaz | DA_18_Alune | 0.0900 |  |
| Jogador 2 | 6-4 | 13:20:18 | MOVE Board -> Board: Diana (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Vivaz | DA_18_Alune | 0.0000 |  |
| Jogador 2 | 6-4 | 13:20:19 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Vivaz | DA_18_Alune | -0.0200 |  |
| Jogador 2 | 6-4 | 13:20:19 | MOVE Board -> Board: Kobuko (i:2.0) <-> Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Vivaz | DA_18_Alune | -0.0100 |  |
| Jogador 3 | ? | 12:59:32 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 12:59:34 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 12:59:35 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 12:59:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 12:59:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 12:59:40 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 12:59:40 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 12:59:41 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 12:59:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 12:59:45 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 12:59:47 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 12:59:47 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 12:59:48 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 12:59:48 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 12:59:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 12:59:52 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 12:59:56 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 12:59:56 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 12:59:57 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 12:59:57 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 12:59:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 13:00:04 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 13:00:06 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 13:00:06 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 13:00:06 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 13:00:07 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-4 | 13:00:10 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 1-4 | 13:00:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-1 | 13:00:13 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 13:00:14 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 13:00:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 13:00:24 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 13:00:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 13:00:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 13:00:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 13:00:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 13:00:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-3 | 13:00:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 13:00:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 13:00:53 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-4 | 13:00:53 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.7100 |  |
| Jogador 3 | 2-4 | 13:00:54 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.4700 |  |
| Jogador 3 | 2-4 | 13:00:54 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-4 | 13:00:55 | MOVE Bench -> Board: Akali (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 2-4 | 13:00:55 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 2-4 | 13:00:56 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.6200 |  |
| Jogador 3 | 2-4 | 13:00:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-5 | 13:01:08 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.8700 |  |
| Jogador 3 | 2-5 | 13:01:08 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.4400 |  |
| Jogador 3 | 2-5 | 13:01:09 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.3600 |  |
| Jogador 3 | 2-5 | 13:01:09 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 13:01:10 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 13:01:10 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-5 | 13:01:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 13:01:24 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 2-6 | 13:01:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-6 | 13:01:25 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 13:01:26 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 2-6 | 13:01:26 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 13:01:27 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 13:01:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 13:01:43 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 2-7 | 13:01:43 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | -0.5900 |  |
| Jogador 3 | 2-7 | 13:01:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 2-7 | 13:01:44 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 2-7 | 13:01:45 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-7 | 13:01:45 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.4600 |  |
| Jogador 3 | 2-7 | 13:01:46 | MOVE Bench -> Board: Shen (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 2-7 | 13:01:46 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Devastador | DA_18_Akali_AD | -0.5300 |  |
| Jogador 3 | 2-7 | 13:01:47 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 3-1 | 13:02:03 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 3-1 | 13:02:04 | MOVE Bench -> Board: Vi (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 3-1 | 13:02:04 | MOVE Bench -> Board: Shen (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 3-1 | 13:02:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-2 | 13:02:26 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Devastador | DA_18_Akali_AD | 0.4200 |  |
| Jogador 3 | 3-2 | 13:02:27 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 13:02:27 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Devastador | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 3-2 | 13:02:28 | MOVE Bench -> Board: Sivir (i:8.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Devastador | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 3-2 | 13:02:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 2 | Devastador | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-2 | 13:02:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 13:02:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 13:02:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 2 | Devastador | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-2 | 13:02:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 13:02:52 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.6100 |  |
| Jogador 3 | 3-3 | 13:02:52 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-3 | 13:02:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.2000 |  |
| Jogador 3 | 3-3 | 13:02:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 13:02:54 | MOVE Board -> Board: Sivir (i:8.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 13:02:55 | MOVE Board -> Board: Diana (i:6.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 13:02:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 13:03:18 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 13:03:19 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_18_Akali_AD | 0.7400 |  |
| Jogador 3 | 3-4 | 13:03:20 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_18_Akali_AD | -0.0800 |  |
| Jogador 3 | 3-4 | 13:03:20 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Devastador | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 3-4 | 13:03:21 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 13:03:21 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 13:03:22 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-4 | 13:03:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 13:03:47 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | 0.0300 |  |
| Jogador 3 | 3-5 | 13:03:48 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 3-5 | 13:03:48 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-5 | 13:03:49 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Devastador | DA_18_Akali_AD | 0.7400 |  |
| Jogador 3 | 3-5 | 13:03:49 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 3-5 | 13:03:50 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 3-5 | 13:03:50 | MOVE Board -> Board: Sivir (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 13:03:51 | MOVE Board -> Board: Diana (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-5 | 13:03:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-6 | 13:04:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Devastador | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-6 | 13:04:18 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 3-6 | 13:04:18 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 13:04:19 | MOVE Board -> Board: Sivir (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 13:04:20 | MOVE Board -> Board: Diana (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 13:04:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-7 | 13:04:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Devastador | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Devastador | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 3-7 | 13:04:51 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Devastador | DA_18_Akali_AD | -0.5800 |  |
| Jogador 3 | 3-7 | 13:04:52 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Devastador | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 3 | 3-7 | 13:04:52 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 3 | 3-7 | 13:04:54 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Devastador | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 3 | 3-7 | 13:04:55 | MOVE Board -> Board: Camille (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Devastador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 13:04:55 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Devastador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 3-7 | 13:04:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Devastador | DA_KogMaw18_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-1 | 13:05:27 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 1 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-1 | 13:05:28 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Devastador | DA_18_Akali_AD | 0.3800 |  |
| Jogador 3 | 4-1 | 13:05:28 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Devastador | DA_18_Akali_AD | 0.4700 |  |
| Jogador 3 | 4-1 | 13:05:29 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Devastador | DA_18_Akali_AD | 0.2800 |  |
| Jogador 3 | 4-1 | 13:05:30 | MOVE Board -> Board: Camille (i:2.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 13:05:30 | MOVE Board -> Board: Sivir (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-1 | 13:05:31 | MOVE Board -> Board: Sivir (i:8.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-1 | 13:05:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Devastador | DA_18_Akali_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-2 | 13:06:05 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-2 | 13:06:05 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 13:06:06 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 13:06:07 | MOVE Board -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 13:06:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Devastador | DA_18_Akali_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-3 | 13:06:44 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-3 | 13:06:44 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-3 | 13:06:45 | MOVE Board -> Board: Akali (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 13:06:46 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-3 | 13:06:47 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-3 | 13:06:47 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Devastador | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | 4-3 | 13:06:48 | MOVE Board -> Board: Camille (i:2.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 13:06:48 | MOVE Board -> Board: Sivir (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-3 | 13:06:49 | MOVE Board -> Board: Sivir (i:8.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 13:07:27 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 13:07:28 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 4 | Devastador | DA_18_Akali_AD | 0.8800 |  |
| Jogador 3 | 4-4 | 13:07:28 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 4-4 | 13:07:29 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 4 | Devastador | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 4-4 | 13:07:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Devastador | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 4-4 | 13:07:30 | MOVE Board -> Board: Camille (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-4 | 13:07:30 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 13:07:31 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Devastador | DA_18_Akali_AD | -0.2100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-5 | 13:08:11 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 55 | 4 | Devastador | DA_18_Diana | 1.0200 |  |
| Jogador 3 | 4-5 | 13:08:12 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 54 | 4 | Devastador | DA_18_Diana | 0.4700 |  |
| Jogador 3 | 4-5 | 13:08:12 | MOVE Bench -> Board: Vi (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 54 | 4 | Devastador | DA_18_Diana | 0.4000 |  |
| Jogador 3 | 4-5 | 13:08:12 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Devastador | DA_18_Diana | 0.0700 |  |
| Jogador 3 | 4-5 | 13:08:13 | MOVE Board -> Board: Vi (i:12.0) <-> Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Devastador | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-5 | 13:08:14 | MOVE Board -> Board: Sivir (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Devastador | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 4-5 | 13:08:14 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Devastador | DA_18_Diana | -0.4400 |  |
| Jogador 3 | 4-6 | 13:08:53 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Devastador | DA_Vi18 | -0.7300 |  |
| Jogador 3 | 4-6 | 13:08:54 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Devastador | DA_Vi18 | 1.0700 |  |
| Jogador 3 | 4-6 | 13:08:54 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Devastador | DA_Vi18 | 0.7600 |  |
| Jogador 3 | 4-6 | 13:08:55 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Devastador | DA_Vi18 | 0.3800 |  |
| Jogador 3 | 4-6 | 13:08:55 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Camille (i:2.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Devastador | DA_Vi18 | 0.1600 |  |
| Jogador 3 | 4-6 | 13:08:55 | MOVE Board -> Board: Camille (i:2.0) <-> Vi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Devastador | DA_Vi18 | 0.0000 |  |
| Jogador 3 | 4-6 | 13:08:56 | MOVE Board -> Board: Vi (i:12.0) <-> Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Devastador | DA_Vi18 | -0.0100 |  |
| Jogador 3 | 4-6 | 13:08:56 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 59 | 5 | Devastador | DA_Vi18 | -0.0700 |  |
| Jogador 3 | 4-6 | 13:08:57 | VENDEU: Lobo Trevoguari (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Devastador | DA_Vi18 | -0.7200 |  |
| Jogador 3 | 4-7 | 13:09:37 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Devastador | DA_Vi18 | 0.9000 |  |
| Jogador 3 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Devastador | DA_Vi18 | 0.1400 |  |
| Jogador 3 | 4-7 | 13:09:38 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Devastador | DA_Vi18 | 0.1000 |  |
| Jogador 3 | 4-7 | 13:09:38 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Devastador | DA_Vi18 | -0.0200 |  |
| Jogador 3 | 4-7 | 13:09:39 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Devastador | DA_Vi18 | 0.4100 |  |
| Jogador 3 | 4-7 | 13:09:39 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Devastador | DA_Vi18 | -0.1200 |  |
| Jogador 3 | 4-7 | 13:09:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Devastador | DA_Vi18 | 0.0700 |  |
| Jogador 3 | 4-7 | 13:09:40 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Devastador | DA_Vi18 | -0.0700 |  |
| Jogador 3 | 4-7 | 13:09:41 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Devastador | DA_Vi18 | -0.0200 |  |
| Jogador 4 | ? | 12:59:32 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 12:59:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 12:59:35 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 12:59:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:59:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 12:59:40 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:59:40 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 12:59:41 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 12:59:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:59:45 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4700 |  |
| Jogador 4 | 1-2 | 12:59:47 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 12:59:47 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 12:59:48 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 12:59:48 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 12:59:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 12:59:56 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 12:59:56 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 12:59:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 13:00:04 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 13:00:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 13:00:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 13:00:10 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3900 |  |
| Jogador 4 | 2-1 | 13:00:13 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 13:00:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 13:00:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 13:00:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 13:00:24 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 13:00:25 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 13:00:25 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 13:00:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 13:00:26 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 13:00:27 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 13:00:27 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-2 | 13:00:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 13:00:36 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 13:00:37 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 13:00:37 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 13:00:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 13:00:39 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 13:00:39 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 13:00:40 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 13:00:40 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 13:00:41 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 4 | 2-4 | 13:00:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 13:00:53 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 13:00:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 13:00:54 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 2-4 | 13:00:54 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 2-4 | 13:00:55 | MOVE Bench -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-4 | 13:00:55 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 2-4 | 13:00:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 13:00:56 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 13:01:08 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 4 | 2-5 | 13:01:08 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 2-5 | 13:01:09 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 2-5 | 13:01:09 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 13:01:10 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-5 | 13:01:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-6 | 13:01:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 4 | 2-6 | 13:01:25 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 4 | 2-6 | 13:01:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 13:01:26 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 4 | 2-6 | 13:01:26 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 4 | 2-6 | 13:01:27 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 2-6 | 13:01:27 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 4 | 2-6 | 13:01:27 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-6 | 13:01:28 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 13:01:43 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 2-7 | 13:01:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 4 | 2-7 | 13:01:44 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 13:01:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 13:01:45 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 4 | 2-7 | 13:01:45 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 4 | 2-7 | 13:01:46 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 13:01:46 | MOVE Bench -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-7 | 13:01:47 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 4 | 3-1 | 13:02:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-1 | 13:02:04 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 4 | 3-1 | 13:02:04 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 13:02:05 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.6100 |  |
| Jogador 4 | 3-1 | 13:02:05 | MOVE Board -> Board: Yorick (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-1 | 13:02:06 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 3-1 | 13:02:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-2 | 13:02:26 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 4 | 3-2 | 13:02:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.7700 |  |
| Jogador 4 | 3-2 | 13:02:27 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 4 | 3-2 | 13:02:28 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 4 | 3-2 | 13:02:29 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 4 | 3-2 | 13:02:29 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 4 | 3-2 | 13:02:30 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-2 | 13:02:30 | MOVE Board -> Board: Yorick (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-2 | 13:02:31 | MOVE Board -> Board: Sejuani (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 3-3 | 13:02:52 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Florescer | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 4 | 3-3 | 13:02:52 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 3-3 | 13:02:53 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 3-3 | 13:02:54 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 13:02:54 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 3-3 | 13:02:55 | MOVE Board -> Board: Diana (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Florescer | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 4 | 3-3 | 13:02:55 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-3 | 13:02:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Florescer | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-4 | 13:03:18 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-4 | 13:03:19 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 4 | 3-4 | 13:03:20 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Florescer | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 4 | 3-4 | 13:03:20 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-4 | 13:03:21 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 3-4 | 13:03:21 | MOVE Board -> Board: Diana (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 13:03:22 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-4 | 13:03:22 | MOVE Board -> Board: Sejuani (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 4 | 3-4 | 13:03:23 | MOVE Board -> Board: Karma (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 13:03:47 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | 0.8500 |  |
| Jogador 4 | 3-5 | 13:03:48 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Florescer | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 4 | 3-5 | 13:03:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-5 | 13:03:49 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 4 | 3-5 | 13:03:49 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 13:03:50 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 13:03:50 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 13:03:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_KogMaw18_AD | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-6 | 13:04:18 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_KogMaw18_AD | 0.6600 |  |
| Jogador 4 | 3-6 | 13:04:18 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 3-6 | 13:04:18 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 4 | 3-6 | 13:04:19 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Florescer | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 4 | 3-6 | 13:04:20 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-6 | 13:04:20 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 13:04:21 | MOVE Board -> Board: Karma (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-6 | 13:04:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Florescer | DA_KogMaw18_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-7 | 13:04:50 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Florescer | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 4 | 3-7 | 13:04:51 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-7 | 13:04:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Florescer | DA_KogMaw18_AD | 0.8700 |  |
| Jogador 4 | 3-7 | 13:04:52 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-7 | 13:04:54 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Florescer | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 4 | 3-7 | 13:04:55 | MOVE Board -> Board: Diana (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 13:04:55 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-7 | 13:04:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Florescer | DA_KogMaw18_AD | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-1 | 13:05:27 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 3 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 4-1 | 13:05:28 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 3 | Florescer | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 4 | 4-1 | 13:05:28 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 3 | Florescer | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 4 | 4-1 | 13:05:29 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 49 | 3 | Florescer | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 4 | 4-1 | 13:05:30 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 3 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 4 | 4-1 | 13:05:30 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 3 | Florescer | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 4 | 4-1 | 13:05:31 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 3 | Florescer | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 4 | 4-1 | 13:05:31 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 49 | 3 | Florescer | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 4 | 4-1 | 13:05:32 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 49 | 3 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 13:06:05 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 4 | Florescer | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 4 | 4-2 | 13:06:05 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 4 | Florescer | DA_KogMaw18_AD | 0.9300 |  |
| Jogador 4 | 4-2 | 13:06:06 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 4 | Florescer | DA_KogMaw18_AD | -0.6400 |  |
| Jogador 4 | 4-2 | 13:06:07 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 4 | Florescer | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 4 | 4-2 | 13:06:07 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 4 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 4-2 | 13:06:08 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Florescer | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 4-2 | 13:06:08 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 4 | Florescer | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 4 | 4-2 | 13:06:09 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 13:06:09 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Florescer | DA_KogMaw18_AD | -0.7500 |  |
| Jogador 4 | 4-3 | 13:06:44 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Florescer | DA_KogMaw18_AD | -0.5200 |  |
| Jogador 4 | 4-3 | 13:06:44 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Florescer | DA_KogMaw18_AD | 1.1100 |  |
| Jogador 4 | 4-3 | 13:06:45 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Florescer | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 4 | 4-3 | 13:06:46 | MOVE Bench -> Board: Rengar (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Florescer | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 4 | 4-3 | 13:06:47 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Florescer | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 4 | 4-3 | 13:06:47 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 4 | 4-3 | 13:06:48 | MOVE Board -> Board: Rengar (i:6.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-3 | 13:06:48 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 4-3 | 13:06:49 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.4900 |  |
| Jogador 4 | 4-4 | 13:07:27 | VENDEU: Yunara (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Florescer | DA_KogMaw18_AD | -0.7400 |  |
| Jogador 4 | 4-4 | 13:07:28 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Florescer | DA_KogMaw18_AD | 0.5600 |  |
| Jogador 4 | 4-4 | 13:07:28 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 13:07:29 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Florescer | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 4 | 4-4 | 13:07:29 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 4-4 | 13:07:30 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 4-4 | 13:07:30 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 13:07:31 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 4-4 | 13:07:32 | MOVE Bench -> Board: Sivir (i:8.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Florescer | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 4 | 4-5 | 13:08:11 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-5 | 13:08:12 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Florescer | DA_KogMaw18_AD | 1.1000 |  |
| Jogador 4 | 4-5 | 13:08:12 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Florescer | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 4 | 4-5 | 13:08:12 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Florescer | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 4 | 4-5 | 13:08:13 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Florescer | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 4 | 4-5 | 13:08:14 | VENDEU: Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Florescer | DA_18_Yorick | -0.7300 |  |
| Jogador 4 | 4-5 | 13:08:14 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Rengar (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Florescer | DA_18_Yorick | 0.1000 |  |
| Jogador 4 | 4-5 | 13:08:15 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Rengar (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Florescer | DA_18_Yorick | 0.0700 |  |
| Jogador 4 | 4-5 | 13:08:15 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Florescer | DA_18_Yorick | 0.0300 |  |
| Jogador 4 | 4-6 | 13:08:53 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Florescer | DA_18_Yorick | -0.0200 |  |
| Jogador 4 | 4-6 | 13:08:54 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Florescer | DA_18_Yorick | 0.9200 |  |
| Jogador 4 | 4-6 | 13:08:54 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-6 | 13:08:55 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Florescer | DA_18_Diana | 1.1000 |  |
| Jogador 4 | 4-6 | 13:08:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Florescer | DA_18_Diana | 0.2300 |  |
| Jogador 4 | 4-6 | 13:08:55 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Florescer | DA_18_Diana | 0.1100 |  |
| Jogador 4 | 4-6 | 13:08:56 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Florescer | DA_18_Diana | 0.0000 |  |
| Jogador 4 | 4-6 | 13:08:56 | MOVE Board -> Board: Rengar (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Florescer | DA_18_Diana | -0.0200 |  |
| Jogador 4 | 4-6 | 13:08:57 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Florescer | DA_18_Diana | -0.5300 |  |
| Jogador 4 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Florescer | DA_18_Diana | 0.1500 |  |
| Jogador 4 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Florescer | DA_18_Diana | 0.1000 |  |
| Jogador 4 | 4-7 | 13:09:38 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Florescer | DA_18_Yorick | -0.7500 |  |
| Jogador 4 | 4-7 | 13:09:38 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Florescer | DA_18_Yorick | 0.2300 |  |
| Jogador 4 | 4-7 | 13:09:39 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Florescer | DA_18_Yorick | -0.0600 |  |
| Jogador 4 | 4-7 | 13:09:39 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Florescer | DA_18_Yorick | 0.1800 |  |
| Jogador 4 | 4-7 | 13:09:40 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Florescer | DA_18_Yorick | -0.0200 |  |
| Jogador 4 | 4-7 | 13:09:40 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Florescer | DA_18_Yorick | 0.0600 |  |
| Jogador 4 | 4-7 | 13:09:41 | VENDEU: Alistar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 5-1 | 13:10:23 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Florescer | DA_18_Yorick | 0.4100 |  |
| Jogador 4 | 5-1 | 13:10:24 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Florescer | DA_18_Yorick | -0.0300 |  |
| Jogador 4 | 5-1 | 13:10:24 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Florescer | DA_18_Yorick | 0.9300 |  |
| Jogador 4 | 5-1 | 13:10:25 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Florescer | DA_18_Yorick | -0.0500 |  |
| Jogador 4 | 5-1 | 13:10:25 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Florescer | DA_18_Yorick | 0.0300 |  |
| Jogador 4 | 5-1 | 13:10:26 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Florescer | DA_18_Yorick | 0.0800 |  |
| Jogador 4 | 5-1 | 13:10:26 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Florescer | DA_18_Yorick | -0.7000 |  |
| Jogador 4 | 5-1 | 13:10:27 | MOVE Bench -> Board: Sivir (i:8.0) <-> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Florescer | DA_18_Yorick | -0.1100 |  |
| Jogador 4 | 5-1 | 13:10:27 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Florescer | DA_18_Yorick | -0.6000 |  |
| Jogador 5 | ? | 12:59:32 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 12:59:34 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 12:59:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 12:59:39 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 12:59:40 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 12:59:40 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 12:59:41 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 12:59:42 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 12:59:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 12:59:45 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 12:59:47 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 12:59:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 12:59:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 12:59:56 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 12:59:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 13:00:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 13:00:06 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 13:00:06 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 13:00:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 13:00:13 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 13:00:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 13:00:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 13:00:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 13:00:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 13:00:25 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 13:00:25 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 13:00:26 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 13:00:26 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 13:00:27 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 13:00:27 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-2 | 13:00:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 13:00:36 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 13:00:37 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 13:00:37 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 13:00:38 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 13:00:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 13:00:39 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 13:00:40 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 13:00:40 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | 0.1900 |  |
| Jogador 5 | 2-3 | 13:00:41 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.1800 |  |
| Jogador 5 | 2-4 | 13:00:52 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2700 |  |
| Jogador 5 | 2-4 | 13:00:53 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 13:00:53 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-4 | 13:00:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 13:00:54 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-4 | 13:00:55 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.4100 |  |
| Jogador 5 | 2-4 | 13:00:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 13:00:56 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1000 |  |
| Jogador 5 | 2-4 | 13:00:56 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 13:01:08 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0200 |  |
| Jogador 5 | 2-5 | 13:01:08 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 2-5 | 13:01:09 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 13:01:09 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-5 | 13:01:10 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 2-5 | 13:01:10 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-5 | 13:01:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-5 | 13:01:11 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3300 |  |
| Jogador 5 | 2-5 | 13:01:12 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.4900 |  |
| Jogador 5 | 2-6 | 13:01:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | 1.1200 |  |
| Jogador 5 | 2-6 | 13:01:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-6 | 13:01:25 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0200 |  |
| Jogador 5 | 2-6 | 13:01:26 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.6000 |  |
| Jogador 5 | 2-6 | 13:01:26 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1700 |  |
| Jogador 5 | 2-6 | 13:01:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-6 | 13:01:27 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.6300 |  |
| Jogador 5 | 2-6 | 13:01:27 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-6 | 13:01:28 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3600 |  |
| Jogador 5 | 2-7 | 13:01:43 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Yunara | 0.6800 |  |
| Jogador 5 | 2-7 | 13:01:43 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Yunara | 0.2100 |  |
| Jogador 5 | 2-7 | 13:01:44 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Yunara | 0.1500 |  |
| Jogador 5 | 2-7 | 13:01:44 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Yunara | 0.1300 |  |
| Jogador 5 | 2-7 | 13:01:45 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | -0.2500 |  |
| Jogador 5 | 2-7 | 13:01:45 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | 0.5600 |  |
| Jogador 5 | 2-7 | 13:01:46 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 2-7 | 13:01:46 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | -0.0100 |  |
| Jogador 5 | 2-7 | 13:01:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 3-1 | 13:02:03 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Yunara | 0.7200 |  |
| Jogador 5 | 3-1 | 13:02:04 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Yunara | 0.1200 |  |
| Jogador 5 | 3-1 | 13:02:04 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Tristana | -0.1400 |  |
| Jogador 5 | 3-1 | 13:02:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-1 | 13:02:05 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 3-1 | 13:02:06 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-1 | 13:02:06 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Tristana | -0.4100 |  |
| Jogador 5 | 3-1 | 13:02:07 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 3-1 | 13:02:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-2 | 13:02:26 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-2 | 13:02:27 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Tristana | 0.7300 |  |
| Jogador 5 | 3-2 | 13:02:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-2 | 13:02:28 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.5700 |  |
| Jogador 5 | 3-2 | 13:02:29 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Tristana | -0.0900 |  |
| Jogador 5 | 3-2 | 13:02:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-2 | 13:02:30 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 3-2 | 13:02:30 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 3-2 | 13:02:31 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 3-3 | 13:02:52 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Tristana | 0.8100 |  |
| Jogador 5 | 3-3 | 13:02:52 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-3 | 13:02:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | 0.0600 |  |
| Jogador 5 | 3-3 | 13:02:54 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-3 | 13:02:54 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.3600 |  |
| Jogador 5 | 3-3 | 13:02:55 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | 0.5700 |  |
| Jogador 5 | 3-3 | 13:02:55 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-3 | 13:02:56 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-3 | 13:02:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-4 | 13:03:18 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Tristana | 0.2900 |  |
| Jogador 5 | 3-4 | 13:03:19 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | 0.1700 |  |
| Jogador 5 | 3-4 | 13:03:20 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-4 | 13:03:20 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-4 | 13:03:21 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 3-4 | 13:03:21 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 3-4 | 13:03:22 | COMPROU: Morgana (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 3-4 | 13:03:22 | MOVE Board -> Board: Veigar (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-4 | 13:03:23 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-5 | 13:03:47 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.7800 |  |
| Jogador 5 | 3-5 | 13:03:48 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 5 | 3-5 | 13:03:48 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.2300 |  |
| Jogador 5 | 3-5 | 13:03:49 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 5 | 3-5 | 13:03:49 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 5 | 3-5 | 13:03:50 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 3-5 | 13:03:50 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 5 | 3-5 | 13:03:51 | VENDEU: Morgana (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 3-5 | 13:03:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 5 | 3-6 | 13:04:18 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 5 | 3-6 | 13:04:18 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1700 |  |
| Jogador 5 | 3-6 | 13:04:18 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-6 | 13:04:19 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 3-6 | 13:04:20 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-6 | 13:04:20 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 3-6 | 13:04:21 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 5 | 3-6 | 13:04:21 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-6 | 13:04:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.4900 |  |
| Jogador 5 | 3-7 | 13:04:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 5 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 5 | 3-7 | 13:04:51 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 5 | 3-7 | 13:04:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 5 | 3-7 | 13:04:52 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.4300 |  |
| Jogador 5 | 3-7 | 13:04:54 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Rammus | 0.7400 |  |
| Jogador 5 | 3-7 | 13:04:55 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.5300 |  |
| Jogador 5 | 3-7 | 13:04:55 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 5 | 3-7 | 13:04:55 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.3700 |  |
| Jogador 5 | 4-1 | 13:05:27 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.8400 |  |
| Jogador 5 | 4-1 | 13:05:28 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.8700 |  |
| Jogador 5 | 4-1 | 13:05:28 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.7000 |  |
| Jogador 5 | 4-1 | 13:05:29 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.5900 |  |
| Jogador 5 | 4-1 | 13:05:30 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.2100 |  |
| Jogador 5 | 4-1 | 13:05:30 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-1 | 13:05:31 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 5 | 4-1 | 13:05:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-2 | 13:06:05 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.3100 |  |
| Jogador 5 | 4-2 | 13:06:05 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.5800 |  |
| Jogador 5 | 4-2 | 13:06:06 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.1800 |  |
| Jogador 5 | 4-2 | 13:06:07 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 4-2 | 13:06:07 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.1900 |  |
| Jogador 5 | 4-2 | 13:06:08 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 4-2 | 13:06:08 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.3700 |  |
| Jogador 5 | 4-2 | 13:06:09 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.4800 |  |
| Jogador 5 | 4-2 | 13:06:09 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.5500 |  |
| Jogador 5 | 4-3 | 13:06:44 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.9200 |  |
| Jogador 5 | 4-3 | 13:06:44 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 5 | 4-3 | 13:06:45 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1300 |  |
| Jogador 5 | 4-3 | 13:06:46 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1200 |  |
| Jogador 5 | 4-3 | 13:06:47 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 5 | 4-3 | 13:06:47 | VENDEU: Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.5400 |  |
| Jogador 5 | 4-3 | 13:06:48 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Mamãe Bicuda (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1400 |  |
| Jogador 5 | 4-3 | 13:06:48 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Mamãe Bicuda (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1200 |  |
| Jogador 5 | 4-3 | 13:06:49 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-4 | 13:07:27 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.6000 |  |
| Jogador 5 | 4-4 | 13:07:28 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1700 |  |
| Jogador 5 | 4-4 | 13:07:28 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 5 | 4-4 | 13:07:29 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 5 | 4-4 | 13:07:29 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 5 | 4-4 | 13:07:30 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1300 |  |
| Jogador 5 | 4-4 | 13:07:30 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-4 | 13:07:31 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 5 | 4-4 | 13:07:32 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.6000 |  |
| Jogador 5 | 4-5 | 13:08:11 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.3300 |  |
| Jogador 5 | 4-5 | 13:08:12 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 5 | 4-5 | 13:08:12 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.2100 |  |
| Jogador 5 | 4-5 | 13:08:12 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1300 |  |
| Jogador 5 | 4-5 | 13:08:13 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 5 | 4-5 | 13:08:14 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.2200 |  |
| Jogador 5 | 4-5 | 13:08:14 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 4-5 | 13:08:15 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | -0.2200 |  |
| Jogador 5 | 4-5 | 13:08:15 | MOVE Board -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-6 | 13:08:53 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 4-6 | 13:08:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 5 | 4-6 | 13:08:54 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 5 | 4-6 | 13:08:55 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Espinhos Negros | DA_Sentinel18 | -0.5200 |  |
| Jogador 5 | 4-6 | 13:08:55 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Espinhos Negros | DA_Sentinel18 | 0.0300 |  |
| Jogador 5 | 4-6 | 13:08:55 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 4-6 | 13:08:56 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Espinhos Negros | DA_Sentinel18 | -0.2000 |  |
| Jogador 5 | 4-6 | 13:08:56 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 4-6 | 13:08:57 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Espinhos Negros | DA_Sentinel18 | -0.3500 |  |
| Jogador 5 | 4-7 | 13:09:37 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Espinhos Negros | DA_Sentinel18 | 0.3600 |  |
| Jogador 5 | 4-7 | 13:09:37 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 4-7 | 13:09:38 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Espinhos Negros | DA_Sentinel18 | 0.1100 |  |
| Jogador 5 | 4-7 | 13:09:38 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Espinhos Negros | DA_Sentinel18 | 0.1100 |  |
| Jogador 5 | 4-7 | 13:09:39 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 4-7 | 13:09:39 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0200 |  |
| Jogador 5 | 4-7 | 13:09:40 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 4-7 | 13:09:40 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0500 |  |
| Jogador 5 | 4-7 | 13:09:41 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0100 |  |
| Jogador 5 | 5-1 | 13:10:23 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Espinhos Negros | DA_Sentinel18 | 0.1400 |  |
| Jogador 5 | 5-1 | 13:10:24 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0400 |  |
| Jogador 5 | 5-1 | 13:10:24 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1200 |  |
| Jogador 5 | 5-1 | 13:10:25 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Espinhos Negros | DA_Sentinel18 | 0.4700 |  |
| Jogador 5 | 5-1 | 13:10:25 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0400 |  |
| Jogador 5 | 5-1 | 13:10:26 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-1 | 13:10:26 | MOVE Board -> Board: Yorick (i:2.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-1 | 13:10:27 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-2 | 13:11:15 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-2 | 13:11:15 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Espinhos Negros | DA_Sentinel18 | 0.9000 |  |
| Jogador 5 | 5-2 | 13:11:16 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-2 | 13:11:16 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1400 |  |
| Jogador 5 | 5-2 | 13:11:17 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-2 | 13:11:17 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1400 |  |
| Jogador 5 | 5-2 | 13:11:18 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-2 | 13:11:19 | MOVE Board -> Board: Veigar (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-2 | 13:11:19 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-3 | 13:12:10 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-3 | 13:12:11 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Espinhos Negros | DA_CrimsonRaptor18 | 1.0200 |  |
| Jogador 5 | 5-3 | 13:12:13 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 94 | 5 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 5 | 5-3 | 13:12:14 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Espinhos Negros | DA_18_Ashe | -0.6000 |  |
| Jogador 5 | 5-3 | 13:12:14 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Fiddlesticks (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Espinhos Negros | DA_18_Ashe | 0.1300 |  |
| Jogador 5 | 5-3 | 13:12:15 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Fiddlesticks (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Espinhos Negros | DA_18_Ashe | 0.0500 |  |
| Jogador 5 | 5-3 | 13:12:15 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Fiddlesticks (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Espinhos Negros | DA_18_Ashe | 0.1300 |  |
| Jogador 5 | 5-3 | 13:12:15 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Espinhos Negros | DA_18_Ashe | 0.5100 |  |
| Jogador 5 | 5-3 | 13:12:16 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Espinhos Negros | DA_18_Ashe | -0.0100 |  |
| Jogador 5 | 5-4 | 13:13:05 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Espinhos Negros | DA_18_Ashe | 0.0100 |  |
| Jogador 5 | 5-4 | 13:13:05 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Espinhos Negros | DA_18_Ashe | 0.0100 |  |
| Jogador 5 | 5-4 | 13:13:06 | MOVE Board -> Board: Azir (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Espinhos Negros | DA_18_Ashe | 0.0000 |  |
| Jogador 5 | 5-4 | 13:13:06 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Espinhos Negros | DA_18_Ashe | -0.0100 |  |
| Jogador 5 | 5-4 | 13:13:07 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Espinhos Negros | DA_18_Ashe | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-5 | 13:13:57 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 123 | 5 | Espinhos Negros | DA_18_Ashe | -0.0100 |  |
| Jogador 5 | 5-5 | 13:13:57 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 120 | 5 | Espinhos Negros | DA_18_Ashe | 0.8700 |  |
| Jogador 5 | 5-5 | 13:13:58 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 122 | 5 | Espinhos Negros | DA_18_Ashe | -0.0100 |  |
| Jogador 5 | 5-5 | 13:13:58 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 120 | 5 | Espinhos Negros | DA_18_Ashe | 0.7700 |  |
| Jogador 5 | 5-5 | 13:13:59 | VENDEU: Ashe (i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 125 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-5 | 13:13:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 123 | 5 | Espinhos Negros | DA_Sentinel18 | 0.3700 |  |
| Jogador 5 | 5-5 | 13:14:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 123 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-5 | 13:14:00 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 123 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-5 | 13:14:01 | MOVE Board -> Board: Veigar (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 123 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0200 |  |
| Jogador 5 | 5-6 | 13:15:16 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1200 |  |
| Jogador 5 | 5-6 | 13:15:17 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-6 | 13:15:18 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0200 |  |
| Jogador 5 | 5-6 | 13:15:18 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0100 |  |
| Jogador 5 | 5-6 | 13:15:19 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0200 |  |
| Jogador 5 | 5-6 | 13:15:19 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0100 |  |
| Jogador 5 | 5-6 | 13:15:20 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-6 | 13:15:21 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-6 | 13:15:21 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 5-7 | 13:16:24 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Aronguejo (i:4.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 143 | 5 | Espinhos Negros | DA_Sentinel18 | 0.1100 |  |
| Jogador 5 | 5-7 | 13:16:25 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-7 | 13:16:25 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 141 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0300 |  |
| Jogador 5 | 5-7 | 13:16:26 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0200 |  |
| Jogador 5 | 5-7 | 13:16:26 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 141 | 5 | Espinhos Negros | DA_Sentinel18 | -0.2300 |  |
| Jogador 5 | 5-7 | 13:16:27 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-7 | 13:16:27 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 143 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0100 |  |
| Jogador 5 | 5-7 | 13:16:28 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0200 |  |
| Jogador 5 | 5-7 | 13:16:29 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 143 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0200 |  |
| Jogador 5 | 6-1 | 13:17:21 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 6-1 | 13:17:22 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Espinhos Negros | DA_18_Azir | 1.1100 |  |
| Jogador 5 | 6-1 | 13:17:22 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Espinhos Negros | DA_18_Azir | -0.1700 |  |
| Jogador 5 | 6-1 | 13:17:23 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Espinhos Negros | DA_18_Azir | 0.5600 |  |
| Jogador 5 | 6-1 | 13:17:23 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Espinhos Negros | DA_18_Azir | 0.0700 |  |
| Jogador 5 | 6-1 | 13:17:23 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Espinhos Negros | DA_18_Azir | -0.0700 |  |
| Jogador 5 | 6-1 | 13:17:24 | VENDEU: Azir (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.7000 |  |
| Jogador 5 | 6-1 | 13:17:25 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.5200 |  |
| Jogador 5 | 6-1 | 13:17:25 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0200 |  |
| Jogador 5 | 6-2 | 13:18:18 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | 1.1000 |  |
| Jogador 5 | 6-2 | 13:18:18 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0400 |  |
| Jogador 5 | 6-2 | 13:18:19 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0700 |  |
| Jogador 5 | 6-2 | 13:18:19 | VENDEU: Aronguejo (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.7400 |  |
| Jogador 5 | 6-2 | 13:18:19 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Rek'Sai (i:2.0) (tabuleiro slot 23) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.1400 |  |
| Jogador 5 | 6-2 | 13:18:20 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Rek'Sai (i:2.0) (tabuleiro slot 23) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0900 |  |
| Jogador 5 | 6-2 | 13:18:20 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | 0.0400 |  |
| Jogador 5 | 6-2 | 13:18:21 | MOVE Bench -> Board: Vi (i:6.0) <-> Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.3900 |  |
| Jogador 5 | 6-2 | 13:18:21 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Espinhos Negros | DA_18_Lux_Sunbeam | -0.0200 |  |
| Jogador 6 | ? | 12:59:32 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 12:59:34 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 12:59:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 12:59:39 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 12:59:40 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 12:59:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 12:59:45 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 12:59:47 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 12:59:47 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 12:59:48 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 12:59:48 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 12:59:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 12:59:52 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5800 |  |
| Jogador 6 | 1-3 | 12:59:56 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0200 |  |
| Jogador 6 | 1-3 | 12:59:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 13:00:04 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 13:00:05 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 13:00:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 13:00:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 13:00:10 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0900 |  |
| Jogador 6 | 2-1 | 13:00:13 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 13:00:14 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 13:00:14 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 13:00:15 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 13:00:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 13:00:24 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 13:00:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 13:00:25 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 13:00:25 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 13:00:26 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 13:00:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 13:00:36 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 13:00:37 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 13:00:37 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 2-3 | 13:00:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 13:00:39 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 13:00:39 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 13:00:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 13:00:40 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-3 | 13:00:41 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-4 | 13:00:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 2-4 | 13:00:53 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-4 | 13:00:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 13:00:54 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -0.4500 |  |
| Jogador 6 | 2-4 | 13:00:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 13:00:55 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-4 | 13:00:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 2-4 | 13:00:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 2-4 | 13:00:56 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Yorick | -0.6300 |  |
| Jogador 6 | 2-5 | 13:01:08 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 13:01:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 2-5 | 13:01:09 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Yorick | -0.1900 |  |
| Jogador 6 | 2-5 | 13:01:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 2-5 | 13:01:10 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 2-5 | 13:01:10 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | -1.0200 |  |
| Jogador 6 | 2-5 | 13:01:11 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.1600 |  |
| Jogador 6 | 2-5 | 13:01:11 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.6000 |  |
| Jogador 6 | 2-5 | 13:01:12 | MOVE Board -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-6 | 13:01:24 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 6 | 2-6 | 13:01:25 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 6 | 2-6 | 13:01:25 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 6 | 2-6 | 13:01:26 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-6 | 13:01:26 | MOVE Board -> Board: Cascalho (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 6 | 2-6 | 13:01:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-7 | 13:01:43 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 6 | 2-7 | 13:01:43 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 6 | 2-7 | 13:01:44 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 6 | 2-7 | 13:01:44 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 6 | 2-7 | 13:01:45 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 6 | 2-7 | 13:01:45 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 2-7 | 13:01:46 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 6 | 2-7 | 13:01:46 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 6 | 2-7 | 13:01:47 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_Fiddlesticks18 | -0.3100 |  |
| Jogador 6 | 3-1 | 13:02:03 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 6 | 3-1 | 13:02:04 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Feérico | DA_Fiddlesticks18 | 0.8100 |  |
| Jogador 6 | 3-1 | 13:02:04 | MOVE Bench -> Board: Cascalho (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Feérico | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 6 | 3-1 | 13:02:05 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Feérico | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-1 | 13:02:05 | MOVE Bench -> Board: Alistar (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Feérico | DA_Fiddlesticks18 | -0.2800 |  |
| Jogador 6 | 3-1 | 13:02:06 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Feérico | DA_Fiddlesticks18 | 0.2200 |  |
| Jogador 6 | 3-1 | 13:02:06 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Feérico | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 6 | 3-1 | 13:02:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Feérico | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 6 | 3-1 | 13:02:07 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Feérico | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 6 | 3-2 | 13:02:26 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 6 | 3-2 | 13:02:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Feérico | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 6 | 3-2 | 13:02:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Feérico | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 6 | 3-2 | 13:02:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | Feérico | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 6 | 3-2 | 13:02:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Feérico | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 6 | 3-2 | 13:02:29 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Feérico | DA_Fiddlesticks18 | -0.6300 |  |
| Jogador 6 | 3-2 | 13:02:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 1 | Feérico | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 6 | 3-2 | 13:02:30 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 1 | Feérico | DA_Fiddlesticks18 | 0.3800 |  |
| Jogador 6 | 3-2 | 13:02:31 | MOVE Board -> Board: Rammus (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 1 | Feérico | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 6 | 3-3 | 13:02:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.2800 |  |
| Jogador 6 | 3-3 | 13:02:52 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 6 | 3-3 | 13:02:53 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-3 | 13:02:54 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 6 | 3-3 | 13:02:54 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-3 | 13:02:55 | MOVE Board -> Board: Cascalho (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 6 | 3-3 | 13:02:55 | MOVE Board -> Board: Rammus (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 6 | 3-3 | 13:02:56 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 6 | 3-3 | 13:02:56 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-4 | 13:03:18 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.8000 |  |
| Jogador 6 | 3-4 | 13:03:19 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.5000 |  |
| Jogador 6 | 3-4 | 13:03:20 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 6 | 3-4 | 13:03:20 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 6 | 3-4 | 13:03:21 | MOVE Board -> Board: Vi (i:6.0) <-> Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 3-4 | 13:03:21 | MOVE Board -> Board: Cascalho (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-4 | 13:03:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-5 | 13:03:47 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 6 | 3-5 | 13:03:48 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | -0.1400 |  |
| Jogador 6 | 3-5 | 13:03:48 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-5 | 13:03:49 | MOVE Board -> Board: Xayah (i:2.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-5 | 13:03:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-6 | 13:04:18 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 6 | 3-6 | 13:04:18 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 6 | 3-6 | 13:04:18 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-6 | 13:04:19 | COMPROU: Gnar (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_GnarSmall | 0.2100 |  |
| Jogador 6 | 3-6 | 13:04:20 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-6 | 13:04:20 | MOVE Board -> Board: Cascalho (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-6 | 13:04:21 | MOVE Board -> Board: Xayah (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-6 | 13:04:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 13:04:50 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_GnarSmall | 0.2500 |  |
| Jogador 6 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_GnarSmall | 0.1900 |  |
| Jogador 6 | 3-7 | 13:04:51 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_GnarSmall | 0.0100 |  |
| Jogador 6 | 3-7 | 13:04:52 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_GnarSmall | 0.6300 |  |
| Jogador 6 | 3-7 | 13:04:52 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 13:04:54 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_GnarSmall | 0.6800 |  |
| Jogador 6 | 3-7 | 13:04:55 | MOVE Bench -> Board: Rammus (i:12.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_GnarSmall | 0.4000 |  |
| Jogador 6 | 3-7 | 13:04:55 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 3-7 | 13:04:55 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_GnarSmall | 0.0100 |  |
| Jogador 6 | 4-1 | 13:05:27 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-1 | 13:05:28 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_GnarSmall | 0.2000 |  |
| Jogador 6 | 4-1 | 13:05:28 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-1 | 13:05:29 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_GnarSmall | -0.2000 |  |
| Jogador 6 | 4-1 | 13:05:30 | MOVE Board -> Board: Rammus (i:12.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-1 | 13:05:30 | MOVE Board -> Board: Vi (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-1 | 13:05:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 13:06:05 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_GnarSmall | -0.0400 |  |
| Jogador 6 | 4-2 | 13:06:05 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_18_GnarSmall | 0.7500 |  |
| Jogador 6 | 4-2 | 13:06:06 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 13:06:07 | MOVE Bench -> Board: Alistar (i:8.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_GnarSmall | -0.4000 |  |
| Jogador 6 | 4-2 | 13:06:07 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-2 | 13:06:08 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-2 | 13:06:08 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Feérico | DA_18_GnarSmall | 0.5700 |  |
| Jogador 6 | 4-2 | 13:06:09 | COMPROU: Kobuko (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Feérico | DA_18_GnarSmall | -0.0600 |  |
| Jogador 6 | 4-2 | 13:06:09 | MOVE Board -> Board: Alistar (i:8.0) <-> Cascalho (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Feérico | DA_18_GnarSmall | -0.0600 |  |
| Jogador 6 | 4-3 | 13:06:44 | VENDEU: Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Feérico | DA_18_GnarSmall | 0.0700 |  |
| Jogador 6 | 4-3 | 13:06:44 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Feérico | DA_18_GnarSmall | 0.1500 |  |
| Jogador 6 | 4-3 | 13:06:45 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 13:06:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_GnarSmall | 0.2200 |  |
| Jogador 6 | 4-3 | 13:06:47 | MOVE Board -> Board: Cascalho (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-3 | 13:06:47 | MOVE Board -> Board: Xayah (i:2.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_GnarSmall | 0.0200 |  |
| Jogador 6 | 4-3 | 13:06:48 | MOVE Board -> Board: Alistar (i:8.0) <-> Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 13:06:48 | MOVE Board -> Board: Rammus (i:12.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 13:06:49 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_GnarSmall | -0.0300 |  |
| Jogador 6 | 4-4 | 13:07:27 | VENDEU: Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 13:07:28 | COMPROU: Varus (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Feérico | DA_18_GnarSmall | 0.2200 |  |
| Jogador 6 | 4-4 | 13:07:28 | MOVE Board -> Board: Vi (i:6.0) <-> Cascalho (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 13:07:29 | MOVE Board -> Board: Cascalho (i:4.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Feérico | DA_18_GnarSmall | -0.0300 |  |
| Jogador 6 | 4-4 | 13:07:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Feérico | DA_18_GnarSmall | -0.0300 |  |
| Jogador 6 | 4-5 | 13:08:11 | VENDEU: Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Feérico | DA_18_GnarSmall | -0.0300 |  |
| Jogador 6 | 4-5 | 13:08:12 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Feérico | DA_18_GnarSmall | 0.2500 |  |
| Jogador 6 | 4-5 | 13:08:12 | MOVE Board -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Feérico | DA_18_GnarSmall | -0.0400 |  |
| Jogador 6 | 4-5 | 13:08:12 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-5 | 13:08:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Feérico | DA_18_GnarSmall | -0.0400 |  |
| Jogador 6 | 4-6 | 13:08:53 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-6 | 13:08:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Feérico | DA_18_GnarSmall | 0.8600 |  |
| Jogador 6 | 4-6 | 13:08:54 | VENDEU: Gnar (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Feérico | DA_18_Rammus | -0.0400 |  |
| Jogador 6 | 4-6 | 13:08:55 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Feérico | DA_18_Rammus | 0.2000 |  |
| Jogador 6 | 4-6 | 13:08:55 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Feérico | DA_18_Rammus | -0.0400 |  |
| Jogador 6 | 4-6 | 13:08:55 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Feérico | DA_18_Rammus | 0.0400 |  |
| Jogador 6 | 4-6 | 13:08:56 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-6 | 13:08:56 | MOVE Board -> Board: Xayah (i:2.0) <-> Alistar (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Feérico | DA_18_Rammus | 0.0300 |  |
| Jogador 6 | 4-6 | 13:08:57 | MOVE Board -> Board: Alistar (i:8.0) <-> Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Feérico | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Rammus | 0.1500 |  |
| Jogador 6 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Rammus | 0.1200 |  |
| Jogador 6 | 4-7 | 13:09:38 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Feérico | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 4-7 | 13:09:38 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Rammus | 0.9000 |  |
| Jogador 6 | 4-7 | 13:09:39 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Rammus | -0.5900 |  |
| Jogador 6 | 4-7 | 13:09:39 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Feérico | DA_18_Rammus | 0.1400 |  |
| Jogador 6 | 4-7 | 13:09:40 | MOVE Board -> Board: Rammus (i:12.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-7 | 13:09:40 | MOVE Board -> Board: Vi (i:6.0) <-> Cascalho (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Feérico | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 4-7 | 13:09:41 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Feérico | DA_18_Rammus | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 5-1 | 13:10:23 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_18_Rammus | -0.0400 |  |
| Jogador 6 | 5-1 | 13:10:24 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Feérico | DA_18_Rammus | -0.2100 |  |
| Jogador 6 | 5-1 | 13:10:24 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-1 | 13:10:25 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Rammus | -0.1700 |  |
| Jogador 6 | 5-1 | 13:10:25 | MOVE Board -> Board: Cascalho (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-1 | 13:10:26 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 5-1 | 13:10:26 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 5-1 | 13:10:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Feérico | DA_18_Rammus | -0.2200 |  |
| Jogador 6 | 5-1 | 13:10:27 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 5-2 | 13:11:15 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Feérico | DA_18_Rammus | 1.0500 |  |
| Jogador 6 | 5-2 | 13:11:15 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Rammus | 1.0500 |  |
| Jogador 6 | 5-2 | 13:11:16 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Rammus | 0.3500 |  |
| Jogador 6 | 5-2 | 13:11:16 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-2 | 13:11:17 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Feérico | DA_18_Rammus | 0.4000 |  |
| Jogador 6 | 5-2 | 13:11:17 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Feérico | DA_18_Rammus | -0.2000 |  |
| Jogador 6 | 5-2 | 13:11:18 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Feérico | DA_18_Rammus | 0.4000 |  |
| Jogador 6 | 5-2 | 13:11:19 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-2 | 13:11:19 | MOVE Board -> Board: Tristana (i:6.0) <-> Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Feérico | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 5-3 | 13:12:10 | VENDEU: Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Feérico | DA_18_Rammus | -0.7000 |  |
| Jogador 6 | 5-3 | 13:12:11 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Rammus | 0.9300 |  |
| Jogador 6 | 5-3 | 13:12:13 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Yorick (i:2.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Rammus | 0.1200 |  |
| Jogador 6 | 5-3 | 13:12:14 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Hecarim (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Rammus | 0.0900 |  |
| Jogador 6 | 5-3 | 13:12:14 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Rammus | -0.7000 |  |
| Jogador 6 | 5-3 | 13:12:15 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Feérico | DA_18_Rammus | 0.4300 |  |
| Jogador 6 | 5-3 | 13:12:15 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Rammus | -0.5200 |  |
| Jogador 6 | 5-3 | 13:12:15 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Feérico | DA_18_Rammus | 0.2800 |  |
| Jogador 6 | 5-3 | 13:12:16 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-4 | 13:13:05 | VENDEU: Alistar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Feérico | DA_18_Rammus | -0.0700 |  |
| Jogador 6 | 5-4 | 13:13:05 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Feérico | DA_18_Rammus | 0.1700 |  |
| Jogador 6 | 5-4 | 13:13:06 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-4 | 13:13:06 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Feérico | DA_18_Rammus | 0.0900 |  |
| Jogador 6 | 5-4 | 13:13:07 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Feérico | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 5-4 | 13:13:07 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Feérico | DA_18_Rammus | 0.0900 |  |
| Jogador 6 | 5-4 | 13:13:08 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Feérico | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 5-4 | 13:13:08 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Feérico | DA_18_Rammus | -0.2200 |  |
| Jogador 6 | 5-4 | 13:13:08 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Feérico | DA_18_Rammus | 0.0100 |  |
| Jogador 6 | 5-5 | 13:13:57 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_18_Rammus | 0.9500 |  |
| Jogador 6 | 5-5 | 13:13:57 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Feérico | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 5-5 | 13:13:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Feérico | DA_18_Rammus | 0.4500 |  |
| Jogador 6 | 5-5 | 13:13:58 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Feérico | DA_18_Rammus | -0.6900 |  |
| Jogador 6 | 5-5 | 13:13:59 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_18_Rammus | 0.1700 |  |
| Jogador 6 | 5-5 | 13:13:59 | MOVE Bench -> Board: Diana (i:6.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_18_Rammus | 0.0300 |  |
| Jogador 6 | 5-5 | 13:14:00 | MOVE Bench -> Board: Vi (i:6.0) <-> Rammus (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_18_Rammus | -0.6600 |  |
| Jogador 6 | 5-5 | 13:14:00 | MOVE Bench -> Board: Rammus (i:12.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_18_Rammus | 0.0800 |  |
| Jogador 6 | 5-5 | 13:14:01 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_18_Rammus | 0.0800 |  |
| Jogador 6 | 5-6 | 13:15:16 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 5-6 | 13:15:17 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Feérico | DA_18_Rammus | 1.0500 |  |
| Jogador 6 | 5-6 | 13:15:18 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Feérico | DA_18_Rammus | 0.1500 |  |
| Jogador 6 | 5-6 | 13:15:18 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Feérico | DA_18_Rammus | 0.4500 |  |
| Jogador 6 | 5-6 | 13:15:19 | MOVE Bench -> Board: Tristana (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Feérico | DA_18_Rammus | 0.6000 |  |
| Jogador 6 | 5-6 | 13:15:19 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rammus | -0.2400 |  |
| Jogador 6 | 5-6 | 13:15:20 | MOVE Board -> Board: Tristana (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-6 | 13:15:21 | MOVE Board -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 5-6 | 13:15:21 | MOVE Board -> Board: Hecarim (i:6.0) <-> Tristana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 5-7 | 13:16:24 | EQUIP_FROM_INVENTORY: DA_18_EmblemSpellweaver -> Tristana (i:12.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_18_Rammus | 0.0100 |  |
| Jogador 6 | 5-7 | 13:16:25 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-7 | 13:16:25 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_18_Rammus | 0.7900 |  |
| Jogador 6 | 5-7 | 13:16:26 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Feérico | DA_18_Rammus | -0.6900 |  |
| Jogador 6 | 5-7 | 13:16:26 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Feérico | DA_18_Rammus | 0.0500 |  |
| Jogador 6 | 5-7 | 13:16:27 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Rammus | -0.0700 |  |
| Jogador 6 | 5-7 | 13:16:27 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 5-7 | 13:16:28 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Rammus | 0.2300 |  |
| Jogador 6 | 5-7 | 13:16:29 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Rammus | -0.0600 |  |
| Jogador 6 | 6-1 | 13:17:21 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Feérico | DA_18_Rammus | 0.4300 |  |
| Jogador 6 | 6-1 | 13:17:22 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Rammus | -0.6200 |  |
| Jogador 6 | 6-1 | 13:17:22 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Feérico | DA_18_Rammus | 0.2400 |  |
| Jogador 6 | 6-1 | 13:17:23 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Rammus | -0.0600 |  |
| Jogador 6 | 6-1 | 13:17:23 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Feérico | DA_18_Rammus | 0.1500 |  |
| Jogador 6 | 6-1 | 13:17:23 | MOVE Board -> Board: Tristana (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Feérico | DA_18_Rammus | 0.0100 |  |
| Jogador 6 | 6-1 | 13:17:24 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 6-1 | 13:17:25 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Feérico | DA_18_Rammus | 0.0700 |  |
| Jogador 6 | 6-1 | 13:17:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Feérico | DA_18_Rammus | -0.0700 |  |
| Jogador 7 | ? | 12:59:32 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 12:59:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 12:59:39 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 12:59:40 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 12:59:40 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 12:59:41 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 12:59:42 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 12:59:42 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 12:59:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 12:59:45 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 12:59:47 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 12:59:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 12:59:48 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 12:59:48 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 12:59:50 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 12:59:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 12:59:56 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 12:59:56 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 7 | 1-3 | 12:59:57 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 12:59:57 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 12:59:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 13:00:04 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 13:00:06 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 13:00:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 13:00:10 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4400 |  |
| Jogador 7 | 2-1 | 13:00:13 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 13:00:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 13:00:14 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 13:00:15 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 13:00:15 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 13:00:16 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 13:00:16 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-2 | 13:00:24 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 13:00:24 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6800 |  |
| Jogador 7 | 2-2 | 13:00:25 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 13:00:25 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-2 | 13:00:26 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 13:00:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-3 | 13:00:36 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 13:00:37 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 2-3 | 13:00:37 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 2-3 | 13:00:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-3 | 13:00:39 | MOVE Board -> Board: Varus (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.3200 |  |
| Jogador 7 | 2-3 | 13:00:39 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 2-3 | 13:00:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.2300 |  |
| Jogador 7 | 2-3 | 13:00:40 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.1100 |  |
| Jogador 7 | 2-3 | 13:00:41 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 13:00:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.3200 |  |
| Jogador 7 | 2-4 | 13:00:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.3300 |  |
| Jogador 7 | 2-4 | 13:00:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-4 | 13:00:54 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.4600 |  |
| Jogador 7 | 2-4 | 13:00:54 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 13:00:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 13:01:08 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 1.0100 |  |
| Jogador 7 | 2-5 | 13:01:08 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.9600 |  |
| Jogador 7 | 2-5 | 13:01:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 13:01:09 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.6200 |  |
| Jogador 7 | 2-5 | 13:01:10 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | -0.6300 |  |
| Jogador 7 | 2-5 | 13:01:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 2-5 | 13:01:11 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 2-5 | 13:01:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-5 | 13:01:12 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 2-6 | 13:01:24 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 7 | 2-6 | 13:01:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-6 | 13:01:25 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 2-6 | 13:01:26 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 2-6 | 13:01:26 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 2-6 | 13:01:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-6 | 13:01:27 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -1.0200 |  |
| Jogador 7 | 2-6 | 13:01:27 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 2-6 | 13:01:28 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 7 | 2-7 | 13:01:43 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 2-7 | 13:01:43 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 7 | 2-7 | 13:01:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 2-7 | 13:01:44 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 7 | 2-7 | 13:01:45 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 7 | 2-7 | 13:01:45 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 2-7 | 13:01:46 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 2-7 | 13:01:46 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 7 | 2-7 | 13:01:47 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 3-1 | 13:02:03 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 7 | 3-1 | 13:02:04 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 7 | 3-1 | 13:02:04 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 3-1 | 13:02:05 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 3-1 | 13:02:05 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.3300 |  |
| Jogador 7 | 3-1 | 13:02:06 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-1 | 13:02:06 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 7 | 3-1 | 13:02:07 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 7 | 3-1 | 13:02:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-2 | 13:02:26 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 7 | 3-2 | 13:02:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-2 | 13:02:27 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 3-2 | 13:02:28 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 3-2 | 13:02:29 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-2 | 13:02:29 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 7 | 3-2 | 13:02:30 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 7 | 3-2 | 13:02:30 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-2 | 13:02:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 13:02:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 7 | 3-3 | 13:02:52 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 7 | 3-3 | 13:02:53 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 7 | 3-3 | 13:02:54 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 7 | 3-3 | 13:02:54 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 7 | 3-3 | 13:02:55 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 13:02:55 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Varus | -0.6200 |  |
| Jogador 7 | 3-3 | 13:02:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.0300 |  |
| Jogador 7 | 3-3 | 13:02:56 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.3300 |  |
| Jogador 7 | 3-4 | 13:03:18 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | 0.2000 |  |
| Jogador 7 | 3-4 | 13:03:19 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | 0.2000 |  |
| Jogador 7 | 3-4 | 13:03:20 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.0300 |  |
| Jogador 7 | 3-4 | 13:03:20 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-4 | 13:03:21 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-4 | 13:03:21 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 3-4 | 13:03:22 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 3-4 | 13:03:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-5 | 13:03:47 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.2800 |  |
| Jogador 7 | 3-5 | 13:03:48 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 3-5 | 13:03:48 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-5 | 13:03:49 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 3-5 | 13:03:49 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 3-5 | 13:03:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-6 | 13:04:18 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.8000 |  |
| Jogador 7 | 3-6 | 13:04:18 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0400 |  |
| Jogador 7 | 3-6 | 13:04:18 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.8100 |  |
| Jogador 7 | 3-6 | 13:04:19 | MOVE Board -> Board: Varus (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-6 | 13:04:20 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-6 | 13:04:20 | MOVE Board -> Board: Rakan (i:2.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-6 | 13:04:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-7 | 13:04:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | 0.1300 |  |
| Jogador 7 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | 0.1400 |  |
| Jogador 7 | 3-7 | 13:04:51 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 3-7 | 13:04:52 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.0900 |  |
| Jogador 7 | 3-7 | 13:04:52 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-7 | 13:04:54 | MOVE Board -> Board: Varus (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 3-7 | 13:04:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-1 | 13:05:27 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-1 | 13:05:28 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Varus | 0.2700 |  |
| Jogador 7 | 4-1 | 13:05:28 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-1 | 13:05:29 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | 0.7900 |  |
| Jogador 7 | 4-1 | 13:05:30 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-1 | 13:05:30 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-1 | 13:05:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-1 | 13:05:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-2 | 13:06:05 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Varus | 0.0600 |  |
| Jogador 7 | 4-2 | 13:06:05 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Varus | 0.8700 |  |
| Jogador 7 | 4-2 | 13:06:06 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_18_Varus | -0.2100 |  |
| Jogador 7 | 4-2 | 13:06:07 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_18_Varus | 0.4200 |  |
| Jogador 7 | 4-2 | 13:06:07 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 4-2 | 13:06:08 | MOVE Board -> Board: Sejuani (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-2 | 13:06:08 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-2 | 13:06:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Varus | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-3 | 13:06:44 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Colosso | DA_18_Varus | -0.5800 |  |
| Jogador 7 | 4-3 | 13:06:44 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Varus | 0.2900 |  |
| Jogador 7 | 4-3 | 13:06:45 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Rakan (i:2.0) (tabuleiro slot 23) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Varus | 0.1200 |  |
| Jogador 7 | 4-3 | 13:06:46 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Rakan (i:2.0) (tabuleiro slot 23) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Varus | 0.1300 |  |
| Jogador 7 | 4-3 | 13:06:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-3 | 13:06:47 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-3 | 13:06:48 | MOVE Board -> Board: Varus (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Varus | -0.1500 |  |
| Jogador 7 | 4-3 | 13:06:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Varus | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-4 | 13:07:27 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-4 | 13:07:28 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_18_Varus | 0.7600 |  |
| Jogador 7 | 4-4 | 13:07:28 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_18_Varus | 0.1000 |  |
| Jogador 7 | 4-4 | 13:07:29 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-4 | 13:07:29 | MOVE Board -> Board: Sejuani (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-4 | 13:07:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_18_Varus | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-5 | 13:08:11 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-5 | 13:08:12 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Varus | 0.9300 |  |
| Jogador 7 | 4-5 | 13:08:12 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Rek'Sai (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Varus | 0.0800 |  |
| Jogador 7 | 4-5 | 13:08:12 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rek'Sai (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Varus | 0.0600 |  |
| Jogador 7 | 4-5 | 13:08:13 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Varus | 0.3000 |  |
| Jogador 7 | 4-5 | 13:08:14 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Varus | 0.7500 |  |
| Jogador 7 | 4-5 | 13:08:14 | MOVE Bench -> Board: Diana (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Varus | -0.1000 |  |
| Jogador 7 | 4-5 | 13:08:15 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Varus | 0.5000 |  |
| Jogador 7 | 4-5 | 13:08:15 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Varus | 0.0600 |  |
| Jogador 7 | 4-6 | 13:08:53 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Colosso | DA_18_Varus | -0.5800 |  |
| Jogador 7 | 4-6 | 13:08:54 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Colosso | DA_18_Hecarim | 0.9200 |  |
| Jogador 7 | 4-6 | 13:08:54 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Hecarim | 0.3400 |  |
| Jogador 7 | 4-6 | 13:08:55 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Rek'Sai (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Hecarim | 0.0600 |  |
| Jogador 7 | 4-6 | 13:08:55 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Diana (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Hecarim | 0.1300 |  |
| Jogador 7 | 4-6 | 13:08:55 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Diana (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Hecarim | 0.0700 |  |
| Jogador 7 | 4-6 | 13:08:56 | MOVE Board -> Board: Diana (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-6 | 13:08:56 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-6 | 13:08:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Hecarim | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-7 | 13:09:37 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_18_Hecarim | 0.1200 |  |
| Jogador 7 | 4-7 | 13:09:37 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_18_Hecarim | 0.1200 |  |
| Jogador 7 | 4-7 | 13:09:38 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_NegatronCloak -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_18_Hecarim | 0.1300 |  |
| Jogador 7 | 4-7 | 13:09:38 | MOVE Board -> Board: Sejuani (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_18_Hecarim | 0.0500 |  |
| Jogador 7 | 4-7 | 13:09:39 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-7 | 13:09:39 | MOVE Board -> Board: Diana (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-7 | 13:09:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Colosso | DA_18_Hecarim | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 5-1 | 13:10:23 | VENDEU: Hecarim (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Colosso | DA_Sentinel18 | -0.5500 |  |
| Jogador 7 | 5-1 | 13:10:24 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Colosso | DA_Sentinel18 | 1.0000 |  |
| Jogador 7 | 5-1 | 13:10:24 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Colosso | DA_Sentinel18 | 0.4500 |  |
| Jogador 7 | 5-1 | 13:10:25 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Colosso | DA_Sentinel18 | 0.4700 |  |
| Jogador 7 | 5-1 | 13:10:25 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-1 | 13:10:26 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 5-1 | 13:10:26 | MOVE Board -> Board: Diana (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-1 | 13:10:27 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-1 | 13:10:27 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Sentinel18 | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 5-2 | 13:11:15 | VENDEU: Lobo Trevoguari (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-2 | 13:11:15 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 5-2 | 13:11:16 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-2 | 13:11:16 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 5-2 | 13:11:17 | MOVE Board -> Board: Sejuani (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_Sentinel18 | -0.1800 |  |
| Jogador 7 | 5-2 | 13:11:17 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 5-2 | 13:11:18 | MOVE Board -> Board: Diana (i:6.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-2 | 13:11:19 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-2 | 13:11:19 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_Sentinel18 | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 5-3 | 13:12:10 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-3 | 13:12:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Colosso | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 5-3 | 13:12:13 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-3 | 13:12:14 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Colosso | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 5-3 | 13:12:14 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-3 | 13:12:15 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 5-3 | 13:12:15 | MOVE Board -> Board: Azuporã (i:8.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-3 | 13:12:15 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 5-3 | 13:12:16 | MOVE Board -> Board: Diana (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-4 | 13:13:05 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-4 | 13:13:05 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 5-4 | 13:13:06 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Colosso | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 5-4 | 13:13:06 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Colosso | DA_Sentinel18 | -0.2100 |  |
| Jogador 7 | 5-4 | 13:13:07 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-4 | 13:13:07 | MOVE Board -> Board: Sejuani (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-4 | 13:13:08 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Colosso | DA_Sentinel18 | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 5-5 | 13:13:57 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-5 | 13:13:57 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 5-5 | 13:13:58 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-5 | 13:13:58 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-5 | 13:13:59 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-5 | 13:13:59 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 5-5 | 13:14:00 | MOVE Board -> Board: Diana (i:6.0) <-> Varus (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 5-5 | 13:14:00 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-5 | 13:14:01 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-6 | 13:15:16 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Colosso | DA_Sentinel18 | 0.9300 |  |
| Jogador 7 | 5-6 | 13:15:17 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 5-6 | 13:15:18 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 5-6 | 13:15:18 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-6 | 13:15:19 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Colosso | DA_Sentinel18 | 0.2200 |  |
| Jogador 7 | 5-6 | 13:15:19 | VENDEU: Cascalho (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 5-6 | 13:15:20 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-6 | 13:15:21 | MOVE Board -> Board: Varus (i:4.0) <-> Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-6 | 13:15:21 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-7 | 13:16:24 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Colosso | DA_Sentinel18 | 1.0100 |  |
| Jogador 7 | 5-7 | 13:16:25 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 5-7 | 13:16:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Colosso | DA_Sentinel18 | -0.2100 |  |
| Jogador 7 | 5-7 | 13:16:26 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Azuporã (i:8.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 5-7 | 13:16:26 | VENDEU: Grompe (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Colosso | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 5-7 | 13:16:27 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Colosso | DA_Sentinel18 | -0.2600 |  |
| Jogador 7 | 5-7 | 13:16:27 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-7 | 13:16:28 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Colosso | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 5-7 | 13:16:29 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 6-1 | 13:17:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Colosso | DA_Sentinel18 | 1.0000 |  |
| Jogador 7 | 6-1 | 13:17:22 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-1 | 13:17:22 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Colosso | DA_Sentinel18 | 1.1100 |  |
| Jogador 7 | 6-1 | 13:17:23 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 6-1 | 13:17:23 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 6-1 | 13:17:23 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Colosso | DA_Sentinel18 | -0.7300 |  |
| Jogador 7 | 6-1 | 13:17:24 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Colosso | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 6-1 | 13:17:25 | VENDEU: Rubrivirim (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-1 | 13:17:25 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Colosso | DA_Sentinel18 | -0.3800 |  |
| Jogador 7 | 6-2 | 13:18:18 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Colosso | DA_Sentinel18 | 0.4300 |  |
| Jogador 7 | 6-2 | 13:18:18 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 6-2 | 13:18:19 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 6-2 | 13:18:19 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Colosso | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 6-2 | 13:18:19 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-2 | 13:18:20 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Colosso | DA_Sentinel18 | -0.2600 |  |
| Jogador 7 | 6-2 | 13:18:20 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 6-2 | 13:18:21 | COMPROU: Camille (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Colosso | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 6-2 | 13:18:21 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 6-3 | 13:19:15 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 161 | 5 | Colosso | DA_Sentinel18 | 1.1100 |  |
| Jogador 7 | 6-3 | 13:19:15 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Colosso | DA_Sentinel18 | 0.1300 |  |
| Jogador 7 | 6-3 | 13:19:16 | VENDEU: Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Colosso | DA_Sentinel18 | -0.7300 |  |
| Jogador 7 | 6-3 | 13:19:16 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 6-3 | 13:19:17 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 167 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 6-3 | 13:19:19 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Colosso | DA_Sentinel18 | -0.2600 |  |
| Jogador 7 | 6-3 | 13:19:19 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-3 | 13:19:20 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Colosso | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 6-3 | 13:19:20 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Colosso | DA_Sentinel18 | 0.5700 |  |
| Jogador 7 | 6-4 | 13:20:16 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Colosso | DA_Sentinel18 | 1.1000 |  |
| Jogador 7 | 6-4 | 13:20:16 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 170 | 5 | Colosso | DA_Sentinel18 | 0.4300 |  |
| Jogador 7 | 6-4 | 13:20:17 | VENDEU: Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Colosso | DA_Sentinel18 | -0.1400 |  |
| Jogador 7 | 6-4 | 13:20:17 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Colosso | DA_Sentinel18 | 0.2600 |  |
| Jogador 7 | 6-4 | 13:20:18 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 176 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 6-4 | 13:20:18 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 6-4 | 13:20:18 | VENDEU: Cascalho (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Colosso | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-4 | 13:20:19 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Colosso | DA_Sentinel18 | 0.7100 |  |
| Jogador 7 | 6-4 | 13:20:19 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Colosso | DA_Sentinel18 | 0.5800 |  |
| Jogador 8 | ? | 12:59:32 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 12:59:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 12:59:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 12:59:39 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 12:59:40 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 12:59:40 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 12:59:41 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 12:59:42 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 12:59:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 12:59:45 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 12:59:47 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 12:59:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 12:59:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 12:59:56 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 12:59:56 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 12:59:57 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 12:59:57 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 12:59:58 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 12:59:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 13:00:04 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 13:00:05 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 13:00:06 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 13:00:06 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 13:00:06 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 13:00:07 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 1-4 | 13:00:10 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.4100 |  |
| Jogador 8 | 1-4 | 13:00:10 | MOVE Board -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-1 | 13:00:13 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 13:00:14 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-1 | 13:00:14 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 2-1 | 13:00:15 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 2-1 | 13:00:15 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.4300 |  |
| Jogador 8 | 2-1 | 13:00:16 | MOVE Bench -> Board: Karma (i:4.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-1 | 13:00:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-2 | 13:00:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.9900 |  |
| Jogador 8 | 2-2 | 13:00:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.0500 |  |
| Jogador 8 | 2-2 | 13:00:25 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.3700 |  |
| Jogador 8 | 2-2 | 13:00:25 | MOVE Bench -> Board: Xayah (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-2 | 13:00:26 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.3800 |  |
| Jogador 8 | 2-2 | 13:00:26 | MOVE Bench -> Board: Karma (i:2.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 2-2 | 13:00:27 | MOVE Bench -> Board: Xayah (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-2 | 13:00:27 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 2-2 | 13:00:28 | MOVE Bench -> Board: Karma (i:2.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 2-3 | 13:00:36 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-3 | 13:00:37 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1500 |  |
| Jogador 8 | 2-3 | 13:00:37 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.1500 |  |
| Jogador 8 | 2-3 | 13:00:38 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 2-3 | 13:00:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-3 | 13:00:39 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.3500 |  |
| Jogador 8 | 2-3 | 13:00:40 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 2-3 | 13:00:40 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1500 |  |
| Jogador 8 | 2-3 | 13:00:41 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | -0.6300 |  |
| Jogador 8 | 2-4 | 13:00:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 2-4 | 13:00:53 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_Karma18 | 0.7800 |  |
| Jogador 8 | 2-4 | 13:00:53 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-4 | 13:00:54 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-4 | 13:00:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-4 | 13:00:55 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 2-4 | 13:00:55 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-4 | 13:00:56 | MOVE Bench -> Board: Karma (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-4 | 13:00:56 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_Karma18 | -0.3500 |  |
| Jogador 8 | 2-5 | 13:01:08 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 2-5 | 13:01:08 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 2-5 | 13:01:09 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 2-5 | 13:01:09 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-5 | 13:01:10 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 2-5 | 13:01:10 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-5 | 13:01:11 | MOVE Bench -> Board: Karma (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | -0.4000 |  |
| Jogador 8 | 2-5 | 13:01:11 | MOVE Bench -> Board: Karma (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 2-5 | 13:01:12 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | -0.3800 |  |
| Jogador 8 | 2-6 | 13:01:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | 0.8800 |  |
| Jogador 8 | 2-6 | 13:01:25 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-6 | 13:01:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-6 | 13:01:26 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_Karma18 | -0.2500 |  |
| Jogador 8 | 2-6 | 13:01:26 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 2-6 | 13:01:27 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 2-6 | 13:01:27 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | -0.1500 |  |
| Jogador 8 | 2-6 | 13:01:27 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | 0.1300 |  |
| Jogador 8 | 2-6 | 13:01:28 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-7 | 13:01:43 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.0400 |  |
| Jogador 8 | 2-7 | 13:01:43 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-7 | 13:01:44 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-7 | 13:01:44 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | -0.1200 |  |
| Jogador 8 | 2-7 | 13:01:45 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-7 | 13:01:45 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | -0.1200 |  |
| Jogador 8 | 2-7 | 13:01:46 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-7 | 13:01:46 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | -0.1400 |  |
| Jogador 8 | 2-7 | 13:01:47 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 3-1 | 13:02:03 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_Karma18 | 0.7100 |  |
| Jogador 8 | 3-1 | 13:02:04 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 3-1 | 13:02:04 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_Karma18 | -0.1700 |  |
| Jogador 8 | 3-1 | 13:02:05 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 3-1 | 13:02:05 | MOVE Bench -> Board: Karma (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_Karma18 | -0.4000 |  |
| Jogador 8 | 3-1 | 13:02:06 | MOVE Bench -> Board: Karma (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_Karma18 | -0.1500 |  |
| Jogador 8 | 3-1 | 13:02:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_Karma18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-2 | 13:02:26 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 3-2 | 13:02:27 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-2 | 13:02:27 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 3-2 | 13:02:28 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.3500 |  |
| Jogador 8 | 3-2 | 13:02:29 | MOVE Bench -> Board: Karma (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 3-2 | 13:02:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-3 | 13:02:52 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 2 | Enfeitiçador | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 3-3 | 13:02:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 2 | Enfeitiçador | DA_Karma18 | 0.8800 |  |
| Jogador 8 | 3-3 | 13:02:53 | MOVE Bench -> Board: Tristana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 2 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-3 | 13:02:54 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 2 | Enfeitiçador | DA_Karma18 | 0.6800 |  |
| Jogador 8 | 3-3 | 13:02:54 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-3 | 13:02:55 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 2 | Enfeitiçador | DA_Karma18 | -0.8000 |  |
| Jogador 8 | 3-3 | 13:02:55 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 2 | Enfeitiçador | DA_Karma18 | -0.3700 |  |
| Jogador 8 | 3-3 | 13:02:56 | MOVE Bench -> Board: Tristana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 2 | Enfeitiçador | DA_Karma18 | -0.1600 |  |
| Jogador 8 | 3-3 | 13:02:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 2 | Enfeitiçador | DA_Karma18 | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-4 | 13:03:18 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Enfeitiçador | DA_Karma18 | 0.8400 |  |
| Jogador 8 | 3-4 | 13:03:19 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Enfeitiçador | DA_Karma18 | 0.8200 |  |
| Jogador 8 | 3-4 | 13:03:20 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-4 | 13:03:20 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Enfeitiçador | DA_Karma18 | 0.3400 |  |
| Jogador 8 | 3-4 | 13:03:21 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Enfeitiçador | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 3-4 | 13:03:21 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 4 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-4 | 13:03:22 | MOVE Board -> Board: Kobuko (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 4 | Enfeitiçador | DA_Karma18 | 0.1600 |  |
| Jogador 8 | 3-4 | 13:03:22 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 4 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-4 | 13:03:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 4 | Enfeitiçador | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 3-5 | 13:03:47 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Enfeitiçador | DA_Karma18 | 0.8300 |  |
| Jogador 8 | 3-5 | 13:03:48 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 3 | Enfeitiçador | DA_Karma18 | -0.5000 |  |
| Jogador 8 | 3-5 | 13:03:48 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Enfeitiçador | DA_Karma18 | 0.2800 |  |
| Jogador 8 | 3-5 | 13:03:49 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 3 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-5 | 13:03:49 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 3 | Enfeitiçador | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 3-5 | 13:03:50 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 3 | Enfeitiçador | DA_Karma18 | -0.3400 |  |
| Jogador 8 | 3-5 | 13:03:50 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Enfeitiçador | DA_Karma18 | -0.1700 |  |
| Jogador 8 | 3-5 | 13:03:51 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Enfeitiçador | DA_Karma18 | 0.1000 |  |
| Jogador 8 | 3-5 | 13:03:52 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 3 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 3-6 | 13:04:18 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 5 | Enfeitiçador | DA_Karma18 | -0.1600 |  |
| Jogador 8 | 3-6 | 13:04:18 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Enfeitiçador | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 3-6 | 13:04:18 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 5 | Enfeitiçador | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 3-6 | 13:04:19 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-6 | 13:04:20 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-6 | 13:04:20 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-6 | 13:04:21 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-6 | 13:04:21 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-6 | 13:04:21 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-7 | 13:04:50 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_Karma18 | 0.3700 |  |
| Jogador 8 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_Karma18 | 0.2200 |  |
| Jogador 8 | 3-7 | 13:04:51 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Karma (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_Karma18 | 0.2400 |  |
| Jogador 8 | 3-7 | 13:04:52 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 3-7 | 13:04:52 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Enfeitiçador | DA_Karma18 | 0.9300 |  |
| Jogador 8 | 3-7 | 13:04:54 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Enfeitiçador | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 3-7 | 13:04:55 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 3-7 | 13:04:55 | VENDEU: Warwick (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Enfeitiçador | DA_Karma18 | -0.5200 |  |
| Jogador 8 | 3-7 | 13:04:55 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 4-1 | 13:05:27 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-1 | 13:05:28 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Enfeitiçador | DA_Karma18 | 0.9400 |  |
| Jogador 8 | 4-1 | 13:05:28 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-1 | 13:05:29 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Enfeitiçador | DA_Karma18 | 1.0100 |  |
| Jogador 8 | 4-1 | 13:05:30 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 4-1 | 13:05:30 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Enfeitiçador | DA_Karma18 | 0.5200 |  |
| Jogador 8 | 4-1 | 13:05:31 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Enfeitiçador | DA_Karma18 | -0.2800 |  |
| Jogador 8 | 4-1 | 13:05:31 | MOVE Board -> Board: Veigar (i:2.0) <-> Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-1 | 13:05:32 | MOVE Board -> Board: Teemo (i:4.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Enfeitiçador | DA_Karma18 | -0.3000 |  |
| Jogador 8 | 4-2 | 13:06:05 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Enfeitiçador | DA_Karma18 | -0.7200 |  |
| Jogador 8 | 4-2 | 13:06:05 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Enfeitiçador | DA_18_Tristana | 1.0700 |  |
| Jogador 8 | 4-2 | 13:06:06 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Enfeitiçador | DA_18_Tristana | 0.9500 |  |
| Jogador 8 | 4-2 | 13:06:07 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Karma (i:4.0) (tabuleiro slot 12) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Enfeitiçador | DA_18_Tristana | 0.1300 |  |
| Jogador 8 | 4-2 | 13:06:07 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Kobuko (i:2.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Enfeitiçador | DA_18_Tristana | 0.1100 |  |
| Jogador 8 | 4-2 | 13:06:08 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Kobuko (i:2.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Enfeitiçador | DA_18_Tristana | 0.0800 |  |
| Jogador 8 | 4-2 | 13:06:08 | VENDEU: Tristana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Enfeitiçador | DA_18_Sivir | -0.7300 |  |
| Jogador 8 | 4-2 | 13:06:09 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Enfeitiçador | DA_18_Sivir | 0.6200 |  |
| Jogador 8 | 4-2 | 13:06:09 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Enfeitiçador | DA_18_Sivir | -0.0700 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 33 | 33 | 165 | 33 | 17 | 256 | 12 | 47 |
| Jogador 2 | 37 | 37 | 185 | 37 | 17 | 298 | 7 | 45 |
| Jogador 3 | 26 | 28 | 140 | 26 | 16 | 179 | 7 | 12 |
| Jogador 4 | 27 | 27 | 135 | 27 | 16 | 208 | 7 | 18 |
| Jogador 5 | 35 | 38 | 190 | 35 | 17 | 279 | 17 | 29 |
| Jogador 6 | 34 | 36 | 180 | 34 | 17 | 255 | 11 | 55 |
| Jogador 7 | 37 | 37 | 185 | 37 | 18 | 289 | 8 | 49 |
| Jogador 8 | 21 | 22 | 110 | 21 | 12 | 165 | 5 | 25 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 256 | 256 | 256 | 0 | 243 | 0 | 256 | 256 | 256 | 93/80 |
| Jogador 2 | 298 | 298 | 298 | 0 | 290 | 0 | 298 | 298 | 298 | 105/89 |
| Jogador 3 | 179 | 179 | 179 | 0 | 171 | 0 | 179 | 179 | 179 | 56/42 |
| Jogador 4 | 208 | 208 | 208 | 0 | 199 | 0 | 208 | 208 | 208 | 78/63 |
| Jogador 5 | 279 | 279 | 279 | 0 | 264 | 0 | 279 | 279 | 279 | 110/97 |
| Jogador 6 | 255 | 255 | 255 | 0 | 245 | 0 | 255 | 255 | 255 | 87/72 |
| Jogador 7 | 289 | 289 | 289 | 0 | 271 | 0 | 289 | 289 | 289 | 100/86 |
| Jogador 8 | 165 | 165 | 165 | 0 | 157 | 0 | 165 | 165 | 165 | 67/54 |

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
| Jogador 1 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4272024929523468 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3464421331882477 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2493164837360382 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0388073921203613 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0312374830245972 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 57 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39937448501586914 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 64 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33591338992118835 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 65 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1294165700674057 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 66 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06047050654888153 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 68 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27562013268470764 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 70 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17279936373233795 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2729596197605133 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35910847783088684 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 75 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1783411055803299 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 76 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 79 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1169795989990234 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 83 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 84 | PASS | STABILIZE | 94.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0230985879898071 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | SELL | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-5 | 94 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 12.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2975885272026062 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 95 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 12.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006044889334589243 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 0 | 0 | 12.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39945074915885925 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 16.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00312969577498734 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 16.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008528998587280512 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 100 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 16.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0247692558914423 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 94.0 | 6 | 6 | 0 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179970502853394 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06641755253076553 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 104 | BUY | STABILIZE | 94.0 | 6 | 2 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06843315809965134 | 0.0 | 0.0 | +b32c67a7-6903-403a-9ed6-519ac8487685 / -— |
| Jogador 1 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042125146836042404 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 106 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1177939176559448 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 113 | BUY | STABILIZE | 94.0 | 6 | 6 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9420243501663208 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 4 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2626439034938812 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13607652485370636 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 116 | BUY | STABILIZE | 94.0 | 6 | 4 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07344847917556763 | 0.0 | 0.0 | +acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce / -— |
| Jogador 1 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 3 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0011849881848320365 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 118 | SELL | STABILIZE | 94.0 | 6 | 3 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 1 | 2-7 | 119 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 6 | 6 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1125856563448906 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 120 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 6 | 6 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10228565335273743 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | BUY | STABILIZE | 94.0 | 6 | 12 | 1 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.002703554928302765 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 9 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19252198934555054 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 124 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 9 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39993414282798767 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 125 | BUY | STABILIZE | 94.0 | 6 | 9 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06191443279385567 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 126 | BUY_XP | STABILIZE | 94.0 | 6 | 7 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 127 | BUY | STABILIZE | 94.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06558594852685928 | 0.0 | 0.0 | +8980fd33-79c8-4825-95e9-9298680cbc6d / -— |
| Jogador 1 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16355419158935547 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 130 | PASS | STABILIZE | 94.0 | 6 | 1 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | BUY | STABILIZE | 94.0 | 6 | 8 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.664993166923523 | 0.0 | 0.0 | +1e504283-c5d1-4eb3-915e-20533ec3a756 / -— |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36203163862228394 | 0.0 | 0.0 | +5204a655-be8f-4607-8fa3-28c981ac1397 / -— |
| Jogador 1 | 3-2 | 134 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24205680191516876 | 0.0 | 0.0 | +dc9a3df1-7032-4c92-a919-ca17ae7639ea / -— |
| Jogador 1 | 3-2 | 135 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13547472655773163 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 136 | SELL | STABILIZE | 94.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02373254857957363 | 0.0 | 0.0 | +— / -8e819ba6-a356-4d9b-a8c9-7493332900fb |
| Jogador 1 | 3-2 | 137 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22634033858776093 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 138 | SELL | STABILIZE | 94.0 | 6 | 2 | 0 | 20.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011692014522850513 | 0.0 | 0.0 | +— / -7c218f01-e884-46da-8a1a-2d2db27a5ff1 |
| Jogador 1 | 3-2 | 139 | BUY_XP | STABILIZE | 94.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 140 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 1 | 0 | 20.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010206981562077999 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 142 | BUY | STABILIZE | 94.0 | 6 | 8 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20595990121364594 | 0.0 | 0.0 | +45450b46-63b4-488f-9469-3348c6da8f4b / -— |
| Jogador 1 | 3-3 | 143 | SELL | STABILIZE | 94.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002166666556149721 | 0.0 | 0.0 | +— / -45450b46-63b4-488f-9469-3348c6da8f4b |
| Jogador 1 | 3-3 | 144 | BUY | STABILIZE | 94.0 | 6 | 8 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24575623869895935 | 0.0 | 0.0 | +bb3be648-cee1-4b75-b472-59653324b9bd / -— |
| Jogador 1 | 3-3 | 145 | SELL | STABILIZE | 94.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -bb3be648-cee1-4b75-b472-59653324b9bd |
| Jogador 1 | 3-3 | 146 | SELL | STABILIZE | 94.0 | 6 | 8 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1007387638092041 | 0.0 | 0.0 | +— / -9fe58106-e0c4-4ecc-b152-13c8c0eb564e |
| Jogador 1 | 3-3 | 147 | SELL | STABILIZE | 94.0 | 6 | 11 | 1 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4323333203792572 | 0.0 | 0.0 | +— / -b32c67a7-6903-403a-9ed6-519ac8487685 |
| Jogador 1 | 3-3 | 148 | BUY_XP | STABILIZE | 94.0 | 6 | 13 | 1 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 149 | BUY_XP | STABILIZE | 94.0 | 6 | 9 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 150 | BUY_XP | STABILIZE | 94.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | BUY | STABILIZE | 82.0 | 6 | 6 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28659114241600037 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 1 | 3-4 | 153 | BUY | STABILIZE | 82.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06207326799631119 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 154 | BUY | STABILIZE | 82.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07394994050264359 | 0.0 | 0.0 | +54b47885-6cb9-42e7-a9bb-049e0e2d2956 / -— |
| Jogador 1 | 3-4 | 155 | SELL | STABILIZE | 82.0 | 6 | 2 | 0 | 20.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005966666620224714 | 0.0 | 0.0 | +— / -54b47885-6cb9-42e7-a9bb-049e0e2d2956 |
| Jogador 1 | 3-4 | 156 | SELL | STABILIZE | 82.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -dc9a3df1-7032-4c92-a919-ca17ae7639ea |
| Jogador 1 | 3-4 | 157 | BUY_XP | STABILIZE | 82.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 1 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4116368591785431 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 1 | 0 | 24.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014737206511199474 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 1 | 0 | 24.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | BUY | STABILIZE | 82.0 | 7 | 6 | 0 | 24.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359144330024719 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 4 | 0 | 16.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38729128241539 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 164 | BUY | STABILIZE | 82.0 | 7 | 4 | 0 | 20.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7598252892494202 | 0.0 | 0.0 | +f6e6e08d-ecfe-4c84-acfa-6ad8292968ee / -1e504283-c5d1-4eb3-915e-20533ec3a756,acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce |
| Jogador 1 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 3 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3523584008216858 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 166 | BUY | STABILIZE | 82.0 | 7 | 3 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028214918449521065 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1507563591003418 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 0 | 0 | 28.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014956208877265453 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 0 | 0 | 28.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015021390281617641 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 170 | PASS | STABILIZE | 82.0 | 7 | 0 | 0 | 28.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 172 | BUY | STABILIZE | 82.0 | 7 | 6 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8047192096710205 | 0.0 | 0.0 | +600071dd-5c17-4f03-903f-d1cd6c20bb28 / -— |
| Jogador 1 | 3-6 | 173 | BUY | STABILIZE | 82.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2859839200973511 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 174 | BUY | STABILIZE | 82.0 | 7 | 3 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021332234144210815 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020954085048288107 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500207744538784 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05519872531294823 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 178 | PASS | STABILIZE | 82.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | BUY | STABILIZE | 70.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2809305489063263 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 183 | SELL | STABILIZE | 70.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07575012743473053 | 0.0 | 0.0 | +— / -f6e6e08d-ecfe-4c84-acfa-6ad8292968ee |
| Jogador 1 | 3-7 | 184 | BUY | STABILIZE | 70.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8006423711776733 | 0.0 | 0.0 | +0d8cf876-2884-4724-ab79-246f8e0406f0 / -— |
| Jogador 1 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023233706131577492 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015135658904910088 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014865169301629066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 188 | PASS | STABILIZE | 70.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 7 | 7 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2415591925382614 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 7 | 7 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17542000114917755 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | SELL | STABILIZE | 70.0 | 7 | 7 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07090233266353607 | 0.0 | 0.0 | +— / -d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-1 | 195 | BUY | STABILIZE | 70.0 | 7 | 10 | 1 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.407376766204834 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 1 | 4-1 | 196 | SELL | STABILIZE | 70.0 | 7 | 7 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4471871852874756 | 0.0 | 0.0 | +— / -8980fd33-79c8-4825-95e9-9298680cbc6d |
| Jogador 1 | 4-1 | 197 | BUY | STABILIZE | 70.0 | 7 | 9 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03175870701670647 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 1 | 4-1 | 198 | SELL | STABILIZE | 70.0 | 7 | 6 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00396723160520196 | 0.0 | 0.0 | +— / -5204a655-be8f-4607-8fa3-28c981ac1397 |
| Jogador 1 | 4-1 | 199 | BUY | STABILIZE | 70.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5024128556251526 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 1 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.175322828814387e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | STABILIZE | 70.0 | 7 | 11 | 1 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5860000252723694 | 0.0 | 0.0 | +— / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 |
| Jogador 1 | 4-2 | 203 | BUY | STABILIZE | 70.0 | 7 | 13 | 1 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879968583583832 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -— |
| Jogador 1 | 4-2 | 204 | SELL | STABILIZE | 70.0 | 7 | 12 | 1 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 1 | 4-2 | 205 | BUY | STABILIZE | 70.0 | 7 | 13 | 1 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23448242247104645 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 1 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 10 | 1 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001998917869059369 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 207 | SELL | STABILIZE | 70.0 | 7 | 10 | 1 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07844516634941101 | 0.0 | 0.0 | +— / -c617e958-b482-40ce-ab24-acff4dc48bc0 |
| Jogador 1 | 4-2 | 208 | BUY | STABILIZE | 70.0 | 7 | 13 | 1 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01768803782761097 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -— |
| Jogador 1 | 4-2 | 209 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 10 | 1 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00019898860773537308 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 210 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 10 | 1 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014965183101594448 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 212 | SELL | STABILIZE | 70.0 | 7 | 18 | 1 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06909693777561188 | 0.0 | 0.0 | +— / -9cb61b5c-2c8a-43a2-a854-517f4377f6db |
| Jogador 1 | 4-3 | 213 | BUY | STABILIZE | 70.0 | 7 | 21 | 2 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07160281389951706 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 1 | 4-3 | 214 | SELL | STABILIZE | 70.0 | 7 | 18 | 1 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07090000063180923 | 0.0 | 0.0 | +— / -caf1c554-2223-4090-9f96-b551e5c579ce |
| Jogador 1 | 4-3 | 215 | BUY | STABILIZE | 70.0 | 7 | 21 | 2 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07086598873138428 | 0.0 | 0.0 | +84886290-556f-45e9-805b-9ca86a80ba27 / -— |
| Jogador 1 | 4-3 | 216 | SELL | STABILIZE | 70.0 | 7 | 20 | 2 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023062095046043396 | 0.0 | 0.0 | +— / -84886290-556f-45e9-805b-9ca86a80ba27 |
| Jogador 1 | 4-3 | 217 | BUY | STABILIZE | 70.0 | 7 | 21 | 2 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05518165975809097 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -— |
| Jogador 1 | 4-3 | 218 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 20 | 2 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 219 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 20 | 2 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014990726485848427 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 220 | PASS | STABILIZE | 70.0 | 7 | 20 | 2 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02857142873108387 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | SELL | STABILIZE | 70.0 | 7 | 29 | 2 | 30.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05823333188891411 | 0.0 | 0.0 | +— / -6538f28f-845f-4f45-92bf-120931553bec |
| Jogador 1 | 4-4 | 223 | BUY | STABILIZE | 70.0 | 7 | 30 | 3 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8125693202018738 | 0.0 | 0.0 | +30d2995a-d9b8-4424-af46-8766734e440c / -0d8cf876-2884-4724-ab79-246f8e0406f0,c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 4-4 | 224 | BUY | STABILIZE | 70.0 | 7 | 27 | 2 | 30.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7560287714004517 | 0.0 | 0.0 | +d974e68a-e978-4335-8827-a94a9219be58 / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164,1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 |
| Jogador 1 | 4-4 | 225 | BUY | STABILIZE | 70.0 | 7 | 24 | 2 | 30.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18377450108528137 | 0.0 | 0.0 | +a2b57772-7a23-4ffd-ace1-d2a7a3f5a7cd / -— |
| Jogador 1 | 4-4 | 226 | BUY | STABILIZE | 70.0 | 7 | 21 | 2 | 30.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07818225026130676 | 0.0 | 0.0 | +f4173576-aa2e-4a93-94ec-ecd49d90d2b7 / -— |
| Jogador 1 | 4-4 | 227 | BUY | STABILIZE | 70.0 | 7 | 19 | 1 | 30.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04550638422369957 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -— |
| Jogador 1 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 17 | 1 | 30.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.422209192649461e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 229 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 17 | 1 | 30.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014956886880099773 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 230 | PASS | STABILIZE | 70.0 | 7 | 17 | 1 | 30.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026428570970892906 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | SELL | STABILIZE | 70.0 | 7 | 24 | 2 | 30.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022833332419395447 | 0.0 | 0.0 | +— / -d974e68a-e978-4335-8827-a94a9219be58 |
| Jogador 1 | 4-5 | 233 | BUY | STABILIZE | 70.0 | 7 | 32 | 3 | 30.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21316395699977875 | 0.0 | 0.0 | +1022f12a-84e9-4eeb-81dc-706092de3728 / -— |
| Jogador 1 | 4-5 | 234 | SELL | STABILIZE | 70.0 | 7 | 29 | 2 | 30.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -30d2995a-d9b8-4424-af46-8766734e440c |
| Jogador 1 | 4-5 | 235 | BUY | STABILIZE | 70.0 | 7 | 37 | 3 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15574148297309875 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 1 | 4-5 | 236 | SELL | STABILIZE | 70.0 | 7 | 33 | 3 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -f4173576-aa2e-4a93-94ec-ecd49d90d2b7 |
| Jogador 1 | 4-5 | 237 | BUY | STABILIZE | 70.0 | 7 | 35 | 3 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15574148297309875 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 1 | 4-5 | 238 | SELL | STABILIZE | 70.0 | 7 | 31 | 3 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010736650787293911 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 1 | 4-5 | 239 | BUY | STABILIZE | 70.0 | 7 | 33 | 3 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04794988036155701 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 1 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 30 | 3 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.128986347495811e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | SELL | STABILIZE | 70.0 | 7 | 40 | 4 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -d1f19609-8b5f-489d-a2cf-d015fe7ed27e |
| Jogador 1 | 4-6 | 243 | BUY | STABILIZE | 70.0 | 7 | 43 | 4 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9245041012763977 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -760d5bee-7d64-4f03-abf0-6357c914a1ed,b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 4-6 | 244 | BUY | STABILIZE | 70.0 | 7 | 41 | 4 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2404307872056961 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -— |
| Jogador 1 | 4-6 | 245 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 38 | 3 | 26.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40029478073120117 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 246 | BUY | STABILIZE | 70.0 | 7 | 38 | 3 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22529080510139465 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -— |
| Jogador 1 | 4-6 | 247 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 35 | 3 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 248 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 35 | 3 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999360777437687 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 249 | PASS | STABILIZE | 70.0 | 7 | 35 | 3 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03928571566939354 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 252 | SELL | STABILIZE | 70.0 | 7 | 46 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5033000111579895 | 0.0 | 0.0 | +— / -0f5471bd-1451-4979-adc9-aced6bb63610 |
| Jogador 1 | 4-7 | 253 | BUY | STABILIZE | 70.0 | 7 | 51 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26936274766921997 | 0.0 | 0.0 | +0435182d-aea5-44fe-ba36-601627982b66 / -— |
| Jogador 1 | 4-7 | 254 | SELL | STABILIZE | 70.0 | 7 | 48 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09099999815225601 | 0.0 | 0.0 | +— / -4c1dab77-0e6d-401b-a341-40117b445957 |
| Jogador 1 | 4-7 | 255 | BUY | STABILIZE | 70.0 | 7 | 51 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06127940118312836 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 1 | 4-7 | 256 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 49 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 257 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 49 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015024359337985516 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 258 | PASS | STABILIZE | 70.0 | 7 | 49 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04928571358323097 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 7 | 60 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.0896705612540245 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 7 | 60 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08150175958871841 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 264 | SELL | STABILIZE | 70.0 | 7 | 60 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050200000405311584 | 0.0 | 0.0 | +— / -84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 1 | 5-1 | 265 | BUY | STABILIZE | 70.0 | 7 | 62 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9079408049583435 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -— |
| Jogador 1 | 5-1 | 266 | SELL | STABILIZE | 70.0 | 7 | 59 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -1022f12a-84e9-4eeb-81dc-706092de3728 |
| Jogador 1 | 5-1 | 267 | BUY | STABILIZE | 70.0 | 7 | 62 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6626790761947632 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -— |
| Jogador 1 | 5-1 | 268 | SELL | STABILIZE | 70.0 | 7 | 59 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 1 | 5-1 | 269 | BUY | STABILIZE | 70.0 | 7 | 63 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9852394461631775 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -2f5d8cb8-8ba3-45e9-a345-00e931d34490,2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 5-1 | 270 | BUY | STABILIZE | 70.0 | 7 | 60 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1920558363199234 | 0.0 | 0.0 | +d6a929d8-6d7c-4bcd-880d-d819daca2ae0 / -— |
| Jogador 1 | 5-2 | 272 | BUY | STABILIZE | 56.0 | 7 | 67 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0202443599700928 | 0.0 | 0.0 | +8d75ef64-e2c3-47b6-a336-c9e5867158e5 / -600071dd-5c17-4f03-903f-d1cd6c20bb28,cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 5-2 | 273 | BUY | STABILIZE | 56.0 | 7 | 66 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37828484177589417 | 0.0 | 0.0 | +6594349f-ecaa-4212-b063-815acae6d0bb / -— |
| Jogador 1 | 5-2 | 274 | SELL | STABILIZE | 56.0 | 7 | 63 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -8d75ef64-e2c3-47b6-a336-c9e5867158e5 |
| Jogador 1 | 5-2 | 275 | BUY | STABILIZE | 56.0 | 7 | 66 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.12468934059143066 | 0.0 | 0.0 | +2f75fcd7-1405-49fd-8a0c-649c1f8a9f09 / -— |
| Jogador 1 | 5-2 | 276 | EQUIP_FROM_INVENTORY | STABILIZE | 56.0 | 7 | 63 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1126796156167984 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 277 | EQUIP_FROM_INVENTORY | STABILIZE | 56.0 | 7 | 63 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08572280406951904 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 278 | EQUIP_FROM_INVENTORY | STABILIZE | 56.0 | 7 | 63 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05711981654167175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 279 | MOVE_BENCH | STABILIZE | 56.0 | 7 | 63 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5262824892997742 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 280 | BUY | FAST8 | 56.0 | 7 | 63 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2452351152896881 | 0.0 | 0.0 | +5821f43b-b898-4842-b309-d175f2284a84 / -— |
| Jogador 1 | 5-3 | 282 | SELL | FAST8 | 41.0 | 7 | 70 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4976666569709778 | 0.0 | 0.0 | +— / -ee67f5c6-559f-492e-9cc0-6bc19a203d6a |
| Jogador 1 | 5-3 | 283 | BUY | FAST8 | 41.0 | 7 | 78 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38374555110931396 | 0.0 | 0.0 | +45b96060-6eda-4d0b-9012-e80db31b71d2 / -— |
| Jogador 1 | 5-3 | 284 | SELL | FAST8 | 41.0 | 7 | 76 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -d6a929d8-6d7c-4bcd-880d-d819daca2ae0 |
| Jogador 1 | 5-3 | 285 | BUY | FAST8 | 41.0 | 7 | 79 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4012988805770874 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -— |
| Jogador 1 | 5-3 | 286 | SELL | FAST8 | 41.0 | 7 | 78 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -5821f43b-b898-4842-b309-d175f2284a84 |
| Jogador 1 | 5-3 | 287 | BUY | FAST8 | 41.0 | 7 | 82 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2915515899658203 | 0.0 | 0.0 | +4e6b6f57-7f94-46ba-b832-c3198d4a5949 / -— |
| Jogador 1 | 5-3 | 288 | MOVE_BOARD | FAST8 | 41.0 | 7 | 78 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002454970090184361 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 289 | MOVE_BOARD | FAST8 | 41.0 | 7 | 78 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 290 | MOVE_BOARD | FAST8 | 41.0 | 7 | 78 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 292 | SELL | STABILIZE | 26.0 | 7 | 89 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11951515823602676 | 0.0 | 0.0 | +— / -4e6b6f57-7f94-46ba-b832-c3198d4a5949 |
| Jogador 1 | 5-4 | 293 | BUY | STABILIZE | 26.0 | 7 | 93 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9737437963485718 | 0.0 | 0.0 | +7a419783-907e-47e2-bf69-29a54ee18a02 / -— |
| Jogador 1 | 5-4 | 294 | SELL | STABILIZE | 26.0 | 7 | 91 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -22f3c707-2635-41cb-a228-10d5ed1883b3 |
| Jogador 1 | 5-4 | 295 | BUY | STABILIZE | 26.0 | 7 | 92 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35089194774627686 | 0.0 | 0.0 | +1512b230-15a6-405f-9b6b-4387a3091648 / -— |
| Jogador 1 | 5-4 | 296 | SELL | STABILIZE | 26.0 | 7 | 90 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43924039602279663 | 0.0 | 0.0 | +— / -1512b230-15a6-405f-9b6b-4387a3091648 |
| Jogador 1 | 5-4 | 297 | BUY | STABILIZE | 26.0 | 7 | 92 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10036126524209976 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 1 | 5-4 | 298 | MOVE_BOARD | STABILIZE | 26.0 | 7 | 90 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -7.588668609059823e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 299 | MOVE_BOARD | STABILIZE | 26.0 | 7 | 90 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015006707049906254 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 300 | PASS | STABILIZE | 26.0 | 7 | 90 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16934619843959808 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 302 | SELL | STABILIZE | 26.0 | 7 | 101 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -64d87de4-68df-4a72-8b8d-f78039ae4ce5 |
| Jogador 1 | 5-5 | 303 | BUY | STABILIZE | 26.0 | 7 | 103 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1917126625776291 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 1 | 5-5 | 304 | SELL | STABILIZE | 26.0 | 7 | 101 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06319999694824219 | 0.0 | 0.0 | +— / -d30c92eb-1279-4532-b763-7c30826c8430 |
| Jogador 1 | 5-5 | 305 | BUY | STABILIZE | 26.0 | 7 | 103 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1815345585346222 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 1 | 5-5 | 306 | SELL | STABILIZE | 26.0 | 7 | 98 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -6fb5e8f1-2656-486b-9478-161c1b430d5f |
| Jogador 1 | 5-5 | 307 | BUY | STABILIZE | 26.0 | 7 | 103 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02706700749695301 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -— |
| Jogador 1 | 5-5 | 308 | MOVE_BOARD | STABILIZE | 26.0 | 7 | 102 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.0696573958266526e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 309 | MOVE_BOARD | STABILIZE | 26.0 | 7 | 102 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500497292727232 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 310 | MOVE_BOARD | STABILIZE | 26.0 | 7 | 102 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04741757735610008 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 312 | SELL | ALL_IN | 10.0 | 7 | 113 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -8da82a9e-0746-43e1-81c3-fa22ec3bb863 |
| Jogador 1 | 5-6 | 313 | BUY | ALL_IN | 10.0 | 7 | 114 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9243443608283997 | 0.0 | 0.0 | +551e9535-d584-4055-a544-ed78d65ecacb / -— |
| Jogador 1 | 5-6 | 314 | SELL | ALL_IN | 10.0 | 7 | 111 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5765171051025391 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 1 | 5-6 | 315 | BUY | ALL_IN | 10.0 | 7 | 114 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5535284280776978 | 0.0 | 0.0 | +d3fddd9d-ee81-418d-9c58-0baa4ed99f61 / -— |
| Jogador 1 | 5-6 | 316 | SELL | ALL_IN | 10.0 | 7 | 111 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5764638185501099 | 0.0 | 0.0 | +— / -d3fddd9d-ee81-418d-9c58-0baa4ed99f61 |
| Jogador 1 | 5-6 | 317 | BUY | ALL_IN | 10.0 | 7 | 114 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14944350719451904 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -— |
| Jogador 1 | 5-6 | 318 | SELL | ALL_IN | 10.0 | 7 | 112 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030252590775489807 | 0.0 | 0.0 | +— / -01c587bb-ca4f-4690-9e4b-d1e9c44fd33e |
| Jogador 1 | 5-6 | 319 | BUY | ALL_IN | 10.0 | 7 | 114 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13181041181087494 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 1 | 5-6 | 320 | MOVE_BOARD | ALL_IN | 10.0 | 7 | 112 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006333725526928902 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 322 | SELL | ALL_IN | 10.0 | 7 | 123 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -3c5f5211-f30d-44e7-ac68-0ce513a3d614 |
| Jogador 1 | 5-7 | 323 | BUY | ALL_IN | 10.0 | 7 | 125 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0648536682128906 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -2f75fcd7-1405-49fd-8a0c-649c1f8a9f09,551e9535-d584-4055-a544-ed78d65ecacb |
| Jogador 1 | 5-7 | 324 | BUY | ALL_IN | 10.0 | 7 | 122 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1983167827129364 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 1 | 5-7 | 325 | BUY | ALL_IN | 10.0 | 7 | 119 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06385891139507294 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 1 | 5-7 | 326 | SELL | ALL_IN | 10.0 | 7 | 118 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7224000096321106 | 0.0 | 0.0 | +— / -c2bf43be-e6e1-47ed-bcb4-606e37f26671 |
| Jogador 1 | 5-7 | 327 | BUY | ALL_IN | 10.0 | 7 | 126 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05476577207446098 | 0.0 | 0.0 | +d58ebcea-d18b-42f8-a6ca-984d15656662 / -— |
| Jogador 1 | 5-7 | 328 | MOVE_BOARD | ALL_IN | 10.0 | 7 | 124 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 329 | SELL | ALL_IN | 10.0 | 7 | 124 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 1 | 5-7 | 330 | BUY | ALL_IN | 10.0 | 7 | 125 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2677542567253113 | 0.0 | 0.0 | +b58c0c0e-9c6f-4977-91d1-177b7113c439 / -— |
| Jogador 1 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 10.0 | 7 | 133 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.049296729266643524 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 333 | SELL | ALL_IN | 10.0 | 7 | 133 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -b58c0c0e-9c6f-4977-91d1-177b7113c439 |
| Jogador 1 | 6-1 | 334 | BUY | ALL_IN | 10.0 | 7 | 135 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1108973026275635 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -45b96060-6eda-4d0b-9012-e80db31b71d2,7a419783-907e-47e2-bf69-29a54ee18a02 |
| Jogador 1 | 6-1 | 335 | BUY | ALL_IN | 10.0 | 7 | 133 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9459677934646606 | 0.0 | 0.0 | +56332309-e8e8-464a-904f-e9253912cd2f / -— |
| Jogador 1 | 6-1 | 336 | BUY | ALL_IN | 10.0 | 7 | 130 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1098636388778687 | 0.0 | 0.0 | +e89905aa-6564-4e15-bc3a-c281646446bc / -56332309-e8e8-464a-904f-e9253912cd2f,9717d30c-f073-470c-a6ce-7db8257de559 |
| Jogador 1 | 6-1 | 337 | BUY | ALL_IN | 10.0 | 7 | 127 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07532169669866562 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 1 | 6-1 | 338 | BUY | ALL_IN | 10.0 | 7 | 124 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2668493688106537 | 0.0 | 0.0 | +b1d58916-6d8b-4071-a37d-a478395e6a1e / -— |
| Jogador 1 | 6-1 | 339 | SELL | ALL_IN | 10.0 | 7 | 122 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.972000002861023 | 0.0 | 0.0 | +— / -4261ad99-2607-4d90-978c-9e9abffd6d95 |
| Jogador 1 | 6-1 | 340 | SELL | ALL_IN | 10.0 | 7 | 127 | 5 | 38.0 | Inferno/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7674000263214111 | 0.0 | 0.0 | +— / -e89905aa-6564-4e15-bc3a-c281646446bc |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5006924271583557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178046464920044 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11945630609989166 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30802857875823975 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40789613127708435 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0719952583312988 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20253360271453857 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.400325745344162 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 48 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0379780530929565 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18191392719745636 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.27331092953681946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2659701406955719 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 58 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14810088276863098 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04755423590540886 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1965099424123764 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-1 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028999745845794678 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004016788676381111 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 64 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047968864440918 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 65 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23487500846385956 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 66 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.153025284409523 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 67 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 68 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000639524485450238 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29771703481674194 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03795068338513374 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 74 | SELL | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-3 | 75 | BUY | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03060082532465458 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 2 | 2-3 | 76 | SELL | STABILIZE | 90.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12360385060310364 | 0.0 | 0.0 | +— / -7ca9b803-76eb-4283-9648-7f98bfd81149 |
| Jogador 2 | 2-3 | 77 | SELL | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05833333358168602 | 0.0 | 0.0 | +— / -e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 2 | 2-3 | 78 | BUY_XP | STABILIZE | 90.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 79 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4012211561203003 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3562205135822296 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 83 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1331465244293213 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 84 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.1642698533905786e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997730031609535 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 86 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33776789903640747 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 93 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0755184069275856 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 2 | 2-5 | 94 | BUY | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1036272719502449 | 0.0 | 0.0 | +be53a299-cc3e-4af3-94f6-343f9de1e0a0 / -— |
| Jogador 2 | 2-5 | 95 | SELL | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3409999907016754 | 0.0 | 0.0 | +— / -eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 2 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39996740221977234 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 97 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04100000113248825 | 0.0 | 0.0 | +— / -be53a299-cc3e-4af3-94f6-343f9de1e0a0 |
| Jogador 2 | 2-5 | 98 | PASS | STABILIZE | 90.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 102 | BUY | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8926606178283691 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 103 | BUY | STABILIZE | 84.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20412035286426544 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 104 | SELL | STABILIZE | 84.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1276666671037674 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-6 | 105 | SELL | STABILIZE | 84.0 | 5 | 3 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043666668236255646 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 2-6 | 106 | BUY_XP | STABILIZE | 84.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 107 | SELL | STABILIZE | 84.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 108 | BUY_XP | STABILIZE | 84.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 109 | BUY | STABILIZE | 84.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023411432281136513 | 0.0 | 0.0 | +8ea1c095-e10b-46d0-8097-a70a211e2881 / -— |
| Jogador 2 | 2-6 | 110 | SELL | STABILIZE | 84.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3409999907016754 | 0.0 | 0.0 | +— / -8ea1c095-e10b-46d0-8097-a70a211e2881 |
| Jogador 2 | 2-7 | 112 | BUY | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6489893198013306 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 113 | BUY | STABILIZE | 84.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2074202299118042 | 0.0 | 0.0 | +0067f61f-504d-440a-b071-de7f18886e3d / -— |
| Jogador 2 | 2-7 | 114 | BUY | STABILIZE | 84.0 | 5 | 3 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11446979641914368 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 115 | SELL | STABILIZE | 84.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15408919751644135 | 0.0 | 0.0 | +— / -0067f61f-504d-440a-b071-de7f18886e3d |
| Jogador 2 | 2-7 | 116 | SELL | STABILIZE | 84.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09857334941625595 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 2-7 | 117 | BUY_XP | STABILIZE | 84.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 118 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5983387231826782 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997811056673527 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999941922724247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 122 | BUY | STABILIZE | 84.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2865546643733978 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 123 | BUY | STABILIZE | 84.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26519888639450073 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25968435406684875 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 125 | SELL | STABILIZE | 84.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46448686718940735 | 0.0 | 0.0 | +— / -729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 3-1 | 126 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 127 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09952849894762039 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 129 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499656438827515 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999709092080593 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 132 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2857327461242676 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 133 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03649163991212845 | 0.0 | 0.0 | +f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 / -— |
| Jogador 2 | 3-2 | 134 | BUY_XP | STABILIZE | 84.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 135 | SELL | STABILIZE | 84.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899999871850014 | 0.0 | 0.0 | +— / -f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 |
| Jogador 2 | 3-2 | 136 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6255555748939514 | 0.0 | 0.0 | +— / -584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 3-2 | 137 | BUY | STABILIZE | 84.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006764198653399944 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -— |
| Jogador 2 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.263719690949074e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997491613030434 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 140 | PASS | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 142 | BUY | STABILIZE | 84.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7216460108757019 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03638006001710892 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 144 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05338666960597038 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-3 | 145 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 146 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 26.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-3 | 147 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 148 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 26.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4308995306491852 | 0.0 | 0.0 | +— / -e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 3-3 | 149 | BUY | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03188019245862961 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 0 | 0 | 26.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007509884424507618 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03382771089673042 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 153 | BUY | STABILIZE | 84.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3923170566558838 | 0.0 | 0.0 | +a15ff9dc-bf8a-49e0-9893-f92a212263d8 / -— |
| Jogador 2 | 3-4 | 154 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 2 | 3-4 | 155 | BUY_XP | STABILIZE | 84.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 156 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5679555535316467 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 2 | 3-4 | 157 | BUY_XP | STABILIZE | 84.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0074412086978554726 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014930048026144505 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | BUY | STABILIZE | 84.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23746918141841888 | 0.0 | 0.0 | +b5cec20a-0619-4060-9f1b-e72942ac34dd / -— |
| Jogador 2 | 3-5 | 163 | BUY | STABILIZE | 84.0 | 7 | 5 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04855526238679886 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4004051685333252 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 165 | BUY | STABILIZE | 84.0 | 7 | 2 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11124088615179062 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00027376957586966455 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014727097004652023 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 168 | PASS | STABILIZE | 84.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 172 | BUY | STABILIZE | 84.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8339879512786865 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -561fb9a8-e987-4935-b11c-6c6104ced65d,6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 3-6 | 173 | BUY | STABILIZE | 84.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28749364614486694 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 174 | BUY | STABILIZE | 84.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13183461129665375 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 177 | PASS | STABILIZE | 84.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 182 | SELL | STABILIZE | 84.0 | 7 | 10 | 1 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -63304cf5-4aa7-473e-9bfb-ec04cd68ebbd |
| Jogador 2 | 3-7 | 183 | BUY | STABILIZE | 84.0 | 7 | 15 | 1 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8336384296417236 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 184 | BUY | STABILIZE | 84.0 | 7 | 12 | 1 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14065034687519073 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 185 | SELL | STABILIZE | 84.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 186 | BUY | STABILIZE | 84.0 | 7 | 16 | 1 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1386016309261322 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 187 | SELL | STABILIZE | 84.0 | 7 | 13 | 1 | 26.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0038061607629060745 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-7 | 188 | BUY_XP | STABILIZE | 84.0 | 7 | 15 | 1 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 189 | BUY_XP | STABILIZE | 84.0 | 7 | 11 | 1 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 190 | BUY_XP | STABILIZE | 84.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 192 | BUY | STABILIZE | 84.0 | 7 | 11 | 1 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08406729996204376 | 0.0 | 0.0 | +15d93457-0760-419e-87db-74223c1cb7f4 / -— |
| Jogador 2 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13779425621032715 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1824129819869995 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 195 | BUY_XP | STABILIZE | 84.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 196 | BUY_XP | STABILIZE | 84.0 | 7 | 4 | 0 | 26.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4008723199367523 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 200 | PASS | STABILIZE | 84.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 202 | BUY | STABILIZE | 72.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379983305931091 | 0.0 | 0.0 | +bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-2 | 203 | BUY | STABILIZE | 72.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42681825160980225 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 2 | 4-2 | 204 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.808650813472923e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 205 | SELL | STABILIZE | 72.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b |
| Jogador 2 | 4-2 | 206 | BUY | STABILIZE | 72.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012864258140325546 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 2 | 4-2 | 207 | SELL | STABILIZE | 72.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -9bd6852a-b7a4-468c-a8cc-5318f7906eae |
| Jogador 2 | 4-2 | 208 | BUY_XP | STABILIZE | 72.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 209 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08443906903266907 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 210 | MOVE_BOARD | FAST8 | 72.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | BUY | FAST8 | 72.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7415308356285095 | 0.0 | 0.0 | +3f488391-7117-4e28-b6cc-7416722351d4 / -0534477f-2ff8-47a7-b71b-1a1d5430589e,15d93457-0760-419e-87db-74223c1cb7f4 |
| Jogador 2 | 4-3 | 213 | BUY | STABILIZE | 72.0 | 7 | 3 | 0 | 24.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2824349105358124 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 2 | 4-3 | 214 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013072162866592407 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 215 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6059762239456177 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 216 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059645507484674454 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 217 | SELL | STABILIZE | 72.0 | 7 | 0 | 0 | 24.0 | Vivaz/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059601955115795135 | 0.0 | 0.0 | +— / -3f488391-7117-4e28-b6cc-7416722351d4 |
| Jogador 2 | 4-3 | 218 | BUY | STABILIZE | 72.0 | 7 | 8 | 0 | 24.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1672661006450653 | 0.0 | 0.0 | +395ae945-c8a2-4d80-98a4-5eb6887b8f78 / -— |
| Jogador 2 | 4-3 | 219 | SELL | STABILIZE | 72.0 | 7 | 7 | 0 | 24.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012900000438094139 | 0.0 | 0.0 | +— / -395ae945-c8a2-4d80-98a4-5eb6887b8f78 |
| Jogador 2 | 4-3 | 220 | BUY_XP | STABILIZE | 72.0 | 7 | 8 | 0 | 24.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 222 | BUY | STABILIZE | 59.0 | 7 | 9 | 0 | 24.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8032217025756836 | 0.0 | 0.0 | +b5b3098f-d48c-42b8-8022-639a25225980 / -— |
| Jogador 2 | 4-4 | 223 | SELL | STABILIZE | 59.0 | 7 | 6 | 0 | 24.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -b5cec20a-0619-4060-9f1b-e72942ac34dd |
| Jogador 2 | 4-4 | 224 | BUY | STABILIZE | 59.0 | 7 | 8 | 0 | 24.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021349921822547913 | 0.0 | 0.0 | +fb551efa-6ad5-4f97-aa05-bc5eb70943d4 / -— |
| Jogador 2 | 4-4 | 225 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 5 | 0 | 24.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06447431445121765 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 226 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 5 | 0 | 28.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2329675853252411 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 227 | BUY | STABILIZE | 59.0 | 7 | 5 | 0 | 30.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19494421780109406 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 2 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 59.0 | 7 | 4 | 0 | 30.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0003395673702470958 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 229 | MOVE_BOARD | STABILIZE | 59.0 | 7 | 4 | 0 | 30.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014659163542091846 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 230 | PASS | STABILIZE | 59.0 | 7 | 4 | 0 | 30.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 232 | BUY | FAST8 | 59.0 | 7 | 9 | 0 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7302842736244202 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 2 | 4-5 | 233 | MOVE_BOARD | FAST8 | 59.0 | 7 | 6 | 0 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 234 | MOVE_BOARD | FAST8 | 59.0 | 7 | 6 | 0 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09118848294019699 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 235 | PASS | FAST8 | 59.0 | 7 | 6 | 0 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 242 | SELL | FAST8 | 47.0 | 7 | 12 | 1 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018333332845941186 | 0.0 | 0.0 | +— / -29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 2 | 4-6 | 243 | BUY | FAST8 | 47.0 | 7 | 13 | 1 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7379989624023438 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 2 | 4-6 | 244 | MOVE_BOARD | FAST8 | 47.0 | 7 | 12 | 1 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052913181483745575 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 245 | SELL | FAST8 | 47.0 | 7 | 12 | 1 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12783333659172058 | 0.0 | 0.0 | +— / -235510e3-df54-4de9-9bcf-bff6d47e364a |
| Jogador 2 | 4-6 | 246 | BUY | FAST8 | 47.0 | 7 | 15 | 1 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04085463657975197 | 0.0 | 0.0 | +a11208a9-96bf-468e-ab92-2ead6308be26 / -— |
| Jogador 2 | 4-6 | 247 | SELL | FAST8 | 47.0 | 7 | 14 | 1 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023499999195337296 | 0.0 | 0.0 | +— / -a11208a9-96bf-468e-ab92-2ead6308be26 |
| Jogador 2 | 4-6 | 248 | BUY | FAST8 | 47.0 | 7 | 15 | 1 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11304739117622375 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 2 | 4-6 | 249 | SELL | FAST8 | 47.0 | 7 | 13 | 1 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010799452662467957 | 0.0 | 0.0 | +— / -ded275a3-9551-4816-8112-f0a25524412c |
| Jogador 2 | 4-6 | 250 | BUY | FAST8 | 47.0 | 7 | 15 | 1 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11910901218652725 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 2 | 4-7 | 252 | SELL | FAST8 | 47.0 | 7 | 21 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010129163973033428 | 0.0 | 0.0 | +— / -42aa4dc8-e388-40dd-a210-4c59e358afcd |
| Jogador 2 | 4-7 | 253 | BUY | FAST8 | 47.0 | 7 | 22 | 2 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1286403387784958 | 0.0 | 0.0 | +590d07db-5e90-4705-a7ae-96f84fd06382 / -— |
| Jogador 2 | 4-7 | 254 | SELL | FAST8 | 47.0 | 7 | 21 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044705264270305634 | 0.0 | 0.0 | +— / -590d07db-5e90-4705-a7ae-96f84fd06382 |
| Jogador 2 | 4-7 | 255 | BUY | FAST8 | 47.0 | 7 | 22 | 2 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04649049788713455 | 0.0 | 0.0 | +8b75555c-d84d-4b8a-8d6c-012585a05b99 / -— |
| Jogador 2 | 4-7 | 256 | SELL | FAST8 | 47.0 | 7 | 20 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02320774644613266 | 0.0 | 0.0 | +— / -8b75555c-d84d-4b8a-8d6c-012585a05b99 |
| Jogador 2 | 4-7 | 257 | BUY | FAST8 | 47.0 | 7 | 22 | 2 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2654106020927429 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -— |
| Jogador 2 | 4-7 | 258 | SELL | FAST8 | 47.0 | 7 | 20 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 |
| Jogador 2 | 4-7 | 259 | BUY | FAST8 | 47.0 | 7 | 22 | 2 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2330828458070755 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 2 | 4-7 | 260 | MOVE_BOARD | FAST8 | 47.0 | 7 | 21 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 47.0 | 7 | 28 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14753475785255432 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 47.0 | 7 | 28 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14728902280330658 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | SELL | FAST8 | 47.0 | 7 | 28 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -18e21ac6-f873-4310-95c8-bd8e62612479 |
| Jogador 2 | 5-1 | 265 | BUY | FAST8 | 47.0 | 7 | 29 | 2 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3297414183616638 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 2 | 5-1 | 266 | SELL | FAST8 | 47.0 | 7 | 26 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4073333442211151 | 0.0 | 0.0 | +— / -ff0d9869-c346-4210-be85-1e802a25dd8b |
| Jogador 2 | 5-1 | 267 | BUY | FAST8 | 47.0 | 7 | 28 | 2 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23108753561973572 | 0.0 | 0.0 | +a64cf09b-42bf-494e-9603-d387b6740200 / -— |
| Jogador 2 | 5-1 | 268 | SELL | FAST8 | 47.0 | 7 | 25 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -a15ff9dc-bf8a-49e0-9893-f92a212263d8 |
| Jogador 2 | 5-1 | 269 | BUY | FAST8 | 47.0 | 7 | 27 | 2 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17365165054798126 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 2 | 5-1 | 270 | MOVE_BOARD | FAST8 | 47.0 | 7 | 22 | 2 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001733462791889906 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 272 | SELL | FAST8 | 47.0 | 7 | 31 | 3 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0052999998442828655 | 0.0 | 0.0 | +— / -5754c4b4-0a7d-49e5-93e4-b144c3090a41 |
| Jogador 2 | 5-2 | 273 | BUY | FAST8 | 47.0 | 7 | 36 | 3 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2610898017883301 | 0.0 | 0.0 | +9414ca8e-930e-4a0e-8cbd-42d8997d8705 / -— |
| Jogador 2 | 5-2 | 274 | SELL | FAST8 | 47.0 | 7 | 33 | 3 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12783333659172058 | 0.0 | 0.0 | +— / -9414ca8e-930e-4a0e-8cbd-42d8997d8705 |
| Jogador 2 | 5-2 | 275 | BUY | FAST8 | 47.0 | 7 | 36 | 3 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.046222321689128876 | 0.0 | 0.0 | +da6c9f59-1fc3-467d-8845-bf7b38b4232c / -— |
| Jogador 2 | 5-2 | 276 | SELL | FAST8 | 47.0 | 7 | 33 | 3 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -da6c9f59-1fc3-467d-8845-bf7b38b4232c |
| Jogador 2 | 5-2 | 277 | BUY | FAST8 | 47.0 | 7 | 36 | 3 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019275780767202377 | 0.0 | 0.0 | +79b461e3-2c4f-40a2-b967-e0b6d5248bf6 / -— |
| Jogador 2 | 5-2 | 278 | SELL | FAST8 | 47.0 | 7 | 32 | 3 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -79b461e3-2c4f-40a2-b967-e0b6d5248bf6 |
| Jogador 2 | 5-2 | 279 | BUY | FAST8 | 47.0 | 7 | 36 | 3 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26688167452812195 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -— |
| Jogador 2 | 5-2 | 280 | SELL | FAST8 | 47.0 | 7 | 34 | 3 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 2 | 5-3 | 282 | BUY | FAST8 | 47.0 | 7 | 46 | 4 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8976417183876038 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -734c25e1-eddf-4452-a04a-1b39db3b94d0,74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 2 | 5-3 | 283 | BUY | FAST8 | 47.0 | 7 | 43 | 4 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1579539030790329 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 2 | 5-3 | 284 | BUY | FAST8 | 47.0 | 7 | 40 | 4 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17409105598926544 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 2 | 5-3 | 285 | SELL | FAST8 | 47.0 | 7 | 37 | 3 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -e1055913-2340-4af0-8527-e175c8bc1ccb |
| Jogador 2 | 5-3 | 286 | BUY | FAST8 | 47.0 | 7 | 45 | 4 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10113614052534103 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 2 | 5-3 | 287 | SELL | FAST8 | 47.0 | 7 | 43 | 4 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -4b1f1146-d580-41e9-987f-c32b1eb98b75 |
| Jogador 2 | 5-3 | 288 | BUY | FAST8 | 47.0 | 7 | 45 | 4 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1011352464556694 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -— |
| Jogador 2 | 5-3 | 289 | MOVE_BOARD | FAST8 | 47.0 | 7 | 43 | 4 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 290 | MOVE_BOARD | FAST8 | 47.0 | 7 | 43 | 4 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009943023324012756 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 292 | SELL | STABILIZE | 33.0 | 7 | 52 | 5 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -f84cc827-410f-47eb-bd95-bd650acfdd4b |
| Jogador 2 | 5-4 | 293 | BUY | STABILIZE | 33.0 | 7 | 54 | 5 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.021299123764038 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -7fb0217d-521c-42b5-995c-81e299b3b934,f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 5-4 | 294 | BUY | STABILIZE | 33.0 | 7 | 53 | 5 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4734167456626892 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -— |
| Jogador 2 | 5-4 | 295 | BUY | STABILIZE | 33.0 | 7 | 50 | 5 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1266831010580063 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 2 | 5-4 | 296 | SELL | STABILIZE | 33.0 | 7 | 45 | 4 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8374999761581421 | 0.0 | 0.0 | +— / -57ba484a-6228-4263-8171-00a8a5893bea |
| Jogador 2 | 5-4 | 297 | BUY | STABILIZE | 33.0 | 7 | 48 | 4 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004845115821808577 | 0.0 | 0.0 | +0c96798c-ee23-488b-974f-74e8e3da6aa6 / -— |
| Jogador 2 | 5-4 | 298 | SELL | STABILIZE | 33.0 | 7 | 46 | 4 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0022784178145229816 | 0.0 | 0.0 | +— / -0c96798c-ee23-488b-974f-74e8e3da6aa6 |
| Jogador 2 | 5-4 | 299 | BUY | STABILIZE | 33.0 | 7 | 48 | 4 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03638715669512749 | 0.0 | 0.0 | +eb418af1-c963-4da2-b052-86a153fc5ba1 / -— |
| Jogador 2 | 5-4 | 300 | MOVE_BOARD | STABILIZE | 33.0 | 7 | 47 | 4 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 302 | SELL | STABILIZE | 33.0 | 8 | 56 | 5 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -eb418af1-c963-4da2-b052-86a153fc5ba1 |
| Jogador 2 | 5-5 | 303 | BUY | STABILIZE | 33.0 | 8 | 57 | 5 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8555812239646912 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 2 | 5-5 | 304 | SELL | STABILIZE | 33.0 | 8 | 53 | 5 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005500408820807934 | 0.0 | 0.0 | +— / -973ba75e-ffa8-41f5-a3fb-e238e34d0216 |
| Jogador 2 | 5-5 | 305 | BUY | STABILIZE | 33.0 | 8 | 56 | 5 | 36.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35478565096855164 | 0.0 | 0.0 | +95a2e19e-619f-4497-ba52-e9bbf06b364f / -— |
| Jogador 2 | 5-5 | 306 | MOVE_BENCH | STABILIZE | 33.0 | 8 | 53 | 5 | 36.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4208795428276062 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 307 | BUY | STABILIZE | 33.0 | 8 | 53 | 5 | 42.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21049821376800537 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -— |
| Jogador 2 | 5-5 | 308 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 50 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 309 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 50 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499240007251501 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 310 | PASS | STABILIZE | 33.0 | 8 | 50 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1114666685461998 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 312 | SELL | STABILIZE | 33.0 | 8 | 60 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -0e5921d4-a056-4f42-951e-93de5f2834bb |
| Jogador 2 | 5-6 | 313 | BUY | STABILIZE | 33.0 | 8 | 63 | 5 | 42.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36532989144325256 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 2 | 5-6 | 314 | SELL | STABILIZE | 33.0 | 8 | 59 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42937877774238586 | 0.0 | 0.0 | +— / -91966802-adc2-46d2-9e7e-194283bca85c |
| Jogador 2 | 5-6 | 315 | BUY | STABILIZE | 33.0 | 8 | 62 | 5 | 42.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016040781512856483 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 2 | 5-6 | 316 | SELL | STABILIZE | 33.0 | 8 | 58 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003912182990461588 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 2 | 5-6 | 317 | BUY | STABILIZE | 33.0 | 8 | 62 | 5 | 42.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025355160236358643 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 2 | 5-6 | 318 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 59 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00022565036488231272 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 319 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 59 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014738375321030617 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 320 | PASS | STABILIZE | 33.0 | 8 | 59 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11954674124717712 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 322 | SELL | STABILIZE | 33.0 | 8 | 70 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0027547909412533045 | 0.0 | 0.0 | +— / -0a29573e-2a7b-4719-9b6e-49c2f476bc04 |
| Jogador 2 | 5-7 | 323 | BUY | STABILIZE | 33.0 | 8 | 73 | 5 | 42.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.023734450340271 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -b5b3098f-d48c-42b8-8022-639a25225980,cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 2 | 5-7 | 324 | MOVE_BENCH | STABILIZE | 33.0 | 8 | 70 | 5 | 30.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23352652788162231 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 325 | BUY | STABILIZE | 33.0 | 8 | 70 | 5 | 38.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8780649304389954 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 2 | 5-7 | 326 | MOVE_BENCH | STABILIZE | 33.0 | 8 | 67 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5076181888580322 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 327 | BUY | STABILIZE | 33.0 | 8 | 67 | 5 | 44.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23952727019786835 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -— |
| Jogador 2 | 5-7 | 328 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 62 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003282112069427967 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 329 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 62 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 330 | PASS | STABILIZE | 33.0 | 8 | 62 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12246720492839813 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 332 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 8 | 72 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08335704356431961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 333 | SELL | STABILIZE | 33.0 | 8 | 72 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -68a0405b-6231-471f-98a5-1661d32f4ac4 |
| Jogador 2 | 6-1 | 334 | BUY | STABILIZE | 33.0 | 8 | 80 | 5 | 44.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09746475517749786 | 0.0 | 0.0 | +85d35881-ba70-4310-8d5f-bae796309eed / -— |
| Jogador 2 | 6-1 | 335 | SELL | STABILIZE | 33.0 | 8 | 76 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -85d35881-ba70-4310-8d5f-bae796309eed |
| Jogador 2 | 6-1 | 336 | BUY | STABILIZE | 33.0 | 8 | 80 | 5 | 44.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02817043475806713 | 0.0 | 0.0 | +9af00d66-f862-45b7-98d4-93fbd69fedba / -— |
| Jogador 2 | 6-1 | 337 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 76 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2577098608016968 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 338 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 76 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10779447853565216 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 339 | MOVE_BENCH | STABILIZE | 33.0 | 8 | 76 | 5 | 44.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21751388907432556 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 340 | SELL | STABILIZE | 33.0 | 8 | 76 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024432819336652756 | 0.0 | 0.0 | +— / -fb551efa-6ad5-4f97-aa05-bc5eb70943d4 |
| Jogador 2 | 6-2 | 342 | BUY | STABILIZE | 33.0 | 8 | 91 | 5 | 48.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15206454694271088 | 0.0 | 0.0 | +3a17cc98-2024-4ac0-b627-9a751d138cd9 / -— |
| Jogador 2 | 6-2 | 343 | SELL | STABILIZE | 33.0 | 8 | 89 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032474175095558167 | 0.0 | 0.0 | +— / -3a17cc98-2024-4ac0-b627-9a751d138cd9 |
| Jogador 2 | 6-2 | 344 | BUY | STABILIZE | 33.0 | 8 | 91 | 5 | 48.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015450781211256981 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -— |
| Jogador 2 | 6-2 | 345 | BUY_XP | STABILIZE | 33.0 | 8 | 87 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.064472496509552 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 346 | BUY_XP | STABILIZE | 33.0 | 8 | 83 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06390249729156494 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 347 | BUY_XP | STABILIZE | 33.0 | 8 | 79 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06333249807357788 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 348 | BUY_XP | STABILIZE | 33.0 | 8 | 75 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06276249885559082 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 349 | BUY_XP | STABILIZE | 33.0 | 8 | 71 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06219249963760376 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 350 | BUY_XP | STABILIZE | 33.0 | 8 | 67 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0616225004196167 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 352 | SELL | STABILIZE | 33.0 | 8 | 75 | 5 | 48.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -9af00d66-f862-45b7-98d4-93fbd69fedba |
| Jogador 2 | 6-3 | 353 | BUY | STABILIZE | 33.0 | 8 | 79 | 5 | 48.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9547277688980103 | 0.0 | 0.0 | +94e47e85-54f4-4546-af6a-3700e3c325a8 / -0b38218d-9c50-41ac-b761-115c054bf314,23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 6-3 | 354 | BUY | STABILIZE | 33.0 | 8 | 75 | 5 | 48.0 | Vivaz/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10181456804275513 | 0.0 | 0.0 | +158c7931-f8db-44bd-a279-53dd6e59b352 / -— |
| Jogador 2 | 6-3 | 355 | BUY | STABILIZE | 33.0 | 8 | 71 | 5 | 48.0 | Vivaz/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06856022775173187 | 0.0 | 0.0 | +40263a7a-96e9-4752-b149-8235892508e0 / -— |
| Jogador 2 | 6-3 | 356 | BUY_XP | STABILIZE | 33.0 | 8 | 68 | 5 | 48.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061765000224113464 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 357 | BUY_XP | STABILIZE | 33.0 | 8 | 64 | 5 | 48.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061195001006126404 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 358 | BUY_XP | STABILIZE | 33.0 | 8 | 60 | 5 | 48.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06062500178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 359 | BUY_XP | STABILIZE | 33.0 | 8 | 56 | 5 | 48.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04019999876618385 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 360 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 52 | 5 | 48.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 362 | SELL | STABILIZE | 33.0 | 8 | 64 | 5 | 48.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08616666495800018 | 0.0 | 0.0 | +— / -94e47e85-54f4-4546-af6a-3700e3c325a8 |
| Jogador 2 | 6-4 | 363 | BUY | STABILIZE | 33.0 | 8 | 75 | 5 | 48.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6302513480186462 | 0.0 | 0.0 | +b5e5c8e4-7fb5-4b4b-b284-f0794e78eadc / -— |
| Jogador 2 | 6-4 | 364 | SELL | STABILIZE | 33.0 | 8 | 72 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 2 | 6-4 | 365 | BUY | STABILIZE | 33.0 | 8 | 76 | 5 | 48.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17521430552005768 | 0.0 | 0.0 | +6f0b2edb-0f61-4838-b698-703f080582a1 / -— |
| Jogador 2 | 6-4 | 366 | SELL | STABILIZE | 33.0 | 8 | 72 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02524620108306408 | 0.0 | 0.0 | +— / -158c7931-f8db-44bd-a279-53dd6e59b352 |
| Jogador 2 | 6-4 | 367 | BUY | STABILIZE | 33.0 | 8 | 76 | 5 | 48.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07979441434144974 | 0.0 | 0.0 | +52799e57-7b54-4dc5-b7f8-c39c8f57e7fa / -— |
| Jogador 2 | 6-4 | 368 | SELL | STABILIZE | 33.0 | 8 | 72 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -52799e57-7b54-4dc5-b7f8-c39c8f57e7fa |
| Jogador 2 | 6-4 | 369 | BUY | STABILIZE | 33.0 | 8 | 76 | 5 | 48.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09021881967782974 | 0.0 | 0.0 | +ee093d10-ed4b-4e0e-8e0a-37247f9aa517 / -— |
| Jogador 2 | 6-4 | 370 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 72 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 372 | SELL | STABILIZE | 33.0 | 8 | 83 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -ee093d10-ed4b-4e0e-8e0a-37247f9aa517 |
| Jogador 2 | 6-5 | 373 | BUY | STABILIZE | 33.0 | 8 | 87 | 5 | 48.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9445378184318542 | 0.0 | 0.0 | +e8658026-70da-4dca-9f24-5a4aab392ddb / -— |
| Jogador 2 | 6-5 | 374 | SELL | STABILIZE | 33.0 | 8 | 84 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04124118760228157 | 0.0 | 0.0 | +— / -6f0b2edb-0f61-4838-b698-703f080582a1 |
| Jogador 2 | 6-5 | 375 | BUY | STABILIZE | 33.0 | 8 | 88 | 5 | 48.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4227614998817444 | 0.0 | 0.0 | +a960f5cb-d806-4d73-9146-244e1ecde6f2 / -— |
| Jogador 2 | 6-5 | 376 | SELL | STABILIZE | 33.0 | 8 | 85 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42998260259628296 | 0.0 | 0.0 | +— / -a960f5cb-d806-4d73-9146-244e1ecde6f2 |
| Jogador 2 | 6-5 | 377 | BUY | STABILIZE | 33.0 | 8 | 88 | 5 | 48.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09034562855958939 | 0.0 | 0.0 | +389bcf7d-1a3c-4360-8bcf-a98cacecbaea / -— |
| Jogador 2 | 6-5 | 378 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 85 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002921982668340206 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 379 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 85 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01822335459291935 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 380 | MOVE_BOARD | STABILIZE | 33.0 | 8 | 85 | 5 | 48.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4068913459777832 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.039654016494751 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179771423339844 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5892800092697144 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22632597386837006 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21145518124103546 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2642599940299988 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39558395743370056 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21892458200454712 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007771904114633799 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012296375818550587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015378622338175774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 62 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 64 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.960719645023346 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 65 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3371342122554779 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 66 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33283865451812744 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26616108417510986 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 75 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8901258707046509 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 83 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 84 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8980405926704407 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9475498199462891 | 0.0 | 0.0 | +492fa74a-22b8-4f7d-a4f9-346fdcf565be / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-5 | 94 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 12.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7087386250495911 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4741053283214569 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020538339391350746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09967894107103348 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049516402184963226 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 99 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -492fa74a-22b8-4f7d-a4f9-346fdcf565be |
| Jogador 3 | 2-5 | 100 | BUY_XP | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 5 | 10 | 1 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8683999180793762 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 9 | 0 | 16.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43676409125328064 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 104 | BUY | STABILIZE | 90.0 | 5 | 9 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3551364541053772 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 105 | BUY | STABILIZE | 90.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002625571098178625 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 3 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012297529028728604 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02490667812526226 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 108 | PASS | STABILIZE | 90.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.820499062538147 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | STABILIZE | 84.0 | 5 | 8 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8886560797691345 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 114 | SELL | STABILIZE | 84.0 | 5 | 6 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00286666676402092 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 3 | 2-7 | 115 | BUY | STABILIZE | 84.0 | 5 | 8 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16189250349998474 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.551115123125783e-17 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007911337539553642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 118 | PASS | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23765182495117188 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 123 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 3-1 | 124 | BUY | STABILIZE | 84.0 | 5 | 14 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8143919110298157 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 13 | 1 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40503379702568054 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016572264954447746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 127 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4607555568218231 | 0.0 | 0.0 | +— / -2fa86b11-4e28-4652-890e-f00a79068223 |
| Jogador 3 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.644633412361145 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 129 | SELL | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5274560451507568 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-1 | 130 | BUY | STABILIZE | 84.0 | 5 | 19 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09884177893400192 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-2 | 132 | BUY | STABILIZE | 74.0 | 5 | 23 | 2 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25702425837516785 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 133 | MOVE_BENCH | STABILIZE | 74.0 | 5 | 20 | 2 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6370076537132263 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 74.0 | 5 | 20 | 2 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40302368998527527 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 135 | PASS | STABILIZE | 74.0 | 5 | 20 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | MOVE_BENCH | STABILIZE | 65.0 | 6 | 29 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4248037040233612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 143 | BUY | STABILIZE | 65.0 | 6 | 29 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003091435879468918 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 144 | BUY | STABILIZE | 65.0 | 6 | 25 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24511918425559998 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BENCH | STABILIZE | 65.0 | 6 | 22 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3993009030818939 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | BUY_XP | STABILIZE | 65.0 | 6 | 22 | 2 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | BUY_XP | STABILIZE | 65.0 | 6 | 18 | 1 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 148 | BUY_XP | STABILIZE | 65.0 | 6 | 14 | 1 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 149 | BUY_XP | STABILIZE | 65.0 | 6 | 10 | 1 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 150 | BUY_XP | STABILIZE | 65.0 | 6 | 6 | 0 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | BUY | STABILIZE | 65.0 | 6 | 8 | 0 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6086833477020264 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 153 | SELL | STABILIZE | 65.0 | 6 | 5 | 0 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 |
| Jogador 3 | 3-4 | 154 | BUY | STABILIZE | 65.0 | 6 | 8 | 0 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2010740041732788 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 155 | BUY_XP | STABILIZE | 65.0 | 6 | 5 | 0 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 1 | 0 | 32.0 | Devastador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 1 | 0 | 32.0 | Devastador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 158 | PASS | STABILIZE | 65.0 | 6 | 1 | 0 | 32.0 | Devastador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | SELL | STABILIZE | 65.0 | 6 | 6 | 0 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010833333246409893 | 0.0 | 0.0 | +— / -e8b0d22c-35bc-459e-a90c-7db13fcbe34f |
| Jogador 3 | 3-5 | 163 | BUY | STABILIZE | 65.0 | 6 | 9 | 0 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7377579808235168 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 65.0 | 6 | 6 | 0 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07778818905353546 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 165 | BUY | STABILIZE | 65.0 | 6 | 6 | 0 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22259938716888428 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 166 | BUY | STABILIZE | 65.0 | 6 | 3 | 0 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01062069833278656 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -— |
| Jogador 3 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 1 | 0 | 28.0 | Devastador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00010802772885654122 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 1 | 0 | 28.0 | Devastador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015360520221292973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 169 | PASS | STABILIZE | 65.0 | 6 | 1 | 0 | 28.0 | Devastador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | SELL | STABILIZE | 54.0 | 6 | 6 | 0 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025105908513069153 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-6 | 173 | BUY | STABILIZE | 54.0 | 6 | 14 | 1 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.80648273229599 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 174 | SELL | STABILIZE | 54.0 | 6 | 13 | 1 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023126717656850815 | 0.0 | 0.0 | +— / -65a6d68c-90ae-4e31-8bbc-82e8ec75b3de |
| Jogador 3 | 3-6 | 175 | BUY | STABILIZE | 54.0 | 6 | 15 | 1 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7401599287986755 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 176 | SELL | STABILIZE | 54.0 | 6 | 12 | 1 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045499999076128006 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 3 | 3-6 | 177 | BUY | STABILIZE | 54.0 | 6 | 15 | 1 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8325982689857483 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0,bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 3 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 54.0 | 6 | 13 | 1 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 54.0 | 6 | 13 | 1 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01553304959088564 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 180 | PASS | STABILIZE | 54.0 | 6 | 13 | 1 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | BUY | STABILIZE | 43.0 | 6 | 20 | 2 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08922301232814789 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 183 | BUY | STABILIZE | 43.0 | 6 | 17 | 1 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.242402583360672 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 184 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 14 | 1 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006542146438732743 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 14 | 1 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 14 | 1 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014759103767573833 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 187 | PASS | STABILIZE | 43.0 | 6 | 14 | 1 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 43.0 | 6 | 21 | 2 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18210986256599426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 43.0 | 6 | 21 | 2 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07001886516809464 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | SELL | STABILIZE | 43.0 | 6 | 21 | 2 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -0e31b1ec-3ead-480e-8577-f59bb5486d00 |
| Jogador 3 | 4-1 | 195 | BUY | STABILIZE | 43.0 | 6 | 26 | 2 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8326498866081238 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9,b75c9bc5-9bc7-465a-a97c-59156e5c482d |
| Jogador 3 | 4-1 | 196 | BUY | STABILIZE | 43.0 | 6 | 23 | 2 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4464563727378845 | 0.0 | 0.0 | +9175d2a8-4736-402d-873b-cf4846b04d97 / -— |
| Jogador 3 | 4-1 | 197 | BUY | STABILIZE | 43.0 | 6 | 20 | 2 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26168814301490784 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 3 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 16 | 1 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.9465962395770475e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 16 | 1 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014455718919634819 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 200 | PASS | STABILIZE | 43.0 | 6 | 16 | 1 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026425397023558617 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | SELL | STABILIZE | 43.0 | 7 | 23 | 2 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028757380321621895 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 3 | 4-2 | 203 | BUY | STABILIZE | 43.0 | 7 | 31 | 3 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3765527606010437 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 3 | 4-2 | 204 | MOVE_BENCH | STABILIZE | 43.0 | 7 | 27 | 2 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4706985056400299 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 205 | BUY | STABILIZE | 43.0 | 7 | 27 | 2 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.277217298746109 | 0.0 | 0.0 | +cb216a0d-8bff-41f9-99bd-231ca5186fb5 / -— |
| Jogador 3 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 25 | 2 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.0789488189620897e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 25 | 2 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015163120813667774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 25 | 2 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497601717710495 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 209 | PASS | STABILIZE | 43.0 | 7 | 25 | 2 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03392063453793526 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 212 | SELL | STABILIZE | 43.0 | 7 | 34 | 3 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 4-3 | 213 | BUY | STABILIZE | 43.0 | 7 | 37 | 3 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0033413616474717855 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 3 | 4-3 | 214 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 34 | 3 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.62662719655782e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 215 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 34 | 3 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 216 | PASS | STABILIZE | 43.0 | 7 | 34 | 3 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041415873914957047 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 222 | SELL | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010310470126569271 | 0.0 | 0.0 | +— / -26462e09-ab6e-4b87-85a8-6bda974b0c45 |
| Jogador 3 | 4-4 | 223 | BUY | STABILIZE | 32.0 | 7 | 45 | 4 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009959490969777107 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 3 | 4-4 | 224 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.635022378352005e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 225 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014845922589302063 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 226 | SELL | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022099999710917473 | 0.0 | 0.0 | +— / -ad19ac66-9f86-4c29-8ae7-7222164aece1 |
| Jogador 3 | 4-4 | 227 | BUY | STABILIZE | 32.0 | 7 | 45 | 4 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2118230164051056 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 3 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.4640223273308948e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 229 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015207957476377487 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 230 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497076079249382 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 232 | SELL | STABILIZE | 32.0 | 7 | 51 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009728331118822098 | 0.0 | 0.0 | +— / -b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 3 | 4-5 | 233 | BUY | STABILIZE | 32.0 | 7 | 54 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8815949559211731 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 3 | 4-5 | 234 | SELL | STABILIZE | 32.0 | 7 | 52 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09613333642482758 | 0.0 | 0.0 | +— / -cb216a0d-8bff-41f9-99bd-231ca5186fb5 |
| Jogador 3 | 4-5 | 235 | BUY | STABILIZE | 32.0 | 7 | 54 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8255401253700256 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -9175d2a8-4736-402d-873b-cf4846b04d97,bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-5 | 236 | BUY | STABILIZE | 32.0 | 7 | 51 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1423177868127823 | 0.0 | 0.0 | +fcc4f620-7b85-40ed-a42c-2eadd37a82fd / -— |
| Jogador 3 | 4-5 | 237 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 48 | 4 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 48 | 4 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014719449914991856 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 239 | PASS | STABILIZE | 32.0 | 7 | 48 | 4 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2116825431585312 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | BUY | ALL_IN | 21.0 | 7 | 58 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0197227001190186 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -79786887-d318-4836-b2f0-c0f03e86cbe5,8a68772c-3f02-4f2e-882b-4fa69fbb6750 |
| Jogador 3 | 4-6 | 243 | BUY | ALL_IN | 21.0 | 7 | 55 | 5 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4688176214694977 | 0.0 | 0.0 | +738fea60-6b44-40f1-9936-43accf852bd7 / -— |
| Jogador 3 | 4-6 | 244 | MOVE_BENCH | ALL_IN | 21.0 | 7 | 54 | 5 | 24.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40214625000953674 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 245 | BUY | ALL_IN | 21.0 | 7 | 54 | 5 | 36.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786441057920456 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 3 | 4-6 | 246 | MOVE_BOARD | ALL_IN | 21.0 | 7 | 51 | 5 | 36.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 247 | MOVE_BOARD | ALL_IN | 21.0 | 7 | 51 | 5 | 36.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015141806565225124 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 248 | PASS | ALL_IN | 21.0 | 7 | 51 | 5 | 36.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44352656602859497 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 252 | SELL | ALL_IN | 9.0 | 7 | 62 | 5 | 36.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7251999974250793 | 0.0 | 0.0 | +— / -f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 3 | 4-7 | 253 | BUY | ALL_IN | 9.0 | 7 | 70 | 5 | 36.0 | Devastador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0713683366775513 | 0.0 | 0.0 | +b9b38183-663e-43a4-9f9d-02f1bd4d2d24 / -111acae7-a889-409f-a15e-419d250fccd0,41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 4-7 | 254 | BUY | ALL_IN | 9.0 | 7 | 68 | 5 | 36.0 | Devastador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7620806097984314 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 3 | 4-7 | 255 | BUY | ALL_IN | 9.0 | 7 | 64 | 5 | 36.0 | Devastador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.3832351863384247 | 0.0 | 0.0 | +d366508d-f33b-485a-8ff3-e5d0a248ae3e / -— |
| Jogador 3 | 4-7 | 256 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 7 | 61 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1575479954481125 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 257 | MOVE_BOARD | ALL_IN | 9.0 | 7 | 61 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.052564226090908e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 258 | MOVE_BOARD | ALL_IN | 9.0 | 7 | 61 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 259 | REROLL | ALL_IN | 9.0 | 7 | 61 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 260 | SELL | ALL_IN | 9.0 | 7 | 59 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7213000059127808 | 0.0 | 0.0 | +— / -b9b38183-663e-43a4-9f9d-02f1bd4d2d24 |
| Jogador 3 | 5-1 | 262 | BUY | ALL_IN | 9.0 | 7 | 75 | 5 | 36.0 | Devastador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9006636142730713 | 0.0 | 0.0 | +0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c / -— |
| Jogador 3 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 9.0 | 7 | 74 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13760946691036224 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 264 | CRAFT_AND_EQUIP | ALL_IN | 9.0 | 7 | 74 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10379872471094131 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 265 | SELL | ALL_IN | 9.0 | 7 | 74 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021994005888700485 | 0.0 | 0.0 | +— / -98b72340-a402-45bc-9493-71263e3168d6 |
| Jogador 3 | 5-1 | 266 | BUY | ALL_IN | 9.0 | 7 | 77 | 5 | 36.0 | Devastador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4097760319709778 | 0.0 | 0.0 | +685fc2a9-6a67-445e-ab34-59ec1f986f8e / -— |
| Jogador 3 | 5-1 | 267 | SELL | ALL_IN | 9.0 | 7 | 75 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11779999732971191 | 0.0 | 0.0 | +— / -685fc2a9-6a67-445e-ab34-59ec1f986f8e |
| Jogador 3 | 5-1 | 268 | BUY | ALL_IN | 9.0 | 7 | 77 | 5 | 36.0 | Devastador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06828464567661285 | 0.0 | 0.0 | +952ea2b4-387d-455d-b1ad-fb0de8c46e47 / -— |
| Jogador 3 | 5-1 | 269 | REROLL | ALL_IN | 9.0 | 7 | 74 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 270 | SELL | ALL_IN | 9.0 | 7 | 72 | 5 | 36.0 | Devastador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02369861677289009 | 0.0 | 0.0 | +— / -952ea2b4-387d-455d-b1ad-fb0de8c46e47 |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46534693241119385 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1641255021095276 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0601743720471859 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128071308135986 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33921104669570923 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9802227020263672 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18400593101978302 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21635636687278748 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 57 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3917297422885895 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 64 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9556944966316223 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 65 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9438979625701904 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0434505939483643 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3042053282260895 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 75 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 76 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10035749524831772 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 80 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13735529780387878 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23763148486614227 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 89 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2500207722187042 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 90 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9549816846847534 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0011732578277588 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3844694197177887 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 94 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20775020122528076 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 96 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2166292667388916 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3975071609020233 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5793930888175964 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01303399633616209 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3260316848754883 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 103 | BUY | STABILIZE | 90.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2837255597114563 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008337188512086868 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014826050959527493 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01666545867919922 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 107 | PASS | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 112 | BUY | STABILIZE | 83.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9389603734016418 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 113 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3618030250072479 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 114 | BUY_XP | STABILIZE | 83.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 115 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2590000033378601 | 0.0 | 0.0 | +— / -5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 2-7 | 116 | SELL | STABILIZE | 83.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5897884964942932 | 0.0 | 0.0 | +— / -814d07bd-0296-44af-9626-26a8a224d86f |
| Jogador 4 | 2-7 | 117 | BUY | STABILIZE | 83.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13401184976100922 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 4 | 2-7 | 118 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15007710456848145 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 2-7 | 119 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39851123094558716 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 122 | BUY | STABILIZE | 83.0 | 6 | 9 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8029270172119141 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 123 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2251192033290863 | 0.0 | 0.0 | +cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 / -— |
| Jogador 4 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 83.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24341042339801788 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 125 | BUY_XP | STABILIZE | 83.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 126 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11922940611839294 | 0.0 | 0.0 | +— / -cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 |
| Jogador 4 | 3-1 | 127 | SELL | STABILIZE | 83.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 4 | 3-1 | 128 | BUY | STABILIZE | 83.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04824843630194664 | 0.0 | 0.0 | +31aa0a5f-4d66-48c2-b6d4-b76ac220c752 / -— |
| Jogador 4 | 3-1 | 129 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09845808893442154 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 130 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39075928926467896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 83.0 | 6 | 8 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379985094070435 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2299346774816513 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 134 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28799891471862793 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.605002224445343 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 6 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 6 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01846756599843502 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 138 | PASS | STABILIZE | 83.0 | 6 | 6 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | STABILIZE | 72.0 | 6 | 11 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7548127174377441 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -8052731e-e34c-4de7-84b1-2b986cfeddaa,c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 3-3 | 143 | BUY | STABILIZE | 72.0 | 6 | 9 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7717025279998779 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 144 | BUY | STABILIZE | 72.0 | 6 | 6 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17191413044929504 | 0.0 | 0.0 | +e2ed7625-f3aa-43f0-936b-7322cb9d16f1 / -— |
| Jogador 4 | 3-3 | 145 | SELL | STABILIZE | 72.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -52018505-08c9-471f-83b9-fd5066efe55a |
| Jogador 4 | 3-3 | 146 | SELL | STABILIZE | 72.0 | 6 | 9 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03500000014901161 | 0.0 | 0.0 | +— / -31aa0a5f-4d66-48c2-b6d4-b76ac220c752 |
| Jogador 4 | 3-3 | 147 | BUY | STABILIZE | 72.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17700156569480896 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 11 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003642295952886343 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 11 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 11 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015140553936362267 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | BUY | STABILIZE | 60.0 | 6 | 18 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.738166093826294 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 153 | BUY | STABILIZE | 60.0 | 6 | 17 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2812280058860779 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 154 | BUY | STABILIZE | 60.0 | 6 | 14 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2832888662815094 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 155 | MOVE_BOARD | STABILIZE | 60.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00010775929695228115 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 156 | BUY | STABILIZE | 60.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24064435064792633 | 0.0 | 0.0 | +e01be6cf-34fe-4057-aef3-c08c504794cf / -— |
| Jogador 4 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 60.0 | 6 | 10 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20228411257266998 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 60.0 | 6 | 10 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 159 | PASS | STABILIZE | 60.0 | 6 | 10 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | BUY | STABILIZE | 60.0 | 6 | 17 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8029260635375977 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 163 | SELL | STABILIZE | 60.0 | 6 | 15 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12610000371932983 | 0.0 | 0.0 | +— / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc |
| Jogador 4 | 3-5 | 164 | BUY | STABILIZE | 60.0 | 6 | 18 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2246946543455124 | 0.0 | 0.0 | +805375b9-df52-4342-b581-4b92fcd12033 / -— |
| Jogador 4 | 3-5 | 165 | SELL | STABILIZE | 60.0 | 6 | 15 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -805375b9-df52-4342-b581-4b92fcd12033 |
| Jogador 4 | 3-5 | 166 | BUY | STABILIZE | 60.0 | 6 | 18 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059331461787223816 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 4 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 60.0 | 6 | 15 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 168 | SELL | STABILIZE | 60.0 | 6 | 15 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010376463644206524 | 0.0 | 0.0 | +— / -62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 |
| Jogador 4 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 60.0 | 6 | 18 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1892310231924057 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 170 | MOVE_BOARD | STABILIZE | 60.0 | 6 | 18 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0024173702113330364 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | BUY | STABILIZE | 49.0 | 6 | 25 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8497429490089417 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -7fd03119-ac82-49e1-b3bb-3a0caa31011f,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 3-6 | 173 | BUY | STABILIZE | 49.0 | 6 | 23 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10881156474351883 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 174 | BUY | STABILIZE | 49.0 | 6 | 20 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010494555346667767 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -— |
| Jogador 4 | 3-6 | 175 | SELL | STABILIZE | 49.0 | 6 | 19 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -23f4d10f-2614-47b2-bfb2-4fb276764b5e |
| Jogador 4 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 24 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013668438186869025 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 24 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014830400235950947 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 24 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014917723834514618 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 179 | PASS | STABILIZE | 49.0 | 6 | 24 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | BUY | STABILIZE | 39.0 | 6 | 32 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.659469723701477 | 0.0 | 0.0 | +e3fdce1f-991f-4305-9aaa-fbf72ede6c01 / -— |
| Jogador 4 | 3-7 | 183 | SELL | STABILIZE | 39.0 | 6 | 31 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04158266633749008 | 0.0 | 0.0 | +— / -8e1a5a7a-d27d-47c9-a197-b383c1c3da3b |
| Jogador 4 | 3-7 | 184 | BUY | STABILIZE | 39.0 | 6 | 34 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2999705374240875 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -— |
| Jogador 4 | 3-7 | 185 | SELL | STABILIZE | 39.0 | 6 | 31 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12610000371932983 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 3-7 | 186 | BUY | STABILIZE | 39.0 | 6 | 34 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006193942856043577 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 4 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 39.0 | 6 | 32 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005960733979009092 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 39.0 | 6 | 32 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014972459524869919 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 189 | PASS | STABILIZE | 39.0 | 6 | 32 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031475555151700974 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 39.0 | 6 | 41 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12659543752670288 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 39.0 | 6 | 41 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18531590700149536 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | SELL | STABILIZE | 39.0 | 6 | 41 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -eab06dbd-05d4-43b6-88f0-e6abb0e83d34 |
| Jogador 4 | 4-1 | 195 | BUY | STABILIZE | 39.0 | 6 | 43 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8663684129714966 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -320038b5-88c4-48fe-a7fa-a30823d674c0,e3fdce1f-991f-4305-9aaa-fbf72ede6c01 |
| Jogador 4 | 4-1 | 196 | BUY | STABILIZE | 39.0 | 6 | 42 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007061793003231287 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 4 | 4-1 | 197 | BUY | STABILIZE | 39.0 | 6 | 40 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30549126863479614 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -— |
| Jogador 4 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 39.0 | 6 | 37 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 39.0 | 6 | 37 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 200 | PASS | STABILIZE | 39.0 | 6 | 37 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0503142848610878 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | SELL | STABILIZE | 26.0 | 6 | 47 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015466511249542236 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 4 | 4-2 | 203 | BUY | STABILIZE | 26.0 | 6 | 50 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2718077301979065 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 4 | 4-2 | 204 | SELL | STABILIZE | 26.0 | 6 | 48 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05806666612625122 | 0.0 | 0.0 | +— / -60255a84-4f78-49f0-a4f1-d598704c7ee7 |
| Jogador 4 | 4-2 | 205 | BUY | STABILIZE | 26.0 | 6 | 50 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15712064504623413 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 4 | 4-2 | 206 | SELL | STABILIZE | 26.0 | 6 | 49 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08250000327825546 | 0.0 | 0.0 | +— / -0c07379e-5dd1-42e9-aa7a-a764f949deee |
| Jogador 4 | 4-2 | 207 | BUY | STABILIZE | 26.0 | 6 | 52 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7609246969223022 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -— |
| Jogador 4 | 4-2 | 208 | SELL | STABILIZE | 26.0 | 6 | 51 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -d71a866d-0c5a-41c2-9996-0e179f062aa2 |
| Jogador 4 | 4-2 | 209 | BUY | STABILIZE | 26.0 | 6 | 52 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036031078547239304 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 4 | 4-2 | 210 | MOVE_BOARD | STABILIZE | 26.0 | 6 | 49 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00041674711974337697 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 212 | SELL | ALL_IN | 14.0 | 6 | 61 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03492196649312973 | 0.0 | 0.0 | +— / -9593a62e-442f-410a-8a0c-7d781e2487cc |
| Jogador 4 | 4-3 | 213 | BUY | ALL_IN | 14.0 | 6 | 64 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9348679184913635 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 4 | 4-3 | 214 | SELL | ALL_IN | 14.0 | 6 | 62 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6365951299667358 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 4-3 | 215 | BUY | ALL_IN | 14.0 | 6 | 63 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3961053490638733 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 4 | 4-3 | 216 | SELL | ALL_IN | 14.0 | 6 | 60 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06441431492567062 | 0.0 | 0.0 | +— / -d754fcfc-6d22-4bc0-8643-8f4bef9afda5 |
| Jogador 4 | 4-3 | 217 | BUY | ALL_IN | 14.0 | 6 | 61 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1382571905851364 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -— |
| Jogador 4 | 4-3 | 218 | SELL | ALL_IN | 14.0 | 6 | 58 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -333b0a0b-8868-40b2-96e9-71e468c5dd1f |
| Jogador 4 | 4-3 | 219 | BUY | ALL_IN | 14.0 | 6 | 61 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002142783021554351 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 4 | 4-3 | 220 | MOVE_BENCH | ALL_IN | 14.0 | 6 | 58 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7450336813926697 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 222 | SELL | ALL_IN | 1.0 | 7 | 71 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5164666771888733 | 0.0 | 0.0 | +— / -e01be6cf-34fe-4057-aef3-c08c504794cf |
| Jogador 4 | 4-4 | 223 | BUY | ALL_IN | 1.0 | 7 | 73 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1055408716201782 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -d8ecc66e-097d-4caa-a657-90fcd1286c2b,fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 4 | 4-4 | 224 | BUY | ALL_IN | 1.0 | 7 | 71 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19884198904037476 | 0.0 | 0.0 | +677ea844-e1bf-4c68-a0b0-136abb86ba7b / -— |
| Jogador 4 | 4-4 | 225 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 68 | 5 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.400483101606369 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 226 | BUY | ALL_IN | 1.0 | 7 | 68 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18591122329235077 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 4 | 4-4 | 227 | BUY | ALL_IN | 1.0 | 7 | 65 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19285739958286285 | 0.0 | 0.0 | +15c93ffb-d63e-43e6-aa46-ba2beed9cb53 / -— |
| Jogador 4 | 4-4 | 228 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 229 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015150720253586769 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 230 | PASS | ALL_IN | 1.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49334272742271423 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | SELL | ALL_IN | 1.0 | 7 | 75 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7437000274658203 | 0.0 | 0.0 | +— / -e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 |
| Jogador 4 | 4-5 | 233 | BUY | ALL_IN | 1.0 | 7 | 80 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5647261142730713 | 0.0 | 0.0 | +477a3c7c-70fe-4f67-ab00-8c9c397365bf / -— |
| Jogador 4 | 4-5 | 234 | SELL | ALL_IN | 1.0 | 7 | 77 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -b755a0c5-f515-4f95-8f58-1e05f40ad302 |
| Jogador 4 | 4-5 | 235 | BUY | ALL_IN | 1.0 | 7 | 80 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19511382281780243 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 4 | 4-5 | 236 | SELL | ALL_IN | 1.0 | 7 | 76 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012390876188874245 | 0.0 | 0.0 | +— / -15c93ffb-d63e-43e6-aa46-ba2beed9cb53 |
| Jogador 4 | 4-5 | 237 | BUY | ALL_IN | 1.0 | 7 | 79 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027902796864509583 | 0.0 | 0.0 | +8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e / -— |
| Jogador 4 | 4-5 | 238 | SELL | ALL_IN | 1.0 | 7 | 76 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0026158771943300962 | 0.0 | 0.0 | +— / -8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e |
| Jogador 4 | 4-5 | 239 | BUY | ALL_IN | 1.0 | 7 | 79 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028160227462649345 | 0.0 | 0.0 | +7643f027-a90f-4f3a-8b4c-7be4cba17f95 / -— |
| Jogador 4 | 4-5 | 240 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 76 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3949030637741089 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 242 | SELL | ALL_IN | 1.0 | 7 | 87 | 5 | 34.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002939061028882861 | 0.0 | 0.0 | +— / -7643f027-a90f-4f3a-8b4c-7be4cba17f95 |
| Jogador 4 | 4-6 | 243 | BUY | ALL_IN | 1.0 | 7 | 90 | 5 | 34.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0977907180786133 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -409b32b9-5280-4d79-b5b2-871ed597ba56,9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 4 | 4-6 | 244 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 87 | 5 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43068474531173706 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 245 | BUY | ALL_IN | 1.0 | 7 | 87 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08644530177116394 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -— |
| Jogador 4 | 4-6 | 246 | BUY | ALL_IN | 1.0 | 7 | 83 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10723866522312164 | 0.0 | 0.0 | +815aab3d-cea8-4ca6-aea3-3c9d656e6edd / -— |
| Jogador 4 | 4-6 | 247 | SELL | ALL_IN | 1.0 | 7 | 81 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7290580868721008 | 0.0 | 0.0 | +— / -772bccc4-15f4-4de2-95f8-82d0ed9a72d2 |
| Jogador 4 | 4-6 | 248 | EQUIP_FROM_INVENTORY | ALL_IN | 1.0 | 7 | 89 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09904606640338898 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 249 | EQUIP_FROM_INVENTORY | ALL_IN | 1.0 | 7 | 89 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07493061572313309 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 250 | BUY | ALL_IN | 1.0 | 7 | 89 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030494937673211098 | 0.0 | 0.0 | +99182042-c4b9-4801-b66a-1f4432d301f3 / -— |
| Jogador 4 | 4-7 | 252 | SELL | ALL_IN | 1.0 | 7 | 96 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015533333644270897 | 0.0 | 0.0 | +— / -815aab3d-cea8-4ca6-aea3-3c9d656e6edd |
| Jogador 4 | 4-7 | 253 | BUY | ALL_IN | 1.0 | 7 | 98 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9158186316490173 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 4 | 4-7 | 254 | SELL | ALL_IN | 1.0 | 7 | 95 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0027210176922380924 | 0.0 | 0.0 | +— / -99182042-c4b9-4801-b66a-1f4432d301f3 |
| Jogador 4 | 4-7 | 255 | BUY | ALL_IN | 1.0 | 7 | 98 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.100772500038147 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -a92eca5d-299f-4f4d-a16b-d23981ef719f,bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 4 | 4-7 | 256 | BUY | ALL_IN | 1.0 | 7 | 95 | 5 | 32.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22859525680541992 | 0.0 | 0.0 | +5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 / -— |
| Jogador 4 | 4-7 | 257 | BUY | ALL_IN | 1.0 | 7 | 94 | 5 | 32.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11306306719779968 | 0.0 | 0.0 | +e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b / -— |
| Jogador 4 | 4-7 | 258 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 91 | 5 | 32.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 259 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 91 | 5 | 32.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01505491603165865 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 260 | PASS | ALL_IN | 1.0 | 7 | 91 | 5 | 32.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5331358909606934 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 1.0 | 7 | 101 | 5 | 32.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14655543863773346 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 1.0 | 7 | 101 | 5 | 32.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09678439795970917 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 264 | SELL | ALL_IN | 1.0 | 7 | 101 | 5 | 32.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7476000189781189 | 0.0 | 0.0 | +— / -6eecc806-dcf8-47df-bc1d-bc5bc5f07099 |
| Jogador 4 | 5-1 | 265 | BUY | ALL_IN | 1.0 | 7 | 109 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23400254547595978 | 0.0 | 0.0 | +58cbdbde-2151-438c-8897-902bef9bcd92 / -— |
| Jogador 4 | 5-1 | 266 | SELL | ALL_IN | 1.0 | 7 | 106 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06151719391345978 | 0.0 | 0.0 | +— / -5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 |
| Jogador 4 | 5-1 | 267 | BUY | ALL_IN | 1.0 | 7 | 107 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18127009272575378 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 4 | 5-1 | 268 | SELL | ALL_IN | 1.0 | 7 | 104 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02016017958521843 | 0.0 | 0.0 | +— / -e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b |
| Jogador 4 | 5-1 | 269 | BUY | ALL_IN | 1.0 | 7 | 107 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06219366937875748 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -— |
| Jogador 4 | 5-1 | 270 | SELL | ALL_IN | 1.0 | 7 | 105 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009484252892434597 | 0.0 | 0.0 | +— / -b0c8ce74-5ce1-4ed0-82ac-f95013475f3c |
| Jogador 4 | 5-2 | 272 | BUY | ALL_IN | 1.0 | 7 | 119 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4063504636287689 | 0.0 | 0.0 | +99857cfa-b422-4167-bb01-d9fd94a55d88 / -— |
| Jogador 4 | 5-2 | 273 | SELL | ALL_IN | 1.0 | 7 | 116 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 |
| Jogador 4 | 5-2 | 274 | BUY | ALL_IN | 1.0 | 7 | 119 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9270064830780029 | 0.0 | 0.0 | +c8706680-2712-4914-b6c0-59bf92a2796d / -— |
| Jogador 4 | 5-2 | 275 | SELL | ALL_IN | 1.0 | 7 | 116 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04846666753292084 | 0.0 | 0.0 | +— / -58cbdbde-2151-438c-8897-902bef9bcd92 |
| Jogador 4 | 5-2 | 276 | BUY | ALL_IN | 1.0 | 7 | 119 | 5 | 32.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029076995328068733 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -— |
| Jogador 4 | 5-2 | 277 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 117 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08304324746131897 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 278 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 117 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.702579915523529 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 279 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 117 | 5 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11416268348693848 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 280 | PASS | ALL_IN | 1.0 | 7 | 117 | 5 | 32.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5953001976013184 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43023744225502014 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21626177430152893 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3297761380672455 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2880711853504181 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.032692790031433 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19865769147872925 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2126627266407013 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4088355004787445 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22647081315517426 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 59 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 64 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.972019612789154 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 65 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 66 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441185235977173 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12275639176368713 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 75 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2461189180612564 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4363241195678711 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16280071437358856 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25775080919265747 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 80 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31068703532218933 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21857225894927979 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 85 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08825498074293137 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 86 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 87 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09729351848363876 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 88 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10471328347921371 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-4 | 89 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18893152475357056 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 90 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1796523481607437 | 0.0 | 0.0 | +32b7b452-7702-43a3-b3c4-8eda786225b9 / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26717609167099 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32465675473213196 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 5 | 2-5 | 94 | SELL | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030366666615009308 | 0.0 | 0.0 | +— / -32b7b452-7702-43a3-b3c4-8eda786225b9 |
| Jogador 5 | 2-5 | 95 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 96 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030533334240317345 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-5 | 97 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40817776322364807 | 0.0 | 0.0 | +— / -de78e1b7-ed58-42dd-8374-76b578543e94 |
| Jogador 5 | 2-5 | 98 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0983823761343956 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3566199839115143 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015697868540883064 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021104255691170692 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05602027103304863 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 105 | SELL | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 106 | SELL | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3451807200908661 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 2-6 | 107 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005923189222812653 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 108 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 109 | SELL | STABILIZE | 100.0 | 6 | 2 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3343333303928375 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 110 | SELL | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49260789155960083 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 95.0 | 6 | 11 | 1 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179349422454834 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 95.0 | 6 | 10 | 1 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025081027299165726 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 114 | BUY | STABILIZE | 95.0 | 6 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018524540588259697 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 115 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6000106930732727 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 116 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 4 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1665094941854477 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 117 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 118 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 119 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028821077197790146 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 2-7 | 120 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3569999933242798 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 95.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6830056309700012 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -46838f8d-8037-485c-8c34-9639f14ada19,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 123 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21044772863388062 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 124 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15437588095664978 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 125 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13081450760364532 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 126 | BUY | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2520761787891388 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 5 | 3-1 | 127 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 16.0 | Espinhos Negros/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5645714998245239 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003997073043137789 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014393298886716366 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 130 | PASS | STABILIZE | 95.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7181552052497864 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12487950921058655 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 134 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13899999856948853 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-2 | 135 | BUY_XP | STABILIZE | 95.0 | 6 | 6 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 136 | BUY | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052398115396499634 | 0.0 | 0.0 | +1662b43d-12f4-45d6-b1bf-3733d5214808 / -— |
| Jogador 5 | 3-2 | 137 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 5 | 3-2 | 138 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4129999876022339 | 0.0 | 0.0 | +— / -1662b43d-12f4-45d6-b1bf-3733d5214808 |
| Jogador 5 | 3-2 | 139 | SELL | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030533334240317345 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 3-2 | 140 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 95.0 | 6 | 8 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2838425636291504 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 143 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7300059199333191 | 0.0 | 0.0 | +a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a / -— |
| Jogador 5 | 3-3 | 144 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2761562168598175 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 145 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5686606764793396 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-3 | 146 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09254060685634613 | 0.0 | 0.0 | +— / -a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a |
| Jogador 5 | 3-3 | 147 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 148 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5409597158432007 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-3 | 149 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038758572190999985 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 150 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 3-4 | 152 | BUY | STABILIZE | 85.0 | 6 | 8 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8055679202079773 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 153 | BUY | STABILIZE | 85.0 | 6 | 7 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28113725781440735 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 154 | BUY_XP | STABILIZE | 85.0 | 6 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 155 | BUY | STABILIZE | 85.0 | 7 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021900992840528488 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 156 | SELL | STABILIZE | 85.0 | 7 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36310991644859314 | 0.0 | 0.0 | +— / -6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 3-4 | 157 | MOVE_BENCH | STABILIZE | 85.0 | 7 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5728297829627991 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 1 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 1 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016422640532255173 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 160 | PASS | STABILIZE | 85.0 | 7 | 1 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 162 | BUY | STABILIZE | 85.0 | 7 | 6 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28755509853363037 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 5 | 3-5 | 163 | BUY | STABILIZE | 85.0 | 7 | 5 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16511717438697815 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 164 | BUY | STABILIZE | 85.0 | 7 | 2 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01747140660881996 | 0.0 | 0.0 | +6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 / -— |
| Jogador 5 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008209064602851868 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 166 | SELL | STABILIZE | 85.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038333334028720856 | 0.0 | 0.0 | +— / -6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 |
| Jogador 5 | 3-5 | 167 | SELL | STABILIZE | 85.0 | 7 | 2 | 0 | 24.0 | Espinhos Negros/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0941333919763565 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-5 | 168 | BUY | STABILIZE | 85.0 | 7 | 5 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09709446132183075 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 1 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007917294278740883 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 170 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 1 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 172 | BUY | STABILIZE | 75.0 | 7 | 7 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7844718098640442 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 173 | BUY | STABILIZE | 75.0 | 7 | 4 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6549030542373657 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 174 | SELL | STABILIZE | 75.0 | 7 | 1 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22670629620552063 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-6 | 175 | BUY | STABILIZE | 75.0 | 7 | 3 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05185455456376076 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 176 | SELL | STABILIZE | 75.0 | 7 | 1 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05833333358168602 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-6 | 177 | MOVE_BENCH | STABILIZE | 75.0 | 7 | 3 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09889239817857742 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 178 | MOVE_BENCH | STABILIZE | 75.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40706393122673035 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 179 | SELL | STABILIZE | 75.0 | 7 | 3 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038333334028720856 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 3-6 | 180 | BUY | STABILIZE | 75.0 | 7 | 7 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1926639825105667 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-7 | 182 | BUY | STABILIZE | 75.0 | 7 | 12 | 1 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3172597587108612 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 183 | BUY | STABILIZE | 75.0 | 7 | 9 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.172454833984375 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 184 | SELL | STABILIZE | 75.0 | 7 | 6 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011166666634380817 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 3-7 | 185 | BUY | STABILIZE | 75.0 | 7 | 7 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017926273867487907 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 186 | SELL | STABILIZE | 75.0 | 7 | 4 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012343819253146648 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 3-7 | 187 | BUY | STABILIZE | 75.0 | 7 | 7 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020455770194530487 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 5 | 3-7 | 188 | REROLL | STABILIZE | 75.0 | 7 | 5 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20399999618530273 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 189 | SELL | STABILIZE | 75.0 | 7 | 3 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009705305099487305 | 0.0 | 0.0 | +— / -691cde76-cf1b-4a60-b818-65f790e312ec |
| Jogador 5 | 3-7 | 190 | BUY | STABILIZE | 75.0 | 7 | 5 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48908111453056335 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 5 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 75.0 | 7 | 8 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17453166842460632 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 75.0 | 7 | 8 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1651339828968048 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 194 | SELL | STABILIZE | 75.0 | 7 | 8 | 0 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08910000324249268 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 4-1 | 195 | BUY | STABILIZE | 75.0 | 7 | 11 | 1 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8070844411849976 | 0.0 | 0.0 | +3d7ba32f-3349-479e-bb6f-9cd1f2006149 / -— |
| Jogador 5 | 4-1 | 196 | SELL | STABILIZE | 75.0 | 7 | 10 | 1 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4330253303050995 | 0.0 | 0.0 | +— / -844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 5 | 4-1 | 197 | BUY | STABILIZE | 75.0 | 7 | 12 | 1 | 20.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7449017763137817 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -750eedbe-93d9-46de-b3b8-a88e41f395f0,a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 4-1 | 198 | SELL | STABILIZE | 75.0 | 7 | 9 | 0 | 20.0 | Espinhos Negros/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5277908444404602 | 0.0 | 0.0 | +— / -f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 5 | 4-1 | 199 | BUY | STABILIZE | 75.0 | 7 | 17 | 1 | 20.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09092332422733307 | 0.0 | 0.0 | +45d53a67-4ed4-495d-8751-5ea0f72f91e9 / -— |
| Jogador 5 | 4-1 | 200 | SELL | STABILIZE | 75.0 | 7 | 13 | 1 | 20.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37166666984558105 | 0.0 | 0.0 | +— / -45d53a67-4ed4-495d-8751-5ea0f72f91e9 |
| Jogador 5 | 4-2 | 202 | BUY | STABILIZE | 75.0 | 7 | 25 | 2 | 20.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8421947956085205 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 5 | 4-2 | 203 | BUY | STABILIZE | 75.0 | 7 | 22 | 2 | 20.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8678497076034546 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -3d7ba32f-3349-479e-bb6f-9cd1f2006149,ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 4-2 | 204 | BUY | STABILIZE | 75.0 | 7 | 21 | 2 | 18.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6983250379562378 | 0.0 | 0.0 | +6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb / -— |
| Jogador 5 | 4-2 | 205 | MOVE_BENCH | STABILIZE | 75.0 | 7 | 18 | 1 | 18.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5870315432548523 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 206 | BUY | STABILIZE | 75.0 | 7 | 18 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20611701905727386 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -— |
| Jogador 5 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 75.0 | 7 | 15 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 75.0 | 7 | 15 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01512239221483469 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 209 | PASS | STABILIZE | 75.0 | 7 | 15 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 212 | BUY | STABILIZE | 63.0 | 7 | 21 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30983495712280273 | 0.0 | 0.0 | +840740a6-45be-4107-a4b7-b10cefe1a667 / -— |
| Jogador 5 | 4-3 | 213 | SELL | STABILIZE | 63.0 | 7 | 20 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -93f7279f-b03b-407b-b623-c0a2bd88f877 |
| Jogador 5 | 4-3 | 214 | BUY | STABILIZE | 63.0 | 7 | 23 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18396678566932678 | 0.0 | 0.0 | +651884f1-8453-44cb-ac46-780eb9f7ac86 / -— |
| Jogador 5 | 4-3 | 215 | SELL | STABILIZE | 63.0 | 7 | 20 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014299999922513962 | 0.0 | 0.0 | +— / -7fd8b302-97aa-4373-94f4-adfcad477ed2 |
| Jogador 5 | 4-3 | 216 | BUY | STABILIZE | 63.0 | 7 | 23 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19244588911533356 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 5 | 4-3 | 217 | SELL | STABILIZE | 63.0 | 7 | 20 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -651884f1-8453-44cb-ac46-780eb9f7ac86 |
| Jogador 5 | 4-3 | 218 | SELL | STABILIZE | 63.0 | 7 | 23 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3656631410121918 | 0.0 | 0.0 | +— / -badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 5 | 4-3 | 219 | SELL | STABILIZE | 63.0 | 7 | 26 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48405176401138306 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 4-3 | 220 | SELL | STABILIZE | 63.0 | 7 | 29 | 2 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5529999732971191 | 0.0 | 0.0 | +— / -840740a6-45be-4107-a4b7-b10cefe1a667 |
| Jogador 5 | 4-4 | 222 | BUY | STABILIZE | 63.0 | 7 | 39 | 3 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9243975877761841 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -5627d898-cff3-4664-87d1-40a8f3656ab3,ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 4-4 | 223 | BUY | STABILIZE | 63.0 | 7 | 38 | 3 | 20.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01787371002137661 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 5 | 4-4 | 224 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 36 | 3 | 20.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12713071703910828 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 225 | BUY | STABILIZE | 63.0 | 7 | 36 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11954239010810852 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 5 | 4-4 | 226 | BUY | STABILIZE | 63.0 | 7 | 35 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08574287593364716 | 0.0 | 0.0 | +bb51728e-fcc5-4950-ad03-c864c51c2371 / -— |
| Jogador 5 | 4-4 | 227 | SELL | STABILIZE | 63.0 | 7 | 33 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5411555767059326 | 0.0 | 0.0 | +— / -84a3b0f5-c448-4fe1-b001-5ceff2ed306a |
| Jogador 5 | 4-4 | 228 | EQUIP_FROM_INVENTORY | STABILIZE | 63.0 | 7 | 36 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14237967133522034 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 229 | EQUIP_FROM_INVENTORY | STABILIZE | 63.0 | 7 | 36 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1219363734126091 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 230 | MOVE_BOARD | STABILIZE | 63.0 | 7 | 36 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0009636835311539471 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 232 | BUY | STABILIZE | 63.0 | 7 | 44 | 4 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.601597011089325 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -— |
| Jogador 5 | 4-5 | 233 | BUY | STABILIZE | 63.0 | 7 | 43 | 4 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16700242459774017 | 0.0 | 0.0 | +652568b9-7093-4e77-8b9c-7ed286cf7f4c / -— |
| Jogador 5 | 4-5 | 234 | SELL | STABILIZE | 63.0 | 7 | 39 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10400000214576721 | 0.0 | 0.0 | +— / -bb51728e-fcc5-4950-ad03-c864c51c2371 |
| Jogador 5 | 4-5 | 235 | BUY | STABILIZE | 63.0 | 7 | 41 | 4 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05859775096178055 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 5 | 4-5 | 236 | SELL | STABILIZE | 63.0 | 7 | 38 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -17170204-1921-4cf1-b92b-cc73bb0701ea |
| Jogador 5 | 4-5 | 237 | BUY | STABILIZE | 63.0 | 7 | 40 | 4 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1304088532924652 | 0.0 | 0.0 | +1ff42607-ccac-4d3f-8277-bccddf08862f / -— |
| Jogador 5 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 63.0 | 7 | 39 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003738262690603733 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 63.0 | 7 | 39 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048986636102199554 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 240 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 39 | 3 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6000687479972839 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 242 | BUY | STABILIZE | 52.0 | 7 | 47 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3313181400299072 | 0.0 | 0.0 | +241a8a03-6e6f-4a9a-8550-e9154f3e1e76 / -— |
| Jogador 5 | 4-6 | 243 | SELL | STABILIZE | 52.0 | 7 | 46 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047097306698560715 | 0.0 | 0.0 | +— / -1ff42607-ccac-4d3f-8277-bccddf08862f |
| Jogador 5 | 4-6 | 244 | BUY | STABILIZE | 52.0 | 7 | 47 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21234643459320068 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 5 | 4-6 | 245 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 43 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13457642495632172 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 246 | SELL | STABILIZE | 52.0 | 7 | 43 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02480577677488327 | 0.0 | 0.0 | +— / -a72137b3-498b-40e1-938a-639f56745f08 |
| Jogador 5 | 4-6 | 247 | BUY | STABILIZE | 52.0 | 7 | 46 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22365498542785645 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 5 | 4-6 | 248 | SELL | STABILIZE | 52.0 | 7 | 44 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -c65dacb1-5745-49d1-b7d4-e45d8e24aa84 |
| Jogador 5 | 4-6 | 249 | BUY | STABILIZE | 52.0 | 7 | 46 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22358572483062744 | 0.0 | 0.0 | +51a5a5d7-c5ea-43e2-a521-22fe0275c231 / -— |
| Jogador 5 | 4-6 | 250 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 44 | 4 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00033651504782028496 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 252 | SELL | STABILIZE | 52.0 | 7 | 54 | 5 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -51a5a5d7-c5ea-43e2-a521-22fe0275c231 |
| Jogador 5 | 4-7 | 253 | BUY | STABILIZE | 52.0 | 7 | 56 | 5 | 32.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9634069800376892 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -0f1b15a2-9978-4691-a15e-483ccd03db7f,6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb |
| Jogador 5 | 4-7 | 254 | BUY | STABILIZE | 52.0 | 7 | 53 | 5 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.081483393907547 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 5 | 4-7 | 255 | SELL | STABILIZE | 52.0 | 7 | 49 | 4 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5170999765396118 | 0.0 | 0.0 | +— / -6722b147-c2a7-4fd0-a943-5036adb3e3a1 |
| Jogador 5 | 4-7 | 256 | BUY | STABILIZE | 52.0 | 7 | 57 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028518905863165855 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 5 | 4-7 | 257 | SELL | STABILIZE | 52.0 | 7 | 54 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -1388df2e-8cb4-4e29-8b30-776c29406917 |
| Jogador 5 | 4-7 | 258 | BUY | STABILIZE | 52.0 | 7 | 57 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20316354930400848 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 5 | 4-7 | 259 | SELL | STABILIZE | 52.0 | 7 | 53 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0009951874380931258 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 5 | 4-7 | 260 | SELL | STABILIZE | 52.0 | 7 | 57 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35153332352638245 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 5 | 5-1 | 262 | BUY | STABILIZE | 52.0 | 7 | 71 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.35969313979148865 | 0.0 | 0.0 | +55cd39c0-65d5-410e-917e-501f584115fa / -— |
| Jogador 5 | 5-1 | 263 | BUY | STABILIZE | 52.0 | 7 | 68 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.028879011049866676 | 0.0 | 0.0 | +c7a7408a-e7bd-428d-9935-4d5a002d8d9f / -— |
| Jogador 5 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 52.0 | 7 | 65 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10638825595378876 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 265 | CRAFT_AND_EQUIP | STABILIZE | 52.0 | 7 | 65 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11287283152341843 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 266 | SELL | STABILIZE | 52.0 | 7 | 65 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -c7a7408a-e7bd-428d-9935-4d5a002d8d9f |
| Jogador 5 | 5-1 | 267 | BUY | STABILIZE | 52.0 | 7 | 68 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018675681203603745 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 5 | 5-1 | 268 | SELL | STABILIZE | 52.0 | 7 | 67 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006991952192038298 | 0.0 | 0.0 | +— / -98b600a1-736b-437d-a69e-8a7f7235d9c3 |
| Jogador 5 | 5-1 | 269 | BUY | STABILIZE | 52.0 | 7 | 68 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04780412092804909 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -— |
| Jogador 5 | 5-1 | 270 | SELL | STABILIZE | 52.0 | 7 | 66 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 |
| Jogador 5 | 5-2 | 272 | BUY | STABILIZE | 52.0 | 7 | 78 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1368410289287567 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 5 | 5-2 | 273 | SELL | STABILIZE | 52.0 | 7 | 75 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03826567158102989 | 0.0 | 0.0 | +— / -3b934078-806c-40f0-b102-e9131220f70e |
| Jogador 5 | 5-2 | 274 | BUY | STABILIZE | 52.0 | 7 | 79 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12244848161935806 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -— |
| Jogador 5 | 5-2 | 275 | MOVE_BENCH | STABILIZE | 52.0 | 7 | 76 | 5 | 26.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4650191366672516 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 276 | BUY | STABILIZE | 52.0 | 7 | 76 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04169069603085518 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -— |
| Jogador 5 | 5-2 | 277 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 74 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 278 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 74 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 279 | PASS | STABILIZE | 52.0 | 7 | 74 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10516668111085892 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 282 | SELL | STABILIZE | 52.0 | 7 | 86 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -9f445115-49cc-4647-91a0-a80e347e9c62 |
| Jogador 5 | 5-3 | 283 | BUY | STABILIZE | 52.0 | 7 | 88 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9048567414283752 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -— |
| Jogador 5 | 5-3 | 284 | SELL | STABILIZE | 52.0 | 7 | 87 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 5 | 5-3 | 285 | BUY | STABILIZE | 52.0 | 7 | 90 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13506492972373962 | 0.0 | 0.0 | +2f2b455f-7035-4948-9429-612018ae7063 / -— |
| Jogador 5 | 5-3 | 286 | SELL | STABILIZE | 52.0 | 7 | 87 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -2f2b455f-7035-4948-9429-612018ae7063 |
| Jogador 5 | 5-3 | 287 | BUY | STABILIZE | 52.0 | 7 | 90 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13505707681179047 | 0.0 | 0.0 | +a899fe97-90e4-4ae3-941c-af3dee48fed3 / -— |
| Jogador 5 | 5-3 | 288 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 87 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015706081176176667 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 289 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 87 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013407844118773937 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 290 | PASS | STABILIZE | 52.0 | 7 | 87 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11563604325056076 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 292 | SELL | STABILIZE | 52.0 | 7 | 99 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -a899fe97-90e4-4ae3-941c-af3dee48fed3 |
| Jogador 5 | 5-4 | 293 | BUY | STABILIZE | 52.0 | 7 | 102 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.023305058479309 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -1457cd1e-c240-4ce5-9217-a91bddfc8807,4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 5-4 | 294 | BUY | STABILIZE | 52.0 | 7 | 99 | 5 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028601177036762238 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -— |
| Jogador 5 | 5-4 | 295 | SELL | STABILIZE | 52.0 | 7 | 94 | 5 | 26.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -76fcc4d0-4988-4e99-8ac0-c251f0b99dcd |
| Jogador 5 | 5-4 | 296 | EQUIP_FROM_INVENTORY | STABILIZE | 52.0 | 7 | 102 | 5 | 26.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13383597135543823 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 297 | EQUIP_FROM_INVENTORY | STABILIZE | 52.0 | 7 | 102 | 5 | 26.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04772048816084862 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 298 | EQUIP_FROM_INVENTORY | STABILIZE | 52.0 | 7 | 102 | 5 | 26.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12580204010009766 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 299 | MOVE_BENCH | STABILIZE | 52.0 | 7 | 102 | 5 | 26.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5060449838638306 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 300 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 102 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01494276151061058 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 302 | BUY | STABILIZE | 52.0 | 7 | 113 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007390447426587343 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -— |
| Jogador 5 | 5-5 | 303 | BUY | STABILIZE | 52.0 | 7 | 111 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007649773731827736 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -— |
| Jogador 5 | 5-5 | 304 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 109 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00048138442798517644 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 305 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 109 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 306 | PASS | STABILIZE | 52.0 | 7 | 109 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13417333364486694 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 312 | SELL | STABILIZE | 52.0 | 7 | 121 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -f087511a-d834-4f41-9b99-00bf0f6dc061 |
| Jogador 5 | 5-6 | 313 | BUY | STABILIZE | 52.0 | 7 | 123 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8692535758018494 | 0.0 | 0.0 | +3ae84928-bc2a-4c1e-8663-b7ad05da4501 / -— |
| Jogador 5 | 5-6 | 314 | SELL | STABILIZE | 52.0 | 7 | 120 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -c07a17cf-e9e7-42be-b925-cb4f699593de |
| Jogador 5 | 5-6 | 315 | BUY | STABILIZE | 52.0 | 7 | 122 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7652719020843506 | 0.0 | 0.0 | +3eccad10-cc50-4695-852e-0809356dd33b / -— |
| Jogador 5 | 5-6 | 316 | SELL | STABILIZE | 52.0 | 7 | 120 | 5 | 28.0 | Espinhos Negros/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0025333333760499954 | 0.0 | 0.0 | +— / -2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d |
| Jogador 5 | 5-6 | 317 | BUY | STABILIZE | 52.0 | 7 | 125 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37213143706321716 | 0.0 | 0.0 | +caeaaabc-213a-4018-97f3-8797a0711863 / -— |
| Jogador 5 | 5-6 | 318 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 123 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004910281277261674 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 319 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 123 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 320 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 123 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0151199446991086 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 322 | SELL | STABILIZE | 37.0 | 7 | 133 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11779999732971191 | 0.0 | 0.0 | +— / -caeaaabc-213a-4018-97f3-8797a0711863 |
| Jogador 5 | 5-7 | 323 | BUY | STABILIZE | 37.0 | 7 | 135 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002958969445899129 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -— |
| Jogador 5 | 5-7 | 324 | SELL | STABILIZE | 37.0 | 7 | 131 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01596544310450554 | 0.0 | 0.0 | +— / -1f349179-be2a-4738-bda1-072f7fae2147 |
| Jogador 5 | 5-7 | 325 | BUY | STABILIZE | 37.0 | 7 | 135 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013380996882915497 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -— |
| Jogador 5 | 5-7 | 326 | SELL | STABILIZE | 37.0 | 7 | 133 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015533333644270897 | 0.0 | 0.0 | +— / -0a0e7d41-96bf-404f-a3bf-98df0a182b63 |
| Jogador 5 | 5-7 | 327 | BUY | STABILIZE | 37.0 | 7 | 135 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0053108069114387035 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 5 | 5-7 | 328 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 133 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.014664202462882e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 329 | SELL | STABILIZE | 37.0 | 7 | 133 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -bdee5671-864a-47c9-9576-9e0d8d2a7c6a |
| Jogador 5 | 5-7 | 330 | BUY | STABILIZE | 37.0 | 7 | 135 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025095120072364807 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 5 | 6-1 | 332 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 7 | 143 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1106070727109909 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 333 | SELL | STABILIZE | 37.0 | 7 | 143 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009656690061092377 | 0.0 | 0.0 | +— / -c5520bc4-3123-40f3-b275-83fa8cb06309 |
| Jogador 5 | 6-1 | 334 | BUY | STABILIZE | 37.0 | 7 | 145 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028379984200000763 | 0.0 | 0.0 | +63c47a3f-6712-4cfa-9376-6140da170089 / -— |
| Jogador 5 | 6-1 | 335 | SELL | STABILIZE | 37.0 | 7 | 141 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -63c47a3f-6712-4cfa-9376-6140da170089 |
| Jogador 5 | 6-1 | 336 | BUY | STABILIZE | 37.0 | 7 | 145 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22994616627693176 | 0.0 | 0.0 | +78adfe0a-b6d8-4cc4-a482-26451f95e788 / -— |
| Jogador 5 | 6-1 | 337 | SELL | STABILIZE | 37.0 | 7 | 141 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -78adfe0a-b6d8-4cc4-a482-26451f95e788 |
| Jogador 5 | 6-1 | 338 | BUY | STABILIZE | 37.0 | 7 | 145 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013399580493569374 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -— |
| Jogador 5 | 6-1 | 339 | SELL | STABILIZE | 37.0 | 7 | 143 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015533333644270897 | 0.0 | 0.0 | +— / -6b7f5603-ce44-4b91-8a3e-939c4fbb26ac |
| Jogador 5 | 6-1 | 340 | BUY | STABILIZE | 37.0 | 7 | 145 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024860257282853127 | 0.0 | 0.0 | +5098782d-1ec1-4a5b-a435-f3c84ab1be0d / -— |
| Jogador 5 | 6-2 | 342 | SELL | ALL_IN | 19.0 | 7 | 154 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009653489105403423 | 0.0 | 0.0 | +— / -5098782d-1ec1-4a5b-a435-f3c84ab1be0d |
| Jogador 5 | 6-2 | 343 | BUY | ALL_IN | 19.0 | 7 | 156 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.111350417137146 | 0.0 | 0.0 | +d47034a1-8b51-4b82-b1b4-5f2aee8f959a / -1d7b6420-388f-4cb1-b25c-2e5a3dfec742,ef54ddfd-f436-4813-9585-cb652488ffa3 |
| Jogador 5 | 6-2 | 344 | BUY | ALL_IN | 19.0 | 7 | 153 | 5 | 22.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16994360089302063 | 0.0 | 0.0 | +04ebf9b8-7683-4270-b98a-a3bfb342dcf8 / -— |
| Jogador 5 | 6-2 | 345 | MOVE_BENCH | ALL_IN | 19.0 | 7 | 148 | 5 | 22.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5610942840576172 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 346 | BUY | ALL_IN | 19.0 | 7 | 148 | 5 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06945821642875671 | 0.0 | 0.0 | +d4e5375b-6b8c-4492-b9cc-ded108270798 / -— |
| Jogador 5 | 6-2 | 347 | REROLL | ALL_IN | 19.0 | 7 | 144 | 5 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 348 | SELL | ALL_IN | 19.0 | 7 | 142 | 5 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6972000002861023 | 0.0 | 0.0 | +— / -d47034a1-8b51-4b82-b1b4-5f2aee8f959a |
| Jogador 5 | 6-2 | 349 | BUY | ALL_IN | 19.0 | 7 | 150 | 5 | 24.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5151273012161255 | 0.0 | 0.0 | +e1be174a-f112-4e1b-8bf6-738af52f27e8 / -— |
| Jogador 5 | 6-2 | 350 | SELL | ALL_IN | 19.0 | 7 | 147 | 5 | 24.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -d4e5375b-6b8c-4492-b9cc-ded108270798 |
| Jogador 5 | 6-3 | 352 | BUY | ALL_IN | 1.0 | 7 | 162 | 5 | 24.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1018341779708862 | 0.0 | 0.0 | +d1f4a2a4-f3cb-413d-8ed8-b373fa56f1f2 / -3eccad10-cc50-4695-852e-0809356dd33b,6eee9a92-4235-46af-ae42-c38acd6847ef |
| Jogador 5 | 6-3 | 353 | BUY | ALL_IN | 1.0 | 7 | 160 | 5 | 20.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042950473725795746 | 0.0 | 0.0 | +80241b75-9eb3-4b89-a754-8df65ec59786 / -— |
| Jogador 5 | 6-3 | 354 | REROLL | ALL_IN | 1.0 | 7 | 157 | 5 | 20.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 355 | SELL | ALL_IN | 1.0 | 7 | 155 | 5 | 20.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7437000274658203 | 0.0 | 0.0 | +— / -d1f4a2a4-f3cb-413d-8ed8-b373fa56f1f2 |
| Jogador 5 | 6-3 | 356 | EQUIP_FROM_INVENTORY | ALL_IN | 1.0 | 7 | 160 | 5 | 20.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1445533037185669 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 357 | EQUIP_FROM_INVENTORY | ALL_IN | 1.0 | 7 | 160 | 5 | 20.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08994539082050323 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 358 | BUY | ALL_IN | 1.0 | 7 | 160 | 5 | 20.0 | Espinhos Negros/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041915398091077805 | 0.0 | 0.0 | +bf33b437-04ac-4dd7-8c7d-ad48546675b8 / -— |
| Jogador 5 | 6-3 | 359 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 157 | 5 | 20.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3888562023639679 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 360 | SELL | ALL_IN | 1.0 | 7 | 157 | 5 | 24.0 | Espinhos Negros/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -80241b75-9eb3-4b89-a754-8df65ec59786 |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2209876924753189 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0373761653900146 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5755935311317444 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.023976445198059 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12821809947490692 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15193839371204376 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29001790285110474 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 57 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09122555702924728 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 64 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2638055086135864 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24732834100723267 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 66 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 67 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 68 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2889452278614044 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1800447255373001 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2381841391324997 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 75 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1451059877872467 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 76 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15174691379070282 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 77 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 82 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18297378718852997 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 83 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24062861502170563 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 84 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8069473505020142 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 85 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 86 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 87 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10960464179515839 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 88 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 89 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14379313588142395 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-4 | 90 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14379039406776428 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 92 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8596822023391724 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 93 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2884131073951721 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 94 | BUY_XP | STABILIZE | 83.0 | 5 | 7 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 95 | SELL | STABILIZE | 83.0 | 5 | 3 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45226430892944336 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 96 | BUY_XP | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 97 | SELL | STABILIZE | 83.0 | 5 | 1 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4931749105453491 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-5 | 98 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 8.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21166107058525085 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 100 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32035812735557556 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 103 | BUY_XP | STABILIZE | 76.0 | 6 | 6 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 104 | SELL | STABILIZE | 76.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18617047369480133 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 105 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006841098889708519 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 107 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-6 | 108 | BUY | STABILIZE | 76.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15727946162223816 | 0.0 | 0.0 | +2a7dd07f-3b48-489c-8822-9ec2434a01cf / -— |
| Jogador 6 | 2-6 | 109 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6007081270217896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020107917487621307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 76.0 | 6 | 6 | 0 | 12.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3116063177585602 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 76.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12100201845169067 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09657106548547745 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05070220306515694 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 117 | PASS | STABILIZE | 76.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 76.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2592379152774811 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 76.0 | 6 | 2 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19527630507946014 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | SELL | STABILIZE | 76.0 | 6 | 2 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07351678609848022 | 0.0 | 0.0 | +— / -2a7dd07f-3b48-489c-8822-9ec2434a01cf |
| Jogador 6 | 3-1 | 125 | SELL | STABILIZE | 76.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09214000403881073 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-1 | 126 | BUY | STABILIZE | 76.0 | 6 | 7 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09856212884187698 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 127 | SELL | STABILIZE | 76.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038333334028720856 | 0.0 | 0.0 | +— / -4eedd873-e4ec-41e5-9f5e-48e443e80f86 |
| Jogador 6 | 3-1 | 128 | SELL | STABILIZE | 76.0 | 6 | 7 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07905938476324081 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 3-1 | 129 | BUY | STABILIZE | 76.0 | 6 | 10 | 1 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04786885902285576 | 0.0 | 0.0 | +91f05e8c-f467-4f22-9cb0-c814ffa93198 / -— |
| Jogador 6 | 3-1 | 130 | SELL | STABILIZE | 76.0 | 6 | 8 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3137311339378357 | 0.0 | 0.0 | +— / -91f05e8c-f467-4f22-9cb0-c814ffa93198 |
| Jogador 6 | 3-2 | 132 | BUY | STABILIZE | 67.0 | 6 | 16 | 1 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379331827163696 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 133 | BUY | STABILIZE | 67.0 | 6 | 15 | 1 | 10.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8144418597221375 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 14 | 1 | 6.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05768655613064766 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 135 | BUY | STABILIZE | 67.0 | 6 | 14 | 1 | 10.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012462062761187553 | 0.0 | 0.0 | +9204a42c-6310-4b08-9bc7-8a2e786b077a / -— |
| Jogador 6 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 12 | 1 | 10.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27830788493156433 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 137 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 12 | 1 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22499480843544006 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 138 | BUY | STABILIZE | 67.0 | 6 | 12 | 1 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03769697993993759 | 0.0 | 0.0 | +4278eb73-acda-419d-bf9e-53a29ff6900d / -— |
| Jogador 6 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 11 | 1 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08174370974302292 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 140 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 11 | 1 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13632939755916595 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 67.0 | 6 | 18 | 1 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06889783591032028 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 143 | BUY | STABILIZE | 67.0 | 6 | 15 | 1 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11108789592981339 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 144 | BUY | STABILIZE | 67.0 | 6 | 12 | 1 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08780688047409058 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 6 | 3-3 | 145 | BUY_XP | STABILIZE | 67.0 | 6 | 10 | 1 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | BUY_XP | STABILIZE | 67.0 | 6 | 6 | 0 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 147 | SELL | STABILIZE | 67.0 | 6 | 2 | 0 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-3 | 148 | BUY_XP | STABILIZE | 67.0 | 6 | 5 | 0 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 149 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 1 | 0 | 14.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38049039244651794 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 1 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15145951509475708 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | STABILIZE | 67.0 | 6 | 8 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2827892005443573 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 6 | 3-4 | 153 | BUY | STABILIZE | 67.0 | 6 | 5 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08899445831775665 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 6 | 3-4 | 154 | BUY | STABILIZE | 67.0 | 6 | 2 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009777313098311424 | 0.0 | 0.0 | +4698e3b3-0833-4895-a1f1-26b372b2f965 / -— |
| Jogador 6 | 3-4 | 155 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 0 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08812952041625977 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 0 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 0 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0844740942120552 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 0 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060032233595848083 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 0 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03241601213812828 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 0 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008738551405258477 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | STABILIZE | 67.0 | 7 | 6 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8029887676239014 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 163 | BUY | STABILIZE | 67.0 | 7 | 3 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4974943697452545 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 6 | 3-5 | 164 | SELL | STABILIZE | 67.0 | 7 | 0 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02843683958053589 | 0.0 | 0.0 | +— / -4278eb73-acda-419d-bf9e-53a29ff6900d |
| Jogador 6 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 67.0 | 7 | 1 | 0 | 20.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4009955823421478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 1 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015130972489714622 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 1 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 168 | PASS | STABILIZE | 67.0 | 7 | 1 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | BUY | STABILIZE | 67.0 | 7 | 8 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19197505712509155 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 173 | BUY | STABILIZE | 67.0 | 7 | 5 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14489039778709412 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 2 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 2 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01490163616836071 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 176 | PASS | STABILIZE | 67.0 | 7 | 2 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | SELL | STABILIZE | 67.0 | 7 | 9 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07699964195489883 | 0.0 | 0.0 | +— / -25b16126-6e41-4649-a47f-42656ffc7a08 |
| Jogador 6 | 3-7 | 183 | BUY | STABILIZE | 67.0 | 7 | 11 | 1 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13229885697364807 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 184 | SELL | STABILIZE | 67.0 | 7 | 7 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0029415390454232693 | 0.0 | 0.0 | +— / -4698e3b3-0833-4895-a1f1-26b372b2f965 |
| Jogador 6 | 3-7 | 185 | BUY | STABILIZE | 67.0 | 7 | 9 | 0 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20570148527622223 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 4 | 0 | 26.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.4445804228889756e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 4 | 0 | 26.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 4 | 0 | 26.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499870140105486 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 189 | PASS | STABILIZE | 67.0 | 7 | 4 | 0 | 26.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 67.0 | 7 | 10 | 1 | 26.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2543240189552307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 67.0 | 7 | 10 | 1 | 26.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18881899118423462 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | SELL | STABILIZE | 67.0 | 7 | 10 | 1 | 26.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b |
| Jogador 6 | 4-1 | 195 | BUY | STABILIZE | 67.0 | 7 | 13 | 1 | 26.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6279587149620056 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 6 | 4-1 | 196 | SELL | STABILIZE | 67.0 | 7 | 11 | 1 | 26.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002166666556149721 | 0.0 | 0.0 | +— / -cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 4-1 | 197 | BUY | STABILIZE | 67.0 | 7 | 14 | 1 | 26.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6785060167312622 | 0.0 | 0.0 | +ddf39480-6ce0-46d0-ac45-57114245ffba / -06db3a99-d008-406a-ac86-30884335d7c2,50f9a30c-27db-4ed0-804e-548f87950b17 |
| Jogador 6 | 4-1 | 198 | MOVE_BENCH | STABILIZE | 67.0 | 7 | 11 | 1 | 20.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40121978521347046 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 199 | BUY | STABILIZE | 67.0 | 7 | 11 | 1 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.052225831896066666 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -— |
| Jogador 6 | 4-1 | 200 | BUY | STABILIZE | 67.0 | 7 | 8 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011274127289652824 | 0.0 | 0.0 | +626c50be-ec88-444f-84bb-9b8d41100085 / -— |
| Jogador 6 | 4-2 | 202 | SELL | STABILIZE | 56.0 | 7 | 11 | 1 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00591541500762105 | 0.0 | 0.0 | +— / -626c50be-ec88-444f-84bb-9b8d41100085 |
| Jogador 6 | 4-2 | 203 | BUY | STABILIZE | 56.0 | 7 | 13 | 1 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20411862432956696 | 0.0 | 0.0 | +7920bf77-c0ba-4906-a82d-6c18bc42f4d9 / -— |
| Jogador 6 | 4-2 | 204 | SELL | STABILIZE | 56.0 | 7 | 10 | 1 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005970389116555452 | 0.0 | 0.0 | +— / -cc56fedc-f555-4075-af15-6b5fb93a156f |
| Jogador 6 | 4-2 | 205 | BUY | STABILIZE | 56.0 | 7 | 13 | 1 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20488406717777252 | 0.0 | 0.0 | +bf0751f0-8094-4441-adb3-e5f8b4158426 / -— |
| Jogador 6 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 9 | 0 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 9 | 0 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015172761864960194 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 208 | PASS | STABILIZE | 56.0 | 7 | 9 | 0 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | SELL | STABILIZE | 44.0 | 7 | 15 | 1 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.040456805378198624 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 6 | 4-3 | 213 | BUY | STABILIZE | 44.0 | 7 | 18 | 1 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7467266321182251 | 0.0 | 0.0 | +f5cca112-4fa0-4ee6-a863-20a5d49ab7ef / -9204a42c-6310-4b08-9bc7-8a2e786b077a,97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 6 | 4-3 | 214 | BUY | STABILIZE | 44.0 | 7 | 16 | 1 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013750293292105198 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 6 | 4-3 | 215 | MOVE_BENCH | STABILIZE | 44.0 | 7 | 12 | 1 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3979186713695526 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 216 | SELL | STABILIZE | 44.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045499999076128006 | 0.0 | 0.0 | +— / -7920bf77-c0ba-4906-a82d-6c18bc42f4d9 |
| Jogador 6 | 4-3 | 217 | BUY | STABILIZE | 44.0 | 7 | 15 | 1 | 34.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060671366751194 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 6 | 4-3 | 218 | MOVE_BENCH | STABILIZE | 44.0 | 7 | 13 | 1 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5656209588050842 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 219 | BUY | FAST8 | 44.0 | 7 | 13 | 1 | 36.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058314114809036255 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -— |
| Jogador 6 | 4-3 | 220 | MOVE_BOARD | FAST8 | 44.0 | 7 | 12 | 1 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05961999297142029 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | SELL | FAST8 | 44.0 | 7 | 19 | 1 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07296666502952576 | 0.0 | 0.0 | +— / -485dab1f-b3a1-4170-8ed6-c0035072ae9b |
| Jogador 6 | 4-4 | 223 | BUY | FAST8 | 44.0 | 7 | 20 | 2 | 36.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15091611444950104 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 6 | 4-4 | 224 | SELL | FAST8 | 44.0 | 7 | 17 | 1 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013776589184999466 | 0.0 | 0.0 | +— / -80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 6 | 4-4 | 225 | BUY | FAST8 | 44.0 | 7 | 19 | 1 | 36.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21730993688106537 | 0.0 | 0.0 | +8995f621-b355-44ec-816e-797184bdc266 / -— |
| Jogador 6 | 4-4 | 226 | MOVE_BOARD | FAST8 | 44.0 | 7 | 18 | 1 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05823177099227905 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 227 | MOVE_BOARD | FAST8 | 44.0 | 7 | 18 | 1 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020899740979075432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 228 | MOVE_BOARD | FAST8 | 44.0 | 7 | 18 | 1 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 229 | MOVE_BOARD | FAST8 | 44.0 | 7 | 18 | 1 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 230 | PASS | FAST8 | 44.0 | 7 | 18 | 1 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02761693112552166 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | SELL | FAST8 | 44.0 | 7 | 24 | 2 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0035391105338931084 | 0.0 | 0.0 | +— / -c7841e00-91da-410b-b00f-62f4bf32f666 |
| Jogador 6 | 4-5 | 233 | BUY | FAST8 | 44.0 | 7 | 28 | 2 | 36.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21542119979858398 | 0.0 | 0.0 | +31ea6d79-501d-4f2a-821d-7058334be82f / -— |
| Jogador 6 | 4-5 | 234 | MOVE_BOARD | FAST8 | 44.0 | 7 | 27 | 2 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0010343819158151746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 235 | MOVE_BOARD | FAST8 | 44.0 | 7 | 27 | 2 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0250881165266037 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 236 | PASS | FAST8 | 44.0 | 7 | 27 | 2 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034578837454319 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | FAST8 | 44.0 | 7 | 36 | 3 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026606354862451553 | 0.0 | 0.0 | +— / -31ea6d79-501d-4f2a-821d-7058334be82f |
| Jogador 6 | 4-6 | 243 | BUY | FAST8 | 44.0 | 7 | 37 | 3 | 36.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24932123720645905 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 6 | 4-6 | 244 | MOVE_BOARD | FAST8 | 44.0 | 7 | 33 | 3 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03574999049305916 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 245 | MOVE_BOARD | FAST8 | 44.0 | 7 | 33 | 3 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010351707227528095 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 246 | PASS | FAST8 | 44.0 | 7 | 33 | 3 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03922010585665703 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 252 | SELL | STABILIZE | 32.0 | 7 | 41 | 4 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -bf0751f0-8094-4441-adb3-e5f8b4158426 |
| Jogador 6 | 4-7 | 253 | BUY | STABILIZE | 32.0 | 7 | 45 | 4 | 36.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8572813868522644 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 6 | 4-7 | 254 | SELL | STABILIZE | 32.0 | 7 | 42 | 4 | 36.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042042650282382965 | 0.0 | 0.0 | +— / -891aea62-e06a-46d4-8250-a3d4a56e847d |
| Jogador 6 | 4-7 | 255 | BUY | STABILIZE | 32.0 | 7 | 47 | 4 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19642190635204315 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -— |
| Jogador 6 | 4-7 | 256 | SELL | STABILIZE | 32.0 | 7 | 44 | 4 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04203333333134651 | 0.0 | 0.0 | +— / -57d86f23-f167-472f-9878-21dcddc0a5f7 |
| Jogador 6 | 4-7 | 257 | BUY | STABILIZE | 32.0 | 7 | 47 | 4 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041434310376644135 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 6 | 4-7 | 258 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 44 | 4 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 259 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 44 | 4 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026751665398478508 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 260 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 44 | 4 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 7 | 53 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15471868216991425 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 7 | 53 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12262962758541107 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 264 | SELL | STABILIZE | 32.0 | 7 | 53 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 6 | 5-1 | 265 | BUY | STABILIZE | 32.0 | 7 | 56 | 5 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8974963426589966 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -— |
| Jogador 6 | 5-1 | 266 | SELL | STABILIZE | 32.0 | 7 | 53 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -8995f621-b355-44ec-816e-797184bdc266 |
| Jogador 6 | 5-1 | 267 | BUY | STABILIZE | 32.0 | 7 | 54 | 5 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1418437361717224 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 6 | 5-1 | 268 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 50 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 269 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 50 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997906051576138 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 270 | PASS | STABILIZE | 32.0 | 7 | 50 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1134222224354744 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 272 | SELL | STABILIZE | 32.0 | 7 | 61 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03865427151322365 | 0.0 | 0.0 | +— / -f32e50e0-1430-4549-a1dd-a8473ffe0bd4 |
| Jogador 6 | 5-2 | 273 | BUY | STABILIZE | 32.0 | 7 | 65 | 5 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20850956439971924 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 6 | 5-2 | 274 | SELL | STABILIZE | 32.0 | 7 | 62 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002360889222472906 | 0.0 | 0.0 | +— / -b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 6 | 5-2 | 275 | BUY | STABILIZE | 32.0 | 7 | 65 | 5 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16918422281742096 | 0.0 | 0.0 | +c7762d7d-bcfa-4694-a3fc-038d7242207f / -— |
| Jogador 6 | 5-2 | 276 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 64 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.0812125260126777e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 277 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 64 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015003063715994358 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 278 | SELL | STABILIZE | 32.0 | 7 | 64 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019866665825247765 | 0.0 | 0.0 | +— / -c7762d7d-bcfa-4694-a3fc-038d7242207f |
| Jogador 6 | 5-2 | 279 | BUY | STABILIZE | 32.0 | 7 | 65 | 5 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21851037442684174 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 6 | 5-2 | 280 | SELL | STABILIZE | 32.0 | 7 | 63 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008763761259615421 | 0.0 | 0.0 | +— / -7313188a-ce84-4a52-b2d0-a94b2c420cdb |
| Jogador 6 | 5-3 | 282 | BUY | ALL_IN | 17.0 | 7 | 75 | 5 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.050958514213562 | 0.0 | 0.0 | +ad363fca-33b7-4257-99d6-7093df66caf6 / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4,ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c |
| Jogador 6 | 5-3 | 283 | BUY | ALL_IN | 17.0 | 7 | 72 | 5 | 36.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0504435300827026 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 5-3 | 284 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 71 | 5 | 32.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3471930921077728 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 285 | BUY | ALL_IN | 17.0 | 7 | 71 | 5 | 38.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0037950132973492146 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 6 | 5-3 | 286 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 68 | 5 | 38.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40043142437934875 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 287 | BUY | ALL_IN | 17.0 | 7 | 68 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20104776322841644 | 0.0 | 0.0 | +499f10b9-47ba-4cab-add1-31b452acae6d / -— |
| Jogador 6 | 5-3 | 288 | BUY | ALL_IN | 17.0 | 7 | 65 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40091684460639954 | 0.0 | 0.0 | +33e9808b-2f92-49e7-ac35-1f6f9388edef / -— |
| Jogador 6 | 5-3 | 289 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 62 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00022922914649825543 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 290 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 62 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014401957392692566 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 292 | SELL | ALL_IN | 17.0 | 7 | 72 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6963000297546387 | 0.0 | 0.0 | +— / -908d49c8-626c-44b5-9b03-6a85442f358b |
| Jogador 6 | 5-4 | 293 | BUY | ALL_IN | 17.0 | 7 | 75 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9264243245124817 | 0.0 | 0.0 | +3329c812-11fa-4335-a982-f03e6ab28ee0 / -— |
| Jogador 6 | 5-4 | 294 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 71 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1172526627779007 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 295 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 71 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09247073531150818 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 296 | SELL | ALL_IN | 17.0 | 7 | 71 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7027999758720398 | 0.0 | 0.0 | +— / -ad363fca-33b7-4257-99d6-7093df66caf6 |
| Jogador 6 | 5-4 | 297 | BUY | ALL_IN | 17.0 | 7 | 79 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42512792348861694 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -— |
| Jogador 6 | 5-4 | 298 | SELL | ALL_IN | 17.0 | 7 | 76 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.520966649055481 | 0.0 | 0.0 | +— / -499f10b9-47ba-4cab-add1-31b452acae6d |
| Jogador 6 | 5-4 | 299 | BUY | ALL_IN | 17.0 | 7 | 79 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2830040454864502 | 0.0 | 0.0 | +98991369-e5f0-4725-928c-f2fa5362bf73 / -— |
| Jogador 6 | 5-4 | 300 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 77 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.9713571620959556e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 302 | SELL | ALL_IN | 17.0 | 7 | 87 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07013333588838577 | 0.0 | 0.0 | +— / -98991369-e5f0-4725-928c-f2fa5362bf73 |
| Jogador 6 | 5-5 | 303 | BUY | ALL_IN | 17.0 | 7 | 89 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16804392635822296 | 0.0 | 0.0 | +407092ea-3a14-4555-9ebd-64a36c41d1d0 / -— |
| Jogador 6 | 5-5 | 304 | SELL | ALL_IN | 17.0 | 7 | 86 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004399999976158142 | 0.0 | 0.0 | +— / -33e9808b-2f92-49e7-ac35-1f6f9388edef |
| Jogador 6 | 5-5 | 305 | BUY | ALL_IN | 17.0 | 7 | 89 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08662011474370956 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 6 | 5-5 | 306 | SELL | ALL_IN | 17.0 | 7 | 86 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -7de5aac5-85d7-4add-b5a7-1c89be9d7e40 |
| Jogador 6 | 5-5 | 307 | BUY | ALL_IN | 17.0 | 7 | 89 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0866180807352066 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -— |
| Jogador 6 | 5-5 | 308 | SELL | ALL_IN | 17.0 | 7 | 86 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -2b89bd83-8449-4c63-9da2-62a46c68bdf5 |
| Jogador 6 | 5-5 | 309 | BUY | ALL_IN | 17.0 | 7 | 89 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2198985368013382 | 0.0 | 0.0 | +674bcfdb-fddd-498c-ba65-ef3a3b989f07 / -— |
| Jogador 6 | 5-5 | 310 | SELL | ALL_IN | 17.0 | 7 | 87 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -674bcfdb-fddd-498c-ba65-ef3a3b989f07 |
| Jogador 6 | 5-6 | 312 | BUY | ALL_IN | 17.0 | 7 | 100 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9475491046905518 | 0.0 | 0.0 | +9f1c634e-13c7-4b59-838c-4b676fa059be / -— |
| Jogador 6 | 5-6 | 313 | SELL | ALL_IN | 17.0 | 7 | 97 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -407092ea-3a14-4555-9ebd-64a36c41d1d0 |
| Jogador 6 | 5-6 | 314 | BUY | ALL_IN | 17.0 | 7 | 100 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45461252331733704 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 6 | 5-6 | 315 | SELL | ALL_IN | 17.0 | 7 | 99 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6937000155448914 | 0.0 | 0.0 | +— / -85fb6db6-e1b0-4fa1-b99a-2f205305ef0b |
| Jogador 6 | 5-6 | 316 | BUY | ALL_IN | 17.0 | 7 | 100 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16799312829971313 | 0.0 | 0.0 | +be1e11e4-dc58-4e75-a402-3a2d831ac7b3 / -— |
| Jogador 6 | 5-6 | 317 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 97 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030905667692422867 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 318 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 97 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6600307822227478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 319 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 97 | 5 | 38.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08471421897411346 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 320 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 97 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08487704396247864 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 322 | SELL | ALL_IN | 17.0 | 7 | 107 | 5 | 44.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018588021397590637 | 0.0 | 0.0 | +— / -2ed895f2-1e83-426c-88fc-b9fb6403835d |
| Jogador 6 | 5-7 | 323 | BUY | ALL_IN | 17.0 | 7 | 110 | 5 | 44.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0512901544570923 | 0.0 | 0.0 | +7d8564c6-8151-4e04-b028-2121cb064215 / -bae633d7-8337-461a-9a84-9c9758392bb6,d80c845d-24bc-4053-a60d-5d0122839b0c |
| Jogador 6 | 5-7 | 324 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 107 | 5 | 32.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1529146432876587 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 325 | BUY | ALL_IN | 17.0 | 7 | 107 | 5 | 38.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44894078373908997 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 6 | 5-7 | 326 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 106 | 5 | 38.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5977966785430908 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 327 | BUY | ALL_IN | 17.0 | 7 | 106 | 5 | 50.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23570917546749115 | 0.0 | 0.0 | +1ad1f705-7e6b-4c1f-811c-2863dbf2db9e / -— |
| Jogador 6 | 5-7 | 328 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 103 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00011117709073005244 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 329 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 103 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 330 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 103 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024894367903470993 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 113 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.005366666708141565 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 333 | SELL | ALL_IN | 17.0 | 7 | 113 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004399999976158142 | 0.0 | 0.0 | +— / -1ad1f705-7e6b-4c1f-811c-2863dbf2db9e |
| Jogador 6 | 6-1 | 334 | BUY | ALL_IN | 17.0 | 7 | 116 | 5 | 50.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7910906672477722 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -— |
| Jogador 6 | 6-1 | 335 | SELL | ALL_IN | 17.0 | 7 | 113 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6937000155448914 | 0.0 | 0.0 | +— / -c93990ff-0a6f-46bc-8fc1-12623d55abc1 |
| Jogador 6 | 6-1 | 336 | BUY | ALL_IN | 17.0 | 7 | 114 | 5 | 50.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05255211889743805 | 0.0 | 0.0 | +d79de824-d9b2-4dfb-a7be-a359b416aea1 / -— |
| Jogador 6 | 6-1 | 337 | REROLL | ALL_IN | 17.0 | 7 | 111 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 338 | SELL | ALL_IN | 17.0 | 7 | 109 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -d79de824-d9b2-4dfb-a7be-a359b416aea1 |
| Jogador 6 | 6-1 | 339 | BUY | ALL_IN | 17.0 | 7 | 112 | 5 | 50.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22703175246715546 | 0.0 | 0.0 | +4b4293ce-1cca-473e-8c07-b441686985ac / -— |
| Jogador 6 | 6-1 | 340 | SELL | ALL_IN | 17.0 | 7 | 109 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -4b4293ce-1cca-473e-8c07-b441686985ac |
| Jogador 6 | 6-2 | 342 | BUY | ALL_IN | 17.0 | 7 | 122 | 5 | 50.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43057307600975037 | 0.0 | 0.0 | +9f271ee0-c506-40b7-b3f3-bac209974ba2 / -— |
| Jogador 6 | 6-2 | 343 | SELL | ALL_IN | 17.0 | 7 | 121 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6220004558563232 | 0.0 | 0.0 | +— / -2b10436d-ccfe-4329-aef8-2769899b3787 |
| Jogador 6 | 6-2 | 344 | BUY | ALL_IN | 17.0 | 7 | 124 | 5 | 50.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23695063591003418 | 0.0 | 0.0 | +8c4772c9-83f1-4021-b83f-a9ff1773bea0 / -— |
| Jogador 6 | 6-2 | 345 | SELL | ALL_IN | 17.0 | 7 | 121 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -8c4772c9-83f1-4021-b83f-a9ff1773bea0 |
| Jogador 6 | 6-2 | 346 | BUY | ALL_IN | 17.0 | 7 | 124 | 5 | 50.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1479686200618744 | 0.0 | 0.0 | +87902519-e44a-4d4c-9956-ac5aedc9b0c6 / -— |
| Jogador 6 | 6-2 | 347 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 122 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009323805570602417 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 348 | SELL | ALL_IN | 17.0 | 7 | 122 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0325281098484993 | 0.0 | 0.0 | +— / -87902519-e44a-4d4c-9956-ac5aedc9b0c6 |
| Jogador 6 | 6-2 | 349 | BUY | ALL_IN | 17.0 | 7 | 124 | 5 | 50.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06693556904792786 | 0.0 | 0.0 | +c55e9bf2-c9cf-4b76-a40c-6e8d73205402 / -— |
| Jogador 6 | 6-2 | 350 | REROLL | ALL_IN | 17.0 | 7 | 121 | 5 | 50.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40457043051719666 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.048290491104126 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23154349625110626 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368900299072266 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2447219043970108 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8282138705253601 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1995398998260498 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24522534012794495 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3011479377746582 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4377012252807617 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 64 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475761890411377 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 65 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15446917712688446 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1791847199201584 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0476582050323486 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.6826884746551514 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 74 | EQUIP_FROM_INVENTORY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1409839391708374 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 75 | EQUIP_FROM_INVENTORY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10851456224918365 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 76 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09810419380664825 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 77 | PASS | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3069070279598236 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20879311859607697 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12788841128349304 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32358306646347046 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08233333379030228 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-4 | 88 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2270868569612503 | 0.0 | 0.0 | +3280b28e-bd8f-494b-a78d-111744e2178b / -— |
| Jogador 7 | 2-4 | 89 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10828060656785965 | 0.0 | 0.0 | +— / -3280b28e-bd8f-494b-a78d-111744e2178b |
| Jogador 7 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0011077991221100092 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32316482067108154 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3267695903778076 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 94 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4610944986343384 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-5 | 96 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04367225617170334 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-5 | 97 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0054153203964233 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.963241457939148 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 104 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 105 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6157711148262024 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-6 | 106 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6251818537712097 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 2-6 | 107 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050634998828172684 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 108 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6269999742507935 | 0.0 | 0.0 | +— / -fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 2-6 | 109 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013304771855473518 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 112 | BUY | STABILIZE | 95.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2818029820919037 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 113 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 114 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 2-7 | 115 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01704118587076664 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 116 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ac02c0c4-a10d-497d-b6c1-d458ad7ae58c |
| Jogador 7 | 2-7 | 117 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 118 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21613341569900513 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2829407751560211 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18571749329566956 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 124 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 125 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.619088888168335 | 0.0 | 0.0 | +— / -033a84d9-70f6-46a8-a6eb-a2f03be70400 |
| Jogador 7 | 3-1 | 126 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06368608772754669 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002529659541323781 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 128 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08854430913925171 | 0.0 | 0.0 | +— / -ad1693cd-1ab5-43a9-8164-25929b8bd68e |
| Jogador 7 | 3-1 | 129 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2524043023586273 | 0.0 | 0.0 | +5d00c8ab-55fb-42ec-b8ec-75011c7722fc / -— |
| Jogador 7 | 3-1 | 130 | BUY | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08629923313856125 | 0.0 | 0.0 | +dbe9f465-e302-46d0-9bd4-93969fde6ecb / -— |
| Jogador 7 | 3-2 | 132 | BUY | STABILIZE | 85.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2677675187587738 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 133 | BUY | STABILIZE | 85.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25249525904655457 | 0.0 | 0.0 | +fa331d8d-1e0c-49b4-848e-8ad58859331c / -— |
| Jogador 7 | 3-2 | 134 | SELL | STABILIZE | 85.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045099999755620956 | 0.0 | 0.0 | +— / -dbe9f465-e302-46d0-9bd4-93969fde6ecb |
| Jogador 7 | 3-2 | 135 | BUY | STABILIZE | 85.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08628001064062119 | 0.0 | 0.0 | +8043a64c-a04d-4399-b52d-2246fe74e470 / -— |
| Jogador 7 | 3-2 | 136 | SELL | STABILIZE | 85.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3343333303928375 | 0.0 | 0.0 | +— / -8043a64c-a04d-4399-b52d-2246fe74e470 |
| Jogador 7 | 3-2 | 137 | SELL | STABILIZE | 85.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030533334240317345 | 0.0 | 0.0 | +— / -5d00c8ab-55fb-42ec-b8ec-75011c7722fc |
| Jogador 7 | 3-2 | 138 | BUY | STABILIZE | 85.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31226786971092224 | 0.0 | 0.0 | +96bf8f0a-9fe1-4182-95dc-903c1e623983 / -— |
| Jogador 7 | 3-2 | 139 | SELL | STABILIZE | 85.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19699999690055847 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 3-2 | 140 | BUY_XP | STABILIZE | 85.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | BUY | STABILIZE | 76.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8377366065979004 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -242805ca-f275-4e04-a2f5-81e0b6680dd1,7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 3-3 | 143 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 144 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 7 | 3-3 | 145 | BUY | STABILIZE | 76.0 | 6 | 4 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.08432763814926147 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 1 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.013093136250972748 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 147 | EQUIP_FROM_INVENTORY | STABILIZE | 76.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15541720390319824 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 148 | BUY | STABILIZE | 76.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25873202085494995 | 0.0 | 0.0 | +2399a42a-332c-42ee-9bd8-5f52bb921ffa / -— |
| Jogador 7 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0260844137519598 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 152 | BUY | STABILIZE | 76.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079814910888672 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 7 | 3-4 | 153 | BUY | STABILIZE | 76.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8334090709686279 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 154 | BUY | STABILIZE | 76.0 | 6 | 2 | 0 | 16.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28545570373535156 | 0.0 | 0.0 | +7e545d27-1847-4016-b42b-e7db1960ae89 / -— |
| Jogador 7 | 3-4 | 155 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 0 | 0 | 16.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4576675593852997 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 156 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 0 | 0 | 12.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2730194628238678 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014924944378435612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 158 | SELL | STABILIZE | 76.0 | 6 | 0 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6190000176429749 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 3-4 | 159 | BUY_XP | STABILIZE | 76.0 | 6 | 8 | 0 | 18.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 160 | MOVE_BENCH | STABILIZE | 76.0 | 7 | 4 | 0 | 18.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33183810114860535 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | STABILIZE | 76.0 | 7 | 9 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20226097106933594 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 163 | BUY | STABILIZE | 76.0 | 7 | 6 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20318055152893066 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 164 | BUY | STABILIZE | 76.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033798329532146454 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 7 | 3-5 | 165 | BUY | STABILIZE | 76.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0011853622272610664 | 0.0 | 0.0 | +2074e6ec-81e7-41c9-be7e-a0d9310fbafa / -— |
| Jogador 7 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 76.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0146877684746869e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 76.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000074170529842 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 76.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015161524526774883 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 169 | PASS | STABILIZE | 76.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | BUY | STABILIZE | 76.0 | 7 | 8 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28090900182724 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 173 | BUY | STABILIZE | 76.0 | 7 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0144646679982543 | 0.0 | 0.0 | +1726bcae-3006-426c-a6c7-4e317e10b637 / -— |
| Jogador 7 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 76.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001031512874760665 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 76.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015003676526248455 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 76.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015729010105133057 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 177 | PASS | STABILIZE | 76.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | BUY | STABILIZE | 64.0 | 7 | 5 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8009218573570251 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 183 | SELL | STABILIZE | 64.0 | 7 | 1 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04029826819896698 | 0.0 | 0.0 | +— / -42f739bb-e676-4a27-a96f-c09d09d592bb |
| Jogador 7 | 3-7 | 184 | BUY | STABILIZE | 64.0 | 7 | 2 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.805779755115509 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000739733106456697 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998147264122963 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997714199125767 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 188 | PASS | STABILIZE | 64.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 64.0 | 7 | 5 | 0 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1273757368326187 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 64.0 | 7 | 5 | 0 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14196504652500153 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | SELL | STABILIZE | 64.0 | 7 | 5 | 0 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -2074e6ec-81e7-41c9-be7e-a0d9310fbafa |
| Jogador 7 | 4-1 | 195 | BUY | STABILIZE | 64.0 | 7 | 7 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08659834414720535 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 7 | 4-1 | 196 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.304183379299502e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 197 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016714315861463547 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 198 | PASS | STABILIZE | 64.0 | 7 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | SELL | STABILIZE | 64.0 | 7 | 10 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -7c8b3027-1434-4346-95b3-5463e8a4aa9b |
| Jogador 7 | 4-2 | 203 | BUY | STABILIZE | 64.0 | 7 | 12 | 1 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.273831307888031 | 0.0 | 0.0 | +07cc291c-137e-4668-9caf-3a1fa8f09c3d / -— |
| Jogador 7 | 4-2 | 204 | SELL | STABILIZE | 64.0 | 7 | 10 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -f116ca4e-dbe8-457e-83a5-958525aa384a |
| Jogador 7 | 4-2 | 205 | BUY | STABILIZE | 64.0 | 7 | 13 | 1 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7927020192146301 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 7 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 11 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0016656954539939761 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 11 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 11 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015052362345159054 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 209 | PASS | STABILIZE | 64.0 | 7 | 11 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | SELL | STABILIZE | 64.0 | 7 | 19 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056166667491197586 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 7 | 4-3 | 213 | BUY | STABILIZE | 64.0 | 7 | 22 | 2 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8659160733222961 | 0.0 | 0.0 | +579b987a-fedf-45d8-92fc-634a041d3d4f / -21135c93-ae87-47a0-899c-7eaa0c2c30b8,7e545d27-1847-4016-b42b-e7db1960ae89 |
| Jogador 7 | 4-3 | 214 | BUY | STABILIZE | 64.0 | 7 | 20 | 2 | 20.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21204456686973572 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 7 | 4-3 | 215 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 16 | 1 | 20.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4232335686683655 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 216 | BUY | STABILIZE | 64.0 | 7 | 16 | 1 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014540293253958225 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 7 | 4-3 | 217 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 14 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 218 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 14 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 219 | PASS | STABILIZE | 64.0 | 7 | 14 | 1 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | SELL | STABILIZE | 64.0 | 7 | 22 | 2 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -579b987a-fedf-45d8-92fc-634a041d3d4f |
| Jogador 7 | 4-4 | 223 | BUY | STABILIZE | 64.0 | 7 | 27 | 2 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.29182156920433044 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 7 | 4-4 | 224 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 7 | 24 | 2 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11639716476202011 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 225 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 7 | 24 | 2 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1300784796476364 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 226 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 24 | 2 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.2267537385923788e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 24 | 2 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015123489312827587 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 24 | 2 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15235404670238495 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 229 | PASS | STABILIZE | 64.0 | 7 | 24 | 2 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03142857179045677 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | SELL | STABILIZE | 64.0 | 7 | 32 | 3 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023614726960659027 | 0.0 | 0.0 | +— / -8455b875-27e0-4172-9311-5cbb3e2242b9 |
| Jogador 7 | 4-5 | 233 | BUY | STABILIZE | 64.0 | 7 | 34 | 3 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7592632174491882 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 7 | 4-5 | 234 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 31 | 3 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09880577772855759 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 235 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 31 | 3 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01058387290686369 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 236 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 31 | 3 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 237 | PASS | STABILIZE | 64.0 | 7 | 31 | 3 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03642857074737549 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | STABILIZE | 64.0 | 7 | 40 | 4 | 24.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 7 | 4-6 | 243 | BUY | STABILIZE | 64.0 | 7 | 44 | 4 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9279950857162476 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -1ff50c59-5133-459e-8bf1-d449c26efabf,4e206e09-40e3-4699-81cb-8aaf01109dea |
| Jogador 7 | 4-6 | 244 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 7 | 43 | 4 | 20.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07680507749319077 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 245 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 7 | 43 | 4 | 20.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05623921751976013 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 246 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 43 | 4 | 20.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3035598397254944 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 247 | BUY | STABILIZE | 64.0 | 7 | 43 | 4 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7460494637489319 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 7 | 4-6 | 248 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 40 | 4 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 249 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 40 | 4 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49530360102653503 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 250 | BUY | STABILIZE | 64.0 | 7 | 40 | 4 | 32.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06204632297158241 | 0.0 | 0.0 | +5c931416-3aeb-40d4-9e6f-612b0d387226 / -— |
| Jogador 7 | 4-7 | 252 | SELL | STABILIZE | 53.0 | 7 | 45 | 4 | 32.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -565ff610-fe51-470b-8452-a7eec5e31653 |
| Jogador 7 | 4-7 | 253 | BUY | STABILIZE | 53.0 | 7 | 48 | 4 | 32.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9150223731994629 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 7 | 4-7 | 254 | BUY | STABILIZE | 53.0 | 7 | 45 | 4 | 26.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.34496834874153137 | 0.0 | 0.0 | +deb56311-9843-48be-9a22-3529305d04e5 / -— |
| Jogador 7 | 4-7 | 255 | EQUIP_FROM_INVENTORY | STABILIZE | 53.0 | 7 | 43 | 4 | 26.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06177247315645218 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | EQUIP_FROM_INVENTORY | STABILIZE | 53.0 | 7 | 43 | 4 | 26.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12814559042453766 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 257 | EQUIP_FROM_INVENTORY | STABILIZE | 53.0 | 7 | 43 | 4 | 26.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07333975285291672 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 258 | MOVE_BOARD | STABILIZE | 53.0 | 7 | 43 | 4 | 26.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 259 | MOVE_BOARD | STABILIZE | 53.0 | 7 | 43 | 4 | 26.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 260 | PASS | STABILIZE | 53.0 | 7 | 43 | 4 | 26.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | BUY | STABILIZE | 53.0 | 7 | 52 | 5 | 34.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.12196921557188034 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 53.0 | 7 | 50 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11630948632955551 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 53.0 | 7 | 50 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12632670998573303 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | MOVE_BOARD | STABILIZE | 53.0 | 7 | 50 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045521609485149384 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 266 | MOVE_BOARD | STABILIZE | 53.0 | 7 | 50 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011771567165851593 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 267 | MOVE_BOARD | STABILIZE | 53.0 | 7 | 50 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 268 | PASS | STABILIZE | 53.0 | 7 | 50 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | SELL | STABILIZE | 37.0 | 7 | 61 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5462689399719238 | 0.0 | 0.0 | +— / -b70671f9-0d78-4ae8-bd13-0267c96e7207 |
| Jogador 7 | 5-2 | 273 | BUY | STABILIZE | 37.0 | 7 | 69 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0046623945236206 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -96bf8f0a-9fe1-4182-95dc-903c1e623983,fa331d8d-1e0c-49b4-848e-8ad58859331c |
| Jogador 7 | 5-2 | 274 | BUY | STABILIZE | 37.0 | 7 | 67 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4504051208496094 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 7 | 5-2 | 275 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 65 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4658908247947693 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 276 | BUY | STABILIZE | 37.0 | 7 | 65 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017839282751083374 | 0.0 | 0.0 | +5e843c10-0a8b-4781-983a-8e6e6f28253e / -— |
| Jogador 7 | 5-2 | 277 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 62 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005876059178262949 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 278 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 62 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 279 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 62 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 280 | PASS | STABILIZE | 37.0 | 7 | 62 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11394098401069641 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | SELL | STABILIZE | 37.0 | 7 | 73 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07744169980287552 | 0.0 | 0.0 | +— / -e9bb05f6-3838-423a-bfd2-3791379b479e |
| Jogador 7 | 5-3 | 283 | BUY | STABILIZE | 37.0 | 7 | 78 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030451789498329163 | 0.0 | 0.0 | +987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 / -— |
| Jogador 7 | 5-3 | 284 | SELL | STABILIZE | 37.0 | 7 | 76 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 |
| Jogador 7 | 5-3 | 285 | BUY | STABILIZE | 37.0 | 7 | 78 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03054097294807434 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 7 | 5-3 | 286 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 76 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18119807541370392 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 287 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 76 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16140927374362946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 288 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 76 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02048027701675892 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 289 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 76 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01329317968338728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 290 | PASS | STABILIZE | 37.0 | 7 | 76 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12734846770763397 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | SELL | STABILIZE | 37.0 | 7 | 88 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -a5e92183-8d5d-434c-9294-47c6b7bfb91b |
| Jogador 7 | 5-4 | 293 | BUY | STABILIZE | 37.0 | 7 | 90 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8947362899780273 | 0.0 | 0.0 | +dcb61be2-9a58-49bc-9f11-2f5fce42e7ea / -— |
| Jogador 7 | 5-4 | 294 | SELL | STABILIZE | 37.0 | 7 | 87 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -5e843c10-0a8b-4781-983a-8e6e6f28253e |
| Jogador 7 | 5-4 | 295 | BUY | STABILIZE | 37.0 | 7 | 90 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04111194238066673 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 7 | 5-4 | 296 | SELL | STABILIZE | 37.0 | 7 | 86 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01850304566323757 | 0.0 | 0.0 | +— / -3faf4ab2-44b3-4779-985b-658c64791c28 |
| Jogador 7 | 5-4 | 297 | BUY | STABILIZE | 37.0 | 7 | 90 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026205310598015785 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -— |
| Jogador 7 | 5-4 | 298 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 88 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029184356331825256 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 299 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 88 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02037944085896015 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 300 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 88 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 302 | SELL | STABILIZE | 37.0 | 7 | 99 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -f2dbe099-e518-4261-b120-9f327b112dcb |
| Jogador 7 | 5-5 | 303 | BUY | STABILIZE | 37.0 | 7 | 101 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19860035181045532 | 0.0 | 0.0 | +9c07608c-00e1-40f1-9671-6d8bc584a6c9 / -— |
| Jogador 7 | 5-5 | 304 | SELL | STABILIZE | 37.0 | 7 | 100 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06539158523082733 | 0.0 | 0.0 | +— / -9c07608c-00e1-40f1-9671-6d8bc584a6c9 |
| Jogador 7 | 5-5 | 305 | BUY | STABILIZE | 37.0 | 7 | 101 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20628833770751953 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 7 | 5-5 | 306 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 98 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 307 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 98 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 308 | PASS | STABILIZE | 37.0 | 7 | 98 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1495940238237381 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | SELL | ALL_IN | 23.0 | 7 | 108 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -0c5adb43-b194-486e-b59c-c0f3b5479d40 |
| Jogador 7 | 5-6 | 313 | BUY | ALL_IN | 23.0 | 7 | 111 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15189272165298462 | 0.0 | 0.0 | +3c46b699-2b56-48d0-820c-b523c5153b9f / -— |
| Jogador 7 | 5-6 | 314 | SELL | ALL_IN | 23.0 | 7 | 108 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0343707799911499 | 0.0 | 0.0 | +— / -3c46b699-2b56-48d0-820c-b523c5153b9f |
| Jogador 7 | 5-6 | 315 | BUY | ALL_IN | 23.0 | 7 | 111 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003856369061395526 | 0.0 | 0.0 | +8068dc77-9528-4a1d-b4dc-5ac216e8684f / -— |
| Jogador 7 | 5-6 | 316 | SELL | ALL_IN | 23.0 | 7 | 108 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -8068dc77-9528-4a1d-b4dc-5ac216e8684f |
| Jogador 7 | 5-6 | 317 | BUY | ALL_IN | 23.0 | 7 | 111 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.051969822496175766 | 0.0 | 0.0 | +8faad4f9-9f15-49e8-94af-b4d28879cc0d / -— |
| Jogador 7 | 5-6 | 318 | MOVE_BOARD | ALL_IN | 23.0 | 7 | 109 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007840733975172043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 319 | MOVE_BOARD | ALL_IN | 23.0 | 7 | 109 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01492886058986187 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 320 | SELL | ALL_IN | 23.0 | 7 | 109 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -8faad4f9-9f15-49e8-94af-b4d28879cc0d |
| Jogador 7 | 5-7 | 322 | BUY | ALL_IN | 7.0 | 7 | 122 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9347676634788513 | 0.0 | 0.0 | +f9820f05-e1b0-4953-a98d-3ae191b1249a / -— |
| Jogador 7 | 5-7 | 323 | SELL | ALL_IN | 7.0 | 7 | 119 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04740837961435318 | 0.0 | 0.0 | +— / -1726bcae-3006-426c-a6c7-4e317e10b637 |
| Jogador 7 | 5-7 | 324 | BUY | ALL_IN | 7.0 | 7 | 123 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14576415717601776 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 7 | 5-7 | 325 | SELL | ALL_IN | 7.0 | 7 | 120 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -8538e488-6f36-433a-b261-73626f24bb07 |
| Jogador 7 | 5-7 | 326 | BUY | ALL_IN | 7.0 | 7 | 123 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21896766126155853 | 0.0 | 0.0 | +e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 / -— |
| Jogador 7 | 5-7 | 327 | SELL | ALL_IN | 7.0 | 7 | 122 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04633349925279617 | 0.0 | 0.0 | +— / -e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 |
| Jogador 7 | 5-7 | 328 | BUY | ALL_IN | 7.0 | 7 | 123 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0038771650288254023 | 0.0 | 0.0 | +93581e04-3f00-4430-8e5b-c953196bc1de / -— |
| Jogador 7 | 5-7 | 329 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 120 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.4204869330569636e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 330 | SELL | ALL_IN | 7.0 | 7 | 120 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -93581e04-3f00-4430-8e5b-c953196bc1de |
| Jogador 7 | 6-1 | 332 | BUY | ALL_IN | 7.0 | 7 | 134 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0053057670593262 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -aee0c45d-0178-4238-987f-5ee83dae7bce,ff181737-4995-4a67-add2-4f55cebabbee |
| Jogador 7 | 6-1 | 333 | BUY | ALL_IN | 7.0 | 7 | 132 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.051963530480861664 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 7 | 6-1 | 334 | BUY | ALL_IN | 7.0 | 7 | 130 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.2133522927761078 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -— |
| Jogador 7 | 6-1 | 335 | EQUIP_FROM_INVENTORY | ALL_IN | 7.0 | 7 | 127 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12130580842494965 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 336 | SELL | ALL_IN | 7.0 | 7 | 127 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09111744165420532 | 0.0 | 0.0 | +— / -a810e10d-e7ef-4ece-8fb2-8b6471b557ec |
| Jogador 7 | 6-1 | 337 | BUY | ALL_IN | 7.0 | 7 | 132 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25727394223213196 | 0.0 | 0.0 | +3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 / -— |
| Jogador 7 | 6-1 | 338 | SELL | ALL_IN | 7.0 | 7 | 128 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -2ac6d717-87f1-4421-929e-1934a9317e72 |
| Jogador 7 | 6-1 | 339 | BUY | ALL_IN | 7.0 | 7 | 130 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2690315246582031 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 7 | 6-1 | 340 | SELL | ALL_IN | 7.0 | 7 | 128 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -ae9da355-52b7-402c-be6e-41fa1148a550 |
| Jogador 7 | 6-2 | 342 | BUY | ALL_IN | 7.0 | 7 | 141 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9950669407844543 | 0.0 | 0.0 | +07080859-42b2-498e-9c11-257fea02f14b / -— |
| Jogador 7 | 6-2 | 343 | SELL | ALL_IN | 7.0 | 7 | 139 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -425a58b3-d906-4381-9afc-00f9852c9982 |
| Jogador 7 | 6-2 | 344 | BUY | ALL_IN | 7.0 | 7 | 142 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1088275909423828 | 0.0 | 0.0 | +b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 / -d175e09c-3ed6-4fb3-8c97-0c167862e29e,f9820f05-e1b0-4953-a98d-3ae191b1249a |
| Jogador 7 | 6-2 | 345 | BUY | ALL_IN | 7.0 | 7 | 139 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06397548317909241 | 0.0 | 0.0 | +249d7b90-0660-4e4f-885a-7791c1cac21a / -— |
| Jogador 7 | 6-2 | 346 | BUY | ALL_IN | 7.0 | 7 | 138 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0269436277449131 | 0.0 | 0.0 | +ffd44f6f-388e-4792-ae4f-77f2faa3e95f / -— |
| Jogador 7 | 6-2 | 347 | SELL | ALL_IN | 7.0 | 7 | 137 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7307999730110168 | 0.0 | 0.0 | +— / -b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 |
| Jogador 7 | 6-2 | 348 | BUY | ALL_IN | 7.0 | 7 | 145 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2669406533241272 | 0.0 | 0.0 | +54b8f150-85a6-4fad-9a4f-3b04897733cf / -— |
| Jogador 7 | 6-2 | 349 | SELL | ALL_IN | 7.0 | 7 | 143 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005590954329818487 | 0.0 | 0.0 | +— / -ffd44f6f-388e-4792-ae4f-77f2faa3e95f |
| Jogador 7 | 6-2 | 350 | SELL | ALL_IN | 7.0 | 7 | 144 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37630000710487366 | 0.0 | 0.0 | +— / -249d7b90-0660-4e4f-885a-7791c1cac21a |
| Jogador 7 | 6-3 | 352 | BUY | ALL_IN | 7.0 | 7 | 157 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4292373061180115 | 0.0 | 0.0 | +ae89881d-8a08-4f60-ad51-1b0fe152958d / -— |
| Jogador 7 | 6-3 | 353 | BUY | ALL_IN | 7.0 | 7 | 154 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04959909990429878 | 0.0 | 0.0 | +d8ca1093-815c-4f3e-af3e-fd6c4ab6ecd8 / -— |
| Jogador 7 | 6-3 | 354 | SELL | ALL_IN | 7.0 | 7 | 151 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -54b8f150-85a6-4fad-9a4f-3b04897733cf |
| Jogador 7 | 6-3 | 355 | BUY | ALL_IN | 7.0 | 7 | 153 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05679497495293617 | 0.0 | 0.0 | +14c1ca8a-e057-4184-9c83-0b8846824932 / -— |
| Jogador 7 | 6-3 | 356 | SELL | ALL_IN | 7.0 | 7 | 151 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -14c1ca8a-e057-4184-9c83-0b8846824932 |
| Jogador 7 | 6-3 | 357 | BUY | ALL_IN | 7.0 | 7 | 153 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26171207427978516 | 0.0 | 0.0 | +f55e2447-5d65-4f95-9f26-5b9017efefe0 / -— |
| Jogador 7 | 6-3 | 358 | SELL | ALL_IN | 7.0 | 7 | 150 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -f55e2447-5d65-4f95-9f26-5b9017efefe0 |
| Jogador 7 | 6-3 | 359 | BUY | ALL_IN | 7.0 | 7 | 153 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2718210816383362 | 0.0 | 0.0 | +9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 / -— |
| Jogador 7 | 6-3 | 360 | SELL | ALL_IN | 7.0 | 7 | 152 | 5 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 |
| Jogador 7 | 6-4 | 362 | BUY | ALL_IN | 7.0 | 7 | 164 | 5 | 36.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1080272197723389 | 0.0 | 0.0 | +24d03668-5dc4-4b40-9439-a1d67522d0a3 / -5c931416-3aeb-40d4-9e6f-612b0d387226,dcb61be2-9a58-49bc-9f11-2f5fce42e7ea |
| Jogador 7 | 6-4 | 363 | BUY | ALL_IN | 7.0 | 7 | 161 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1261601597070694 | 0.0 | 0.0 | +e903e009-8dae-4fc9-b0ec-bc028c3f9f3e / -— |
| Jogador 7 | 6-4 | 364 | SELL | ALL_IN | 7.0 | 7 | 160 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7307999730110168 | 0.0 | 0.0 | +— / -24d03668-5dc4-4b40-9439-a1d67522d0a3 |
| Jogador 7 | 6-4 | 365 | BUY | ALL_IN | 7.0 | 7 | 168 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0076624625362455845 | 0.0 | 0.0 | +f5a067a8-3eba-4efb-a5cf-76571eb8516e / -— |
| Jogador 7 | 6-4 | 366 | SELL | ALL_IN | 7.0 | 7 | 166 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -e903e009-8dae-4fc9-b0ec-bc028c3f9f3e |
| Jogador 7 | 6-4 | 367 | BUY | ALL_IN | 7.0 | 7 | 167 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26273980736732483 | 0.0 | 0.0 | +7fd34ef6-a124-4d23-a166-9f7ad919c826 / -— |
| Jogador 7 | 6-4 | 368 | SELL | ALL_IN | 7.0 | 7 | 164 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -f5a067a8-3eba-4efb-a5cf-76571eb8516e |
| Jogador 7 | 6-4 | 369 | BUY | ALL_IN | 7.0 | 7 | 166 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26806744933128357 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -— |
| Jogador 7 | 6-4 | 370 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 164 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5742306709289551 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 372 | BUY | ALL_IN | 7.0 | 7 | 175 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1037849187850952 | 0.0 | 0.0 | +533790d1-aca6-417d-b163-b0bda70d1500 / -07cc291c-137e-4668-9caf-3a1fa8f09c3d,08a36d54-bb5c-48a6-afb1-e0f9943bf069 |
| Jogador 7 | 6-5 | 373 | BUY | ALL_IN | 7.0 | 7 | 173 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4333026707172394 | 0.0 | 0.0 | +14f6071d-5085-47a5-b657-04043b21adce / -— |
| Jogador 7 | 6-5 | 374 | SELL | ALL_IN | 7.0 | 7 | 170 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14249999821186066 | 0.0 | 0.0 | +— / -533790d1-aca6-417d-b163-b0bda70d1500 |
| Jogador 7 | 6-5 | 375 | BUY | ALL_IN | 7.0 | 7 | 175 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2556701600551605 | 0.0 | 0.0 | +1cd4d2ae-a25f-4a8d-93e5-42284161b055 / -— |
| Jogador 7 | 6-5 | 376 | SELL | ALL_IN | 7.0 | 7 | 174 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -c3596d89-03d2-4fc7-afaf-591f10423252 |
| Jogador 7 | 6-5 | 377 | BUY | ALL_IN | 7.0 | 7 | 176 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12206202745437622 | 0.0 | 0.0 | +ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 / -— |
| Jogador 7 | 6-5 | 378 | SELL | ALL_IN | 7.0 | 7 | 174 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06619151681661606 | 0.0 | 0.0 | +— / -1cd4d2ae-a25f-4a8d-93e5-42284161b055 |
| Jogador 7 | 6-5 | 379 | BUY | ALL_IN | 7.0 | 7 | 175 | 5 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7114652395248413 | 0.0 | 0.0 | +0366f83c-b9d4-47c2-aa5e-4dc1021bd201 / -— |
| Jogador 7 | 6-5 | 380 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 173 | 5 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5757611989974976 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.50416499376297 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0143887996673584 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3602963089942932 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2804618179798126 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9756572246551514 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 44 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17336434125900269 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 45 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2515988051891327 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 46 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11602762341499329 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 47 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.114278793334961 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20073555409908295 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17906300723552704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05929341912269592 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1033570766448975 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12412204593420029 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03404243662953377 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40752023458480835 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06387472152709961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 64 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25714367628097534 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20797282457351685 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 66 | SELL | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045099999755620956 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 67 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07587534189224243 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 68 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4258500039577484 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 69 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004570872522890568 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 70 | PASS | STABILIZE | 95.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 72 | BUY | STABILIZE | 91.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.985266923904419 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 73 | BUY | STABILIZE | 91.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047898769378662 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -01f4a73c-7202-4ee3-964e-d32370c3c547,64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-3 | 74 | BUY | STABILIZE | 91.0 | 4 | 5 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36945509910583496 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 75 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 4 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09245023131370544 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 4 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3764873743057251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 77 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 4 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0056752851232886314 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07128899544477463 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 79 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4142305254936218 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 80 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 4 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020176058635115623 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 82 | BUY | STABILIZE | 84.0 | 4 | 10 | 1 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07478288561105728 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 83 | BUY | STABILIZE | 84.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15284138917922974 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 84 | BUY | STABILIZE | 84.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15354059636592865 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 85 | MOVE_BENCH | STABILIZE | 84.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011764369904994965 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 86 | BUY_XP | STABILIZE | 84.0 | 4 | 4 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 87 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35143810510635376 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 88 | SELL | STABILIZE | 84.0 | 5 | 0 | 0 | 18.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.214307963848114 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-4 | 89 | BUY | STABILIZE | 84.0 | 5 | 3 | 0 | 18.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15145903825759888 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 90 | SELL | STABILIZE | 84.0 | 5 | 2 | 0 | 18.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-5 | 92 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 18.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9002665877342224 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 93 | BUY | STABILIZE | 84.0 | 5 | 10 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7754866480827332 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 94 | BUY | STABILIZE | 84.0 | 5 | 8 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11065340042114258 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 95 | SELL | STABILIZE | 84.0 | 5 | 5 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011366666294634342 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-5 | 96 | BUY_XP | STABILIZE | 84.0 | 5 | 6 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 97 | SELL | STABILIZE | 84.0 | 5 | 2 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08850999921560287 | 0.0 | 0.0 | +— / -3644801e-2247-403d-8b81-d2d3f15c2f55 |
| Jogador 8 | 2-5 | 98 | BUY | STABILIZE | 84.0 | 5 | 3 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07265698164701462 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 1 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06338558346033096 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 1 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35388436913490295 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 84.0 | 5 | 7 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8992202877998352 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 103 | SELL | STABILIZE | 84.0 | 5 | 6 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028711585327982903 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 2-6 | 104 | BUY | STABILIZE | 84.0 | 5 | 8 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08494038879871368 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 105 | SELL | STABILIZE | 84.0 | 5 | 5 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013976681977510452 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-6 | 106 | SELL | STABILIZE | 84.0 | 5 | 7 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07317031174898148 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 2-6 | 107 | BUY | STABILIZE | 84.0 | 5 | 10 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17770321667194366 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 108 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 7 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 109 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 7 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023758811876177788 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 110 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3785082995891571 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 112 | BUY | STABILIZE | 77.0 | 5 | 12 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.876910924911499 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 113 | SELL | STABILIZE | 77.0 | 5 | 11 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06291050463914871 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 2-7 | 114 | BUY | STABILIZE | 77.0 | 5 | 14 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08707710355520248 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 115 | SELL | STABILIZE | 77.0 | 5 | 11 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2519777715206146 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 2-7 | 116 | BUY | STABILIZE | 77.0 | 5 | 14 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02226138673722744 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 117 | SELL | STABILIZE | 77.0 | 5 | 11 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024700000882148743 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 2-7 | 118 | BUY | STABILIZE | 77.0 | 5 | 14 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1474984586238861 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 8 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 13 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13278265297412872 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 120 | SELL | STABILIZE | 77.0 | 5 | 13 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0027000000700354576 | 0.0 | 0.0 | +— / -d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 8 | 3-1 | 122 | BUY | STABILIZE | 77.0 | 5 | 20 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03936824947595596 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 77.0 | 5 | 16 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2646680474281311 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 124 | SELL | STABILIZE | 77.0 | 5 | 16 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057733334600925446 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 8 | 3-1 | 125 | BUY | STABILIZE | 77.0 | 5 | 20 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12301119416952133 | 0.0 | 0.0 | +88420167-3841-43dd-b1d0-3e5ab2294c78 / -— |
| Jogador 8 | 3-1 | 126 | SELL | STABILIZE | 77.0 | 5 | 18 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -88420167-3841-43dd-b1d0-3e5ab2294c78 |
| Jogador 8 | 3-1 | 127 | BUY | STABILIZE | 77.0 | 5 | 20 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12292461842298508 | 0.0 | 0.0 | +a5c0595b-85f9-4c71-a156-675d22a7b3c2 / -— |
| Jogador 8 | 3-1 | 128 | SELL | STABILIZE | 77.0 | 5 | 18 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -a5c0595b-85f9-4c71-a156-675d22a7b3c2 |
| Jogador 8 | 3-1 | 129 | BUY | STABILIZE | 77.0 | 5 | 20 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14343641698360443 | 0.0 | 0.0 | +7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 / -— |
| Jogador 8 | 3-1 | 130 | SELL | STABILIZE | 77.0 | 5 | 18 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09143786877393723 | 0.0 | 0.0 | +— / -7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 |
| Jogador 8 | 3-2 | 132 | BUY | STABILIZE | 67.0 | 5 | 28 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7079315185546875 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655,fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 3-2 | 133 | BUY | STABILIZE | 67.0 | 5 | 27 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09736184775829315 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 134 | SELL | STABILIZE | 67.0 | 5 | 23 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1668114811182022 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 135 | BUY | STABILIZE | 67.0 | 5 | 26 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04334353283047676 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 67.0 | 5 | 24 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 137 | MOVE_BENCH | STABILIZE | 67.0 | 5 | 24 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15396836400032043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 138 | PASS | STABILIZE | 67.0 | 5 | 24 | 2 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02199999988079071 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 142 | BUY | STABILIZE | 55.0 | 5 | 32 | 3 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3000100255012512 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 8 | 3-3 | 143 | SELL | STABILIZE | 55.0 | 5 | 30 | 3 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004554311744868755 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 8 | 3-3 | 144 | BUY | STABILIZE | 55.0 | 5 | 32 | 3 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24969135224819183 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 145 | MOVE_BENCH | STABILIZE | 55.0 | 5 | 29 | 2 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35000261664390564 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 55.0 | 5 | 29 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 147 | PASS | STABILIZE | 55.0 | 5 | 29 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02449999935925007 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 152 | SELL | STABILIZE | 45.0 | 5 | 37 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10713333636522293 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 3-4 | 153 | BUY | STABILIZE | 45.0 | 5 | 41 | 4 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8829854130744934 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -5de56114-806a-4f58-8241-b3b8434a2154,b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 45.0 | 5 | 40 | 4 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006716725882142782 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 155 | MOVE_BENCH | STABILIZE | 45.0 | 5 | 40 | 4 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6768431663513184 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 156 | BUY | STABILIZE | 45.0 | 5 | 40 | 4 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013848074711859226 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -— |
| Jogador 8 | 3-4 | 157 | SELL | STABILIZE | 45.0 | 5 | 39 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8025000095367432 | 0.0 | 0.0 | +— / -eb7e36f0-cef9-4a2e-979a-f8a357da73e8 |
| Jogador 8 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 45.0 | 5 | 42 | 4 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.365923672914505 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 159 | MOVE_BENCH | STABILIZE | 45.0 | 5 | 42 | 4 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1627703160047531 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 160 | PASS | STABILIZE | 45.0 | 5 | 42 | 4 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1289999932050705 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 162 | BUY | STABILIZE | 45.0 | 6 | 52 | 5 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.84312504529953 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 163 | BUY | STABILIZE | 45.0 | 6 | 50 | 5 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8152382969856262 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -1af578c1-57cf-4752-93e7-d0eebc6e8ae5,9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 45.0 | 6 | 48 | 4 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00471291970461607 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 45.0 | 6 | 48 | 4 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3439667224884033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 166 | BUY | STABILIZE | 45.0 | 6 | 48 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29843682050704956 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 167 | BUY | STABILIZE | 45.0 | 6 | 45 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0661819577217102 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 45.0 | 6 | 42 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15865716338157654 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 45.0 | 6 | 42 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06515269726514816 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 170 | BUY_XP | STABILIZE | 45.0 | 6 | 42 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06834399700164795 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 172 | BUY | STABILIZE | 33.0 | 6 | 48 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8264415860176086 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -— |
| Jogador 8 | 3-6 | 173 | SELL | STABILIZE | 33.0 | 6 | 45 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 |
| Jogador 8 | 3-6 | 174 | BUY | STABILIZE | 33.0 | 6 | 50 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28067612648010254 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 175 | SELL | STABILIZE | 33.0 | 6 | 47 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07127673923969269 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 3-6 | 176 | BUY | STABILIZE | 33.0 | 6 | 50 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2588197588920593 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 8 | 3-6 | 177 | SELL | STABILIZE | 33.0 | 6 | 48 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3432949185371399 | 0.0 | 0.0 | +— / -e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 3-6 | 178 | BUY | STABILIZE | 33.0 | 6 | 51 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17460739612579346 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 179 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 47 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09998304396867752 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 180 | SELL | STABILIZE | 33.0 | 6 | 47 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08767732232809067 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 3-7 | 182 | BUY | STABILIZE | 33.0 | 6 | 61 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15913845598697662 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 183 | SELL | STABILIZE | 33.0 | 6 | 58 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 3-7 | 184 | BUY | STABILIZE | 33.0 | 6 | 61 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20676876604557037 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 185 | SELL | STABILIZE | 33.0 | 6 | 58 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 3-7 | 186 | BUY | STABILIZE | 33.0 | 6 | 61 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012662357650697231 | 0.0 | 0.0 | +014c92c3-e588-4e8b-b4bd-93cee45d74af / -— |
| Jogador 8 | 3-7 | 187 | SELL | STABILIZE | 33.0 | 6 | 60 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -014c92c3-e588-4e8b-b4bd-93cee45d74af |
| Jogador 8 | 3-7 | 188 | BUY | STABILIZE | 33.0 | 6 | 61 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0069831362925469875 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 189 | SELL | STABILIZE | 33.0 | 6 | 60 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008901541121304035 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 33.0 | 6 | 61 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006709045264869928 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | BUY | STABILIZE | 33.0 | 6 | 71 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.36897557973861694 | 0.0 | 0.0 | +b750b244-a898-479e-9a8e-f30a3f4b0005 / -— |
| Jogador 8 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 33.0 | 6 | 70 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21970976889133453 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 33.0 | 6 | 70 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2367083579301834 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 195 | SELL | STABILIZE | 33.0 | 6 | 70 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 8 | 4-1 | 196 | BUY | STABILIZE | 33.0 | 6 | 74 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.927223265171051 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -35e1a0f6-207d-4df2-b096-fc07962d094a,a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 4-1 | 197 | BUY | STABILIZE | 33.0 | 6 | 72 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21314963698387146 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 8 | 4-1 | 198 | BUY | STABILIZE | 33.0 | 6 | 69 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03275642544031143 | 0.0 | 0.0 | +e94d3ae5-8c17-4d86-b6d9-f8141ac1756b / -— |
| Jogador 8 | 4-1 | 199 | SELL | STABILIZE | 33.0 | 6 | 67 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5160999894142151 | 0.0 | 0.0 | +— / -5af104f2-7959-4ca5-91a9-7d44494532ea |
| Jogador 8 | 4-1 | 200 | BUY | STABILIZE | 33.0 | 6 | 72 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012986117042601109 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 8 | 4-2 | 202 | SELL | ALL_IN | 22.0 | 6 | 81 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -6fa83356-562b-4a26-a77d-3e989089e70a |
| Jogador 8 | 4-2 | 203 | BUY | ALL_IN | 22.0 | 6 | 82 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.939873218536377 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 8 | 4-2 | 204 | SELL | ALL_IN | 22.0 | 6 | 79 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -e94d3ae5-8c17-4d86-b6d9-f8141ac1756b |
| Jogador 8 | 4-2 | 205 | BUY | ALL_IN | 22.0 | 6 | 81 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.014289379119873 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 4-2 | 206 | BUY | ALL_IN | 22.0 | 6 | 80 | 5 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0785643681883812 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 8 | 4-2 | 207 | MOVE_BENCH | ALL_IN | 22.0 | 6 | 76 | 5 | 22.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5227137804031372 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 208 | BUY | ALL_IN | 22.0 | 6 | 76 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28331273794174194 | 0.0 | 0.0 | +cb30dcaa-bc26-4584-9b50-24e47e70fcb0 / -— |
| Jogador 8 | 4-2 | 209 | MOVE_BOARD | ALL_IN | 22.0 | 6 | 74 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 210 | MOVE_BOARD | ALL_IN | 22.0 | 6 | 74 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30455124378204346 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 212 | SELL | ALL_IN | 9.0 | 6 | 85 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7186999917030334 | 0.0 | 0.0 | +— / -ea460790-b046-451d-9174-8b613e476241 |
| Jogador 8 | 4-3 | 213 | BUY | ALL_IN | 9.0 | 6 | 88 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0720767974853516 | 0.0 | 0.0 | +6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1,d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-3 | 214 | BUY | ALL_IN | 9.0 | 6 | 85 | 5 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9538350105285645 | 0.0 | 0.0 | +3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 / -— |
| Jogador 8 | 4-3 | 215 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 6 | 83 | 5 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12696363031864166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 216 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 6 | 83 | 5 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11226355284452438 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 217 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 6 | 83 | 5 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07544413954019547 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 218 | SELL | ALL_IN | 9.0 | 6 | 83 | 5 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7251999974250793 | 0.0 | 0.0 | +— / -6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 |
| Jogador 8 | 4-3 | 219 | BUY | ALL_IN | 9.0 | 6 | 91 | 5 | 18.0 | Enfeitiçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6152973175048828 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 8 | 4-3 | 220 | REROLL | ALL_IN | 9.0 | 6 | 89 | 5 | 18.0 | Enfeitiçador/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 256 | 258 | 163 | 11 | 9 | 0 | 0 | 0 | 135 | 38.0 |
- Jogador 1 — gasto por ação: BUY: 210g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 46g, stage 3: 67g, stage 4: 61g, stage 5: 65g, stage 6: 13g
| Jogador 2 | 298 | 369 | 197 | 6 | 26 | 0 | 0 | 0 | 85 | 48.0 |
- Jogador 2 — gasto por ação: BUY: 257g, BUY_XP: 112g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 58g, stage 3: 82g, stage 4: 53g, stage 5: 80g, stage 6: 89g
| Jogador 3 | 179 | 169 | 81 | 8 | 9 | 0 | 2 | 0 | 75 | 36.0 |
- Jogador 3 — gasto por ação: BUY: 129g, BUY_XP: 36g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 39g, stage 3: 64g, stage 4: 51g, stage 5: 8g
| Jogador 4 | 208 | 198 | 123 | 7 | 6 | 1 | 0 | 0 | 117 | 32.0 |
- Jogador 4 — gasto por ação: BUY: 166g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 48g, stage 4: 70g, stage 5: 16g
| Jogador 5 | 279 | 305 | 213 | 8 | 9 | 0 | 3 | 0 | 160 | 24.0 |
- Jogador 5 — gasto por ação: BUY: 251g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 6g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 65g, stage 3: 78g, stage 4: 63g, stage 5: 53g, stage 6: 39g
| Jogador 6 | 255 | 258 | 148 | 7 | 10 | 0 | 2 | 0 | 119 | 50.0 |
- Jogador 6 — gasto por ação: BUY: 210g, BUY_XP: 44g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 64g, stage 3: 63g, stage 4: 44g, stage 5: 60g, stage 6: 22g
| Jogador 7 | 289 | 269 | 172 | 2 | 10 | 1 | 0 | 0 | 173 | 34.0 |
- Jogador 7 — gasto por ação: BUY: 221g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 66g, stage 3: 65g, stage 4: 33g, stage 5: 44g, stage 6: 55g
| Jogador 8 | 165 | 145 | 95 | 14 | 2 | 0 | 1 | 0 | 87 | 18.0 |
- Jogador 8 — gasto por ação: BUY: 131g, BUY_XP: 12g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 52g, stage 3: 58g, stage 4: 28g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 12 | 5 |
- Jogador 1 · 4-3 · step 220: PASS com 20g, HP 70, nível 7/8 (STABILIZE).
- Jogador 1 · 4-4 · step 230: PASS com 17g, HP 70, nível 7/8 (STABILIZE).
- Jogador 1 · 4-6 · step 249: PASS com 35g, HP 70, nível 7/8 (STABILIZE).
- Jogador 1 · 4-7 · step 258: PASS com 49g, HP 70, nível 7/8 (STABILIZE).
- Jogador 1 · 5-4 · step 300: PASS com 90g, HP 26, nível 7/8 (STABILIZE).
| Jogador 2 | 28 | 2 |
- Jogador 2 · 4-4 · step 230: PASS com 4g, HP 59, nível 7/8 (STABILIZE).
- Jogador 2 · 4-5 · step 235: PASS com 6g, HP 59, nível 7/8 (FAST8).
| Jogador 3 | 9 | 12 |
- Jogador 3 · 2-6 · step 108: PASS com 5g, HP 90, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 118: PASS com 7g, HP 84, nível 5/8 (STABILIZE).
- Jogador 3 · 3-2 · step 135: PASS com 20g, HP 74, nível 5/8 (STABILIZE).
- Jogador 3 · 3-6 · step 180: PASS com 13g, HP 54, nível 6/8 (STABILIZE).
- Jogador 3 · 3-7 · step 187: PASS com 14g, HP 43, nível 6/8 (STABILIZE).
- Jogador 3 · 4-1 · step 200: PASS com 16g, HP 43, nível 6/8 (STABILIZE).
- Jogador 3 · 4-2 · step 209: PASS com 25g, HP 43, nível 7/8 (STABILIZE).
- Jogador 3 · 4-3 · step 216: PASS com 34g, HP 43, nível 7/8 (STABILIZE).
- Jogador 3 · 4-5 · step 239: PASS com 48g, HP 32, nível 7/8 (STABILIZE).
- Jogador 3 · 4-6 · step 248: PASS com 51g, HP 21, nível 7/8 (ALL_IN).
- Jogador 3 · 4-7 · step 259: REROLL com 61g, HP 9, nível 7/8 (ALL_IN).
- Jogador 3 · 5-1 · step 269: REROLL com 74g, HP 9, nível 7/8 (ALL_IN).
| Jogador 4 | 8 | 8 |
- Jogador 4 · 3-2 · step 138: PASS com 6g, HP 83, nível 6/8 (STABILIZE).
- Jogador 4 · 3-4 · step 159: PASS com 10g, HP 60, nível 6/8 (STABILIZE).
- Jogador 4 · 3-6 · step 179: PASS com 24g, HP 49, nível 6/8 (STABILIZE).
- Jogador 4 · 3-7 · step 189: PASS com 32g, HP 39, nível 6/8 (STABILIZE).
- Jogador 4 · 4-1 · step 200: PASS com 37g, HP 39, nível 6/8 (STABILIZE).
- Jogador 4 · 4-4 · step 230: PASS com 62g, HP 1, nível 7/8 (ALL_IN).
- Jogador 4 · 4-7 · step 260: PASS com 91g, HP 1, nível 7/8 (ALL_IN).
- Jogador 4 · 5-2 · step 280: PASS com 117g, HP 1, nível 7/8 (ALL_IN).
| Jogador 5 | 12 | 7 |
- Jogador 5 · 3-7 · step 188: REROLL com 5g, HP 75, nível 7/8 (STABILIZE).
- Jogador 5 · 4-2 · step 209: PASS com 15g, HP 75, nível 7/8 (STABILIZE).
- Jogador 5 · 5-2 · step 279: PASS com 74g, HP 52, nível 7/8 (STABILIZE).
- Jogador 5 · 5-3 · step 290: PASS com 87g, HP 52, nível 7/8 (STABILIZE).
- Jogador 5 · 5-5 · step 306: PASS com 109g, HP 52, nível 7/8 (STABILIZE).
- Jogador 5 · 6-2 · step 347: REROLL com 144g, HP 19, nível 7/8 (ALL_IN).
- Jogador 5 · 6-3 · step 354: REROLL com 157g, HP 1, nível 7/8 (ALL_IN).
| Jogador 6 | 11 | 8 |
- Jogador 6 · 3-7 · step 189: PASS com 4g, HP 67, nível 7/8 (STABILIZE).
- Jogador 6 · 4-2 · step 208: PASS com 9g, HP 56, nível 7/8 (STABILIZE).
- Jogador 6 · 4-4 · step 230: PASS com 18g, HP 44, nível 7/8 (FAST8).
- Jogador 6 · 4-5 · step 236: PASS com 27g, HP 44, nível 7/8 (FAST8).
- Jogador 6 · 4-6 · step 246: PASS com 33g, HP 44, nível 7/8 (FAST8).
- Jogador 6 · 5-1 · step 270: PASS com 50g, HP 32, nível 7/8 (STABILIZE).
- Jogador 6 · 6-1 · step 337: REROLL com 111g, HP 17, nível 7/8 (ALL_IN).
- Jogador 6 · 6-2 · step 350: REROLL com 121g, HP 17, nível 7/8 (ALL_IN).
| Jogador 7 | 12 | 10 |
- Jogador 7 · 4-1 · step 198: PASS com 4g, HP 64, nível 7/8 (STABILIZE).
- Jogador 7 · 4-2 · step 209: PASS com 11g, HP 64, nível 7/8 (STABILIZE).
- Jogador 7 · 4-3 · step 219: PASS com 14g, HP 64, nível 7/8 (STABILIZE).
- Jogador 7 · 4-4 · step 229: PASS com 24g, HP 64, nível 7/8 (STABILIZE).
- Jogador 7 · 4-5 · step 237: PASS com 31g, HP 64, nível 7/8 (STABILIZE).
- Jogador 7 · 4-7 · step 260: PASS com 43g, HP 53, nível 7/8 (STABILIZE).
- Jogador 7 · 5-1 · step 268: PASS com 50g, HP 53, nível 7/8 (STABILIZE).
- Jogador 7 · 5-2 · step 280: PASS com 62g, HP 37, nível 7/8 (STABILIZE).
- Jogador 7 · 5-3 · step 290: PASS com 76g, HP 37, nível 7/8 (STABILIZE).
- Jogador 7 · 5-5 · step 308: PASS com 98g, HP 37, nível 7/8 (STABILIZE).
| Jogador 8 | 3 | 4 |
- Jogador 8 · 3-2 · step 138: PASS com 24g, HP 67, nível 5/8 (STABILIZE).
- Jogador 8 · 3-3 · step 147: PASS com 29g, HP 55, nível 5/8 (STABILIZE).
- Jogador 8 · 3-4 · step 160: PASS com 42g, HP 45, nível 5/8 (STABILIZE).
- Jogador 8 · 4-3 · step 220: REROLL com 89g, HP 9, nível 6/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 2 | 2 | 0 | 0.0% |
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
| Jogador 1 | 256 | 48 | 46 | 162 | 0.0013 | 0.2566 | 0.0000 | 0.3435 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0138 (93 ações), BUY_XP: Δ 0.0117 (12 ações), CRAFT_AND_EQUIP: Δ 0.0020 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0255 (16 ações), MOVE_BOARD: Δ 0.0092 (51 ações), PASS: Δ 0.0000 (17 ações), SELL: Δ 0.0110 (54 ações)
| Jogador 2 | 298 | 44 | 35 | 219 | 0.0014 | 0.4280 | 0.0008 | 0.2996 | 0.0006 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0116 (105 ações), BUY_XP: Δ 0.0035 (28 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0585 (23 ações), MOVE_BOARD: Δ -0.0070 (50 ações), PASS: Δ 0.0000 (15 ações), SELL: Δ 0.0079 (69 ações)
| Jogador 3 | 179 | 37 | 36 | 106 | 0.0029 | 0.2613 | 0.0019 | 0.2847 | 0.0010 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0182 (56 ações), BUY_XP: Δ 0.0000 (9 ações), CRAFT_AND_EQUIP: Δ 0.0106 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0379 (19 ações), MOVE_BOARD: Δ 0.0061 (43 ações), PASS: Δ 0.0000 (20 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0219 (22 ações)
| Jogador 4 | 208 | 44 | 33 | 131 | 0.0027 | 0.1653 | 0.0013 | 0.4173 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0143 (78 ações), BUY_XP: Δ 0.0135 (8 ações), CRAFT_AND_EQUIP: Δ 0.0036 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0377 (19 ações), MOVE_BOARD: Δ 0.0096 (33 ações), PASS: Δ 0.0000 (16 ações), SELL: Δ 0.0114 (45 ações)
| Jogador 5 | 279 | 43 | 40 | 196 | 0.0003 | 0.1681 | -0.0005 | 0.3764 | 0.0009 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0249 (110 ações), BUY_XP: Δ 0.0117 (12 ações), CRAFT_AND_EQUIP: Δ 0.0049 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0856 (8 ações), MOVE_BENCH: Δ 0.0124 (20 ações), MOVE_BOARD: Δ 0.0187 (30 ações), PASS: Δ 0.0000 (12 ações), REROLL: Δ 0.0000 (3 ações), SELL: Δ 0.0150 (77 ações)
| Jogador 6 | 255 | 55 | 53 | 147 | 0.0032 | -0.0344 | 0.0022 | 0.3960 | 0.0010 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0123 (87 ações), BUY_XP: Δ 0.0024 (11 ações), CRAFT_AND_EQUIP: Δ 0.0037 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0029 (3 ações), MOVE_BENCH: Δ -0.0015 (22 ações), MOVE_BOARD: Δ 0.0257 (49 ações), PASS: Δ 0.0000 (16 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0103 (58 ações)
| Jogador 7 | 289 | 57 | 43 | 189 | 0.0022 | 0.2530 | 0.0015 | 0.2996 | 0.0007 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0157 (100 ações), BUY_XP: Δ 0.0083 (12 ações), CRAFT_AND_EQUIP: Δ 0.0086 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0076 (11 ações), MOVE_BENCH: Δ 0.0246 (16 ações), MOVE_BOARD: Δ 0.0132 (61 ações), PASS: Δ 0.0000 (20 ações), SELL: Δ 0.0123 (62 ações)
| Jogador 8 | 165 | 38 | 32 | 95 | -0.0006 | -0.3768 | -0.0030 | 0.3486 | 0.0024 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0008 (67 ações), BUY_XP: Δ 0.0152 (3 ações), CRAFT_AND_EQUIP: Δ 0.0042 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0120 (3 ações), MOVE_BENCH: Δ -0.0142 (32 ações), MOVE_BOARD: Δ -0.0171 (10 ações), PASS: Δ 0.0000 (8 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0133 (36 ações)
- Jogador 1 — rounds avaliados: 33; correlação estrutural/combate: 0.013; posicional/combate: 0.238.
- Jogador 1 — combate positive: score estrutural prévio 0.195
  score posicional prévio 0.366
- Jogador 1 — combate negative: score estrutural prévio 0.176
  score posicional prévio 0.308
- Jogador 2 — rounds avaliados: 37; correlação estrutural/combate: 0.030; posicional/combate: -0.301.
- Jogador 2 — combate positive: score estrutural prévio 0.490
  score posicional prévio 0.271
- Jogador 2 — combate negative: score estrutural prévio 0.529
  score posicional prévio 0.302
- Jogador 3 — rounds avaliados: 26; correlação estrutural/combate: 0.079; posicional/combate: -0.008.
- Jogador 3 — combate positive: score estrutural prévio 0.284
  score posicional prévio 0.305
- Jogador 3 — combate negative: score estrutural prévio 0.242
  score posicional prévio 0.290
- Jogador 4 — rounds avaliados: 27; correlação estrutural/combate: 0.011; posicional/combate: -0.287.
- Jogador 4 — combate positive: score estrutural prévio 0.206
  score posicional prévio 0.395
- Jogador 4 — combate negative: score estrutural prévio 0.176
  score posicional prévio 0.460
- Jogador 5 — rounds avaliados: 35; correlação estrutural/combate: 0.145; posicional/combate: 0.302.
- Jogador 5 — combate positive: score estrutural prévio 0.215
  score posicional prévio 0.393
- Jogador 5 — combate negative: score estrutural prévio 0.142
  score posicional prévio 0.337
- Jogador 6 — rounds avaliados: 34; correlação estrutural/combate: 0.202; posicional/combate: -0.231.
- Jogador 6 — combate positive: score estrutural prévio 0.124
  score posicional prévio 0.370
- Jogador 6 — combate negative: score estrutural prévio -0.296
  score posicional prévio 0.443
- Jogador 7 — rounds avaliados: 37; correlação estrutural/combate: -0.031; posicional/combate: -0.139.
- Jogador 7 — combate positive: score estrutural prévio 0.217
  score posicional prévio 0.277
- Jogador 7 — combate negative: score estrutural prévio 0.274
  score posicional prévio 0.323
- Jogador 8 — rounds avaliados: 21; correlação estrutural/combate: 0.353; posicional/combate: 0.107.
- Jogador 8 — combate positive: score estrutural prévio -0.223
  score posicional prévio 0.374
- Jogador 8 — combate negative: score estrutural prévio -0.504
  score posicional prévio 0.349

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 288 | OK (288) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Crownguard, TFT_Item_Deathblade, TFT_Item_JeweledGauntlet, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_SpectralGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 335 | OK (335) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_GargoyleStoneplate, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 204 | OK (204) | 7 | 0 | 0 | 0 | 7 | 1 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 234 | OK (234) | 7 | 0 | 0 | 0 | 7 | 2 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_BlueBuff, TFT_Item_JeweledGauntlet, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 313 | OK (313) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_GuinsoosRageblade, TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 288 | OK (288) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 6 — IDs equipados observados: DA_18_EmblemSpellweaver, TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 325 | OK (325) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 185 | OK (185) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_LastWhisper, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.012 | 0.366 |
| Jogador 1 | 2-2 | 8 | 2.000 | -4.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 10 | 7 | 4 → 5 | -0.034 | 0.330 |
| Jogador 1 | 2-3 | 9 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 18% → 18% | 10 → 5 | 11 | 5 → 5 | 0.000 | -0.281 |
| Jogador 1 | 2-4 | 4 | 2.000 | -2.000 | 0 → 0 | 3 → 2 | 18% → 18% | 5 → 5 | 5 | 5 → 5 | -0.008 | 0.000 |
| Jogador 1 | 2-5 | 10 | 4.000 | 0.000 | 0 → 0 | 2 → 3 | 18% → 21% | 5 → 6 | 8 | 5 → 6 | 0.023 | 0.285 |
| Jogador 1 | 2-6 | 6 | 2.000 | 8.000 | 0 → 0 | 3 → 2 | 21% → 21% | 6 → 7 | 6 | 6 → 6 | 0.016 | 0.459 |
| Jogador 1 | 2-7 | 10 | 0.000 | 2.000 | 0 → 1 | 2 → 2 | 21% → 18% | 7 → 12 | 4 | 6 → 6 | 0.022 | 0.000 |
| Jogador 1 | 3-1 | 10 | 2.000 | 12.000 | 1 → 1 | 2 → 2 | 18% → 21% | 12 → 8 | 11 | 6 → 6 | -0.054 | 0.286 |
| Jogador 1 | 3-2 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 5 | 21% → 21% | 8 → 8 | 12 | 6 → 6 | 0.023 | 0.277 |
| Jogador 1 | 3-3 | 10 | 0.000 | -10.000 | 1 → 1 | 5 → 4 | 21% → 21% | 8 → 6 | 18 | 6 → 6 | 0.000 | -0.291 |
| Jogador 1 | 3-4 | 10 | 4.000 | -2.000 | 1 → 1 | 4 → 4 | 21% → 25% | 6 → 6 | 8 | 6 → 7 | 0.045 | 0.000 |
| Jogador 1 | 3-5 | 10 | 6.000 | 0.000 | 1 → 2 | 4 → 2 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | -0.020 | 0.300 |
| Jogador 1 | 3-6 | 8 | 0.000 | 12.000 | 2 → 2 | 2 → 3 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | -0.038 | -0.352 |
| Jogador 1 | 3-7 | 8 | 0.000 | 8.000 | 2 → 2 | 3 → 4 | 25% → 25% | 5 → 7 | 6 | 7 → 7 | 0.108 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 4.000 | 2 → 2 | 4 → 5 | 25% → 25% | 7 → 11 | 9 | 7 → 7 | -0.019 | 0.285 |
| Jogador 1 | 4-2 | 10 | 0.000 | 2.000 | 2 → 2 | 5 → 5 | 25% → 25% | 11 → 18 | 7 | 7 → 7 | 0.012 | 0.311 |
| Jogador 1 | 4-3 | 10 | 0.000 | -4.000 | 2 → 2 | 5 → 5 | 25% → 25% | 18 → 29 | 5 | 7 → 7 | 0.009 | 0.306 |
| Jogador 1 | 4-4 | 10 | 0.000 | 12.000 | 2 → 2 | 5 → 3 | 25% → 25% | 29 → 24 | 13 | 7 → 7 | -0.006 | 0.000 |
| Jogador 1 | 4-5 | 10 | 0.000 | -4.000 | 2 → 2 | 3 → 3 | 25% → 25% | 24 → 40 | 14 | 7 → 7 | 0.004 | 0.293 |
| Jogador 1 | 4-6 | 9 | 4.000 | 2.000 | 2 → 2 | 3 → 2 | 25% → 25% | 40 → 46 | 8 | 7 → 7 | -0.011 | 0.332 |
| Jogador 1 | 4-7 | 8 | 0.000 | -4.000 | 2 → 2 | 2 → 2 | 25% → 25% | 46 → 60 | 5 | 7 → 7 | -0.006 | 0.000 |
| Jogador 1 | 5-1 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 3 | 25% → 25% | 60 → 67 | 12 | 7 → 7 | -0.006 | -0.273 |
| Jogador 1 | 5-2 | 10 | 4.000 | 12.000 | 2 → 2 | 3 → 2 | 25% → 25% | 67 → 70 | 11 | 7 → 7 | -0.011 | -0.285 |
| Jogador 1 | 5-3 | 10 | 0.000 | -12.000 | 2 → 2 | 2 → 2 | 25% → 25% | 70 → 89 | 7 | 7 → 7 | 0.054 | -0.280 |
| Jogador 1 | 5-4 | 10 | 0.000 | -2.000 | 2 → 2 | 2 → 3 | 25% → 25% | 89 → 101 | 6 | 7 → 7 | -0.022 | 0.000 |
| Jogador 1 | 5-5 | 10 | 0.000 | -2.000 | 2 → 2 | 3 → 3 | 25% → 25% | 101 → 113 | 8 | 7 → 7 | -0.084 | -0.280 |
| Jogador 1 | 5-6 | 10 | 0.000 | 2.000 | 2 → 2 | 3 → 3 | 25% → 25% | 113 → 123 | 10 | 7 → 7 | -0.002 | 0.302 |
| Jogador 1 | 5-7 | 10 | 0.000 | -2.000 | 2 → 2 | 3 → 2 | 25% → 25% | 123 → 133 | 11 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 10 | -38.000 | -46.000 | 2 → 0 | 2 → 0 | 25% → 0% | 133 → 135 | 13 | 7 → 7 | -0.021 | -0.275 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 32, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 13, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 51 ações e piorou em 50.
- Jogador 1 — estado final: ouro 135, nível 7, vida 10.0, colocação 5.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 10 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | 0.026 | -0.226 |
| Jogador 2 | 2-2 | 8 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.041 | -0.310 |
| Jogador 2 | 2-3 | 10 | 6.000 | -2.000 | 1 → 1 | 1 → 1 | 14% → 18% | 6 → 6 | 10 | 4 → 5 | 0.005 | 0.269 |
| Jogador 2 | 2-4 | 6 | 0.000 | 12.000 | 1 → 1 | 1 → 1 | 18% → 18% | 6 → 5 | 6 | 5 → 5 | 0.003 | 0.000 |
| Jogador 2 | 2-5 | 8 | 4.000 | 2.000 | 1 → 1 | 1 → 1 | 18% → 18% | 5 → 7 | 5 | 5 → 5 | 0.011 | -0.297 |
| Jogador 2 | 2-6 | 10 | 0.000 | -4.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 7 | 14 | 5 → 5 | 0.000 | 0.264 |
| Jogador 2 | 2-7 | 10 | 2.000 | 4.000 | 1 → 1 | 2 → 3 | 18% → 21% | 7 → 5 | 10 | 5 → 6 | 0.007 | 0.000 |
| Jogador 2 | 3-1 | 10 | 4.000 | -4.000 | 1 → 1 | 3 → 2 | 21% → 21% | 5 → 8 | 8 | 6 → 6 | 0.004 | 0.277 |
| Jogador 2 | 3-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 8 → 10 | 8 | 6 → 6 | -0.004 | 0.308 |
| Jogador 2 | 3-3 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 3 | 21% → 21% | 10 → 7 | 18 | 6 → 6 | -0.081 | 0.303 |
| Jogador 2 | 3-4 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 21% → 21% | 7 → 7 | 12 | 6 → 7 | 0.093 | 0.000 |
| Jogador 2 | 3-5 | 8 | 6.000 | 8.000 | 1 → 1 | 4 → 4 | 21% → 25% | 7 → 8 | 7 | 7 → 7 | -0.012 | 0.385 |
| Jogador 2 | 3-6 | 7 | 0.000 | 10.000 | 1 → 1 | 4 → 3 | 25% → 25% | 8 → 10 | 7 | 7 → 7 | -0.009 | 0.419 |
| Jogador 2 | 3-7 | 10 | -6.000 | -4.000 | 1 → 1 | 3 → 2 | 25% → 21% | 10 → 11 | 22 | 7 → 7 | -0.004 | 0.000 |
| Jogador 2 | 4-1 | 10 | 6.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 25% | 11 → 5 | 11 | 7 → 7 | -0.002 | -0.271 |
| Jogador 2 | 4-2 | 10 | 4.000 | -2.000 | 1 → 1 | 2 → 2 | 25% → 25% | 5 → 6 | 10 | 7 → 7 | 0.009 | 0.288 |
| Jogador 2 | 4-3 | 10 | -12.000 | 6.000 | 1 → 1 | 2 → 1 | 25% → 18% | 6 → 9 | 11 | 7 → 7 | -0.016 | -0.285 |
| Jogador 2 | 4-4 | 10 | 12.000 | -2.000 | 1 → 1 | 1 → 2 | 18% → 25% | 9 → 9 | 7 | 7 → 7 | 0.012 | 0.000 |
| Jogador 2 | 4-5 | 5 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 9 → 12 | 3 | 7 → 7 | -0.204 | -0.553 |
| Jogador 2 | 4-6 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 25% → 25% | 12 → 21 | 5 | 7 → 7 | 0.014 | 0.288 |
| Jogador 2 | 4-7 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 21 → 28 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 10 | 0.000 | 12.000 | 1 → 1 | 4 → 4 | 25% → 25% | 28 → 31 | 11 | 7 → 7 | -0.001 | 0.289 |
| Jogador 2 | 5-2 | 10 | 0.000 | -10.000 | 1 → 1 | 4 → 4 | 25% → 25% | 31 → 46 | 12 | 7 → 7 | 0.000 | 0.306 |
| Jogador 2 | 5-3 | 10 | 0.000 | 4.000 | 1 → 1 | 4 → 3 | 25% → 25% | 46 → 52 | 13 | 7 → 7 | 0.060 | -0.273 |
| Jogador 2 | 5-4 | 10 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 25% → 25% | 52 → 56 | 12 | 7 → 8 | 0.005 | 0.000 |
| Jogador 2 | 5-5 | 10 | 6.000 | 6.000 | 1 → 1 | 3 → 4 | 25% → 29% | 56 → 60 | 10 | 8 → 8 | -0.000 | 0.000 |
| Jogador 2 | 5-6 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 3 | 29% → 29% | 60 → 70 | 11 | 8 → 8 | 0.017 | 0.301 |
| Jogador 2 | 5-7 | 10 | 2.000 | 8.000 | 1 → 1 | 3 → 3 | 29% → 29% | 70 → 72 | 11 | 8 → 8 | -0.063 | 0.000 |
| Jogador 2 | 6-1 | 10 | 4.000 | -14.000 | 1 → 1 | 3 → 3 | 29% → 29% | 72 → 91 | 8 | 8 → 8 | 0.002 | 0.292 |
| Jogador 2 | 6-2 | 10 | 0.000 | 8.000 | 1 → 1 | 3 → 3 | 29% → 29% | 91 → 75 | 30 | 8 → 8 | 0.000 | 0.310 |
| Jogador 2 | 6-3 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 2 | 29% → 29% | 75 → 64 | 27 | 8 → 8 | -0.006 | 0.310 |
| Jogador 2 | 6-4 | 10 | 0.000 | -10.000 | 1 → 1 | 2 → 3 | 29% → 29% | 64 → 83 | 15 | 8 → 8 | 0.006 | 0.000 |
| Jogador 2 | 6-5 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 29% → 29% | 83 → 86 | 9 | 8 → 8 | -0.001 | 0.299 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 39, COMPOSITION_COMPATIBILITY: 38, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 18; mudanças de composição: 1; posicionamento melhorou em 48 ações e piorou em 36.
- Jogador 2 — estado final: ouro 86, nível 8, vida 33.0, colocação 1.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 10 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.003 | 0.261 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 6 | 7 | 4 → 5 | 0.006 | -0.484 |
| Jogador 3 | 2-4 | 4 | 4.000 | -2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 6 → 6 | 5 | 5 → 5 | 0.026 | 0.000 |
| Jogador 3 | 2-5 | 10 | 2.000 | -8.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 10 | 7 | 5 → 5 | -0.027 | -0.237 |
| Jogador 3 | 2-6 | 8 | 2.000 | 6.000 | 1 → 2 | 2 → 1 | 18% → 18% | 10 → 11 | 5 | 5 → 5 | 0.002 | -0.310 |
| Jogador 3 | 2-7 | 8 | 0.000 | 8.000 | 2 → 2 | 1 → 3 | 18% → 18% | 11 → 13 | 6 | 5 → 5 | 0.006 | 0.000 |
| Jogador 3 | 3-1 | 10 | 0.000 | -4.000 | 2 → 1 | 3 → 2 | 18% → 18% | 13 → 23 | 4 | 5 → 5 | -0.001 | -0.268 |
| Jogador 3 | 3-2 | 5 | 4.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 23 → 29 | 3 | 5 → 6 | 0.016 | -0.517 |
| Jogador 3 | 3-3 | 10 | 8.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 21% | 29 → 8 | 27 | 6 → 6 | 0.024 | 0.276 |
| Jogador 3 | 3-4 | 8 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 21% → 21% | 8 → 6 | 10 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 3-5 | 9 | -4.000 | 8.000 | 1 → 1 | 3 → 2 | 21% → 21% | 6 → 6 | 8 | 6 → 6 | -0.010 | -0.308 |
| Jogador 3 | 3-6 | 10 | 0.000 | -14.000 | 1 → 1 | 2 → 3 | 21% → 21% | 6 → 20 | 6 | 6 → 6 | -0.004 | -0.278 |
| Jogador 3 | 3-7 | 7 | 0.000 | 12.000 | 1 → 1 | 3 → 3 | 21% → 21% | 20 → 21 | 6 | 6 → 6 | 0.010 | 0.000 |
| Jogador 3 | 4-1 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 21 → 23 | 10 | 6 → 7 | 0.015 | 0.288 |
| Jogador 3 | 4-2 | 9 | 2.000 | -2.000 | 1 → 1 | 3 → 4 | 21% → 25% | 23 → 34 | 6 | 7 → 7 | -0.000 | 0.332 |
| Jogador 3 | 4-3 | 6 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 34 → 42 | 3 | 7 → 7 | -0.004 | -0.438 |
| Jogador 3 | 4-4 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 42 → 51 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 9 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 51 → 58 | 8 | 7 → 7 | 0.006 | -0.303 |
| Jogador 3 | 4-6 | 8 | 6.000 | 2.000 | 1 → 2 | 4 → 3 | 25% → 25% | 58 → 62 | 7 | 7 → 7 | -0.007 | -0.339 |
| Jogador 3 | 4-7 | 10 | 0.000 | -6.000 | 2 → 2 | 3 → 3 | 25% → 25% | 62 → 75 | 11 | 7 → 7 | 0.010 | 0.000 |
| Jogador 3 | 5-1 | 10 | -36.000 | -46.000 | 2 → 0 | 3 → 0 | 25% → 0% | 75 → 75 | 8 | 7 → 7 | -0.082 | -0.280 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 14; mudanças de composição: 1; posicionamento melhorou em 43 ações e piorou em 37.
- Jogador 3 — estado final: ouro 75, nível 7, vida 9.0, colocação 7.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.018 | -0.346 |
| Jogador 4 | 2-2 | 4 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.034 | 0.684 |
| Jogador 4 | 2-3 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 6 → 9 | 9 | 5 → 5 | 0.005 | 0.285 |
| Jogador 4 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 10 | 12 | 5 → 5 | -0.013 | 0.000 |
| Jogador 4 | 2-5 | 10 | 6.000 | -2.000 | 0 → 0 | 3 → 2 | 18% → 21% | 10 → 5 | 14 | 5 → 6 | -0.003 | -0.232 |
| Jogador 4 | 2-6 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 5 → 8 | 3 | 6 → 6 | 0.019 | -0.369 |
| Jogador 4 | 2-7 | 10 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 9 | 10 | 6 → 6 | 0.009 | 0.000 |
| Jogador 4 | 3-1 | 10 | -4.000 | 10.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 8 | 10 | 6 → 6 | -0.007 | 0.286 |
| Jogador 4 | 3-2 | 8 | 6.000 | -4.000 | 0 → 1 | 3 → 2 | 21% → 21% | 8 → 11 | 2 | 6 → 6 | -0.007 | -0.341 |
| Jogador 4 | 3-3 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 11 → 18 | 8 | 6 → 6 | 0.031 | -0.286 |
| Jogador 4 | 3-4 | 9 | 0.000 | 16.000 | 1 → 1 | 2 → 3 | 21% → 21% | 18 → 17 | 8 | 6 → 6 | -0.088 | 0.000 |
| Jogador 4 | 3-5 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 21% → 21% | 17 → 25 | 8 | 6 → 6 | 0.057 | -0.283 |
| Jogador 4 | 3-6 | 9 | 0.000 | 0.000 | 1 → 1 | 4 → 3 | 21% → 21% | 25 → 32 | 6 | 6 → 6 | 0.053 | -0.298 |
| Jogador 4 | 3-7 | 9 | 0.000 | 0.000 | 1 → 1 | 3 → 4 | 21% → 21% | 32 → 41 | 6 | 6 → 6 | -0.041 | 0.000 |
| Jogador 4 | 4-1 | 10 | 0.000 | 6.000 | 1 → 1 | 4 → 3 | 21% → 21% | 41 → 47 | 6 | 6 → 6 | -0.005 | -0.285 |
| Jogador 4 | 4-2 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 21% → 21% | 47 → 61 | 7 | 6 → 6 | 0.022 | -0.281 |
| Jogador 4 | 4-3 | 10 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 21% → 21% | 61 → 71 | 11 | 6 → 7 | 0.004 | -0.290 |
| Jogador 4 | 4-4 | 10 | 6.000 | 8.000 | 1 → 1 | 4 → 3 | 21% → 25% | 71 → 75 | 11 | 7 → 7 | -0.010 | 0.000 |
| Jogador 4 | 4-5 | 10 | 4.000 | -4.000 | 1 → 1 | 3 → 4 | 25% → 25% | 75 → 87 | 13 | 7 → 7 | 0.007 | 0.290 |
| Jogador 4 | 4-6 | 10 | -2.000 | 2.000 | 1 → 1 | 4 → 3 | 25% → 25% | 87 → 96 | 12 | 7 → 7 | 0.002 | 0.000 |
| Jogador 4 | 4-7 | 10 | 0.000 | 4.000 | 1 → 1 | 3 → 3 | 25% → 25% | 96 → 101 | 10 | 7 → 7 | -0.010 | 0.000 |
| Jogador 4 | 5-1 | 10 | 0.000 | -8.000 | 1 → 1 | 3 → 3 | 25% → 25% | 101 → 119 | 8 | 7 → 7 | 0.006 | 0.296 |
| Jogador 4 | 5-2 | 10 | -32.000 | -40.000 | 1 → 0 | 3 → 0 | 25% → 0% | 119 → 117 | 8 | 7 → 7 | -0.082 | -0.290 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 26, COMPOSITION_COMPATIBILITY: 27, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 49 ações e piorou em 34.
- Jogador 4 — estado final: ouro 117, nível 7, vida 1.0, colocação 6.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.340 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.595 |
| Jogador 5 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 7 | 11 | 4 → 5 | -0.007 | 0.256 |
| Jogador 5 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 8 | 12 | 5 → 5 | 0.006 | 0.000 |
| Jogador 5 | 2-5 | 10 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 8 → 7 | 12 | 5 → 6 | -0.010 | 0.254 |
| Jogador 5 | 2-6 | 10 | 0.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 11 | 9 | 6 → 6 | 0.019 | -0.242 |
| Jogador 5 | 2-7 | 10 | -4.000 | 12.000 | 0 → 0 | 1 → 1 | 21% → 18% | 11 → 8 | 12 | 6 → 6 | 0.010 | 0.000 |
| Jogador 5 | 3-1 | 10 | 6.000 | 6.000 | 0 → 0 | 1 → 0 | 18% → 21% | 8 → 6 | 8 | 6 → 6 | 0.016 | 0.291 |
| Jogador 5 | 3-2 | 10 | 0.000 | -4.000 | 0 → 0 | 0 → 1 | 21% → 21% | 6 → 8 | 14 | 6 → 6 | 0.006 | 0.290 |
| Jogador 5 | 3-3 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 0 | 21% → 21% | 8 → 8 | 14 | 6 → 6 | 0.000 | -0.258 |
| Jogador 5 | 3-4 | 10 | 2.000 | 4.000 | 0 → 0 | 0 → 1 | 21% → 25% | 8 → 6 | 8 | 6 → 7 | -0.015 | 0.000 |
| Jogador 5 | 3-5 | 10 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 7 | 10 | 7 → 7 | -0.002 | -0.258 |
| Jogador 5 | 3-6 | 10 | -4.000 | 6.000 | 0 → 0 | 1 → 3 | 25% → 25% | 7 → 12 | 9 | 7 → 7 | 0.032 | 0.298 |
| Jogador 5 | 3-7 | 10 | 0.000 | 14.000 | 0 → 0 | 3 → 5 | 25% → 25% | 12 → 8 | 15 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 10 | 0.000 | -20.000 | 0 → 0 | 5 → 4 | 25% → 25% | 8 → 25 | 8 | 7 → 7 | 0.003 | 0.285 |
| Jogador 5 | 4-2 | 9 | 4.000 | 14.000 | 0 → 0 | 4 → 5 | 25% → 25% | 25 → 21 | 10 | 7 → 7 | -0.019 | -0.302 |
| Jogador 5 | 4-3 | 10 | 0.000 | -16.000 | 0 → 0 | 5 → 4 | 25% → 25% | 21 → 39 | 7 | 7 → 7 | 0.006 | 0.280 |
| Jogador 5 | 4-4 | 10 | 2.000 | 4.000 | 0 → 0 | 4 → 3 | 25% → 21% | 39 → 44 | 6 | 7 → 7 | -0.018 | 0.000 |
| Jogador 5 | 4-5 | 10 | 6.000 | 4.000 | 0 → 0 | 3 → 4 | 21% → 25% | 44 → 47 | 9 | 7 → 7 | -0.054 | -0.268 |
| Jogador 5 | 4-6 | 10 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 25% → 25% | 47 → 54 | 9 | 7 → 7 | 0.060 | 0.280 |
| Jogador 5 | 4-7 | 10 | -6.000 | -10.000 | 0 → 0 | 4 → 3 | 25% → 21% | 54 → 71 | 14 | 7 → 7 | -0.004 | 0.000 |
| Jogador 5 | 5-1 | 10 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 71 → 78 | 9 | 7 → 7 | 0.016 | 0.000 |
| Jogador 5 | 5-2 | 9 | 6.000 | 2.000 | 0 → 0 | 3 → 3 | 21% → 25% | 78 → 86 | 8 | 7 → 7 | 0.012 | 0.334 |
| Jogador 5 | 5-3 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 25% → 25% | 86 → 99 | 7 | 7 → 7 | 0.005 | 0.289 |
| Jogador 5 | 5-4 | 10 | -4.000 | -4.000 | 0 → 0 | 4 → 3 | 25% → 25% | 99 → 113 | 8 | 7 → 7 | 0.002 | 0.000 |
| Jogador 5 | 5-5 | 6 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 25% → 25% | 113 → 121 | 4 | 7 → 7 | -0.047 | 0.481 |
| Jogador 5 | 5-6 | 10 | 0.000 | -4.000 | 0 → 0 | 3 → 5 | 25% → 25% | 121 → 133 | 7 | 7 → 7 | 0.013 | -0.285 |
| Jogador 5 | 5-7 | 10 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 133 → 143 | 10 | 7 → 7 | 0.004 | 0.000 |
| Jogador 5 | 6-1 | 10 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 143 → 154 | 12 | 7 → 7 | 0.000 | -0.290 |
| Jogador 5 | 6-2 | 10 | -4.000 | 4.000 | 0 → 0 | 5 → 4 | 25% → 25% | 154 → 162 | 17 | 7 → 7 | -0.065 | -0.290 |
| Jogador 5 | 6-3 | 10 | -24.000 | -44.000 | 0 → 0 | 4 → 0 | 25% → 0% | 162 → 160 | 10 | 7 → 7 | -0.018 | -0.290 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 50, COMPOSITION_COMPATIBILITY: 33, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 17; mudanças de composição: 0; posicionamento melhorou em 45 ações e piorou em 41.
- Jogador 5 — estado final: ouro 160, nível 7, vida 1.0, colocação 3.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.018 | -0.353 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 14% → 14% | 9 → 10 | 13 | 5 → 5 | 0.006 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | -12.000 | 0 → 0 | 3 → 4 | 14% → 18% | 10 → 9 | 15 | 5 → 6 | 0.052 | -0.269 |
| Jogador 6 | 2-6 | 10 | 2.000 | 0.000 | 0 → 0 | 4 → 3 | 18% → 21% | 9 → 6 | 13 | 6 → 6 | 0.010 | 0.280 |
| Jogador 6 | 2-7 | 7 | 0.000 | 12.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 5 | 6 | 6 → 6 | 0.004 | 0.000 |
| Jogador 6 | 3-1 | 10 | 0.000 | -10.000 | 0 → 0 | 3 → 3 | 21% → 21% | 5 → 16 | 9 | 6 → 6 | 0.006 | -0.259 |
| Jogador 6 | 3-2 | 10 | 2.000 | 4.000 | 0 → 1 | 3 → 1 | 21% → 18% | 16 → 18 | 5 | 6 → 6 | 0.017 | 0.277 |
| Jogador 6 | 3-3 | 10 | 6.000 | 6.000 | 1 → 1 | 1 → 1 | 18% → 21% | 18 → 8 | 20 | 6 → 6 | -0.017 | 0.308 |
| Jogador 6 | 3-4 | 10 | 0.000 | 16.000 | 1 → 1 | 1 → 1 | 21% → 21% | 8 → 6 | 8 | 6 → 7 | 0.097 | 0.000 |
| Jogador 6 | 3-5 | 8 | 6.000 | 4.000 | 1 → 1 | 1 → 3 | 21% → 25% | 6 → 8 | 6 | 7 → 7 | -0.023 | 0.345 |
| Jogador 6 | 3-6 | 6 | 0.000 | 12.000 | 1 → 1 | 3 → 3 | 25% → 25% | 8 → 9 | 6 | 7 → 7 | 0.017 | 0.492 |
| Jogador 6 | 3-7 | 9 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 25% → 25% | 9 → 10 | 9 | 7 → 7 | 0.006 | 0.000 |
| Jogador 6 | 4-1 | 10 | 6.000 | -4.000 | 1 → 2 | 3 → 3 | 25% → 25% | 10 → 11 | 10 | 7 → 7 | -0.003 | -0.268 |
| Jogador 6 | 4-2 | 8 | 0.000 | 4.000 | 2 → 2 | 3 → 3 | 25% → 25% | 11 → 15 | 7 | 7 → 7 | -0.020 | -0.339 |
| Jogador 6 | 4-3 | 10 | 4.000 | -2.000 | 2 → 3 | 3 → 2 | 25% → 25% | 15 → 19 | 9 | 7 → 7 | -0.064 | 0.301 |
| Jogador 6 | 4-4 | 10 | 0.000 | 2.000 | 3 → 3 | 2 → 2 | 25% → 25% | 19 → 24 | 4 | 7 → 7 | 0.078 | 0.000 |
| Jogador 6 | 4-5 | 6 | 0.000 | -6.000 | 3 → 3 | 2 → 2 | 25% → 25% | 24 → 36 | 1 | 7 → 7 | -0.089 | 0.475 |
| Jogador 6 | 4-6 | 6 | 0.000 | 6.000 | 3 → 3 | 2 → 2 | 25% → 25% | 36 → 41 | 4 | 7 → 7 | -0.024 | -0.469 |
| Jogador 6 | 4-7 | 10 | 0.000 | -6.000 | 3 → 3 | 2 → 3 | 25% → 25% | 41 → 53 | 9 | 7 → 7 | 0.088 | 0.000 |
| Jogador 6 | 5-1 | 10 | 0.000 | 6.000 | 3 → 3 | 3 → 4 | 25% → 25% | 53 → 61 | 7 | 7 → 7 | 0.007 | 0.292 |
| Jogador 6 | 5-2 | 10 | 0.000 | -8.000 | 3 → 3 | 4 → 4 | 25% → 25% | 61 → 75 | 6 | 7 → 7 | 0.000 | -0.280 |
| Jogador 6 | 5-3 | 10 | 8.000 | 10.000 | 3 → 3 | 4 → 3 | 25% → 25% | 75 → 72 | 13 | 7 → 7 | -0.015 | 0.000 |
| Jogador 6 | 5-4 | 10 | 0.000 | -4.000 | 3 → 3 | 3 → 3 | 25% → 25% | 72 → 87 | 9 | 7 → 7 | 0.016 | 0.000 |
| Jogador 6 | 5-5 | 10 | 0.000 | -4.000 | 3 → 3 | 3 → 3 | 25% → 25% | 87 → 100 | 11 | 7 → 7 | 0.000 | 0.297 |
| Jogador 6 | 5-6 | 10 | 0.000 | 6.000 | 3 → 3 | 3 → 4 | 25% → 25% | 100 → 107 | 7 | 7 → 7 | -0.035 | 0.000 |
| Jogador 6 | 5-7 | 10 | 6.000 | -4.000 | 3 → 4 | 4 → 3 | 25% → 25% | 107 → 113 | 7 | 7 → 7 | -0.045 | 0.000 |
| Jogador 6 | 6-1 | 10 | 0.000 | -2.000 | 4 → 4 | 3 → 4 | 25% → 25% | 113 → 122 | 11 | 7 → 7 | 0.001 | 0.000 |
| Jogador 6 | 6-2 | 10 | -50.000 | -54.000 | 4 → 0 | 4 → 0 | 25% → 0% | 122 → 119 | 11 | 7 → 7 | -0.036 | -0.275 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 27, COMPOSITION_COMPATIBILITY: 40, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 59 ações e piorou em 55.
- Jogador 6 — estado final: ouro 119, nível 7, vida 17.0, colocação 4.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 7 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.014 | 0.366 |
| Jogador 7 | 2-2 | 8 | 4.000 | -2.000 | 0 → 0 | 3 → 2 | 14% → 14% | 8 → 8 | 8 | 4 → 4 | 0.000 | -0.303 |
| Jogador 7 | 2-3 | 7 | 2.000 | 6.000 | 0 → 1 | 2 → 2 | 14% → 14% | 8 → 9 | 5 | 4 → 5 | 0.082 | 0.391 |
| Jogador 7 | 2-4 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 14% → 14% | 9 → 8 | 13 | 5 → 5 | -0.074 | 0.000 |
| Jogador 7 | 2-5 | 7 | 6.000 | -2.000 | 1 → 1 | 2 → 1 | 14% → 18% | 8 → 9 | 8 | 5 → 5 | 0.013 | 0.352 |
| Jogador 7 | 2-6 | 10 | 0.000 | -8.000 | 1 → 1 | 1 → 3 | 18% → 18% | 9 → 8 | 16 | 5 → 6 | 0.007 | 0.256 |
| Jogador 7 | 2-7 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 2 | 18% → 18% | 8 → 7 | 13 | 6 → 6 | 0.056 | 0.000 |
| Jogador 7 | 3-1 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 5 | 12 | 6 → 6 | 0.053 | -0.268 |
| Jogador 7 | 3-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 18% → 18% | 5 → 6 | 12 | 6 → 6 | 0.000 | -0.259 |
| Jogador 7 | 3-3 | 10 | 8.000 | -4.000 | 1 → 1 | 3 → 2 | 18% → 21% | 6 → 6 | 9 | 6 → 6 | -0.083 | 0.296 |
| Jogador 7 | 3-4 | 10 | -6.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 9 | 10 | 6 → 7 | 0.094 | 0.000 |
| Jogador 7 | 3-5 | 9 | 2.000 | 14.000 | 1 → 1 | 2 → 2 | 21% → 25% | 9 → 8 | 8 | 7 → 7 | -0.036 | 0.328 |
| Jogador 7 | 3-6 | 7 | 0.000 | 16.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 5 | 8 | 7 → 7 | -0.028 | -0.395 |
| Jogador 7 | 3-7 | 8 | 0.000 | 10.000 | 1 → 1 | 2 → 4 | 25% → 25% | 5 → 5 | 6 | 7 → 7 | 0.077 | 0.000 |
| Jogador 7 | 4-1 | 8 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 5 → 10 | 3 | 7 → 7 | -0.088 | 0.376 |
| Jogador 7 | 4-2 | 9 | 0.000 | -2.000 | 1 → 1 | 4 → 5 | 25% → 25% | 10 → 19 | 4 | 7 → 7 | 0.031 | 0.320 |
| Jogador 7 | 4-3 | 9 | 0.000 | 6.000 | 1 → 1 | 5 → 4 | 25% → 25% | 19 → 22 | 8 | 7 → 7 | -0.027 | 0.343 |
| Jogador 7 | 4-4 | 9 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 22 → 32 | 3 | 7 → 7 | -0.058 | 0.000 |
| Jogador 7 | 4-5 | 7 | 0.000 | 2.000 | 1 → 1 | 4 → 5 | 25% → 25% | 32 → 40 | 3 | 7 → 7 | 0.026 | 0.000 |
| Jogador 7 | 4-6 | 10 | 8.000 | -4.000 | 1 → 1 | 5 → 5 | 25% → 25% | 40 → 45 | 7 | 7 → 7 | -0.009 | -0.263 |
| Jogador 7 | 4-7 | 10 | 2.000 | -2.000 | 1 → 1 | 5 → 4 | 25% → 25% | 45 → 52 | 5 | 7 → 7 | -0.007 | 0.000 |
| Jogador 7 | 5-1 | 8 | 0.000 | 4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 52 → 61 | 2 | 7 → 7 | 0.009 | -0.344 |
| Jogador 7 | 5-2 | 10 | 2.000 | -4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 61 → 73 | 7 | 7 → 7 | 0.020 | 0.296 |
| Jogador 7 | 5-3 | 10 | 0.000 | -4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 73 → 88 | 4 | 7 → 7 | -0.004 | 0.296 |
| Jogador 7 | 5-4 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 5 | 25% → 25% | 88 → 99 | 9 | 7 → 7 | 0.006 | 0.000 |
| Jogador 7 | 5-5 | 8 | 0.000 | 2.000 | 1 → 1 | 5 → 5 | 25% → 25% | 99 → 108 | 4 | 7 → 7 | 0.000 | -0.342 |
| Jogador 7 | 5-6 | 10 | 0.000 | -6.000 | 1 → 1 | 5 → 5 | 25% → 25% | 108 → 122 | 8 | 7 → 7 | 0.063 | -0.285 |
| Jogador 7 | 5-7 | 10 | 0.000 | -2.000 | 1 → 1 | 5 → 6 | 25% → 25% | 122 → 134 | 10 | 7 → 7 | 0.033 | 0.000 |
| Jogador 7 | 6-1 | 10 | 0.000 | 6.000 | 1 → 1 | 6 → 5 | 25% → 25% | 134 → 141 | 13 | 7 → 7 | 0.000 | 0.310 |
| Jogador 7 | 6-2 | 10 | 0.000 | -10.000 | 1 → 1 | 5 → 5 | 25% → 25% | 141 → 157 | 9 | 7 → 7 | 0.000 | 0.294 |
| Jogador 7 | 6-3 | 10 | 0.000 | 8.000 | 1 → 1 | 5 → 5 | 25% → 25% | 157 → 164 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-4 | 10 | -2.000 | 0.000 | 1 → 1 | 5 → 4 | 25% → 25% | 164 → 175 | 11 | 7 → 7 | -0.009 | 0.000 |
| Jogador 7 | 6-5 | 10 | -34.000 | -46.000 | 1 → 0 | 4 → 0 | 25% → 0% | 175 → 173 | 10 | 7 → 7 | -0.125 | -0.280 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 41, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 64 ações e piorou em 45.
- Jogador 7 — estado final: ouro 173, nível 7, vida 7.0, colocação 2.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 10 | 6.000 | 0.000 | 0 → 2 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.012 | -0.242 |
| Jogador 8 | 2-2 | 8 | 0.000 | 10.000 | 2 → 1 | 0 → 0 | 14% → 14% | 6 → 7 | 6 | 4 → 4 | -0.015 | -0.283 |
| Jogador 8 | 2-3 | 10 | 0.000 | 4.000 | 1 → 1 | 0 → 0 | 14% → 14% | 7 → 10 | 3 | 4 → 4 | -0.045 | -0.269 |
| Jogador 8 | 2-4 | 10 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 10 → 11 | 11 | 4 → 5 | 0.072 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | 12.000 | 1 → 1 | 0 → 2 | 18% → 18% | 11 → 7 | 12 | 5 → 5 | 0.003 | 0.251 |
| Jogador 8 | 2-6 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 18% → 18% | 7 → 12 | 7 | 5 → 5 | -0.003 | -0.264 |
| Jogador 8 | 2-7 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 18% → 18% | 12 → 20 | 8 | 5 → 5 | 0.012 | 0.000 |
| Jogador 8 | 3-1 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 18% → 18% | 20 → 28 | 10 | 5 → 5 | 0.001 | -0.273 |
| Jogador 8 | 3-2 | 8 | -4.000 | 12.000 | 1 → 1 | 4 → 3 | 18% → 18% | 28 → 32 | 7 | 5 → 5 | -0.098 | -0.364 |
| Jogador 8 | 3-3 | 7 | 4.000 | 2.000 | 1 → 1 | 3 → 4 | 18% → 18% | 32 → 37 | 5 | 5 → 5 | 0.078 | -0.398 |
| Jogador 8 | 3-4 | 10 | 0.000 | -10.000 | 1 → 1 | 4 → 3 | 18% → 18% | 37 → 52 | 2 | 5 → 6 | 0.013 | 0.000 |
| Jogador 8 | 3-5 | 10 | 6.000 | 10.000 | 1 → 1 | 3 → 3 | 18% → 21% | 52 → 48 | 14 | 6 → 6 | 0.031 | -0.291 |
| Jogador 8 | 3-6 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 48 → 61 | 12 | 6 → 6 | 0.006 | 0.286 |
| Jogador 8 | 3-7 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 21% | 61 → 71 | 8 | 6 → 6 | 0.008 | 0.000 |
| Jogador 8 | 4-1 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 2 | 21% → 21% | 71 → 81 | 9 | 6 → 6 | 0.000 | -0.268 |
| Jogador 8 | 4-2 | 10 | 0.000 | 12.000 | 1 → 1 | 2 → 2 | 21% → 21% | 81 → 85 | 10 | 6 → 6 | -0.062 | -0.295 |
| Jogador 8 | 4-3 | 10 | -24.000 | -50.000 | 1 → 0 | 2 → 0 | 21% → 0% | 85 → 87 | 9 | 6 → 6 | 0.021 | -0.291 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 21, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 41 ações e piorou em 33.
- Jogador 8 — estado final: ouro 87, nível 6, vida 9.0, colocação 8.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 93 | 54 | 0 | 0 | 0 | 0 | 0 | 1 | 19 | 1 | 0 | 0 |
| Jogador 2 | 105 | 69 | 1 | 4 | 5 | 0 | 0 | 0 | 27 | 5 | 1 | 0 |
| Jogador 3 | 56 | 22 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 |
| Jogador 4 | 78 | 45 | 0 | 0 | 0 | 1 | 1 | 0 | 11 | 4 | 0 | 0 |
| Jogador 5 | 110 | 77 | 4 | 8 | 9 | 1 | 1 | 1 | 23 | 3 | 2 | 0 |
| Jogador 6 | 87 | 58 | 2 | 2 | 2 | 0 | 0 | 0 | 15 | 2 | 1 | 0 |
| Jogador 7 | 100 | 62 | 1 | 1 | 1 | 0 | 0 | 0 | 21 | 6 | 1 | 0 |
| Jogador 8 | 67 | 36 | 0 | 1 | 1 | 2 | 0 | 0 | 12 | 0 | 1 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 93): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Rakan (2-7, step 118): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Elise (3-3, step 147): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Kayle (4-1, step 196): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Krug18 (5-3, step 282): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Scuttlecrab18 (5-4, step 296): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Vi18 (5-6, step 314): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Vi18 (5-6, step 316): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Shen (6-1, step 339): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_KhaZix (3-1, step 125): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 2 — venda DA_18_Rakan (4-2, step 205): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Elise (5-1, step 266): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Veigar (5-4, step 296): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_KhaZix (5-6, step 314): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_KhaZix (6-5, step 376): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (3-1, step 127): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Yorick (3-1, step 129): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Scuttlecrab18 (4-1, step 194): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Diana (4-7, step 252): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Rakan (2-5, step 98): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Rakan (2-7, step 116): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Akali_AD (4-3, step 214): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_KogMaw18_AD (4-6, step 247): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Diana (5-1, step 264): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (2-7, step 118): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Teemo (3-3, step 145): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-3, step 148): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Scuttlecrab18 (4-1, step 196): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_18_Cassiopeia (4-3, step 219): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_KogMaw18_AD (4-7, step 255): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-6, step 107): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Xayah (5-4, step 292): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_CrimsonRaptor18 (5-4, step 296): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_MasterYi_AD (5-4, step 298): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Diana (6-2, step 343): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Camille (2-5, step 95): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 7 — venda DA_18_Rakan (2-7, step 118): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rakan (4-7, step 252): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_Hecarim (5-2, step 272): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_Krug18 (2-7, step 115): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Karma18 (3-4, step 157): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_KhaZix (3-6, step 177): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_18_Rakan (4-3, step 212): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Tristana (4-3, step 218): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **5**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 2-5 | 93 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 2-7 | 118 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 3-3 | 147 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-1 | 196 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kayle' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 5-3 | 282 | SOLD_CORE_UNIT | Venda de 'DA_Krug18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 5-4 | 296 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 5-6 | 314 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 5-6 | 316 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 6-1 | 339 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 68 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 69 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 229 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 230 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 339 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 516 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 696 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-5 | 832 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 919 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 920 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1062 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1193 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1194 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1329 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1330 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1460 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-3 | 1461 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1594 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1835 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 1947 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 2085 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2359 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2496 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 2497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2637 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2638 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2762 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-6 | 2763 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 2876 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-7 | 2877 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-1 | 3015 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-1 | 3016 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 3158 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-2 | 3159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 3301 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-3 | 3302 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-4 | 3447 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-4 | 3448 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-5 | 3592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-5 | 3593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-6 | 3736 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-6 | 3737 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-7 | 3876 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-7 | 3877 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-1 | 4019 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-1 | 4020 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 4-2 | 2336 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-3 | 2473 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-5 | 2739 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2853 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-3 | 3424 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 95 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-5 | 97 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-6 | 110 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-7 | 115 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-2 | 135 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 2 | 3-2 | 136 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yorick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 2 | 4-2 | 205 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-1 | 266 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-4 | 296 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Veigar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-6 | 314 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-5 | 376 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 353 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 354 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 355 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 356 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 357 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 358 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 359 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 360 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 361 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 362 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 363 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 364 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 365 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 366 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 367 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 368 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 369 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 370 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-4 | 371 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 372 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 373 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 374 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 375 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 376 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 377 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 378 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 379 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 380 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-5 | 381 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-1 | 1307 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-2 | 1440 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-3 | 1574 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-3 | 1575 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-4 | 1714 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-4 | 1715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1830 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-5 | 1831 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1927 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-6 | 1928 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 2061 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 2193 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 2332 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2470 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2616 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2694 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 2695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2833 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-6 | 2834 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 2974 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 2975 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 3114 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-1 | 3115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 3249 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-2 | 3250 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 3389 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 3528 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 3666 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-6 | 3803 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-7 | 3936 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-7 | 3937 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-1 | 4080 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-1 | 4081 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-2 | 4214 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-2 | 4215 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-3 | 4348 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-3 | 4349 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-4 | 4485 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-4 | 4486 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-5 | 4624 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-5 | 4625 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| MEDIUM | Jogador 2 | 5-4 | 3643 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-5 | 3779 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-6 | 3913 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 3 | 3-1 | 127 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 3-1 | 129 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-5 | 804 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-6 | 914 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-7 | 1022 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-1 | 1155 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-2 | 1228 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1229 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-3 | 1357 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-3 | 1358 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 2864 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-1 | 2865 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 3-1 | 1205 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-5 | 1711 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-6 | 1812 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-7 | 1954 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-1 | 2082 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-2 | 2171 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-4 | 2442 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-3 | 214 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 4-6 | 247 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 5-1 | 264 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-1 | 1225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-2 | 1342 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-3 | 1481 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 1604 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1605 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 1737 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2530 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2666 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-5 | 2667 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 2806 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 2807 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 2944 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-7 | 2945 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-1 | 3082 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-1 | 3083 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-2 | 3220 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-2 | 3221 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 3-3 | 1581 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-5 | 1838 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-6 | 1958 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-7 | 2094 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 109 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 5 | 2-7 | 118 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 2-7 | 120 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 138 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-3 | 145 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-3 | 148 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-3 | 150 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Yunara) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-4 | 156 | PURCHASE_SALE_REVIEW | Compra de DA_Karma18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 3-5 | 166 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Alistar) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 176 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 4-1 | 200 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Soraka) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 4-3 | 218 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rammus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 4-3 | 219 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 4-7 | 255 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-7 | 260 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Nidalee18_AP) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 2-1 | 58 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 59 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 293 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 294 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 295 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 296 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 297 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 298 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 299 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 300 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 301 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 302 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 303 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 304 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 305 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 306 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 311 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 312 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 313 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 314 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 315 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 343 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 344 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 345 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 346 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 347 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 348 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 349 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 350 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 351 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 352 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 353 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 354 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 355 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 356 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 357 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 358 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 359 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 360 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-3 | 361 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 822 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 956 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1760 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 2568 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2707 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 2845 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-7 | 2985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 3125 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 3255 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 3256 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 3397 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-3 | 3398 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3540 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-4 | 3541 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3633 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-5 | 3634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3778 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-6 | 3779 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 3923 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-7 | 3924 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 4063 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-1 | 4064 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-2 | 4201 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-2 | 4202 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-3 | 4344 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-3 | 4345 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 4-1 | 2264 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 3232 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-2 | 3374 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-4 | 3610 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-3 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 3-1 | 127 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ahri) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 3-1 | 130 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Alistar) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 5-4 | 292 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-4 | 296 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 5-4 | 298 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 6-2 | 343 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 68 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 3-4 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 4-7 | 260 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 5-2 | 275 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 276 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 277 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 278 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 279 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 280 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 281 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 282 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 2-7 | 1045 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1181 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1450 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1451 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1587 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1588 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1700 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1701 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 1784 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1785 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1907 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 2045 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 2046 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2155 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2295 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2296 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2434 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2523 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2524 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 2613 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2614 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 2750 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 2889 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 2890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 3032 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-2 | 3033 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 3174 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-3 | 3175 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-4 | 3318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-4 | 3319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-5 | 3454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-5 | 3455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-6 | 3592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-6 | 3593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-7 | 3734 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-7 | 3735 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-1 | 3871 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 6-1 | 3872 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-2 | 4012 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-2 | 4013 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 4-7 | 2866 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 7 | 2-4 | 89 | PURCHASE_SALE_REVIEW | Compra de DA_Scuttlecrab18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 7 | 2-7 | 118 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-2 | 136 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 7 | 2-4 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 7 | 3-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 441 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 553 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 554 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-3 | 653 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-4 | 790 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-4 | 791 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-5 | 887 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-5 | 888 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 1023 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 1024 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1294 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1427 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1569 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-3 | 1570 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1704 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2153 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 2278 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 2279 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-3 | 2408 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2534 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-4 | 2535 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2633 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2772 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-6 | 2773 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2918 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2919 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 3031 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 3032 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 3170 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 3171 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 3309 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-3 | 3310 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 3451 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-4 | 3452 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 3568 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 3569 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 3707 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 3844 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 3983 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-2 | 4125 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-3 | 4262 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-4 | 4402 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 4542 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-5 | 4543 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 4-1 | 2255 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-2 | 2384 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-3 | 2511 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-4 | 2610 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-6 | 2895 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-7 | 3008 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-1 | 3147 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-2 | 3286 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-4 | 3545 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-4 | 46 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Tristana) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 8 | 2-7 | 115 | SOLD_CORE_UNIT | Venda de 'DA_Krug18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-4 | 157 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Karma18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-3 | 218 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 457 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 564 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 703 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 837 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 974 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 1112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1251 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1388 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1594 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1729 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1865 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 2000 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 2135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 2136 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2274 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2275 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2416 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2417 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 4-3 | 2560 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 3-1 | 1474 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-2 | 1571 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-3 | 1706 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
