# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4315**
- Achados: **174**
- CRITICAL: 0 | HIGH: 18 | MEDIUM: 91 | LOW: 65

## Metadados da sessão

- Match ID: 64b82cbe-01a8-46a5-bac7-7bdd4ef13fa3
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 7ca55b815020c2c4d963f621d072c062eb05bd1c4aa917bb80e798386967e73f
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **3532**
- Entradas posteriores à eliminação ignoradas: **783**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 0 | 8 | 23 | 1 | 30 | 0 | 0 | não/inconclusivo | 1 |
| Jogador 6 | 1 | 8 | 29 | 9 | 32 | 4 | 0 | não/inconclusivo | 1 |
| Jogador 7 | 0 | 7 | 15 | 9 | 27 | 0 | 4 | sim | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 122 | 35 | 12 | 14 | 1 | 24 | 35 | 0.0608 | 9 | 5 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::PASS: 1, FAST8::BUY: 12, FAST8::BUY_XP: 9, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 16, FAST8::PASS: 11, FAST8::SELL: 5, SLOWROLL::BUY: 4, SLOWROLL::BUY_XP: 4, SLOWROLL::MOVE_BENCH: 4, SLOWROLL::PASS: 2, SLOWROLL::SELL: 3, STABILIZE::BUY: 17, STABILIZE::BUY_XP: 1, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 2, STABILIZE::PASS: 10, STABILIZE::REROLL: 1, STABILIZE::SELL: 4
- Jogador 1 — recompensas por ação: BUY: média 0.3349 (n=35), BUY_XP: média -0.0307 (n=14), ITEM: média 0.1500 (n=1), MOVE_BENCH: média 0.0442 (n=33), MOVE_BOARD: média -0.0750 (n=2), PASS: média -0.0021 (n=24), REROLL: média -0.0900 (n=1), SELL: média -0.4325 (n=12)
| Jogador 2 | 224 | 67 | 40 | 26 | 19 | 34 | 34 | 0.0382 | 19 | 22 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::REROLL: 3, ALL_IN::SELL: 2, ECON::BUY: 15, ECON::MOVE_BENCH: 6, ECON::PASS: 4, ECON::REROLL: 5, ECON::SELL: 8, FAST8::BUY: 12, FAST8::BUY_XP: 17, FAST8::MOVE_BENCH: 8, FAST8::PASS: 11, FAST8::SELL: 10, SLOWROLL::BUY: 1, SLOWROLL::BUY_XP: 1, SLOWROLL::MOVE_BENCH: 1, SLOWROLL::PASS: 1, STABILIZE::BUY: 24, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 12, STABILIZE::REROLL: 11, STABILIZE::SELL: 17, WINSTREAK::BUY: 11, WINSTREAK::BUY_XP: 4, WINSTREAK::ITEM: 2, WINSTREAK::PASS: 6, WINSTREAK::SELL: 3
- Jogador 2 — recompensas por ação: BUY: média 0.3248 (n=67), BUY_XP: média -0.0192 (n=26), ITEM: média 0.0500 (n=4), MOVE_BENCH: média -0.0133 (n=33), MOVE_BOARD: média 0.0700 (n=1), PASS: média -0.0024 (n=34), REROLL: média -0.1168 (n=19), SELL: média -0.2560 (n=40)
| Jogador 3 | 135 | 36 | 14 | 21 | 1 | 26 | 35 | 0.0490 | 17 | 13 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::ITEM: 2, ALL_IN::PASS: 2, ALL_IN::REROLL: 1, FAST8::BUY: 17, FAST8::BUY_XP: 14, FAST8::MOVE_BENCH: 15, FAST8::PASS: 12, FAST8::SELL: 10, SLOWROLL::BUY: 4, SLOWROLL::BUY_XP: 4, SLOWROLL::MOVE_BENCH: 7, SLOWROLL::PASS: 3, SLOWROLL::SELL: 1, STABILIZE::BUY: 11, STABILIZE::BUY_XP: 3, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 9, STABILIZE::SELL: 3
- Jogador 3 — recompensas por ação: BUY: média 0.3378 (n=36), BUY_XP: média -0.0252 (n=21), ITEM: média 0.0600 (n=2), MOVE_BENCH: média 0.0244 (n=34), MOVE_BOARD: média -0.1400 (n=1), PASS: média -0.0039 (n=26), REROLL: média -0.0900 (n=1), SELL: média -0.4021 (n=14)
| Jogador 4 | 135 | 30 | 10 | 23 | 5 | 31 | 34 | 0.0442 | 9 | 7 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::PASS: 4, ALL_IN::REROLL: 5, ALL_IN::SELL: 2, ECON::BUY: 5, ECON::BUY_XP: 2, ECON::ITEM: 1, ECON::MOVE_BENCH: 6, ECON::PASS: 4, FAST8::BUY: 7, FAST8::BUY_XP: 15, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 9, FAST8::MOVE_BOARD: 1, FAST8::PASS: 14, FAST8::SELL: 3, SLOWROLL::BUY: 2, SLOWROLL::BUY_XP: 1, SLOWROLL::MOVE_BENCH: 5, SLOWROLL::PASS: 2, SLOWROLL::SELL: 1, STABILIZE::BUY: 9, STABILIZE::BUY_XP: 5, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 2, STABILIZE::PASS: 7, STABILIZE::SELL: 4
- Jogador 4 — recompensas por ação: BUY: média 0.3297 (n=30), BUY_XP: média -0.0113 (n=23), ITEM: média 0.0200 (n=2), MOVE_BENCH: média 0.0061 (n=31), MOVE_BOARD: média -0.1200 (n=3), PASS: média -0.0065 (n=31), REROLL: média -0.0900 (n=5), SELL: média -0.2880 (n=10)
| Jogador 5 | 208 | 56 | 29 | 26 | 7 | 36 | 50 | 0.0284 | 15 | 6 |
- Jogador 5 — ações por estratégia: ECON::BUY: 3, ECON::BUY_XP: 2, ECON::MOVE_BENCH: 11, ECON::PASS: 3, ECON::SELL: 1, FAST8::BUY: 14, FAST8::BUY_XP: 17, FAST8::MOVE_BENCH: 11, FAST8::PASS: 13, FAST8::SELL: 10, STABILIZE::BUY: 18, STABILIZE::BUY_XP: 4, STABILIZE::MOVE_BENCH: 25, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 11, STABILIZE::REROLL: 2, STABILIZE::SELL: 8, WINSTREAK::BUY: 21, WINSTREAK::BUY_XP: 3, WINSTREAK::ITEM: 4, WINSTREAK::MOVE_BENCH: 2, WINSTREAK::PASS: 9, WINSTREAK::REROLL: 5, WINSTREAK::SELL: 10
- Jogador 5 — recompensas por ação: BUY: média 0.3527 (n=56), BUY_XP: média -0.0211 (n=26), ITEM: média 0.0525 (n=4), MOVE_BENCH: média -0.0737 (n=49), MOVE_BOARD: média -0.2100 (n=1), PASS: média -0.0150 (n=36), REROLL: média -0.1743 (n=7), SELL: média -0.2735 (n=29)
| Jogador 6 | 158 | 32 | 12 | 29 | 7 | 27 | 49 | -0.0204 | 20 | 4 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::BUY_XP: 2, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 2, ALL_IN::PASS: 6, ALL_IN::REROLL: 7, ALL_IN::SELL: 1, FAST8::BUY: 4, FAST8::BUY_XP: 10, FAST8::MOVE_BENCH: 10, FAST8::PASS: 4, FAST8::SELL: 1, SLOWROLL::BUY: 4, SLOWROLL::MOVE_BENCH: 14, SLOWROLL::PASS: 6, SLOWROLL::SELL: 3, STABILIZE::BUY: 15, STABILIZE::BUY_XP: 17, STABILIZE::MOVE_BENCH: 22, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 11, STABILIZE::SELL: 7
- Jogador 6 — recompensas por ação: BUY: média 0.3219 (n=32), BUY_XP: média 0.0314 (n=29), ITEM: média 0.0750 (n=2), MOVE_BENCH: média -0.1727 (n=48), MOVE_BOARD: média -0.3100 (n=1), PASS: média -0.0663 (n=27), REROLL: média -0.0900 (n=7), SELL: média -0.2967 (n=12)
| Jogador 7 | 118 | 27 | 10 | 15 | 5 | 23 | 38 | 0.0046 | 12 | 3 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::PASS: 3, ALL_IN::REROLL: 5, ALL_IN::SELL: 1, FAST8::BUY: 6, FAST8::BUY_XP: 7, FAST8::MOVE_BENCH: 6, FAST8::PASS: 5, FAST8::SELL: 3, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 7, SLOWROLL::MOVE_BENCH: 10, SLOWROLL::PASS: 3, SLOWROLL::SELL: 1, STABILIZE::BUY: 13, STABILIZE::BUY_XP: 1, STABILIZE::MOVE_BENCH: 21, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 12, STABILIZE::SELL: 5
- Jogador 7 — recompensas por ação: BUY: média 0.3744 (n=27), BUY_XP: média -0.0527 (n=15), MOVE_BENCH: média -0.0830 (n=37), MOVE_BOARD: média -0.1400 (n=1), PASS: média -0.0091 (n=23), REROLL: média -0.0900 (n=5), SELL: média -0.4910 (n=10)
| Jogador 8 | 130 | 30 | 9 | 22 | 8 | 28 | 31 | 0.0333 | 4 | 5 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 1, ALL_IN::PASS: 4, ALL_IN::REROLL: 6, ALL_IN::SELL: 1, FAST8::BUY: 4, FAST8::BUY_XP: 8, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 4, FAST8::PASS: 9, FAST8::SELL: 2, SLOWROLL::BUY: 6, SLOWROLL::BUY_XP: 8, SLOWROLL::MOVE_BENCH: 7, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::PASS: 7, SLOWROLL::SELL: 4, STABILIZE::BUY: 14, STABILIZE::BUY_XP: 6, STABILIZE::MOVE_BENCH: 17, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 8, STABILIZE::REROLL: 2, STABILIZE::SELL: 2
- Jogador 8 — recompensas por ação: BUY: média 0.3853 (n=30), BUY_XP: média -0.0423 (n=22), ITEM: média 0.0850 (n=2), MOVE_BENCH: média -0.0621 (n=29), MOVE_BOARD: média 0.0100 (n=2), PASS: média -0.0150 (n=28), REROLL: média -0.0900 (n=8), SELL: média -0.3944 (n=9)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 19:38:48 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | 0.0000 |  |
| Jogador 1 | ? | 19:38:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 1 | ? | 19:38:49 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6000 |  |
| Jogador 1 | ? | 19:38:49 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0700 |  |
| Jogador 1 | ? | 19:38:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-1 | 19:38:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 1 | 1-1 | 19:38:55 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-1 | 19:38:55 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1700 |  |
| Jogador 1 | 1-1 | 19:38:56 | MOVE Bench -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3100 |  |
| Jogador 1 | 1-1 | 19:38:56 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6200 |  |
| Jogador 1 | 1-1 | 19:38:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-2 | 19:39:01 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1700 |  |
| Jogador 1 | 1-2 | 19:39:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-3 | 19:39:07 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | -0.4000 |  |
| Jogador 1 | 1-3 | 19:39:07 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 1 | 1-3 | 19:39:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 1 | 1-3 | 19:39:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-3 | 19:39:12 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 1 | 1-4 | 19:39:14 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 1.1200 |  |
| Jogador 1 | 1-4 | 19:39:14 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.4100 |  |
| Jogador 1 | 1-4 | 19:39:14 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.2200 |  |
| Jogador 1 | 1-4 | 19:39:15 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1500 |  |
| Jogador 1 | 1-4 | 19:39:15 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.5400 |  |
| Jogador 1 | 1-4 | 19:39:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-1 | 19:39:20 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 1 | 2-1 | 19:39:21 | MOVE Bench -> Board: Diana (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 1 | 2-1 | 19:39:21 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.2800 |  |
| Jogador 1 | 2-1 | 19:39:22 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.4700 |  |
| Jogador 1 | 2-1 | 19:39:22 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0200 |  |
| Jogador 1 | 2-1 | 19:39:22 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.4400 |  |
| Jogador 1 | 2-1 | 19:39:22 | MOVE Bench -> Board: Diana (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.2500 |  |
| Jogador 1 | 2-1 | 19:39:23 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-2 | 19:39:27 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Rakan | -0.7200 |  |
| Jogador 1 | 2-2 | 19:39:27 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 1 | 2-2 | 19:39:28 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | -0.4000 |  |
| Jogador 1 | 2-2 | 19:39:29 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | -0.8800 |  |
| Jogador 1 | 2-2 | 19:39:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-3 | 19:39:34 | VENDEU: Rakan (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 0 | — | DA_18_Diana | -0.5000 |  |
| Jogador 1 | 2-3 | 19:39:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 0 | — | DA_18_Diana | 0.2900 |  |
| Jogador 1 | 2-3 | 19:39:34 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 0 | — | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 1 | 2-3 | 19:39:35 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | — | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 2-3 | 19:39:35 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | — | DA_18_Diana | -0.3100 |  |
| Jogador 1 | 2-3 | 19:39:36 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Diana | -0.1600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-3 | 19:39:36 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Diana | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-3 | 19:39:36 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Diana | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-3 | 19:39:36 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 19:39:41 | VENDEU: Kog'Maw (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Colosso | DA_18_Diana | -0.4500 |  |
| Jogador 1 | 2-4 | 19:39:41 | COMPROU: Vi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_18_Diana | 0.3200 |  |
| Jogador 1 | 2-4 | 19:39:41 | MOVE Bench -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_18_Diana | 0.0700 |  |
| Jogador 1 | 2-4 | 19:39:42 | VENDEU: Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Colosso | DA_18_Diana | -0.4600 |  |
| Jogador 1 | 2-4 | 19:39:42 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_18_Diana | 0.2500 |  |
| Jogador 1 | 2-4 | 19:39:42 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_18_Diana | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-4 | 19:39:42 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-5 | 19:39:48 | MOVE Bench -> Board: Shen (i:4.0) <-> Vi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Colosso | DA_18_Diana | -0.3500 |  |
| Jogador 1 | 2-5 | 19:39:48 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Diana | 0.5600 |  |
| Jogador 1 | 2-5 | 19:39:48 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | 0.2400 |  |
| Jogador 1 | 2-5 | 19:39:48 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Diana | -0.7300 |  |
| Jogador 1 | 2-5 | 19:39:49 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Diana | 0.9700 |  |
| Jogador 1 | 2-5 | 19:39:50 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-5 | 19:39:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-6 | 19:39:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-6 | 19:39:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-6 | 19:39:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-7 | 19:40:02 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Diana | -0.8500 |  |
| Jogador 1 | 2-7 | 19:40:02 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Diana | -0.1400 |  |
| Jogador 1 | 2-7 | 19:40:02 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Diana | -0.7300 |  |
| Jogador 1 | 2-7 | 19:40:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-7 | 19:40:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 3-1 | 19:40:09 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Diana | -0.4200 |  |
| Jogador 1 | 3-1 | 19:40:09 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Ezreal | -0.2800 |  |
| Jogador 1 | 3-1 | 19:40:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-1 | 19:40:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-2 | 19:40:16 | VENDEU: Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Diana | -0.2800 |  |
| Jogador 1 | 3-2 | 19:40:16 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Diana | 0.6500 |  |
| Jogador 1 | 3-2 | 19:40:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 3-2 | 19:40:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 3-3 | 19:40:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | 0.1000 |  |
| Jogador 1 | 3-3 | 19:40:24 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Diana | 0.5500 |  |
| Jogador 1 | 3-3 | 19:40:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | -0.1600 |  |
| Jogador 1 | 3-3 | 19:40:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 3-4 | 19:40:31 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Diana | 0.0900 |  |
| Jogador 1 | 3-4 | 19:40:31 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_Vi18 | 0.6800 |  |
| Jogador 1 | 3-4 | 19:40:32 | MOVE Bench -> Board: Vi (i:12.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Vi18 | 0.1500 |  |
| Jogador 1 | 3-4 | 19:40:33 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Vi18 | 0.3200 |  |
| Jogador 1 | 3-4 | 19:40:33 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Vi18 | 0.1900 |  |
| Jogador 1 | 3-4 | 19:40:33 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Vi18 | 0.4400 |  |
| Jogador 1 | 3-4 | 19:40:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 3-4 | 19:40:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 3-5 | 19:40:38 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | 0.7700 |  |
| Jogador 1 | 3-5 | 19:40:38 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | -0.3600 |  |
| Jogador 1 | 3-5 | 19:40:39 | MOVE Bench -> Board: Vi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | 0.4900 |  |
| Jogador 1 | 3-5 | 19:40:39 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.5100 |  |
| Jogador 1 | 3-5 | 19:40:40 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.4300 |  |
| Jogador 1 | 3-5 | 19:40:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 3-6 | 19:40:46 | COMPROU: Lux (Feérica) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | -0.0500 |  |
| Jogador 1 | 3-6 | 19:40:46 | MOVE Bench -> Board: Lux (Feérica) (i:10.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | -0.5300 |  |
| Jogador 1 | 3-6 | 19:40:47 | MOVE Bench -> Board: Vi (i:12.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | 0.1500 |  |
| Jogador 1 | 3-6 | 19:40:47 | MOVE Bench -> Board: Shen (i:4.0) <-> Lux (Feérica) (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | 0.2100 |  |
| Jogador 1 | 3-6 | 19:40:47 | MOVE Bench -> Board: Lux (Feérica) (i:10.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | -0.2100 |  |
| Jogador 1 | 3-6 | 19:40:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 3-7 | 19:40:55 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Vi18 | 0.2100 |  |
| Jogador 1 | 3-7 | 19:40:55 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NeedlesslyLargeRod -> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Vi18 | 0.1500 |  |
| Jogador 1 | 3-7 | 19:40:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 3-7 | 19:40:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-1 | 19:41:03 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | 0.7400 |  |
| Jogador 1 | 4-1 | 19:41:04 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | -0.3100 |  |
| Jogador 1 | 4-1 | 19:41:04 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | 0.2100 |  |
| Jogador 1 | 4-1 | 19:41:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-1 | 19:41:08 | MOVE Bench -> Board: Vi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Vi18 | 0.6700 |  |
| Jogador 1 | 4-2 | 19:41:11 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.3000 |  |
| Jogador 1 | 4-2 | 19:41:13 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 4-3 | 19:41:19 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 1 | 4-3 | 19:41:19 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.0400 |  |
| Jogador 1 | 4-3 | 19:41:19 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 4-4 | 19:41:29 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_MasterYi_AD | -0.2200 |  |
| Jogador 1 | 4-4 | 19:41:29 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_MasterYi_AD | -0.1400 |  |
| Jogador 1 | 4-4 | 19:41:29 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 19:41:30 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 1 | 4-4 | 19:41:30 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 4-5 | 19:41:37 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.2300 |  |
| Jogador 1 | 4-5 | 19:41:37 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.2700 |  |
| Jogador 1 | 4-5 | 19:41:38 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 2 | ? | 19:38:48 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0200 |  |
| Jogador 2 | ? | 19:38:48 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.3100 |  |
| Jogador 2 | ? | 19:38:49 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5800 |  |
| Jogador 2 | ? | 19:38:49 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0700 |  |
| Jogador 2 | ? | 19:38:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-1 | 19:38:54 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 2 | 1-1 | 19:38:55 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-1 | 19:38:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-2 | 19:39:01 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1300 |  |
| Jogador 2 | 1-2 | 19:39:01 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | 0.5800 |  |
| Jogador 2 | 1-2 | 19:39:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 1-3 | 19:39:07 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Sejuani | 0.2700 |  |
| Jogador 2 | 1-3 | 19:39:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 1-4 | 19:39:14 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yunara | 0.3000 |  |
| Jogador 2 | 1-4 | 19:39:14 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | 0.3300 |  |
| Jogador 2 | 1-4 | 19:39:14 | MOVE Bench -> Board: Vi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | -0.3600 |  |
| Jogador 2 | 1-4 | 19:39:15 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | -0.3200 |  |
| Jogador 2 | 1-4 | 19:39:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-1 | 19:39:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 2 | 2-1 | 19:39:21 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-1 | 19:39:21 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | 0.6300 |  |
| Jogador 2 | 2-1 | 19:39:22 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-2 | 19:39:27 | COMPROU: Master Yi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_Vi18 | 0.2100 |  |
| Jogador 2 | 2-2 | 19:39:27 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 2 | 2-2 | 19:39:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 2 | 2-2 | 19:39:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 2-3 | 19:39:34 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_MasterYi_AD | -0.5100 |  |
| Jogador 2 | 2-3 | 19:39:34 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Fiddlesticks18 | 0.3300 |  |
| Jogador 2 | 2-3 | 19:39:34 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Fiddlesticks18 | -0.2500 |  |
| Jogador 2 | 2-3 | 19:39:35 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 2 | 2-3 | 19:39:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 2-4 | 19:39:41 | MOVE Bench -> Board: Vi (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_Fiddlesticks18 | -0.8600 |  |
| Jogador 2 | 2-4 | 19:39:41 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_Fiddlesticks18 | -0.1400 |  |
| Jogador 2 | 2-4 | 19:39:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_Fiddlesticks18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 2-5 | 19:39:48 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Florescer | DA_Fiddlesticks18 | -0.3900 |  |
| Jogador 2 | 2-5 | 19:39:48 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Florescer | DA_Fiddlesticks18 | 0.2100 |  |
| Jogador 2 | 2-5 | 19:39:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Florescer | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 2 | 2-5 | 19:39:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Florescer | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 2 | 2-5 | 19:39:49 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Florescer | DA_Fiddlesticks18 | 0.3500 |  |
| Jogador 2 | 2-5 | 19:39:50 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Florescer | DA_Fiddlesticks18 | 0.3300 |  |
| Jogador 2 | 2-5 | 19:39:50 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 1 | Florescer | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 2 | 2-5 | 19:39:51 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Florescer | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 2 | 2-5 | 19:39:51 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 2-6 | 19:39:55 | VENDEU: Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Florescer | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 2 | 2-6 | 19:39:55 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Lillia | 0.0600 |  |
| Jogador 2 | 2-6 | 19:39:55 | MOVE Bench -> Board: Lillia (i:8.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Lillia | -0.2400 |  |
| Jogador 2 | 2-6 | 19:39:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 2-7 | 19:40:02 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Florescer | DA_18_Lillia | -0.3400 |  |
| Jogador 2 | 2-7 | 19:40:02 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Florescer | DA_18_Lillia | 0.6500 |  |
| Jogador 2 | 2-7 | 19:40:02 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Florescer | DA_18_Lillia | 0.0900 |  |
| Jogador 2 | 2-7 | 19:40:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 2-7 | 19:40:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 2-7 | 19:40:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-1 | 19:40:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-1 | 19:40:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-2 | 19:40:16 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-2 | 19:40:16 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Florescer | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 3-2 | 19:40:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-2 | 19:40:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Lillia | 0.0800 |  |
| Jogador 2 | 3-2 | 19:40:17 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Lillia | 0.4600 |  |
| Jogador 2 | 3-2 | 19:40:18 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-3 | 19:40:24 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_Fiddlesticks18 | 0.7300 |  |
| Jogador 2 | 3-3 | 19:40:24 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Lillia | -1.1100 |  |
| Jogador 2 | 3-3 | 19:40:24 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_Fiddlesticks18 | 0.7300 |  |
| Jogador 2 | 3-3 | 19:40:25 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 2 | 3-3 | 19:40:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-3 | 19:40:26 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_Fiddlesticks18 | -0.4500 |  |
| Jogador 2 | 3-3 | 19:40:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-4 | 19:40:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-4 | 19:40:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-5 | 19:40:38 | VENDEU: Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_Fiddlesticks18 | -0.5100 |  |
| Jogador 2 | 3-5 | 19:40:38 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Florescer | DA_Fiddlesticks18 | 0.6400 |  |
| Jogador 2 | 3-5 | 19:40:39 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_Fiddlesticks18 | -1.0100 |  |
| Jogador 2 | 3-5 | 19:40:39 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Florescer | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 2 | 3-5 | 19:40:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-5 | 19:40:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-6 | 19:40:46 | VENDEU: Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Florescer | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 2 | 3-6 | 19:40:46 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_Lillia | 0.7200 |  |
| Jogador 2 | 3-6 | 19:40:47 | MOVE Bench -> Board: Lillia (i:8.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_Lillia | -0.4000 |  |
| Jogador 2 | 3-6 | 19:40:47 | MOVE Bench -> Board: Lillia (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_Lillia | -0.4000 |  |
| Jogador 2 | 3-6 | 19:40:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-7 | 19:40:55 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Florescer | DA_18_Lillia | -0.7500 |  |
| Jogador 2 | 3-7 | 19:40:55 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Florescer | DA_18_Lillia | -0.0700 |  |
| Jogador 2 | 3-7 | 19:40:55 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Florescer | DA_18_Lillia | -0.2300 |  |
| Jogador 2 | 3-7 | 19:40:56 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Florescer | DA_18_Lillia | -0.3400 |  |
| Jogador 2 | 3-7 | 19:40:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-7 | 19:40:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-7 | 19:40:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 1 | Florescer | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 3-7 | 19:40:57 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 1 | Florescer | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-7 | 19:40:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 1 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-1 | 19:41:03 | VENDEU: Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Florescer | DA_18_Lillia | -0.3500 |  |
| Jogador 2 | 4-1 | 19:41:04 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Florescer | DA_18_Lillia | 0.2500 |  |
| Jogador 2 | 4-1 | 19:41:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-1 | 19:41:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Florescer | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 4-1 | 19:41:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Florescer | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-1 | 19:41:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-2 | 19:41:11 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Florescer | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 4-2 | 19:41:13 | VENDEU: Karma (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Florescer | DA_18_Lillia | -0.5000 |  |
| Jogador 2 | 4-2 | 19:41:13 | COMPROU: Tristana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Florescer | DA_18_Lillia | 0.2300 |  |
| Jogador 2 | 4-2 | 19:41:13 | VENDEU: Tristana (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Florescer | DA_18_Lillia | -0.7000 |  |
| Jogador 2 | 4-2 | 19:41:13 | COMPROU: Grompe (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Florescer | DA_18_Lillia | 0.0300 |  |
| Jogador 2 | 4-2 | 19:41:14 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Florescer | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 4-2 | 19:41:14 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Florescer | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-3 | 19:41:19 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Adaptador | DA_18_Lillia | -0.0400 |  |
| Jogador 2 | 4-3 | 19:41:19 | VENDEU: Mamãe Bicuda (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Adaptador | DA_18_Lillia | -0.2300 |  |
| Jogador 2 | 4-3 | 19:41:19 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Adaptador | DA_18_Lillia | -0.1400 |  |
| Jogador 2 | 4-3 | 19:41:20 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Adaptador | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-4 | 19:41:29 | COMPROU: Ahri (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Adaptador | DA_18_Lillia | 0.2900 |  |
| Jogador 2 | 4-4 | 19:41:29 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Adaptador | DA_18_Lillia | -0.0600 |  |
| Jogador 2 | 4-4 | 19:41:29 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Adaptador | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-4 | 19:41:30 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Adaptador | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-4 | 19:41:30 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Adaptador | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-5 | 19:41:37 | COMPROU: Karma (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Adaptador | DA_18_Lillia | 0.1700 |  |
| Jogador 2 | 4-5 | 19:41:37 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Adaptador | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-6 | 19:41:45 | COMPROU: Grompe (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 15 | 0 | Adaptador | DA_18_Lillia | 0.8100 |  |
| Jogador 2 | 4-6 | 19:41:45 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 15 | 0 | Adaptador | DA_18_Lillia | -0.0800 |  |
| Jogador 2 | 4-7 | 19:41:54 | BIGORNA: escolheu componente TFT_Item_TearOfTheGoddess | WINSTREAK | WINSTREAK: preservar vantagem atual | 24 | 1 | Adaptador | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-7 | 19:41:54 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 19 | 1 | Adaptador | DA_18_Lux_Sunbeam | -0.0500 |  |
| Jogador 2 | 4-7 | 19:41:54 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 1 | Adaptador | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 4-7 | 19:41:55 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 1 | Adaptador | DA_18_Lux_Sunbeam | -0.2100 |  |
| Jogador 2 | 4-7 | 19:41:55 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Nidalee (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.0800 |  |
| Jogador 2 | 4-7 | 19:41:55 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-1 | 19:42:03 | COMPROU: Soraka (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 15 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.4500 |  |
| Jogador 2 | 5-1 | 19:42:05 | VENDEU: Kha'Zix (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 18 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.0700 |  |
| Jogador 2 | 5-1 | 19:42:05 | COMPROU: Grompe (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.7600 |  |
| Jogador 2 | 5-1 | 19:42:05 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 13 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.2100 |  |
| Jogador 2 | 5-1 | 19:42:06 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 13 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-2 | 19:42:11 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 15 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.7300 |  |
| Jogador 2 | 5-2 | 19:42:12 | VENDEU: Mamãe Bicuda (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 18 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.0700 |  |
| Jogador 2 | 5-2 | 19:42:12 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 1 | Adaptador | DA_18_Lux_Sunbeam | 0.4200 |  |
| Jogador 2 | 5-2 | 19:42:12 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 14 | 1 | Adaptador | DA_18_Lux_Sunbeam | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 19:42:12 | VENDEU: Sejuani (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 1 | Adaptador | DA_18_Lux_Sunbeam | -0.3200 |  |
| Jogador 2 | 5-2 | 19:42:13 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 13 | 1 | Adaptador | DA_18_MasterYi_AD | 0.7600 |  |
| Jogador 2 | 5-2 | 19:42:13 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Lillia (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 13 | 1 | Adaptador | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 2 | 5-2 | 19:42:13 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 13 | 1 | Adaptador | DA_18_MasterYi_AD | 0.2300 |  |
| Jogador 2 | 5-2 | 19:42:13 | COMPROU: Alune (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 8 | 1 | Adaptador | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 2 | 5-2 | 19:42:16 | MOVE Bench -> Board: Alune (i:10.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 8 | 1 | Adaptador | DA_18_Alune | 0.3700 |  |
| Jogador 2 | 5-2 | 19:42:16 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 8 | 1 | Adaptador | DA_18_Alune | 0.0000 |  |
| Jogador 2 | 5-3 | 19:42:20 | COMPROU: Grompe (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Adaptador | DA_18_Alune | 0.2200 |  |
| Jogador 2 | 5-3 | 19:42:21 | VENDEU: Soraka (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 0 | Adaptador | DA_18_Alune | -0.3200 |  |
| Jogador 2 | 5-3 | 19:42:21 | COMPROU: Zyra (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Adaptador | DA_18_Alune | -0.1100 |  |
| Jogador 2 | 5-3 | 19:42:21 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 10 | 0 | Adaptador | DA_18_Alune | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-3 | 19:42:22 | VENDEU: Zyra (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 14 | 0 | Adaptador | DA_18_Alune | 0.0500 |  |
| Jogador 2 | 5-3 | 19:42:22 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 10 | 0 | Adaptador | DA_18_Ahri | 0.7600 |  |
| Jogador 2 | 5-3 | 19:42:22 | COMPROU: Malphite (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Ahri | -0.1900 |  |
| Jogador 2 | 5-3 | 19:42:22 | MOVE Bench -> Board: Grompe (i:4.0) <-> Lillia (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Ahri | 0.0100 |  |
| Jogador 2 | 5-3 | 19:42:23 | MOVE Bench -> Board: Lillia (i:8.0) <-> Alune (i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Ahri | 0.1000 |  |
| Jogador 2 | 5-3 | 19:42:23 | MOVE Bench -> Board: Alune (i:10.0) <-> Grompe (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Ahri | -0.3500 |  |
| Jogador 2 | 5-3 | 19:42:25 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 5-4 | 19:42:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Adaptador | DA_18_Ahri | 0.6500 |  |
| Jogador 2 | 5-4 | 19:42:29 | VENDEU: Soraka (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 13 | 0 | Adaptador | DA_18_Ahri | 0.1300 |  |
| Jogador 2 | 5-4 | 19:42:30 | COMPROU: Lux (Lunar) (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Adaptador | DA_18_Ahri | 0.0200 |  |
| Jogador 2 | 5-4 | 19:42:30 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Ahri | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-4 | 19:42:32 | VENDEU: Malphite (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 10 | 0 | Adaptador | DA_18_Ahri | 0.1300 |  |
| Jogador 2 | 5-4 | 19:42:33 | COMPROU: Morgana (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Ahri | -0.2900 |  |
| Jogador 2 | 5-4 | 19:42:33 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Adaptador | DA_18_Ahri | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-4 | 19:42:33 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Ahri | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-4 | 19:42:33 | VENDEU: Morgana (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Ahri | 0.0700 |  |
| Jogador 2 | 5-4 | 19:42:34 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Ahri | 0.2100 |  |
| Jogador 2 | 5-4 | 19:42:34 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 5-5 | 19:42:40 | VENDEU: Lux (Solar) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Adaptador | DA_18_Ahri | 0.1300 |  |
| Jogador 2 | 5-5 | 19:42:40 | COMPROU: Lux (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Adaptador | DA_18_Ahri | -0.2600 |  |
| Jogador 2 | 5-5 | 19:42:40 | REROLL | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 5-5 | 19:42:40 | VENDEU: Lux (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Adaptador | DA_18_Ahri | 0.1500 |  |
| Jogador 2 | 5-5 | 19:42:40 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Adaptador | DA_18_Ahri | 0.7200 |  |
| Jogador 2 | 5-5 | 19:42:41 | REROLL | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 5-5 | 19:42:41 | VENDEU: Lux (Lunar) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Adaptador | DA_18_Ahri | 0.1100 |  |
| Jogador 2 | 5-5 | 19:42:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Adaptador | DA_18_Ahri | 0.2000 |  |
| Jogador 2 | 5-5 | 19:42:41 | REROLL | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 5-5 | 19:42:44 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | 0.0200 |  |
| Jogador 2 | 5-5 | 19:42:44 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 5-6 | 19:42:48 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Adaptador | DA_18_Ahri | 0.7500 |  |
| Jogador 2 | 5-6 | 19:42:51 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Adaptador | DA_18_Ahri | 0.2700 |  |
| Jogador 2 | 5-6 | 19:42:51 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Adaptador | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 5-6 | 19:42:51 | MOVE Bench -> Board: Sett (i:8.0) <-> Alune (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Adaptador | DA_18_Ahri | -0.2900 |  |
| Jogador 2 | 5-6 | 19:42:51 | MOVE Bench -> Board: Alune (i:10.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Adaptador | DA_18_Ahri | -0.3500 |  |
| Jogador 2 | 5-6 | 19:42:52 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Adaptador | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 5-7 | 19:42:58 | BIGORNA: escolheu item completo TFT_Item_IonicSpark | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Adaptador | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 5-7 | 19:42:58 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Nidalee (i:8.0) (tabuleiro slot 10) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Adaptador | DA_18_Ahri | 0.1200 |  |
| Jogador 2 | 5-7 | 19:42:58 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | -0.0100 |  |
| Jogador 2 | 5-7 | 19:42:59 | MOVE Bench -> Board: Grompe (i:4.0) <-> Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | -0.0600 |  |
| Jogador 2 | 5-7 | 19:42:59 | MOVE Bench -> Board: Sett (i:8.0) <-> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | -0.8100 |  |
| Jogador 2 | 5-7 | 19:42:59 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 6-1 | 19:43:07 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Adaptador | DA_18_Ahri | 0.0500 |  |
| Jogador 2 | 6-1 | 19:43:07 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Adaptador | DA_18_Ahri | 0.8300 |  |
| Jogador 2 | 6-1 | 19:43:07 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Adaptador | DA_18_Ahri | 0.3000 |  |
| Jogador 2 | 6-1 | 19:43:07 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Adaptador | DA_18_Ahri | 0.0800 |  |
| Jogador 2 | 6-1 | 19:43:08 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Adaptador | DA_18_Ahri | 0.5600 |  |
| Jogador 2 | 6-1 | 19:43:08 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Adaptador | DA_18_Ahri | 0.4300 |  |
| Jogador 2 | 6-1 | 19:43:08 | REROLL | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 6-1 | 19:43:08 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 6-1 | 19:43:08 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | -0.3200 |  |
| Jogador 2 | 6-1 | 19:43:09 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Adaptador | DA_18_Ahri | 0.6400 |  |
| Jogador 2 | 6-1 | 19:43:12 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Adaptador | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 6-2 | 19:43:15 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Adaptador | DA_18_Ahri | -0.2600 |  |
| Jogador 2 | 6-2 | 19:43:16 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Adaptador | DA_18_Ahri | -0.1800 |  |
| Jogador 2 | 6-2 | 19:43:16 | REROLL | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 6-3 | 19:43:28 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Adaptador | DA_18_Ahri | 0.0700 |  |
| Jogador 2 | 6-3 | 19:43:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Adaptador | DA_18_Ahri | 0.8100 |  |
| Jogador 2 | 6-3 | 19:43:29 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 0 | Adaptador | DA_18_Ahri | 0.0500 |  |
| Jogador 2 | 6-3 | 19:43:29 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Adaptador | DA_18_Ahri | 0.8000 |  |
| Jogador 2 | 6-3 | 19:43:29 | REROLL | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 6-3 | 19:43:29 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Adaptador | DA_18_Ahri | -0.4500 |  |
| Jogador 2 | 6-3 | 19:43:30 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Adaptador | DA_18_Ahri | 0.6300 |  |
| Jogador 2 | 6-3 | 19:43:30 | REROLL | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 6-3 | 19:43:30 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 0 | Adaptador | DA_18_Ahri | -0.3400 |  |
| Jogador 2 | 6-4 | 19:43:45 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Adaptador | DA_18_Ahri | -0.0100 |  |
| Jogador 2 | 6-4 | 19:43:45 | REROLL | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 6-4 | 19:43:45 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Adaptador | DA_18_Ahri | -0.3900 |  |
| Jogador 2 | 6-4 | 19:43:45 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Adaptador | DA_18_Ahri | 0.3200 |  |
| Jogador 2 | 6-4 | 19:43:46 | REROLL | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Adaptador | DA_18_Ahri | -0.0900 |  |
| Jogador 2 | 6-4 | 19:43:46 | VENDEU: Ahri (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 1 | Adaptador | DA_18_Lillia | -0.3100 |  |
| Jogador 2 | 6-4 | 19:43:46 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 1 | Adaptador | DA_18_Lillia | 0.5600 |  |
| Jogador 2 | 6-4 | 19:43:46 | REROLL | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Adaptador | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 6-4 | 19:43:46 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 1 | Adaptador | DA_18_Lillia | -0.3400 |  |
| Jogador 2 | 6-5 | 19:44:01 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Adaptador | DA_18_Lillia | 0.8600 |  |
| Jogador 2 | 6-5 | 19:44:02 | VENDEU: Lillia (i:16.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 2 | Adaptador | DA_18_MasterYi_AD | -0.3200 |  |
| Jogador 2 | 6-5 | 19:44:02 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 40 | 2 | Adaptador | DA_18_MasterYi_AD | 0.8500 |  |
| Jogador 2 | 6-5 | 19:44:02 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 38 | 2 | Adaptador | DA_18_MasterYi_AD | -0.1700 |  |
| Jogador 2 | 6-5 | 19:44:02 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 2 | 6-5 | 19:44:03 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 2 | Adaptador | DA_18_MasterYi_AD | -0.8000 |  |
| Jogador 2 | 6-5 | 19:44:03 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Adaptador | DA_Nidalee18_AP | 0.9400 |  |
| Jogador 2 | 6-5 | 19:44:03 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Adaptador | DA_Nidalee18_AP | 0.6500 |  |
| Jogador 2 | 6-5 | 19:44:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 28 | 2 | Adaptador | DA_Nidalee18_AP | -0.1700 |  |
| Jogador 3 | ? | 19:38:48 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 3 | ? | 19:38:48 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.3000 |  |
| Jogador 3 | ? | 19:38:49 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.5800 |  |
| Jogador 3 | ? | 19:38:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.0000 |  |
| Jogador 3 | 1-1 | 19:38:54 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_RekSai | 1.0400 |  |
| Jogador 3 | 1-1 | 19:38:55 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_RekSai | -0.4000 |  |
| Jogador 3 | 1-1 | 19:38:55 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_RekSai | 0.3500 |  |
| Jogador 3 | 1-1 | 19:38:56 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_RekSai | -0.1400 |  |
| Jogador 3 | 1-1 | 19:38:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1400 |  |
| Jogador 3 | 1-1 | 19:38:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5100 |  |
| Jogador 3 | 1-1 | 19:38:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 1-2 | 19:39:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 1-3 | 19:39:07 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.2100 |  |
| Jogador 3 | 1-3 | 19:39:07 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | -0.2200 |  |
| Jogador 3 | 1-3 | 19:39:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 1-4 | 19:39:14 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | 0.5800 |  |
| Jogador 3 | 1-4 | 19:39:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 1.0200 |  |
| Jogador 3 | 1-4 | 19:39:14 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | -0.2900 |  |
| Jogador 3 | 1-4 | 19:39:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 1-4 | 19:39:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-1 | 19:39:20 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | -0.8300 |  |
| Jogador 3 | 2-1 | 19:39:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 1.1200 |  |
| Jogador 3 | 2-1 | 19:39:21 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 0.4200 |  |
| Jogador 3 | 2-1 | 19:39:22 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.2400 |  |
| Jogador 3 | 2-1 | 19:39:22 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.6100 |  |
| Jogador 3 | 2-1 | 19:39:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-2 | 19:39:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 2-2 | 19:39:27 | MOVE Bench -> Board: Rammus (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | -0.6900 |  |
| Jogador 3 | 2-2 | 19:39:28 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 0.1100 |  |
| Jogador 3 | 2-2 | 19:39:29 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Scuttlecrab18 | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-2 | 19:39:29 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Scuttlecrab18 | 0.5100 |  |
| Jogador 3 | 2-2 | 19:39:29 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-3 | 19:39:34 | COMPROU: Hecarim (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_Scuttlecrab18 | 0.1600 |  |
| Jogador 3 | 2-3 | 19:39:34 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_Scuttlecrab18 | -0.5800 |  |
| Jogador 3 | 2-3 | 19:39:34 | MOVE Bench -> Board: Rammus (i:6.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 2-3 | 19:39:35 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-4 | 19:39:41 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 11 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.0700 |  |
| Jogador 3 | 2-4 | 19:39:41 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.2500 |  |
| Jogador 3 | 2-4 | 19:39:41 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 2-4 | 19:39:42 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 2-4 | 19:39:42 | MOVE Bench -> Board: Rammus (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.3500 |  |
| Jogador 3 | 2-4 | 19:39:42 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.5700 |  |
| Jogador 3 | 2-4 | 19:39:42 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-5 | 19:39:48 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Vanguarda | DA_18_Diana | -0.4300 |  |
| Jogador 3 | 2-5 | 19:39:48 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Vanguarda | DA_18_Diana | 0.9500 |  |
| Jogador 3 | 2-5 | 19:39:48 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 15 | 1 | Vanguarda | DA_18_Diana | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-5 | 19:39:48 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 11 | 1 | Vanguarda | DA_18_Diana | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-5 | 19:39:49 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 1 | Vanguarda | DA_18_Diana | -0.0900 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-5 | 19:39:50 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 1 | Vanguarda | DA_18_Diana | 0.5300 |  |
| Jogador 3 | 2-5 | 19:39:50 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 1 | Vanguarda | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 2-5 | 19:39:51 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 1 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 2-6 | 19:39:55 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_18_Diana | 0.9200 |  |
| Jogador 3 | 2-6 | 19:39:55 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vanguarda | DA_18_Diana | -1.1400 |  |
| Jogador 3 | 2-6 | 19:39:55 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.9600 |  |
| Jogador 3 | 2-6 | 19:39:56 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.4600 |  |
| Jogador 3 | 2-6 | 19:39:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-7 | 19:40:02 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.2100 |  |
| Jogador 3 | 2-7 | 19:40:02 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.4400 |  |
| Jogador 3 | 2-7 | 19:40:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-1 | 19:40:09 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Vanguarda | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 3-1 | 19:40:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Vanguarda | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-1 | 19:40:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Vanguarda | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 3-1 | 19:40:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 1 | Vanguarda | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-1 | 19:40:11 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Vanguarda | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-1 | 19:40:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-2 | 19:40:16 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.3700 |  |
| Jogador 3 | 3-2 | 19:40:16 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.6600 |  |
| Jogador 3 | 3-2 | 19:40:17 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Vanguarda | DA_Scuttlecrab18 | -1.0800 |  |
| Jogador 3 | 3-2 | 19:40:17 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.3100 |  |
| Jogador 3 | 3-2 | 19:40:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-2 | 19:40:18 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-3 | 19:40:24 | VENDEU: Sivir (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.2900 |  |
| Jogador 3 | 3-3 | 19:40:24 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 3-3 | 19:40:24 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.2900 |  |
| Jogador 3 | 3-3 | 19:40:25 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 3-3 | 19:40:26 | MOVE Bench -> Board: Elise (i:4.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.7800 |  |
| Jogador 3 | 3-3 | 19:40:26 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.5700 |  |
| Jogador 3 | 3-3 | 19:40:26 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 3-3 | 19:40:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-4 | 19:40:31 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 3-4 | 19:40:31 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vanguarda | DA_Scuttlecrab18 | 0.6600 |  |
| Jogador 3 | 3-4 | 19:40:32 | MOVE Bench -> Board: Elise (i:4.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vanguarda | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 3 | 3-4 | 19:40:33 | VENDEU: Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Vanguarda | DA_18_Diana | -0.3800 |  |
| Jogador 3 | 3-4 | 19:40:33 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Zyra | -0.1000 |  |
| Jogador 3 | 3-4 | 19:40:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 3-4 | 19:40:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 3-4 | 19:40:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Zyra | 0.0000 |  |
| Jogador 3 | 3-5 | 19:40:38 | VENDEU: Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Vanguarda | DA_18_Diana | -0.3100 |  |
| Jogador 3 | 3-5 | 19:40:38 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Elise | 0.6900 |  |
| Jogador 3 | 3-5 | 19:40:39 | MOVE Bench -> Board: Elise (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Elise | 0.4400 |  |
| Jogador 3 | 3-5 | 19:40:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Elise | 0.0400 |  |
| Jogador 3 | 3-5 | 19:40:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Elise | -0.0300 |  |
| Jogador 3 | 3-5 | 19:40:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Elise | 0.0000 |  |
| Jogador 3 | 3-6 | 19:40:46 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Elise | -0.1000 |  |
| Jogador 3 | 3-6 | 19:40:46 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Elise | -0.5100 |  |
| Jogador 3 | 3-6 | 19:40:47 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Elise | -0.3000 |  |
| Jogador 3 | 3-6 | 19:40:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Elise | 0.0000 |  |
| Jogador 3 | 3-7 | 19:40:55 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Elise (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vanguarda | DA_18_Elise | -0.7000 |  |
| Jogador 3 | 3-7 | 19:40:55 | VENDEU: Elise (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.5300 |  |
| Jogador 3 | 3-7 | 19:40:55 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Vanguarda | DA_18_Soraka | 0.0500 |  |
| Jogador 3 | 3-7 | 19:40:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Soraka | -0.0900 |  |
| Jogador 3 | 3-7 | 19:40:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Soraka | -0.0100 |  |
| Jogador 3 | 3-7 | 19:40:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Soraka | -0.0100 |  |
| Jogador 3 | 3-7 | 19:40:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Soraka | 0.0000 |  |
| Jogador 3 | 4-1 | 19:41:03 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.3200 |  |
| Jogador 3 | 4-1 | 19:41:04 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.6500 |  |
| Jogador 3 | 4-1 | 19:41:04 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 3 | 4-1 | 19:41:04 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 3 | 4-1 | 19:41:05 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Soraka | -0.0900 |  |
| Jogador 3 | 4-1 | 19:41:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Soraka | -0.0100 |  |
| Jogador 3 | 4-1 | 19:41:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Soraka | 0.0000 |  |
| Jogador 3 | 4-2 | 19:41:11 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Hecarim | 0.7600 |  |
| Jogador 3 | 4-2 | 19:41:13 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Hecarim | 0.4800 |  |
| Jogador 3 | 4-2 | 19:41:13 | MOVE Bench -> Board: Soraka (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Hecarim | 0.4200 |  |
| Jogador 3 | 4-2 | 19:41:13 | COMPROU: Sett (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Hecarim | -0.0400 |  |
| Jogador 3 | 4-2 | 19:41:13 | MOVE Bench -> Board: Sett (i:8.0) <-> Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Hecarim | -0.3400 |  |
| Jogador 3 | 4-2 | 19:41:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Hecarim | 0.0000 |  |
| Jogador 3 | 4-3 | 19:41:19 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Vanguarda | DA_18_Hecarim | -0.0100 |  |
| Jogador 3 | 4-3 | 19:41:19 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Vanguarda | DA_18_Hecarim | 0.0000 |  |
| Jogador 3 | 4-4 | 19:41:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Vanguarda | DA_18_Hecarim | 0.7300 |  |
| Jogador 3 | 4-4 | 19:41:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Vanguarda | DA_18_Hecarim | -0.0100 |  |
| Jogador 3 | 4-4 | 19:41:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Vanguarda | DA_18_Hecarim | 0.0000 |  |
| Jogador 3 | 4-5 | 19:41:37 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Vanguarda | DA_18_Hecarim | -0.1800 |  |
| Jogador 3 | 4-5 | 19:41:37 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Vanguarda | DA_18_Hecarim | 0.4000 |  |
| Jogador 3 | 4-5 | 19:41:38 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Vanguarda | DA_18_Hecarim | 0.0000 |  |
| Jogador 3 | 4-5 | 19:41:42 | MOVE Bench -> Board: Soraka (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Vanguarda | DA_18_Hecarim | 0.4000 |  |
| Jogador 3 | 4-6 | 19:41:45 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Vanguarda | DA_18_Hecarim | 0.3400 |  |
| Jogador 3 | 4-6 | 19:41:45 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_18_Hecarim | 0.6500 |  |
| Jogador 3 | 4-6 | 19:41:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_18_Hecarim | -0.0500 |  |
| Jogador 3 | 4-7 | 19:41:54 | BIGORNA: escolheu componente TFT_Item_SparringGloves | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Vanguarda | DA_18_Hecarim | 0.0000 |  |
| Jogador 3 | 4-7 | 19:41:54 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Vanguarda | DA_18_Hecarim | -0.1500 |  |
| Jogador 3 | 4-7 | 19:41:54 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Vanguarda | DA_18_Hecarim | -0.2300 |  |
| Jogador 3 | 4-7 | 19:41:55 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_18_Hecarim | -0.0900 |  |
| Jogador 3 | 4-7 | 19:41:55 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_SparringGloves -> Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_18_Hecarim | 0.1200 |  |
| Jogador 3 | 4-7 | 19:41:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_18_Hecarim | -0.0500 |  |
| Jogador 4 | ? | 19:38:48 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 4 | ? | 19:38:48 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 4 | ? | 19:38:49 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 4 | ? | 19:38:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-1 | 19:38:54 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 4 | 1-1 | 19:38:55 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 4 | 1-1 | 19:38:55 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.1400 |  |
| Jogador 4 | 1-1 | 19:38:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 4 | 1-1 | 19:38:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5200 |  |
| Jogador 4 | 1-1 | 19:38:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-2 | 19:39:01 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Gromp18_AP | 0.2400 |  |
| Jogador 4 | 1-2 | 19:39:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 1-3 | 19:39:07 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.4200 |  |
| Jogador 4 | 1-3 | 19:39:07 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 4 | 1-3 | 19:39:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-4 | 19:39:14 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Akali_AD | 0.5300 |  |
| Jogador 4 | 1-4 | 19:39:14 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 4 | 1-4 | 19:39:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 4 | 1-4 | 19:39:15 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 4 | 1-4 | 19:39:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-1 | 19:39:20 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Akali_AD | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-1 | 19:39:21 | MOVE Bench -> Board: Yorick (i:2.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Yorick | -0.6300 |  |
| Jogador 4 | 2-1 | 19:39:21 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Yorick | 0.5100 |  |
| Jogador 4 | 2-1 | 19:39:22 | COMPROU: Elise (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Yorick | 0.0400 |  |
| Jogador 4 | 2-1 | 19:39:22 | MOVE Bench -> Board: Elise (i:4.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Yorick | -0.2600 |  |
| Jogador 4 | 2-1 | 19:39:22 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 2-2 | 19:39:27 | VENDEU: Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 11 | 0 | — | DA_18_Yorick | -0.8500 |  |
| Jogador 4 | 2-2 | 19:39:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 4 | 2-2 | 19:39:28 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-2 | 19:39:29 | MOVE Bench -> Board: Elise (i:4.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 4 | 2-2 | 19:39:29 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 19:39:34 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | — | DA_KogMaw18_AD | -0.8500 |  |
| Jogador 4 | 2-3 | 19:39:34 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Aphelios | 0.1800 |  |
| Jogador 4 | 2-3 | 19:39:34 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Aphelios | -0.8100 |  |
| Jogador 4 | 2-3 | 19:39:35 | MOVE Bench -> Board: Elise (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Aphelios | 0.0900 |  |
| Jogador 4 | 2-3 | 19:39:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Aphelios | -0.1200 |  |
| Jogador 4 | 2-3 | 19:39:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-3 | 19:39:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-3 | 19:39:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-4 | 19:39:41 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Adaptador | DA_18_Aphelios | -0.0200 |  |
| Jogador 4 | 2-4 | 19:39:41 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_18_Aphelios | 0.3500 |  |
| Jogador 4 | 2-4 | 19:39:41 | MOVE Bench -> Board: Diana (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_18_Aphelios | -0.8400 |  |
| Jogador 4 | 2-4 | 19:39:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_18_Aphelios | 0.0300 |  |
| Jogador 4 | 2-4 | 19:39:42 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_18_Aphelios | 0.1600 |  |
| Jogador 4 | 2-4 | 19:39:42 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Aphelios | 0.4400 |  |
| Jogador 4 | 2-4 | 19:39:42 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-5 | 19:39:48 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Aphelios | 0.3100 |  |
| Jogador 4 | 2-5 | 19:39:48 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Aphelios | 0.1000 |  |
| Jogador 4 | 2-5 | 19:39:48 | MOVE Board -> Board: Nidalee (i:8.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Aphelios | -0.1000 |  |
| Jogador 4 | 2-5 | 19:39:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-6 | 19:39:55 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Adaptador | DA_18_Aphelios | -0.7300 |  |
| Jogador 4 | 2-6 | 19:39:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-6 | 19:39:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-6 | 19:39:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-7 | 19:40:02 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_18_Aphelios | -0.5000 |  |
| Jogador 4 | 2-7 | 19:40:02 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_18_Aphelios | 0.2100 |  |
| Jogador 4 | 2-7 | 19:40:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-7 | 19:40:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-1 | 19:40:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-1 | 19:40:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-2 | 19:40:16 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Adaptador | DA_18_Aphelios | -0.3800 |  |
| Jogador 4 | 3-2 | 19:40:16 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_18_Aphelios | -0.1100 |  |
| Jogador 4 | 3-2 | 19:40:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-2 | 19:40:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-3 | 19:40:24 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_18_Aphelios | 0.2100 |  |
| Jogador 4 | 3-3 | 19:40:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 3-3 | 19:40:24 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | 0.1000 |  |
| Jogador 4 | 3-3 | 19:40:25 | MOVE Bench -> Board: Elise (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | -0.4400 |  |
| Jogador 4 | 3-3 | 19:40:26 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | 0.7400 |  |
| Jogador 4 | 3-3 | 19:40:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-4 | 19:40:31 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Adaptador | DA_18_Aphelios | 0.0700 |  |
| Jogador 4 | 3-4 | 19:40:31 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Adaptador | DA_18_Aphelios | 0.6500 |  |
| Jogador 4 | 3-4 | 19:40:32 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Adaptador | DA_18_Aphelios | 0.0200 |  |
| Jogador 4 | 3-4 | 19:40:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-4 | 19:40:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-4 | 19:40:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-5 | 19:40:38 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-5 | 19:40:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-6 | 19:40:46 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_18_MasterYi_AD | 0.7600 |  |
| Jogador 4 | 3-6 | 19:40:46 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_18_MasterYi_AD | 0.5800 |  |
| Jogador 4 | 3-6 | 19:40:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0300 |  |
| Jogador 4 | 3-6 | 19:40:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 19:40:51 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_MasterYi_AD | 0.4300 |  |
| Jogador 4 | 3-7 | 19:40:55 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Adaptador | DA_18_MasterYi_AD | 0.7300 |  |
| Jogador 4 | 3-7 | 19:40:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-7 | 19:40:55 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0400 |  |
| Jogador 4 | 3-7 | 19:40:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-1 | 19:41:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-1 | 19:41:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 19:41:11 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-2 | 19:41:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-2 | 19:41:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-3 | 19:41:19 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-3 | 19:41:19 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 19:41:29 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 4 | 4-4 | 19:41:29 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Adaptador | DA_18_MasterYi_AD | 0.5600 |  |
| Jogador 4 | 4-4 | 19:41:29 | COMPROU: Soraka (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Adaptador | DA_18_MasterYi_AD | -0.1600 |  |
| Jogador 4 | 4-4 | 19:41:30 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-5 | 19:41:37 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 4 | 4-5 | 19:41:37 | COMPROU: Malphite (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Adaptador | DA_18_MasterYi_AD | -0.1600 |  |
| Jogador 4 | 4-5 | 19:41:38 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-6 | 19:41:45 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Adaptador | DA_18_Diana | 0.7600 |  |
| Jogador 4 | 4-6 | 19:41:45 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Master Yi (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Adaptador | DA_18_Diana | -0.7000 |  |
| Jogador 4 | 4-6 | 19:41:48 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Aphelios (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Adaptador | DA_18_Diana | 0.2600 |  |
| Jogador 4 | 4-6 | 19:41:48 | MOVE Bench -> Board: Malphite (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Adaptador | DA_18_Diana | 0.2100 |  |
| Jogador 4 | 4-6 | 19:41:48 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Adaptador | DA_18_Diana | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 4 | 4-6 | 19:41:48 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Adaptador | DA_18_Diana | 0.0000 |  |
| Jogador 4 | 4-7 | 19:41:54 | BIGORNA: escolheu componente TFT_Item_BFSword | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Adaptador | DA_18_Diana | 0.0000 |  |
| Jogador 4 | 4-7 | 19:41:54 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Adaptador | DA_18_Diana | 0.2100 |  |
| Jogador 4 | 4-7 | 19:41:54 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Malphite (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Adaptador | DA_18_Diana | -0.0300 |  |
| Jogador 4 | 4-7 | 19:41:55 | MOVE Bench -> Board: Malphite (i:8.0) <-> Azuporã (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Adaptador | DA_18_Diana | -0.3500 |  |
| Jogador 4 | 4-7 | 19:41:55 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Adaptador | DA_18_Diana | 0.0000 |  |
| Jogador 4 | 5-1 | 19:42:03 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Adaptador | DA_18_Diana | -0.7000 |  |
| Jogador 4 | 5-1 | 19:42:05 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Adaptador | DA_18_Diana | 0.1100 |  |
| Jogador 4 | 5-1 | 19:42:05 | MOVE Bench -> Board: Malphite (i:8.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Adaptador | DA_18_Diana | -0.3000 |  |
| Jogador 4 | 5-1 | 19:42:05 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Adaptador | DA_18_Diana | 0.8600 |  |
| Jogador 4 | 5-1 | 19:42:06 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Adaptador | DA_18_Diana | 0.0000 |  |
| Jogador 4 | 5-2 | 19:42:11 | COMPROU: Morgana (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Adaptador | DA_18_Diana | 0.1000 |  |
| Jogador 4 | 5-2 | 19:42:12 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Adaptador | DA_18_Diana | -0.0900 |  |
| Jogador 4 | 5-2 | 19:42:12 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_Diana | 0.0900 |  |
| Jogador 4 | 5-2 | 19:42:12 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_Diana | -0.0500 |  |
| Jogador 4 | 5-3 | 19:42:20 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Adaptador | DA_18_Diana | 0.8100 |  |
| Jogador 4 | 5-3 | 19:42:21 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_Diana | 0.0800 |  |
| Jogador 4 | 5-3 | 19:42:21 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_Diana | -0.0500 |  |
| Jogador 4 | 5-4 | 19:42:29 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Adaptador | DA_18_Diana | -0.1700 |  |
| Jogador 4 | 5-4 | 19:42:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_Diana | -0.0900 |  |
| Jogador 4 | 5-4 | 19:42:30 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Adaptador | DA_18_Diana | 0.0500 |  |
| Jogador 4 | 5-4 | 19:42:30 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Adaptador | DA_18_Diana | 0.0600 |  |
| Jogador 4 | 5-4 | 19:42:32 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Adaptador | DA_18_Diana | -0.0500 |  |
| Jogador 4 | 5-5 | 19:42:40 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Adaptador | DA_18_Diana | -0.0900 |  |
| Jogador 4 | 5-5 | 19:42:40 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Adaptador | DA_18_Diana | 0.0500 |  |
| Jogador 4 | 5-5 | 19:42:40 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Adaptador | DA_18_Diana | 0.7900 |  |
| Jogador 4 | 5-5 | 19:42:40 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Adaptador | DA_18_Diana | -0.0900 |  |
| Jogador 4 | 5-5 | 19:42:40 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_Diana | -0.0900 |  |
| Jogador 4 | 5-5 | 19:42:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_Diana | -0.0500 |  |
| Jogador 5 | ? | 19:38:48 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0200 |  |
| Jogador 5 | ? | 19:38:48 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 5 | ? | 19:38:49 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 5 | ? | 19:38:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 5 | 1-1 | 19:38:54 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0300 |  |
| Jogador 5 | 1-1 | 19:38:55 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.3600 |  |
| Jogador 5 | 1-1 | 19:38:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 1-2 | 19:39:01 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.2500 |  |
| Jogador 5 | 1-2 | 19:39:01 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | -0.4200 |  |
| Jogador 5 | 1-2 | 19:39:01 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.5200 |  |
| Jogador 5 | 1-2 | 19:39:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 1-3 | 19:39:07 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | 0.1000 |  |
| Jogador 5 | 1-3 | 19:39:07 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | -0.3100 |  |
| Jogador 5 | 1-3 | 19:39:08 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | -0.4600 |  |
| Jogador 5 | 1-3 | 19:39:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 1-4 | 19:39:14 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Elise | 0.6800 |  |
| Jogador 5 | 1-4 | 19:39:14 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 19:39:14 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Elise | -0.7100 |  |
| Jogador 5 | 1-4 | 19:39:15 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | 0.1300 |  |
| Jogador 5 | 1-4 | 19:39:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 2-1 | 19:39:20 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Elise | 0.0800 |  |
| Jogador 5 | 2-1 | 19:39:21 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | 0.1900 |  |
| Jogador 5 | 2-1 | 19:39:21 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | -0.2800 |  |
| Jogador 5 | 2-1 | 19:39:22 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 5 | 2-1 | 19:39:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-2 | 19:39:27 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 5 | 2-2 | 19:39:27 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_MasterYi_AD | 0.3700 |  |
| Jogador 5 | 2-2 | 19:39:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 5 | 2-2 | 19:39:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_MasterYi_AD | 0.0400 |  |
| Jogador 5 | 2-2 | 19:39:29 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_MasterYi_AD | 0.5500 |  |
| Jogador 5 | 2-2 | 19:39:29 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_MasterYi_AD | 0.3500 |  |
| Jogador 5 | 2-2 | 19:39:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 5 | 2-2 | 19:39:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-3 | 19:39:34 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 5 | 2-3 | 19:39:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.3700 |  |
| Jogador 5 | 2-3 | 19:39:34 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 5 | 2-3 | 19:39:35 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 5 | 2-3 | 19:39:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 2-3 | 19:39:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 2-4 | 19:39:41 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 5 | 2-4 | 19:39:41 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 2-4 | 19:39:41 | MOVE Bench -> Board: Rammus (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 2-4 | 19:39:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 2-5 | 19:39:48 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 2-5 | 19:39:48 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Adaptador | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 5 | 2-5 | 19:39:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 2-5 | 19:39:48 | MOVE Bench -> Board: Grompe (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | -0.8000 |  |
| Jogador 5 | 2-5 | 19:39:49 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.5200 |  |
| Jogador 5 | 2-5 | 19:39:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 2-6 | 19:39:55 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Adaptador | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 5 | 2-6 | 19:39:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Adaptador | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 5 | 2-6 | 19:39:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 2-6 | 19:39:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 2-6 | 19:39:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 2-7 | 19:40:02 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_KogMaw18_AD | -0.4500 |  |
| Jogador 5 | 2-7 | 19:40:02 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 5 | 2-7 | 19:40:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 2-7 | 19:40:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-1 | 19:40:09 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Adaptador | DA_KogMaw18_AD | -0.8800 |  |
| Jogador 5 | 3-1 | 19:40:09 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 5 | 3-1 | 19:40:10 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Adaptador | DA_KogMaw18_AD | -1.1800 |  |
| Jogador 5 | 3-1 | 19:40:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Adaptador | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 5 | 3-1 | 19:40:11 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-1 | 19:40:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-2 | 19:40:16 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Adaptador | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 5 | 3-2 | 19:40:16 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_KogMaw18_AD | 0.5800 |  |
| Jogador 5 | 3-2 | 19:40:17 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 5 | 3-2 | 19:40:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-2 | 19:40:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-3 | 19:40:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 3-3 | 19:40:24 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 3-3 | 19:40:24 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_KogMaw18_AD | -0.3500 |  |
| Jogador 5 | 3-3 | 19:40:25 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.5400 |  |
| Jogador 5 | 3-3 | 19:40:26 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 5 | 3-3 | 19:40:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-3 | 19:40:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-4 | 19:40:31 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Adaptador | DA_KogMaw18_AD | -0.8800 |  |
| Jogador 5 | 3-4 | 19:40:31 | COMPROU: Morgana (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_18_Morgana | -0.0300 |  |
| Jogador 5 | 3-4 | 19:40:32 | MOVE Bench -> Board: Morgana (i:8.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_18_Morgana | 0.0800 |  |
| Jogador 5 | 3-4 | 19:40:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Morgana | -0.0100 |  |
| Jogador 5 | 3-4 | 19:40:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 3-5 | 19:40:38 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Adaptador | DA_18_Morgana | 0.0200 |  |
| Jogador 5 | 3-5 | 19:40:38 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Adaptador | DA_18_Morgana | 0.1100 |  |
| Jogador 5 | 3-5 | 19:40:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Morgana | -0.0100 |  |
| Jogador 5 | 3-5 | 19:40:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Adaptador | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 3-6 | 19:40:46 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Adaptador | DA_18_Morgana | -0.3300 |  |
| Jogador 5 | 3-6 | 19:40:46 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Adaptador | DA_18_Morgana | -0.2100 |  |
| Jogador 5 | 3-6 | 19:40:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Adaptador | DA_18_Morgana | -0.0100 |  |
| Jogador 5 | 3-6 | 19:40:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_18_Morgana | -0.0100 |  |
| Jogador 5 | 3-6 | 19:40:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 3-7 | 19:40:55 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Adaptador | DA_18_Morgana | 0.0900 |  |
| Jogador 5 | 3-7 | 19:40:55 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_18_Morgana | 0.0400 |  |
| Jogador 5 | 3-7 | 19:40:55 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_18_Morgana | -0.4300 |  |
| Jogador 5 | 3-7 | 19:40:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Morgana | -0.0100 |  |
| Jogador 5 | 3-7 | 19:40:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 4-1 | 19:41:03 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Adaptador | DA_18_Morgana | -0.4000 |  |
| Jogador 5 | 4-1 | 19:41:04 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_18_Rammus | 0.6500 |  |
| Jogador 5 | 4-1 | 19:41:04 | MOVE Bench -> Board: Rammus (i:12.0) <-> Morgana (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_18_Rammus | 0.1300 |  |
| Jogador 5 | 4-1 | 19:41:04 | MOVE Bench -> Board: Morgana (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Adaptador | DA_18_Rammus | 0.3700 |  |
| Jogador 5 | 4-1 | 19:41:05 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_18_Rammus | 0.2000 |  |
| Jogador 5 | 4-1 | 19:41:05 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Adaptador | DA_18_Rammus | 0.5600 |  |
| Jogador 5 | 4-1 | 19:41:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-1 | 19:41:06 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-2 | 19:41:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Rammus | 0.7300 |  |
| Jogador 5 | 4-2 | 19:41:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-3 | 19:41:19 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Adaptador | DA_18_Rammus | -0.8400 |  |
| Jogador 5 | 4-3 | 19:41:19 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Adaptador | DA_18_Rammus | 0.6500 |  |
| Jogador 5 | 4-3 | 19:41:19 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Adaptador | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-3 | 19:41:20 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-3 | 19:41:20 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-3 | 19:41:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-4 | 19:41:29 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Rammus | 0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 4-4 | 19:41:29 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rammus (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Rammus | -0.3500 |  |
| Jogador 5 | 4-4 | 19:41:29 | MOVE Bench -> Board: Rammus (i:12.0) <-> Morgana (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 4-4 | 19:41:30 | MOVE Bench -> Board: Morgana (i:8.0) <-> Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Rammus | -0.4600 |  |
| Jogador 5 | 4-4 | 19:41:30 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Rammus | -0.2200 |  |
| Jogador 5 | 4-4 | 19:41:30 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-4 | 19:41:34 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Adaptador | DA_18_Rammus | 0.5300 |  |
| Jogador 5 | 4-5 | 19:41:37 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Adaptador | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 4-5 | 19:41:37 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Morgana (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Adaptador | DA_18_Rammus | 0.1700 |  |
| Jogador 5 | 4-5 | 19:41:38 | MOVE Bench -> Board: Morgana (i:8.0) <-> Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Adaptador | DA_18_Rammus | -0.8200 |  |
| Jogador 5 | 4-5 | 19:41:38 | VENDEU: Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Adaptador | DA_18_Rammus | -0.4300 |  |
| Jogador 5 | 4-5 | 19:41:38 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Adaptador | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 4-5 | 19:41:38 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Adaptador | DA_18_Rammus | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 4-5 | 19:41:39 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-6 | 19:41:45 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Adaptador | DA_18_Rammus | 0.1400 |  |
| Jogador 5 | 4-6 | 19:41:45 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Adaptador | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-6 | 19:41:48 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-7 | 19:41:54 | BIGORNA: escolheu componente TFT_Item_RecurveBow | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-7 | 19:41:54 | COMPROU: Morgana (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Adaptador | DA_18_Rammus | 0.7800 |  |
| Jogador 5 | 4-7 | 19:41:54 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Master Yi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Adaptador | DA_18_Rammus | 0.1100 |  |
| Jogador 5 | 4-7 | 19:41:55 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-1 | 19:42:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Adaptador | DA_18_Rammus | 0.8400 |  |
| Jogador 5 | 5-1 | 19:42:05 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Adaptador | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 5-1 | 19:42:05 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-2 | 19:42:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Adaptador | DA_KogMaw18_AD | 0.7800 |  |
| Jogador 5 | 5-2 | 19:42:12 | MOVE Bench -> Board: Morgana (i:8.0) <-> Morgana (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Adaptador | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 5 | 5-2 | 19:42:12 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Adaptador | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 5 | 5-2 | 19:42:12 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 5-2 | 19:42:12 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-2 | 19:42:17 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.5500 |  |
| Jogador 5 | 5-3 | 19:42:20 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 5 | 5-3 | 19:42:21 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-4 | 19:42:29 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Adaptador | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 5 | 5-4 | 19:42:29 | COMPROU: Ashe (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Adaptador | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 5 | 5-4 | 19:42:30 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-5 | 19:42:40 | COMPROU: Grompe (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Adaptador | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 5 | 5-5 | 19:42:40 | COMPROU: Vi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Adaptador | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 5-5 | 19:42:40 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-6 | 19:42:48 | VENDEU: Vi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 20 | 0 | Adaptador | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 5 | 5-6 | 19:42:51 | COMPROU: Nidalee (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 0 | Adaptador | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 5 | 5-6 | 19:42:51 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Adaptador | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 5 | 5-6 | 19:42:51 | VENDEU: Grompe (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 0 | Adaptador | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 5-6 | 19:42:51 | COMPROU: Rammus (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 0 | Adaptador | DA_18_Rammus | 0.7700 |  |
| Jogador 5 | 5-6 | 19:42:52 | VENDEU: Rubrivira (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 17 | 0 | Adaptador | DA_18_Rammus | 0.0200 |  |
| Jogador 5 | 5-6 | 19:42:52 | COMPROU: Ashe (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Adaptador | DA_18_Rammus | 0.7100 |  |
| Jogador 5 | 5-6 | 19:42:52 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Adaptador | DA_18_Rammus | -0.1600 |  |
| Jogador 5 | 5-6 | 19:42:52 | VENDEU: Kog'Maw (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 0 | Adaptador | DA_18_Rammus | -0.4900 |  |
| Jogador 5 | 5-6 | 19:42:52 | COMPROU: Aphelios (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Adaptador | DA_18_Rammus | -0.2400 |  |
| Jogador 5 | 5-6 | 19:42:53 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-7 | 19:42:58 | BIGORNA: escolheu item completo TFT_Item_ThiefsGloves | WINSTREAK | WINSTREAK: preservar vantagem atual | 23 | 1 | Adaptador | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-7 | 19:42:58 | EQUIP_FROM_INVENTORY: TFT_Item_ThiefsGloves -> Master Yi (i:6.0) (tabuleiro slot 24) | WINSTREAK | WINSTREAK: preservar vantagem atual | 23 | 1 | Adaptador | DA_18_Rammus | 0.1000 |  |
| Jogador 5 | 5-7 | 19:42:58 | VENDEU: Aphelios (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 1 | Adaptador | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 5-7 | 19:42:59 | COMPROU: Maokai (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Adaptador | DA_18_Rammus | -0.1400 |  |
| Jogador 5 | 5-7 | 19:42:59 | VENDEU: Diana (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Adaptador | DA_18_Rammus | -0.7600 |  |
| Jogador 5 | 5-7 | 19:42:59 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 20 | 1 | Adaptador | DA_18_Rammus | -0.1900 |  |
| Jogador 5 | 5-7 | 19:42:59 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 1 | Adaptador | DA_18_Rammus | -0.2400 |  |
| Jogador 5 | 5-7 | 19:42:59 | VENDEU: Maokai (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 23 | 1 | Adaptador | DA_18_Rammus | 0.1300 |  |
| Jogador 5 | 5-7 | 19:43:00 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 20 | 1 | Adaptador | DA_18_Rammus | 0.8100 |  |
| Jogador 5 | 5-7 | 19:43:02 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 1 | Adaptador | DA_18_Rammus | -0.2400 |  |
| Jogador 5 | 5-7 | 19:43:03 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 1 | Adaptador | DA_18_Rammus | -0.0300 |  |
| Jogador 5 | 6-1 | 19:43:07 | VENDEU: Diana (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 31 | 1 | Adaptador | DA_18_Rammus | -0.6800 |  |
| Jogador 5 | 6-1 | 19:43:07 | COMPROU: Lillia (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 1 | Adaptador | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-1 | 19:43:07 | VENDEU: Lillia (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 31 | 1 | Adaptador | DA_18_Rammus | 0.1400 |  |
| Jogador 5 | 6-1 | 19:43:07 | COMPROU: Malphite (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 1 | Adaptador | DA_18_Rammus | -0.2200 |  |
| Jogador 5 | 6-1 | 19:43:08 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Adaptador | DA_18_Rammus | -0.1600 |  |
| Jogador 5 | 6-1 | 19:43:08 | VENDEU: Malphite (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 1 | Adaptador | DA_18_Rammus | 0.0500 |  |
| Jogador 5 | 6-1 | 19:43:08 | COMPROU: Rammus (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 26 | 1 | Adaptador | DA_18_Rammus | 0.8700 |  |
| Jogador 5 | 6-1 | 19:43:08 | COMPROU: Nidalee (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Adaptador | DA_18_Rammus | 0.8700 |  |
| Jogador 5 | 6-1 | 19:43:08 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 19 | 1 | Adaptador | DA_18_Rammus | 0.7900 |  |
| Jogador 5 | 6-1 | 19:43:09 | MOVE Bench -> Board: Ashe (i:10.0) <-> Azuporã (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 19 | 1 | Adaptador | DA_18_Rammus | -1.0400 |  |
| Jogador 5 | 6-1 | 19:43:12 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 19 | 1 | Adaptador | DA_18_Rammus | -0.0300 |  |
| Jogador 5 | 6-2 | 19:43:15 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 25 | 1 | Adaptador | DA_18_Rammus | 0.5600 |  |
| Jogador 5 | 6-2 | 19:43:16 | MOVE Bench -> Board: Nidalee (i:16.0) <-> Ashe (i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 1 | Adaptador | DA_Nidalee18_AP | 0.3200 |  |
| Jogador 5 | 6-2 | 19:43:16 | MOVE Bench -> Board: Ashe (i:10.0) <-> Morgana (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 1 | Adaptador | DA_Nidalee18_AP | -0.8500 |  |
| Jogador 5 | 6-3 | 19:43:28 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | 0.3300 |  |
| Jogador 5 | 6-3 | 19:43:29 | MOVE Bench -> Board: Morgana (i:8.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | -0.7900 |  |
| Jogador 5 | 6-3 | 19:43:29 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Ashe (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | 0.3400 |  |
| Jogador 5 | 6-3 | 19:43:29 | MOVE Bench -> Board: Ashe (i:10.0) <-> Morgana (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | -0.8500 |  |
| Jogador 5 | 6-3 | 19:43:29 | MOVE Bench -> Board: Morgana (i:8.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | -0.7900 |  |
| Jogador 5 | 6-3 | 19:43:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | -0.2400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 6-4 | 19:43:45 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 3 | Adaptador | DA_18_Rammus | 0.8900 |  |
| Jogador 5 | 6-4 | 19:43:45 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Ashe (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 3 | Adaptador | DA_18_Rammus | 0.3500 |  |
| Jogador 5 | 6-4 | 19:43:45 | REROLL | STABILIZE | STABILIZE: pressão de vida | 34 | 3 | Adaptador | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-4 | 19:43:45 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_Rammus | -0.0800 |  |
| Jogador 5 | 6-4 | 19:43:46 | MOVE Bench -> Board: Sett (i:8.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_Rammus | -0.8200 |  |
| Jogador 5 | 6-4 | 19:43:46 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Morgana (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_Rammus | 0.1700 |  |
| Jogador 5 | 6-4 | 19:43:46 | MOVE Bench -> Board: Morgana (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_Rammus | 0.4100 |  |
| Jogador 5 | 6-4 | 19:43:46 | REROLL | STABILIZE | STABILIZE: pressão de vida | 28 | 3 | Adaptador | DA_18_Rammus | -0.1700 |  |
| Jogador 5 | 6-4 | 19:43:46 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 24 | 3 | Adaptador | DA_18_Rammus | -0.1000 |  |
| Jogador 5 | 6-5 | 19:44:01 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Adaptador | DA_18_Rammus | 0.0500 |  |
| Jogador 5 | 6-5 | 19:44:02 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Adaptador | DA_18_Rammus | 0.9500 |  |
| Jogador 5 | 6-5 | 19:44:02 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | 0.8600 |  |
| Jogador 5 | 6-5 | 19:44:02 | MOVE Bench -> Board: Rammus (i:18.0) <-> Nidalee (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | -0.4000 |  |
| Jogador 5 | 6-5 | 19:44:02 | MOVE Bench -> Board: Nidalee (i:16.0) <-> Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | 0.1600 |  |
| Jogador 5 | 6-5 | 19:44:03 | MOVE Bench -> Board: Sett (i:8.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | -0.8200 |  |
| Jogador 5 | 6-5 | 19:44:03 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Nidalee (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | -0.3700 |  |
| Jogador 5 | 6-5 | 19:44:03 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_Rammus | -0.2400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | ? | 19:38:48 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | 0.0000 |  |
| Jogador 6 | ? | 19:38:48 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 6 | ? | 19:38:49 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 6 | ? | 19:38:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 6 | 1-1 | 19:38:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0300 |  |
| Jogador 6 | 1-1 | 19:38:55 | MOVE Bench -> Board: Yunara (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | -1.0600 |  |
| Jogador 6 | 1-1 | 19:38:55 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.5800 |  |
| Jogador 6 | 1-1 | 19:38:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0000 |  |
| Jogador 6 | 1-2 | 19:39:01 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0800 |  |
| Jogador 6 | 1-2 | 19:39:01 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | -0.3100 |  |
| Jogador 6 | 1-2 | 19:39:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0000 |  |
| Jogador 6 | 1-2 | 19:39:06 | MOVE Bench -> Board: Caitlyn (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.3600 |  |
| Jogador 6 | 1-3 | 19:39:07 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yunara | 0.2600 |  |
| Jogador 6 | 1-3 | 19:39:07 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | -0.4800 |  |
| Jogador 6 | 1-3 | 19:39:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 6 | 1-4 | 19:39:14 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Murkwolf18 | -0.0900 |  |
| Jogador 6 | 1-4 | 19:39:14 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | 0.1400 |  |
| Jogador 6 | 1-4 | 19:39:14 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | 0.6700 |  |
| Jogador 6 | 1-4 | 19:39:15 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rammus | 0.2200 |  |
| Jogador 6 | 1-4 | 19:39:15 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rammus | -0.3700 |  |
| Jogador 6 | 1-4 | 19:39:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-1 | 19:39:20 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rammus | -0.0400 |  |
| Jogador 6 | 2-1 | 19:39:21 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.3400 |  |
| Jogador 6 | 2-1 | 19:39:21 | MOVE Bench -> Board: Tristana (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 2-1 | 19:39:22 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | -0.7500 |  |
| Jogador 6 | 2-1 | 19:39:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 19:39:27 | MOVE Bench -> Board: Rammus (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Tristana | -0.2600 |  |
| Jogador 6 | 2-2 | 19:39:27 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Rammus | -0.4500 |  |
| Jogador 6 | 2-2 | 19:39:28 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Rammus | 1.0200 |  |
| Jogador 6 | 2-2 | 19:39:29 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Rammus | -0.4000 |  |
| Jogador 6 | 2-2 | 19:39:29 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Rammus | 0.0300 |  |
| Jogador 6 | 2-2 | 19:39:29 | MOVE Bench -> Board: Rammus (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Rammus | -0.3500 |  |
| Jogador 6 | 2-2 | 19:39:29 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Rammus | -0.4000 |  |
| Jogador 6 | 2-2 | 19:39:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Rammus | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-3 | 19:39:34 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | — | DA_18_Rammus | 0.0300 |  |
| Jogador 6 | 2-3 | 19:39:34 | MOVE Bench -> Board: Rammus (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | — | DA_18_Rammus | -0.7000 |  |
| Jogador 6 | 2-3 | 19:39:34 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | — | DA_18_Rammus | 0.0600 |  |
| Jogador 6 | 2-3 | 19:39:35 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Rammus | 0.0400 |  |
| Jogador 6 | 2-3 | 19:39:35 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Hecarim | -0.3500 |  |
| Jogador 6 | 2-3 | 19:39:36 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Hecarim | -0.4000 |  |
| Jogador 6 | 2-3 | 19:39:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Hecarim | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-4 | 19:39:41 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Rammus | 0.0300 |  |
| Jogador 6 | 2-4 | 19:39:41 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Hecarim | -0.3500 |  |
| Jogador 6 | 2-4 | 19:39:41 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Colosso | DA_18_Hecarim | -0.8800 |  |
| Jogador 6 | 2-4 | 19:39:42 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Hecarim | 0.3600 |  |
| Jogador 6 | 2-4 | 19:39:42 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Colosso | DA_18_Hecarim | -0.7000 |  |
| Jogador 6 | 2-4 | 19:39:42 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_18_Hecarim | 0.4000 |  |
| Jogador 6 | 2-4 | 19:39:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Hecarim | 0.0700 |  |
| Jogador 6 | 2-4 | 19:39:43 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Hecarim | 0.6300 |  |
| Jogador 6 | 2-4 | 19:39:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Hecarim | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-5 | 19:39:48 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 27 | 2 | Colosso | DA_18_Rammus | 0.9300 |  |
| Jogador 6 | 2-5 | 19:39:48 | MOVE Bench -> Board: Rammus (i:6.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 27 | 2 | Colosso | DA_18_Rammus | -0.5700 |  |
| Jogador 6 | 2-5 | 19:39:48 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 27 | 2 | Colosso | DA_18_Rammus | -0.3900 |  |
| Jogador 6 | 2-5 | 19:39:48 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 27 | 2 | Colosso | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 2-6 | 19:39:55 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Defendente | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 2-6 | 19:39:55 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 34 | 2 | Defendente | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 6 | 2-6 | 19:39:55 | VENDEU: Kog'Maw (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Defendente | DA_18_Rammus | -0.7000 |  |
| Jogador 6 | 2-6 | 19:39:56 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Defendente | DA_18_Rammus | -0.0400 |  |
| Jogador 6 | 2-7 | 19:40:02 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Defendente | DA_Fiddlesticks18 | 0.2700 |  |
| Jogador 6 | 2-7 | 19:40:02 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Defendente | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 6 | 2-7 | 19:40:02 | MOVE Bench -> Board: Rammus (i:6.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Defendente | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 6 | 2-7 | 19:40:03 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Fiddlesticks (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Defendente | DA_Fiddlesticks18 | -0.8600 |  |
| Jogador 6 | 2-7 | 19:40:03 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Defendente | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 6 | 2-7 | 19:40:04 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Defendente | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 6 | 3-1 | 19:40:09 | MOVE Bench -> Board: Rammus (i:6.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 4 | Defendente | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 6 | 3-1 | 19:40:09 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 4 | Defendente | DA_Fiddlesticks18 | -0.3500 |  |
| Jogador 6 | 3-1 | 19:40:10 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 4 | Defendente | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 6 | 3-1 | 19:40:10 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 4 | Defendente | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 6 | 3-2 | 19:40:16 | MOVE Bench -> Board: Rammus (i:6.0) <-> Fiddlesticks (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 63 | 5 | Defendente | DA_Fiddlesticks18 | -0.7700 |  |
| Jogador 6 | 3-2 | 19:40:16 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 63 | 5 | Defendente | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 6 | 3-2 | 19:40:17 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 63 | 5 | Defendente | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 6 | 3-3 | 19:40:24 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 74 | 5 | Defendente | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 6 | 3-3 | 19:40:24 | MOVE Bench -> Board: Rammus (i:6.0) <-> Fiddlesticks (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 74 | 5 | Defendente | DA_Fiddlesticks18 | -0.7700 |  |
| Jogador 6 | 3-3 | 19:40:24 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 74 | 5 | Defendente | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 6 | 3-4 | 19:40:31 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 85 | 5 | Defendente | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 6 | 3-4 | 19:40:31 | VENDEU: Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 87 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-4 | 19:40:32 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 85 | 5 | Defendente | DA_Fiddlesticks18 | 0.5200 |  |
| Jogador 6 | 3-4 | 19:40:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Defendente | DA_Fiddlesticks18 | 0.2200 |  |
| Jogador 6 | 3-4 | 19:40:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-4 | 19:40:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-4 | 19:40:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-4 | 19:40:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-4 | 19:40:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-4 | 19:40:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-4 | 19:40:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Defendente | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 6 | 3-5 | 19:40:38 | VENDEU: Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Defendente | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 6 | 3-5 | 19:40:38 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Defendente | DA_Fiddlesticks18 | 0.5100 |  |
| Jogador 6 | 3-5 | 19:40:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-5 | 19:40:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Defendente | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-5 | 19:40:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Defendente | DA_Fiddlesticks18 | 0.3100 |  |
| Jogador 6 | 3-5 | 19:40:40 | MOVE Bench -> Board: Caitlyn (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Defendente | DA_Fiddlesticks18 | -0.2200 |  |
| Jogador 6 | 3-5 | 19:40:41 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 5 | Defendente | DA_18_Caitlyn | 0.8700 |  |
| Jogador 6 | 3-5 | 19:40:41 | MOVE Bench -> Board: Caitlyn (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 5 | Defendente | DA_18_Caitlyn | 0.0400 |  |
| Jogador 6 | 3-5 | 19:40:42 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 5 | Defendente | DA_18_Caitlyn | -0.1600 |  |
| Jogador 6 | 3-6 | 19:40:46 | COMPROU: Gnar (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Defendente | DA_18_GnarSmall | 0.1400 |  |
| Jogador 6 | 3-6 | 19:40:46 | MOVE Bench -> Board: Gnar (i:10.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Defendente | DA_18_GnarSmall | -0.4700 |  |
| Jogador 6 | 3-6 | 19:40:47 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Defendente | DA_18_GnarSmall | -0.4000 |  |
| Jogador 6 | 3-6 | 19:40:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Defendente | DA_18_GnarSmall | -0.1700 |  |
| Jogador 6 | 3-6 | 19:40:51 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Defendente | DA_18_GnarSmall | 0.2400 |  |
| Jogador 6 | 3-7 | 19:40:55 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Defendente | DA_18_GnarSmall | 1.0100 |  |
| Jogador 6 | 3-7 | 19:40:55 | MOVE Bench -> Board: Rammus (i:12.0) <-> Gnar (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Defendente | DA_18_Rammus | 0.2300 |  |
| Jogador 6 | 3-7 | 19:40:55 | MOVE Bench -> Board: Gnar (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Defendente | DA_18_GnarSmall | 0.1000 |  |
| Jogador 6 | 3-7 | 19:40:56 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Defendente | DA_18_GnarSmall | 0.7400 |  |
| Jogador 6 | 3-7 | 19:40:56 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Gnar (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Defendente | DA_18_Rammus | -0.3100 |  |
| Jogador 6 | 3-7 | 19:40:56 | MOVE Bench -> Board: Gnar (i:10.0) <-> Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Defendente | DA_18_GnarSmall | -0.5200 |  |
| Jogador 6 | 3-7 | 19:40:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Defendente | DA_18_GnarSmall | -0.2400 |  |
| Jogador 6 | 3-7 | 19:41:00 | MOVE Bench -> Board: Rammus (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Defendente | DA_18_GnarSmall | 0.3900 |  |
| Jogador 6 | 4-1 | 19:41:03 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Defendente | DA_18_GnarSmall | 0.0700 |  |
| Jogador 6 | 4-1 | 19:41:04 | MOVE Bench -> Board: Soraka (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Defendente | DA_18_GnarSmall | 0.3500 |  |
| Jogador 6 | 4-1 | 19:41:04 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Defendente | DA_18_GnarSmall | 0.4100 |  |
| Jogador 6 | 4-1 | 19:41:04 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Defendente | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-1 | 19:41:05 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Defendente | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-1 | 19:41:05 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Defendente | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-1 | 19:41:05 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 58 | 5 | Defendente | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-1 | 19:41:06 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 54 | 5 | Defendente | DA_18_GnarSmall | 0.0400 |  |
| Jogador 6 | 4-1 | 19:41:06 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 50 | 5 | Defendente | DA_18_GnarSmall | 0.0400 |  |
| Jogador 6 | 4-1 | 19:41:08 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 46 | 5 | Defendente | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-1 | 19:41:08 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 46 | 5 | Defendente | DA_18_GnarSmall | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-2 | 19:41:11 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 4 | Defendente | DA_18_GnarSmall | -0.1900 |  |
| Jogador 6 | 4-2 | 19:41:13 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Defendente | DA_18_GnarSmall | -0.0800 |  |
| Jogador 6 | 4-2 | 19:41:13 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 44 | 4 | Defendente | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 19:41:13 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 40 | 4 | Defendente | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 19:41:13 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 36 | 4 | Defendente | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-2 | 19:41:14 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 32 | 4 | Defendente | DA_18_GnarSmall | 0.4500 |  |
| Jogador 6 | 4-2 | 19:41:14 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 28 | 4 | Defendente | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-2 | 19:41:14 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 24 | 4 | Defendente | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 19:41:15 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 20 | 4 | Defendente | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 19:41:15 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 16 | 4 | Defendente | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-2 | 19:41:15 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 16 | 4 | Defendente | DA_18_GnarSmall | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-3 | 19:41:19 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Defendente | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 19:41:19 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 16 | 1 | Defendente | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-3 | 19:41:19 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 1 | Defendente | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-3 | 19:41:20 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 11 | 1 | Defendente | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-3 | 19:41:20 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 7 | 1 | Defendente | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-3 | 19:41:20 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 3 | 1 | Defendente | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 19:41:21 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 1 | Defendente | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-3 | 19:41:24 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 3 | 1 | Defendente | DA_18_GnarSmall | 0.5800 |  |
| Jogador 6 | 4-4 | 19:41:29 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Defendente | DA_18_GnarSmall | 0.2900 |  |
| Jogador 6 | 4-4 | 19:41:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Defendente | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-4 | 19:41:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-4 | 19:41:30 | MOVE Bench -> Board: Sivir (i:8.0) <-> Caitlyn (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_GnarSmall | -0.4000 |  |
| Jogador 6 | 4-4 | 19:41:30 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-5 | 19:41:37 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Defendente | DA_18_GnarSmall | 0.2200 |  |
| Jogador 6 | 4-5 | 19:41:37 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_GnarSmall | 0.6400 |  |
| Jogador 6 | 4-5 | 19:41:38 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-6 | 19:41:45 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Defendente | DA_18_GnarSmall | -0.1700 |  |
| Jogador 6 | 4-6 | 19:41:45 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Defendente | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-7 | 19:41:54 | BIGORNA: escolheu componente TFT_Item_NegatronCloak | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Defendente | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-7 | 19:41:54 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Defendente | DA_18_Rammus | 0.2700 |  |
| Jogador 6 | 4-7 | 19:41:54 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-7 | 19:41:55 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_SparringGloves -> Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Defendente | DA_18_Rammus | 0.1500 |  |
| Jogador 6 | 4-7 | 19:41:55 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Defendente | DA_18_Rammus | -0.3400 |  |
| Jogador 6 | 4-7 | 19:41:55 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_Rammus | 0.2700 |  |
| Jogador 6 | 4-7 | 19:41:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_Rammus | -0.0500 |  |
| Jogador 6 | 5-1 | 19:42:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 5-1 | 19:42:05 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 5-1 | 19:42:05 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 5-1 | 19:42:05 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Defendente | DA_18_Rammus | -0.0500 |  |
| Jogador 7 | ? | 19:38:48 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 7 | ? | 19:38:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 7 | ? | 19:38:49 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6000 |  |
| Jogador 7 | ? | 19:38:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-1 | 19:38:54 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0800 |  |
| Jogador 7 | 1-1 | 19:38:55 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.7500 |  |
| Jogador 7 | 1-1 | 19:38:55 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.4700 |  |
| Jogador 7 | 1-1 | 19:38:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 1.0300 |  |
| Jogador 7 | 1-1 | 19:38:56 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.7500 |  |
| Jogador 7 | 1-1 | 19:38:56 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.1400 |  |
| Jogador 7 | 1-1 | 19:38:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-1 | 19:38:59 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 7 | 1-2 | 19:39:01 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.2200 |  |
| Jogador 7 | 1-2 | 19:39:01 | MOVE Bench -> Board: Elise (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | -0.2400 |  |
| Jogador 7 | 1-2 | 19:39:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 7 | 1-3 | 19:39:07 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | -0.8400 |  |
| Jogador 7 | 1-3 | 19:39:07 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | 1.0200 |  |
| Jogador 7 | 1-3 | 19:39:08 | MOVE Bench -> Board: Elise (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | -0.4000 |  |
| Jogador 7 | 1-3 | 19:39:08 | MOVE Bench -> Board: Elise (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | -0.3100 |  |
| Jogador 7 | 1-3 | 19:39:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 7 | 1-4 | 19:39:14 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Elise | -0.4000 |  |
| Jogador 7 | 1-4 | 19:39:14 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Elise | 0.1000 |  |
| Jogador 7 | 1-4 | 19:39:14 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Elise | 0.5600 |  |
| Jogador 7 | 1-4 | 19:39:15 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | 0.0900 |  |
| Jogador 7 | 1-4 | 19:39:15 | MOVE Bench -> Board: Alistar (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | -0.3500 |  |
| Jogador 7 | 1-4 | 19:39:16 | MOVE Bench -> Board: Elise (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | -0.0200 |  |
| Jogador 7 | 1-4 | 19:39:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 7 | 2-1 | 19:39:20 | MOVE Bench -> Board: Shen (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Elise | -0.3100 |  |
| Jogador 7 | 2-1 | 19:39:21 | MOVE Bench -> Board: Alistar (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Elise | -0.3500 |  |
| Jogador 7 | 2-1 | 19:39:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 7 | 2-2 | 19:39:27 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | — | DA_18_Alistar | -0.8100 |  |
| Jogador 7 | 2-2 | 19:39:27 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Alistar | 1.0200 |  |
| Jogador 7 | 2-2 | 19:39:28 | MOVE Bench -> Board: Alistar (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Alistar | -0.4000 |  |
| Jogador 7 | 2-2 | 19:39:29 | MOVE Bench -> Board: Alistar (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Alistar | -0.0200 |  |
| Jogador 7 | 2-2 | 19:39:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Alistar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-3 | 19:39:34 | MOVE Bench -> Board: Shen (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_18_Alistar | -0.3200 |  |
| Jogador 7 | 2-3 | 19:39:34 | MOVE Bench -> Board: Alistar (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_18_Alistar | -0.4000 |  |
| Jogador 7 | 2-3 | 19:39:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_18_Alistar | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-4 | 19:39:41 | MOVE Bench -> Board: Alistar (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Vanguarda | DA_18_Alistar | 0.0000 |  |
| Jogador 7 | 2-4 | 19:39:41 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Vanguarda | DA_18_Alistar | -0.3800 |  |
| Jogador 7 | 2-4 | 19:39:41 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Vanguarda | DA_18_Alistar | 0.3000 |  |
| Jogador 7 | 2-4 | 19:39:42 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Vanguarda | DA_18_Alistar | -0.3400 |  |
| Jogador 7 | 2-4 | 19:39:42 | MOVE Bench -> Board: Alistar (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Vanguarda | DA_18_Alistar | -0.4000 |  |
| Jogador 7 | 2-4 | 19:39:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Vanguarda | DA_18_Alistar | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-5 | 19:39:48 | MOVE Bench -> Board: Alistar (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 35 | 2 | Vanguarda | DA_18_Alistar | 0.0400 |  |
| Jogador 7 | 2-5 | 19:39:48 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 35 | 2 | Vanguarda | DA_18_Alistar | 0.3800 |  |
| Jogador 7 | 2-5 | 19:39:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 34 | 2 | Vanguarda | DA_18_Alistar | 0.9700 |  |
| Jogador 7 | 2-5 | 19:39:48 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Vanguarda | DA_18_Alistar | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-5 | 19:39:49 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 2 | Vanguarda | DA_18_Alistar | -0.1600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-5 | 19:39:50 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 2 | Vanguarda | DA_18_Alistar | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-5 | 19:39:50 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 2 | Vanguarda | DA_18_Alistar | -0.1600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-5 | 19:39:51 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Vanguarda | DA_18_Alistar | 0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-5 | 19:39:51 | MOVE Bench -> Board: Rakan (i:2.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Vanguarda | DA_18_Alistar | 0.0400 |  |
| Jogador 7 | 2-5 | 19:39:51 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Alistar (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Vanguarda | DA_18_Alistar | -0.3500 |  |
| Jogador 7 | 2-5 | 19:39:51 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Vanguarda | DA_18_Alistar | 0.0000 |  |
| Jogador 7 | 2-6 | 19:39:55 | MOVE Bench -> Board: Alistar (i:4.0) <-> Rakan (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 21 | 1 | Vanguarda | DA_18_Alistar | -0.3900 |  |
| Jogador 7 | 2-6 | 19:39:55 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 21 | 1 | Vanguarda | DA_18_Alistar | 0.6600 |  |
| Jogador 7 | 2-6 | 19:39:55 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | Vanguarda | DA_18_Rammus | -0.2400 |  |
| Jogador 7 | 2-6 | 19:39:56 | MOVE Bench -> Board: Rammus (i:6.0) <-> Alistar (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | Vanguarda | DA_18_Rammus | -0.3500 |  |
| Jogador 7 | 2-6 | 19:39:56 | MOVE Bench -> Board: Alistar (i:4.0) <-> Rakan (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | Vanguarda | DA_18_Rammus | -0.3600 |  |
| Jogador 7 | 2-6 | 19:39:56 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | Vanguarda | DA_18_Rammus | -0.0200 |  |
| Jogador 7 | 2-7 | 19:40:02 | VENDEU: Rakan (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Vanguarda | DA_18_Rammus | -0.8800 |  |
| Jogador 7 | 2-7 | 19:40:02 | COMPROU: Diana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Vanguarda | DA_18_Diana | 0.2400 |  |
| Jogador 7 | 2-7 | 19:40:02 | MOVE Bench -> Board: Diana (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Vanguarda | DA_18_Diana | 0.1100 |  |
| Jogador 7 | 2-7 | 19:40:03 | MOVE Bench -> Board: Rammus (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Vanguarda | DA_18_Diana | -0.6000 |  |
| Jogador 7 | 2-7 | 19:40:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Vanguarda | DA_18_Diana | -0.0900 |  |
| Jogador 7 | 2-7 | 19:40:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 2-7 | 19:40:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 1 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 2-7 | 19:40:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 1 | Vanguarda | DA_18_Diana | -0.0900 |  |
| Jogador 7 | 2-7 | 19:40:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 1 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 2-7 | 19:40:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 1 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 3-1 | 19:40:09 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Diana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Vanguarda | DA_18_Diana | -0.4100 |  |
| Jogador 7 | 3-1 | 19:40:09 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Vanguarda | DA_18_Diana | -0.0500 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 3-1 | 19:40:10 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Vanguarda | DA_18_Diana | -0.0500 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 3-1 | 19:40:10 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 3-2 | 19:40:16 | MOVE Bench -> Board: Diana (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Vanguarda | DA_18_Diana | 0.1000 |  |
| Jogador 7 | 3-2 | 19:40:16 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_18_Diana | 0.5600 |  |
| Jogador 7 | 3-2 | 19:40:17 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Vanguarda | DA_18_Diana | 0.1200 |  |
| Jogador 7 | 3-2 | 19:40:17 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 7 | 3-2 | 19:40:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-2 | 19:40:18 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-3 | 19:40:24 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 7 | 3-3 | 19:40:24 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Aphelios | -0.0400 |  |
| Jogador 7 | 3-3 | 19:40:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Aphelios | 0.7400 |  |
| Jogador 7 | 3-3 | 19:40:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Aphelios | 0.0000 |  |
| Jogador 7 | 3-4 | 19:40:31 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vanguarda | DA_18_Aphelios | -0.9100 |  |
| Jogador 7 | 3-4 | 19:40:31 | VENDEU: Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.3100 |  |
| Jogador 7 | 3-4 | 19:40:32 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Diana | 0.6500 |  |
| Jogador 7 | 3-4 | 19:40:33 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Vanguarda | DA_18_Alistar | 0.7600 |  |
| Jogador 7 | 3-4 | 19:40:33 | MOVE Bench -> Board: Alistar (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_18_Alistar | 0.3800 |  |
| Jogador 7 | 3-4 | 19:40:33 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_18_Alistar | 0.5500 |  |
| Jogador 7 | 3-4 | 19:40:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_18_Alistar | 0.0000 |  |
| Jogador 7 | 3-5 | 19:40:38 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Alistar | 0.1200 |  |
| Jogador 7 | 3-5 | 19:40:38 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Alistar | -0.2700 |  |
| Jogador 7 | 3-5 | 19:40:39 | COMPROU: Morgana (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Alistar | -0.0400 |  |
| Jogador 7 | 3-5 | 19:40:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Alistar | -0.0100 |  |
| Jogador 7 | 3-5 | 19:40:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vanguarda | DA_18_Alistar | 0.0000 |  |
| Jogador 7 | 3-6 | 19:40:46 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Vanguarda | DA_Sentinel18 | 0.8000 |  |
| Jogador 7 | 3-6 | 19:40:46 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-7 | 19:40:55 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Vanguarda | DA_Sentinel18 | -0.2300 |  |
| Jogador 7 | 3-7 | 19:40:55 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Vanguarda | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-7 | 19:40:55 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-1 | 19:41:03 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Vanguarda | DA_Sentinel18 | 0.2500 |  |
| Jogador 7 | 4-1 | 19:41:04 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-2 | 19:41:11 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Vanguarda | DA_Sentinel18 | 0.3900 |  |
| Jogador 7 | 4-2 | 19:41:13 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Vanguarda | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 4-2 | 19:41:13 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-2 | 19:41:13 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Sentinel18 | 0.7900 |  |
| Jogador 7 | 4-2 | 19:41:13 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-3 | 19:41:19 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Vanguarda | DA_Sentinel18 | -0.1900 |  |
| Jogador 7 | 4-3 | 19:41:19 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-3 | 19:41:19 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Vanguarda | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 4-3 | 19:41:20 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Vanguarda | DA_Sentinel18 | 0.8000 |  |
| Jogador 7 | 4-3 | 19:41:20 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Vanguarda | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-4 | 19:41:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-4 | 19:41:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-4 | 19:41:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-4 | 19:41:30 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Sentinel18 | -0.0500 |  |
| Jogador 8 | ? | 19:38:48 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 8 | ? | 19:38:48 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 8 | ? | 19:38:49 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 8 | ? | 19:38:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 8 | 1-1 | 19:38:54 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 8 | 1-1 | 19:38:55 | MOVE Bench -> Board: Leona (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.8200 |  |
| Jogador 8 | 1-1 | 19:38:55 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.5100 |  |
| Jogador 8 | 1-1 | 19:38:56 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 8 | 1-1 | 19:38:56 | MOVE Bench -> Board: Leona (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.8100 |  |
| Jogador 8 | 1-1 | 19:38:56 | MOVE Bench -> Board: Akali (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2500 |  |
| Jogador 8 | 1-1 | 19:38:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 8 | 1-1 | 19:38:59 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.1300 |  |
| Jogador 8 | 1-2 | 19:39:01 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 8 | 1-2 | 19:39:01 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 8 | 1-2 | 19:39:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 8 | 1-3 | 19:39:07 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.4300 |  |
| Jogador 8 | 1-3 | 19:39:07 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 1.1200 |  |
| Jogador 8 | 1-3 | 19:39:08 | MOVE Bench -> Board: Leona (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.2800 |  |
| Jogador 8 | 1-3 | 19:39:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 1-4 | 19:39:14 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | 0.3900 |  |
| Jogador 8 | 1-4 | 19:39:14 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | 0.2700 |  |
| Jogador 8 | 1-4 | 19:39:14 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Leona | 1.0400 |  |
| Jogador 8 | 1-4 | 19:39:15 | MOVE Bench -> Board: Leona (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Leona | -0.4000 |  |
| Jogador 8 | 1-4 | 19:39:15 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Leona | 0.5200 |  |
| Jogador 8 | 1-4 | 19:39:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-1 | 19:39:20 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Leona | 1.0400 |  |
| Jogador 8 | 2-1 | 19:39:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | -0.1200 |  |
| Jogador 8 | 2-1 | 19:39:21 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Leona | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-1 | 19:39:22 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Leona | 0.4900 |  |
| Jogador 8 | 2-1 | 19:39:22 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-2 | 19:39:27 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 2-2 | 19:39:27 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Leona | -0.4700 |  |
| Jogador 8 | 2-2 | 19:39:28 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Leona | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-2 | 19:39:29 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-3 | 19:39:34 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Leona | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-3 | 19:39:34 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Leona | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-3 | 19:39:34 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-4 | 19:39:41 | VENDEU: Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Defendente | DA_18_Leona | -0.8600 |  |
| Jogador 8 | 2-4 | 19:39:41 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Defendente | DA_18_Leona | 0.3200 |  |
| Jogador 8 | 2-4 | 19:39:41 | MOVE Bench -> Board: Rammus (i:6.0) <-> Leona (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Defendente | DA_18_Leona | -0.2400 |  |
| Jogador 8 | 2-4 | 19:39:42 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-5 | 19:39:48 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Defendente | DA_18_Leona | 0.5000 |  |
| Jogador 8 | 2-5 | 19:39:48 | COMPROU: Soraka (Custo 4 \| i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Defendente | DA_18_Leona | 0.0900 |  |
| Jogador 8 | 2-5 | 19:39:48 | MOVE Board -> Board: Leona (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Defendente | DA_18_Leona | 0.1700 |  |
| Jogador 8 | 2-5 | 19:39:48 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Defendente | DA_18_Leona | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-5 | 19:39:49 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-6 | 19:39:55 | VENDEU: Soraka (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 11 | 0 | Defendente | DA_18_Leona | -0.3200 |  |
| Jogador 8 | 2-6 | 19:39:55 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Defendente | DA_18_Leona | 0.2500 |  |
| Jogador 8 | 2-6 | 19:39:55 | MOVE Bench -> Board: Shen (i:4.0) <-> Cassiopeia (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | Defendente | DA_18_Leona | -0.1000 |  |
| Jogador 8 | 2-6 | 19:39:56 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Defendente | DA_18_Leona | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-6 | 19:39:56 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Defendente | DA_18_Leona | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-6 | 19:39:56 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-7 | 19:40:02 | VENDEU: Cassiopeia (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | Defendente | DA_18_Leona | -0.3400 |  |
| Jogador 8 | 2-7 | 19:40:02 | COMPROU: Lillia (Custo 4 \| i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Defendente | DA_18_Leona | 0.1200 |  |
| Jogador 8 | 2-7 | 19:40:02 | MOVE Bench -> Board: Lillia (i:8.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Defendente | DA_18_Leona | -0.5400 |  |
| Jogador 8 | 2-7 | 19:40:03 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Defendente | DA_18_Leona | -0.0500 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-7 | 19:40:03 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 3-1 | 19:40:09 | VENDEU: Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | Defendente | DA_18_Leona | -0.4200 |  |
| Jogador 8 | 3-1 | 19:40:09 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Defendente | DA_18_Leona | 0.1400 |  |
| Jogador 8 | 3-1 | 19:40:10 | MOVE Bench -> Board: Shen (i:4.0) <-> Lillia (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Defendente | DA_18_Leona | -0.2800 |  |
| Jogador 8 | 3-1 | 19:40:10 | MOVE Bench -> Board: Lillia (i:8.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Leona | -0.3000 |  |
| Jogador 8 | 3-1 | 19:40:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 3-2 | 19:40:16 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 3-2 | 19:40:16 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 3-2 | 19:40:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Leona | 0.0800 |  |
| Jogador 8 | 3-2 | 19:40:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 3-2 | 19:40:21 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Leona | 0.5300 |  |
| Jogador 8 | 3-3 | 19:40:24 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Leona | -0.2500 |  |
| Jogador 8 | 3-3 | 19:40:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 3-3 | 19:40:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 3-4 | 19:40:31 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Leona | -0.3700 |  |
| Jogador 8 | 3-4 | 19:40:31 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Leona | 0.7300 |  |
| Jogador 8 | 3-4 | 19:40:32 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Leona | -0.4000 |  |
| Jogador 8 | 3-4 | 19:40:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 3-4 | 19:40:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 3-5 | 19:40:38 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Leona | -0.8400 |  |
| Jogador 8 | 3-5 | 19:40:38 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Leona | 0.2100 |  |
| Jogador 8 | 3-5 | 19:40:39 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Leona | 0.1500 |  |
| Jogador 8 | 3-5 | 19:40:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 3-5 | 19:40:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 3-6 | 19:40:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 3-6 | 19:40:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 3-6 | 19:40:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 3-7 | 19:40:55 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_ChainVest -> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Leona | 0.1700 |  |
| Jogador 8 | 3-7 | 19:40:55 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 3-7 | 19:40:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 4-1 | 19:41:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 4-2 | 19:41:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Defendente | DA_18_Leona | -0.1100 |  |
| Jogador 8 | 4-3 | 19:41:19 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Defendente | DA_18_Leona | 0.8700 |  |
| Jogador 8 | 4-3 | 19:41:19 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Defendente | DA_18_Leona | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-4 | 19:41:29 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Defendente | DA_18_Leona | 0.9100 |  |
| Jogador 8 | 4-4 | 19:41:29 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 2 | Defendente | DA_18_Leona | 0.8400 |  |
| Jogador 8 | 4-4 | 19:41:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 19 | 2 | Defendente | DA_18_Leona | -0.1100 |  |
| Jogador 8 | 4-4 | 19:41:30 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 15 | 2 | Defendente | DA_18_Leona | -0.0300 |  |
| Jogador 8 | 4-4 | 19:41:30 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 11 | 2 | Defendente | DA_18_Leona | -0.0300 |  |
| Jogador 8 | 4-4 | 19:41:30 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 7 | 2 | Defendente | DA_18_Leona | -0.1100 |  |
| Jogador 8 | 4-4 | 19:41:31 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 2 | Defendente | DA_18_Leona | 0.0300 |  |
| Jogador 8 | 4-4 | 19:41:31 | MOVE Bench -> Board: Tristana (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 2 | Defendente | DA_18_Leona | -0.6500 |  |
| Jogador 8 | 4-4 | 19:41:31 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 3 | 2 | Defendente | DA_18_Leona | 0.4000 |  |
| Jogador 8 | 4-4 | 19:41:33 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 2 | Defendente | DA_18_Leona | -0.4000 |  |
| Jogador 8 | 4-4 | 19:41:33 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 2 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 4-5 | 19:41:37 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Defendente | DA_18_Leona | -0.2100 |  |
| Jogador 8 | 4-5 | 19:41:37 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Defendente | DA_18_Leona | 0.8400 |  |
| Jogador 8 | 4-5 | 19:41:38 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 4-5 | 19:41:38 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Defendente | DA_18_Leona | 0.2900 |  |
| Jogador 8 | 4-5 | 19:41:38 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 4-5 | 19:41:38 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Defendente | DA_18_Leona | -0.1100 |  |
| Jogador 8 | 4-5 | 19:41:39 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Defendente | DA_18_Leona | -0.3200 |  |
| Jogador 8 | 4-5 | 19:41:39 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Defendente | DA_18_Leona | -0.4000 |  |
| Jogador 8 | 4-5 | 19:41:39 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 4-5 | 19:41:42 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Defendente | DA_18_Leona | 0.2200 |  |
| Jogador 8 | 4-6 | 19:41:45 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Defendente | DA_18_Leona | 0.1400 |  |
| Jogador 8 | 4-6 | 19:41:45 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_Leona | 0.0300 |  |
| Jogador 8 | 4-6 | 19:41:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_Leona | -0.0500 |  |
| Jogador 8 | 4-7 | 19:41:54 | BIGORNA: escolheu componente TFT_Item_NegatronCloak | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Defendente | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 4-7 | 19:41:54 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Defendente | DA_18_Leona | 0.5300 |  |
| Jogador 8 | 4-7 | 19:41:54 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_Leona | -0.0800 |  |
| Jogador 8 | 4-7 | 19:41:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_Leona | -0.0500 |  |
| Jogador 8 | 5-1 | 19:42:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 5-1 | 19:42:05 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 5-1 | 19:42:05 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 5-1 | 19:42:05 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_18_Leona | -0.0500 |  |
| Jogador 8 | 5-2 | 19:42:11 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 5-2 | 19:42:12 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 5-2 | 19:42:12 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Defendente | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 5-2 | 19:42:12 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Defendente | DA_18_Leona | 0.0600 |  |
| Jogador 8 | 5-2 | 19:42:12 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Defendente | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 8 | 5-2 | 19:42:13 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 8 | 5-2 | 19:42:13 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 8 | 5-2 | 19:42:17 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Defendente | DA_Fiddlesticks18 | 0.4500 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 24 | 25 | 125 | 24 | 8 | 122 | 9 | 5 |
| Jogador 2 | 38 | 57 | 285 | 38 | 28 | 224 | 19 | 22 |
| Jogador 3 | 26 | 27 | 135 | 26 | 16 | 135 | 17 | 13 |
| Jogador 4 | 31 | 36 | 180 | 31 | 14 | 135 | 9 | 7 |
| Jogador 5 | 38 | 45 | 225 | 38 | 28 | 208 | 15 | 6 |
| Jogador 6 | 27 | 34 | 170 | 27 | 17 | 158 | 20 | 4 |
| Jogador 7 | 23 | 28 | 140 | 23 | 13 | 118 | 12 | 3 |
| Jogador 8 | 28 | 36 | 180 | 28 | 11 | 130 | 4 | 5 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 122 | 122 | 122 | 0 | 121 | 0 | 122 | 122 | 122 | 35/20 |
| Jogador 2 | 224 | 224 | 224 | 0 | 220 | 0 | 224 | 224 | 224 | 67/52 |
| Jogador 3 | 135 | 135 | 135 | 0 | 133 | 0 | 135 | 135 | 135 | 36/22 |
| Jogador 4 | 135 | 135 | 135 | 0 | 133 | 0 | 135 | 135 | 135 | 30/14 |
| Jogador 5 | 208 | 208 | 208 | 0 | 204 | 0 | 208 | 208 | 208 | 56/43 |
| Jogador 6 | 158 | 158 | 158 | 0 | 156 | 0 | 158 | 158 | 158 | 32/16 |
| Jogador 7 | 118 | 118 | 118 | 0 | 118 | 0 | 118 | 118 | 118 | 27/12 |
| Jogador 8 | 130 | 130 | 130 | 0 | 128 | 0 | 130 | 130 | 130 | 30/15 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +a8111a04-3067-4ce6-9a4b-4f5bb205f413 / -— |
| Jogador 1 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.07094134390354156 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0420212745666504 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0014999653212726116 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 30 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.1686171442270279 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30755534768104553 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6227911710739136 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 33 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 54 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16633445024490356 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 55 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 81 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4018702208995819 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 1-4 | 82 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0382823944091797 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 83 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 84 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 101 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07907812297344208 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 106 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.11736261844635 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -a8111a04-3067-4ce6-9a4b-4f5bb205f413,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-1 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41388604044914246 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 108 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.21894723176956177 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14950180053710938 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5427979826927185 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 111 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 132 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3589516878128052 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 133 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08842112869024277 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27923583984375 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 135 | SELL | STABILIZE | 95.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47118350863456726 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 2-2 | 136 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0168670415878296 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 137 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4412292242050171 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 138 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25109124183654785 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 139 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 159 | SELL | STABILIZE | 89.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7219718098640442 | 0.0 | 0.0 | +— / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f |
| Jogador 1 | 2-3 | 160 | BUY | STABILIZE | 89.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.939193844795227 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -— |
| Jogador 1 | 2-3 | 161 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 162 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8823375105857849 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 163 | PASS | STABILIZE | 89.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 182 | SELL | SLOWROLL | 82.0 | 5 | 14 | 1 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5027214288711548 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 2-4 | 183 | BUY | SLOWROLL | 82.0 | 5 | 17 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28681090474128723 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 184 | MOVE_BENCH | SLOWROLL | 82.0 | 5 | 14 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3919597864151001 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 185 | BUY | SLOWROLL | 82.0 | 5 | 14 | 1 | 22.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16825897991657257 | 0.0 | 0.0 | +8c5a0cda-86da-4f36-bee3-c2eae934e263 / -— |
| Jogador 1 | 2-4 | 186 | MOVE_BENCH | SLOWROLL | 82.0 | 5 | 12 | 1 | 22.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30786895751953125 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 187 | BUY_XP | SLOWROLL | 82.0 | 5 | 12 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 188 | BUY_XP | SLOWROLL | 82.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 189 | BUY_XP | SLOWROLL | 82.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 190 | PASS | SLOWROLL | 82.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 203 | SELL | SLOWROLL | 82.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44605880975723267 | 0.0 | 0.0 | +— / -d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 2-5 | 204 | BUY | SLOWROLL | 82.0 | 5 | 9 | 0 | 20.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3220766484737396 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 1 | 2-5 | 205 | MOVE_BENCH | SLOWROLL | 82.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07333209365606308 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 206 | SELL | SLOWROLL | 82.0 | 5 | 6 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4569375813007355 | 0.0 | 0.0 | +— / -8c5a0cda-86da-4f36-bee3-c2eae934e263 |
| Jogador 1 | 2-5 | 207 | BUY | SLOWROLL | 82.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2541710436344147 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 208 | BUY_XP | SLOWROLL | 82.0 | 5 | 6 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 209 | PASS | SLOWROLL | 82.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 226 | MOVE_BENCH | SLOWROLL | 76.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34836649894714355 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 227 | MOVE_BENCH | SLOWROLL | 76.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5579330325126648 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 228 | BUY | FAST8 | 76.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2376679927110672 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 229 | SELL | FAST8 | 76.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.733522891998291 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 2-6 | 230 | BUY | FAST8 | 76.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9678201079368591 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -— |
| Jogador 1 | 2-6 | 231 | BUY_XP | FAST8 | 76.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 232 | PASS | FAST8 | 76.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 245 | BUY_XP | FAST8 | 76.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 246 | BUY_XP | FAST8 | 76.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 247 | PASS | FAST8 | 76.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 266 | SELL | FAST8 | 76.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8457484841346741 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 3-1 | 267 | BUY | FAST8 | 76.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.14367353916168213 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 268 | MOVE_BENCH | FAST8 | 76.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7338952422142029 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 269 | BUY_XP | FAST8 | 76.0 | 6 | 4 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 270 | PASS | FAST8 | 76.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 287 | SELL | FAST8 | 76.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4165768623352051 | 0.0 | 0.0 | +— / -f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-2 | 288 | BUY | FAST8 | 76.0 | 6 | 9 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.28451910614967346 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 289 | BUY_XP | FAST8 | 76.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 290 | PASS | FAST8 | 76.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 306 | SELL | FAST8 | 65.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2755437195301056 | 0.0 | 0.0 | +— / -145f7470-8c0f-4957-b8d6-97939ddaeba1 |
| Jogador 1 | 3-3 | 307 | BUY | FAST8 | 65.0 | 6 | 10 | 1 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6539347171783447 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 308 | BUY_XP | FAST8 | 65.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 309 | PASS | FAST8 | 65.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 328 | BUY_XP | FAST8 | 65.0 | 6 | 9 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09759999811649323 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 329 | MOVE_BENCH | FAST8 | 65.0 | 7 | 5 | 0 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5476402044296265 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 330 | BUY | FAST8 | 65.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15776634216308594 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 331 | PASS | FAST8 | 65.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 349 | SELL | FAST8 | 65.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09087692201137543 | 0.0 | 0.0 | +— / -0450963e-c7e2-4ff5-a2f5-09e65fa63527 |
| Jogador 1 | 3-5 | 350 | BUY | FAST8 | 65.0 | 7 | 10 | 1 | 34.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6839126944541931 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -0c9ac713-08bd-4fa7-a94a-2ab70d7815ff,c30e7bdb-41d6-423c-9d7d-2e146472e724 |
| Jogador 1 | 3-5 | 351 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 7 | 0 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14760024845600128 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 352 | MOVE_BENCH | FAST8 | 65.0 | 7 | 7 | 0 | 28.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32266607880592346 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 353 | BUY | FAST8 | 65.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.18986377120018005 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -— |
| Jogador 1 | 3-5 | 354 | MOVE_BENCH | FAST8 | 65.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4360494911670685 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 355 | BUY_XP | FAST8 | 65.0 | 7 | 5 | 0 | 38.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 356 | PASS | FAST8 | 65.0 | 7 | 1 | 0 | 38.0 | Colosso/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 365 | BUY | FAST8 | 54.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7658941149711609 | 0.0 | 0.0 | +da5abe09-7f54-4361-8d82-84427a9da9e1 / -7aea963f-f0a4-4fa2-8da0-cc5eb260f665,ff10e482-7085-4e73-8a0c-fdd3f4938128 |
| Jogador 1 | 3-6 | 366 | MOVE_BENCH | FAST8 | 54.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36269068717956543 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 367 | MOVE_BENCH | FAST8 | 54.0 | 7 | 4 | 0 | 26.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4905782639980316 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 368 | BUY | FAST8 | 54.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5098370909690857 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 369 | MOVE_BENCH | FAST8 | 54.0 | 7 | 1 | 0 | 38.0 | Colosso/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4264805316925049 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 370 | PASS | FAST8 | 54.0 | 7 | 1 | 0 | 44.0 | Colosso/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 382 | BUY | FAST8 | 43.0 | 7 | 7 | 0 | 44.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04669827222824097 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 383 | MOVE_BENCH | FAST8 | 43.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5329359769821167 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 384 | MOVE_BENCH | FAST8 | 43.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14719907939434052 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 385 | MOVE_BENCH | FAST8 | 43.0 | 7 | 2 | 0 | 50.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2124243676662445 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 386 | MOVE_BENCH | FAST8 | 43.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20928922295570374 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 387 | PASS | FAST8 | 43.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 402 | BUY | FAST8 | 43.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2139725536108017 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 403 | CRAFT_AND_EQUIP | FAST8 | 43.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1501973271369934 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 404 | BUY_XP | FAST8 | 43.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 405 | PASS | FAST8 | 43.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 422 | BUY | FAST8 | 43.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7391344904899597 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -7c218f01-e884-46da-8a1a-2d2db27a5ff1,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-2 | 423 | MOVE_BENCH | FAST8 | 43.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3112167716026306 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 424 | MOVE_BENCH | FAST8 | 43.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21026164293289185 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 425 | PASS | FAST8 | 43.0 | 7 | 4 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 434 | MOVE_BENCH | FAST8 | 43.0 | 7 | 4 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6717262864112854 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 440 | BUY | STABILIZE | 31.0 | 7 | 9 | 0 | 54.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30439308285713196 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 1 | 4-3 | 441 | PASS | STABILIZE | 31.0 | 7 | 6 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 452 | BUY | STABILIZE | 18.0 | 7 | 12 | 1 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11345186084508896 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 1 | 4-4 | 453 | BUY | STABILIZE | 18.0 | 7 | 9 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03643636405467987 | 0.0 | 0.0 | +fcd8f4bf-7e1f-42b3-a989-5b3683394c89 / -— |
| Jogador 1 | 4-4 | 454 | PASS | STABILIZE | 18.0 | 7 | 6 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 472 | BUY | STABILIZE | 18.0 | 7 | 12 | 1 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2220337688922882 | 0.0 | 0.0 | +9d2d95f2-c079-43eb-a4cd-37b224a473a8 / -— |
| Jogador 1 | 4-5 | 473 | BUY | STABILIZE | 18.0 | 7 | 8 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14177751541137695 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 1 | 4-5 | 474 | REROLL | STABILIZE | 18.0 | 7 | 4 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 475 | BUY | STABILIZE | 18.0 | 7 | 2 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04489709064364433 | 0.0 | 0.0 | +5c43307a-6d61-4493-a1ed-cb428d79a254 / -— |
| Jogador 1 | 4-5 | 476 | PASS | STABILIZE | 18.0 | 7 | 0 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 491 | BUY | ALL_IN | 5.0 | 7 | 6 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22739756107330322 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -— |
| Jogador 1 | 4-6 | 492 | BUY | ALL_IN | 5.0 | 7 | 3 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2739914059638977 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -— |
| Jogador 1 | 4-6 | 493 | PASS | ALL_IN | 5.0 | 7 | 0 | 0 | 54.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3124316334724426 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5844191908836365 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.07094134390354156 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0014999653212726116 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 30 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 54 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.13341598212718964 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5813812017440796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 56 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 81 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2743709981441498 | 0.0 | 0.0 | +9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 / -— |
| Jogador 2 | 1-4 | 82 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30002355575561523 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3314823508262634 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3553676903247833 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31550827622413635 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 110 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 132 | BUY_XP | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 133 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 134 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6263140439987183 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 135 | PASS | SLOWROLL | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 159 | BUY | SLOWROLL | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20561787486076355 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 160 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 5 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03437422960996628 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 161 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 162 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 182 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.509073793888092 | 0.0 | 0.0 | +— / -94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 2-4 | 183 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3264397978782654 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 184 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2548281252384186 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 185 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2560839056968689 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 186 | PASS | STABILIZE | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 203 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 22.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8646460175514221 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 204 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1384790539741516 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 205 | PASS | STABILIZE | 100.0 | 5 | 12 | 1 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 226 | SELL | STABILIZE | 95.0 | 5 | 18 | 1 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3904595971107483 | 0.0 | 0.0 | +— / -9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 |
| Jogador 2 | 2-6 | 227 | BUY | STABILIZE | 95.0 | 5 | 20 | 2 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2084461748600006 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 228 | BUY_XP | STABILIZE | 95.0 | 5 | 17 | 1 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 229 | BUY_XP | STABILIZE | 95.0 | 5 | 13 | 1 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07040499895811081 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 230 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 9 | 0 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3540835976600647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 231 | BUY | FAST8 | 95.0 | 6 | 9 | 0 | 30.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.332420289516449 | 0.0 | 0.0 | +8ea1c095-e10b-46d0-8097-a70a211e2881 / -— |
| Jogador 2 | 2-6 | 232 | BUY_XP | FAST8 | 95.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 233 | BUY_XP | FAST8 | 95.0 | 6 | 4 | 0 | 30.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 234 | PASS | FAST8 | 95.0 | 6 | 0 | 0 | 30.0 | Florescer/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 245 | SELL | FAST8 | 88.0 | 6 | 6 | 0 | 30.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5005999803543091 | 0.0 | 0.0 | +— / -8ea1c095-e10b-46d0-8097-a70a211e2881 |
| Jogador 2 | 2-7 | 246 | BUY | FAST8 | 88.0 | 6 | 7 | 0 | 30.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06001240015029907 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 247 | MOVE_BENCH | FAST8 | 88.0 | 6 | 3 | 0 | 30.0 | Florescer/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24466738104820251 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 248 | PASS | FAST8 | 88.0 | 6 | 3 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 266 | SELL | FAST8 | 88.0 | 6 | 9 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3380776047706604 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 3-1 | 267 | BUY | FAST8 | 88.0 | 6 | 12 | 1 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6521003246307373 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 268 | MOVE_BENCH | FAST8 | 88.0 | 6 | 9 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09449122101068497 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 269 | BUY_XP | FAST8 | 88.0 | 6 | 9 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 270 | BUY_XP | FAST8 | 88.0 | 6 | 5 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 271 | PASS | FAST8 | 88.0 | 6 | 1 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 287 | BUY_XP | FAST8 | 88.0 | 6 | 7 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 288 | PASS | FAST8 | 88.0 | 6 | 3 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 306 | SELL | FAST8 | 88.0 | 6 | 10 | 1 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003295564092695713 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 3-3 | 307 | BUY | FAST8 | 88.0 | 6 | 13 | 1 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.025770612061023712 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 308 | BUY_XP | FAST8 | 88.0 | 6 | 9 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 309 | BUY_XP | FAST8 | 88.0 | 6 | 5 | 0 | 32.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08229999989271164 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 310 | MOVE_BENCH | FAST8 | 88.0 | 7 | 1 | 0 | 32.0 | Florescer/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46461817622184753 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 311 | PASS | FAST8 | 88.0 | 7 | 1 | 0 | 40.0 | Florescer/DA_18_Lillia | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 328 | BUY | FAST8 | 88.0 | 7 | 8 | 0 | 40.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.728515625 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 329 | SELL | FAST8 | 88.0 | 7 | 5 | 0 | 40.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1073476076126099 | 0.0 | 0.0 | +— / -ff0d9869-c346-4210-be85-1e802a25dd8b |
| Jogador 2 | 3-4 | 330 | BUY | FAST8 | 88.0 | 7 | 8 | 0 | 40.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.728537917137146 | 0.0 | 0.0 | +a15ff9dc-bf8a-49e0-9893-f92a212263d8 / -— |
| Jogador 2 | 3-4 | 331 | MOVE_BENCH | FAST8 | 88.0 | 7 | 5 | 0 | 40.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041763786226511 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 332 | BUY_XP | FAST8 | 88.0 | 7 | 5 | 0 | 42.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 333 | MOVE_BENCH | FAST8 | 88.0 | 7 | 1 | 0 | 42.0 | Florescer/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45070308446884155 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 334 | PASS | FAST8 | 88.0 | 7 | 1 | 0 | 44.0 | Florescer/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 349 | BUY_XP | FAST8 | 88.0 | 7 | 7 | 0 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 350 | PASS | FAST8 | 88.0 | 7 | 3 | 0 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 365 | SELL | FAST8 | 88.0 | 7 | 10 | 1 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5093504190444946 | 0.0 | 0.0 | +— / -292ef825-d326-4dd8-9c42-c47cfc62116f |
| Jogador 2 | 3-6 | 366 | BUY | FAST8 | 88.0 | 7 | 11 | 1 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6407794952392578 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -— |
| Jogador 2 | 3-6 | 367 | SELL | FAST8 | 88.0 | 7 | 9 | 0 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0102922916412354 | 0.0 | 0.0 | +— / -63304cf5-4aa7-473e-9bfb-ec04cd68ebbd |
| Jogador 2 | 3-6 | 368 | BUY | FAST8 | 88.0 | 7 | 11 | 1 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02531181275844574 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 369 | BUY_XP | FAST8 | 88.0 | 7 | 7 | 0 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 370 | PASS | FAST8 | 88.0 | 7 | 3 | 0 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 382 | SELL | FAST8 | 88.0 | 7 | 11 | 1 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018353845924139023 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 3-7 | 383 | BUY | FAST8 | 88.0 | 7 | 15 | 1 | 44.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7216072082519531 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 384 | MOVE_BENCH | FAST8 | 88.0 | 7 | 11 | 1 | 44.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 385 | MOVE_BENCH | FAST8 | 88.0 | 7 | 11 | 1 | 44.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40146496891975403 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 386 | PASS | FAST8 | 88.0 | 7 | 11 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 402 | SELL | FAST8 | 88.0 | 7 | 19 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7521911859512329 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 2 | 4-1 | 403 | BUY | FAST8 | 88.0 | 7 | 22 | 2 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07224178314208984 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 404 | SELL | FAST8 | 88.0 | 7 | 19 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23487743735313416 | 0.0 | 0.0 | +— / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164 |
| Jogador 2 | 4-1 | 405 | BUY | FAST8 | 88.0 | 7 | 22 | 2 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.33888718485832214 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 406 | BUY_XP | FAST8 | 88.0 | 7 | 18 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019249999895691872 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 407 | BUY_XP | FAST8 | 88.0 | 7 | 14 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019249999895691872 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 408 | BUY_XP | FAST8 | 88.0 | 7 | 10 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 409 | BUY_XP | FAST8 | 88.0 | 7 | 6 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 410 | PASS | FAST8 | 88.0 | 7 | 2 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 422 | SELL | FAST8 | 88.0 | 7 | 11 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3546615242958069 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-2 | 423 | BUY | FAST8 | 88.0 | 7 | 15 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24977973103523254 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 2 | 4-2 | 424 | BUY_XP | FAST8 | 88.0 | 7 | 14 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019249999895691872 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 425 | BUY_XP | FAST8 | 88.0 | 7 | 10 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 426 | BUY_XP | FAST8 | 88.0 | 7 | 6 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 427 | PASS | FAST8 | 88.0 | 7 | 2 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 440 | BUY_XP | FAST8 | 88.0 | 7 | 11 | 1 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025206249207258224 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 441 | SELL | WINSTREAK | 88.0 | 8 | 7 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49538856744766235 | 0.0 | 0.0 | +— / -c617e958-b482-40ce-ab24-acff4dc48bc0 |
| Jogador 2 | 4-3 | 442 | BUY | WINSTREAK | 88.0 | 8 | 8 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22958718240261078 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 2 | 4-3 | 443 | SELL | WINSTREAK | 88.0 | 8 | 5 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7041550278663635 | 0.0 | 0.0 | +— / -104aaac3-252c-4c1b-9ad8-fc10a35c6cda |
| Jogador 2 | 4-3 | 444 | BUY | WINSTREAK | 88.0 | 8 | 8 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03038870170712471 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -— |
| Jogador 2 | 4-3 | 445 | BUY_XP | WINSTREAK | 88.0 | 8 | 6 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 446 | PASS | WINSTREAK | 88.0 | 8 | 2 | 0 | 46.0 | Florescer/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 452 | BUY | WINSTREAK | 88.0 | 8 | 11 | 1 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04209274426102638 | 0.0 | 0.0 | +30d2995a-d9b8-4424-af46-8766734e440c / -— |
| Jogador 2 | 4-4 | 453 | SELL | WINSTREAK | 88.0 | 8 | 8 | 0 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23407691717147827 | 0.0 | 0.0 | +— / -30d2995a-d9b8-4424-af46-8766734e440c |
| Jogador 2 | 4-4 | 454 | BUY | WINSTREAK | 88.0 | 8 | 11 | 1 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13840173184871674 | 0.0 | 0.0 | +d974e68a-e978-4335-8827-a94a9219be58 / -— |
| Jogador 2 | 4-4 | 455 | PASS | WINSTREAK | 88.0 | 8 | 8 | 0 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 472 | BUY | WINSTREAK | 88.0 | 8 | 16 | 1 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28599873185157776 | 0.0 | 0.0 | +7643f027-a90f-4f3a-8b4c-7be4cba17f95 / -— |
| Jogador 2 | 4-5 | 473 | BUY | WINSTREAK | 88.0 | 8 | 12 | 1 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05781467631459236 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 2 | 4-5 | 474 | BUY_XP | WINSTREAK | 88.0 | 8 | 8 | 0 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 475 | BUY_XP | WINSTREAK | 88.0 | 8 | 4 | 0 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 476 | PASS | WINSTREAK | 88.0 | 8 | 0 | 0 | 50.0 | Adaptador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 491 | BUY | WINSTREAK | 88.0 | 8 | 9 | 0 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16531626880168915 | 0.0 | 0.0 | +5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 / -— |
| Jogador 2 | 4-6 | 492 | PASS | WINSTREAK | 88.0 | 8 | 8 | 0 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 509 | BUY | WINSTREAK | 88.0 | 8 | 17 | 1 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8105900883674622 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 2 | 4-7 | 510 | PASS | WINSTREAK | 88.0 | 8 | 15 | 1 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 522 | ANVIL_CHOICE | WINSTREAK | 88.0 | 8 | 24 | 2 | 50.0 | Adaptador/DA_18_Lillia | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 523 | BUY | WINSTREAK | 88.0 | 8 | 24 | 2 | 50.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05212433636188507 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -— |
| Jogador 2 | 5-1 | 524 | BUY | WINSTREAK | 88.0 | 8 | 19 | 1 | 50.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.01494300551712513 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 2 | 5-1 | 525 | BUY | WINSTREAK | 88.0 | 8 | 16 | 1 | 50.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21365050971508026 | 0.0 | 0.0 | +79b461e3-2c4f-40a2-b967-e0b6d5248bf6 / -— |
| Jogador 2 | 5-1 | 526 | CRAFT_AND_EQUIP | WINSTREAK | 88.0 | 8 | 13 | 1 | 50.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08322051912546158 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 527 | PASS | WINSTREAK | 88.0 | 8 | 13 | 1 | 50.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 540 | BUY | ECON | 72.0 | 8 | 19 | 1 | 50.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44783827662467957 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 2 | 5-2 | 541 | SELL | ECON | 72.0 | 8 | 15 | 1 | 50.0 | Adaptador/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.066600002348423 | 0.0 | 0.0 | +— / -79b461e3-2c4f-40a2-b967-e0b6d5248bf6 |
| Jogador 2 | 5-2 | 542 | BUY | ECON | 72.0 | 8 | 18 | 1 | 50.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7637080550193787 | 0.0 | 0.0 | +33e9808b-2f92-49e7-ac35-1f6f9388edef / -6538f28f-845f-4f45-92bf-120931553bec,d381c462-a17f-4192-b694-66a7c3aaee4f |
| Jogador 2 | 5-2 | 543 | BUY | ECON | 72.0 | 8 | 16 | 1 | 46.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21383942663669586 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 2 | 5-2 | 544 | PASS | ECON | 72.0 | 8 | 13 | 1 | 46.0 | Adaptador/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 552 | BUY | ECON | 72.0 | 8 | 19 | 1 | 52.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7260370254516602 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -— |
| Jogador 2 | 5-3 | 553 | SELL | ECON | 72.0 | 8 | 15 | 1 | 52.0 | Adaptador/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06807692348957062 | 0.0 | 0.0 | +— / -986fbe1e-1826-4be7-a5d6-410a4c0a3f2f |
| Jogador 2 | 5-3 | 554 | BUY | ECON | 72.0 | 8 | 18 | 1 | 52.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42118901014328003 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 2 | 5-3 | 555 | REROLL | ECON | 72.0 | 8 | 16 | 1 | 52.0 | Adaptador/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 556 | SELL | ECON | 72.0 | 8 | 14 | 1 | 52.0 | Adaptador/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3223538398742676 | 0.0 | 0.0 | +— / -0c5adb43-b194-486e-b59c-c0f3b5479d40 |
| Jogador 2 | 5-3 | 557 | BUY | ECON | 72.0 | 8 | 16 | 1 | 52.0 | Adaptador/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7639380097389221 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -8c364966-f97c-4f54-b087-ddd182a9f8ea,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 5-3 | 558 | MOVE_BENCH | ECON | 72.0 | 8 | 13 | 1 | 40.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1984865665435791 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 559 | MOVE_BENCH | ECON | 72.0 | 8 | 13 | 1 | 44.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2301119863986969 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 560 | BUY | ECON | 72.0 | 8 | 13 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06474290043115616 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 2 | 5-3 | 561 | MOVE_BENCH | ECON | 72.0 | 8 | 8 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37181591987609863 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 562 | PASS | ECON | 72.0 | 8 | 8 | 0 | 62.0 | Adaptador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 571 | BUY | ECON | 55.0 | 8 | 14 | 1 | 62.0 | Adaptador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21573691070079803 | 0.0 | 0.0 | +2a2b613e-8850-4c70-ab66-bc18356178e8 / -— |
| Jogador 2 | 5-4 | 572 | SELL | ECON | 55.0 | 8 | 12 | 1 | 62.0 | Adaptador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3237203061580658 | 0.0 | 0.0 | +— / -908d49c8-626c-44b5-9b03-6a85442f358b |
| Jogador 2 | 5-4 | 573 | BUY | ECON | 55.0 | 8 | 16 | 1 | 62.0 | Adaptador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10560856014490128 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 2 | 5-4 | 574 | REROLL | ECON | 55.0 | 8 | 12 | 1 | 62.0 | Adaptador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 575 | SELL | ECON | 55.0 | 8 | 10 | 1 | 62.0 | Adaptador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -c93990ff-0a6f-46bc-8fc1-12623d55abc1 |
| Jogador 2 | 5-4 | 576 | BUY | ECON | 55.0 | 8 | 14 | 1 | 62.0 | Adaptador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7602216601371765 | 0.0 | 0.0 | +b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 / -7643f027-a90f-4f3a-8b4c-7be4cba17f95,e5f61076-ec13-419b-a4e8-d91b9975cfd6 |
| Jogador 2 | 5-4 | 577 | BUY | ECON | 55.0 | 8 | 10 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19233061373233795 | 0.0 | 0.0 | +85d35881-ba70-4310-8d5f-bae796309eed / -— |
| Jogador 2 | 5-4 | 578 | MOVE_BENCH | ECON | 55.0 | 8 | 6 | 0 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013053709641098976 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 579 | MOVE_BENCH | ECON | 55.0 | 8 | 6 | 0 | 58.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09772081673145294 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 580 | MOVE_BENCH | ECON | 55.0 | 8 | 6 | 0 | 56.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35100555419921875 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 581 | PASS | ECON | 55.0 | 8 | 6 | 0 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 587 | BUY | ECON | 55.0 | 8 | 12 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6538644433021545 | 0.0 | 0.0 | +78adfe0a-b6d8-4cc4-a482-26451f95e788 / -— |
| Jogador 2 | 5-5 | 588 | SELL | ECON | 55.0 | 8 | 9 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13118144869804382 | 0.0 | 0.0 | +— / -b1efce8c-0cb0-47fc-a361-c50a76c0f9de |
| Jogador 2 | 5-5 | 589 | BUY | ECON | 55.0 | 8 | 13 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01605256460607052 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -— |
| Jogador 2 | 5-5 | 590 | REROLL | ECON | 55.0 | 8 | 8 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 591 | SELL | ECON | 55.0 | 8 | 6 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13272307813167572 | 0.0 | 0.0 | +— / -85d35881-ba70-4310-8d5f-bae796309eed |
| Jogador 2 | 5-5 | 592 | BUY | ECON | 55.0 | 8 | 10 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29297935962677 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -— |
| Jogador 2 | 5-5 | 593 | REROLL | ECON | 55.0 | 8 | 6 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 594 | REROLL | ECON | 55.0 | 8 | 4 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 595 | SELL | ECON | 55.0 | 8 | 2 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07118461281061172 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 2 | 5-5 | 596 | BUY | ECON | 55.0 | 8 | 6 | 0 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21186281740665436 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 2 | 5-5 | 597 | PASS | ECON | 55.0 | 8 | 2 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 602 | SELL | STABILIZE | 38.0 | 8 | 8 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.132876917719841 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 2 | 5-6 | 603 | BUY | STABILIZE | 38.0 | 8 | 13 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2578639090061188 | 0.0 | 0.0 | +249d7b90-0660-4e4f-885a-7791c1cac21a / -— |
| Jogador 2 | 5-6 | 604 | REROLL | STABILIZE | 38.0 | 8 | 8 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 605 | SELL | STABILIZE | 38.0 | 8 | 6 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14690768718719482 | 0.0 | 0.0 | +— / -249d7b90-0660-4e4f-885a-7791c1cac21a |
| Jogador 2 | 5-6 | 606 | BUY | STABILIZE | 38.0 | 8 | 11 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7234724164009094 | 0.0 | 0.0 | +6875f839-cf68-443f-9776-887087b375d3 / -— |
| Jogador 2 | 5-6 | 607 | REROLL | STABILIZE | 38.0 | 8 | 8 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 608 | SELL | STABILIZE | 38.0 | 8 | 6 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11441538482904434 | 0.0 | 0.0 | +— / -6b7f5603-ce44-4b91-8a3e-939c4fbb26ac |
| Jogador 2 | 5-6 | 609 | BUY | STABILIZE | 38.0 | 8 | 11 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20397916436195374 | 0.0 | 0.0 | +ee093d10-ed4b-4e0e-8e0a-37247f9aa517 / -— |
| Jogador 2 | 5-6 | 610 | REROLL | STABILIZE | 38.0 | 8 | 8 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 611 | SELL | STABILIZE | 38.0 | 8 | 6 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02429027110338211 | 0.0 | 0.0 | +— / -5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 |
| Jogador 2 | 5-6 | 612 | PASS | STABILIZE | 38.0 | 8 | 7 | 0 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 620 | BUY | STABILIZE | 38.0 | 8 | 13 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7475917339324951 | 0.0 | 0.0 | +e8658026-70da-4dca-9f24-5a4aab392ddb / -729ccd5b-adc5-4bca-9523-dcb532e93ecb,e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 2 | 5-7 | 621 | MOVE_BENCH | STABILIZE | 38.0 | 8 | 9 | 0 | 46.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26527532935142517 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 622 | BUY | STABILIZE | 38.0 | 8 | 9 | 0 | 50.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0024969500955194235 | 0.0 | 0.0 | +4f8541d3-b2a0-4b56-a409-492d4992c419 / -— |
| Jogador 2 | 5-7 | 623 | MOVE_BENCH | STABILIZE | 38.0 | 8 | 5 | 0 | 50.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2876138687133789 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 624 | MOVE_BENCH | STABILIZE | 38.0 | 8 | 5 | 0 | 48.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3459929823875427 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 625 | PASS | STABILIZE | 38.0 | 8 | 5 | 0 | 54.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 632 | ANVIL_CHOICE | STABILIZE | 38.0 | 8 | 11 | 1 | 62.0 | Adaptador/DA_18_Ahri | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 633 | EQUIP_FROM_INVENTORY | STABILIZE | 38.0 | 8 | 11 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12400093674659729 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 634 | BUY | STABILIZE | 38.0 | 8 | 11 | 1 | 62.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006504180375486612 | 0.0 | 0.0 | +7904ab26-de3f-4144-b70f-ed620b41c907 / -— |
| Jogador 2 | 6-1 | 635 | MOVE_BENCH | STABILIZE | 38.0 | 8 | 7 | 0 | 62.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05548609420657158 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 636 | MOVE_BENCH | STABILIZE | 38.0 | 8 | 7 | 0 | 58.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.808135986328125 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 637 | PASS | STABILIZE | 38.0 | 8 | 7 | 0 | 54.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 651 | SELL | STABILIZE | 20.0 | 8 | 13 | 1 | 54.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -7904ab26-de3f-4144-b70f-ed620b41c907 |
| Jogador 2 | 6-2 | 652 | BUY | STABILIZE | 20.0 | 8 | 17 | 1 | 54.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.833432674407959 | 0.0 | 0.0 | +47b7832a-ef8a-436e-9e2e-84a5160ff6d5 / -6875f839-cf68-443f-9776-887087b375d3,a15ff9dc-bf8a-49e0-9893-f92a212263d8 |
| Jogador 2 | 6-2 | 653 | MOVE_BENCH | STABILIZE | 20.0 | 8 | 14 | 1 | 48.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30265703797340393 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 654 | BUY | STABILIZE | 20.0 | 8 | 14 | 1 | 56.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07508203387260437 | 0.0 | 0.0 | +df0a5d1f-d42d-43eb-b505-cfd00e3dcea8 / -— |
| Jogador 2 | 6-2 | 655 | MOVE_BENCH | STABILIZE | 20.0 | 8 | 11 | 1 | 56.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5555623769760132 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 656 | BUY | STABILIZE | 20.0 | 8 | 11 | 1 | 60.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4306434392929077 | 0.0 | 0.0 | +a74438d5-726a-4a58-a56d-cda374fddd16 / -— |
| Jogador 2 | 6-2 | 657 | REROLL | STABILIZE | 20.0 | 8 | 9 | 0 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 658 | REROLL | STABILIZE | 20.0 | 8 | 7 | 0 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 659 | SELL | STABILIZE | 20.0 | 8 | 5 | 0 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32331156730651855 | 0.0 | 0.0 | +— / -a74438d5-726a-4a58-a56d-cda374fddd16 |
| Jogador 2 | 6-2 | 660 | BUY | STABILIZE | 20.0 | 8 | 7 | 0 | 60.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6427406072616577 | 0.0 | 0.0 | +af23c553-04de-4813-87d0-bb7e4becafe4 / -— |
| Jogador 2 | 6-2 | 661 | PASS | STABILIZE | 20.0 | 8 | 3 | 0 | 60.0 | Adaptador/DA_18_Ahri | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 668 | SELL | STABILIZE | 20.0 | 8 | 9 | 0 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2582080364227295 | 0.0 | 0.0 | +— / -af23c553-04de-4813-87d0-bb7e4becafe4 |
| Jogador 2 | 6-3 | 669 | BUY | STABILIZE | 20.0 | 8 | 13 | 1 | 60.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18002577126026154 | 0.0 | 0.0 | +6426604f-2d8c-4300-a2d5-b068448a6eda / -— |
| Jogador 2 | 6-3 | 670 | REROLL | STABILIZE | 20.0 | 8 | 9 | 0 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 672 | SELL | STABILIZE | 20.0 | 8 | 14 | 1 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06807692348957062 | 0.0 | 0.0 | +— / -df0a5d1f-d42d-43eb-b505-cfd00e3dcea8 |
| Jogador 2 | 6-4 | 673 | BUY | STABILIZE | 20.0 | 8 | 17 | 1 | 60.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8058493137359619 | 0.0 | 0.0 | +8ac322bc-799c-4d78-a2d5-e76b64ce900f / -— |
| Jogador 2 | 6-4 | 674 | SELL | STABILIZE | 20.0 | 8 | 15 | 1 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -6426604f-2d8c-4300-a2d5-b068448a6eda |
| Jogador 2 | 6-4 | 675 | BUY | STABILIZE | 20.0 | 8 | 19 | 1 | 60.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8017631769180298 | 0.0 | 0.0 | +24985c10-0eb6-40fa-9d1a-99ceb7213e06 / -— |
| Jogador 2 | 6-4 | 676 | REROLL | STABILIZE | 20.0 | 8 | 15 | 1 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 677 | SELL | STABILIZE | 20.0 | 8 | 13 | 1 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4524288475513458 | 0.0 | 0.0 | +— / -33e9808b-2f92-49e7-ac35-1f6f9388edef |
| Jogador 2 | 6-4 | 678 | BUY | STABILIZE | 20.0 | 8 | 18 | 1 | 60.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6334284543991089 | 0.0 | 0.0 | +509928e4-3f42-4b0d-a71c-1a45fa23a781 / -— |
| Jogador 2 | 6-4 | 679 | REROLL | STABILIZE | 20.0 | 8 | 15 | 1 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 680 | SELL | STABILIZE | 20.0 | 8 | 13 | 1 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33690696954727173 | 0.0 | 0.0 | +— / -509928e4-3f42-4b0d-a71c-1a45fa23a781 |
| Jogador 2 | 6-5 | 682 | BUY | STABILIZE | 20.0 | 8 | 23 | 2 | 60.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010594910010695457 | 0.0 | 0.0 | +62214a63-ba6e-4230-8f21-741b36c6dae8 / -— |
| Jogador 2 | 6-5 | 683 | REROLL | STABILIZE | 20.0 | 8 | 19 | 1 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 684 | SELL | STABILIZE | 20.0 | 8 | 17 | 1 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38795071840286255 | 0.0 | 0.0 | +— / -47b7832a-ef8a-436e-9e2e-84a5160ff6d5 |
| Jogador 2 | 6-5 | 685 | BUY | STABILIZE | 20.0 | 8 | 25 | 2 | 60.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31538915634155273 | 0.0 | 0.0 | +61fe2c41-5cc2-4b6b-aa92-c83c3d900c07 / -— |
| Jogador 2 | 6-5 | 686 | REROLL | STABILIZE | 20.0 | 8 | 22 | 2 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 687 | SELL | STABILIZE | 20.0 | 8 | 20 | 2 | 60.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3070053458213806 | 0.0 | 0.0 | +— / -b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 |
| Jogador 2 | 6-5 | 688 | BUY | STABILIZE | 20.0 | 8 | 31 | 3 | 60.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5606130361557007 | 0.0 | 0.0 | +75351120-1642-4546-bb50-d7589d297dfc / -— |
| Jogador 2 | 6-5 | 689 | REROLL | STABILIZE | 20.0 | 8 | 27 | 2 | 60.0 | Adaptador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 690 | SELL | STABILIZE | 20.0 | 8 | 25 | 2 | 60.0 | Adaptador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3362849950790405 | 0.0 | 0.0 | +— / -75351120-1642-4546-bb50-d7589d297dfc |
| Jogador 2 | 6-6 | 692 | BUY | ALL_IN | 3.0 | 8 | 36 | 3 | 60.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8579713106155396 | 0.0 | 0.0 | +dcc60ca2-ff4b-4d41-91b3-03a6cd3de0bb / -— |
| Jogador 2 | 6-6 | 693 | SELL | ALL_IN | 3.0 | 8 | 33 | 3 | 60.0 | Adaptador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3165999948978424 | 0.0 | 0.0 | +— / -e8658026-70da-4dca-9f24-5a4aab392ddb |
| Jogador 2 | 6-6 | 694 | BUY | ALL_IN | 3.0 | 8 | 44 | 4 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8531211614608765 | 0.0 | 0.0 | +f0d04ec3-6adf-4895-a8a6-3eed946f2ea9 / -— |
| Jogador 2 | 6-6 | 695 | REROLL | ALL_IN | 3.0 | 8 | 40 | 4 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 696 | REROLL | ALL_IN | 3.0 | 8 | 38 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 697 | SELL | ALL_IN | 3.0 | 8 | 36 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7962563037872314 | 0.0 | 0.0 | +— / -8ac322bc-799c-4d78-a2d5-e76b64ce900f |
| Jogador 2 | 6-6 | 698 | BUY | ALL_IN | 3.0 | 8 | 38 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9419873952865601 | 0.0 | 0.0 | +d140c71c-0721-4d2e-97c7-3efd32bd59db / -24985c10-0eb6-40fa-9d1a-99ceb7213e06,4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 6-6 | 699 | BUY | ALL_IN | 3.0 | 8 | 34 | 3 | 52.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.645000159740448 | 0.0 | 0.0 | +a2a3d5de-f8f7-4ab7-856f-443af0019aba / -— |
| Jogador 2 | 6-6 | 700 | REROLL | ALL_IN | 3.0 | 8 | 30 | 3 | 52.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3026348650455475 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5842720866203308 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.038241982460022 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 30 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3530687689781189 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | -0.13714881241321564 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 32 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | 0.1410975158214569 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5131230354309082 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 34 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 54 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 81 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2068784236907959 | 0.0 | 0.0 | +d15ca853-2585-49d0-9d7f-339dae104062 / -— |
| Jogador 3 | 1-4 | 82 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22353872656822205 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 83 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5838006138801575 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0220333337783813 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2863226532936096 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 109 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 110 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 132 | SELL | STABILIZE | 96.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8301138281822205 | 0.0 | 0.0 | +— / -2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 |
| Jogador 3 | 2-2 | 133 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.115465521812439 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -c70251e8-af44-4466-808f-d49e9e5f57e9,d15ca853-2585-49d0-9d7f-339dae104062 |
| Jogador 3 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 5 | 0 | 4.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41635483503341675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 135 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2371758669614792 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 136 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 2 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6102111339569092 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 137 | PASS | STABILIZE | 96.0 | 4 | 2 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 159 | BUY | STABILIZE | 91.0 | 4 | 8 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09744467586278915 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 3 | 2-3 | 160 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 5 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6933603286743164 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 161 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 5 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11331064999103546 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 162 | BUY_XP | STABILIZE | 91.0 | 4 | 5 | 0 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 163 | MOVE_BENCH | SLOWROLL | 91.0 | 5 | 1 | 0 | 22.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5102147459983826 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 164 | PASS | SLOWROLL | 91.0 | 5 | 1 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 182 | BUY | SLOWROLL | 85.0 | 5 | 7 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15874674916267395 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 183 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 4 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5786264538764954 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 184 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 4 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09489937126636505 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 185 | PASS | SLOWROLL | 85.0 | 5 | 4 | 0 | 28.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 203 | SELL | SLOWROLL | 85.0 | 5 | 10 | 1 | 28.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07496145367622375 | 0.0 | 0.0 | +— / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef |
| Jogador 3 | 2-5 | 204 | BUY | SLOWROLL | 85.0 | 5 | 11 | 1 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.25221067667007446 | 0.0 | 0.0 | +226a1062-8e9a-4652-9da7-a2f215fa46ae / -— |
| Jogador 3 | 2-5 | 205 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 9 | 0 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.046607695519924164 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 206 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 9 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04995971918106079 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 207 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 9 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.353785902261734 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 208 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 9 | 0 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5681386590003967 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 209 | PASS | SLOWROLL | 85.0 | 5 | 9 | 0 | 24.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 226 | SELL | SLOWROLL | 85.0 | 5 | 16 | 1 | 24.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43304315209388733 | 0.0 | 0.0 | +— / -e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 227 | BUY | STABILIZE | 85.0 | 5 | 21 | 2 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9451265931129456 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 228 | BUY_XP | SLOWROLL | 85.0 | 5 | 19 | 1 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 229 | BUY_XP | SLOWROLL | 85.0 | 5 | 15 | 1 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 230 | BUY_XP | SLOWROLL | 85.0 | 5 | 11 | 1 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08884000033140182 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 231 | MOVE_BENCH | SLOWROLL | 85.0 | 6 | 7 | 0 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5331870913505554 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 232 | BUY_XP | FAST8 | 85.0 | 6 | 7 | 0 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 233 | PASS | FAST8 | 85.0 | 6 | 3 | 0 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 245 | BUY | FAST8 | 85.0 | 6 | 10 | 1 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9218663573265076 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 246 | SELL | FAST8 | 85.0 | 6 | 7 | 0 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.137676477432251 | 0.0 | 0.0 | +— / -79786887-d318-4836-b2f0-c0f03e86cbe5 |
| Jogador 3 | 2-7 | 247 | BUY | FAST8 | 85.0 | 6 | 10 | 1 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9634467959403992 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0,226a1062-8e9a-4652-9da7-a2f215fa46ae |
| Jogador 3 | 2-7 | 248 | MOVE_BENCH | SLOWROLL | 85.0 | 6 | 8 | 0 | 20.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4550197422504425 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 249 | PASS | FAST8 | 85.0 | 6 | 8 | 0 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 266 | BUY | FAST8 | 85.0 | 6 | 14 | 1 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21362145245075226 | 0.0 | 0.0 | +dc90c323-d8b9-44ab-b714-ea0fcc860de9 / -— |
| Jogador 3 | 3-1 | 267 | MOVE_BENCH | FAST8 | 85.0 | 6 | 12 | 1 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.435497522354126 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 268 | PASS | FAST8 | 85.0 | 6 | 12 | 1 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 287 | BUY | FAST8 | 85.0 | 6 | 20 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10017628967761993 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 288 | BUY_XP | FAST8 | 85.0 | 6 | 17 | 1 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 289 | BUY_XP | FAST8 | 85.0 | 6 | 13 | 1 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 290 | BUY_XP | FAST8 | 85.0 | 6 | 9 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 291 | BUY_XP | FAST8 | 85.0 | 6 | 5 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 292 | PASS | FAST8 | 85.0 | 6 | 1 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 306 | SELL | FAST8 | 85.0 | 6 | 8 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3721819519996643 | 0.0 | 0.0 | +— / -6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 |
| Jogador 3 | 3-3 | 307 | BUY | FAST8 | 85.0 | 6 | 11 | 1 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6554520726203918 | 0.0 | 0.0 | +ffdee27e-2d30-40b5-9937-92be68ab1390 / -— |
| Jogador 3 | 3-3 | 308 | SELL | FAST8 | 85.0 | 6 | 9 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.077691674232483 | 0.0 | 0.0 | +— / -ffdee27e-2d30-40b5-9937-92be68ab1390 |
| Jogador 3 | 3-3 | 309 | BUY | FAST8 | 85.0 | 6 | 11 | 1 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.310373991727829 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 310 | BUY_XP | FAST8 | 85.0 | 6 | 7 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 311 | PASS | FAST8 | 85.0 | 6 | 3 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 328 | SELL | FAST8 | 74.0 | 6 | 8 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2874935269355774 | 0.0 | 0.0 | +— / -527f78df-1e51-4731-9175-1c4812aa82ad |
| Jogador 3 | 3-4 | 329 | BUY | FAST8 | 74.0 | 6 | 12 | 1 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05038589611649513 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 330 | MOVE_BENCH | FAST8 | 74.0 | 6 | 9 | 0 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2885885536670685 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 331 | BUY_XP | FAST8 | 74.0 | 6 | 9 | 0 | 34.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 332 | MOVE_BENCH | FAST8 | 74.0 | 7 | 5 | 0 | 34.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7772942185401917 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 333 | MOVE_BENCH | FAST8 | 74.0 | 7 | 5 | 0 | 30.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5721601843833923 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 334 | BUY | FAST8 | 74.0 | 7 | 5 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03905276954174042 | 0.0 | 0.0 | +fe8191d8-bc21-499a-aff7-31c3ca9b2e64 / -— |
| Jogador 3 | 3-4 | 335 | PASS | FAST8 | 74.0 | 7 | 3 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 349 | SELL | FAST8 | 74.0 | 7 | 8 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05760711058974266 | 0.0 | 0.0 | +— / -fe8191d8-bc21-499a-aff7-31c3ca9b2e64 |
| Jogador 3 | 3-5 | 350 | BUY | FAST8 | 74.0 | 7 | 10 | 1 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6554911136627197 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -— |
| Jogador 3 | 3-5 | 351 | MOVE_BENCH | FAST8 | 74.0 | 7 | 8 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5858985185623169 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 352 | SELL | FAST8 | 74.0 | 7 | 8 | 0 | 34.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38490769267082214 | 0.0 | 0.0 | +— / -bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 3 | 3-5 | 353 | BUY | FAST8 | 74.0 | 7 | 13 | 1 | 34.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10405638813972473 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 3 | 3-5 | 354 | BUY_XP | FAST8 | 74.0 | 7 | 9 | 0 | 34.0 | Vanguarda/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 355 | BUY_XP | FAST8 | 74.0 | 7 | 5 | 0 | 34.0 | Vanguarda/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 356 | PASS | FAST8 | 74.0 | 7 | 1 | 0 | 34.0 | Vanguarda/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 365 | SELL | FAST8 | 74.0 | 7 | 7 | 0 | 34.0 | Vanguarda/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30504903197288513 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-6 | 366 | BUY | FAST8 | 74.0 | 7 | 11 | 1 | 34.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6858174204826355 | 0.0 | 0.0 | +27102740-ce4d-4bec-a9eb-ed936f6bc364 / -65a6d68c-90ae-4e31-8bbc-82e8ec75b3de,dc90c323-d8b9-44ab-b714-ea0fcc860de9 |
| Jogador 3 | 3-6 | 367 | MOVE_BENCH | FAST8 | 74.0 | 7 | 9 | 0 | 26.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4423378109931946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 368 | BUY | FAST8 | 74.0 | 7 | 9 | 0 | 34.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.043559275567531586 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 369 | BUY_XP | FAST8 | 74.0 | 7 | 6 | 0 | 34.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 370 | PASS | FAST8 | 74.0 | 7 | 2 | 0 | 34.0 | Vanguarda/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 382 | BUY | FAST8 | 74.0 | 7 | 9 | 0 | 40.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09770803898572922 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 383 | MOVE_BENCH | FAST8 | 74.0 | 7 | 6 | 0 | 40.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5063968300819397 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 384 | MOVE_BENCH | FAST8 | 74.0 | 7 | 6 | 0 | 40.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3000815808773041 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 385 | PASS | FAST8 | 74.0 | 7 | 6 | 0 | 40.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 402 | MOVE_BENCH | FAST8 | 74.0 | 7 | 12 | 1 | 40.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6956298351287842 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 403 | SELL | FAST8 | 74.0 | 7 | 12 | 1 | 38.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5298923254013062 | 0.0 | 0.0 | +— / -27102740-ce4d-4bec-a9eb-ed936f6bc364 |
| Jogador 3 | 4-1 | 404 | BUY | FAST8 | 74.0 | 7 | 17 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0463082380592823 | 0.0 | 0.0 | +48be5cb2-e7b3-41f8-b212-79e21249fa6a / -— |
| Jogador 3 | 4-1 | 405 | BUY_XP | FAST8 | 74.0 | 7 | 13 | 1 | 38.0 | Vanguarda/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 406 | BUY_XP | FAST8 | 74.0 | 7 | 9 | 0 | 38.0 | Vanguarda/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 407 | BUY_XP | FAST8 | 74.0 | 7 | 5 | 0 | 38.0 | Vanguarda/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 408 | PASS | FAST8 | 74.0 | 7 | 1 | 0 | 38.0 | Vanguarda/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 422 | SELL | FAST8 | 60.0 | 7 | 6 | 0 | 38.0 | Vanguarda/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3184618353843689 | 0.0 | 0.0 | +— / -48be5cb2-e7b3-41f8-b212-79e21249fa6a |
| Jogador 3 | 4-2 | 423 | BUY | FAST8 | 60.0 | 7 | 10 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6525604724884033 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 3 | 4-2 | 424 | MOVE_BENCH | FAST8 | 60.0 | 7 | 7 | 0 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023755274713039398 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 425 | SELL | FAST8 | 60.0 | 7 | 7 | 0 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08535824716091156 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 4-2 | 426 | BUY | FAST8 | 60.0 | 7 | 10 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08930999785661697 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 3 | 4-2 | 427 | BUY_XP | FAST8 | 60.0 | 7 | 6 | 0 | 38.0 | Vanguarda/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 428 | PASS | FAST8 | 60.0 | 7 | 2 | 0 | 38.0 | Vanguarda/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 440 | BUY | FAST8 | 47.0 | 7 | 8 | 0 | 38.0 | Vanguarda/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7638965249061584 | 0.0 | 0.0 | +3f488391-7117-4e28-b6cc-7416722351d4 / -2a2066ee-841b-49d5-8b82-1d47feb36d8c,9bd6852a-b7a4-468c-a8cc-5318f7906eae |
| Jogador 3 | 4-3 | 441 | MOVE_BENCH | FAST8 | 47.0 | 7 | 5 | 0 | 26.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4788760840892792 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 442 | MOVE_BENCH | FAST8 | 47.0 | 7 | 5 | 0 | 38.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41554147005081177 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 443 | BUY | FAST8 | 47.0 | 7 | 5 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.037287719547748566 | 0.0 | 0.0 | +395ae945-c8a2-4d80-98a4-5eb6887b8f78 / -— |
| Jogador 3 | 4-3 | 444 | MOVE_BENCH | FAST8 | 47.0 | 7 | 1 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3379676938056946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 445 | PASS | FAST8 | 47.0 | 7 | 1 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 452 | BUY_XP | STABILIZE | 34.0 | 7 | 7 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 453 | PASS | STABILIZE | 34.0 | 7 | 3 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 472 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7321398854255676 | 0.0 | 0.0 | +1ff42607-ccac-4d3f-8277-bccddf08862f / -— |
| Jogador 3 | 4-5 | 473 | BUY_XP | STABILIZE | 34.0 | 7 | 6 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 474 | PASS | STABILIZE | 34.0 | 7 | 2 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 491 | BUY | STABILIZE | 21.0 | 8 | 8 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18160289525985718 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 3 | 4-6 | 492 | BUY | STABILIZE | 21.0 | 8 | 4 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3981355130672455 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 3 | 4-6 | 493 | PASS | STABILIZE | 21.0 | 8 | 0 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 503 | MOVE_BENCH | STABILIZE | 21.0 | 8 | 0 | 0 | 46.0 | Vanguarda/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3968736231327057 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 509 | BUY | ALL_IN | 7.0 | 8 | 7 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33716511726379395 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 3 | 4-7 | 510 | BUY | ALL_IN | 7.0 | 8 | 4 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6529142260551453 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 3 | 4-7 | 511 | PASS | ALL_IN | 7.0 | 8 | 0 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 522 | ANVIL_CHOICE | ALL_IN | 7.0 | 8 | 7 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 523 | BUY | ALL_IN | 7.0 | 8 | 7 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1532120257616043 | 0.0 | 0.0 | +c8706680-2712-4914-b6c0-59bf92a2796d / -— |
| Jogador 3 | 5-1 | 524 | BUY | ALL_IN | 7.0 | 8 | 4 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22893333435058594 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 3 | 5-1 | 525 | REROLL | ALL_IN | 7.0 | 8 | 2 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 526 | CRAFT_AND_EQUIP | ALL_IN | 7.0 | 8 | 0 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1161685660481453 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 527 | PASS | ALL_IN | 7.0 | 8 | 0 | 0 | 54.0 | Vanguarda/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +1903eae4-bd37-4ed8-bbae-28177e859592 / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1957342028617859 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30133089423179626 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.13714881241321564 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.1591830998659134 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5162969827651978 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 33 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 54 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23796431720256805 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 55 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 81 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4180184006690979 | 0.0 | 0.0 | +— / -a19fc47b-fc81-49b2-bc25-d25d58b8deef |
| Jogador 4 | 1-4 | 82 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0395427942276 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 83 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5344916582107544 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0332390069961548 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 108 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 109 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12384627014398575 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 110 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 132 | BUY_XP | STABILIZE | 100.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 133 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6342348456382751 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 134 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5073421597480774 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 135 | BUY | SLOWROLL | 100.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.041335996240377426 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 136 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2643498480319977 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 137 | PASS | SLOWROLL | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 159 | SELL | SLOWROLL | 100.0 | 5 | 10 | 1 | 12.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8523814678192139 | 0.0 | 0.0 | +— / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793 |
| Jogador 4 | 2-3 | 160 | BUY | SLOWROLL | 100.0 | 5 | 11 | 1 | 12.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2137860208749771 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 161 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 8 | 0 | 12.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024744365364313126 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 162 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26270580291748047 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 163 | PASS | SLOWROLL | 100.0 | 5 | 8 | 0 | 16.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 182 | SELL | SLOWROLL | 100.0 | 5 | 15 | 1 | 16.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8477845788002014 | 0.0 | 0.0 | +— / -0e9aa759-0538-4168-a523-02a5f8e09e0a |
| Jogador 4 | 2-4 | 183 | BUY | STABILIZE | 100.0 | 5 | 16 | 1 | 16.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.18311768770217896 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 184 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8148549795150757 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 185 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08894836902618408 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 186 | BUY_XP | STABILIZE | 100.0 | 5 | 12 | 1 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 187 | BUY_XP | STABILIZE | 100.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 188 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 189 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 203 | SELL | STABILIZE | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021091975271701813 | 0.0 | 0.0 | +— / -9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 2-5 | 204 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.346016526222229 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 205 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8418828248977661 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 206 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 207 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 22.0 | Adaptador/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16444000601768494 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 208 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Adaptador/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43503478169441223 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 209 | PASS | FAST8 | 100.0 | 6 | 0 | 0 | 28.0 | Adaptador/DA_18_Aphelios | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 226 | BUY | FAST8 | 100.0 | 6 | 7 | 0 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3125828504562378 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 227 | MOVE_BENCH | FAST8 | 100.0 | 6 | 3 | 0 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0959058627486229 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 228 | MOVE_BOARD | FAST8 | 100.0 | 6 | 3 | 0 | 30.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 229 | PASS | FAST8 | 100.0 | 6 | 3 | 0 | 30.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 245 | MOVE_BENCH | FAST8 | 93.0 | 6 | 8 | 0 | 30.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7322977185249329 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 246 | BUY_XP | FAST8 | 93.0 | 6 | 8 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 247 | BUY_XP | FAST8 | 93.0 | 6 | 4 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 248 | PASS | FAST8 | 93.0 | 6 | 0 | 0 | 34.0 | Adaptador/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 266 | SELL | FAST8 | 93.0 | 6 | 5 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49777066707611084 | 0.0 | 0.0 | +— / -1903eae4-bd37-4ed8-bbae-28177e859592 |
| Jogador 4 | 3-1 | 267 | BUY | FAST8 | 93.0 | 6 | 6 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21454231441020966 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 268 | BUY_XP | FAST8 | 93.0 | 6 | 4 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 269 | PASS | FAST8 | 93.0 | 6 | 0 | 0 | 34.0 | Adaptador/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 287 | BUY_XP | FAST8 | 81.0 | 6 | 6 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 288 | PASS | FAST8 | 81.0 | 6 | 2 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 306 | SELL | FAST8 | 71.0 | 6 | 8 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3783538341522217 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-3 | 307 | BUY | FAST8 | 71.0 | 6 | 10 | 1 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10730688273906708 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 308 | BUY_XP | FAST8 | 71.0 | 6 | 7 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 309 | PASS | FAST8 | 71.0 | 6 | 3 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 328 | BUY | FAST8 | 58.0 | 6 | 9 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21267859637737274 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 329 | BUY_XP | FAST8 | 58.0 | 6 | 6 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 330 | MOVE_BENCH | FAST8 | 58.0 | 7 | 2 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09809432923793793 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 331 | MOVE_BENCH | FAST8 | 58.0 | 7 | 2 | 0 | 36.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43929797410964966 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 332 | MOVE_BENCH | FAST8 | 58.0 | 7 | 2 | 0 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7443343997001648 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 333 | PASS | FAST8 | 58.0 | 7 | 2 | 0 | 40.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 349 | SELL | FAST8 | 58.0 | 7 | 8 | 0 | 40.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07256922870874405 | 0.0 | 0.0 | +— / -58c38a13-23c5-4ac1-8601-f0636aeb33ab |
| Jogador 4 | 3-5 | 350 | BUY | FAST8 | 58.0 | 7 | 11 | 1 | 40.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6531850099563599 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 351 | MOVE_BENCH | FAST8 | 58.0 | 7 | 8 | 0 | 40.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02372080832719803 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 352 | BUY_XP | FAST8 | 58.0 | 7 | 8 | 0 | 42.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 353 | BUY_XP | FAST8 | 58.0 | 7 | 4 | 0 | 42.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 354 | PASS | FAST8 | 58.0 | 7 | 0 | 0 | 42.0 | Adaptador/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 365 | BUY_XP | FAST8 | 58.0 | 7 | 6 | 0 | 42.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 366 | PASS | FAST8 | 58.0 | 7 | 2 | 0 | 42.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 382 | BUY | FAST8 | 58.0 | 7 | 9 | 0 | 42.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7631979584693909 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,40f2a32f-1ace-4700-8a79-e6b5d3212036 |
| Jogador 4 | 3-7 | 383 | MOVE_BENCH | FAST8 | 58.0 | 7 | 6 | 0 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5838910341262817 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 384 | BUY_XP | FAST8 | 58.0 | 7 | 6 | 0 | 42.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 385 | PASS | FAST8 | 58.0 | 7 | 2 | 0 | 42.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 397 | MOVE_BENCH | FAST8 | 58.0 | 7 | 2 | 0 | 42.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.427694708108902 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 402 | BUY | FAST8 | 58.0 | 7 | 8 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.7312021851539612 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 4 | 4-1 | 403 | BUY_XP | FAST8 | 58.0 | 7 | 5 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 404 | CRAFT_AND_EQUIP | FAST8 | 58.0 | 7 | 1 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.035196367651224136 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 405 | PASS | FAST8 | 58.0 | 7 | 1 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 422 | BUY_XP | FAST8 | 46.0 | 7 | 6 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 423 | PASS | FAST8 | 46.0 | 7 | 2 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 440 | BUY_XP | FAST8 | 46.0 | 7 | 8 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 441 | BUY_XP | FAST8 | 46.0 | 7 | 4 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 442 | PASS | FAST8 | 46.0 | 7 | 0 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 452 | BUY_XP | FAST8 | 46.0 | 7 | 7 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 453 | PASS | FAST8 | 46.0 | 7 | 3 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 472 | BUY_XP | FAST8 | 46.0 | 7 | 9 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08269374817609787 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 473 | MOVE_BENCH | ECON | 46.0 | 8 | 5 | 0 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5597880482673645 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 474 | BUY | ECON | 46.0 | 8 | 5 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16060972213745117 | 0.0 | 0.0 | +d6a00f0c-4823-44d6-b326-67595876998d / -— |
| Jogador 4 | 4-5 | 475 | PASS | ECON | 46.0 | 8 | 1 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 491 | BUY | ECON | 46.0 | 8 | 8 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07117171585559845 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 4 | 4-6 | 492 | BUY | ECON | 46.0 | 8 | 4 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15911361575126648 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 4 | 4-6 | 493 | PASS | ECON | 46.0 | 8 | 0 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 509 | BUY | ECON | 46.0 | 8 | 7 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.763985812664032 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -42733dbd-0bc3-461b-95ab-76daf5ad6296,a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 4-7 | 510 | MOVE_BENCH | ECON | 46.0 | 8 | 4 | 0 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6965172290802002 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 511 | MOVE_BENCH | ECON | 46.0 | 8 | 4 | 0 | 36.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2648846507072449 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 512 | MOVE_BENCH | ECON | 46.0 | 8 | 4 | 0 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21070225536823273 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 513 | BUY_XP | ECON | 46.0 | 8 | 4 | 0 | 48.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 514 | PASS | ECON | 46.0 | 8 | 0 | 0 | 48.0 | Adaptador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 522 | ANVIL_CHOICE | ECON | 46.0 | 8 | 6 | 0 | 56.0 | Adaptador/DA_18_Diana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 523 | BUY | ECON | 46.0 | 8 | 6 | 0 | 56.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21398580074310303 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -— |
| Jogador 4 | 5-1 | 524 | MOVE_BENCH | ECON | 46.0 | 8 | 3 | 0 | 56.0 | Adaptador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03340347856283188 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 525 | MOVE_BENCH | ECON | 46.0 | 8 | 3 | 0 | 56.0 | Adaptador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35107702016830444 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 526 | PASS | ECON | 46.0 | 8 | 3 | 0 | 56.0 | Adaptador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 540 | MOVE_BENCH | STABILIZE | 31.0 | 8 | 8 | 0 | 56.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6965273022651672 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 541 | MOVE_BENCH | STABILIZE | 31.0 | 8 | 8 | 0 | 52.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10622189193964005 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 542 | MOVE_BENCH | STABILIZE | 31.0 | 8 | 8 | 0 | 56.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29807978868484497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 543 | BUY | STABILIZE | 31.0 | 8 | 8 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8618162870407104 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 4 | 5-2 | 544 | PASS | STABILIZE | 31.0 | 8 | 4 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 552 | BUY | ALL_IN | 14.0 | 8 | 10 | 1 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10378380864858627 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -— |
| Jogador 4 | 5-3 | 553 | REROLL | ALL_IN | 14.0 | 8 | 6 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 554 | BUY | ALL_IN | 14.0 | 8 | 4 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08771204203367233 | 0.0 | 0.0 | +3c46b699-2b56-48d0-820c-b523c5153b9f / -— |
| Jogador 4 | 5-3 | 555 | PASS | ALL_IN | 14.0 | 8 | 0 | 0 | 58.0 | Adaptador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 571 | BUY | ALL_IN | 14.0 | 8 | 6 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8128771781921387 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 4 | 5-4 | 572 | BUY | ALL_IN | 14.0 | 8 | 2 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08251217007637024 | 0.0 | 0.0 | +f9820f05-e1b0-4953-a98d-3ae191b1249a / -— |
| Jogador 4 | 5-4 | 573 | PASS | ALL_IN | 14.0 | 8 | 0 | 0 | 58.0 | Adaptador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 587 | BUY | ALL_IN | 14.0 | 8 | 5 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17397719621658325 | 0.0 | 0.0 | +d79de824-d9b2-4dfb-a7be-a359b416aea1 / -— |
| Jogador 4 | 5-5 | 588 | REROLL | ALL_IN | 14.0 | 8 | 2 | 0 | 58.0 | Adaptador/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 589 | SELL | ALL_IN | 14.0 | 8 | 0 | 0 | 58.0 | Adaptador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.049776215106248856 | 0.0 | 0.0 | +— / -f9820f05-e1b0-4953-a98d-3ae191b1249a |
| Jogador 4 | 5-5 | 590 | BUY | ALL_IN | 14.0 | 8 | 2 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058277614414691925 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -— |
| Jogador 4 | 5-5 | 591 | PASS | ALL_IN | 14.0 | 8 | 1 | 0 | 58.0 | Adaptador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 602 | REROLL | ALL_IN | 14.0 | 8 | 8 | 0 | 58.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 603 | SELL | ALL_IN | 14.0 | 8 | 6 | 0 | 58.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05226153880357742 | 0.0 | 0.0 | +— / -8025eaf5-b02b-4f94-b381-b94321bca206 |
| Jogador 4 | 5-6 | 604 | BUY | ALL_IN | 14.0 | 8 | 7 | 0 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7939824461936951 | 0.0 | 0.0 | +40263a7a-96e9-4752-b149-8235892508e0 / -— |
| Jogador 4 | 5-6 | 605 | REROLL | ALL_IN | 14.0 | 8 | 4 | 0 | 58.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 606 | REROLL | ALL_IN | 14.0 | 8 | 2 | 0 | 58.0 | Adaptador/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 607 | PASS | ALL_IN | 14.0 | 8 | 0 | 0 | 58.0 | Adaptador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +a05f4164-724c-4182-bafc-82ef354cea0b / -— |
| Jogador 5 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032908253371715546 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36288121342658997 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 54 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25067511200904846 | 0.0 | 0.0 | +4a7ac9c5-c110-4566-80e5-25d9e6033799 / -— |
| Jogador 5 | 1-3 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42014822363853455 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5188013911247253 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 57 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 81 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10049767792224884 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 82 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3057861924171448 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4617135524749756 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 84 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 12.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6774187088012695 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22516115009784698 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 108 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7063031196594238 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12553547322750092 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -— |
| Jogador 5 | 2-1 | 110 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 132 | SELL | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07832307368516922 | 0.0 | 0.0 | +— / -a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 |
| Jogador 5 | 2-2 | 133 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1871626377105713 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2770327627658844 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 135 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11844202131032944 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 136 | PASS | STABILIZE | 95.0 | 4 | 7 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 159 | SELL | STABILIZE | 91.0 | 4 | 13 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11806993186473846 | 0.0 | 0.0 | +— / -a05f4164-724c-4182-bafc-82ef354cea0b |
| Jogador 5 | 2-3 | 160 | BUY | STABILIZE | 91.0 | 4 | 14 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3726780116558075 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 161 | BUY_XP | STABILIZE | 91.0 | 4 | 13 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 162 | BUY_XP | STABILIZE | 91.0 | 4 | 9 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 163 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 5 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5534232258796692 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 164 | BUY | STABILIZE | 91.0 | 5 | 5 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.34603697061538696 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 165 | BUY_XP | STABILIZE | 91.0 | 5 | 4 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 166 | PASS | STABILIZE | 91.0 | 5 | 0 | 0 | 20.0 | —/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 182 | SELL | STABILIZE | 91.0 | 5 | 6 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06082097068428993 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 183 | BUY | STABILIZE | 91.0 | 5 | 7 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.37276116013526917 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 184 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 4 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2140008509159088 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 185 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 4 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29123714566230774 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 186 | BUY_XP | STABILIZE | 91.0 | 5 | 4 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 187 | PASS | STABILIZE | 91.0 | 5 | 0 | 0 | 24.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 203 | SELL | STABILIZE | 91.0 | 5 | 5 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10011013597249985 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-5 | 204 | BUY | STABILIZE | 91.0 | 5 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.032620806246995926 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 205 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 3 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005400142632424831 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 206 | PASS | STABILIZE | 91.0 | 5 | 3 | 0 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 226 | SELL | STABILIZE | 91.0 | 5 | 10 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004934434778988361 | 0.0 | 0.0 | +— / -df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 2-6 | 227 | BUY | STABILIZE | 91.0 | 5 | 12 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.39922744035720825 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 228 | BUY_XP | STABILIZE | 91.0 | 5 | 10 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07297000288963318 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 229 | MOVE_BENCH | FAST8 | 91.0 | 6 | 6 | 0 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8028383851051331 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 230 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5183669328689575 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 231 | PASS | FAST8 | 91.0 | 6 | 6 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 245 | BUY | FAST8 | 91.0 | 6 | 13 | 1 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3215215504169464 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 2-7 | 246 | BUY_XP | FAST8 | 91.0 | 6 | 12 | 1 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 247 | BUY_XP | FAST8 | 91.0 | 6 | 8 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 248 | BUY_XP | FAST8 | 91.0 | 6 | 4 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 249 | PASS | FAST8 | 91.0 | 6 | 0 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 266 | SELL | FAST8 | 91.0 | 6 | 6 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4502883553504944 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 3-1 | 267 | BUY | FAST8 | 91.0 | 6 | 7 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7358320355415344 | 0.0 | 0.0 | +79ed9815-7667-4e50-86a3-420599ce8c79 / -— |
| Jogador 5 | 3-1 | 268 | BUY_XP | FAST8 | 91.0 | 6 | 5 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 269 | PASS | FAST8 | 91.0 | 6 | 1 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 287 | SELL | FAST8 | 82.0 | 6 | 6 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8762750029563904 | 0.0 | 0.0 | +— / -79ed9815-7667-4e50-86a3-420599ce8c79 |
| Jogador 5 | 3-2 | 288 | BUY | FAST8 | 82.0 | 6 | 8 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7358319163322449 | 0.0 | 0.0 | +d218597b-b641-4a4c-867a-41227b83fcff / -— |
| Jogador 5 | 3-2 | 289 | SELL | FAST8 | 82.0 | 6 | 6 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1762479543685913 | 0.0 | 0.0 | +— / -d218597b-b641-4a4c-867a-41227b83fcff |
| Jogador 5 | 3-2 | 290 | BUY | FAST8 | 82.0 | 6 | 8 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.059101615101099014 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 291 | BUY_XP | FAST8 | 82.0 | 6 | 5 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 292 | PASS | FAST8 | 82.0 | 6 | 1 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 306 | SELL | FAST8 | 82.0 | 6 | 7 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31431111693382263 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-3 | 307 | BUY | FAST8 | 82.0 | 6 | 10 | 1 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5828619599342346 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 308 | MOVE_BENCH | FAST8 | 82.0 | 6 | 7 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3182589113712311 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 309 | BUY_XP | FAST8 | 82.0 | 6 | 7 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 310 | PASS | FAST8 | 82.0 | 6 | 3 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 328 | BUY_XP | FAST8 | 82.0 | 6 | 10 | 1 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02290000021457672 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 329 | MOVE_BENCH | FAST8 | 82.0 | 7 | 6 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016496190801262856 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 330 | MOVE_BENCH | FAST8 | 82.0 | 7 | 6 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35329580307006836 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 331 | MOVE_BENCH | FAST8 | 82.0 | 7 | 6 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5446943044662476 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 332 | BUY | FAST8 | 82.0 | 7 | 6 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.735813319683075 | 0.0 | 0.0 | +3a11170d-1b8e-4316-ad59-9a7e60071f12 / -— |
| Jogador 5 | 3-4 | 333 | BUY_XP | FAST8 | 82.0 | 7 | 4 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 334 | PASS | FAST8 | 82.0 | 7 | 0 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 349 | SELL | FAST8 | 82.0 | 7 | 6 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8763331174850464 | 0.0 | 0.0 | +— / -3a11170d-1b8e-4316-ad59-9a7e60071f12 |
| Jogador 5 | 3-5 | 350 | BUY | FAST8 | 82.0 | 7 | 8 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02739240974187851 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 351 | MOVE_BENCH | FAST8 | 82.0 | 7 | 4 | 0 | 36.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08144140988588333 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 352 | BUY_XP | FAST8 | 82.0 | 7 | 4 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 353 | PASS | FAST8 | 82.0 | 7 | 0 | 0 | 40.0 | Adaptador/DA_18_Morgana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 365 | SELL | FAST8 | 82.0 | 7 | 7 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01899999938905239 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 3-6 | 366 | BUY | FAST8 | 82.0 | 7 | 9 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10800200700759888 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 367 | BUY_XP | FAST8 | 82.0 | 7 | 6 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 368 | PASS | FAST8 | 82.0 | 7 | 2 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 382 | SELL | FAST8 | 82.0 | 7 | 9 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3320116698741913 | 0.0 | 0.0 | +— / -1457cd1e-c240-4ce5-9217-a91bddfc8807 |
| Jogador 5 | 3-7 | 383 | BUY | FAST8 | 82.0 | 7 | 12 | 1 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20920699834823608 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 384 | BUY_XP | FAST8 | 82.0 | 7 | 9 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 385 | BUY_XP | FAST8 | 82.0 | 7 | 5 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 386 | PASS | FAST8 | 82.0 | 7 | 1 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 402 | SELL | FAST8 | 82.0 | 7 | 7 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09103076905012131 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 4-1 | 403 | BUY | FAST8 | 82.0 | 7 | 10 | 1 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03613598272204399 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 404 | MOVE_BENCH | FAST8 | 82.0 | 7 | 7 | 0 | 40.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4316198229789734 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 405 | BUY_XP | FAST8 | 82.0 | 7 | 7 | 0 | 42.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 406 | PASS | FAST8 | 82.0 | 7 | 3 | 0 | 42.0 | Adaptador/DA_18_Morgana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 422 | SELL | FAST8 | 70.0 | 7 | 8 | 0 | 42.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40050768852233887 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 4-2 | 423 | BUY | FAST8 | 70.0 | 7 | 10 | 1 | 42.0 | Adaptador/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6511586904525757 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -486e92ad-4dcf-4c0e-a470-e0b87777d380,a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 4-2 | 424 | MOVE_BENCH | FAST8 | 70.0 | 7 | 7 | 0 | 30.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12611615657806396 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 425 | MOVE_BENCH | FAST8 | 70.0 | 7 | 7 | 0 | 34.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.366862028837204 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 426 | BUY | FAST8 | 70.0 | 7 | 7 | 0 | 42.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19765518605709076 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 5 | 4-2 | 427 | MOVE_BENCH | FAST8 | 70.0 | 7 | 4 | 0 | 42.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5634065866470337 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 428 | BUY_XP | FAST8 | 70.0 | 7 | 4 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 429 | PASS | FAST8 | 70.0 | 7 | 0 | 0 | 48.0 | Adaptador/DA_18_Rammus | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 440 | BUY | FAST8 | 59.0 | 7 | 6 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.733981192111969 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-3 | 441 | PASS | FAST8 | 59.0 | 7 | 3 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 452 | SELL | FAST8 | 59.0 | 7 | 9 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8354595303535461 | 0.0 | 0.0 | +— / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 5 | 4-4 | 453 | BUY | FAST8 | 59.0 | 7 | 12 | 1 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6531424522399902 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 5 | 4-4 | 454 | BUY_XP | FAST8 | 59.0 | 7 | 9 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 455 | BUY_XP | FAST8 | 59.0 | 7 | 5 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 456 | MOVE_BENCH | FAST8 | 59.0 | 7 | 1 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008558243862353265 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 457 | PASS | FAST8 | 59.0 | 7 | 1 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 472 | BUY_XP | FAST8 | 59.0 | 7 | 6 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08269374817609787 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 473 | MOVE_BENCH | ECON | 59.0 | 8 | 2 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3518252372741699 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 474 | MOVE_BENCH | ECON | 59.0 | 8 | 2 | 0 | 42.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0699906274676323 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 475 | MOVE_BENCH | ECON | 59.0 | 8 | 2 | 0 | 46.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4580894410610199 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 476 | MOVE_BENCH | ECON | 59.0 | 8 | 2 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2206481248140335 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 477 | PASS | ECON | 59.0 | 8 | 2 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 485 | MOVE_BENCH | ECON | 59.0 | 8 | 2 | 0 | 48.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5300610661506653 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 491 | BUY | ECON | 59.0 | 8 | 9 | 0 | 54.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20808382332324982 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 5 | 4-6 | 492 | MOVE_BENCH | ECON | 59.0 | 8 | 5 | 0 | 54.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17382773756980896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 493 | MOVE_BENCH | ECON | 59.0 | 8 | 5 | 0 | 54.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8170453310012817 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 494 | SELL | ECON | 59.0 | 8 | 5 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.433413565158844 | 0.0 | 0.0 | +— / -60255a84-4f78-49f0-a4f1-d598704c7ee7 |
| Jogador 5 | 4-6 | 495 | BUY | ECON | 59.0 | 8 | 8 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21104127168655396 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 5 | 4-6 | 496 | BUY_XP | ECON | 59.0 | 8 | 4 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 497 | PASS | ECON | 59.0 | 8 | 0 | 0 | 56.0 | Adaptador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 509 | BUY | WINSTREAK | 59.0 | 8 | 7 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14114730060100555 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 5 | 4-7 | 510 | BUY_XP | WINSTREAK | 59.0 | 8 | 4 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 511 | PASS | WINSTREAK | 59.0 | 8 | 0 | 0 | 56.0 | Adaptador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 522 | ANVIL_CHOICE | WINSTREAK | 59.0 | 8 | 6 | 0 | 56.0 | Adaptador/DA_18_Rammus | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 523 | BUY | WINSTREAK | 59.0 | 8 | 6 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7801085114479065 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 5 | 5-1 | 524 | CRAFT_AND_EQUIP | WINSTREAK | 59.0 | 8 | 2 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11035983264446259 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 525 | PASS | WINSTREAK | 59.0 | 8 | 2 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 540 | BUY | WINSTREAK | 59.0 | 8 | 9 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8447763919830322 | 0.0 | 0.0 | +f0264dc3-6749-4682-929e-fab42383532a / -— |
| Jogador 5 | 5-2 | 541 | BUY_XP | WINSTREAK | 59.0 | 8 | 6 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 542 | PASS | WINSTREAK | 59.0 | 8 | 2 | 0 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 552 | BUY | WINSTREAK | 59.0 | 8 | 10 | 1 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7796278595924377 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -0f1b15a2-9978-4691-a15e-483ccd03db7f,f0264dc3-6749-4682-929e-fab42383532a |
| Jogador 5 | 5-3 | 553 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 7 | 0 | 50.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 554 | BUY | WINSTREAK | 59.0 | 8 | 7 | 0 | 50.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20757460594177246 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 5 | 5-3 | 555 | BUY_XP | WINSTREAK | 59.0 | 8 | 4 | 0 | 50.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 556 | PASS | WINSTREAK | 59.0 | 8 | 0 | 0 | 50.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 564 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 0 | 0 | 50.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5466621518135071 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 571 | BUY | WINSTREAK | 59.0 | 8 | 9 | 0 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8267732858657837 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 5 | 5-4 | 572 | PASS | WINSTREAK | 59.0 | 8 | 6 | 0 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 587 | BUY | WINSTREAK | 59.0 | 8 | 14 | 1 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17283132672309875 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 5 | 5-5 | 588 | BUY | WINSTREAK | 59.0 | 8 | 10 | 1 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05587693303823471 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -— |
| Jogador 5 | 5-5 | 589 | PASS | WINSTREAK | 59.0 | 8 | 5 | 0 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 602 | BUY | WINSTREAK | 59.0 | 8 | 13 | 1 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2640542984008789 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 5 | 5-6 | 603 | BUY | WINSTREAK | 59.0 | 8 | 11 | 1 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07112324237823486 | 0.0 | 0.0 | +bfff6629-3ccc-4136-82a4-319a2fc5350e / -— |
| Jogador 5 | 5-6 | 604 | PASS | WINSTREAK | 59.0 | 8 | 8 | 0 | 58.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 620 | SELL | WINSTREAK | 59.0 | 8 | 17 | 1 | 58.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13256922364234924 | 0.0 | 0.0 | +— / -bfff6629-3ccc-4136-82a4-319a2fc5350e |
| Jogador 5 | 5-7 | 621 | BUY | WINSTREAK | 59.0 | 8 | 20 | 2 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.733677864074707 | 0.0 | 0.0 | +1cd4d2ae-a25f-4a8d-93e5-42284161b055 / -— |
| Jogador 5 | 5-7 | 622 | REROLL | WINSTREAK | 59.0 | 8 | 16 | 1 | 58.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 623 | SELL | WINSTREAK | 59.0 | 8 | 14 | 1 | 58.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06834098696708679 | 0.0 | 0.0 | +— / -ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 |
| Jogador 5 | 5-7 | 624 | BUY | WINSTREAK | 59.0 | 8 | 16 | 1 | 58.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7676488757133484 | 0.0 | 0.0 | +e99948bb-f38f-41e0-b1c4-1864c35ffe14 / -— |
| Jogador 5 | 5-7 | 625 | SELL | WINSTREAK | 59.0 | 8 | 13 | 1 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02103268913924694 | 0.0 | 0.0 | +— / -ae9da355-52b7-402c-be6e-41fa1148a550 |
| Jogador 5 | 5-7 | 626 | BUY | WINSTREAK | 59.0 | 8 | 17 | 1 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.712856113910675 | 0.0 | 0.0 | +f7f1b5db-dae6-4b1c-9a1f-94fefd1cf248 / -— |
| Jogador 5 | 5-7 | 627 | REROLL | WINSTREAK | 59.0 | 8 | 12 | 1 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 628 | SELL | WINSTREAK | 59.0 | 8 | 10 | 1 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48899999260902405 | 0.0 | 0.0 | +— / -2d5214b0-3e0c-4e71-8664-2459bf616650 |
| Jogador 5 | 5-7 | 629 | BUY | WINSTREAK | 59.0 | 8 | 18 | 1 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23743896186351776 | 0.0 | 0.0 | +e32f79ba-6ddd-4e40-8150-666105cb09b7 / -— |
| Jogador 5 | 5-7 | 630 | PASS | WINSTREAK | 59.0 | 8 | 14 | 1 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 632 | ANVIL_CHOICE | WINSTREAK | 59.0 | 8 | 23 | 2 | 58.0 | Adaptador/DA_18_Rammus | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 633 | EQUIP_FROM_INVENTORY | WINSTREAK | 59.0 | 8 | 23 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09688373655080795 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 634 | SELL | WINSTREAK | 59.0 | 8 | 23 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07118461281061172 | 0.0 | 0.0 | +— / -e32f79ba-6ddd-4e40-8150-666105cb09b7 |
| Jogador 5 | 6-1 | 635 | BUY | WINSTREAK | 59.0 | 8 | 27 | 2 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13725529611110687 | 0.0 | 0.0 | +699b59c7-1237-472b-a4d1-18a35e88b7c2 / -— |
| Jogador 5 | 6-1 | 636 | SELL | WINSTREAK | 59.0 | 8 | 22 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7636541128158569 | 0.0 | 0.0 | +— / -4261ad99-2607-4d90-978c-9e9abffd6d95 |
| Jogador 5 | 6-1 | 637 | BUY | WINSTREAK | 59.0 | 8 | 25 | 2 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1923181265592575 | 0.0 | 0.0 | +19e8f3ef-c3a6-459e-bf05-a53f742ba05d / -— |
| Jogador 5 | 6-1 | 638 | REROLL | WINSTREAK | 59.0 | 8 | 20 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 639 | SELL | WINSTREAK | 59.0 | 8 | 18 | 1 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.132876917719841 | 0.0 | 0.0 | +— / -699b59c7-1237-472b-a4d1-18a35e88b7c2 |
| Jogador 5 | 6-1 | 640 | BUY | WINSTREAK | 59.0 | 8 | 23 | 2 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.813532829284668 | 0.0 | 0.0 | +12d02679-e950-433b-ad9e-679a89cf86d8 / -— |
| Jogador 5 | 6-1 | 641 | REROLL | WINSTREAK | 59.0 | 8 | 20 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 642 | PASS | WINSTREAK | 59.0 | 8 | 18 | 1 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03257142752408981 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 651 | SELL | WINSTREAK | 59.0 | 8 | 28 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6836540699005127 | 0.0 | 0.0 | +— / -0a29573e-2a7b-4719-9b6e-49c2f476bc04 |
| Jogador 5 | 6-2 | 652 | BUY | WINSTREAK | 59.0 | 8 | 31 | 3 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09452741593122482 | 0.0 | 0.0 | +61c89fb9-3f6f-4386-a3b9-5e4fc71ee9c3 / -— |
| Jogador 5 | 6-2 | 653 | SELL | WINSTREAK | 59.0 | 8 | 27 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13696983456611633 | 0.0 | 0.0 | +— / -61c89fb9-3f6f-4386-a3b9-5e4fc71ee9c3 |
| Jogador 5 | 6-2 | 654 | BUY | WINSTREAK | 59.0 | 8 | 31 | 3 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21930564939975739 | 0.0 | 0.0 | +c06a964e-4ad5-444a-8800-0410c94f5c1f / -— |
| Jogador 5 | 6-2 | 655 | REROLL | WINSTREAK | 59.0 | 8 | 27 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 656 | SELL | WINSTREAK | 59.0 | 8 | 25 | 2 | 58.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -c06a964e-4ad5-444a-8800-0410c94f5c1f |
| Jogador 5 | 6-2 | 657 | BUY | WINSTREAK | 59.0 | 8 | 29 | 2 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8659387826919556 | 0.0 | 0.0 | +b1e5b3b9-fda8-4d4a-9368-94fd558da4f7 / -e99948bb-f38f-41e0-b1c4-1864c35ffe14,fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 5 | 6-2 | 658 | BUY | WINSTREAK | 59.0 | 8 | 26 | 2 | 52.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8718621730804443 | 0.0 | 0.0 | +2ce6c216-8ffa-4f9b-b78a-aed96adfa47b / -1cd4d2ae-a25f-4a8d-93e5-42284161b055,de8de4b5-48ea-4947-ae08-2b90d94b0fc1 |
| Jogador 5 | 6-2 | 659 | BUY | WINSTREAK | 59.0 | 8 | 22 | 2 | 44.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7939307689666748 | 0.0 | 0.0 | +c339a5f7-66d9-4d5f-b331-4bac23a83a4a / -68cd8ae3-399f-461f-89a8-189d7b0a6b59,e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 |
| Jogador 5 | 6-2 | 660 | MOVE_BENCH | ECON | 59.0 | 8 | 19 | 1 | 32.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.041545033454895 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 661 | PASS | ECON | 59.0 | 8 | 19 | 1 | 34.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03342857211828232 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 668 | MOVE_BENCH | ECON | 40.0 | 8 | 25 | 2 | 34.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5646030902862549 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 669 | MOVE_BENCH | ECON | 40.0 | 8 | 25 | 2 | 42.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3237176537513733 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 670 | MOVE_BENCH | ECON | 40.0 | 8 | 25 | 2 | 48.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.853753924369812 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 672 | BUY | STABILIZE | 23.0 | 8 | 33 | 3 | 60.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.333128958940506 | 0.0 | 0.0 | +9b92b0ec-011f-487d-b6c8-5e95ee8b37ff / -— |
| Jogador 5 | 6-4 | 673 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 60.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7883389592170715 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 674 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 60.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34395092725753784 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 675 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 58.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8507065773010254 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 676 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 60.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7883389592170715 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 677 | PASS | STABILIZE | 23.0 | 8 | 30 | 3 | 60.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24214603006839752 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 682 | BUY | STABILIZE | 23.0 | 8 | 39 | 3 | 66.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8886002898216248 | 0.0 | 0.0 | +9315c427-7094-4e56-adb5-70be515fddaa / -— |
| Jogador 5 | 6-5 | 683 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 36 | 3 | 66.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34740781784057617 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 684 | REROLL | STABILIZE | 23.0 | 8 | 36 | 3 | 64.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 685 | BUY | STABILIZE | 23.0 | 8 | 34 | 3 | 64.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08378835767507553 | 0.0 | 0.0 | +7be7d9db-fa8f-421e-93d5-5910cc3e1bf2 / -— |
| Jogador 5 | 6-5 | 686 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 64.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8224374651908875 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 687 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 64.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16702918708324432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 688 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 64.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4085314869880676 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 689 | REROLL | STABILIZE | 23.0 | 8 | 30 | 3 | 72.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 690 | BUY | STABILIZE | 23.0 | 8 | 28 | 2 | 72.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10251586139202118 | 0.0 | 0.0 | +b1e222db-5292-4836-a0b4-2fe583bea359 / -— |
| Jogador 5 | 6-6 | 692 | SELL | STABILIZE | 23.0 | 8 | 32 | 3 | 72.0 | Adaptador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -b1e222db-5292-4836-a0b4-2fe583bea359 |
| Jogador 5 | 6-6 | 693 | BUY | STABILIZE | 23.0 | 8 | 36 | 3 | 72.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9539169073104858 | 0.0 | 0.0 | +8c57b805-656c-4993-8264-71d58537a9cd / -9315c427-7094-4e56-adb5-70be515fddaa,9b92b0ec-011f-487d-b6c8-5e95ee8b37ff,b1e5b3b9-fda8-4d4a-9368-94fd558da4f7,dde5ed69-0fc4-4d15-b12c-a5252a239040 |
| Jogador 5 | 6-6 | 694 | BUY | STABILIZE | 23.0 | 8 | 33 | 3 | 54.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8577656149864197 | 0.0 | 0.0 | +ea58e457-6e29-42e7-b60f-f8c157981c75 / -— |
| Jogador 5 | 6-6 | 695 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 54.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3963225185871124 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 696 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15850789844989777 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 697 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 64.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8225255012512207 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 698 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 30 | 3 | 64.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36598557233810425 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 699 | PASS | STABILIZE | 23.0 | 8 | 30 | 3 | 56.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24214603006839752 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +5fb26eae-800c-4f7a-8caa-e94d36794159 / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032908253371715546 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.063498616218567 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 30 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5817632079124451 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 54 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08310991525650024 | 0.0 | 0.0 | +f29b0444-8dd6-44a6-9a04-824febf737a0 / -— |
| Jogador 6 | 1-3 | 55 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3136013150215149 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 56 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35743480920791626 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 81 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.26253482699394226 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 82 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4764462113380432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 83 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 106 | SELL | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08585182577371597 | 0.0 | 0.0 | +— / -5fb26eae-800c-4f7a-8caa-e94d36794159 |
| Jogador 6 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1443754881620407 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6725063323974609 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21683338284492493 | 0.0 | 0.0 | +c8b72b14-11a4-48e6-8135-41efdbc347cb / -— |
| Jogador 6 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 18.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37132954597473145 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 111 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 18.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 132 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038011156022548676 | 0.0 | 0.0 | +— / -c19cf6a8-c66e-4670-b0fc-fb83453f22e7 |
| Jogador 6 | 2-2 | 133 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.34462276101112366 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023335222154855728 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 135 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7487065196037292 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 136 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 159 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 11 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2600180506706238 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 160 | SELL | STABILIZE | 94.0 | 4 | 11 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44712308049201965 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-3 | 161 | BUY | STABILIZE | 94.0 | 4 | 14 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0235213041305542 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 162 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 163 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031179118901491165 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 164 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 12 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3487708866596222 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 165 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 166 | PASS | STABILIZE | 94.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 182 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 19 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031179118901491165 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 183 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 19 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7039525508880615 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 184 | SELL | STABILIZE | 94.0 | 4 | 19 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05937511846423149 | 0.0 | 0.0 | +— / -4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 |
| Jogador 6 | 2-4 | 185 | BUY | STABILIZE | 94.0 | 4 | 21 | 2 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.043957702815532684 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 186 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 18 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3487708866596222 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 187 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 18 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 188 | PASS | STABILIZE | 94.0 | 4 | 18 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02053571492433548 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 203 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 24 | 2 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031179118901491165 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 204 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 24 | 2 | 18.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3537225127220154 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 205 | SELL | STABILIZE | 94.0 | 4 | 24 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8841728568077087 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 206 | BUY | STABILIZE | 94.0 | 4 | 26 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3581686019897461 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 207 | SELL | STABILIZE | 94.0 | 4 | 24 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6970615386962891 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 208 | BUY | STABILIZE | 94.0 | 4 | 26 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3993517756462097 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 209 | BUY_XP | STABILIZE | 94.0 | 4 | 25 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06859000027179718 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 210 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 21 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6273468136787415 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 211 | PASS | STABILIZE | 94.0 | 5 | 21 | 2 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.021071428433060646 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 226 | BUY | STABILIZE | 94.0 | 5 | 30 | 3 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9254416823387146 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 227 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 27 | 2 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5685409903526306 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 228 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 27 | 2 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38867127895355225 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 229 | PASS | SLOWROLL | 94.0 | 5 | 27 | 2 | 26.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022142857313156128 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 245 | SELL | SLOWROLL | 94.0 | 5 | 36 | 3 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026720253750681877 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-7 | 246 | BUY | SLOWROLL | 94.0 | 5 | 37 | 3 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15502557158470154 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 247 | SELL | SLOWROLL | 94.0 | 5 | 34 | 3 | 26.0 | Defendente/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6983846426010132 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 248 | PASS | SLOWROLL | 94.0 | 5 | 37 | 3 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.038928572088479996 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 266 | BUY | SLOWROLL | 94.0 | 5 | 46 | 4 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26516658067703247 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 267 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 43 | 4 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23651695251464844 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 268 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 43 | 4 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05349862203001976 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 269 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 43 | 4 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8572202324867249 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 270 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 43 | 4 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23783139884471893 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 271 | PASS | SLOWROLL | 94.0 | 5 | 43 | 4 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1120000034570694 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 287 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 52 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05349898338317871 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 288 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 52 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3537796139717102 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 289 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 52 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 290 | PASS | SLOWROLL | 83.0 | 5 | 52 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12321005761623383 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 306 | MOVE_BENCH | SLOWROLL | 73.0 | 5 | 63 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7688936591148376 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 307 | MOVE_BENCH | SLOWROLL | 73.0 | 5 | 63 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2356388121843338 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 308 | PASS | SLOWROLL | 73.0 | 5 | 63 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12806540727615356 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 328 | MOVE_BENCH | SLOWROLL | 63.0 | 5 | 74 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 329 | MOVE_BENCH | SLOWROLL | 63.0 | 5 | 74 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7688936591148376 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 330 | PASS | SLOWROLL | 63.0 | 5 | 74 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13342425227165222 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 349 | MOVE_BENCH | SLOWROLL | 63.0 | 5 | 85 | 5 | 26.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19050072133541107 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 350 | SELL | SLOWROLL | 63.0 | 5 | 85 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014999999664723873 | 0.0 | 0.0 | +— / -c8b72b14-11a4-48e6-8135-41efdbc347cb |
| Jogador 6 | 3-5 | 351 | BUY | SLOWROLL | 63.0 | 5 | 87 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5247015357017517 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-5 | 352 | BUY_XP | SLOWROLL | 63.0 | 5 | 85 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21681000292301178 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 353 | BUY_XP | FAST8 | 63.0 | 6 | 81 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 354 | BUY_XP | FAST8 | 63.0 | 6 | 77 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 355 | BUY_XP | FAST8 | 63.0 | 6 | 73 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 356 | BUY_XP | FAST8 | 63.0 | 6 | 69 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 357 | BUY_XP | FAST8 | 63.0 | 6 | 65 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 358 | BUY_XP | FAST8 | 63.0 | 6 | 61 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 359 | PASS | FAST8 | 63.0 | 6 | 57 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15681686997413635 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 365 | SELL | FAST8 | 51.0 | 6 | 68 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4010292887687683 | 0.0 | 0.0 | +— / -5b95b64a-b46a-4827-8613-307c8dadc072 |
| Jogador 6 | 3-6 | 366 | BUY | FAST8 | 51.0 | 6 | 70 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5093426704406738 | 0.0 | 0.0 | +ab050f92-777b-429f-9ed8-9b6c63794641 / -— |
| Jogador 6 | 3-6 | 367 | BUY_XP | FAST8 | 51.0 | 6 | 68 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 368 | BUY_XP | FAST8 | 51.0 | 6 | 64 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 369 | BUY_XP | FAST8 | 51.0 | 6 | 60 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3095000088214874 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 370 | MOVE_BENCH | FAST8 | 51.0 | 7 | 56 | 5 | 28.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21788889169692993 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 371 | BUY | FAST8 | 51.0 | 7 | 56 | 5 | 32.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8748925924301147 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -ab050f92-777b-429f-9ed8-9b6c63794641,f29b0444-8dd6-44a6-9a04-824febf737a0 |
| Jogador 6 | 3-6 | 372 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 54 | 5 | 24.0 | Defendente/DA_18_Caitlyn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03804996237158775 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 373 | PASS | FAST8 | 51.0 | 7 | 54 | 5 | 32.0 | Defendente/DA_18_Caitlyn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15552203357219696 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 382 | BUY | FAST8 | 39.0 | 7 | 66 | 5 | 32.0 | Defendente/DA_18_Caitlyn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14007072150707245 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 383 | MOVE_BENCH | FAST8 | 39.0 | 7 | 61 | 5 | 32.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46631473302841187 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 384 | MOVE_BENCH | FAST8 | 39.0 | 7 | 61 | 5 | 36.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 385 | PASS | FAST8 | 39.0 | 7 | 61 | 5 | 36.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16609784960746765 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 397 | MOVE_BENCH | FAST8 | 39.0 | 7 | 61 | 5 | 36.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2371818870306015 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 402 | BUY | FAST8 | 39.0 | 7 | 73 | 5 | 42.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.00771963596344 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -2938180d-94e5-4bb7-832e-baa51f820ba2,75005e9c-56d1-48d6-815e-573e489e3dd7 |
| Jogador 6 | 4-1 | 403 | MOVE_BENCH | FAST8 | 39.0 | 7 | 70 | 5 | 30.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23277269303798676 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 404 | MOVE_BENCH | FAST8 | 39.0 | 7 | 70 | 5 | 32.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0957815870642662 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 405 | BUY | FAST8 | 39.0 | 7 | 70 | 5 | 42.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7440069317817688 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 6 | 4-1 | 406 | MOVE_BENCH | FAST8 | 39.0 | 7 | 67 | 5 | 42.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30873948335647583 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 407 | MOVE_BENCH | FAST8 | 39.0 | 7 | 67 | 5 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5214794278144836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 408 | PASS | FAST8 | 39.0 | 7 | 67 | 5 | 36.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24134626984596252 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 418 | MOVE_BENCH | FAST8 | 39.0 | 7 | 67 | 5 | 36.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38651666045188904 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 422 | BUY | STABILIZE | 27.0 | 7 | 80 | 5 | 48.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06559436768293381 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 6 | 4-2 | 423 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 76 | 5 | 48.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3464546203613281 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 424 | BUY | STABILIZE | 27.0 | 7 | 76 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4131697416305542 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 6 | 4-2 | 425 | BUY_XP | STABILIZE | 27.0 | 7 | 74 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057420000433921814 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 426 | BUY_XP | STABILIZE | 27.0 | 7 | 70 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05685000121593475 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 427 | BUY_XP | STABILIZE | 27.0 | 7 | 66 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056279998272657394 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 428 | BUY_XP | STABILIZE | 27.0 | 7 | 62 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055709999054670334 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 429 | BUY_XP | STABILIZE | 27.0 | 7 | 58 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 430 | BUY_XP | STABILIZE | 27.0 | 7 | 54 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 431 | BUY_XP | STABILIZE | 27.0 | 7 | 50 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 432 | PASS | STABILIZE | 27.0 | 7 | 46 | 4 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07914285361766815 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 440 | BUY | STABILIZE | 27.0 | 7 | 56 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18872232735157013 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-3 | 441 | BUY_XP | STABILIZE | 27.0 | 7 | 52 | 5 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 442 | BUY_XP | STABILIZE | 27.0 | 7 | 48 | 4 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 443 | BUY_XP | STABILIZE | 27.0 | 7 | 44 | 4 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 444 | BUY_XP | STABILIZE | 27.0 | 7 | 40 | 4 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 445 | BUY_XP | STABILIZE | 27.0 | 7 | 36 | 3 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4494968056678772 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 446 | BUY_XP | STABILIZE | 27.0 | 8 | 32 | 3 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 447 | BUY_XP | STABILIZE | 27.0 | 8 | 28 | 2 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 448 | BUY_XP | STABILIZE | 27.0 | 8 | 24 | 2 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 449 | BUY_XP | STABILIZE | 27.0 | 8 | 20 | 2 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 450 | PASS | STABILIZE | 27.0 | 8 | 16 | 1 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08711428940296173 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 452 | BUY | ALL_IN | 14.0 | 8 | 22 | 2 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011210386641323566 | 0.0 | 0.0 | +1f7f2a48-1318-4fc6-87cc-03d557bf69ea / -— |
| Jogador 6 | 4-4 | 453 | REROLL | ALL_IN | 14.0 | 8 | 18 | 1 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 454 | BUY | ALL_IN | 14.0 | 8 | 16 | 1 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05982096493244171 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 6 | 4-4 | 455 | BUY | ALL_IN | 14.0 | 8 | 13 | 1 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05865008011460304 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 6 | 4-4 | 456 | BUY_XP | ALL_IN | 14.0 | 8 | 11 | 1 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 457 | BUY_XP | ALL_IN | 14.0 | 8 | 7 | 0 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 458 | PASS | ALL_IN | 14.0 | 8 | 3 | 0 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 467 | MOVE_BENCH | ALL_IN | 14.0 | 8 | 3 | 0 | 56.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5785810947418213 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 472 | BUY | ALL_IN | 14.0 | 8 | 8 | 0 | 60.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29053255915641785 | 0.0 | 0.0 | +fe12befc-b473-4f91-9e51-558a03efa3ad / -— |
| Jogador 6 | 4-5 | 473 | REROLL | ALL_IN | 14.0 | 8 | 4 | 0 | 60.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 474 | REROLL | ALL_IN | 14.0 | 8 | 2 | 0 | 60.0 | Defendente/DA_18_GnarSmall | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 475 | MOVE_BENCH | ALL_IN | 14.0 | 8 | 0 | 0 | 60.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4037988781929016 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 476 | PASS | ALL_IN | 14.0 | 8 | 0 | 0 | 60.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 491 | BUY | ALL_IN | 14.0 | 8 | 6 | 0 | 60.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22358524799346924 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 6 | 4-6 | 492 | BUY | ALL_IN | 14.0 | 8 | 2 | 0 | 60.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6385601162910461 | 0.0 | 0.0 | +0fd34229-b814-4580-8651-59e712d5657f / -— |
| Jogador 6 | 4-6 | 493 | PASS | ALL_IN | 14.0 | 8 | 0 | 0 | 60.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 509 | BUY | ALL_IN | 14.0 | 8 | 5 | 0 | 60.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17462334036827087 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 6 | 4-7 | 510 | PASS | ALL_IN | 14.0 | 8 | 1 | 0 | 60.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 522 | ANVIL_CHOICE | ALL_IN | 14.0 | 8 | 6 | 0 | 60.0 | Defendente/DA_18_GnarSmall | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 523 | BUY | ALL_IN | 14.0 | 8 | 6 | 0 | 60.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.27399176359176636 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -— |
| Jogador 6 | 5-1 | 524 | REROLL | ALL_IN | 14.0 | 8 | 3 | 0 | 60.0 | Defendente/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 525 | CRAFT_AND_EQUIP | ALL_IN | 14.0 | 8 | 1 | 0 | 60.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15405790507793427 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 526 | SELL | ALL_IN | 14.0 | 8 | 1 | 0 | 60.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3365240693092346 | 0.0 | 0.0 | +— / -e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 |
| Jogador 6 | 5-1 | 527 | BUY | ALL_IN | 14.0 | 8 | 3 | 0 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27251383662223816 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 6 | 5-1 | 528 | PASS | ALL_IN | 14.0 | 8 | 0 | 0 | 60.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 540 | REROLL | ALL_IN | 14.0 | 8 | 7 | 0 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 541 | REROLL | ALL_IN | 14.0 | 8 | 5 | 0 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 542 | REROLL | ALL_IN | 14.0 | 8 | 3 | 0 | 60.0 | Defendente/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 543 | PASS | ALL_IN | 14.0 | 8 | 1 | 0 | 60.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0808350220322609 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7490466237068176 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 30 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4692978262901306 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 1.0300228595733643 | 0.0 | 0.0 | +a529e9b4-89c2-47e0-b821-7269b112f8ef / -— |
| Jogador 7 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7520930767059326 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13714881241321564 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 34 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.429470032453537 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 54 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2195654809474945 | 0.0 | 0.0 | +42edb83f-b613-45e2-95e2-d603ddf9d104 / -— |
| Jogador 7 | 1-3 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2359296977519989 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 56 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 81 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8434817790985107 | 0.0 | 0.0 | +— / -a529e9b4-89c2-47e0-b821-7269b112f8ef |
| Jogador 7 | 1-4 | 82 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.022661805152893 | 0.0 | 0.0 | +a179e7d4-31e2-4a74-9905-0daede16517e / -— |
| Jogador 7 | 1-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31174448132514954 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 85 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 106 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4030213952064514 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09662589430809021 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.561637818813324 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08821059763431549 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35290125012397766 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 111 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023938201367855072 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 112 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 132 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3097219169139862 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 133 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35309967398643494 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 134 | PASS | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 159 | SELL | STABILIZE | 95.0 | 4 | 14 | 1 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8136714100837708 | 0.0 | 0.0 | +— / -a179e7d4-31e2-4a74-9905-0daede16517e |
| Jogador 7 | 2-3 | 160 | BUY | STABILIZE | 95.0 | 4 | 16 | 1 | 14.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0227689743041992 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 7 | 2-3 | 161 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 14 | 1 | 14.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 162 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 14 | 1 | 14.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015615341253578663 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 163 | PASS | STABILIZE | 95.0 | 4 | 14 | 1 | 14.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 182 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 20 | 2 | 14.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31936773657798767 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 183 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 20 | 2 | 14.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 184 | PASS | STABILIZE | 90.0 | 4 | 20 | 2 | 14.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020892856642603874 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 203 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 27 | 2 | 14.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012051875237375498 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 204 | SELL | STABILIZE | 90.0 | 4 | 27 | 2 | 14.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38081538677215576 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-5 | 205 | BUY | STABILIZE | 90.0 | 4 | 29 | 2 | 14.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.30340901017189026 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 206 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 27 | 2 | 14.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3398191034793854 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 207 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 27 | 2 | 14.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 208 | PASS | STABILIZE | 90.0 | 4 | 27 | 2 | 14.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022142857313156128 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 226 | MOVE_BENCH | SLOWROLL | 82.0 | 5 | 35 | 3 | 14.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03914326801896095 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 227 | MOVE_BENCH | SLOWROLL | 82.0 | 5 | 35 | 3 | 14.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3821587562561035 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 228 | BUY | SLOWROLL | 82.0 | 5 | 35 | 3 | 18.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9739426374435425 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 229 | BUY_XP | SLOWROLL | 82.0 | 5 | 34 | 3 | 18.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 230 | BUY_XP | SLOWROLL | 82.0 | 5 | 30 | 3 | 18.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 231 | BUY_XP | SLOWROLL | 82.0 | 5 | 26 | 2 | 18.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 232 | BUY_XP | SLOWROLL | 82.0 | 5 | 22 | 2 | 18.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 233 | BUY_XP | SLOWROLL | 82.0 | 5 | 18 | 1 | 18.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025180000811815262 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 234 | MOVE_BENCH | SLOWROLL | 82.0 | 6 | 14 | 1 | 18.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04145139828324318 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 235 | MOVE_BENCH | SLOWROLL | 82.0 | 6 | 14 | 1 | 16.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35114821791648865 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 236 | PASS | SLOWROLL | 82.0 | 6 | 14 | 1 | 16.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 245 | MOVE_BENCH | SLOWROLL | 75.0 | 6 | 21 | 2 | 16.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3905572295188904 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 246 | MOVE_BENCH | SLOWROLL | 75.0 | 6 | 21 | 2 | 18.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6626839637756348 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 247 | BUY | SLOWROLL | 75.0 | 6 | 21 | 2 | 20.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.23852764070034027 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 248 | MOVE_BENCH | SLOWROLL | 75.0 | 6 | 18 | 1 | 20.0 | Vanguarda/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35298049449920654 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 249 | MOVE_BENCH | SLOWROLL | 75.0 | 6 | 18 | 1 | 22.0 | Vanguarda/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36057713627815247 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 250 | PASS | SLOWROLL | 75.0 | 6 | 18 | 1 | 24.0 | Vanguarda/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02053571492433548 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 266 | SELL | SLOWROLL | 75.0 | 6 | 25 | 2 | 24.0 | Vanguarda/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8760836124420166 | 0.0 | 0.0 | +— / -a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 3-1 | 267 | BUY | SLOWROLL | 75.0 | 6 | 26 | 2 | 24.0 | Vanguarda/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23742391169071198 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 268 | MOVE_BENCH | SLOWROLL | 75.0 | 6 | 23 | 2 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10847818851470947 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 269 | MOVE_BENCH | SLOWROLL | 75.0 | 6 | 23 | 2 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5969274640083313 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 270 | BUY_XP | FAST8 | 75.0 | 6 | 23 | 2 | 26.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 271 | BUY_XP | FAST8 | 75.0 | 6 | 19 | 1 | 26.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 272 | BUY_XP | FAST8 | 75.0 | 6 | 15 | 1 | 26.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 273 | BUY_XP | FAST8 | 75.0 | 6 | 11 | 1 | 26.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 274 | BUY_XP | FAST8 | 75.0 | 6 | 7 | 0 | 26.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 275 | PASS | FAST8 | 75.0 | 6 | 3 | 0 | 26.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 287 | MOVE_BENCH | FAST8 | 64.0 | 6 | 9 | 0 | 26.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4091940224170685 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 288 | BUY_XP | SLOWROLL | 64.0 | 6 | 9 | 0 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 289 | BUY_XP | SLOWROLL | 64.0 | 6 | 5 | 0 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 290 | PASS | SLOWROLL | 64.0 | 6 | 1 | 0 | 24.0 | Vanguarda/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 306 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 7 | 0 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10297411680221558 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 307 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 7 | 0 | 24.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5632855892181396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 308 | BUY | FAST8 | 64.0 | 7 | 7 | 0 | 30.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12427636235952377 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 309 | MOVE_BENCH | FAST8 | 64.0 | 7 | 4 | 0 | 30.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13877180218696594 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 310 | BUY_XP | FAST8 | 64.0 | 7 | 4 | 0 | 32.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 311 | PASS | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Vanguarda/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 328 | SELL | FAST8 | 52.0 | 7 | 5 | 0 | 32.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40556275844573975 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 3-4 | 329 | BUY | FAST8 | 52.0 | 7 | 7 | 0 | 32.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.039232008159160614 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 330 | BUY | FAST8 | 52.0 | 7 | 3 | 0 | 32.0 | Vanguarda/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7379611730575562 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 7 | 3-4 | 331 | PASS | FAST8 | 52.0 | 7 | 2 | 0 | 32.0 | Vanguarda/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 349 | SELL | FAST8 | 52.0 | 7 | 7 | 0 | 32.0 | Vanguarda/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9063845872879028 | 0.0 | 0.0 | +— / -1ff50c59-5133-459e-8bf1-d449c26efabf |
| Jogador 7 | 3-5 | 350 | SELL | FAST8 | 52.0 | 7 | 8 | 0 | 32.0 | Vanguarda/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3052347004413605 | 0.0 | 0.0 | +— / -86c1ac55-598e-426a-86ea-64249f82b085 |
| Jogador 7 | 3-5 | 351 | BUY | FAST8 | 52.0 | 7 | 12 | 1 | 32.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6539920568466187 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 352 | BUY | FAST8 | 52.0 | 7 | 9 | 0 | 32.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7590435147285461 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -4367c039-e64e-4a3c-a49f-57cb2674a08f,de82e676-8d8b-4437-958e-a8398a3cfade |
| Jogador 7 | 3-5 | 353 | MOVE_BENCH | STABILIZE | 52.0 | 7 | 7 | 0 | 24.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3796960413455963 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 354 | MOVE_BENCH | FAST8 | 52.0 | 7 | 7 | 0 | 32.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5460686683654785 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 355 | PASS | FAST8 | 52.0 | 7 | 7 | 0 | 38.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 365 | BUY | FAST8 | 40.0 | 7 | 13 | 1 | 38.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11877194046974182 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 366 | MOVE_BENCH | FAST8 | 40.0 | 7 | 9 | 0 | 38.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2710922360420227 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 367 | BUY | FAST8 | 40.0 | 7 | 9 | 0 | 40.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044010043144226074 | 0.0 | 0.0 | +6caec849-54f8-4ec1-90a4-fc0587510013 / -— |
| Jogador 7 | 3-6 | 368 | BUY_XP | FAST8 | 40.0 | 7 | 5 | 0 | 40.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 369 | PASS | FAST8 | 40.0 | 7 | 1 | 0 | 40.0 | Vanguarda/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 382 | BUY | STABILIZE | 27.0 | 7 | 7 | 0 | 40.0 | Vanguarda/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8018221855163574 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 383 | PASS | STABILIZE | 27.0 | 7 | 3 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 402 | BUY | STABILIZE | 27.0 | 7 | 9 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2256394475698471 | 0.0 | 0.0 | +6a30a366-c631-429d-9523-af769cdf48a4 / -— |
| Jogador 7 | 4-1 | 403 | BUY_XP | STABILIZE | 27.0 | 7 | 6 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 404 | PASS | STABILIZE | 27.0 | 7 | 2 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 422 | BUY | STABILIZE | 27.0 | 7 | 8 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25328609347343445 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -— |
| Jogador 7 | 4-2 | 423 | PASS | STABILIZE | 27.0 | 7 | 6 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 440 | BUY | ALL_IN | 15.0 | 7 | 11 | 1 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3938976228237152 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 7 | 4-3 | 441 | BUY | ALL_IN | 15.0 | 7 | 8 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017043158411979675 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 7 | 4-3 | 442 | REROLL | ALL_IN | 15.0 | 7 | 4 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 443 | BUY | ALL_IN | 15.0 | 7 | 2 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7928115129470825 | 0.0 | 0.0 | +3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 / -— |
| Jogador 7 | 4-3 | 444 | PASS | ALL_IN | 15.0 | 7 | 0 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 452 | BUY | ALL_IN | 15.0 | 7 | 6 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19309112429618835 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 7 | 4-4 | 453 | REROLL | ALL_IN | 15.0 | 7 | 2 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 454 | SELL | ALL_IN | 15.0 | 7 | 0 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0634923055768013 | 0.0 | 0.0 | +— / -0803068a-0141-4e75-ab81-12bb13986025 |
| Jogador 7 | 4-4 | 455 | BUY | ALL_IN | 15.0 | 7 | 2 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7977874279022217 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -— |
| Jogador 7 | 4-4 | 456 | PASS | ALL_IN | 15.0 | 7 | 1 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 472 | REROLL | ALL_IN | 15.0 | 7 | 6 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 473 | REROLL | ALL_IN | 15.0 | 7 | 4 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 474 | REROLL | ALL_IN | 15.0 | 7 | 2 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 475 | PASS | ALL_IN | 15.0 | 7 | 0 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02 |
| Jogador 8 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +d40a14f6-4b32-4cf9-8eb7-2778414b099a / -— |
| Jogador 8 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.011937879957258701 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8217591643333435 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 30 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5078703761100769 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 1.0163516998291016 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8123393058776855 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2483258843421936 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 34 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13030986487865448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 54 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.15013419091701508 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 55 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2650611400604248 | 0.0 | 0.0 | +f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 / -— |
| Jogador 8 | 1-3 | 56 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 81 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4289169907569885 | 0.0 | 0.0 | +— / -f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 |
| Jogador 8 | 1-4 | 82 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1167714595794678 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -78019889-2624-4adb-917b-619681f23053,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 1-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2821456789970398 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 84 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 106 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.39378562569618225 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27171942591667175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 108 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.03920578956604 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5191993117332458 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 111 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 132 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0385910272598267 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 133 | BUY_XP | STABILIZE | 100.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 134 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 135 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4862423539161682 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 136 | PASS | SLOWROLL | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 159 | BUY | SLOWROLL | 100.0 | 5 | 10 | 1 | 12.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09097443521022797 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 160 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47183576226234436 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 161 | BUY_XP | SLOWROLL | 100.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 162 | PASS | SLOWROLL | 100.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 182 | BUY_XP | SLOWROLL | 95.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 183 | BUY_XP | SLOWROLL | 95.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 184 | PASS | SLOWROLL | 95.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 203 | SELL | SLOWROLL | 95.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8617753982543945 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-5 | 204 | BUY | SLOWROLL | 95.0 | 5 | 6 | 0 | 16.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31693071126937866 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 205 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 3 | 0 | 16.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2414645403623581 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 206 | PASS | SLOWROLL | 95.0 | 5 | 3 | 0 | 20.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 226 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 9 | 0 | 20.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5042626857757568 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 227 | BUY | SLOWROLL | 89.0 | 6 | 9 | 0 | 22.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08876638859510422 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 228 | MOVE_BOARD | SLOWROLL | 89.0 | 6 | 5 | 0 | 22.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17290917038917542 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 229 | BUY_XP | SLOWROLL | 89.0 | 6 | 5 | 0 | 22.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 230 | PASS | SLOWROLL | 89.0 | 6 | 1 | 0 | 22.0 | Defendente/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 245 | SELL | SLOWROLL | 84.0 | 6 | 7 | 0 | 22.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32095953822135925 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 2-7 | 246 | BUY | SLOWROLL | 84.0 | 6 | 11 | 1 | 22.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24587370455265045 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 8 | 2-7 | 247 | MOVE_BENCH | SLOWROLL | 84.0 | 6 | 9 | 0 | 22.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09647473692893982 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 248 | BUY_XP | SLOWROLL | 84.0 | 6 | 9 | 0 | 20.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 249 | BUY_XP | SLOWROLL | 84.0 | 6 | 5 | 0 | 20.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 250 | PASS | SLOWROLL | 84.0 | 6 | 1 | 0 | 20.0 | Defendente/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 266 | SELL | SLOWROLL | 84.0 | 6 | 7 | 0 | 20.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34470823407173157 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 3-1 | 267 | BUY | SLOWROLL | 84.0 | 6 | 10 | 1 | 20.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12125121802091599 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 268 | MOVE_BENCH | SLOWROLL | 84.0 | 6 | 6 | 0 | 20.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5378669500350952 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 269 | BUY_XP | SLOWROLL | 84.0 | 6 | 6 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 270 | PASS | SLOWROLL | 84.0 | 6 | 2 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 287 | SELL | SLOWROLL | 84.0 | 6 | 8 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4213865101337433 | 0.0 | 0.0 | +— / -d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 8 | 3-2 | 288 | BUY | SLOWROLL | 84.0 | 6 | 10 | 1 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13531456887722015 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-2 | 289 | MOVE_BENCH | SLOWROLL | 84.0 | 6 | 8 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2836708128452301 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 290 | MOVE_BENCH | SLOWROLL | 84.0 | 6 | 8 | 0 | 20.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29866093397140503 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 291 | PASS | FAST8 | 84.0 | 6 | 8 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 306 | BUY_XP | FAST8 | 73.0 | 6 | 13 | 1 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 307 | BUY_XP | FAST8 | 73.0 | 6 | 9 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 308 | BUY_XP | FAST8 | 73.0 | 6 | 5 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08320000022649765 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 309 | PASS | FAST8 | 73.0 | 7 | 1 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 321 | MOVE_BENCH | FAST8 | 73.0 | 7 | 1 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.527593195438385 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 328 | BUY | FAST8 | 73.0 | 7 | 7 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.24821820855140686 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 329 | BUY_XP | FAST8 | 73.0 | 7 | 4 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 330 | PASS | FAST8 | 73.0 | 7 | 0 | 0 | 28.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 349 | SELL | FAST8 | 73.0 | 7 | 5 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3704862594604492 | 0.0 | 0.0 | +— / -d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 3-5 | 350 | BUY | FAST8 | 73.0 | 7 | 8 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7344005107879639 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -— |
| Jogador 8 | 3-5 | 351 | MOVE_BENCH | FAST8 | 73.0 | 7 | 6 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 352 | BUY_XP | FAST8 | 73.0 | 7 | 6 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 353 | PASS | FAST8 | 73.0 | 7 | 2 | 0 | 28.0 | Defendente/DA_18_Leona | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 365 | SELL | FAST8 | 61.0 | 7 | 7 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8432638049125671 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 8 | 3-6 | 366 | BUY | FAST8 | 61.0 | 7 | 9 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21266838908195496 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 367 | MOVE_BENCH | FAST8 | 61.0 | 7 | 6 | 0 | 28.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15462568402290344 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 368 | BUY_XP | FAST8 | 61.0 | 7 | 6 | 0 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 369 | PASS | FAST8 | 61.0 | 7 | 2 | 0 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 382 | BUY_XP | FAST8 | 50.0 | 7 | 8 | 0 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 383 | BUY_XP | FAST8 | 50.0 | 7 | 4 | 0 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 384 | PASS | FAST8 | 50.0 | 7 | 0 | 0 | 30.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 402 | CRAFT_AND_EQUIP | FAST8 | 50.0 | 7 | 6 | 0 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16682426631450653 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 403 | BUY | FAST8 | 50.0 | 7 | 6 | 0 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01054183766245842 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 404 | PASS | FAST8 | 50.0 | 7 | 3 | 0 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 422 | PASS | FAST8 | 50.0 | 7 | 9 | 0 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 440 | PASS | FAST8 | 50.0 | 7 | 17 | 1 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10642857104539871 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 452 | BUY | STABILIZE | 38.0 | 7 | 23 | 2 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8703091144561768 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 8 | 4-4 | 453 | PASS | STABILIZE | 38.0 | 7 | 20 | 2 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1127195730805397 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 472 | BUY | STABILIZE | 38.0 | 7 | 27 | 2 | 30.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9083343744277954 | 0.0 | 0.0 | +738fea60-6b44-40f1-9936-43accf852bd7 / -630d9254-3856-4d88-b981-43a8270b4b3d,f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 4-5 | 473 | BUY | STABILIZE | 38.0 | 7 | 26 | 2 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8437087535858154 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 8 | 4-5 | 474 | BUY_XP | STABILIZE | 38.0 | 7 | 23 | 2 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10844375193119049 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 475 | BUY_XP | STABILIZE | 38.0 | 7 | 19 | 1 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028443749994039536 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 476 | BUY_XP | STABILIZE | 38.0 | 7 | 15 | 1 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028443749994039536 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 477 | BUY_XP | STABILIZE | 38.0 | 7 | 11 | 1 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10844375193119049 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 478 | BUY_XP | STABILIZE | 38.0 | 7 | 7 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031214062124490738 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 479 | MOVE_BENCH | STABILIZE | 38.0 | 8 | 3 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6520869135856628 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 480 | MOVE_BENCH | STABILIZE | 38.0 | 8 | 3 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3985386788845062 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 481 | MOVE_BENCH | STABILIZE | 38.0 | 8 | 3 | 0 | 32.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 482 | PASS | STABILIZE | 38.0 | 8 | 3 | 0 | 32.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 491 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 9 | 0 | 32.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2073262482881546 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 492 | BUY | STABILIZE | 23.0 | 8 | 9 | 0 | 32.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8381593823432922 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -— |
| Jogador 8 | 4-6 | 493 | REROLL | STABILIZE | 23.0 | 8 | 7 | 0 | 32.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 494 | BUY | STABILIZE | 23.0 | 8 | 5 | 0 | 32.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879386842250824 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 8 | 4-6 | 495 | REROLL | STABILIZE | 23.0 | 8 | 4 | 0 | 32.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 496 | BUY | STABILIZE | 23.0 | 8 | 2 | 0 | 32.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1109563410282135 | 0.0 | 0.0 | +811fcf1f-2023-4c36-a961-d61cb0dd68d0 / -— |
| Jogador 8 | 4-6 | 497 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 0 | 0 | 32.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3238353729248047 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 498 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 0 | 0 | 30.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 499 | PASS | STABILIZE | 23.0 | 8 | 0 | 0 | 30.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 503 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 0 | 0 | 30.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2163119614124298 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 509 | BUY | ALL_IN | 11.0 | 8 | 6 | 0 | 34.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13858449459075928 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -— |
| Jogador 8 | 4-7 | 510 | BUY | ALL_IN | 11.0 | 8 | 3 | 0 | 34.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03312152251601219 | 0.0 | 0.0 | +6594349f-ecaa-4212-b063-815acae6d0bb / -— |
| Jogador 8 | 4-7 | 511 | PASS | ALL_IN | 11.0 | 8 | 0 | 0 | 34.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 522 | ANVIL_CHOICE | ALL_IN | 11.0 | 8 | 6 | 0 | 40.0 | Defendente/DA_18_Leona | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 523 | BUY | ALL_IN | 11.0 | 8 | 6 | 0 | 40.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5347042679786682 | 0.0 | 0.0 | +4e6b6f57-7f94-46ba-b832-c3198d4a5949 / -— |
| Jogador 8 | 5-1 | 524 | BUY | ALL_IN | 11.0 | 8 | 3 | 0 | 40.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08248347789049149 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -— |
| Jogador 8 | 5-1 | 525 | PASS | ALL_IN | 11.0 | 8 | 0 | 0 | 40.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 540 | REROLL | ALL_IN | 11.0 | 8 | 6 | 0 | 40.0 | Defendente/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 541 | REROLL | ALL_IN | 11.0 | 8 | 4 | 0 | 40.0 | Defendente/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 542 | REROLL | ALL_IN | 11.0 | 8 | 2 | 0 | 40.0 | Defendente/DA_18_Leona | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 543 | PASS | ALL_IN | 11.0 | 8 | 0 | 0 | 40.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 552 | REROLL | ALL_IN | 11.0 | 8 | 7 | 0 | 40.0 | Defendente/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 553 | REROLL | ALL_IN | 11.0 | 8 | 5 | 0 | 40.0 | Defendente/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 554 | REROLL | ALL_IN | 11.0 | 8 | 3 | 0 | 40.0 | Defendente/DA_18_Leona | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 555 | SELL | ALL_IN | 11.0 | 8 | 1 | 0 | 40.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06364615261554718 | 0.0 | 0.0 | +— / -b6883c6a-7149-4088-8506-20bd8dfed6a5 |
| Jogador 8 | 5-3 | 556 | BUY | ALL_IN | 11.0 | 8 | 4 | 0 | 40.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8239949941635132 | 0.0 | 0.0 | +9c3b3b78-e99c-4947-b958-cce156ecccb1 / -23366968-ed3f-43d0-9f24-bb7691bf5d45,ddae48a6-5360-4660-9fa1-143ac35635ee |
| Jogador 8 | 5-3 | 557 | BUY | ALL_IN | 11.0 | 8 | 1 | 0 | 34.0 | Defendente/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2573855519294739 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -— |
| Jogador 8 | 5-3 | 558 | PASS | ALL_IN | 11.0 | 8 | 0 | 0 | 34.0 | Defendente/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 564 | MOVE_BENCH | ALL_IN | 11.0 | 8 | 0 | 0 | 34.0 | Defendente/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45453140139579773 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 122 | 146 | 26 | 6 | 12 | 1 | 1 | 0 | 0 | 54.0 |
- Jogador 1 — gasto por ação: BUY: 88g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 10g, stage 2: 52g, stage 3: 47g, stage 4: 37g
| Jogador 2 | 224 | 356 | 143 | 31 | 22 | 1 | 19 | 0 | 28 | 52.0 |
- Jogador 2 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 214g, BUY_XP: 104g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 38g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 6g, stage 2: 45g, stage 3: 55g, stage 4: 74g, stage 5: 99g, stage 6: 77g
| Jogador 3 | 135 | 184 | 43 | 16 | 18 | 0 | 1 | 0 | 0 | 54.0 |
- Jogador 3 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 98g, BUY_XP: 84g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 5g, stage 2: 46g, stage 3: 66g, stage 4: 60g, stage 5: 7g
| Jogador 4 | 135 | 185 | 15 | 5 | 19 | 0 | 5 | 1 | 0 | 58.0 |
- Jogador 4 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 83g, BUY_XP: 92g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 10g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 49g, stage 3: 46g, stage 4: 46g, stage 5: 38g
| Jogador 5 | 208 | 289 | 81 | 20 | 22 | 1 | 7 | 1 | 30 | 56.0 |
- Jogador 5 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 171g, BUY_XP: 104g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 14g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 51g, stage 3: 58g, stage 4: 54g, stage 5: 58g, stage 6: 61g
| Jogador 6 | 158 | 218 | 23 | 9 | 25 | 2 | 7 | 1 | 1 | 60.0 |
- Jogador 6 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 88g, BUY_XP: 116g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 14g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 26g, stage 3: 54g, stage 4: 117g, stage 5: 14g
| Jogador 7 | 118 | 136 | 17 | 8 | 14 | 1 | 5 | 1 | 0 | 40.0 |
- Jogador 7 — gasto por ação: BUY: 66g, BUY_XP: 60g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 10g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 7g, stage 2: 32g, stage 3: 64g, stage 4: 33g
| Jogador 8 | 130 | 169 | 20 | 8 | 19 | 1 | 8 | 1 | 0 | 40.0 |
- Jogador 8 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 65g, BUY_XP: 88g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 16g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 5g, stage 2: 47g, stage 3: 50g, stage 4: 45g, stage 5: 22g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 14 | 5 |
- Jogador 1 · 2-3 · step 163: PASS com 8g, HP 89, nível 4/8 (STABILIZE).
- Jogador 1 · 4-2 · step 425: PASS com 4g, HP 43, nível 7/8 (FAST8).
- Jogador 1 · 4-3 · step 441: PASS com 6g, HP 31, nível 7/8 (STABILIZE).
- Jogador 1 · 4-4 · step 454: PASS com 6g, HP 18, nível 7/8 (STABILIZE).
- Jogador 1 · 4-5 · step 474: REROLL com 4g, HP 18, nível 7/8 (STABILIZE).
| Jogador 2 | 26 | 3 |
- Jogador 2 · 2-4 · step 186: PASS com 6g, HP 100, nível 5/8 (STABILIZE).
- Jogador 2 · 2-5 · step 205: PASS com 12g, HP 100, nível 5/8 (STABILIZE).
- Jogador 2 · 3-7 · step 386: PASS com 11g, HP 88, nível 7/8 (FAST8).
| Jogador 3 | 21 | 3 |
- Jogador 3 · 2-7 · step 249: PASS com 8g, HP 85, nível 6/8 (FAST8).
- Jogador 3 · 3-1 · step 268: PASS com 12g, HP 85, nível 6/8 (FAST8).
- Jogador 3 · 3-7 · step 385: PASS com 6g, HP 74, nível 7/8 (FAST8).
| Jogador 4 | 23 | 1 |
- Jogador 4 · 1-4 · step 83: PASS com 4g, HP 100, nível 3/8 (STABILIZE).
| Jogador 5 | 26 | 2 |
- Jogador 5 · 2-2 · step 136: PASS com 7g, HP 95, nível 4/8 (STABILIZE).
- Jogador 5 · 2-6 · step 231: PASS com 6g, HP 91, nível 6/8 (FAST8).
| Jogador 6 | 29 | 9 |
- Jogador 6 · 2-2 · step 136: PASS com 6g, HP 100, nível 4/8 (STABILIZE).
- Jogador 6 · 2-3 · step 166: PASS com 12g, HP 94, nível 4/8 (STABILIZE).
- Jogador 6 · 2-4 · step 188: PASS com 18g, HP 94, nível 4/8 (STABILIZE).
- Jogador 6 · 2-5 · step 211: PASS com 21g, HP 94, nível 5/8 (STABILIZE).
- Jogador 6 · 3-5 · step 359: PASS com 57g, HP 63, nível 6/8 (FAST8).
- Jogador 6 · 3-6 · step 373: PASS com 54g, HP 51, nível 7/8 (FAST8).
- Jogador 6 · 3-7 · step 385: PASS com 61g, HP 39, nível 7/8 (FAST8).
- Jogador 6 · 4-1 · step 408: PASS com 67g, HP 39, nível 7/8 (FAST8).
- Jogador 6 · 4-2 · step 432: PASS com 46g, HP 27, nível 7/8 (STABILIZE).
| Jogador 7 | 15 | 9 |
- Jogador 7 · 2-2 · step 134: PASS com 8g, HP 95, nível 4/8 (STABILIZE).
- Jogador 7 · 2-3 · step 163: PASS com 14g, HP 95, nível 4/8 (STABILIZE).
- Jogador 7 · 2-4 · step 184: PASS com 20g, HP 90, nível 4/8 (STABILIZE).
- Jogador 7 · 2-5 · step 208: PASS com 27g, HP 90, nível 4/8 (STABILIZE).
- Jogador 7 · 3-5 · step 355: PASS com 7g, HP 52, nível 7/8 (FAST8).
- Jogador 7 · 4-2 · step 423: PASS com 6g, HP 27, nível 7/8 (STABILIZE).
- Jogador 7 · 4-3 · step 442: REROLL com 4g, HP 15, nível 7/8 (ALL_IN).
- Jogador 7 · 4-5 · step 472: REROLL com 6g, HP 15, nível 7/8 (ALL_IN).
- Jogador 7 · 4-5 · step 473: REROLL com 4g, HP 15, nível 7/8 (ALL_IN).
| Jogador 8 | 22 | 6 |
- Jogador 8 · 1-4 · step 84: PASS com 4g, HP 100, nível 3/8 (STABILIZE).
- Jogador 8 · 2-1 · step 111: PASS com 6g, HP 100, nível 4/8 (STABILIZE).
- Jogador 8 · 3-2 · step 291: PASS com 8g, HP 84, nível 6/8 (FAST8).
- Jogador 8 · 4-2 · step 422: PASS com 9g, HP 50, nível 7/8 (FAST8).
- Jogador 8 · 4-3 · step 440: PASS com 17g, HP 50, nível 7/8 (FAST8).
- Jogador 8 · 4-4 · step 453: PASS com 20g, HP 38, nível 7/8 (STABILIZE).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 3 | 3 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 122 | 25 | 24 | 73 | 0.0048 | -0.0485 | 0.0013 | 0.4276 | 0.0035 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0267 (35 ações), BUY_XP: Δ 0.0000 (14 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0369 (33 ações), MOVE_BOARD: Δ -0.0276 (2 ações), PASS: Δ 0.0000 (24 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0300 (12 ações)
| Jogador 2 | 224 | 25 | 28 | 171 | -0.0016 | -0.4801 | -0.0044 | 0.5589 | 0.0028 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (2 ações), BUY: Δ -0.0158 (67 ações), BUY_XP: Δ 0.0000 (26 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0070 (33 ações), MOVE_BOARD: Δ 0.0833 (1 ações), PASS: Δ 0.0000 (34 ações), REROLL: Δ 0.0000 (19 ações), SELL: Δ 0.0095 (40 ações)
| Jogador 3 | 135 | 21 | 20 | 94 | 0.0030 | -0.1131 | -0.0013 | 0.5339 | 0.0043 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0192 (36 ações), BUY_XP: Δ 0.0000 (21 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0228 (34 ações), MOVE_BOARD: Δ -0.0383 (1 ações), PASS: Δ 0.0000 (26 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0257 (14 ações)
| Jogador 4 | 135 | 13 | 19 | 103 | -0.0003 | -0.6538 | -0.0043 | 0.4010 | 0.0040 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0194 (30 ações), BUY_XP: Δ 0.0000 (23 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0175 (31 ações), MOVE_BOARD: Δ -0.0209 (3 ações), PASS: Δ 0.0000 (31 ações), REROLL: Δ 0.0000 (5 ações), SELL: Δ 0.0060 (10 ações)
| Jogador 5 | 208 | 28 | 26 | 154 | 0.0009 | -0.3085 | -0.0019 | 0.5508 | 0.0029 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (2 ações), BUY: Δ -0.0197 (56 ações), BUY_XP: Δ 0.0000 (26 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0230 (49 ações), MOVE_BOARD: Δ -0.1311 (1 ações), PASS: Δ 0.0000 (36 ações), REROLL: Δ 0.0000 (7 ações), SELL: Δ 0.0103 (29 ações)
| Jogador 6 | 158 | 9 | 20 | 129 | -0.0037 | -0.6497 | -0.0068 | 0.5682 | 0.0031 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ 0.0054 (32 ações), BUY_XP: Δ 0.0000 (29 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0057 (48 ações), MOVE_BOARD: Δ -0.4892 (1 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0000 (7 ações), SELL: Δ 0.0000 (12 ações)
| Jogador 7 | 118 | 13 | 12 | 93 | 0.0028 | -0.0837 | -0.0017 | 0.5005 | 0.0045 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0178 (27 ações), BUY_XP: Δ 0.0000 (15 ações), MOVE_BENCH: Δ 0.0214 (37 ações), MOVE_BOARD: Δ -0.0383 (1 ações), PASS: Δ 0.0000 (23 ações), REROLL: Δ 0.0000 (5 ações), SELL: Δ 0.0060 (10 ações)
| Jogador 8 | 130 | 15 | 18 | 97 | -0.0003 | -0.1496 | -0.0029 | 0.4069 | 0.0027 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0126 (30 ações), BUY_XP: Δ 0.0000 (22 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0061 (29 ações), MOVE_BOARD: Δ 0.1693 (2 ações), PASS: Δ 0.0000 (28 ações), REROLL: Δ 0.0000 (8 ações), SELL: Δ 0.0200 (9 ações)
- Jogador 1 — rounds avaliados: 24; correlação estrutural/combate: -0.081; posicional/combate: 0.374.
- Jogador 1 — combate positive: score estrutural prévio -0.035
  score posicional prévio 0.522
- Jogador 1 — combate negative: score estrutural prévio -0.007
  score posicional prévio 0.429
- Jogador 2 — rounds avaliados: 38; correlação estrutural/combate: 0.347; posicional/combate: 0.131.
- Jogador 2 — combate positive: score estrutural prévio -0.298
  score posicional prévio 0.578
- Jogador 2 — combate negative: score estrutural prévio -0.709
  score posicional prévio 0.559
- Jogador 3 — rounds avaliados: 26; correlação estrutural/combate: 0.431; posicional/combate: 0.034.
- Jogador 3 — combate positive: score estrutural prévio -0.020
  score posicional prévio 0.573
- Jogador 3 — combate negative: score estrutural prévio -0.212
  score posicional prévio 0.551
- Jogador 4 — rounds avaliados: 31; correlação estrutural/combate: 0.170; posicional/combate: -0.027.
- Jogador 4 — combate positive: score estrutural prévio -0.665
  score posicional prévio 0.404
- Jogador 4 — combate negative: score estrutural prévio -0.861
  score posicional prévio 0.414
- Jogador 5 — rounds avaliados: 38; correlação estrutural/combate: 0.171; posicional/combate: 0.253.
- Jogador 5 — combate positive: score estrutural prévio -0.307
  score posicional prévio 0.577
- Jogador 5 — combate negative: score estrutural prévio -0.471
  score posicional prévio 0.538
- Jogador 6 — rounds avaliados: 27; correlação estrutural/combate: 0.007; posicional/combate: -0.149.
- Jogador 6 — combate positive: score estrutural prévio -0.653
  score posicional prévio 0.577
- Jogador 6 — combate negative: score estrutural prévio -0.686
  score posicional prévio 0.609
- Jogador 7 — rounds avaliados: 23; correlação estrutural/combate: 0.001; posicional/combate: -0.066.
- Jogador 7 — combate positive: score estrutural prévio -0.095
  score posicional prévio 0.545
- Jogador 7 — combate negative: score estrutural prévio -0.088
  score posicional prévio 0.529
- Jogador 8 — rounds avaliados: 28; correlação estrutural/combate: 0.396; posicional/combate: -0.183.
- Jogador 8 — combate positive: score estrutural prévio -0.085
  score posicional prévio 0.401
- Jogador 8 — combate negative: score estrutural prévio -0.238
  score posicional prévio 0.433

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 145 | OK (145) | 1 | 0 | 0 | 0 | 1 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_IonicSpark; eventos: COMPONENT_LOOT_GRANTED: 16.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak.
| Jogador 2 | 261 | OK (261) | 0 | 2 | 0 | 1 | 2 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_BlueBuff, TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 2, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
- Jogador 2 — bigornas: 2 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_Spatula, TFT_Item_TearOfTheGoddess.
- Jogador 2 — bigorna 5-1 step 522: seleção TFT_Item_TearOfTheGoddess entre TFT_Item_TearOfTheGoddess, TFT_Item_ChainVest, TFT_Item_FryingPan; consistente: True; fit 0.0.
- Jogador 2 — bigorna 6-1 step 632: seleção TFT_Item_IonicSpark entre TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_InfinityEdge, DA_18_EmblemBlossom; consistente: True; fit 0.0.
| Jogador 3 | 160 | OK (160) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 3 — IDs equipados observados: TFT_Item_JeweledGauntlet; eventos: COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
- Jogador 3 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_NeedlesslyLargeRod, TFT_Item_Spatula.
- Jogador 3 — bigorna 5-1 step 522: seleção TFT_Item_SparringGloves entre TFT_Item_SparringGloves, TFT_Item_FryingPan, TFT_Item_Spatula; consistente: True; fit 0.0.
| Jogador 4 | 165 | OK (165) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 4 — IDs equipados observados: TFT_Item_Redemption; eventos: COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
- Jogador 4 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_TearOfTheGoddess.
- Jogador 4 — bigorna 5-1 step 522: seleção TFT_Item_BFSword entre TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak; consistente: True; fit 0.0.
| Jogador 5 | 246 | OK (246) | 0 | 2 | 0 | 1 | 2 | 1 |
- Jogador 5 — IDs equipados observados: TFT_Item_ThiefsGloves, TFT_Item_TitansResolve; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 2, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
- Jogador 5 — bigornas: 2 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_FryingPan.
- Jogador 5 — bigorna 5-1 step 522: seleção TFT_Item_RecurveBow entre TFT_Item_RecurveBow, TFT_Item_FryingPan, TFT_Item_GiantsBelt; consistente: True; fit 0.0.
- Jogador 5 — bigorna 6-1 step 632: seleção TFT_Item_ThiefsGloves entre TFT_Item_ThiefsGloves, TFT_Item_JeweledGauntlet, DA_18_EmblemExecutioner, TFT_Item_BrambleVest; consistente: True; fit 0.0.
| Jogador 6 | 184 | OK (184) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 6 — IDs equipados observados: TFT_Item_Quicksilver; eventos: COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
- Jogador 6 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_SparringGloves, TFT_Item_Spatula.
- Jogador 6 — bigorna 5-1 step 522: seleção TFT_Item_NegatronCloak entre TFT_Item_NegatronCloak, TFT_Item_GiantsBelt, TFT_Item_BFSword; consistente: True; fit 0.0.
| Jogador 7 | 140 | OK (140) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 7 — IDs equipados observados: nenhum observado; eventos: COMPONENT_LOOT_GRANTED: 16.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 0 (conversões observadas: 0); componentes persistentes entre rounds: TFT_Item_SparringGloves, TFT_Item_Spatula.
- Jogador 7 — revisão de conversão: componentes foram observados, mas nenhuma ação de craft/equip foi registrada; isso não prova receita viável.
| Jogador 8 | 157 | OK (157) | 0 | 1 | 0 | 1 | 1 | 0 |
- Jogador 8 — IDs equipados observados: TFT_Item_Crownguard; eventos: COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
- Jogador 8 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_NegatronCloak.
- Jogador 8 — bigorna 5-1 step 522: seleção TFT_Item_NegatronCloak entre TFT_Item_NegatronCloak, TFT_Item_Spatula, TFT_Item_RecurveBow; consistente: True; fit 0.0.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.060 | 0.000 |
| Jogador 1 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.006 | 0.000 |
| Jogador 1 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.020 | 0.000 |
| Jogador 1 | 1-4 | 6 | 2.000 | -4.000 | 0 → 0 | 1 → 2 | 11% → 14% | 3 → 4 | 5 | 3 → 4 | -0.005 | 0.000 |
| Jogador 1 | 2-1 | 7 | 4.000 | 0.000 | 0 → 1 | 2 → 1 | 14% → 14% | 4 → 6 | 3 | 4 → 4 | -0.016 | -0.339 |
| Jogador 1 | 2-2 | 9 | 4.000 | 4.000 | 1 → 1 | 1 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | -0.281 |
| Jogador 1 | 2-3 | 6 | 0.000 | 0.000 | 1 → 0 | 1 → 1 | 14% → 14% | 8 → 14 | 2 | 4 → 5 | -0.006 | -0.448 |
| Jogador 1 | 2-4 | 10 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 14% → 18% | 14 → 6 | 17 | 5 → 5 | 0.020 | 0.000 |
| Jogador 1 | 2-5 | 8 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 8 | 9 | 5 → 6 | 0.000 | -0.310 |
| Jogador 1 | 2-6 | 8 | 4.000 | -2.000 | 0 → 0 | 1 → 2 | 18% → 21% | 8 → 9 | 8 | 6 → 6 | 0.006 | 0.344 |
| Jogador 1 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 3-1 | 6 | 2.000 | 2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 6 → 7 | 7 | 6 → 6 | 0.000 | 0.475 |
| Jogador 1 | 3-2 | 5 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 6 | 8 | 6 → 6 | -0.012 | -0.535 |
| Jogador 1 | 3-3 | 5 | 0.000 | -2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 6 → 9 | 7 | 6 → 6 | 0.012 | 0.562 |
| Jogador 1 | 3-4 | 5 | 6.000 | -2.000 | 0 → 0 | 2 → 2 | 21% → 25% | 9 → 8 | 6 | 6 → 7 | -0.023 | 0.000 |
| Jogador 1 | 3-5 | 9 | 4.000 | -4.000 | 0 → 1 | 2 → 1 | 25% → 25% | 8 → 6 | 9 | 7 → 7 | 0.021 | -0.297 |
| Jogador 1 | 3-6 | 7 | 6.000 | 0.000 | 1 → 2 | 1 → 1 | 25% → 25% | 6 → 7 | 5 | 7 → 7 | -0.002 | -0.382 |
| Jogador 1 | 3-7 | 7 | -2.000 | 12.000 | 2 → 1 | 1 → 1 | 25% → 25% | 7 → 8 | 5 | 7 → 7 | 0.028 | 0.000 |
| Jogador 1 | 4-1 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 7 | 7 | 7 → 7 | 0.000 | 0.577 |
| Jogador 1 | 4-2 | 6 | 12.000 | -12.000 | 1 → 3 | 1 → 0 | 25% → 25% | 7 → 9 | 3 | 7 → 7 | -0.015 | -0.444 |
| Jogador 1 | 4-3 | 3 | 0.000 | 6.000 | 3 → 3 | 0 → 0 | 25% → 25% | 9 → 12 | 3 | 7 → 7 | 0.000 | -0.917 |
| Jogador 1 | 4-4 | 4 | 0.000 | 12.000 | 3 → 3 | 0 → 0 | 25% → 25% | 12 → 12 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 6 | 0.000 | 20.000 | 3 → 3 | 0 → 0 | 25% → 25% | 12 → 6 | 12 | 7 → 7 | 0.000 | -0.450 |
| Jogador 1 | 4-6 | 4 | -54.000 | -44.000 | 3 → 0 | 0 → 0 | 25% → 0% | 6 → 0 | 6 | 7 → 7 | -0.147 | -0.696 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 7, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 25 ações e piorou em 25.
- Jogador 1 — estado final: ouro 0, nível 7, vida 5.0, colocação 7.
| Jogador 2 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.060 | 0.000 |
| Jogador 2 | 1-2 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.000 | 0.000 |
| Jogador 2 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | 0.034 | 0.000 |
| Jogador 2 | 1-4 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 4 → 6 | 2 | 3 → 4 | -0.020 | 0.000 |
| Jogador 2 | 2-1 | 6 | 8.000 | -2.000 | 0 → 0 | 1 → 1 | 11% → 14% | 6 → 9 | 3 | 4 → 4 | -0.117 | 0.410 |
| Jogador 2 | 2-2 | 5 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 14% → 18% | 9 → 8 | 8 | 4 → 5 | 0.007 | 0.537 |
| Jogador 2 | 2-3 | 5 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 8 | 7 | 5 → 5 | 0.011 | 0.571 |
| Jogador 2 | 2-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 0 | 18% → 18% | 8 → 12 | 3 | 5 → 5 | 0.009 | 0.000 |
| Jogador 2 | 2-5 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 12 → 18 | 0 | 5 → 5 | 0.164 | -0.580 |
| Jogador 2 | 2-6 | 10 | 6.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 21% | 18 → 6 | 20 | 5 → 6 | -0.055 | -0.254 |
| Jogador 2 | 2-7 | 5 | 2.000 | 4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 9 | 4 | 6 → 6 | 0.119 | 0.000 |
| Jogador 2 | 3-1 | 7 | 0.000 | 0.000 | 0 → 0 | 0 → 1 | 21% → 21% | 9 → 7 | 11 | 6 → 6 | 0.015 | 0.414 |
| Jogador 2 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 10 | 4 | 6 → 6 | 0.000 | 0.967 |
| Jogador 2 | 3-3 | 7 | 8.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 25% | 10 → 8 | 12 | 6 → 7 | -0.005 | 0.437 |
| Jogador 2 | 3-4 | 8 | 4.000 | 2.000 | 0 → 0 | 1 → 2 | 25% → 25% | 8 → 7 | 10 | 7 → 7 | 0.003 | 0.000 |
| Jogador 2 | 3-5 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 10 | 4 | 7 → 7 | 0.000 | 0.978 |
| Jogador 2 | 3-6 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 10 → 11 | 10 | 7 → 7 | -0.009 | 0.423 |
| Jogador 2 | 3-7 | 6 | 2.000 | -2.000 | 0 → 0 | 2 → 3 | 25% → 25% | 11 → 19 | 4 | 7 → 7 | 0.010 | 0.000 |
| Jogador 2 | 4-1 | 10 | 0.000 | 2.000 | 0 → 0 | 3 → 2 | 25% → 25% | 19 → 11 | 23 | 7 → 7 | -0.006 | 0.294 |
| Jogador 2 | 4-2 | 7 | 0.000 | -6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 11 → 11 | 13 | 7 → 7 | 0.000 | 0.400 |
| Jogador 2 | 4-3 | 8 | 4.000 | -2.000 | 0 → 0 | 2 → 2 | 25% → 29% | 11 → 11 | 13 | 7 → 8 | -0.038 | 0.364 |
| Jogador 2 | 4-4 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 29% → 29% | 11 → 16 | 6 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 6 | 0.000 | 16.000 | 0 → 0 | 2 → 2 | 29% → 29% | 16 → 9 | 16 | 8 → 8 | 0.000 | 0.477 |
| Jogador 2 | 4-6 | 3 | 0.000 | 2.000 | 0 → 0 | 2 → 2 | 29% → 29% | 9 → 17 | 1 | 8 → 8 | 0.000 | 0.978 |
| Jogador 2 | 4-7 | 3 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 29% → 29% | 17 → 24 | 2 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 7 | 0.000 | 22.000 | 0 → 0 | 3 → 3 | 29% → 29% | 24 → 19 | 11 | 8 → 8 | 0.000 | -0.393 |
| Jogador 2 | 5-2 | 6 | 2.000 | 6.000 | 0 → 0 | 3 → 3 | 29% → 29% | 19 → 19 | 9 | 8 → 8 | -0.010 | 0.000 |
| Jogador 2 | 5-3 | 12 | 10.000 | 2.000 | 0 → 1 | 3 → 3 | 29% → 29% | 19 → 14 | 16 | 8 → 8 | -0.039 | -0.233 |
| Jogador 2 | 5-4 | 12 | 0.000 | 4.000 | 1 → 1 | 3 → 1 | 29% → 29% | 14 → 12 | 16 | 8 → 8 | -0.005 | 0.000 |
| Jogador 2 | 5-5 | 12 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 29% → 29% | 12 → 8 | 22 | 8 → 8 | 0.000 | -0.233 |
| Jogador 2 | 5-6 | 12 | 0.000 | -10.000 | 1 → 1 | 2 → 3 | 29% → 29% | 8 → 13 | 17 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-7 | 7 | 0.000 | 8.000 | 1 → 1 | 3 → 2 | 29% → 29% | 13 → 11 | 8 | 8 → 8 | 0.002 | 0.000 |
| Jogador 2 | 6-1 | 7 | -8.000 | 16.000 | 1 → 0 | 2 → 2 | 29% → 29% | 11 → 13 | 4 | 8 → 8 | -0.046 | -0.407 |
| Jogador 2 | 6-2 | 12 | 6.000 | 0.000 | 0 → 1 | 2 → 2 | 29% → 29% | 13 → 9 | 16 | 8 → 8 | 0.011 | 0.267 |
| Jogador 2 | 6-3 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 1 | 29% → 29% | 9 → 14 | 6 | 8 → 8 | 0.000 | 0.759 |
| Jogador 2 | 6-4 | 10 | 0.000 | -10.000 | 1 → 1 | 1 → 3 | 29% → 29% | 14 → 23 | 13 | 8 → 8 | 0.006 | 0.000 |
| Jogador 2 | 6-5 | 10 | 0.000 | -14.000 | 1 → 1 | 3 → 3 | 29% → 29% | 23 → 36 | 17 | 8 → 8 | -0.010 | -0.280 |
| Jogador 2 | 6-6 | 10 | -60.000 | -60.000 | 1 → 0 | 3 → 0 | 29% → 0% | 36 → 28 | 21 | 8 → 8 | 0.049 | -0.280 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 16, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 21; mudanças de composição: 1; posicionamento melhorou em 28 ações e piorou em 29.
- Jogador 2 — estado final: ouro 28, nível 8, vida 3.0, colocação 2.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 3 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.016 | 0.000 |
| Jogador 3 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 5 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 3 | 1-4 | 4 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 7 | 2 | 3 → 4 | 0.022 | 0.000 |
| Jogador 3 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 7 → 6 | 6 | 4 → 4 | 0.014 | -0.385 |
| Jogador 3 | 2-2 | 7 | 6.000 | -2.000 | 0 → 1 | 2 → 0 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | -0.009 | -0.332 |
| Jogador 3 | 2-3 | 7 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 8 → 7 | 7 | 4 → 5 | 0.006 | -0.347 |
| Jogador 3 | 2-4 | 5 | 4.000 | 2.000 | 1 → 1 | 0 → 0 | 18% → 18% | 7 → 10 | 3 | 5 → 5 | 0.011 | 0.000 |
| Jogador 3 | 2-5 | 8 | -4.000 | 6.000 | 1 → 0 | 0 → 0 | 18% → 18% | 10 → 16 | 2 | 5 → 5 | -0.008 | 0.330 |
| Jogador 3 | 2-6 | 9 | 4.000 | -8.000 | 0 → 0 | 0 → 1 | 18% → 21% | 16 → 10 | 18 | 5 → 6 | 0.012 | 0.300 |
| Jogador 3 | 2-7 | 6 | 0.000 | 0.000 | 0 → 1 | 1 → 0 | 21% → 18% | 10 → 14 | 5 | 6 → 6 | 0.005 | 0.000 |
| Jogador 3 | 3-1 | 4 | 4.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 21% | 14 → 20 | 2 | 6 → 6 | -0.020 | 0.721 |
| Jogador 3 | 3-2 | 7 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 20 → 8 | 19 | 6 → 6 | -0.009 | 0.407 |
| Jogador 3 | 3-3 | 7 | 0.000 | 2.000 | 1 → 1 | 0 → 0 | 21% → 21% | 8 → 8 | 10 | 6 → 6 | 0.000 | -0.375 |
| Jogador 3 | 3-4 | 9 | 6.000 | -4.000 | 1 → 1 | 0 → 0 | 21% → 25% | 8 → 8 | 9 | 6 → 7 | -0.005 | 0.000 |
| Jogador 3 | 3-5 | 9 | -4.000 | 4.000 | 1 → 0 | 0 → 1 | 25% → 25% | 8 → 7 | 14 | 7 → 7 | -0.007 | 0.315 |
| Jogador 3 | 3-6 | 7 | 6.000 | -8.000 | 0 → 1 | 1 → 0 | 25% → 25% | 7 → 9 | 9 | 7 → 7 | -0.027 | 0.419 |
| Jogador 3 | 3-7 | 5 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 25% → 25% | 9 → 12 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 8 | -2.000 | 2.000 | 1 → 0 | 0 → 0 | 25% → 25% | 12 → 6 | 16 | 7 → 7 | 0.000 | -0.348 |
| Jogador 3 | 4-2 | 8 | 0.000 | 0.000 | 0 → 0 | 0 → 1 | 25% → 25% | 6 → 8 | 11 | 7 → 7 | 0.000 | -0.337 |
| Jogador 3 | 4-3 | 7 | 8.000 | 0.000 | 0 → 1 | 1 → 0 | 25% → 25% | 8 → 7 | 7 | 7 → 7 | 0.000 | -0.386 |
| Jogador 3 | 4-4 | 3 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 4 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 25% → 25% | 9 → 8 | 7 | 7 → 8 | 0.000 | -0.675 |
| Jogador 3 | 4-6 | 5 | 8.000 | 8.000 | 1 → 1 | 1 → 2 | 25% → 29% | 8 → 7 | 8 | 8 → 8 | -0.027 | -0.556 |
| Jogador 3 | 4-7 | 4 | 0.000 | 14.000 | 1 → 1 | 2 → 3 | 29% → 29% | 7 → 7 | 7 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 5-1 | 7 | -54.000 | -36.000 | 1 → 0 | 3 → 0 | 29% → 0% | 7 → 0 | 7 | 8 → 8 | -0.016 | -0.407 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 10; mudanças de composição: 2; posicionamento melhorou em 21 ações e piorou em 22.
- Jogador 3 — estado final: ouro 0, nível 8, vida 7.0, colocação 6.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.018 | 0.000 |
| Jogador 4 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.020 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | -2.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 8 | 1 | 3 → 4 | 0.015 | 0.000 |
| Jogador 4 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 8 → 9 | 5 | 4 → 4 | -0.015 | 0.419 |
| Jogador 4 | 2-2 | 7 | 4.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 18% | 9 → 10 | 6 | 4 → 5 | -0.008 | 0.384 |
| Jogador 4 | 2-3 | 6 | 4.000 | 0.000 | 0 → 0 | 2 → 1 | 18% → 18% | 10 → 15 | 3 | 5 → 5 | -0.036 | 0.410 |
| Jogador 4 | 2-4 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 0 | 18% → 18% | 15 → 6 | 16 | 5 → 5 | -0.033 | 0.000 |
| Jogador 4 | 2-5 | 8 | 6.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 21% | 6 → 7 | 7 | 5 → 6 | -0.045 | 0.364 |
| Jogador 4 | 2-6 | 5 | 2.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 7 → 8 | 4 | 6 → 6 | 0.000 | -0.517 |
| Jogador 4 | 2-7 | 5 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 5 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 3-1 | 5 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 5 → 6 | 6 | 6 → 6 | 0.000 | -0.543 |
| Jogador 4 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.000 | -0.894 |
| Jogador 4 | 3-3 | 5 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 9 | 7 | 6 → 6 | 0.000 | -0.580 |
| Jogador 4 | 3-4 | 7 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 25% | 9 → 8 | 7 | 6 → 7 | 0.017 | 0.000 |
| Jogador 4 | 3-5 | 7 | 2.000 | -2.000 | 0 → 0 | 0 → 1 | 25% → 25% | 8 → 6 | 11 | 7 → 7 | 0.000 | 0.407 |
| Jogador 4 | 3-6 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 9 | 4 | 7 → 7 | 0.000 | 0.950 |
| Jogador 4 | 3-7 | 6 | 4.000 | -4.000 | 0 → 1 | 1 → 0 | 25% → 25% | 9 → 8 | 7 | 7 → 7 | -0.004 | 0.000 |
| Jogador 4 | 4-1 | 5 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 25% → 25% | 8 → 6 | 7 | 7 → 7 | 0.000 | -0.533 |
| Jogador 4 | 4-2 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | 0.954 |
| Jogador 4 | 4-3 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 7 | 8 | 7 → 7 | 0.000 | 0.728 |
| Jogador 4 | 4-4 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-5 | 5 | 6.000 | 2.000 | 1 → 1 | 1 → 1 | 25% → 29% | 9 → 8 | 8 | 7 → 8 | -0.005 | 0.572 |
| Jogador 4 | 4-6 | 4 | 0.000 | 16.000 | 1 → 1 | 1 → 1 | 29% → 29% | 8 → 7 | 8 | 8 → 8 | 0.000 | 0.708 |
| Jogador 4 | 4-7 | 7 | 4.000 | -4.000 | 1 → 1 | 1 → 0 | 29% → 29% | 7 → 6 | 7 | 8 → 8 | 0.010 | 0.000 |
| Jogador 4 | 5-1 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 29% → 29% | 6 → 8 | 3 | 8 → 8 | -0.016 | -0.467 |
| Jogador 4 | 5-2 | 6 | 2.000 | 6.000 | 1 → 1 | 0 → 1 | 29% → 29% | 8 → 10 | 4 | 8 → 8 | 0.087 | -0.467 |
| Jogador 4 | 5-3 | 5 | 0.000 | 16.000 | 1 → 1 | 1 → 1 | 29% → 29% | 10 → 6 | 10 | 8 → 8 | 0.000 | 0.597 |
| Jogador 4 | 5-4 | 4 | 0.000 | 12.000 | 1 → 1 | 1 → 2 | 29% → 29% | 6 → 5 | 6 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-5 | 6 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 29% → 29% | 5 → 8 | 6 | 8 → 8 | 0.000 | 0.498 |
| Jogador 4 | 5-6 | 7 | -58.000 | -64.000 | 1 → 0 | 2 → 0 | 29% → 0% | 8 → 0 | 9 | 8 → 8 | 0.006 | -0.393 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 15 ações e piorou em 19.
- Jogador 4 — estado final: ouro 0, nível 8, vida 14.0, colocação 3.
| Jogador 5 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 5 | 1-2 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.066 | 0.000 |
| Jogador 5 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.023 | 0.000 |
| Jogador 5 | 1-4 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.018 | 0.000 |
| Jogador 5 | 2-1 | 6 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 8 | 5 | 4 → 4 | 0.004 | -0.387 |
| Jogador 5 | 2-2 | 6 | 4.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 8 → 13 | 3 | 4 → 4 | 0.021 | -0.377 |
| Jogador 5 | 2-3 | 9 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 13 → 6 | 14 | 4 → 5 | -0.011 | 0.287 |
| Jogador 5 | 2-4 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 5 | 7 | 5 → 5 | 0.019 | 0.000 |
| Jogador 5 | 2-5 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 5 → 10 | 3 | 5 → 5 | 0.000 | 0.492 |
| Jogador 5 | 2-6 | 7 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 21% | 10 → 13 | 6 | 5 → 6 | -0.112 | 0.401 |
| Jogador 5 | 2-7 | 6 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 13 → 6 | 13 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-1 | 5 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 21% → 21% | 6 → 6 | 6 | 6 → 6 | 0.000 | -0.507 |
| Jogador 5 | 3-2 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 0 | 21% → 21% | 6 → 7 | 9 | 6 → 6 | 0.000 | 0.409 |
| Jogador 5 | 3-3 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 1 | 21% → 21% | 7 → 10 | 7 | 6 → 6 | 0.136 | 0.467 |
| Jogador 5 | 3-4 | 8 | 6.000 | -2.000 | 0 → 0 | 1 → 2 | 21% → 25% | 10 → 6 | 10 | 6 → 7 | -0.084 | 0.000 |
| Jogador 5 | 3-5 | 6 | 4.000 | 0.000 | 0 → 0 | 2 → 1 | 25% → 25% | 6 → 7 | 8 | 7 → 7 | 0.000 | 0.506 |
| Jogador 5 | 3-6 | 5 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 9 | 7 | 7 → 7 | 0.000 | 0.570 |
| Jogador 5 | 3-7 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 7 | 11 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 6 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 8 | 7 | 7 → 7 | -0.016 | -0.461 |
| Jogador 5 | 4-2 | 9 | 6.000 | -4.000 | 0 → 1 | 1 → 0 | 25% → 25% | 8 → 6 | 10 | 7 → 7 | 0.000 | -0.292 |
| Jogador 5 | 4-3 | 3 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 25% → 25% | 6 → 9 | 3 | 7 → 7 | 0.000 | 0.954 |
| Jogador 5 | 4-4 | 7 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 9 → 6 | 11 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 8 | 6.000 | -6.000 | 1 → 1 | 1 → 1 | 25% → 29% | 6 → 9 | 4 | 7 → 8 | 0.041 | 0.376 |
| Jogador 5 | 4-6 | 8 | 2.000 | 8.000 | 1 → 1 | 1 → 1 | 29% → 29% | 9 → 7 | 12 | 8 → 8 | 0.000 | 0.367 |
| Jogador 5 | 4-7 | 4 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 29% → 29% | 7 → 6 | 7 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 5 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 29% → 29% | 6 → 9 | 4 | 8 → 8 | 0.000 | 0.607 |
| Jogador 5 | 5-2 | 4 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 29% → 29% | 9 → 10 | 7 | 8 → 8 | 0.000 | 0.746 |
| Jogador 5 | 5-3 | 7 | 2.000 | 4.000 | 1 → 1 | 3 → 2 | 29% → 29% | 10 → 9 | 10 | 8 → 8 | 0.032 | 0.426 |
| Jogador 5 | 5-4 | 3 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 29% → 29% | 9 → 14 | 3 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 4 | 0.000 | 18.000 | 1 → 1 | 3 → 3 | 29% → 29% | 14 → 13 | 9 | 8 → 8 | -0.015 | 0.000 |
| Jogador 5 | 5-6 | 4 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 29% → 29% | 13 → 17 | 5 | 8 → 8 | -0.015 | 0.734 |
| Jogador 5 | 5-7 | 12 | 0.000 | 2.000 | 1 → 1 | 3 → 6 | 29% → 29% | 17 → 23 | 20 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 12 | 0.000 | 2.000 | 1 → 1 | 6 → 6 | 29% → 29% | 23 → 28 | 17 | 8 → 8 | 0.000 | 0.254 |
| Jogador 5 | 6-2 | 12 | -24.000 | 18.000 | 1 → 1 | 6 → 2 | 29% → 14% | 28 → 25 | 20 | 8 → 8 | -0.063 | -0.250 |
| Jogador 5 | 6-3 | 4 | 26.000 | -26.000 | 1 → 2 | 2 → 2 | 14% → 21% | 25 → 33 | 0 | 8 → 8 | 0.002 | -0.712 |
| Jogador 5 | 6-4 | 7 | 6.000 | 0.000 | 2 → 2 | 2 → 2 | 21% → 25% | 33 → 39 | 3 | 8 → 8 | 0.017 | 0.000 |
| Jogador 5 | 6-5 | 10 | 6.000 | 16.000 | 2 → 2 | 2 → 3 | 25% → 29% | 39 → 32 | 15 | 8 → 8 | 0.042 | 0.299 |
| Jogador 5 | 6-6 | 9 | -10.000 | -10.000 | 2 → 1 | 3 → 3 | 29% → 25% | 32 → 31 | 6 | 8 → 8 | -0.000 | 0.332 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 5, NO_IDENTIFIED_STRATEGIC_GAIN: 1, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 30 ações e piorou em 27.
- Jogador 5 — estado final: ouro 31, nível 8, vida 23.0, colocação 1.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 6 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.008 | 0.000 |
| Jogador 6 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.121 | 0.000 |
| Jogador 6 | 1-4 | 4 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 7 | 6.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 7 | 5 | 4 → 4 | 0.102 | 0.347 |
| Jogador 6 | 2-2 | 6 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 7 → 11 | 3 | 4 → 4 | -0.163 | -0.422 |
| Jogador 6 | 2-3 | 9 | 0.000 | -2.000 | 0 → 0 | 0 → 1 | 14% → 14% | 11 → 19 | 2 | 4 → 4 | 0.109 | 0.274 |
| Jogador 6 | 2-4 | 8 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 19 → 24 | 3 | 4 → 4 | -0.014 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | -4.000 | 0 → 0 | 1 → 0 | 14% → 18% | 24 → 30 | 7 | 4 → 5 | -0.004 | 0.264 |
| Jogador 6 | 2-6 | 5 | 4.000 | 2.000 | 0 → 0 | 0 → 1 | 18% → 18% | 30 → 36 | 3 | 5 → 5 | 0.011 | 0.492 |
| Jogador 6 | 2-7 | 5 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 36 → 46 | 3 | 5 → 5 | 0.000 | 0.000 |
| Jogador 6 | 3-1 | 7 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 46 → 52 | 3 | 5 → 5 | 0.000 | -0.389 |
| Jogador 6 | 3-2 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 52 → 63 | 0 | 5 → 5 | 0.000 | -0.517 |
| Jogador 6 | 3-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 63 → 74 | 0 | 5 → 5 | 0.000 | -0.658 |
| Jogador 6 | 3-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 74 → 85 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 6 | 3-5 | 12 | 2.000 | -2.000 | 0 → 0 | 1 → 2 | 18% → 18% | 85 → 68 | 30 | 5 → 6 | 0.000 | -0.239 |
| Jogador 6 | 3-6 | 10 | 4.000 | -4.000 | 0 → 1 | 2 → 1 | 18% → 18% | 68 → 66 | 16 | 6 → 7 | 0.005 | -0.276 |
| Jogador 6 | 3-7 | 6 | 10.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 21% | 66 → 73 | 5 | 7 → 7 | -0.100 | 0.000 |
| Jogador 6 | 4-1 | 9 | 6.000 | 0.000 | 1 → 2 | 1 → 1 | 21% → 21% | 73 → 80 | 6 | 7 → 7 | 0.000 | -0.302 |
| Jogador 6 | 4-2 | 12 | 8.000 | 4.000 | 2 → 2 | 1 → 1 | 21% → 25% | 80 → 56 | 34 | 7 → 7 | -0.019 | 0.236 |
| Jogador 6 | 4-3 | 12 | 0.000 | 8.000 | 2 → 2 | 1 → 1 | 25% → 25% | 56 → 22 | 40 | 7 → 8 | 0.000 | -0.229 |
| Jogador 6 | 4-4 | 9 | 4.000 | 14.000 | 2 → 2 | 1 → 1 | 25% → 29% | 22 → 8 | 19 | 8 → 8 | -0.001 | 0.000 |
| Jogador 6 | 4-5 | 6 | 0.000 | 8.000 | 2 → 1 | 1 → 1 | 29% → 29% | 8 → 6 | 8 | 8 → 8 | -0.010 | 0.518 |
| Jogador 6 | 4-6 | 4 | 0.000 | 12.000 | 1 → 1 | 1 → 2 | 29% → 29% | 6 → 5 | 6 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 4-7 | 3 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 29% → 29% | 5 → 6 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 8 | 0.000 | 8.000 | 1 → 1 | 2 → 1 | 29% → 29% | 6 → 7 | 8 | 8 → 8 | 0.000 | 0.369 |
| Jogador 6 | 5-2 | 5 | -60.000 | -62.000 | 1 → 0 | 1 → 0 | 29% → 0% | 7 → 1 | 6 | 8 → 8 | 0.118 | -0.550 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 6; mudanças de composição: 1; posicionamento melhorou em 10 ações e piorou em 20.
- Jogador 6 — estado final: ouro 1, nível 8, vida 14.0, colocação 5.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.005 | 0.000 |
| Jogador 7 | 1-3 | 4 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.012 | 0.000 |
| Jogador 7 | 1-4 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 6 | 2 | 3 → 4 | 0.011 | 0.000 |
| Jogador 7 | 2-1 | 8 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 14% | 6 → 8 | 4 | 4 → 4 | 0.013 | -0.296 |
| Jogador 7 | 2-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 8 → 14 | 0 | 4 → 4 | 0.000 | 0.616 |
| Jogador 7 | 2-3 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 14 → 20 | 2 | 4 → 4 | 0.000 | -0.387 |
| Jogador 7 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 20 → 27 | 0 | 4 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-5 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 27 → 35 | 2 | 4 → 5 | 0.000 | -0.391 |
| Jogador 7 | 2-6 | 12 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 14% → 18% | 35 → 21 | 21 | 5 → 6 | -0.009 | -0.220 |
| Jogador 7 | 2-7 | 7 | 8.000 | -2.000 | 0 → 0 | 2 → 2 | 18% → 21% | 21 → 25 | 3 | 6 → 6 | 0.023 | 0.000 |
| Jogador 7 | 3-1 | 11 | 2.000 | 2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 25 → 9 | 23 | 6 → 6 | -0.004 | -0.243 |
| Jogador 7 | 3-2 | 5 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 7 | 8 | 6 → 7 | 0.008 | 0.552 |
| Jogador 7 | 3-3 | 7 | 8.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 25% | 7 → 5 | 7 | 7 → 7 | 0.015 | -0.388 |
| Jogador 7 | 3-4 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 25% → 25% | 5 → 7 | 5 | 7 → 7 | -0.012 | 0.000 |
| Jogador 7 | 3-5 | 8 | 6.000 | -10.000 | 0 → 1 | 2 → 1 | 25% → 25% | 7 → 13 | 5 | 7 → 7 | -0.017 | -0.333 |
| Jogador 7 | 3-6 | 6 | 2.000 | 14.000 | 1 → 1 | 1 → 1 | 25% → 25% | 13 → 7 | 12 | 7 → 7 | 0.007 | -0.467 |
| Jogador 7 | 3-7 | 3 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 4 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 9 → 8 | 7 | 7 → 7 | 0.000 | 0.708 |
| Jogador 7 | 4-2 | 3 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 11 | 2 | 7 → 7 | 0.000 | -0.888 |
| Jogador 7 | 4-3 | 6 | 0.000 | 18.000 | 1 → 1 | 2 → 4 | 25% → 25% | 11 → 6 | 11 | 7 → 7 | -0.010 | 0.472 |
| Jogador 7 | 4-4 | 6 | 0.000 | 6.000 | 1 → 1 | 4 → 5 | 25% → 25% | 6 → 6 | 7 | 7 → 7 | -0.010 | 0.000 |
| Jogador 7 | 4-5 | 5 | -40.000 | -56.000 | 1 → 0 | 5 → 0 | 25% → 0% | 6 → 0 | 6 | 7 → 7 | -0.067 | -0.570 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 4, COMPOSITION_COMPATIBILITY: 12, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 13 ações e piorou em 13.
- Jogador 7 — estado final: ouro 0, nível 7, vida 15.0, colocação 8.
| Jogador 8 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 8 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.001 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 4 | 1 | 3 → 3 | -0.028 | 0.000 |
| Jogador 8 | 1-4 | 5 | 0.000 | -2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 4 → 8 | 1 | 3 → 4 | 0.037 | 0.000 |
| Jogador 8 | 2-1 | 7 | 4.000 | 0.000 | 1 → 1 | 0 → 1 | 7% → 14% | 8 → 12 | 2 | 4 → 4 | 0.011 | 0.359 |
| Jogador 8 | 2-2 | 6 | 2.000 | 0.000 | 1 → 1 | 1 → 2 | 14% → 18% | 12 → 10 | 9 | 4 → 5 | -0.009 | 0.397 |
| Jogador 8 | 2-3 | 5 | 4.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 10 → 8 | 7 | 5 → 5 | -0.044 | -0.464 |
| Jogador 8 | 2-4 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 8 → 5 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 8 | 2-5 | 5 | 4.000 | 0.000 | 1 → 1 | 2 → 1 | 18% → 18% | 5 → 9 | 3 | 5 → 6 | 0.011 | -0.496 |
| Jogador 8 | 2-6 | 6 | 2.000 | 6.000 | 1 → 1 | 1 → 1 | 18% → 21% | 9 → 7 | 8 | 6 → 6 | 0.048 | -0.387 |
| Jogador 8 | 2-7 | 7 | -2.000 | -2.000 | 1 → 1 | 1 → 1 | 21% → 21% | 7 → 7 | 10 | 6 → 6 | -0.042 | 0.000 |
| Jogador 8 | 3-1 | 6 | 4.000 | -2.000 | 1 → 1 | 1 → 1 | 21% → 21% | 7 → 8 | 8 | 6 → 6 | 0.010 | 0.453 |
| Jogador 8 | 3-2 | 6 | 2.000 | -2.000 | 1 → 1 | 1 → 1 | 21% → 21% | 8 → 13 | 2 | 6 → 6 | 0.000 | -0.454 |
| Jogador 8 | 3-3 | 6 | 2.000 | -2.000 | 1 → 1 | 1 → 1 | 21% → 25% | 13 → 7 | 12 | 6 → 7 | -0.011 | 0.481 |
| Jogador 8 | 3-4 | 4 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 5 | 7 | 7 → 7 | -0.015 | 0.000 |
| Jogador 8 | 3-5 | 6 | 0.000 | -2.000 | 1 → 1 | 1 → 2 | 25% → 25% | 5 → 7 | 6 | 7 → 7 | 0.010 | -0.461 |
| Jogador 8 | 3-6 | 6 | 2.000 | 0.000 | 1 → 1 | 2 → 1 | 25% → 25% | 7 → 8 | 7 | 7 → 7 | 0.000 | -0.446 |
| Jogador 8 | 3-7 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 4 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 9 | 3 | 7 → 7 | -0.015 | 0.733 |
| Jogador 8 | 4-2 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 9 → 17 | 0 | 7 → 7 | 0.000 | 1.417 |
| Jogador 8 | 4-3 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 17 → 23 | 0 | 7 → 7 | 0.000 | -1.332 |
| Jogador 8 | 4-4 | 3 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 25% → 25% | 23 → 27 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 12 | 2.000 | 4.000 | 1 → 1 | 2 → 2 | 25% → 21% | 27 → 9 | 24 | 7 → 8 | -0.038 | -0.246 |
| Jogador 8 | 4-6 | 11 | 2.000 | 8.000 | 1 → 1 | 2 → 3 | 21% → 25% | 9 → 6 | 9 | 8 → 8 | 0.043 | -0.242 |
| Jogador 8 | 4-7 | 4 | 6.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 29% | 6 → 6 | 6 | 8 → 8 | 0.067 | 0.000 |
| Jogador 8 | 5-1 | 5 | 0.000 | 12.000 | 1 → 1 | 3 → 4 | 29% → 29% | 6 → 6 | 6 | 8 → 8 | 0.000 | 0.584 |
| Jogador 8 | 5-2 | 5 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 29% → 29% | 6 → 7 | 6 | 8 → 8 | 0.000 | 0.584 |
| Jogador 8 | 5-3 | 9 | -40.000 | -46.000 | 1 → 0 | 4 → 0 | 29% → 0% | 7 → 0 | 10 | 8 → 8 | -0.049 | -0.311 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 8; mudanças de composição: 0; posicionamento melhorou em 16 ações e piorou em 19.
- Jogador 8 — estado final: ouro 0, nível 8, vida 11.0, colocação 4.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 35 | 12 | 1 | 1 | 4 | 0 | 4 | 2 | 4.1204 |
| Jogador 2 | 67 | 40 | 5 | 5 | 6 | 0 | 6 | 11 | 3.2563 |
| Jogador 3 | 36 | 14 | 2 | 2 | 4 | 0 | 4 | 5 | 4.2052 |
| Jogador 4 | 30 | 10 | 0 | 0 | 1 | 0 | 2 | 0 | 4.3585 |
| Jogador 5 | 56 | 29 | 2 | 2 | 9 | 0 | 5 | 8 | 3.9681 |
| Jogador 6 | 32 | 12 | 2 | 2 | 2 | 0 | 2 | 4 | 2.3726 |
| Jogador 7 | 27 | 10 | 0 | 0 | 1 | 0 | 1 | 0 | 4.3719 |
| Jogador 8 | 30 | 9 | 0 | 0 | 2 | 0 | 3 | 2 | 6.1124 |
- Jogador 1 — venda DA_KogMaw18_AD (2-5, step 203): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 1 — venda DA_KogMaw18_AD (2-6, step 229): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Akali_AD (3-1, step 266): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 1 — venda DA_18_Ezreal (3-3, step 306): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_KogMaw18_AD (3-1, step 266): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Fiddlesticks18 (3-4, step 329): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_Sejuani (3-6, step 367): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Fiddlesticks18 (4-1, step 402): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Ezreal (4-2, step 422): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Sejuani (5-3, step 556): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Soraka (5-4, step 572): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Sejuani (6-2, step 659): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Sett (6-3, step 668): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Cassiopeia (6-4, step 680): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Fiddlesticks18 (6-5, step 684): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Sett (6-5, step 690): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Lillia (6-6, step 693): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Gromp18_AP (6-6, step 697): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Diana (2-7, step 246): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Tristana (3-3, step 306): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Elise (3-3, step 308): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Sivir (3-4, step 328): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 3 — venda DA_Scuttlecrab18 (3-5, step 352): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Zyra (3-6, step 365): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Elise (4-1, step 403): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Soraka (4-2, step 422): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Gromp18_AP (3-2, step 287): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Gromp18_AP (3-2, step 289): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-3, step 306): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Gromp18_AP (3-5, step 349): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_CrimsonRaptor18 (3-7, step 382): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_KogMaw18_AD (4-4, step 452): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_KogMaw18_AD (5-7, step 628): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Diana (6-1, step 636): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Diana (6-2, step 651): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Scuttlecrab18 (2-5, step 205): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (2-7, step 247): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Caitlyn (3-6, step 365): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Teemo (5-1, step 526): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Shen (2-5, step 204): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 7 — venda DA_18_Rakan (3-1, step 266): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 7 — venda DA_18_Rakan (3-5, step 349): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 7 — venda DA_18_Aphelios (3-5, step 350): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_18_Akali_AD (2-5, step 203): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_18_Soraka (2-7, step 245): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Cassiopeia (3-1, step 266): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_CrimsonRaptor18 (3-5, step 349): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Shen (3-6, step 365): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.

Vendas de core/pares ignoradas antes da decisão da composição: **15**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente. Ganhos nas três ações seguintes do mesmo round podem compensar uma venda; falta de ganho imediato isoladamente não gera penalidade.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| MEDIUM | Jogador 1 | 1-4 | 81 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 2-6 | 229 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 2-6 | 229 | PURCHASE_REVERSED | Compra de DA_KogMaw18_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 3-3 | 306 | SOLD_CORE_UNIT | Venda de 'DA_18_Ezreal' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 3-3 | 306 | PURCHASE_REVERSED | Compra de DA_18_Ezreal desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 3-5 | 349 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| LOW | Jogador 1 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-2 | 175 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-3 | 222 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 4-6 | 2021 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 4-6 | 2022 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 2-3 | 680 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 2-3 | 691 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 2-3 | 702 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 2-4 | 808 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 2 | 3-1 | 266 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-4 | 329 | PURCHASE_REVERSED | Compra de DA_Fiddlesticks18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-6 | 367 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-6 | 367 | PURCHASE_REVERSED | Compra de DA_18_Sejuani desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-7 | 382 | PURCHASE_REVERSED | Compra de DA_18_Zyra desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-1 | 402 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Fiddlesticks18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-1 | 404 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 4-2 | 422 | SOLD_CORE_UNIT | Venda de 'DA_18_Ezreal' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-3 | 443 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-4 | 453 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 5-4 | 572 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Soraka' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-2 | 659 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-3 | 668 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sett' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-4 | 680 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 6-5 | 684 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-5 | 690 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sett' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 6-6 | 693 | SOLD_CORE_UNIT | Venda de 'DA_18_Lillia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 139 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-3 | 199 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-4 | 247 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-1 | 330 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-2 | 399 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-3 | 469 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-4 | 552 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-5 | 611 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-6 | 740 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-7 | 812 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 3-1 | 906 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 3-2 | 952 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 3-3 | 1047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 3-4 | 1156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 3-5 | 1202 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 3-6 | 1297 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 3-7 | 1380 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 4-1 | 1507 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 4-2 | 1600 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 6-6 | 3589 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 6-6 | 3590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-1 | 353 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-4 | 588 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 2189 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-3 | 2347 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-4 | 2504 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-4 | 2541 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-4 | 2553 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-7 | 246 | PURCHASE_REVERSED | Compra de DA_18_Diana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-3 | 306 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 3-3 | 308 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 3-3 | 308 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 3 | 3-4 | 328 | PURCHASE_REVERSED | Compra de DA_18_Sivir desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 3 | 3-5 | 349 | PURCHASE_REVERSED | Compra de DA_18_Alistar desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-5 | 352 | SOLD_CORE_UNIT | Venda de 'DA_Scuttlecrab18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 4-1 | 403 | SOLD_CORE_UNIT | Venda de 'DA_18_Elise' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 4-2 | 422 | SOLD_CORE_UNIT | Venda de 'DA_18_Soraka' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-2 | 175 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-3 | 210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-4 | 269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-1 | 352 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-2 | 448 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-3 | 542 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-4 | 613 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-5 | 721 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-6 | 836 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-7 | 921 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 5-1 | 2209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-1 | 2210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 2-2 | 496 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-5 | 757 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-5 | 768 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-5 | 779 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 1-4 | 81 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 1-3 | 210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 1-4 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 2-1 | 352 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 5-6 | 2330 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-6 | 2331 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-1 | 364 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-4 | 1635 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-6 | 1814 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-1 | 108 | PURCHASE_REVERSED | Compra de DA_18_Cassiopeia desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-2 | 132 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-4 | 182 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-2 | 287 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-2 | 287 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-2 | 289 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-2 | 289 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 3-3 | 306 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-3 | 306 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-5 | 349 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 3-7 | 382 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-7 | 382 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 4-4 | 452 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-4 | 452 | PURCHASE_REVERSED | Compra de DA_KogMaw18_AD desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 5-7 | 628 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-1 | 636 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-2 | 651 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 1-3 | 198 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 1-4 | 269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-1 | 352 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-2 | 435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 4-4 | 1846 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-5 | 2014 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 6-3 | 3119 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 6-5 | 3373 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-5 | 205 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 2-5 | 207 | PURCHASE_REVERSED | Compra de DA_18_Kayle desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 2-7 | 247 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 2-7 | 247 | PURCHASE_REVERSED | Compra de DA_KogMaw18_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 3-6 | 365 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 5-1 | 526 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 139 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-2 | 2501 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-2 | 2502 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 2-2 | 543 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-3 | 650 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 780 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-1 | 1837 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-2 | 1983 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-5 | 349 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| LOW | Jogador 7 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 4-5 | 1939 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-5 | 1940 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 2-2 | 557 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-3 | 616 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-4 | 711 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-5 | 784 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-5 | 795 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-5 | 806 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-5 | 817 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-5 | 828 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-1 | 1146 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-1 | 1157 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 7 | 1-1 | 128 | TEXT_MOVE_OSCILLATION | Possível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados. |
| MEDIUM | Jogador 8 | 1-4 | 81 | PURCHASE_REVERSED | Compra de DA_18_Varus desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 2-7 | 245 | SOLD_CORE_UNIT | Venda de 'DA_18_Soraka' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 3-5 | 349 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-5 | 349 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| LOW | Jogador 8 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-4 | 317 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 2-1 | 414 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 5-3 | 2202 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 5-3 | 2203 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 2-1 | 449 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-2 | 531 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-3 | 577 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-3 | 588 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-5 | 741 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-6 | 823 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-6 | 834 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-7 | 917 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-3 | 1551 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 8 | 1-1 | 128 | TEXT_MOVE_OSCILLATION | Possível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
\n\n---\n\n## Evidências resumidas dos achados\n\nO relatório apresenta métricas agregadas e a timeline em tabelas. Esta seção complementa apenas os achados com o contexto mínimo da decisão; snapshots, máscaras brutas e diagnósticos completos não são duplicados em Markdown.\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 1 · 1-4 · step 81\n\nCompra de DA_Gromp18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 3, força 6.0\n- Composição: — / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4018702208995819, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=54, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.393\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 2-6 · step 229\n\nVenda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 76.0, nível 6, ouro 5, força 26.0\n- Composição: Colosso / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.733522891998291, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 1 · 2-6 · step 229\n\nCompra de DA_KogMaw18_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 76.0, nível 6, ouro 5, força 26.0\n- Composição: Colosso / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.733522891998291, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=228, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 3-3 · step 306\n\nVenda de 'DA_18_Ezreal' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 65.0, nível 6, ouro 6, força 28.0\n- Composição: Colosso / DA_18_Ezreal\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2755437195301056, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ezreal, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 1 · 3-3 · step 306\n\nCompra de DA_18_Ezreal desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 65.0, nível 6, ouro 6, força 28.0\n- Composição: Colosso / DA_18_Ezreal\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2755437195301056, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=288, cost=4, sale_gold_delta=4, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 1 · 3-5 · step 349\n\nCompra de DA_18_Yunara desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 65.0, nível 7, ouro 8, força 34.0\n- Composição: Colosso / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação 0.09087692201137543, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=330, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 1-1 · step 80\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 1-2 · step 175\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 1-3 · step 222\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-6 · step 2021\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-6 · step 2022\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_1_log.tft\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 1 · 2-3 · step 680\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=8, comp_direction=—, comp_focus=DA_18_Diana, reward=-0.16, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 1 · 2-3 · step 691\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=4, comp_direction=—, comp_focus=DA_18_Diana, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 1 · 2-3 · step 702\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=0, comp_direction=—, comp_focus=DA_18_Diana, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 1 · 2-4 · step 808\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=2, comp_direction=Colosso, comp_focus=DA_18_Diana, reward=-0.08, raw_action=BUY XP\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 3-1 · step 266\n\nVenda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 88.0, nível 6, ouro 9, força 32.0\n- Composição: Florescer / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3380776047706604, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 3-4 · step 329\n\nCompra de DA_Fiddlesticks18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 88.0, nível 7, ouro 5, força 40.0\n- Composição: Florescer / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.1073476076126099, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=328, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=5.5005\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 3-6 · step 367\n\nVenda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 88.0, nível 7, ouro 9, força 44.0\n- Composição: Florescer / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.0102922916412354, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Sejuani, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 3-6 · step 367\n\nCompra de DA_18_Sejuani desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 88.0, nível 7, ouro 9, força 44.0\n- Composição: Florescer / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.0102922916412354, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=366, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 3-7 · step 382\n\nCompra de DA_18_Zyra desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 88.0, nível 7, ouro 11, força 44.0\n- Composição: Florescer / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.018353845924139023, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=368, cost=4, sale_gold_delta=4, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 4-1 · step 402\n\nVenda de 'DA_Fiddlesticks18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 88.0, nível 7, ouro 19, força 46.0\n- Composição: Florescer / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7521911859512329, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Fiddlesticks18, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 4-1 · step 404\n\nCompra de DA_18_Rammus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 88.0, nível 7, ouro 19, força 46.0\n- Composição: Florescer / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.23487743735313416, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=403, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=1.0209\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 4-2 · step 422\n\nVenda de 'DA_18_Ezreal' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 88.0, nível 7, ouro 11, força 46.0\n- Composição: Florescer / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3546615242958069, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ezreal, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 4-3 · step 443\n\nCompra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 88.0, nível 8, ouro 5, força 46.0\n- Composição: Florescer / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7041550278663635, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=442, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.8273\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 4-4 · step 453\n\nCompra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 88.0, nível 8, ouro 8, força 50.0\n- Composição: Adaptador / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.23407691717147827, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=452, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 5-4 · step 572\n\nVenda de 'DA_18_Soraka' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ECON · motivo ECON: acumular até o limite de juros de 50\n- Estado: HP 55.0, nível 8, ouro 12, força 62.0\n- Composição: Adaptador / DA_18_Alune\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3237203061580658, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Soraka, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 6-2 · step 659\n\nVenda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 20.0, nível 8, ouro 5, força 60.0\n- Composição: Adaptador / DA_18_Ahri\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.32331156730651855, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Sejuani, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 6-3 · step 668\n\nVenda de 'DA_18_Sett' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 20.0, nível 8, ouro 9, força 60.0\n- Composição: Adaptador / DA_18_Ahri\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2582080364227295, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Sett, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 6-4 · step 680\n\nVenda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 20.0, nível 8, ouro 13, força 60.0\n- Composição: Adaptador / DA_18_Ahri\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.33690696954727173, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Cassiopeia, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 6-5 · step 684\n\nVenda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 20.0, nível 8, ouro 17, força 60.0\n- Composição: Adaptador / DA_18_Ahri\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.38795071840286255, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Fiddlesticks18, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 6-5 · step 690\n\nVenda de 'DA_18_Sett' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 20.0, nível 8, ouro 25, força 60.0\n- Composição: Adaptador / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3362849950790405, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Sett, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 6-6 · step 693\n\nVenda de 'DA_18_Lillia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 3.0, nível 8, ouro 33, força 60.0\n- Composição: Adaptador / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3165999948978424, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Lillia, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-1 · step 80\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-2 · step 139\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-3 · step 199\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-4 · step 247\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-1 · step 330\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-2 · step 399\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-3 · step 469\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-4 · step 552\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-5 · step 611\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-6 · step 740\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-7 · step 812\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 3-1 · step 906\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 3-2 · step 952\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 3-3 · step 1047\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 3-4 · step 1156\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 3-5 · step 1202\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 3-6 · step 1297\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 3-7 · step 1380\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-1 · step 1507\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-2 · step 1600\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 6-6 · step 3589\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 6-6 · step 3590\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_2_log.tft\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-1 · step 353\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=1, comp_direction=—, comp_focus=DA_Vi18, reward=0.04, raw_action=BUY XP\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 2-4 · step 588\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=12, comp_direction=Florescer, comp_focus=DA_Fiddlesticks18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 2 · 5-2 · step 2189\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=14, comp_direction=Adaptador, comp_focus=DA_18_Lux_Sunbeam, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 2 · 5-3 · step 2347\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=10, comp_direction=Adaptador, comp_focus=DA_18_Alune, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 2 · 5-4 · step 2504\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=6, comp_direction=Adaptador, comp_focus=DA_18_Ahri, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 2 · 5-4 · step 2541\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=4, comp_direction=Adaptador, comp_focus=DA_18_Ahri, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 2 · 5-4 · step 2553\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=2, comp_direction=Adaptador, comp_focus=DA_18_Ahri, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 3 · 2-7 · step 246\n\nCompra de DA_18_Diana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 85.0, nível 6, ouro 7, força 28.0\n- Composição: Vanguarda / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.137676477432251, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=245, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=13.9558\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 3-3 · step 306\n\nVenda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 85.0, nível 6, ouro 8, força 32.0\n- Composição: Vanguarda / DA_Scuttlecrab18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3721819519996643, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Tristana, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 3 · 3-3 · step 308\n\nVenda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 85.0, nível 6, ouro 9, força 32.0\n- Composição: Vanguarda / DA_Scuttlecrab18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.077691674232483, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Elise, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 3 · 3-3 · step 308\n\nCompra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 85.0, nível 6, ouro 9, força 32.0\n- Composição: Vanguarda / DA_Scuttlecrab18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.077691674232483, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=307, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=9.849\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 3 · 3-4 · step 328\n\nCompra de DA_18_Sivir desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 74.0, nível 6, ouro 8, força 32.0\n- Composição: Vanguarda / DA_Scuttlecrab18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2874935269355774, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=309, cost=4, sale_gold_delta=4, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 3 · 3-5 · step 349\n\nCompra de DA_18_Alistar desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 74.0, nível 7, ouro 8, força 38.0\n- Composição: Vanguarda / DA_Scuttlecrab18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação 0.05760711058974266, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=334, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 3-5 · step 352\n\nVenda de 'DA_Scuttlecrab18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 74.0, nível 7, ouro 8, força 34.0\n- Composição: Vanguarda / DA_Scuttlecrab18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.38490769267082214, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Scuttlecrab18, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 4-1 · step 403\n\nVenda de 'DA_18_Elise' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 74.0, nível 7, ouro 12, força 38.0\n- Composição: Vanguarda / DA_18_Elise\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5298923254013062, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Elise, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 4-2 · step 422\n\nVenda de 'DA_18_Soraka' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 60.0, nível 7, ouro 6, força 38.0\n- Composição: Vanguarda / DA_18_Soraka\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3184618353843689, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Soraka, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-2 · step 175\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-3 · step 210\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-4 · step 269\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-1 · step 352\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-2 · step 448\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-3 · step 542\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-4 · step 613\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-5 · step 721\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-6 · step 836\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-7 · step 921\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-1 · step 2209\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-1 · step 2210\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_3_log.tft\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 2-2 · step 496\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=1, comp_direction=—, comp_focus=DA_Scuttlecrab18, reward=0.04, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 2-5 · step 757\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=15, comp_direction=Vanguarda, comp_focus=DA_18_Diana, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 2-5 · step 768\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=11, comp_direction=Vanguarda, comp_focus=DA_18_Diana, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 2-5 · step 779\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=7, comp_direction=Vanguarda, comp_focus=DA_18_Diana, reward=-0.09, raw_action=BUY XP\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 4 · 1-4 · step 81\n\nCompra de DA_Gromp18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 3, força 6.0\n- Composição: — / DA_Gromp18_AP\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4180184006690979, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=54, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=1.8911\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 1-2 · step 163\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 1-3 · step 210\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 1-4 · step 270\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 2-1 · step 352\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 5-6 · step 2330\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 5-6 · step 2331\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_4_log.tft\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 4 · 2-1 · step 364\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=5, comp_direction=—, comp_focus=DA_18_Akali_AD, reward=0.04, raw_action=BUY XP\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 4 · 4-4 · step 1635\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=5, comp_direction=Adaptador, comp_focus=DA_18_MasterYi_AD, reward=0.08, raw_action=BUY XP\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 4 · 4-6 · step 1814\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=0, comp_direction=Adaptador, comp_focus=DA_18_Diana, reward=-0.03, raw_action=BUY XP\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 2-1 · step 108\n\nCompra de DA_18_Cassiopeia desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 4, ouro 2, força 14.0\n- Composição: — / DA_18_Cassiopeia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7063031196594238, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=107, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.9874\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 2-2 · step 132\n\nCompra de DA_18_LeBlanc desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 95.0, nível 4, ouro 8, força 14.0\n- Composição: — / DA_18_Elise\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação 0.07832307368516922, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=109, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 2-4 · step 182\n\nCompra de DA_18_Camille desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 91.0, nível 5, ouro 6, força 20.0\n- Composição: — / DA_18_MasterYi_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.06082097068428993, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=164, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=4.7457\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 3-2 · step 287\n\nVenda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 6, ouro 6, força 30.0\n- Composição: Adaptador / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8762750029563904, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Gromp18_AP, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 3-2 · step 287\n\nCompra de DA_Gromp18_AP desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 6, ouro 6, força 30.0\n- Composição: Adaptador / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8762750029563904, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=267, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=9.7123\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 3-2 · step 289\n\nVenda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 6, ouro 6, força 30.0\n- Composição: Adaptador / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.1762479543685913, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Gromp18_AP, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 3-2 · step 289\n\nCompra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 6, ouro 6, força 30.0\n- Composição: Adaptador / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.1762479543685913, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=288, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=9.7401\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 3-3 · step 306\n\nVenda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 6, ouro 7, força 30.0\n- Composição: Adaptador / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.31431111693382263, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Tristana, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 3-3 · step 306\n\nCompra de DA_18_Tristana desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 6, ouro 7, força 30.0\n- Composição: Adaptador / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.31431111693382263, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=290, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 3-5 · step 349\n\nCompra de DA_Gromp18_AP desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 7, ouro 6, força 36.0\n- Composição: Adaptador / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8763331174850464, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=332, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=9.5014\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 3-7 · step 382\n\nVenda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 7, ouro 9, força 40.0\n- Composição: Adaptador / DA_18_Morgana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3320116698741913, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_CrimsonRaptor18, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 3-7 · step 382\n\nCompra de DA_CrimsonRaptor18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 82.0, nível 7, ouro 9, força 40.0\n- Composição: Adaptador / DA_18_Morgana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3320116698741913, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=366, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.0739\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 4-4 · step 452\n\nVenda de 'DA_KogMaw18_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 59.0, nível 7, ouro 9, força 48.0\n- Composição: Adaptador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8354595303535461, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 4-4 · step 452\n\nCompra de DA_KogMaw18_AD desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 59.0, nível 7, ouro 9, força 48.0\n- Composição: Adaptador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8354595303535461, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=440, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=13.6679\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 5-7 · step 628\n\nVenda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 10, força 58.0\n- Composição: Adaptador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.48899999260902405, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 6-1 · step 636\n\nVenda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 22, força 58.0\n- Composição: Adaptador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7636541128158569, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 6-2 · step 651\n\nVenda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 28, força 58.0\n- Composição: Adaptador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.6836540699005127, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-2 · step 127\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-3 · step 198\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-4 · step 269\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 2-1 · step 352\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 2-2 · step 435\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_5_log.tft\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 5 · 4-4 · step 1846\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=2, comp_direction=Adaptador, comp_focus=DA_18_Rammus, reward=0.08, raw_action=BUY XP\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 5 · 4-5 · step 2014\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=0, comp_direction=Adaptador, comp_focus=DA_18_Rammus, reward=-0.01, raw_action=BUY XP\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 6-3 · step 3119\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=30, comp_direction=Adaptador, comp_focus=DA_18_Rammus, reward=-0.24, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 6-5 · step 3373\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=30, comp_direction=Adaptador, comp_focus=DA_18_Rammus, reward=-0.24, raw_action=PASSOU TURNO\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 6 · 2-5 · step 205\n\nVenda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 94.0, nível 4, ouro 24, força 20.0\n- Composição: Colosso / DA_18_Hecarim\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8841728568077087, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Scuttlecrab18, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 6 · 2-5 · step 207\n\nCompra de DA_18_Kayle desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 94.0, nível 4, ouro 24, força 20.0\n- Composição: Colosso / DA_18_Hecarim\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.6970615386962891, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=206, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 6 · 2-7 · step 247\n\nVenda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia SLOWROLL · motivo SLOWROLL: composição tem alvo de 3 estrelas\n- Estado: HP 94.0, nível 5, ouro 34, força 26.0\n- Composição: Defendente / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.6983846426010132, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 6 · 2-7 · step 247\n\nCompra de DA_KogMaw18_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia SLOWROLL · motivo SLOWROLL: composição tem alvo de 3 estrelas\n- Estado: HP 94.0, nível 5, ouro 34, força 26.0\n- Composição: Defendente / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.6983846426010132, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=246, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 6 · 3-6 · step 365\n\nVenda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 51.0, nível 6, ouro 68, força 28.0\n- Composição: Defendente / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4010292887687683, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Caitlyn, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 6 · 5-1 · step 526\n\nVenda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 14.0, nível 8, ouro 1, força 60.0\n- Composição: Defendente / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3365240693092346, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Teemo, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 1-2 · step 139\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-2 · step 2501\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-2 · step 2502\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_6_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 2-2 · step 543\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=12, comp_direction=—, comp_focus=DA_18_Rammus, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 2-3 · step 650\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=18, comp_direction=—, comp_focus=DA_18_Hecarim, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 2-4 · step 780\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=21, comp_direction=Colosso, comp_focus=DA_18_Hecarim, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 4-1 · step 1837\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=46, comp_direction=Defendente, comp_focus=DA_18_GnarSmall, reward=-0.08, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 4-2 · step 1983\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=16, comp_direction=Defendente, comp_focus=DA_18_GnarSmall, reward=-0.09, raw_action=PASSOU TURNO\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 7 · 3-5 · step 349\n\nCompra de DA_18_Rakan desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 52.0, nível 7, ouro 7, força 32.0\n- Composição: Vanguarda / DA_18_Aphelios\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.9063845872879028, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=330, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=9.0075\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-5 · step 1939\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-5 · step 1940\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_7_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 2-2 · step 557\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=14, comp_direction=—, comp_focus=DA_18_Alistar, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 2-3 · step 616\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=20, comp_direction=—, comp_focus=DA_18_Alistar, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 2-4 · step 711\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=27, comp_direction=Vanguarda, comp_focus=DA_18_Alistar, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 2-5 · step 784\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=30, comp_direction=Vanguarda, comp_focus=DA_18_Alistar, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 2-5 · step 795\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=26, comp_direction=Vanguarda, comp_focus=DA_18_Alistar, reward=-0.16, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 2-5 · step 806\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=22, comp_direction=Vanguarda, comp_focus=DA_18_Alistar, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 2-5 · step 817\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=18, comp_direction=Vanguarda, comp_focus=DA_18_Alistar, reward=-0.16, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 2-5 · step 828\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=14, comp_direction=Vanguarda, comp_focus=DA_18_Alistar, reward=0.03, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 3-1 · step 1146\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=5, comp_direction=Vanguarda, comp_focus=DA_18_Diana, reward=-0.05, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 3-1 · step 1157\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=1, comp_direction=Vanguarda, comp_focus=DA_18_Diana, reward=-0.05, raw_action=BUY XP\n\n### HIGH · TEXT_MOVE_OSCILLATION · Jogador 7 · 1-1 · step 128\n\nPossível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados.\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 8 · 1-4 · step 81\n\nCompra de DA_18_Varus desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 4, força 6.0\n- Composição: — / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4289169907569885, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=55, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=1.9622\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 2-7 · step 245\n\nVenda de 'DA_18_Soraka' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia SLOWROLL · motivo SLOWROLL: composição tem alvo de 3 estrelas\n- Estado: HP 84.0, nível 6, ouro 7, força 22.0\n- Composição: Defendente / DA_18_Leona\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.32095953822135925, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Soraka, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 3-5 · step 349\n\nVenda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 73.0, nível 7, ouro 5, força 28.0\n- Composição: Defendente / DA_18_Leona\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3704862594604492, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_CrimsonRaptor18, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 8 · 3-5 · step 349\n\nCompra de DA_CrimsonRaptor18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 73.0, nível 7, ouro 5, força 28.0\n- Composição: Defendente / DA_18_Leona\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3704862594604492, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=328, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-4 · step 317\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 2-1 · step 414\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-3 · step 2202\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-3 · step 2203\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-193845-64b82cbe\player_8_log.tft\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 8 · 2-1 · step 449\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=3, comp_direction=—, comp_focus=DA_18_Leona, reward=0.04, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 8 · 2-2 · step 531\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=3, comp_direction=—, comp_focus=DA_18_Leona, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 8 · 2-3 · step 577\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=4, comp_direction=—, comp_focus=DA_18_Leona, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 8 · 2-3 · step 588\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=0, comp_direction=—, comp_focus=DA_18_Leona, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 8 · 2-5 · step 741\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=1, comp_direction=Defendente, comp_focus=DA_18_Leona, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 8 · 2-6 · step 823\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=5, comp_direction=Defendente, comp_focus=DA_18_Leona, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 8 · 2-6 · step 834\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=1, comp_direction=Defendente, comp_focus=DA_18_Leona, reward=-0.08, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 8 · 2-7 · step 917\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=2, comp_direction=Defendente, comp_focus=DA_18_Leona, reward=-0.05, raw_action=BUY XP\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 4-3 · step 1551\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=20, comp_direction=Defendente, comp_focus=DA_18_Leona, reward=-0.11, raw_action=PASSOU TURNO\n\n### HIGH · TEXT_MOVE_OSCILLATION · Jogador 8 · 1-1 · step 128\n\nPossível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados.\n\n## Arquivos e rastreabilidade\n\n- Jogadores analisados: 8\n- Entradas analisadas: 4315\n- Decisões únicas estruturadas: 1230\n- Reconstruções textuais corroborativas (não somadas): 1230\n- Achados: 174\n- Os arquivos estruturados de origem permanecem separados deste relatório.\n- Campos ausentes são exibidos como “—”; não são inferidos como zero.\n