# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5358**
- Achados: **385**
- CRITICAL: 0 | HIGH: 19 | MEDIUM: 108 | LOW: 258

## Metadados da sessão

- Match ID: ba52899d-65de-4df4-aded-d31d8a889f22
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 8e9656efb50839ed3dc79f7bcdcb719652ae14887d92a4b0e27d94844c4be999
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4448**
- Entradas posteriores à eliminação ignoradas: **910**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 21 | 7 | 11 | 25 | 70 | 4 | 1 | não/inconclusivo | 0 |
| Jogador 6 | 3 | 7 | 14 | 10 | 58 | 4 | 3 | não/inconclusivo | 0 |
| Jogador 7 | 83 | 8 | 23 | 8 | 98 | 7 | 3 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 170 | 46 | 25 | 13 | 3 | 21 | 57 | 0.0968 | 12 | 21 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 3, FAST8::BUY: 11, FAST8::BUY_XP: 8, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 9, FAST8::MOVE_BOARD: 18, FAST8::PASS: 8, FAST8::SELL: 5, LOSS_STREAK::BUY: 4, LOSS_STREAK::BUY_XP: 2, LOSS_STREAK::MOVE_BOARD: 1, LOSS_STREAK::PASS: 1, LOSS_STREAK::SELL: 4, SLOWROLL::BUY: 1, SLOWROLL::BUY_XP: 1, SLOWROLL::MOVE_BOARD: 2, SLOWROLL::PASS: 1, STABILIZE::BUY: 27, STABILIZE::BUY_XP: 2, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 11, STABILIZE::PASS: 10, STABILIZE::REROLL: 2, STABILIZE::SELL: 13
- Jogador 1 — recompensas por ação: BUY: média 0.3648 (n=46), BUY_XP: média -0.0154 (n=13), ITEM: média 0.1440 (n=5), MOVE_BENCH: média 0.1317 (n=23), MOVE_BOARD: média -0.0073 (n=34), PASS: média -0.0024 (n=21), REROLL: média -0.0900 (n=3), SELL: média -0.1324 (n=25)
| Jogador 2 | 301 | 75 | 50 | 13 | 10 | 36 | 99 | 0.0266 | 10 | 32 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 21, ALL_IN::PASS: 3, ALL_IN::REROLL: 1, ALL_IN::SELL: 5, FAST8::BUY: 41, FAST8::BUY_XP: 10, FAST8::ITEM: 11, FAST8::MOVE_BENCH: 29, FAST8::MOVE_BOARD: 9, FAST8::PASS: 17, FAST8::REROLL: 8, FAST8::SELL: 23, SLOWROLL::BUY: 6, SLOWROLL::BUY_XP: 1, SLOWROLL::ITEM: 1, SLOWROLL::MOVE_BENCH: 7, SLOWROLL::PASS: 3, SLOWROLL::SELL: 4, STABILIZE::BUY: 23, STABILIZE::BUY_XP: 2, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 24, STABILIZE::MOVE_BOARD: 9, STABILIZE::PASS: 13, STABILIZE::REROLL: 1, STABILIZE::SELL: 18
- Jogador 2 — recompensas por ação: BUY: média 0.3303 (n=75), BUY_XP: média -0.0131 (n=13), ITEM: média 0.1050 (n=18), MOVE_BENCH: média -0.1383 (n=81), MOVE_BOARD: média -0.0050 (n=18), PASS: média -0.0725 (n=36), REROLL: média -0.1340 (n=10), SELL: média -0.0648 (n=50)
| Jogador 3 | 166 | 41 | 19 | 3 | 9 | 21 | 66 | 0.0711 | 10 | 18 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::MOVE_BENCH: 1, ALL_IN::PASS: 1, ALL_IN::REROLL: 3, ALL_IN::SELL: 2, FAST8::BUY: 11, FAST8::BUY_XP: 1, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 6, FAST8::PASS: 3, FAST8::REROLL: 2, FAST8::SELL: 3, SLOWROLL::BUY: 10, SLOWROLL::BUY_XP: 1, SLOWROLL::ITEM: 3, SLOWROLL::MOVE_BENCH: 26, SLOWROLL::MOVE_BOARD: 8, SLOWROLL::PASS: 7, SLOWROLL::SELL: 4, STABILIZE::BUY: 16, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 10, STABILIZE::PASS: 10, STABILIZE::REROLL: 4, STABILIZE::SELL: 10
- Jogador 3 — recompensas por ação: BUY: média 0.3851 (n=41), BUY_XP: média 0.0267 (n=3), ITEM: média 0.1729 (n=7), MOVE_BENCH: média -0.0262 (n=42), MOVE_BOARD: média -0.0067 (n=24), PASS: média -0.0486 (n=21), REROLL: média -0.1144 (n=9), SELL: média -0.1037 (n=19)
| Jogador 4 | 240 | 70 | 40 | 11 | 16 | 30 | 63 | 0.0845 | 16 | 37 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::ITEM: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 2, FAST8::BUY: 24, FAST8::BUY_XP: 7, FAST8::ITEM: 5, FAST8::MOVE_BENCH: 24, FAST8::MOVE_BOARD: 11, FAST8::PASS: 17, FAST8::REROLL: 2, FAST8::SELL: 10, SLOWROLL::BUY: 4, SLOWROLL::ITEM: 2, SLOWROLL::MOVE_BENCH: 2, SLOWROLL::MOVE_BOARD: 2, SLOWROLL::PASS: 1, SLOWROLL::SELL: 2, STABILIZE::BUY: 37, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 11, STABILIZE::PASS: 12, STABILIZE::REROLL: 12, STABILIZE::SELL: 26
- Jogador 4 — recompensas por ação: BUY: média 0.4196 (n=70), BUY_XP: média -0.0082 (n=11), ITEM: média 0.1470 (n=10), MOVE_BENCH: média -0.0200 (n=39), MOVE_BOARD: média -0.0050 (n=24), PASS: média -0.0193 (n=30), REROLL: média -0.1087 (n=16), SELL: média -0.1812 (n=40)
| Jogador 5 | 289 | 80 | 48 | 21 | 14 | 34 | 80 | 0.0886 | 19 | 35 |
- Jogador 5 — ações por estratégia: ECON::BUY: 16, ECON::BUY_XP: 1, ECON::ITEM: 2, ECON::MOVE_BENCH: 5, ECON::MOVE_BOARD: 7, ECON::PASS: 7, ECON::REROLL: 3, ECON::SELL: 6, FAST8::BUY: 13, FAST8::BUY_XP: 16, FAST8::ITEM: 3, FAST8::MOVE_BENCH: 14, FAST8::MOVE_BOARD: 16, FAST8::PASS: 14, FAST8::SELL: 5, SLOWROLL::BUY: 1, SLOWROLL::MOVE_BENCH: 7, SLOWROLL::PASS: 1, STABILIZE::BUY: 50, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 16, STABILIZE::OTHER: 1, STABILIZE::PASS: 12, STABILIZE::REROLL: 11, STABILIZE::SELL: 37
- Jogador 5 — recompensas por ação: BUY: média 0.3486 (n=80), BUY_XP: média -0.0319 (n=21), ITEM: média 0.1291 (n=11), MOVE_BENCH: média 0.0732 (n=41), MOVE_BOARD: média -0.0049 (n=39), OTHER: média -0.0300 (n=1), PASS: média -0.0150 (n=34), REROLL: média -0.1107 (n=14), SELL: média -0.0781 (n=48)
| Jogador 6 | 221 | 58 | 33 | 14 | 12 | 27 | 68 | 0.0534 | 22 | 34 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 5, ALL_IN::PASS: 3, ALL_IN::REROLL: 7, ALL_IN::SELL: 4, FAST8::BUY: 17, FAST8::BUY_XP: 9, FAST8::ITEM: 3, FAST8::MOVE_BENCH: 23, FAST8::MOVE_BOARD: 12, FAST8::PASS: 12, FAST8::SELL: 7, SLOWROLL::BUY: 6, SLOWROLL::BUY_XP: 3, SLOWROLL::MOVE_BENCH: 6, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::PASS: 3, SLOWROLL::SELL: 4, STABILIZE::BUY: 28, STABILIZE::BUY_XP: 2, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 9, STABILIZE::PASS: 9, STABILIZE::REROLL: 5, STABILIZE::SELL: 18
- Jogador 6 — recompensas por ação: BUY: média 0.3176 (n=58), BUY_XP: média -0.0321 (n=14), ITEM: média 0.1189 (n=9), MOVE_BENCH: média -0.0502 (n=41), MOVE_BOARD: média -0.0048 (n=27), PASS: média -0.0100 (n=27), REROLL: média -0.0900 (n=12), SELL: média -0.1118 (n=33)
| Jogador 7 | 333 | 98 | 63 | 23 | 27 | 34 | 72 | 0.0767 | 14 | 46 |
- Jogador 7 — ações por estratégia: ECON::BUY: 18, ECON::BUY_XP: 1, ECON::ITEM: 1, ECON::MOVE_BENCH: 2, ECON::MOVE_BOARD: 2, ECON::PASS: 3, ECON::REROLL: 13, ECON::SELL: 14, FAST8::BUY: 12, FAST8::BUY_XP: 17, FAST8::ITEM: 5, FAST8::MOVE_BENCH: 27, FAST8::MOVE_BOARD: 6, FAST8::PASS: 11, FAST8::SELL: 6, SLOWROLL::BUY: 5, SLOWROLL::BUY_XP: 1, SLOWROLL::MOVE_BENCH: 3, SLOWROLL::MOVE_BOARD: 2, SLOWROLL::PASS: 1, SLOWROLL::SELL: 3, STABILIZE::BUY: 16, STABILIZE::BUY_XP: 3, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 7, STABILIZE::PASS: 7, STABILIZE::SELL: 13, WINSTREAK::BUY: 47, WINSTREAK::BUY_XP: 1, WINSTREAK::ITEM: 8, WINSTREAK::MOVE_BENCH: 10, WINSTREAK::MOVE_BOARD: 2, WINSTREAK::PASS: 12, WINSTREAK::REROLL: 14, WINSTREAK::SELL: 27
- Jogador 7 — recompensas por ação: BUY: média 0.3211 (n=98), BUY_XP: média -0.0265 (n=23), ITEM: média 0.1125 (n=16), MOVE_BENCH: média -0.0002 (n=53), MOVE_BOARD: média -0.0010 (n=19), PASS: média -0.0329 (n=34), REROLL: média -0.1411 (n=27), SELL: média -0.0343 (n=63)
| Jogador 8 | 170 | 52 | 33 | 12 | 8 | 21 | 37 | 0.0732 | 27 | 17 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 2, ALL_IN::REROLL: 6, ALL_IN::SELL: 6, FAST8::BUY: 7, FAST8::BUY_XP: 5, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 2, FAST8::PASS: 5, FAST8::SELL: 3, LOSS_STREAK::BUY: 1, LOSS_STREAK::BUY_XP: 1, LOSS_STREAK::MOVE_BENCH: 3, LOSS_STREAK::MOVE_BOARD: 4, LOSS_STREAK::PASS: 1, SLOWROLL::BUY: 6, SLOWROLL::MOVE_BENCH: 1, SLOWROLL::PASS: 2, SLOWROLL::SELL: 1, STABILIZE::BUY: 32, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 12, STABILIZE::PASS: 11, STABILIZE::REROLL: 2, STABILIZE::SELL: 23
- Jogador 8 — recompensas por ação: BUY: média 0.3346 (n=52), BUY_XP: média -0.0333 (n=12), ITEM: média 0.1157 (n=7), MOVE_BENCH: média 0.0574 (n=19), MOVE_BOARD: média 0.0083 (n=18), PASS: média -0.0048 (n=21), REROLL: média -0.0900 (n=8), SELL: média -0.1752 (n=33)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 22:48:49 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | 0.0000 |  |
| Jogador 1 | ? | 22:48:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 1 | ? | 22:48:50 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 1 | ? | 22:48:50 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 1 | ? | 22:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-1 | 22:48:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 1 | 1-1 | 22:48:56 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.4400 |  |
| Jogador 1 | 1-1 | 22:48:56 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 1 | 1-1 | 22:48:57 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 1 | 1-1 | 22:48:57 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-1 | 22:48:58 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-1 | 22:48:58 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5100 |  |
| Jogador 1 | 1-1 | 22:48:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-2 | 22:49:02 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 1 | 1-2 | 22:49:02 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 1 | 1-2 | 22:49:03 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 1 | 1-2 | 22:49:03 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 1 | 1-2 | 22:49:03 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 1 | 1-2 | 22:49:04 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-2 | 22:49:04 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.7600 |  |
| Jogador 1 | 1-2 | 22:49:04 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 1 | 1-2 | 22:49:04 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0000 |  |
| Jogador 1 | 1-2 | 22:49:04 | MOVE Bench -> Board: Leona (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.4000 |  |
| Jogador 1 | 1-2 | 22:49:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-3 | 22:49:09 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.3000 |  |
| Jogador 1 | 1-3 | 22:49:09 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 1 | 1-3 | 22:49:09 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | -0.3900 |  |
| Jogador 1 | 1-3 | 22:49:10 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Leona | 0.2500 |  |
| Jogador 1 | 1-3 | 22:49:10 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Leona | 0.2500 |  |
| Jogador 1 | 1-3 | 22:49:10 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Leona | 0.1300 |  |
| Jogador 1 | 1-3 | 22:49:11 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 22:49:11 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 0.4400 |  |
| Jogador 1 | 1-3 | 22:49:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0400 |  |
| Jogador 1 | 1-3 | 22:49:12 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2800 |  |
| Jogador 1 | 1-3 | 22:49:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 1 | 1-4 | 22:49:15 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | -0.2500 |  |
| Jogador 1 | 1-4 | 22:49:16 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Kobuko | 1.0200 |  |
| Jogador 1 | 1-4 | 22:49:16 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Kobuko | -0.4000 |  |
| Jogador 1 | 1-4 | 22:49:17 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Kobuko | -0.0100 |  |
| Jogador 1 | 1-4 | 22:49:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Kobuko | 0.0000 |  |
| Jogador 1 | 1-4 | 22:49:20 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Kobuko | 0.5700 |  |
| Jogador 1 | 2-1 | 22:49:22 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Alistar | 0.2600 |  |
| Jogador 1 | 2-1 | 22:49:22 | MOVE Bench -> Board: Alistar (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Alistar | -0.2900 |  |
| Jogador 1 | 2-1 | 22:49:23 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Alistar | -0.0600 |  |
| Jogador 1 | 2-1 | 22:49:23 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.3200 |  |
| Jogador 1 | 2-1 | 22:49:24 | MOVE Bench -> Board: Diana (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.1000 |  |
| Jogador 1 | 2-1 | 22:49:24 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.1400 |  |
| Jogador 1 | 2-1 | 22:49:24 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NeedlesslyLargeRod -> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.0700 |  |
| Jogador 1 | 2-1 | 22:49:25 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-1 | 22:49:25 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | 0.2000 |  |
| Jogador 1 | 2-1 | 22:49:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0300 |  |
| Jogador 1 | 2-1 | 22:49:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-2 | 22:49:29 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Diana | 0.4400 |  |
| Jogador 1 | 2-2 | 22:49:30 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.1900 |  |
| Jogador 1 | 2-2 | 22:49:30 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.0400 |  |
| Jogador 1 | 2-2 | 22:49:30 | MOVE Board -> Board: Master Yi (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-2 | 22:49:30 | MOVE Bench -> Board: Elise (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | -0.1000 |  |
| Jogador 1 | 2-2 | 22:49:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 22:49:36 | VENDEU: Kobuko (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Diana | -0.3400 |  |
| Jogador 1 | 2-3 | 22:49:37 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 7 | 0 | — | DA_18_Diana | 0.2200 |  |
| Jogador 1 | 2-3 | 22:49:37 | VENDEU: Kog'Maw (i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Diana | -0.2600 |  |
| Jogador 1 | 2-3 | 22:49:38 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 8 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-3 | 22:49:38 | VENDEU: Caitlyn (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Diana | -0.2500 |  |
| Jogador 1 | 2-3 | 22:49:39 | COMPROU: Teemo (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 8 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-3 | 22:49:39 | BUY XP | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-3 | 22:49:39 | BUY XP | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-3 | 22:49:39 | MOVE Board -> Board: Elise (i:4.0) <-> Alistar (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 22:49:40 | VENDEU: Teemo (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 2 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 22:49:40 | PASSOU TURNO | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 2 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 22:49:43 | COMPROU: Alistar (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 6 | 0 | Lutador | DA_18_Diana | 0.9000 |  |
| Jogador 1 | 2-4 | 22:49:44 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Lutador | DA_18_Diana | -0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-4 | 22:49:44 | MOVE Board -> Board: Alistar (i:4.0) <-> Diana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Lutador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 22:49:44 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Lutador | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-4 | 22:49:45 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Lutador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-5 | 22:49:50 | MOVE Bench -> Board: Alistar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Diana | 0.5900 |  |
| Jogador 1 | 2-5 | 22:49:51 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Diana | 0.3200 |  |
| Jogador 1 | 2-5 | 22:49:51 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Diana | -0.1900 |  |
| Jogador 1 | 2-5 | 22:49:51 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Lutador | DA_18_Diana | 0.9200 |  |
| Jogador 1 | 2-5 | 22:49:52 | MOVE Board -> Board: Alistar (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Lutador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-5 | 22:49:53 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Diana | -0.3500 |  |
| Jogador 1 | 2-5 | 22:49:53 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Lutador | DA_18_Diana | 0.3200 |  |
| Jogador 1 | 2-5 | 22:49:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-5 | 22:49:54 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Lutador | DA_18_Diana | -0.1500 |  |
| Jogador 1 | 2-5 | 22:49:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-5 | 22:49:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-6 | 22:49:58 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Diana | -0.0200 |  |
| Jogador 1 | 2-6 | 22:49:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-6 | 22:49:58 | VENDEU: Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-6 | 22:49:58 | MOVE Board -> Board: Diana (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-6 | 22:49:59 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-6 | 22:49:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-7 | 22:50:05 | COMPROU: Alistar (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Lutador | DA_18_Alistar | 0.6900 |  |
| Jogador 1 | 2-7 | 22:50:05 | MOVE Bench -> Board: Alistar (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Alistar | 0.3500 |  |
| Jogador 1 | 2-7 | 22:50:06 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Alistar | 0.7300 |  |
| Jogador 1 | 2-7 | 22:50:06 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Alistar | 0.5300 |  |
| Jogador 1 | 2-7 | 22:50:06 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Alistar | 0.1600 |  |
| Jogador 1 | 2-7 | 22:50:06 | MOVE Board -> Board: Alistar (i:8.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 2-7 | 22:50:07 | MOVE Board -> Board: Diana (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 1 | 2-7 | 22:50:08 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-1 | 22:50:13 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lutador | DA_18_Alistar | 0.6900 |  |
| Jogador 1 | 3-1 | 22:50:13 | MOVE Board -> Board: Elise (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-1 | 22:50:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Lutador | DA_18_Alistar | -0.0900 |  |
| Jogador 1 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 1 | 3-1 | 22:50:14 | MOVE Bench -> Board: Elise (i:4.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Alistar | -0.4000 |  |
| Jogador 1 | 3-1 | 22:50:14 | MOVE Board -> Board: Master Yi (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 1 | 3-1 | 22:50:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-2 | 22:50:21 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lutador | DA_18_Alistar | -0.2200 |  |
| Jogador 1 | 3-2 | 22:50:21 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Lutador | DA_18_Alistar | 0.1400 |  |
| Jogador 1 | 3-2 | 22:50:21 | MOVE Bench -> Board: Alistar (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Lutador | DA_18_Alistar | 0.0600 |  |
| Jogador 1 | 3-2 | 22:50:22 | MOVE Bench -> Board: Diana (i:6.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 1 | 3-2 | 22:50:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 1 | 3-2 | 22:50:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Alistar | 0.0900 |  |
| Jogador 1 | 3-2 | 22:50:23 | MOVE Bench -> Board: Alistar (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Alistar | 0.5900 |  |
| Jogador 1 | 3-2 | 22:50:23 | MOVE Board -> Board: Alistar (i:8.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 1 | 3-2 | 22:50:23 | MOVE Board -> Board: Diana (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 1 | 3-2 | 22:50:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-3 | 22:50:30 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Lutador | DA_18_Alistar | 0.1900 |  |
| Jogador 1 | 3-3 | 22:50:30 | MOVE Board -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-3 | 22:50:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 1 | 3-3 | 22:50:30 | MOVE Board -> Board: Elise (i:4.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-3 | 22:50:31 | MOVE Board -> Board: Alistar (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Alistar | -0.0200 |  |
| Jogador 1 | 3-3 | 22:50:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-4 | 22:50:39 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Alistar | 0.7100 |  |
| Jogador 1 | 3-4 | 22:50:39 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-4 | 22:50:39 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Alistar | -0.2700 |  |
| Jogador 1 | 3-4 | 22:50:39 | MOVE Board -> Board: Master Yi (i:6.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-4 | 22:50:40 | MOVE Board -> Board: Alistar (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 1 | 3-4 | 22:50:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 1 | 3-5 | 22:50:48 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Lutador | DA_18_MasterYi_AD | 0.7600 |  |
| Jogador 1 | 3-5 | 22:50:49 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 1 | 3-5 | 22:50:49 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 1 | 3-5 | 22:50:49 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_MasterYi_AD | 0.4000 |  |
| Jogador 1 | 3-5 | 22:50:50 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.2900 |  |
| Jogador 1 | 3-5 | 22:50:50 | MOVE Board -> Board: Yunara (i:4.0) <-> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 3-5 | 22:50:50 | MOVE Board -> Board: Yunara (i:4.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 1 | 3-5 | 22:50:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 22:50:56 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Lutador | DA_18_MasterYi_AD | 0.8000 |  |
| Jogador 1 | 3-6 | 22:50:57 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.2700 |  |
| Jogador 1 | 3-6 | 22:50:57 | MOVE Board -> Board: Alistar (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 22:50:57 | MOVE Board -> Board: Diana (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 22:50:57 | MOVE Board -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 22:50:58 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 22:51:05 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Lutador | DA_18_MasterYi_AD | 0.3100 |  |
| Jogador 1 | 3-7 | 22:51:07 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 1 | 3-7 | 22:51:07 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_RecurveBow -> Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.1600 |  |
| Jogador 1 | 3-7 | 22:51:08 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_BFSword -> Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.1900 |  |
| Jogador 1 | 3-7 | 22:51:08 | MOVE Board -> Board: Elise (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 22:51:08 | MOVE Board -> Board: Yunara (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 1 | 3-7 | 22:51:09 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 22:51:14 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Lutador | DA_18_MasterYi_AD | 0.2800 |  |
| Jogador 1 | 4-1 | 22:51:15 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Lutador | DA_18_MasterYi_AD | 0.8100 |  |
| Jogador 1 | 4-1 | 22:51:15 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Lutador | DA_18_MasterYi_AD | -0.1100 |  |
| Jogador 1 | 4-1 | 22:51:15 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Lutador | DA_18_MasterYi_AD | 0.2700 |  |
| Jogador 1 | 4-1 | 22:51:15 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Lutador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 1 | 4-1 | 22:51:15 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Lutador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 1 | 4-1 | 22:51:16 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Lutador | DA_18_MasterYi_AD | -0.2600 |  |
| Jogador 1 | 4-1 | 22:51:16 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 1 | 4-1 | 22:51:16 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Lutador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 1 | 4-1 | 22:51:18 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 22:51:19 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 22:51:25 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 9 | 0 | Lutador | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 1 | 4-2 | 22:51:25 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Lutador | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 1 | 4-2 | 22:51:25 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Lutador | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 1 | 4-2 | 22:51:26 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Lutador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 1 | 4-2 | 22:51:26 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 1 | 4-2 | 22:51:26 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Lutador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 1 | 4-2 | 22:51:26 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 1 | 4-2 | 22:51:27 | MOVE Board -> Board: Yunara (i:4.0) <-> Alistar (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 1 | 4-2 | 22:51:27 | MOVE Board -> Board: Alistar (i:8.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 1 | 4-2 | 22:51:30 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 2 | ? | 22:48:49 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0200 |  |
| Jogador 2 | ? | 22:48:50 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.3100 |  |
| Jogador 2 | ? | 22:48:50 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.6000 |  |
| Jogador 2 | ? | 22:48:50 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 2 | ? | 22:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-1 | 22:48:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 2 | 1-1 | 22:48:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-1 | 22:48:56 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 2 | 1-1 | 22:48:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-1 | 22:48:57 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4000 |  |
| Jogador 2 | 1-1 | 22:48:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-2 | 22:49:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2600 |  |
| Jogador 2 | 1-2 | 22:49:02 | MOVE Board -> Board: Leona (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-2 | 22:49:03 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 2 | 1-2 | 22:49:03 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-3 | 22:49:09 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 1.1200 |  |
| Jogador 2 | 1-3 | 22:49:09 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3900 |  |
| Jogador 2 | 1-3 | 22:49:09 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.4400 |  |
| Jogador 2 | 1-3 | 22:49:10 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1500 |  |
| Jogador 2 | 1-3 | 22:49:10 | MOVE Board -> Board: Yorick (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-3 | 22:49:10 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 2 | 1-3 | 22:49:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-4 | 22:49:15 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | -0.1100 |  |
| Jogador 2 | 1-4 | 22:49:16 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 2 | 1-4 | 22:49:16 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4200 |  |
| Jogador 2 | 1-4 | 22:49:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3700 |  |
| Jogador 2 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_SparringGloves -> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 2 | 1-4 | 22:49:18 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.1800 |  |
| Jogador 2 | 1-4 | 22:49:18 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | -0.0800 |  |
| Jogador 2 | 1-4 | 22:49:19 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0600 |  |
| Jogador 2 | 1-4 | 22:49:19 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.0100 |  |
| Jogador 2 | 1-4 | 22:49:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 2-1 | 22:49:22 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Yorick | 1.0100 |  |
| Jogador 2 | 2-1 | 22:49:22 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Yorick | -0.4600 |  |
| Jogador 2 | 2-1 | 22:49:23 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 2 | 2-1 | 22:49:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | -0.0400 |  |
| Jogador 2 | 2-1 | 22:49:24 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 2-1 | 22:49:24 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 2 | 2-1 | 22:49:24 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Yorick | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-1 | 22:49:25 | COMPROU: Xayah (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Yorick | 0.0600 |  |
| Jogador 2 | 2-1 | 22:49:25 | VENDEU: Xayah (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Yorick | -0.3200 |  |
| Jogador 2 | 2-1 | 22:49:25 | COMPROU: Veigar (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Yorick | 0.0600 |  |
| Jogador 2 | 2-1 | 22:49:25 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 2-2 | 22:49:29 | VENDEU: Veigar (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 2 | 2-2 | 22:49:30 | COMPROU: Master Yi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Yorick | 0.0900 |  |
| Jogador 2 | 2-2 | 22:49:30 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Yorick (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Yorick | -0.6500 |  |
| Jogador 2 | 2-2 | 22:49:30 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Vi18 | -0.4300 |  |
| Jogador 2 | 2-2 | 22:49:30 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Vi18 | 0.1100 |  |
| Jogador 2 | 2-2 | 22:49:31 | MOVE Bench -> Board: Alistar (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Vi18 | -0.6300 |  |
| Jogador 2 | 2-2 | 22:49:31 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Vi18 | 0.4100 |  |
| Jogador 2 | 2-2 | 22:49:31 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Vi18 | 0.1300 |  |
| Jogador 2 | 2-2 | 22:49:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 2 | 2-2 | 22:49:32 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Vi18 | 0.0100 |  |
| Jogador 2 | 2-2 | 22:49:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-3 | 22:49:36 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Fiddlesticks18 | 0.3700 |  |
| Jogador 2 | 2-3 | 22:49:37 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 2 | 2-3 | 22:49:37 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Fiddlesticks18 | 0.2200 |  |
| Jogador 2 | 2-3 | 22:49:38 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 2-3 | 22:49:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 2-4 | 22:49:43 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Fiddlesticks18 | 0.2200 |  |
| Jogador 2 | 2-4 | 22:49:44 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 2-4 | 22:49:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 2-4 | 22:49:44 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 2-4 | 22:49:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 2-5 | 22:49:50 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 2 | 2-5 | 22:49:51 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 2-5 | 22:49:51 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Colosso | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 2 | 2-5 | 22:49:51 | COMPROU: Sejuani (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 0 | Colosso | DA_Fiddlesticks18 | 1.0400 |  |
| Jogador 2 | 2-5 | 22:49:52 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 0 | Colosso | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 2 | 2-5 | 22:49:53 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 0 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 2-5 | 22:49:53 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 0 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 2-5 | 22:49:53 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 0 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 2 | 2-6 | 22:49:58 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 2 | 2-6 | 22:49:58 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 2-6 | 22:49:58 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Fiddlesticks18 | -0.7200 |  |
| Jogador 2 | 2-6 | 22:49:58 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 2 | 2-7 | 22:50:05 | VENDEU: Vi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 2 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 2-7 | 22:50:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Colosso | DA_Fiddlesticks18 | 0.2500 |  |
| Jogador 2 | 2-7 | 22:50:06 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_SparringGloves -> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Colosso | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 2 | 2-7 | 22:50:06 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 2 | Colosso | DA_Fiddlesticks18 | -0.3800 |  |
| Jogador 2 | 2-7 | 22:50:06 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 35 | 2 | Colosso | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 2 | 2-7 | 22:50:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 2 | 2-7 | 22:50:07 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Colosso | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 2 | 2-7 | 22:50:08 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Colosso | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 2 | 2-7 | 22:50:08 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 2-7 | 22:50:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 2-7 | 22:50:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Colosso | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 2 | 3-1 | 22:50:13 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Colosso | DA_Fiddlesticks18 | 0.2500 |  |
| Jogador 2 | 3-1 | 22:50:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Colosso | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 2 | 3-1 | 22:50:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 2 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 2 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 2 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 2 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 2 | 3-1 | 22:50:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 2 | Colosso | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 2 | 3-1 | 22:50:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 2 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-1 | 22:50:18 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 2 | Colosso | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 2 | 3-2 | 22:50:21 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Amumu18 | 0.1200 |  |
| Jogador 2 | 3-2 | 22:50:21 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Amumu18 | 0.2100 |  |
| Jogador 2 | 3-2 | 22:50:21 | MOVE Board -> Board: Rammus (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-2 | 22:50:22 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | 0.0700 |  |
| Jogador 2 | 3-2 | 22:50:22 | MOVE Bench -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | -0.3300 |  |
| Jogador 2 | 3-2 | 22:50:22 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | 0.0800 |  |
| Jogador 2 | 3-2 | 22:50:23 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | -0.7200 |  |
| Jogador 2 | 3-2 | 22:50:23 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-2 | 22:50:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-3 | 22:50:30 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Fiddlesticks18 | 0.6500 |  |
| Jogador 2 | 3-3 | 22:50:30 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Fiddlesticks18 | 0.7600 |  |
| Jogador 2 | 3-3 | 22:50:30 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Fiddlesticks18 | 0.5900 |  |
| Jogador 2 | 3-3 | 22:50:30 | MOVE Bench -> Board: Amumu (i:8.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 2 | 3-3 | 22:50:31 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | 0.6000 |  |
| Jogador 2 | 3-3 | 22:50:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-4 | 22:50:39 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Fiddlesticks18 | 0.7500 |  |
| Jogador 2 | 3-4 | 22:50:39 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Fiddlesticks18 | 0.5400 |  |
| Jogador 2 | 3-4 | 22:50:39 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 2 | 3-4 | 22:50:39 | MOVE Board -> Board: Amumu (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-4 | 22:50:40 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Fiddlesticks18 | 0.4100 |  |
| Jogador 2 | 3-4 | 22:50:40 | COMPROU: Varus (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 2 | 3-4 | 22:50:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-5 | 22:50:48 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Fiddlesticks18 | 0.7700 |  |
| Jogador 2 | 3-5 | 22:50:49 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Fiddlesticks18 | 0.2100 |  |
| Jogador 2 | 3-5 | 22:50:49 | MOVE Bench -> Board: Varus (i:2.0) <-> Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 2 | 3-5 | 22:50:49 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 2 | 3-5 | 22:50:50 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Fiddlesticks18 | -0.3200 |  |
| Jogador 2 | 3-5 | 22:50:50 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 2 | 3-5 | 22:50:50 | MOVE Board -> Board: Cascalho (i:2.0) <-> Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-5 | 22:50:50 | MOVE Board -> Board: Amumu (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-5 | 22:50:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-5 | 22:50:53 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | 0.6000 |  |
| Jogador 2 | 3-6 | 22:50:56 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 2 | 3-6 | 22:50:57 | VENDEU: Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 2 | 3-6 | 22:50:57 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | -0.1800 |  |
| Jogador 2 | 3-6 | 22:50:57 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-6 | 22:50:57 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-6 | 22:50:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-7 | 22:51:05 | VENDEU: Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Fiddlesticks18 | -0.1400 |  |
| Jogador 2 | 3-7 | 22:51:07 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Fiddlesticks18 | -0.2300 |  |
| Jogador 2 | 3-7 | 22:51:07 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_RecurveBow -> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 2 | 3-7 | 22:51:08 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_ChainVest -> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 2 | 3-7 | 22:51:08 | VENDEU: Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 2 | 3-7 | 22:51:08 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 2 | 3-7 | 22:51:09 | MOVE Bench -> Board: Lillia (i:8.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 2 | 3-7 | 22:51:09 | MOVE Board -> Board: Lillia (i:8.0) <-> Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-7 | 22:51:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 4-1 | 22:51:14 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 2 | 4-1 | 22:51:15 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_Fiddlesticks18 | 0.2200 |  |
| Jogador 2 | 4-1 | 22:51:15 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 2 | 4-1 | 22:51:15 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 2 | 4-1 | 22:51:15 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 2 | 4-1 | 22:51:15 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 2 | 4-1 | 22:51:16 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_Fiddlesticks18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 2 | 4-1 | 22:51:16 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 2 | 4-1 | 22:51:16 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_Fiddlesticks18 | 0.7300 |  |
| Jogador 2 | 4-1 | 22:51:18 | VENDEU: Sejuani (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 2 | 4-1 | 22:51:19 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 2 | 4-2 | 22:51:25 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Master Yi (i:6.0) (tabuleiro slot 10) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Colosso | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 2 | 4-2 | 22:51:25 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Cascalho (i:2.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Colosso | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 2 | 4-2 | 22:51:25 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Cascalho (i:2.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Colosso | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 2 | 4-2 | 22:51:26 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_Fiddlesticks18 | 0.6300 |  |
| Jogador 2 | 4-2 | 22:51:26 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Colosso | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 2 | 4-2 | 22:51:26 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 2 | 4-2 | 22:51:26 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 2 | 4-2 | 22:51:27 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_Fiddlesticks18 | -0.2400 | FAST8_REROLL_REVIEW |
| Jogador 2 | 4-2 | 22:51:27 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 2 | 4-2 | 22:51:30 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Mamãe Bicuda (i:6.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 2 | 4-2 | 22:51:30 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 2 | 4-3 | 22:51:33 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Mamãe Bicuda (i:6.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 2 | 4-3 | 22:51:34 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Colosso | DA_Fiddlesticks18 | 0.2300 |  |
| Jogador 2 | 4-3 | 22:51:34 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Colosso | DA_Fiddlesticks18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 2 | 4-3 | 22:51:37 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 2 | 4-3 | 22:51:37 | COMPROU: Varus (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Colosso | DA_Fiddlesticks18 | 0.7400 |  |
| Jogador 2 | 4-3 | 22:51:37 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Colosso | DA_Fiddlesticks18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 2 | 4-3 | 22:51:38 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 2 | 4-3 | 22:51:38 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Colosso | DA_Fiddlesticks18 | -0.1400 |  |
| Jogador 2 | 4-3 | 22:51:38 | MOVE Bench -> Board: Varus (i:2.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Colosso | DA_Fiddlesticks18 | -0.5600 |  |
| Jogador 2 | 4-3 | 22:51:39 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Colosso | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 2 | 4-3 | 22:51:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Colosso | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 2 | 4-4 | 22:51:45 | MOVE Bench -> Board: Lillia (i:8.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Colosso | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 2 | 4-4 | 22:51:46 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Colosso | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 2 | 4-4 | 22:51:46 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Fiddlesticks18 | 0.6900 |  |
| Jogador 2 | 4-4 | 22:51:46 | MOVE Bench -> Board: Varus (i:2.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Fiddlesticks18 | -0.5600 |  |
| Jogador 2 | 4-4 | 22:51:46 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 2 | 4-4 | 22:51:47 | MOVE Bench -> Board: Lillia (i:8.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 4-4 | 22:51:47 | MOVE Bench -> Board: Varus (i:2.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Fiddlesticks18 | -0.5700 |  |
| Jogador 2 | 4-4 | 22:51:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 2 | 4-5 | 22:51:55 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 2 | 4-5 | 22:51:55 | MOVE Bench -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 2 | 4-5 | 22:51:55 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Fiddlesticks18 | -0.6600 |  |
| Jogador 2 | 4-5 | 22:51:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 2 | 4-6 | 22:52:07 | VENDEU: Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Colosso | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 2 | 4-6 | 22:52:07 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Colosso | DA_Fiddlesticks18 | 0.8100 |  |
| Jogador 2 | 4-6 | 22:52:07 | VENDEU: Fiddlesticks (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 3 | Colosso | DA_18_Rammus | -0.0900 |  |
| Jogador 2 | 4-6 | 22:52:07 | COMPROU: Alune (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 3 | Colosso | DA_18_Rammus | 0.0100 |  |
| Jogador 2 | 4-6 | 22:52:08 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Colosso | DA_18_Rammus | -0.1700 | FAST8_REROLL_REVIEW |
| Jogador 2 | 4-6 | 22:52:08 | VENDEU: Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 3 | Colosso | DA_18_Alune | -0.0600 |  |
| Jogador 2 | 4-6 | 22:52:08 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 3 | Colosso | DA_CrimsonRaptor18 | 0.8900 |  |
| Jogador 2 | 4-6 | 22:52:08 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 3 | Colosso | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 2 | 4-6 | 22:52:08 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 3 | Colosso | DA_CrimsonRaptor18 | 0.5700 |  |
| Jogador 2 | 4-6 | 22:52:11 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Colosso | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 2 | 4-6 | 22:52:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Colosso | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 2 | 4-7 | 22:52:17 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_ChainVest -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 2 | 4-7 | 22:52:17 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_TearOfTheGoddess -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Colosso | DA_CrimsonRaptor18 | 0.1200 |  |
| Jogador 2 | 4-7 | 22:52:20 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 2 | 4-7 | 22:52:20 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Colosso | DA_CrimsonRaptor18 | -0.0600 |  |
| Jogador 2 | 4-7 | 22:52:20 | MOVE Bench -> Board: Malphite (i:8.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Colosso | DA_CrimsonRaptor18 | -0.4000 |  |
| Jogador 2 | 4-7 | 22:52:21 | VENDEU: Mamãe Bicuda (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 4 | Colosso | DA_18_Alune | -0.1700 |  |
| Jogador 2 | 4-7 | 22:52:21 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Kha'Zix (i:6.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 4 | Colosso | DA_18_Alune | 0.0800 |  |
| Jogador 2 | 4-7 | 22:52:21 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Lillia (i:8.0) (tabuleiro slot 2) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 4 | Colosso | DA_18_Alune | 0.0900 |  |
| Jogador 2 | 4-7 | 22:52:22 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 4 | Colosso | DA_18_Alune | 0.1900 |  |
| Jogador 2 | 4-7 | 22:52:22 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Colosso | DA_18_Alune | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 2 | 4-7 | 22:52:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Colosso | DA_18_Alune | -0.0900 |  |
| Jogador 2 | 5-1 | 22:52:29 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_18_Alune | 0.0400 |  |
| Jogador 2 | 5-1 | 22:52:29 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Colosso | DA_18_Alune | -0.0300 |  |
| Jogador 2 | 5-1 | 22:52:29 | MOVE Board -> Board: Malphite (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Colosso | DA_18_Alune | 0.0000 |  |
| Jogador 2 | 5-1 | 22:52:29 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Colosso | DA_18_Alune | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 2 | 5-1 | 22:52:29 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Colosso | DA_18_Alune | 0.0700 |  |
| Jogador 2 | 5-1 | 22:52:30 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Colosso | DA_18_Alune | 0.2700 |  |
| Jogador 2 | 5-1 | 22:52:30 | VENDEU: Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Colosso | DA_18_Alune | 0.0500 |  |
| Jogador 2 | 5-1 | 22:52:30 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Colosso | DA_18_Alune | 0.1700 |  |
| Jogador 2 | 5-1 | 22:52:30 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Colosso | DA_18_Alune | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 2 | 5-1 | 22:52:33 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Colosso | DA_18_Alune | 0.0400 |  |
| Jogador 2 | 5-1 | 22:52:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Colosso | DA_18_Alune | -0.2500 |  |
| Jogador 2 | 5-2 | 22:52:38 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_18_Alune | 0.6400 |  |
| Jogador 2 | 5-2 | 22:52:38 | VENDEU: Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 74 | 5 | Colosso | DA_18_Alune | -0.3600 |  |
| Jogador 2 | 5-2 | 22:52:42 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_18_Alune | 0.1900 |  |
| Jogador 2 | 5-2 | 22:52:42 | MOVE Bench -> Board: Varus (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_18_Alune | 0.1000 |  |
| Jogador 2 | 5-2 | 22:52:42 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_18_Alune | -0.1900 |  |
| Jogador 2 | 5-2 | 22:52:42 | MOVE Bench -> Board: Malphite (i:8.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 5-2 | 22:52:42 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_18_Alune | -0.1000 |  |
| Jogador 2 | 5-3 | 22:52:50 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Colosso | DA_18_Alune | 0.0400 |  |
| Jogador 2 | 5-3 | 22:52:50 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Colosso | DA_18_Alune | 0.3900 |  |
| Jogador 2 | 5-3 | 22:52:50 | MOVE Bench -> Board: Varus (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Colosso | DA_18_Alune | 0.1000 |  |
| Jogador 2 | 5-3 | 22:52:50 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Colosso | DA_18_Alune | -0.1900 |  |
| Jogador 2 | 5-3 | 22:52:51 | MOVE Bench -> Board: Malphite (i:8.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 5-3 | 22:52:51 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Colosso | DA_18_Alune | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-4 | 22:52:59 | MOVE Bench -> Board: Varus (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Colosso | DA_18_Alune | 0.1000 |  |
| Jogador 2 | 5-4 | 22:52:59 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Colosso | DA_18_Alune | -0.1900 |  |
| Jogador 2 | 5-4 | 22:53:00 | MOVE Bench -> Board: Malphite (i:8.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 5-4 | 22:53:00 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Colosso | DA_18_Alune | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-5 | 22:53:12 | MOVE Bench -> Board: Lillia (i:8.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Colosso | DA_18_Alune | -0.6800 |  |
| Jogador 2 | 5-5 | 22:53:12 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Colosso | DA_18_Alune | -0.1400 |  |
| Jogador 2 | 5-5 | 22:53:12 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Alune | 0.1900 |  |
| Jogador 2 | 5-5 | 22:53:13 | MOVE Bench -> Board: Varus (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Alune | 0.1000 |  |
| Jogador 2 | 5-5 | 22:53:13 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Alune | -0.2900 |  |
| Jogador 2 | 5-5 | 22:53:13 | MOVE Bench -> Board: Lillia (i:8.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Alune | -0.6900 |  |
| Jogador 2 | 5-5 | 22:53:13 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Alune | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-6 | 22:53:22 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 120 | 5 | Colosso | DA_18_Alune | 0.0500 |  |
| Jogador 2 | 5-6 | 22:53:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Colosso | DA_18_Alune | 0.7100 |  |
| Jogador 2 | 5-6 | 22:53:22 | MOVE Bench -> Board: Varus (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Colosso | DA_18_Alune | 0.1000 |  |
| Jogador 2 | 5-6 | 22:53:22 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Colosso | DA_18_Alune | -0.2900 |  |
| Jogador 2 | 5-6 | 22:53:22 | MOVE Bench -> Board: Lillia (i:8.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Colosso | DA_18_Alune | -0.7000 |  |
| Jogador 2 | 5-6 | 22:53:23 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Colosso | DA_18_Alune | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-7 | 22:53:31 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Lillia (i:8.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 128 | 5 | Colosso | DA_18_Alune | 0.0800 |  |
| Jogador 2 | 5-7 | 22:53:31 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Colosso | DA_18_Alune | -0.1400 |  |
| Jogador 2 | 5-7 | 22:53:32 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 130 | 5 | Colosso | DA_18_Alune | 1.0000 |  |
| Jogador 2 | 5-7 | 22:53:32 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Colosso | DA_18_Alune | -0.3700 |  |
| Jogador 2 | 5-7 | 22:53:35 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 128 | 5 | Colosso | DA_18_Alune | 0.2600 |  |
| Jogador 2 | 5-7 | 22:53:36 | REROLL | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_18_Alune | -0.0900 |  |
| Jogador 2 | 5-7 | 22:53:36 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_18_Alune | 0.0400 |  |
| Jogador 2 | 5-7 | 22:53:36 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_18_Alune | 0.9400 |  |
| Jogador 2 | 5-7 | 22:53:36 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_18_Alune | -0.2700 |  |
| Jogador 2 | 5-7 | 22:53:36 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_18_Alune | 0.4100 |  |
| Jogador 2 | 5-7 | 22:53:37 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_18_Alune | -0.1900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 6-1 | 22:53:41 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Colosso | DA_18_Alune | 0.0900 |  |
| Jogador 2 | 6-1 | 22:53:41 | MOVE Bench -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Colosso | DA_18_Alune | 0.0100 |  |
| Jogador 2 | 6-1 | 22:53:41 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Colosso | DA_18_Alune | -0.4200 |  |
| Jogador 2 | 6-1 | 22:53:41 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Colosso | DA_18_Alune | 0.0800 |  |
| Jogador 2 | 6-1 | 22:53:42 | MOVE Bench -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Colosso | DA_18_Alune | 0.0100 |  |
| Jogador 2 | 6-1 | 22:53:42 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Alune | 0.0700 |  |
| Jogador 2 | 6-1 | 22:53:42 | EQUIP_FROM_INVENTORY: TFT_Item_Crownguard -> Lillia (i:8.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Alune | 0.0700 |  |
| Jogador 2 | 6-1 | 22:53:42 | EQUIP_FROM_INVENTORY: TFT_Item_FrozenHeart -> Malphite (i:8.0) (tabuleiro slot 2) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Alune | 0.0900 |  |
| Jogador 2 | 6-1 | 22:53:43 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Malphite (i:8.0) (tabuleiro slot 2) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Alune | 0.0700 |  |
| Jogador 2 | 6-1 | 22:53:43 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Colosso | DA_18_Alune | 0.2500 |  |
| Jogador 2 | 6-2 | 22:53:51 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Colosso | DA_18_Alune | 0.0400 |  |
| Jogador 2 | 6-2 | 22:53:51 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Colosso | DA_18_Alune | 0.9500 |  |
| Jogador 2 | 6-2 | 22:53:51 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Colosso | DA_18_Alune | 0.1000 |  |
| Jogador 2 | 6-2 | 22:53:51 | MOVE Bench -> Board: Lillia (i:8.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 6-2 | 22:53:52 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 6-2 | 22:53:52 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Colosso | DA_18_Alune | -0.3000 |  |
| Jogador 2 | 6-3 | 22:54:01 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Colosso | DA_18_Alune | 0.1000 |  |
| Jogador 2 | 6-3 | 22:54:01 | MOVE Bench -> Board: Lillia (i:8.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 6-3 | 22:54:01 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Colosso | DA_18_Alune | 0.0500 |  |
| Jogador 2 | 6-3 | 22:54:02 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Colosso | DA_18_Alune | 0.3700 |  |
| Jogador 2 | 6-3 | 22:54:02 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Colosso | DA_18_Alune | -0.0900 |  |
| Jogador 2 | 6-3 | 22:54:02 | VENDEU: Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Colosso | DA_18_Alune | -0.0600 |  |
| Jogador 2 | 6-3 | 22:54:02 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_18_Alune | 0.2000 |  |
| Jogador 2 | 6-3 | 22:54:06 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_18_Alune | -0.4000 |  |
| Jogador 2 | 6-3 | 22:54:06 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_18_Alune | 0.0800 |  |
| Jogador 2 | 6-3 | 22:54:07 | MOVE Bench -> Board: Lillia (i:8.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 6-4 | 22:54:11 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Colosso | DA_18_Alune | -0.4000 |  |
| Jogador 2 | 6-4 | 22:54:11 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Colosso | DA_18_Alune | 0.0800 |  |
| Jogador 2 | 6-4 | 22:54:11 | MOVE Bench -> Board: Lillia (i:8.0) <-> Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Colosso | DA_18_Alune | -0.2100 |  |
| Jogador 2 | 6-4 | 22:54:12 | MOVE Bench -> Board: Malphite (i:8.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 6-4 | 22:54:12 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Colosso | DA_18_Alune | -0.3100 |  |
| Jogador 2 | 6-5 | 22:54:21 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Colosso | DA_18_Alune | -0.0600 |  |
| Jogador 2 | 6-5 | 22:54:22 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Colosso | DA_18_Alune | 1.0100 |  |
| Jogador 2 | 6-5 | 22:54:22 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Colosso | DA_18_Alune | -0.4000 |  |
| Jogador 2 | 6-5 | 22:54:22 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Colosso | DA_18_Alune | 0.0800 |  |
| Jogador 2 | 6-5 | 22:54:23 | MOVE Bench -> Board: Malphite (i:8.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 6-5 | 22:54:23 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Colosso | DA_18_Alune | -0.4100 |  |
| Jogador 2 | 6-5 | 22:54:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Colosso | DA_18_Alune | -0.3300 |  |
| Jogador 3 | ? | 22:48:49 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 3 | ? | 22:48:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.3000 |  |
| Jogador 3 | ? | 22:48:50 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.6000 |  |
| Jogador 3 | ? | 22:48:50 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | -0.0100 |  |
| Jogador 3 | ? | 22:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.0000 |  |
| Jogador 3 | 1-1 | 22:48:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_RekSai | 1.0400 |  |
| Jogador 3 | 1-1 | 22:48:56 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_RekSai | -0.3900 |  |
| Jogador 3 | 1-1 | 22:48:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1500 |  |
| Jogador 3 | 1-1 | 22:48:57 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1800 |  |
| Jogador 3 | 1-1 | 22:48:57 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0600 |  |
| Jogador 3 | 1-1 | 22:48:58 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 1-1 | 22:48:58 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 3 | 1-1 | 22:48:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 1-1 | 22:49:01 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4000 |  |
| Jogador 3 | 1-2 | 22:49:02 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.1000 |  |
| Jogador 3 | 1-2 | 22:49:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 3 | 1-3 | 22:49:09 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | -0.0800 |  |
| Jogador 3 | 1-3 | 22:49:09 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.2400 |  |
| Jogador 3 | 1-3 | 22:49:09 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | -0.3700 |  |
| Jogador 3 | 1-3 | 22:49:10 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 1-3 | 22:49:10 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.1900 |  |
| Jogador 3 | 1-3 | 22:49:10 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 1-3 | 22:49:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 1-3 | 22:49:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 1-4 | 22:49:15 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 1.0300 |  |
| Jogador 3 | 1-4 | 22:49:16 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.5200 |  |
| Jogador 3 | 1-4 | 22:49:16 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.3400 |  |
| Jogador 3 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_BFSword -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.2200 |  |
| Jogador 3 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 1-4 | 22:49:18 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 1-4 | 22:49:18 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 1-4 | 22:49:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-1 | 22:49:22 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 1.1200 |  |
| Jogador 3 | 2-1 | 22:49:22 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.6300 |  |
| Jogador 3 | 2-1 | 22:49:23 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 2-1 | 22:49:23 | MOVE Board -> Board: Yorick (i:2.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-1 | 22:49:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-1 | 22:49:27 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.4900 |  |
| Jogador 3 | 2-2 | 22:49:29 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | 1.0400 |  |
| Jogador 3 | 2-2 | 22:49:30 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 2-2 | 22:49:30 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 2-2 | 22:49:30 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-2 | 22:49:30 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | -0.3000 |  |
| Jogador 3 | 2-2 | 22:49:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-3 | 22:49:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 0 | — | DA_Scuttlecrab18 | 0.5100 |  |
| Jogador 3 | 2-3 | 22:49:37 | COMPROU: Rengar (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_Scuttlecrab18 | 0.1300 |  |
| Jogador 3 | 2-3 | 22:49:37 | MOVE Bench -> Board: Rengar (i:6.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_Scuttlecrab18 | -0.0600 |  |
| Jogador 3 | 2-3 | 22:49:38 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 11 | 0 | — | DA_Scuttlecrab18 | -0.0700 |  |
| Jogador 3 | 2-3 | 22:49:38 | COMPROU: Hecarim (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 2-3 | 22:49:39 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 2-3 | 22:49:39 | MOVE Board -> Board: Hecarim (i:6.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-3 | 22:49:39 | MOVE Board -> Board: Sejuani (i:4.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-3 | 22:49:39 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-4 | 22:49:43 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | Colosso | DA_Scuttlecrab18 | 0.3300 |  |
| Jogador 3 | 2-4 | 22:49:44 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | Colosso | DA_Scuttlecrab18 | -0.5200 |  |
| Jogador 3 | 2-4 | 22:49:44 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 2-4 | 22:49:44 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | Colosso | DA_Scuttlecrab18 | -0.4100 |  |
| Jogador 3 | 2-4 | 22:49:45 | MOVE Board -> Board: Hecarim (i:6.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-4 | 22:49:46 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-5 | 22:49:50 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 2-5 | 22:49:51 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | 1.0200 |  |
| Jogador 3 | 2-5 | 22:49:51 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | -0.5800 |  |
| Jogador 3 | 2-5 | 22:49:51 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | 0.0300 |  |
| Jogador 3 | 2-5 | 22:49:52 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-5 | 22:49:53 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 2-5 | 22:49:53 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 3 | 2-5 | 22:49:53 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 2-5 | 22:49:54 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 2-5 | 22:49:54 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | -0.5800 |  |
| Jogador 3 | 2-5 | 22:49:54 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-6 | 22:49:58 | VENDEU: Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 1 | Colosso | DA_18_Hecarim | -0.5600 |  |
| Jogador 3 | 2-6 | 22:49:58 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Aronguejo (i:4.0) (tabuleiro slot 10) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 1 | Colosso | DA_18_Hecarim | 0.1800 |  |
| Jogador 3 | 2-6 | 22:49:58 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Aronguejo (i:4.0) (tabuleiro slot 10) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 1 | Colosso | DA_18_Hecarim | 0.1200 |  |
| Jogador 3 | 2-6 | 22:49:58 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 1 | Colosso | DA_18_Hecarim | -0.2700 |  |
| Jogador 3 | 2-6 | 22:49:59 | VENDEU: Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 1 | Colosso | DA_18_Hecarim | -0.0100 |  |
| Jogador 3 | 2-6 | 22:49:59 | VENDEU: Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 33 | 1 | Colosso | DA_18_Hecarim | -0.9100 |  |
| Jogador 3 | 2-6 | 22:50:00 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 1 | Colosso | DA_Scuttlecrab18 | 1.0500 |  |
| Jogador 3 | 2-6 | 22:50:00 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 1 | Colosso | DA_Scuttlecrab18 | 0.3500 |  |
| Jogador 3 | 2-6 | 22:50:01 | COMPROU: Diana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 1 | Colosso | DA_Scuttlecrab18 | 0.1100 |  |
| Jogador 3 | 2-6 | 22:50:01 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 1 | Colosso | DA_Scuttlecrab18 | 0.4200 |  |
| Jogador 3 | 2-6 | 22:50:01 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 1 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-7 | 22:50:05 | COMPROU: Vi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 32 | 2 | Colosso | DA_Scuttlecrab18 | 0.2300 |  |
| Jogador 3 | 2-7 | 22:50:05 | MOVE Board -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 32 | 2 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-7 | 22:50:06 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 32 | 2 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-7 | 22:50:06 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 32 | 2 | Colosso | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 3-1 | 22:50:13 | MOVE Bench -> Board: Vi (i:6.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 41 | 3 | Colosso | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 3-1 | 22:50:13 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 41 | 3 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 3-1 | 22:50:13 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 41 | 3 | Colosso | DA_Scuttlecrab18 | -0.4100 |  |
| Jogador 3 | 3-1 | 22:50:14 | MOVE Bench -> Board: Vi (i:6.0) <-> Diana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 41 | 3 | Colosso | DA_Scuttlecrab18 | -0.6100 |  |
| Jogador 3 | 3-1 | 22:50:14 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 41 | 3 | Colosso | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 3-2 | 22:50:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | 0.2800 |  |
| Jogador 3 | 3-2 | 22:50:21 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 3-2 | 22:50:21 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | -0.4100 |  |
| Jogador 3 | 3-2 | 22:50:22 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | 0.1300 |  |
| Jogador 3 | 3-2 | 22:50:22 | MOVE Bench -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 3-2 | 22:50:22 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Diana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 3-2 | 22:50:23 | MOVE Bench -> Board: Diana (i:6.0) <-> Vi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 3-2 | 22:50:23 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Diana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-2 | 22:50:23 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 4 | Colosso | DA_Scuttlecrab18 | -0.1200 |  |
| Jogador 3 | 3-3 | 22:50:30 | COMPROU: Rakan (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 58 | 4 | Colosso | DA_Scuttlecrab18 | 0.3500 |  |
| Jogador 3 | 3-3 | 22:50:30 | MOVE Board -> Board: Diana (i:6.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 58 | 4 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-3 | 22:50:30 | COMPROU: Elise (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 4 | Colosso | DA_Scuttlecrab18 | -0.1200 |  |
| Jogador 3 | 3-3 | 22:50:30 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 4 | Colosso | DA_Scuttlecrab18 | 0.0000 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-3 | 22:50:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 4 | Colosso | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 3-3 | 22:50:31 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 4 | Colosso | DA_Scuttlecrab18 | 0.5900 |  |
| Jogador 3 | 3-3 | 22:50:31 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Colosso | DA_Scuttlecrab18 | -0.1600 |  |
| Jogador 3 | 3-3 | 22:50:31 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-3 | 22:50:32 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-3 | 22:50:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 3-4 | 22:50:39 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Colosso | DA_Scuttlecrab18 | 0.8400 |  |
| Jogador 3 | 3-4 | 22:50:39 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Colosso | DA_Scuttlecrab18 | -0.3200 |  |
| Jogador 3 | 3-4 | 22:50:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 3-4 | 22:50:39 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 4 | Colosso | DA_Scuttlecrab18 | 0.2700 |  |
| Jogador 3 | 3-4 | 22:50:40 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Colosso | DA_Scuttlecrab18 | -0.2800 |  |
| Jogador 3 | 3-4 | 22:50:40 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Colosso | DA_Scuttlecrab18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 3 | 3-4 | 22:50:40 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 3-4 | 22:50:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Colosso | DA_Scuttlecrab18 | 0.7800 |  |
| Jogador 3 | 3-4 | 22:50:41 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-4 | 22:50:43 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-4 | 22:50:43 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 3-5 | 22:50:48 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Colosso | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 3-5 | 22:50:49 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Colosso | DA_Vi18 | 0.8300 |  |
| Jogador 3 | 3-5 | 22:50:49 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Colosso | DA_Vi18 | -0.3100 |  |
| Jogador 3 | 3-5 | 22:50:49 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Colosso | DA_Vi18 | 0.0100 |  |
| Jogador 3 | 3-5 | 22:50:50 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 4 | Colosso | DA_Vi18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 3 | 3-5 | 22:50:50 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 4 | Colosso | DA_Vi18 | 0.0600 |  |
| Jogador 3 | 3-5 | 22:50:50 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Colosso | DA_Vi18 | 0.2500 |  |
| Jogador 3 | 3-5 | 22:50:50 | MOVE Board -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 3 | 3-5 | 22:50:50 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 3 | 3-5 | 22:50:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Colosso | DA_Vi18 | -0.0400 |  |
| Jogador 3 | 3-6 | 22:50:56 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Colosso | DA_Vi18 | -0.1200 |  |
| Jogador 3 | 3-6 | 22:50:57 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Colosso | DA_Vi18 | 0.3100 |  |
| Jogador 3 | 3-6 | 22:50:57 | REROLL | STABILIZE | STABILIZE: pressão de vida | 51 | 4 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 3 | 3-6 | 22:50:57 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Colosso | DA_Vi18 | 0.0700 |  |
| Jogador 3 | 3-6 | 22:50:57 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Colosso | DA_Vi18 | 0.7700 |  |
| Jogador 3 | 3-6 | 22:50:58 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Colosso | DA_Vi18 | -0.6200 |  |
| Jogador 3 | 3-6 | 22:50:58 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Colosso | DA_Vi18 | 0.0500 |  |
| Jogador 3 | 3-6 | 22:50:58 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Colosso | DA_Vi18 | 0.2900 |  |
| Jogador 3 | 3-6 | 22:50:59 | REROLL | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Colosso | DA_Vi18 | -0.1700 |  |
| Jogador 3 | 3-6 | 22:50:59 | REROLL | STABILIZE | STABILIZE: pressão de vida | 46 | 4 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 3 | 3-6 | 22:51:01 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 46 | 4 | Colosso | DA_Vi18 | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-7 | 22:51:05 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 4 | Colosso | DA_Scuttlecrab18 | -0.1700 |  |
| Jogador 3 | 3-7 | 22:51:07 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 4 | Colosso | DA_Scuttlecrab18 | 0.8900 |  |
| Jogador 3 | 3-7 | 22:51:07 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_RecurveBow -> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 4 | Colosso | DA_Scuttlecrab18 | 0.2000 |  |
| Jogador 3 | 3-7 | 22:51:08 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_TearOfTheGoddess -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 4 | Colosso | DA_Scuttlecrab18 | 0.2200 |  |
| Jogador 3 | 3-7 | 22:51:08 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 4 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 3-7 | 22:51:08 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 4 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 3-7 | 22:51:09 | REROLL | STABILIZE | STABILIZE: pressão de vida | 62 | 4 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 3-7 | 22:51:09 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 4 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 3-7 | 22:51:09 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 4 | Colosso | DA_Scuttlecrab18 | 0.8300 |  |
| Jogador 3 | 3-7 | 22:51:09 | MOVE Bench -> Board: Tristana (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 4 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-7 | 22:51:09 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 62 | 4 | Colosso | DA_Scuttlecrab18 | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-1 | 22:51:14 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_Scuttlecrab18 | -0.3900 |  |
| Jogador 3 | 4-1 | 22:51:15 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_Scuttlecrab18 | -0.3100 |  |
| Jogador 3 | 4-1 | 22:51:15 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_Scuttlecrab18 | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-2 | 22:51:25 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Colosso | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 4-2 | 22:51:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_Scuttlecrab18 | 1.0500 |  |
| Jogador 3 | 4-2 | 22:51:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_Scuttlecrab18 | 0.9500 |  |
| Jogador 3 | 4-2 | 22:51:26 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_Scuttlecrab18 | 0.5600 |  |
| Jogador 3 | 4-2 | 22:51:26 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Colosso | DA_Scuttlecrab18 | 0.0300 |  |
| Jogador 3 | 4-2 | 22:51:26 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-2 | 22:51:26 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 4-2 | 22:51:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Colosso | DA_Scuttlecrab18 | 0.0300 |  |
| Jogador 3 | 4-2 | 22:51:27 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-2 | 22:51:30 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-2 | 22:51:30 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_Scuttlecrab18 | -0.2200 |  |
| Jogador 4 | ? | 22:48:49 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 4 | ? | 22:48:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 4 | ? | 22:48:50 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6100 |  |
| Jogador 4 | ? | 22:48:50 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | ? | 22:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-1 | 22:48:56 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 4 | 1-1 | 22:48:56 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 4 | 1-1 | 22:48:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 4 | 1-1 | 22:48:57 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-1 | 22:48:57 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.3900 |  |
| Jogador 4 | 1-1 | 22:48:58 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0600 |  |
| Jogador 4 | 1-1 | 22:48:58 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 4 | 1-1 | 22:48:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-2 | 22:49:02 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 4 | 1-2 | 22:49:02 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.3300 |  |
| Jogador 4 | 1-2 | 22:49:03 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Gromp18_AP | 0.2500 |  |
| Jogador 4 | 1-2 | 22:49:03 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 4 | 1-2 | 22:49:03 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Alistar | 0.2200 |  |
| Jogador 4 | 1-2 | 22:49:04 | MOVE Board -> Board: Kobuko (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Alistar | 0.0000 |  |
| Jogador 4 | 1-2 | 22:49:04 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Alistar | -0.0100 |  |
| Jogador 4 | 1-2 | 22:49:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Alistar | 0.0000 |  |
| Jogador 4 | 1-3 | 22:49:09 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 4 | 1-3 | 22:49:09 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 4 | 1-3 | 22:49:09 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.8300 |  |
| Jogador 4 | 1-3 | 22:49:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 4 | 1-3 | 22:49:10 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.8300 |  |
| Jogador 4 | 1-3 | 22:49:10 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 4 | 1-3 | 22:49:11 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.3300 |  |
| Jogador 4 | 1-3 | 22:49:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0400 |  |
| Jogador 4 | 1-3 | 22:49:11 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 4 | 1-3 | 22:49:12 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.3900 |  |
| Jogador 4 | 1-3 | 22:49:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-4 | 22:49:15 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Gromp18_AP | 0.2400 |  |
| Jogador 4 | 1-4 | 22:49:16 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Gromp18_AP | 0.4600 |  |
| Jogador 4 | 1-4 | 22:49:16 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 1.0300 |  |
| Jogador 4 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_RecurveBow -> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.1700 |  |
| Jogador 4 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.1200 |  |
| Jogador 4 | 1-4 | 22:49:18 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Gromp18_AP | -0.3400 |  |
| Jogador 4 | 1-4 | 22:49:18 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Gromp18_AP | 0.2500 |  |
| Jogador 4 | 1-4 | 22:49:19 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Gromp18_AP | -0.4200 |  |
| Jogador 4 | 1-4 | 22:49:19 | MOVE Board -> Board: Grompe (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 1-4 | 22:49:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-1 | 22:49:22 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Krug18 | 0.3000 |  |
| Jogador 4 | 2-1 | 22:49:22 | MOVE Bench -> Board: Krugue (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Krug18 | 0.0800 |  |
| Jogador 4 | 2-1 | 22:49:23 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Krug18 | -0.0500 |  |
| Jogador 4 | 2-1 | 22:49:23 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Krug18 | 0.8900 |  |
| Jogador 4 | 2-1 | 22:49:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | 0.0300 |  |
| Jogador 4 | 2-1 | 22:49:24 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | -0.6800 |  |
| Jogador 4 | 2-1 | 22:49:24 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | 0.4200 |  |
| Jogador 4 | 2-1 | 22:49:25 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | 0.0900 |  |
| Jogador 4 | 2-1 | 22:49:25 | MOVE Bench -> Board: Elise (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | -0.0900 |  |
| Jogador 4 | 2-1 | 22:49:25 | MOVE Board -> Board: Elise (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | -0.0100 |  |
| Jogador 4 | 2-1 | 22:49:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 4 | 2-2 | 22:49:29 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Krug18 | -0.4300 |  |
| Jogador 4 | 2-2 | 22:49:30 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-2 | 22:49:30 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Krug18 | -0.1700 |  |
| Jogador 4 | 2-2 | 22:49:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Krug18 | 1.0400 |  |
| Jogador 4 | 2-2 | 22:49:30 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Krug18 | -0.4900 |  |
| Jogador 4 | 2-2 | 22:49:31 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Krug18 | 0.9500 |  |
| Jogador 4 | 2-2 | 22:49:31 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Krug18 | -0.4300 |  |
| Jogador 4 | 2-2 | 22:49:31 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Krug18 | 0.3000 |  |
| Jogador 4 | 2-2 | 22:49:31 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Krug18 | -0.3500 |  |
| Jogador 4 | 2-2 | 22:49:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | -0.0400 |  |
| Jogador 4 | 2-2 | 22:49:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 4 | 2-3 | 22:49:36 | COMPROU: Grompe (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_Krug18 | 1.0400 |  |
| Jogador 4 | 2-3 | 22:49:37 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Krug18 | -0.7500 |  |
| Jogador 4 | 2-3 | 22:49:37 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Aphelios | 0.2000 |  |
| Jogador 4 | 2-3 | 22:49:38 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Aphelios | -0.0900 |  |
| Jogador 4 | 2-3 | 22:49:38 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Aphelios | -0.0800 |  |
| Jogador 4 | 2-3 | 22:49:39 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Aphelios | 0.3300 |  |
| Jogador 4 | 2-3 | 22:49:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-3 | 22:49:39 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-3 | 22:49:39 | MOVE Board -> Board: Aphelios (i:8.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-3 | 22:49:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-4 | 22:49:43 | COMPROU: Krugue (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Lutador | DA_18_Aphelios | 1.0300 |  |
| Jogador 4 | 2-4 | 22:49:44 | MOVE Bench -> Board: Krugue (i:6.0) <-> Kobuko (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Lutador | DA_18_Aphelios | 0.1000 |  |
| Jogador 4 | 2-4 | 22:49:44 | VENDEU: Kobuko (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | Lutador | DA_18_Aphelios | -0.1400 |  |
| Jogador 4 | 2-4 | 22:49:44 | COMPROU: Diana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Lutador | DA_18_Aphelios | 0.2700 |  |
| Jogador 4 | 2-4 | 22:49:45 | MOVE Board -> Board: Krugue (i:6.0) <-> Grompe (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Fera do Rift | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-4 | 22:49:46 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Fera do Rift | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-4 | 22:49:46 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Fera do Rift | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-5 | 22:49:50 | MOVE Bench -> Board: Diana (i:6.0) <-> Grompe (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Fera do Rift | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 2-5 | 22:49:51 | VENDEU: Grompe (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Lunar | DA_18_Aphelios | -0.1900 |  |
| Jogador 4 | 2-5 | 22:49:51 | EQUIP_FROM_INVENTORY: TFT_Item_RunaansHurricane -> Krugue (i:6.0) (tabuleiro slot 10) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Lunar | DA_18_Aphelios | 0.1200 |  |
| Jogador 4 | 2-5 | 22:49:51 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Krugue (i:6.0) (tabuleiro slot 10) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Lunar | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 2-5 | 22:49:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Lunar | DA_18_Aphelios | 0.3100 |  |
| Jogador 4 | 2-5 | 22:49:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_Aphelios | 0.0100 |  |
| Jogador 4 | 2-5 | 22:49:53 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_Aphelios | 0.5500 |  |
| Jogador 4 | 2-5 | 22:49:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | 0.1300 |  |
| Jogador 4 | 2-5 | 22:49:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-6 | 22:49:58 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Lunar | DA_18_Aphelios | -0.0300 |  |
| Jogador 4 | 2-6 | 22:49:58 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Lunar | DA_18_Aphelios | -0.1000 |  |
| Jogador 4 | 2-6 | 22:49:58 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Lunar | DA_18_Aphelios | -0.7900 |  |
| Jogador 4 | 2-6 | 22:49:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-6 | 22:49:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-7 | 22:50:05 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lunar | DA_18_Aphelios | 0.1600 |  |
| Jogador 4 | 2-7 | 22:50:05 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lunar | DA_18_Aphelios | -0.1600 |  |
| Jogador 4 | 2-7 | 22:50:06 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Lunar | DA_18_Aphelios | 0.1800 |  |
| Jogador 4 | 2-7 | 22:50:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-7 | 22:50:06 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-1 | 22:50:13 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lunar | DA_18_Aphelios | 0.0400 |  |
| Jogador 4 | 3-1 | 22:50:13 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lunar | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-1 | 22:50:13 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lunar | DA_18_Aphelios | 0.0900 |  |
| Jogador 4 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Lunar | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-1 | 22:50:14 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-1 | 22:50:14 | MOVE Board -> Board: Aphelios (i:8.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-1 | 22:50:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-2 | 22:50:21 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Lunar | DA_18_Aphelios | -0.6300 |  |
| Jogador 4 | 3-2 | 22:50:21 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Lunar | DA_18_Aphelios | -0.1100 |  |
| Jogador 4 | 3-2 | 22:50:21 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Lunar | DA_18_Aphelios | 0.2100 |  |
| Jogador 4 | 3-2 | 22:50:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-2 | 22:50:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-3 | 22:50:30 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Lunar | DA_18_Aphelios | 0.5200 |  |
| Jogador 4 | 3-3 | 22:50:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-3 | 22:50:30 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-4 | 22:50:39 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lunar | DA_18_Aphelios | -0.0700 |  |
| Jogador 4 | 3-4 | 22:50:39 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_MasterYi_AD | 0.7600 |  |
| Jogador 4 | 3-4 | 22:50:39 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_MasterYi_AD | 0.2700 |  |
| Jogador 4 | 3-4 | 22:50:39 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 4 | 3-4 | 22:50:40 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_MasterYi_AD | 0.5500 |  |
| Jogador 4 | 3-4 | 22:50:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 4 | 3-4 | 22:50:40 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 22:50:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 22:50:48 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lunar | DA_18_MasterYi_AD | 0.7300 |  |
| Jogador 4 | 3-5 | 22:50:49 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.4900 |  |
| Jogador 4 | 3-5 | 22:50:49 | MOVE Board -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 22:50:49 | MOVE Board -> Board: Aphelios (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 22:50:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 22:50:56 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lunar | DA_18_MasterYi_AD | 0.2100 |  |
| Jogador 4 | 3-6 | 22:50:57 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lunar | DA_18_MasterYi_AD | 0.6400 |  |
| Jogador 4 | 3-6 | 22:50:57 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | -0.1100 |  |
| Jogador 4 | 3-6 | 22:50:57 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 22:50:57 | MOVE Board -> Board: Diana (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-6 | 22:50:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 22:51:05 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lunar | DA_18_MasterYi_AD | 0.7300 |  |
| Jogador 4 | 3-7 | 22:51:07 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 4 | 3-7 | 22:51:07 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_BFSword -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.2400 |  |
| Jogador 4 | 3-7 | 22:51:08 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.1600 |  |
| Jogador 4 | 3-7 | 22:51:08 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 22:51:08 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-1 | 22:51:14 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lunar | DA_18_MasterYi_AD | 0.0500 |  |
| Jogador 4 | 4-1 | 22:51:15 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 4 | 4-1 | 22:51:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 22:51:25 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lunar | DA_18_MasterYi_AD | 0.1600 |  |
| Jogador 4 | 4-2 | 22:51:25 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lunar | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 4 | 4-2 | 22:51:25 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | -0.0300 |  |
| Jogador 4 | 4-2 | 22:51:26 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 22:51:26 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 4 | 4-2 | 22:51:26 | MOVE Board -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-2 | 22:51:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-3 | 22:51:33 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lunar | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 4 | 4-3 | 22:51:34 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lunar | DA_18_MasterYi_AD | -0.3200 |  |
| Jogador 4 | 4-3 | 22:51:34 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Lunar | DA_18_MasterYi_AD | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 4 | 4-3 | 22:51:37 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Lunar | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 4 | 4-3 | 22:51:37 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lunar | DA_18_MasterYi_AD | 0.4400 |  |
| Jogador 4 | 4-3 | 22:51:37 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lunar | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 4 | 4-3 | 22:51:38 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lunar | DA_18_MasterYi_AD | -0.2900 |  |
| Jogador 4 | 4-3 | 22:51:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 22:51:45 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lunar | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 4 | 4-4 | 22:51:46 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Lunar | DA_18_MasterYi_AD | 0.0500 |  |
| Jogador 4 | 4-4 | 22:51:46 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lunar | DA_18_MasterYi_AD | 0.7300 |  |
| Jogador 4 | 4-4 | 22:51:46 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lunar | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 4 | 4-4 | 22:51:46 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lunar | DA_18_MasterYi_AD | -0.2800 |  |
| Jogador 4 | 4-4 | 22:51:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-5 | 22:51:55 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lunar | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 4 | 4-5 | 22:51:55 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lunar | DA_18_MasterYi_AD | -0.4100 |  |
| Jogador 4 | 4-5 | 22:51:55 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lunar | DA_18_MasterYi_AD | -0.2800 |  |
| Jogador 4 | 4-5 | 22:51:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lunar | DA_18_MasterYi_AD | -0.0300 |  |
| Jogador 4 | 4-6 | 22:52:07 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Lunar | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 4 | 4-6 | 22:52:07 | MOVE Bench -> Board: Krugue (i:6.0) <-> Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Lunar | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 4 | 4-6 | 22:52:07 | VENDEU: Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Lunar | DA_18_MasterYi_AD | -0.0800 |  |
| Jogador 4 | 4-6 | 22:52:07 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Lunar | DA_18_MasterYi_AD | 0.7500 |  |
| Jogador 4 | 4-6 | 22:52:08 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Lunar | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 4 | 4-6 | 22:52:08 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Lunar | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 4 | 4-6 | 22:52:08 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Lunar | DA_18_MasterYi_AD | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 4 | 4-6 | 22:52:08 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Lunar | DA_18_MasterYi_AD | -0.1300 |  |
| Jogador 4 | 4-6 | 22:52:08 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Lunar | DA_18_MasterYi_AD | 0.7600 |  |
| Jogador 4 | 4-6 | 22:52:11 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Lunar | DA_18_MasterYi_AD | -0.5200 |  |
| Jogador 4 | 4-6 | 22:52:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Lunar | DA_18_MasterYi_AD | -0.0300 |  |
| Jogador 4 | 4-7 | 22:52:17 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lunar | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 4-7 | 22:52:17 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_SparringGloves -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lunar | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 4 | 4-7 | 22:52:20 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lunar | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 4 | 4-7 | 22:52:20 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lunar | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 4 | 4-7 | 22:52:20 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lunar | DA_18_MasterYi_AD | -0.5300 |  |
| Jogador 4 | 4-7 | 22:52:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lunar | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 4 | 5-1 | 22:52:29 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 3 | Lunar | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 5-1 | 22:52:29 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Lunar | DA_18_MasterYi_AD | 0.1400 |  |
| Jogador 4 | 5-1 | 22:52:29 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 40 | 3 | Lunar | DA_18_MasterYi_AD | 0.9700 |  |
| Jogador 4 | 5-1 | 22:52:29 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 3 | Lunar | DA_18_MasterYi_AD | -0.1300 |  |
| Jogador 4 | 5-1 | 22:52:29 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 37 | 3 | Lunar | DA_18_MasterYi_AD | 0.5700 |  |
| Jogador 4 | 5-1 | 22:52:30 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 3 | Lunar | DA_18_MasterYi_AD | -0.2500 |  |
| Jogador 4 | 5-1 | 22:52:30 | REROLL | STABILIZE | STABILIZE: pressão de vida | 32 | 3 | Lunar | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-1 | 22:52:30 | MOVE Board -> Board: Master Yi (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 32 | 3 | Lunar | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 5-1 | 22:52:30 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 3 | Lunar | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 4 | 5-1 | 22:52:33 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 3 | Lunar | DA_18_MasterYi_AD | 0.9200 |  |
| Jogador 4 | 5-1 | 22:52:34 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 32 | 3 | Lunar | DA_18_MasterYi_AD | -0.2100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 5-2 | 22:52:38 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Lunar | DA_18_MasterYi_AD | 0.3200 |  |
| Jogador 4 | 5-2 | 22:52:38 | MOVE Bench -> Board: Diana (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Lunar | DA_18_MasterYi_AD | 0.6000 |  |
| Jogador 4 | 5-2 | 22:52:42 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 3 | Lunar | DA_18_MasterYi_AD | 0.1800 |  |
| Jogador 4 | 5-2 | 22:52:42 | REROLL | STABILIZE | STABILIZE: pressão de vida | 34 | 3 | Lunar | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-2 | 22:52:42 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 3 | Lunar | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 4 | 5-2 | 22:52:42 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 3 | Adaptador | DA_18_MasterYi_AD | 0.9200 |  |
| Jogador 4 | 5-2 | 22:52:42 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_MasterYi_AD | 0.3400 |  |
| Jogador 4 | 5-2 | 22:52:43 | MOVE Board -> Board: Diana (i:12.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 4 | 5-2 | 22:52:43 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 4 | 5-2 | 22:52:43 | MOVE Board -> Board: Master Yi (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 5-2 | 22:52:43 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 30 | 3 | Adaptador | DA_18_MasterYi_AD | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 5-3 | 22:52:50 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 39 | 3 | Adaptador | DA_18_MasterYi_AD | 0.4200 |  |
| Jogador 4 | 5-3 | 22:52:50 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 3 | Adaptador | DA_18_MasterYi_AD | 0.9000 |  |
| Jogador 4 | 5-3 | 22:52:50 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 3 | Adaptador | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 5-3 | 22:52:50 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 3 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 5-3 | 22:52:51 | REROLL | STABILIZE | STABILIZE: pressão de vida | 29 | 3 | Adaptador | DA_18_MasterYi_AD | -0.1700 |  |
| Jogador 4 | 5-3 | 22:52:51 | REROLL | STABILIZE | STABILIZE: pressão de vida | 27 | 3 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-3 | 22:52:51 | REROLL | STABILIZE | STABILIZE: pressão de vida | 25 | 3 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-3 | 22:52:51 | REROLL | STABILIZE | STABILIZE: pressão de vida | 23 | 3 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-3 | 22:52:51 | REROLL | STABILIZE | STABILIZE: pressão de vida | 21 | 3 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-3 | 22:52:55 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 3 | Adaptador | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 5-3 | 22:52:55 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 29 | 3 | Adaptador | DA_18_MasterYi_AD | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 5-4 | 22:52:59 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Adaptador | DA_18_MasterYi_AD | 0.3800 |  |
| Jogador 4 | 5-4 | 22:52:59 | REROLL | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-4 | 22:53:00 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Adaptador | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 4 | 5-4 | 22:53:00 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Adaptador | DA_18_MasterYi_AD | 0.3600 |  |
| Jogador 4 | 5-4 | 22:53:03 | REROLL | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-4 | 22:53:04 | REROLL | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Adaptador | DA_18_MasterYi_AD | -0.1700 |  |
| Jogador 4 | 5-4 | 22:53:04 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Adaptador | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 4 | 5-4 | 22:53:04 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Adaptador | DA_18_MasterYi_AD | 0.7600 |  |
| Jogador 4 | 5-4 | 22:53:04 | REROLL | STABILIZE | STABILIZE: pressão de vida | 25 | 2 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-4 | 22:53:04 | REROLL | STABILIZE | STABILIZE: pressão de vida | 23 | 2 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-4 | 22:53:05 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 23 | 2 | Adaptador | DA_18_MasterYi_AD | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 5-5 | 22:53:12 | VENDEU: Fiddlesticks (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 2 | Adaptador | DA_18_MasterYi_AD | -0.1500 |  |
| Jogador 4 | 5-5 | 22:53:12 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Grompe (i:4.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 2 | Adaptador | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 5-5 | 22:53:12 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Adaptador | DA_18_MasterYi_AD | 0.9000 |  |
| Jogador 4 | 5-5 | 22:53:13 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 5-5 | 22:53:13 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Adaptador | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 4 | 5-5 | 22:53:13 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Adaptador | DA_18_Diana | 0.9400 |  |
| Jogador 4 | 5-5 | 22:53:13 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Adaptador | DA_18_Diana | 0.9400 |  |
| Jogador 4 | 5-5 | 22:53:14 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 26 | 2 | Adaptador | DA_18_Diana | 0.0700 |  |
| Jogador 4 | 5-5 | 22:53:14 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 23 | 2 | Adaptador | DA_18_Diana | -0.2500 |  |
| Jogador 4 | 5-5 | 22:53:18 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 21 | 2 | Adaptador | DA_18_Diana | -0.0900 |  |
| Jogador 5 | ? | 22:48:49 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0200 |  |
| Jogador 5 | ? | 22:48:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 5 | ? | 22:48:50 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.6000 |  |
| Jogador 5 | ? | 22:48:50 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 5 | ? | 22:48:51 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.5600 |  |
| Jogador 5 | ? | 22:48:51 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 5 | ? | 22:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 5 | 1-1 | 22:48:56 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 1.0300 |  |
| Jogador 5 | 1-1 | 22:48:56 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 5 | 1-1 | 22:48:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.1300 |  |
| Jogador 5 | 1-1 | 22:48:57 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4500 |  |
| Jogador 5 | 1-1 | 22:48:57 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 5 | 1-1 | 22:48:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 5 | 1-2 | 22:49:02 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0800 |  |
| Jogador 5 | 1-2 | 22:49:02 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Ornn | -0.0800 |  |
| Jogador 5 | 1-2 | 22:49:03 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.1100 |  |
| Jogador 5 | 1-2 | 22:49:03 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 5 | 1-2 | 22:49:03 | MOVE Board -> Board: Ornn (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | -0.0100 |  |
| Jogador 5 | 1-2 | 22:49:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 5 | 1-3 | 22:49:09 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 5 | 1-3 | 22:49:09 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | -0.4100 |  |
| Jogador 5 | 1-3 | 22:49:09 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | -0.3600 |  |
| Jogador 5 | 1-3 | 22:49:10 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Murkwolf18 | 0.1200 |  |
| Jogador 5 | 1-3 | 22:49:10 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Sejuani | -0.3700 |  |
| Jogador 5 | 1-3 | 22:49:10 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Murkwolf18 | -0.4000 |  |
| Jogador 5 | 1-3 | 22:49:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 5 | 1-4 | 22:49:15 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Murkwolf18 | -0.0100 |  |
| Jogador 5 | 1-4 | 22:49:16 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.1400 |  |
| Jogador 5 | 1-4 | 22:49:16 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.4500 |  |
| Jogador 5 | 1-4 | 22:49:17 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.3300 |  |
| Jogador 5 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_SparringGloves -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.1800 |  |
| Jogador 5 | 1-4 | 22:49:18 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.1200 |  |
| Jogador 5 | 1-4 | 22:49:18 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 1-4 | 22:49:19 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 1-4 | 22:49:19 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 1-4 | 22:49:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 1-4 | 22:49:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 22:49:22 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-1 | 22:49:22 | MOVE Bench -> Board: Rammus (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 2-1 | 22:49:23 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rammus | -0.0800 |  |
| Jogador 5 | 2-1 | 22:49:23 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Rammus (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 2-1 | 22:49:24 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Rammus (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rammus | 0.1100 |  |
| Jogador 5 | 2-1 | 22:49:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 5 | 2-1 | 22:49:24 | MOVE Board -> Board: Rammus (i:6.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-1 | 22:49:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-2 | 22:49:29 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Rammus | -0.1700 |  |
| Jogador 5 | 2-2 | 22:49:30 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Rammus | 0.3400 |  |
| Jogador 5 | 2-2 | 22:49:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rammus | -0.0600 |  |
| Jogador 5 | 2-2 | 22:49:30 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rammus | -0.0600 |  |
| Jogador 5 | 2-2 | 22:49:30 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rammus | 0.2000 |  |
| Jogador 5 | 2-2 | 22:49:31 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rammus | -0.3300 |  |
| Jogador 5 | 2-2 | 22:49:31 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rammus | 0.2000 |  |
| Jogador 5 | 2-2 | 22:49:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | -0.0600 |  |
| Jogador 5 | 2-2 | 22:49:31 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | -0.3300 |  |
| Jogador 5 | 2-2 | 22:49:32 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 2-2 | 22:49:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 2-3 | 22:49:36 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rammus | 0.1600 |  |
| Jogador 5 | 2-3 | 22:49:37 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rammus | 0.0100 |  |
| Jogador 5 | 2-3 | 22:49:37 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | -0.0600 |  |
| Jogador 5 | 2-3 | 22:49:38 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rammus | 0.1900 |  |
| Jogador 5 | 2-3 | 22:49:38 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | -0.3100 |  |
| Jogador 5 | 2-3 | 22:49:39 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rammus | 0.1500 |  |
| Jogador 5 | 2-3 | 22:49:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | -0.0600 |  |
| Jogador 5 | 2-3 | 22:49:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 2-3 | 22:49:41 | MOVE Bench -> Board: Caitlyn (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | 0.4100 |  |
| Jogador 5 | 2-4 | 22:49:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Defendente | DA_18_Rammus | 1.0300 |  |
| Jogador 5 | 2-4 | 22:49:44 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Defendente | DA_18_Rammus | 0.0900 |  |
| Jogador 5 | 2-4 | 22:49:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Defendente | DA_18_Rammus | -0.4100 |  |
| Jogador 5 | 2-4 | 22:49:44 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Defendente | DA_18_Rammus | -0.4100 |  |
| Jogador 5 | 2-4 | 22:49:45 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 2-5 | 22:49:50 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | Defendente | DA_18_Rammus | 0.0900 |  |
| Jogador 5 | 2-5 | 22:49:51 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | Defendente | DA_18_Rammus | -0.4100 |  |
| Jogador 5 | 2-5 | 22:49:51 | MOVE Bench -> Board: Rammus (i:6.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 2-5 | 22:49:51 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 2-5 | 22:49:52 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Defendente | DA_18_Rammus | -0.7100 |  |
| Jogador 5 | 2-5 | 22:49:53 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | 0.4500 |  |
| Jogador 5 | 2-5 | 22:49:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | 0.0300 |  |
| Jogador 5 | 2-5 | 22:49:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Rammus | -0.0400 |  |
| Jogador 5 | 2-5 | 22:49:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 2-6 | 22:49:58 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 2-6 | 22:49:58 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | 0.7800 |  |
| Jogador 5 | 2-6 | 22:49:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.0400 |  |
| Jogador 5 | 2-6 | 22:49:58 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 2-6 | 22:49:59 | MOVE Board -> Board: Rammus (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 2-6 | 22:49:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 2-7 | 22:50:05 | VENDEU: Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | -0.3100 |  |
| Jogador 5 | 2-7 | 22:50:05 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Tristana | 0.1800 |  |
| Jogador 5 | 2-7 | 22:50:06 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_ChainVest -> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Tristana | 0.1400 |  |
| Jogador 5 | 2-7 | 22:50:06 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-7 | 22:50:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 2-7 | 22:50:06 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-7 | 22:50:07 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-1 | 22:50:13 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Defendente | DA_18_Rammus | -0.0700 |  |
| Jogador 5 | 3-1 | 22:50:13 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 3-1 | 22:50:13 | MOVE Bench -> Board: Shen (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 3-1 | 22:50:14 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 3-1 | 22:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-1 | 22:50:14 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.4000 |  |
| Jogador 5 | 3-1 | 22:50:15 | MOVE Board -> Board: Rammus (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-1 | 22:50:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-2 | 22:50:21 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_18_Rammus | -0.7100 |  |
| Jogador 5 | 3-2 | 22:50:21 | MOVE Bench -> Board: Shen (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_18_Rammus | -0.4100 |  |
| Jogador 5 | 3-2 | 22:50:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-3 | 22:50:30 | MOVE Bench -> Board: Rammus (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Defendente | DA_18_Rammus | 0.1000 |  |
| Jogador 5 | 3-3 | 22:50:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 3-3 | 22:50:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 3-3 | 22:50:30 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_18_Rammus | 0.4000 |  |
| Jogador 5 | 3-3 | 22:50:31 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Rammus | 0.0200 |  |
| Jogador 5 | 3-3 | 22:50:31 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-3 | 22:50:31 | MOVE Board -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-3 | 22:50:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-4 | 22:50:39 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-4 | 22:50:39 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-4 | 22:50:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-5 | 22:50:48 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Defendente | DA_18_Rammus | 0.7300 |  |
| Jogador 5 | 3-5 | 22:50:49 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 3-5 | 22:50:49 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-5 | 22:50:49 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-5 | 22:50:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-6 | 22:50:56 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Rammus | 0.0600 |  |
| Jogador 5 | 3-6 | 22:50:57 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Defendente | DA_18_Rammus | -0.3700 |  |
| Jogador 5 | 3-6 | 22:50:57 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | -0.1800 |  |
| Jogador 5 | 3-6 | 22:50:57 | MOVE Bench -> Board: Rengar (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | -0.4000 |  |
| Jogador 5 | 3-6 | 22:50:57 | MOVE Bench -> Board: Rammus (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 3-6 | 22:50:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-6 | 22:50:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-6 | 22:50:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-7 | 22:51:05 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | 0.7200 |  |
| Jogador 5 | 3-7 | 22:51:07 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_SparringGloves -> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 3-7 | 22:51:07 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | 0.1900 |  |
| Jogador 5 | 3-7 | 22:51:08 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-7 | 22:51:08 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-1 | 22:51:14 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Defendente | DA_18_Rammus | 0.7600 |  |
| Jogador 5 | 4-1 | 22:51:15 | EQUIP_FROM_INVENTORY: TFT_Item_Crownguard -> Rengar (i:6.0) (tabuleiro slot 4) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 4-1 | 22:51:15 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Defendente | DA_18_Rammus | 0.0900 |  |
| Jogador 5 | 4-1 | 22:51:15 | MOVE Bench -> Board: Rengar (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | 0.1500 |  |
| Jogador 5 | 4-1 | 22:51:15 | MOVE Bench -> Board: Rammus (i:12.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 4-1 | 22:51:15 | MOVE Board -> Board: Rammus (i:12.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-1 | 22:51:16 | MOVE Bench -> Board: Rengar (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | 0.0100 |  |
| Jogador 5 | 4-1 | 22:51:16 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 4-1 | 22:51:16 | MOVE Board -> Board: Rengar (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-1 | 22:51:18 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Rammus | 0.5800 |  |
| Jogador 5 | 4-1 | 22:51:19 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-2 | 22:51:25 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Rammus | 0.7300 |  |
| Jogador 5 | 4-2 | 22:51:25 | MOVE Board -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-2 | 22:51:25 | MOVE Board -> Board: Shen (i:4.0) <-> Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-2 | 22:51:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-3 | 22:51:33 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | 0.4700 |  |
| Jogador 5 | 4-3 | 22:51:34 | MOVE Board -> Board: Rammus (i:12.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-3 | 22:51:34 | MOVE Board -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-3 | 22:51:37 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-3 | 22:51:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-4 | 22:51:45 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Rammus | 0.2300 |  |
| Jogador 5 | 4-4 | 22:51:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 4-4 | 22:51:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-4 | 22:51:46 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-5 | 22:51:55 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Rammus | 0.7300 |  |
| Jogador 5 | 4-5 | 22:51:55 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Defendente | DA_18_Rammus | 0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 4-5 | 22:51:55 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | -0.2200 |  |
| Jogador 5 | 4-5 | 22:51:55 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.4000 |  |
| Jogador 5 | 4-5 | 22:51:58 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-6 | 22:52:07 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Defendente | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 4-6 | 22:52:07 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.4300 |  |
| Jogador 5 | 4-6 | 22:52:07 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-7 | 22:52:17 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Defendente | DA_18_Rammus | 0.7200 |  |
| Jogador 5 | 4-7 | 22:52:17 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Defendente | DA_18_Rammus | 0.3400 |  |
| Jogador 5 | 4-7 | 22:52:20 | COMPROU: Morgana (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | -0.0400 |  |
| Jogador 5 | 4-7 | 22:52:20 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Azuporã (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.1400 |  |
| Jogador 5 | 4-7 | 22:52:20 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Azuporã (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.0900 |  |
| Jogador 5 | 4-7 | 22:52:21 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Rammus (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-7 | 22:52:21 | MOVE Board -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-7 | 22:52:21 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-7 | 22:52:22 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.4000 |  |
| Jogador 5 | 5-1 | 22:52:29 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.7300 |  |
| Jogador 5 | 5-1 | 22:52:29 | MOVE Board -> Board: Shen (i:4.0) <-> Rammus (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-1 | 22:52:29 | MOVE Board -> Board: Rammus (i:12.0) <-> Lobo Trevoguari (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 5-1 | 22:52:29 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-2 | 22:52:38 | VENDEU: Sejuani (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 5-2 | 22:52:38 | COMPROU: Shen (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Defendente | DA_18_Rammus | 0.7400 |  |
| Jogador 5 | 5-2 | 22:52:42 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Rengar (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-2 | 22:52:42 | MOVE Board -> Board: Rengar (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 5-2 | 22:52:42 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-3 | 22:52:50 | VENDEU: Caitlyn (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 0 | Defendente | DA_18_Rammus | -0.1200 |  |
| Jogador 5 | 5-3 | 22:52:50 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 13 | 0 | Defendente | DA_18_Rammus | 0.1300 |  |
| Jogador 5 | 5-3 | 22:52:50 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 11 | 0 | Defendente | DA_18_Rammus | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-3 | 22:52:50 | VENDEU: Diana (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 14 | 0 | Defendente | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 5-3 | 22:52:51 | COMPROU: Ashe (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Defendente | DA_18_Rammus | -0.1600 |  |
| Jogador 5 | 5-3 | 22:52:51 | VENDEU: Rengar (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Defendente | DA_18_Rammus | -0.0400 |  |
| Jogador 5 | 5-3 | 22:52:51 | COMPROU: Sivir (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Defendente | DA_18_Rammus | -0.1100 |  |
| Jogador 5 | 5-3 | 22:52:51 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Defendente | DA_18_Rammus | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-3 | 22:52:51 | VENDEU: Kha'Zix (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 14 | 0 | Defendente | DA_18_Rammus | 0.0100 |  |
| Jogador 5 | 5-3 | 22:52:55 | COMPROU: Shen (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Defendente | DA_18_Rammus | 0.7700 |  |
| Jogador 5 | 5-3 | 22:52:55 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-4 | 22:52:59 | COMPROU: Tristana (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 1 | Defendente | DA_18_Rammus | 0.1700 |  |
| Jogador 5 | 5-4 | 22:52:59 | MOVE Bench -> Board: Morgana (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 16 | 1 | Defendente | DA_18_Rammus | 0.4000 |  |
| Jogador 5 | 5-4 | 22:53:00 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 12 | 1 | Defendente | DA_18_Rammus | -0.2200 |  |
| Jogador 5 | 5-4 | 22:53:00 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 10 | 1 | Defendente | DA_18_Rammus | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-4 | 22:53:03 | VENDEU: Nidalee (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 14 | 1 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 5-4 | 22:53:04 | COMPROU: Rammus (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 11 | 1 | Defendente | DA_18_Rammus | 0.7600 |  |
| Jogador 5 | 5-4 | 22:53:04 | COMPROU: Dragão Ancião (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 1 | Defendente | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 5-4 | 22:53:04 | MOVE Board -> Board: Morgana (i:8.0) <-> Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 1 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-4 | 22:53:04 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 6 | 1 | Defendente | DA_18_Rammus | 0.5700 |  |
| Jogador 5 | 5-4 | 22:53:04 | COMPROU: Karma (Custo 1 \| i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 1 | Defendente | DA_18_Rammus | 0.2000 |  |
| Jogador 5 | 5-4 | 22:53:05 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 5 | 1 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-5 | 22:53:12 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-5 | 22:53:12 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Defendente | DA_18_Rammus | 0.0500 |  |
| Jogador 5 | 5-5 | 22:53:12 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Defendente | DA_18_Rammus | 0.1900 |  |
| Jogador 5 | 5-5 | 22:53:13 | MOVE Board -> Board: Azuporã (i:8.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-5 | 22:53:13 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Defendente | DA_18_Rammus | -0.0700 |  |
| Jogador 5 | 5-5 | 22:53:13 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Defendente | DA_18_Rammus | 0.1400 |  |
| Jogador 5 | 5-5 | 22:53:13 | REROLL | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Defendente | DA_18_Rammus | -0.1700 |  |
| Jogador 5 | 5-5 | 22:53:14 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Defendente | DA_18_Rammus | 0.1400 |  |
| Jogador 5 | 5-5 | 22:53:14 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Defendente | DA_18_Rammus | 0.2900 |  |
| Jogador 5 | 5-5 | 22:53:18 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 5-6 | 22:53:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Defendente | DA_18_Rammus | 0.7600 |  |
| Jogador 5 | 5-6 | 22:53:22 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Morgana (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-6 | 22:53:22 | MOVE Board -> Board: Morgana (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 5-6 | 22:53:22 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Defendente | DA_18_Rammus | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-7 | 22:53:31 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Rengar (i:6.0) (tabuleiro slot 10) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Defendente | DA_18_Rammus | 0.0900 |  |
| Jogador 5 | 5-7 | 22:53:31 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 1 | Defendente | DA_18_Rammus | -0.2100 |  |
| Jogador 5 | 5-7 | 22:53:32 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 1 | Defendente | DA_18_Rammus | 0.3800 |  |
| Jogador 5 | 5-7 | 22:53:32 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 1 | Defendente | DA_18_Rammus | -0.2700 |  |
| Jogador 5 | 5-7 | 22:53:35 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 1 | Defendente | DA_18_Rammus | 0.1400 |  |
| Jogador 5 | 5-7 | 22:53:36 | REROLL | STABILIZE | STABILIZE: pressão de vida | 26 | 1 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 5-7 | 22:53:36 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 1 | Defendente | DA_18_Rammus | 0.0500 |  |
| Jogador 5 | 5-7 | 22:53:36 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Defendente | DA_18_Rammus | 0.8200 |  |
| Jogador 5 | 5-7 | 22:53:36 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 1 | Defendente | DA_18_Rammus | -0.0700 |  |
| Jogador 5 | 5-7 | 22:53:36 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Defendente | DA_18_Lillia | 0.8900 |  |
| Jogador 5 | 5-7 | 22:53:37 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Defendente | DA_18_Lillia | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 6-1 | 22:53:41 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Defendente | DA_18_Lillia | 0.8200 |  |
| Jogador 5 | 6-1 | 22:53:41 | COMPROU: Morgana (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 2 | Defendente | DA_18_Lillia | 0.7400 |  |
| Jogador 5 | 6-1 | 22:53:41 | REROLL | STABILIZE | STABILIZE: pressão de vida | 21 | 2 | Defendente | DA_18_Lillia | -0.0900 |  |
| Jogador 5 | 6-1 | 22:53:41 | VENDEU: Lillia (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Defendente | DA_18_Rammus | -0.0500 |  |
| Jogador 5 | 6-1 | 22:53:42 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Defendente | DA_18_Rammus | 0.8700 |  |
| Jogador 5 | 6-1 | 22:53:42 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Defendente | DA_18_Rammus | 0.8500 |  |
| Jogador 5 | 6-1 | 22:53:42 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 6-1 | 22:53:42 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Defendente | DA_18_Rammus | 0.5800 |  |
| Jogador 5 | 6-1 | 22:53:43 | COMPROU: Alune (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 2 | Defendente | DA_18_Rammus | 0.0300 |  |
| Jogador 5 | 6-1 | 22:53:43 | REROLL | STABILIZE | STABILIZE: pressão de vida | 20 | 2 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-2 | 22:53:51 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Defendente | DA_18_Rammus | -0.1200 |  |
| Jogador 5 | 6-2 | 22:53:51 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Defendente | DA_18_Rammus | 0.9500 |  |
| Jogador 5 | 6-2 | 22:53:51 | COMPROU: Lux (Feérica) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Defendente | DA_18_Rammus | -0.1500 |  |
| Jogador 5 | 6-2 | 22:53:51 | MOVE Bench -> Board: Alune (i:10.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Defendente | DA_18_Rammus | 0.4900 |  |
| Jogador 5 | 6-2 | 22:53:52 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 2 | Defendente | DA_18_Rammus | -0.0800 |  |
| Jogador 5 | 6-2 | 22:53:52 | REROLL | STABILIZE | STABILIZE: pressão de vida | 23 | 2 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-2 | 22:53:52 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 6-2 | 22:53:52 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 2 | Defendente | DA_18_Rammus | 0.3100 |  |
| Jogador 5 | 6-2 | 22:53:53 | REROLL | STABILIZE | STABILIZE: pressão de vida | 21 | 2 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-2 | 22:53:56 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Defendente | DA_18_Rammus | -0.3100 |  |
| Jogador 5 | 6-2 | 22:53:57 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Defendente | DA_18_Rammus | -0.1700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 6-3 | 22:54:01 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Defendente | DA_18_Rammus | 0.3900 |  |
| Jogador 5 | 6-3 | 22:54:01 | VENDEU: Ashe (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 2 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 6-3 | 22:54:01 | COMPROU: Morgana (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Defendente | DA_18_Morgana | 0.9400 |  |
| Jogador 5 | 6-3 | 22:54:02 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Defendente | DA_18_Morgana | -0.2200 |  |
| Jogador 5 | 6-3 | 22:54:02 | MOVE Board -> Board: Alune (i:10.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Defendente | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 6-3 | 22:54:02 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Defendente | DA_18_Morgana | 0.5400 |  |
| Jogador 5 | 6-3 | 22:54:02 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Defendente | DA_18_Morgana | 0.0100 |  |
| Jogador 5 | 6-3 | 22:54:06 | REROLL | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Defendente | DA_18_Morgana | -0.0900 |  |
| Jogador 5 | 6-3 | 22:54:06 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Defendente | DA_18_Morgana | 0.0700 |  |
| Jogador 5 | 6-3 | 22:54:07 | COMPROU: Lux (Feérica) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 24 | 2 | Defendente | DA_18_Morgana | 0.7000 |  |
| Jogador 5 | 6-4 | 22:54:11 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Defendente | DA_18_Morgana | 0.0800 |  |
| Jogador 5 | 6-4 | 22:54:11 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Defendente | DA_18_Morgana | 0.1600 |  |
| Jogador 5 | 6-4 | 22:54:11 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Defendente | DA_18_Morgana | 0.0600 |  |
| Jogador 5 | 6-4 | 22:54:12 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Defendente | DA_18_Morgana | 0.5500 |  |
| Jogador 5 | 6-4 | 22:54:12 | MOVE Board -> Board: Lillia (i:8.0) <-> Alune (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Defendente | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 6-4 | 22:54:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Defendente | DA_18_Morgana | -0.0900 |  |
| Jogador 5 | 6-4 | 22:54:17 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Defendente | DA_18_Morgana | -0.1200 |  |
| Jogador 5 | 6-5 | 22:54:21 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Defendente | DA_18_Morgana | -0.1900 |  |
| Jogador 5 | 6-5 | 22:54:22 | VENDEU: Morgana (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 49 | 3 | Defendente | DA_18_Rammus | 0.0200 |  |
| Jogador 5 | 6-5 | 22:54:22 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Defendente | DA_18_Rammus | 0.2400 |  |
| Jogador 5 | 6-5 | 22:54:22 | REROLL | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-5 | 22:54:23 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Defendente | DA_18_Rammus | 0.0500 |  |
| Jogador 5 | 6-5 | 22:54:23 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Defendente | DA_18_Rammus | 0.7900 |  |
| Jogador 5 | 6-5 | 22:54:23 | REROLL | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-5 | 22:54:23 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Defendente | DA_18_Rammus | -0.2400 |  |
| Jogador 5 | 6-6 | 22:54:34 | COMPROU: Lux (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Defendente | DA_18_Rammus | -0.1200 |  |
| Jogador 5 | 6-6 | 22:54:34 | MOVE Board -> Board: Alune (i:10.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 6-6 | 22:54:34 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 6-6 | 22:54:35 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Defendente | DA_18_Rammus | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 6-7 | 22:54:44 | EQUIP_FROM_INVENTORY: DA_18_EmblemSlayer -> Rengar (i:6.0) (tabuleiro slot 10) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Defendente | DA_18_Rammus | -0.0300 |  |
| Jogador 5 | 6-7 | 22:54:45 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Defendente | DA_18_Rammus | -0.0500 |  |
| Jogador 5 | 6-7 | 22:54:45 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 5 | Defendente | DA_18_Rammus | 0.9300 |  |
| Jogador 5 | 6-7 | 22:54:45 | MOVE Bench -> Board: Lux (Feérica) (i:10.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 5 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 6-7 | 22:54:45 | REROLL | STABILIZE | STABILIZE: pressão de vida | 56 | 5 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-7 | 22:54:46 | VENDEU: Lux (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 6-7 | 22:54:46 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 5 | Defendente | DA_18_Rammus | 0.1200 |  |
| Jogador 5 | 6-7 | 22:54:46 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Defendente | DA_18_Rammus | 0.0600 |  |
| Jogador 5 | 6-7 | 22:54:46 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 5 | Defendente | DA_18_Rammus | 0.1600 |  |
| Jogador 6 | ? | 22:48:49 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | 0.0000 |  |
| Jogador 6 | ? | 22:48:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 6 | ? | 22:48:50 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.6000 |  |
| Jogador 6 | ? | 22:48:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 6 | ? | 22:48:51 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 6 | ? | 22:48:51 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | ? | 22:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 1-1 | 22:48:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 6 | 1-1 | 22:48:56 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1300 |  |
| Jogador 6 | 1-1 | 22:48:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 6 | 1-1 | 22:48:57 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1700 |  |
| Jogador 6 | 1-1 | 22:48:57 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 6 | 1-1 | 22:48:58 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.4300 |  |
| Jogador 6 | 1-1 | 22:48:58 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1900 |  |
| Jogador 6 | 1-1 | 22:48:58 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.4000 |  |
| Jogador 6 | 1-1 | 22:48:58 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-1 | 22:48:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-2 | 22:49:02 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Teemo | 0.0700 |  |
| Jogador 6 | 1-2 | 22:49:02 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | -0.0800 |  |
| Jogador 6 | 1-2 | 22:49:03 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Caitlyn | 0.0700 |  |
| Jogador 6 | 1-2 | 22:49:03 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | -0.0800 |  |
| Jogador 6 | 1-2 | 22:49:03 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 6 | 1-2 | 22:49:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-2 | 22:49:07 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.4200 |  |
| Jogador 6 | 1-3 | 22:49:09 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | 0.0900 |  |
| Jogador 6 | 1-3 | 22:49:09 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | -0.7500 |  |
| Jogador 6 | 1-3 | 22:49:09 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | -0.0500 |  |
| Jogador 6 | 1-3 | 22:49:10 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | 0.2200 |  |
| Jogador 6 | 1-3 | 22:49:10 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 1-3 | 22:49:10 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | 0.2200 |  |
| Jogador 6 | 1-3 | 22:49:11 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 1-3 | 22:49:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.0400 |  |
| Jogador 6 | 1-3 | 22:49:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 6 | 1-4 | 22:49:15 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Murkwolf18 | 0.3300 |  |
| Jogador 6 | 1-4 | 22:49:16 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Murkwolf18 | 0.5400 |  |
| Jogador 6 | 1-4 | 22:49:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | 0.3800 |  |
| Jogador 6 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_BFSword -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | 0.1000 |  |
| Jogador 6 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | 0.1300 |  |
| Jogador 6 | 1-4 | 22:49:18 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 6 | 1-4 | 22:49:18 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 6 | 1-4 | 22:49:19 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.3800 |  |
| Jogador 6 | 1-4 | 22:49:19 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 6 | 1-4 | 22:49:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 6 | 2-1 | 22:49:22 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 6 | 2-1 | 22:49:22 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.3200 |  |
| Jogador 6 | 2-1 | 22:49:23 | MOVE Bench -> Board: Tristana (i:6.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.3200 |  |
| Jogador 6 | 2-1 | 22:49:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0300 |  |
| Jogador 6 | 2-1 | 22:49:24 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.4500 |  |
| Jogador 6 | 2-1 | 22:49:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 22:49:29 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Tristana | 1.0400 |  |
| Jogador 6 | 2-2 | 22:49:30 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Tristana | 0.0500 |  |
| Jogador 6 | 2-2 | 22:49:30 | VENDEU: Lobo Trevoguari (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_18_Tristana | -0.1300 |  |
| Jogador 6 | 2-2 | 22:49:30 | COMPROU: Hecarim (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-2 | 22:49:30 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Tristana | -0.4000 |  |
| Jogador 6 | 2-2 | 22:49:31 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Tristana | -0.4100 |  |
| Jogador 6 | 2-2 | 22:49:31 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 22:49:36 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Tristana | -0.6000 |  |
| Jogador 6 | 2-3 | 22:49:37 | EQUIP_FROM_INVENTORY: TFT_Item_SpearOfShojin -> Hecarim (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Tristana | 0.0700 |  |
| Jogador 6 | 2-3 | 22:49:37 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Hecarim (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Tristana | 0.0900 |  |
| Jogador 6 | 2-3 | 22:49:38 | COMPROU: Hecarim (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Tristana | 0.9500 |  |
| Jogador 6 | 2-3 | 22:49:38 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Tristana | -0.4000 |  |
| Jogador 6 | 2-3 | 22:49:39 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Tristana | 0.0600 |  |
| Jogador 6 | 2-3 | 22:49:39 | MOVE Board -> Board: Hecarim (i:6.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 22:49:39 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 2-3 | 22:49:39 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-4 | 22:49:43 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 0 | Sabugueiro | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-4 | 22:49:44 | COMPROU: Varus (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | Sabugueiro | DA_18_Tristana | 0.2800 |  |
| Jogador 6 | 2-4 | 22:49:44 | VENDEU: Varus (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 0 | Sabugueiro | DA_18_Tristana | -0.1000 |  |
| Jogador 6 | 2-4 | 22:49:44 | COMPROU: Kayle (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 11 | 0 | Sabugueiro | DA_18_Tristana | 0.0400 |  |
| Jogador 6 | 2-4 | 22:49:45 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | Sabugueiro | DA_18_Tristana | -0.1600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-4 | 22:49:46 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Sabugueiro | DA_18_Tristana | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-4 | 22:49:46 | VENDEU: Kayle (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Sabugueiro | DA_18_Tristana | -0.0900 |  |
| Jogador 6 | 2-4 | 22:49:46 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Sabugueiro | DA_18_Tristana | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-4 | 22:49:46 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Sabugueiro | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-5 | 22:49:50 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | Sabugueiro | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-5 | 22:49:51 | MOVE Bench -> Board: Rammus (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_18_Tristana | 0.0500 |  |
| Jogador 6 | 2-5 | 22:49:51 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_18_Tristana | 0.3900 |  |
| Jogador 6 | 2-5 | 22:49:51 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_Tristana | 0.2000 |  |
| Jogador 6 | 2-5 | 22:49:52 | MOVE Board -> Board: Rammus (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-5 | 22:49:53 | MOVE Board -> Board: Hecarim (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-5 | 22:49:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-6 | 22:49:58 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Sabugueiro | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 2-6 | 22:49:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Sabugueiro | DA_18_Tristana | 0.1200 |  |
| Jogador 6 | 2-6 | 22:49:58 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Sabugueiro | DA_18_Tristana | -0.3300 |  |
| Jogador 6 | 2-6 | 22:49:58 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Sabugueiro | DA_18_Tristana | 0.0400 |  |
| Jogador 6 | 2-6 | 22:49:59 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Sabugueiro | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-6 | 22:49:59 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-6 | 22:50:00 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-6 | 22:50:00 | MOVE Bench -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 2-6 | 22:50:01 | MOVE Board -> Board: Vi (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-6 | 22:50:01 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_Tristana | -0.4100 |  |
| Jogador 6 | 2-6 | 22:50:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-7 | 22:50:05 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Sabugueiro | DA_18_Tristana | 0.1000 |  |
| Jogador 6 | 2-7 | 22:50:05 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Sabugueiro | DA_18_Tristana | -0.6500 |  |
| Jogador 6 | 2-7 | 22:50:06 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Sabugueiro | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-7 | 22:50:06 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Sabugueiro | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 2-7 | 22:50:06 | MOVE Bench -> Board: Alistar (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Sabugueiro | DA_18_Tristana | -0.3900 |  |
| Jogador 6 | 2-7 | 22:50:06 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Sabugueiro | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-7 | 22:50:07 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_BFSword -> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Sabugueiro | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-7 | 22:50:08 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Sabugueiro | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-7 | 22:50:08 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Sabugueiro | DA_18_Hecarim | -0.1300 |  |
| Jogador 6 | 2-7 | 22:50:09 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_18_Ahri | -0.2800 |  |
| Jogador 6 | 2-7 | 22:50:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_18_Ahri | 0.0000 |  |
| Jogador 6 | 3-1 | 22:50:13 | VENDEU: Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Sabugueiro | DA_18_Hecarim | 0.0200 |  |
| Jogador 6 | 3-1 | 22:50:13 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Sabugueiro | DA_18_Rammus | 0.5500 |  |
| Jogador 6 | 3-1 | 22:50:13 | MOVE Bench -> Board: Rammus (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Sabugueiro | DA_18_Rammus | -0.7500 |  |
| Jogador 6 | 3-1 | 22:50:14 | MOVE Bench -> Board: Alistar (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Sabugueiro | DA_18_Rammus | -0.4100 |  |
| Jogador 6 | 3-1 | 22:50:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Sabugueiro | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 3-2 | 22:50:21 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Sabugueiro | DA_18_Rammus | 0.1000 |  |
| Jogador 6 | 3-2 | 22:50:21 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Sabugueiro | DA_18_Rammus | -0.4100 |  |
| Jogador 6 | 3-2 | 22:50:21 | MOVE Bench -> Board: Rammus (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Sabugueiro | DA_18_Rammus | -0.6500 |  |
| Jogador 6 | 3-2 | 22:50:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Sabugueiro | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 3-3 | 22:50:30 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_18_Hecarim | 0.1000 |  |
| Jogador 6 | 3-3 | 22:50:30 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_18_Hecarim | -0.4100 |  |
| Jogador 6 | 3-3 | 22:50:30 | MOVE Bench -> Board: Rammus (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_18_Hecarim | -0.7600 |  |
| Jogador 6 | 3-3 | 22:50:30 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_18_Hecarim | -0.0600 |  |
| Jogador 6 | 3-4 | 22:50:39 | MOVE Bench -> Board: Alistar (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Sabugueiro | DA_18_Hecarim | 0.0800 |  |
| Jogador 6 | 3-4 | 22:50:39 | MOVE Bench -> Board: Rammus (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Sabugueiro | DA_18_Rammus | -0.6500 |  |
| Jogador 6 | 3-4 | 22:50:39 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Sabugueiro | DA_18_Rammus | 0.0500 |  |
| Jogador 6 | 3-4 | 22:50:39 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Sabugueiro | DA_18_Rammus | -0.0700 |  |
| Jogador 6 | 3-4 | 22:50:40 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Sabugueiro | DA_18_Rammus | 0.1700 |  |
| Jogador 6 | 3-4 | 22:50:40 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Sabugueiro | DA_18_Rammus | -0.0700 |  |
| Jogador 6 | 3-4 | 22:50:40 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Sabugueiro | DA_CrimsonRaptor18 | -0.0600 |  |
| Jogador 6 | 3-4 | 22:50:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Sabugueiro | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 6 | 3-4 | 22:50:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 2 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 3-4 | 22:50:43 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Sabugueiro | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 6 | 3-4 | 22:50:43 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Sabugueiro | DA_CrimsonRaptor18 | -0.0600 |  |
| Jogador 6 | 3-5 | 22:50:48 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_CrimsonRaptor18 | 0.4100 |  |
| Jogador 6 | 3-5 | 22:50:49 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Sabugueiro | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 6 | 3-5 | 22:50:49 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Sabugueiro | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 6 | 3-5 | 22:50:49 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 1 | Sabugueiro | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 6 | 3-5 | 22:50:50 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 1 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 3-5 | 22:50:50 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 1 | Sabugueiro | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 6 | 3-5 | 22:50:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 1 | Sabugueiro | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 6 | 3-6 | 22:50:56 | COMPROU: Gnar (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_18_GnarSmall | 0.2100 |  |
| Jogador 6 | 3-6 | 22:50:57 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0900 |  |
| Jogador 6 | 3-6 | 22:50:57 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-6 | 22:50:57 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-6 | 22:50:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 22:51:05 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_18_GnarSmall | 0.7600 |  |
| Jogador 6 | 3-7 | 22:51:07 | MOVE Bench -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_18_GnarSmall | -0.4000 |  |
| Jogador 6 | 3-7 | 22:51:07 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_18_GnarSmall | 0.3300 |  |
| Jogador 6 | 3-7 | 22:51:08 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_18_GnarSmall | 0.3900 |  |
| Jogador 6 | 3-7 | 22:51:08 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | 0.2100 |  |
| Jogador 6 | 3-7 | 22:51:08 | MOVE Board -> Board: Hecarim (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-7 | 22:51:09 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 22:51:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-1 | 22:51:14 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0900 |  |
| Jogador 6 | 4-1 | 22:51:15 | MOVE Bench -> Board: Soraka (i:8.0) <-> Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-1 | 22:51:15 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_GnarSmall | 0.2100 |  |
| Jogador 6 | 4-1 | 22:51:15 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_GnarSmall | 0.1300 |  |
| Jogador 6 | 4-1 | 22:51:15 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0800 |  |
| Jogador 6 | 4-1 | 22:51:15 | MOVE Board -> Board: Soraka (i:8.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-1 | 22:51:16 | MOVE Board -> Board: Hecarim (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-1 | 22:51:16 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 22:51:25 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_18_GnarSmall | 0.7300 |  |
| Jogador 6 | 4-2 | 22:51:25 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 22:51:25 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 22:51:26 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 22:51:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-3 | 22:51:33 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Sabugueiro | DA_18_GnarSmall | 0.2900 |  |
| Jogador 6 | 4-3 | 22:51:34 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-3 | 22:51:34 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0400 |  |
| Jogador 6 | 4-3 | 22:51:37 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Sabugueiro | DA_18_GnarSmall | -0.2600 |  |
| Jogador 6 | 4-3 | 22:51:37 | REROLL | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-3 | 22:51:37 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0800 |  |
| Jogador 6 | 4-3 | 22:51:38 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Sabugueiro | DA_18_GnarSmall | 0.7700 |  |
| Jogador 6 | 4-3 | 22:51:38 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-3 | 22:51:38 | MOVE Board -> Board: Soraka (i:8.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 22:51:39 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 22:51:45 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-4 | 22:51:46 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Sabugueiro | DA_18_GnarSmall | 0.8300 |  |
| Jogador 6 | 4-4 | 22:51:46 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0500 |  |
| Jogador 6 | 4-4 | 22:51:46 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Sabugueiro | DA_18_GnarSmall | -0.1400 |  |
| Jogador 6 | 4-4 | 22:51:46 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Sabugueiro | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-4 | 22:51:47 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Sabugueiro | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-4 | 22:51:47 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Sabugueiro | DA_18_GnarSmall | 0.8300 |  |
| Jogador 6 | 4-4 | 22:51:47 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Sabugueiro | DA_18_Hecarim | 0.4100 |  |
| Jogador 6 | 4-4 | 22:51:47 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Sabugueiro | DA_18_Hecarim | 0.7500 |  |
| Jogador 6 | 4-4 | 22:51:50 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Sabugueiro | DA_18_Hecarim | -0.0900 |  |
| Jogador 6 | 4-4 | 22:51:51 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Sabugueiro | DA_18_Hecarim | 0.0000 |  |
| Jogador 6 | 4-5 | 22:51:55 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Sabugueiro | DA_18_Hecarim | -0.1500 |  |
| Jogador 6 | 4-5 | 22:51:55 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.8300 |  |
| Jogador 6 | 4-5 | 22:51:55 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 6 | 4-5 | 22:51:55 | MOVE Bench -> Board: Mamãe Bicuda (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.3500 |  |
| Jogador 6 | 4-5 | 22:51:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.8100 |  |
| Jogador 6 | 4-5 | 22:51:59 | MOVE Board -> Board: Hecarim (i:12.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 6 | 4-5 | 22:51:59 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 4-5 | 22:51:59 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 6 | 4-5 | 22:51:59 | MOVE Board -> Board: Soraka (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 6 | 4-5 | 22:51:59 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 6 | 4-5 | 22:52:00 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.4000 |  |
| Jogador 6 | 4-6 | 22:52:07 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.0300 |  |
| Jogador 6 | 4-6 | 22:52:07 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 4-6 | 22:52:07 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 6 | 4-6 | 22:52:07 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.8300 |  |
| Jogador 6 | 4-6 | 22:52:08 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.7500 |  |
| Jogador 6 | 4-6 | 22:52:08 | MOVE Board -> Board: Mamãe Bicuda (i:12.0) <-> Hecarim (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 6 | 4-6 | 22:52:08 | MOVE Board -> Board: Hecarim (i:12.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 6 | 4-6 | 22:52:08 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 6 | 4-6 | 22:52:08 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 6 | 4-6 | 22:52:12 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.6000 |  |
| Jogador 6 | 4-7 | 22:52:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.7900 |  |
| Jogador 6 | 4-7 | 22:52:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 6 | 4-7 | 22:52:20 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_TearOfTheGoddess -> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.1300 |  |
| Jogador 6 | 4-7 | 22:52:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 4-7 | 22:52:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 4-7 | 22:52:21 | MOVE Board -> Board: Soraka (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 6 | 4-7 | 22:52:21 | MOVE Board -> Board: Diana (i:6.0) <-> Hecarim (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 6 | 4-7 | 22:52:21 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 6 | 5-1 | 22:52:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 5-1 | 22:52:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 5-1 | 22:52:29 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.1500 |  |
| Jogador 6 | 5-1 | 22:52:29 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 6 | 5-1 | 22:52:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 5-1 | 22:52:30 | VENDEU: Alistar (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.1600 |  |
| Jogador 6 | 5-1 | 22:52:30 | COMPROU: Gnar (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.7900 |  |
| Jogador 6 | 5-1 | 22:52:30 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 5-1 | 22:52:30 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 6 | 5-1 | 22:52:33 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Sabugueiro | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 6 | 5-1 | 22:52:34 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Sabugueiro | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 7 | ? | 22:48:49 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 7 | ? | 22:48:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 7 | ? | 22:48:50 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 7 | ? | 22:48:50 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 7 | ? | 22:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-1 | 22:48:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0800 |  |
| Jogador 7 | 1-1 | 22:48:56 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 7 | 1-1 | 22:48:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 1.0300 |  |
| Jogador 7 | 1-1 | 22:48:57 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-1 | 22:48:57 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.7200 |  |
| Jogador 7 | 1-1 | 22:48:58 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 7 | 1-1 | 22:48:58 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4100 |  |
| Jogador 7 | 1-1 | 22:48:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-2 | 22:49:02 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.2500 |  |
| Jogador 7 | 1-2 | 22:49:02 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 7 | 1-2 | 22:49:03 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 7 | 1-2 | 22:49:03 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.2400 |  |
| Jogador 7 | 1-2 | 22:49:03 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 1-2 | 22:49:04 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 7 | 1-2 | 22:49:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 1-3 | 22:49:09 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | -0.3000 |  |
| Jogador 7 | 1-3 | 22:49:09 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 7 | 1-3 | 22:49:09 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.2300 |  |
| Jogador 7 | 1-3 | 22:49:10 | MOVE Bench -> Board: Elise (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 7 | 1-3 | 22:49:10 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 7 | 1-3 | 22:49:10 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 7 | 1-3 | 22:49:11 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | -0.3300 |  |
| Jogador 7 | 1-3 | 22:49:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 1-4 | 22:49:15 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 7 | 1-4 | 22:49:16 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 0.4300 |  |
| Jogador 7 | 1-4 | 22:49:16 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.1600 |  |
| Jogador 7 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_SparringGloves -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 7 | 1-4 | 22:49:17 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.1300 |  |
| Jogador 7 | 1-4 | 22:49:18 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 1-4 | 22:49:18 | MOVE Bench -> Board: Alistar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | -0.4600 |  |
| Jogador 7 | 1-4 | 22:49:19 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.0500 |  |
| Jogador 7 | 1-4 | 22:49:19 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.2100 |  |
| Jogador 7 | 1-4 | 22:49:19 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 1-4 | 22:49:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 2-1 | 22:49:22 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 0.2600 |  |
| Jogador 7 | 2-1 | 22:49:22 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 2-1 | 22:49:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.0400 |  |
| Jogador 7 | 2-1 | 22:49:23 | MOVE Board -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-1 | 22:49:24 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 2-1 | 22:49:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Hecarim | 0.3400 |  |
| Jogador 7 | 2-1 | 22:49:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Hecarim | 0.0400 |  |
| Jogador 7 | 2-1 | 22:49:25 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Hecarim | -0.0600 |  |
| Jogador 7 | 2-1 | 22:49:25 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Hecarim | 0.2000 |  |
| Jogador 7 | 2-1 | 22:49:25 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Hecarim | -0.3300 |  |
| Jogador 7 | 2-1 | 22:49:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-2 | 22:49:29 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_18_Hecarim | 1.0300 |  |
| Jogador 7 | 2-2 | 22:49:30 | MOVE Bench -> Board: Shen (i:4.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 22:49:30 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_18_Hecarim | 0.3900 |  |
| Jogador 7 | 2-2 | 22:49:30 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Hecarim | 0.1300 |  |
| Jogador 7 | 2-2 | 22:49:30 | VENDEU: Cassiopeia (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_18_Hecarim | -0.1000 |  |
| Jogador 7 | 2-2 | 22:49:31 | COMPROU: Alistar (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 22:49:31 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Hecarim | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-2 | 22:49:31 | MOVE Board -> Board: Shen (i:4.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-2 | 22:49:31 | MOVE Board -> Board: Elise (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 2-2 | 22:49:32 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-3 | 22:49:36 | VENDEU: Alistar (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | — | DA_18_Hecarim | -0.0300 |  |
| Jogador 7 | 2-3 | 22:49:37 | COMPROU: Azuporã (Custo 4 \| i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 2-3 | 22:49:37 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 2-3 | 22:49:38 | VENDEU: Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 2-3 | 22:49:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 2-3 | 22:49:39 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | — | DA_Sentinel18 | -0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 2-3 | 22:49:39 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 22:49:43 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Vanguarda | DA_Sentinel18 | -0.3700 |  |
| Jogador 7 | 2-4 | 22:49:44 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Vanguarda | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 2-4 | 22:49:44 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Vanguarda | DA_Sentinel18 | -0.1400 |  |
| Jogador 7 | 2-4 | 22:49:44 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vanguarda | DA_Sentinel18 | 0.3700 |  |
| Jogador 7 | 2-4 | 22:49:45 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Vanguarda | DA_Sentinel18 | -0.1500 |  |
| Jogador 7 | 2-4 | 22:49:46 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vanguarda | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 22:49:46 | MOVE Bench -> Board: Rengar (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vanguarda | DA_Sentinel18 | -0.4000 |  |
| Jogador 7 | 2-4 | 22:49:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vanguarda | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 22:49:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 22:49:50 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_Sentinel18 | 0.9700 |  |
| Jogador 7 | 2-5 | 22:49:51 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_Sentinel18 | 0.6000 |  |
| Jogador 7 | 2-5 | 22:49:51 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vanguarda | DA_Sentinel18 | -0.3800 |  |
| Jogador 7 | 2-5 | 22:49:51 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_Sentinel18 | 1.0000 |  |
| Jogador 7 | 2-5 | 22:49:52 | MOVE Bench -> Board: Shen (i:8.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Shen | 0.1000 |  |
| Jogador 7 | 2-5 | 22:49:53 | MOVE Bench -> Board: Rengar (i:6.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Shen | -0.6600 |  |
| Jogador 7 | 2-5 | 22:49:53 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 2-5 | 22:49:53 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 2-5 | 22:49:54 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-5 | 22:49:54 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Vanguarda | DA_Sentinel18 | 0.3200 |  |
| Jogador 7 | 2-5 | 22:49:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-6 | 22:49:58 | MOVE Bench -> Board: Elise (i:4.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Shen | -0.7000 |  |
| Jogador 7 | 2-6 | 22:49:58 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 2-6 | 22:49:58 | MOVE Bench -> Board: Rengar (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | -0.4100 |  |
| Jogador 7 | 2-6 | 22:49:58 | MOVE Bench -> Board: Elise (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | -0.7700 |  |
| Jogador 7 | 2-6 | 22:49:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-6 | 22:50:03 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | 0.5700 |  |
| Jogador 7 | 2-7 | 22:50:05 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Vanguarda | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 2-7 | 22:50:05 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Vanguarda | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 2-7 | 22:50:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 2-7 | 22:50:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 22:50:06 | MOVE Board -> Board: Elise (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 22:50:06 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 22:50:07 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-1 | 22:50:13 | MOVE Bench -> Board: Diana (i:6.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 3-1 | 22:50:13 | MOVE Bench -> Board: Rengar (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | -0.4100 |  |
| Jogador 7 | 3-1 | 22:50:13 | MOVE Bench -> Board: Elise (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | -0.7500 |  |
| Jogador 7 | 3-1 | 22:50:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-2 | 22:50:21 | MOVE Bench -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Vanguarda | DA_Sentinel18 | -0.3500 |  |
| Jogador 7 | 3-2 | 22:50:21 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Vanguarda | DA_Sentinel18 | -0.3400 |  |
| Jogador 7 | 3-2 | 22:50:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Vanguarda | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 3-3 | 22:50:30 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Vanguarda | DA_Sentinel18 | -0.1600 |  |
| Jogador 7 | 3-3 | 22:50:30 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Vanguarda | DA_Sentinel18 | 0.7700 |  |
| Jogador 7 | 3-3 | 22:50:30 | MOVE Bench -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Vanguarda | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 3-3 | 22:50:30 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Vanguarda | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 3-3 | 22:50:31 | MOVE Bench -> Board: Rengar (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Vanguarda | DA_Sentinel18 | -0.4100 |  |
| Jogador 7 | 3-3 | 22:50:31 | MOVE Bench -> Board: Diana (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Vanguarda | DA_Sentinel18 | -0.4100 |  |
| Jogador 7 | 3-3 | 22:50:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Vanguarda | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 3-4 | 22:50:39 | MOVE Bench -> Board: Diana (i:6.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Vanguarda | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 3-4 | 22:50:39 | MOVE Bench -> Board: Rengar (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Vanguarda | DA_Sentinel18 | -0.6600 |  |
| Jogador 7 | 3-4 | 22:50:39 | VENDEU: Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Vanguarda | DA_Sentinel18 | -0.1100 |  |
| Jogador 7 | 3-4 | 22:50:39 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Azuporã (i:8.0) (tabuleiro slot 10) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Vanguarda | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 3-4 | 22:50:40 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Azuporã (i:8.0) (tabuleiro slot 10) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Vanguarda | DA_Sentinel18 | 0.1400 |  |
| Jogador 7 | 3-4 | 22:50:40 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Vanguarda | DA_18_Diana | 0.8200 |  |
| Jogador 7 | 3-4 | 22:50:40 | MOVE Bench -> Board: Diana (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Vanguarda | DA_18_Diana | 0.3400 |  |
| Jogador 7 | 3-4 | 22:50:40 | MOVE Board -> Board: Diana (i:12.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 3-4 | 22:50:41 | MOVE Board -> Board: Rengar (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 3-4 | 22:50:43 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Vanguarda | DA_18_Diana | -0.1200 |  |
| Jogador 7 | 3-5 | 22:50:48 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Vanguarda | DA_18_Diana | -0.0700 |  |
| Jogador 7 | 3-5 | 22:50:49 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Vanguarda | DA_18_Diana | 0.4000 |  |
| Jogador 7 | 3-5 | 22:50:49 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Vanguarda | DA_18_Diana | 0.6800 |  |
| Jogador 7 | 3-5 | 22:50:49 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 3 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 3-5 | 22:50:50 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 3 | Vanguarda | DA_18_Diana | -0.0800 |  |
| Jogador 7 | 3-5 | 22:50:50 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 3 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 3-5 | 22:50:50 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 3 | Vanguarda | DA_18_Diana | 0.1100 |  |
| Jogador 7 | 3-5 | 22:50:50 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 3 | Vanguarda | DA_18_Diana | -0.5300 |  |
| Jogador 7 | 3-5 | 22:50:50 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 3 | Vanguarda | DA_18_Diana | -0.3400 |  |
| Jogador 7 | 3-5 | 22:50:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 3 | Vanguarda | DA_18_Diana | -0.0600 |  |
| Jogador 7 | 3-5 | 22:50:53 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 3 | Vanguarda | DA_18_Diana | 0.4200 |  |
| Jogador 7 | 3-6 | 22:50:56 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Vanguarda | DA_18_Diana | 0.7100 |  |
| Jogador 7 | 3-6 | 22:50:57 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Vanguarda | DA_18_Diana | 0.1000 |  |
| Jogador 7 | 3-6 | 22:50:57 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Vanguarda | DA_18_Diana | 0.3100 |  |
| Jogador 7 | 3-6 | 22:50:57 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 2 | Vanguarda | DA_18_Diana | -0.0900 |  |
| Jogador 7 | 3-6 | 22:50:57 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 3-6 | 22:50:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 2 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 3-6 | 22:50:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 2 | Vanguarda | DA_18_Diana | -0.0900 |  |
| Jogador 7 | 3-6 | 22:50:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 2 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 3-6 | 22:50:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 2 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 3-7 | 22:51:05 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vanguarda | DA_18_Diana | 0.1700 |  |
| Jogador 7 | 3-7 | 22:51:07 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vanguarda | DA_18_Diana | 0.1700 |  |
| Jogador 7 | 3-7 | 22:51:07 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Diana | -0.0900 |  |
| Jogador 7 | 3-7 | 22:51:08 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 3-7 | 22:51:08 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 4-1 | 22:51:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_18_Diana | -0.0900 |  |
| Jogador 7 | 4-1 | 22:51:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 4-1 | 22:51:15 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 4-1 | 22:51:15 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Diana | -0.1700 |  |
| Jogador 7 | 4-1 | 22:51:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 4-1 | 22:51:15 | VENDEU: Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Diana | -0.3100 |  |
| Jogador 7 | 4-1 | 22:51:16 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Vanguarda | DA_18_Diana | 0.0900 |  |
| Jogador 7 | 4-1 | 22:51:16 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 7 | 4-1 | 22:51:16 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 4-2 | 22:51:25 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Vanguarda | DA_18_Diana | 0.0400 |  |
| Jogador 7 | 4-2 | 22:51:25 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_18_Diana | -0.2400 |  |
| Jogador 7 | 4-2 | 22:51:25 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_18_Diana | 0.0900 |  |
| Jogador 7 | 4-2 | 22:51:26 | MOVE Bench -> Board: Soraka (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_18_Diana | 0.4000 |  |
| Jogador 7 | 4-2 | 22:51:26 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_18_Diana | 0.0600 |  |
| Jogador 7 | 4-2 | 22:51:26 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 4-3 | 22:51:33 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Vanguarda | DA_18_Diana | 0.1800 |  |
| Jogador 7 | 4-3 | 22:51:34 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_18_Diana | 0.1700 |  |
| Jogador 7 | 4-3 | 22:51:34 | COMPROU: Elise (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_18_Diana | 0.2600 |  |
| Jogador 7 | 4-3 | 22:51:37 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 4-4 | 22:51:45 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Vanguarda | DA_18_Diana | 0.7800 |  |
| Jogador 7 | 4-4 | 22:51:46 | COMPROU: Lillia (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Vanguarda | DA_18_Diana | -0.2400 |  |
| Jogador 7 | 4-4 | 22:51:46 | COMPROU: Teemo (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Vanguarda | DA_18_Diana | 0.0200 |  |
| Jogador 7 | 4-4 | 22:51:46 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 4-5 | 22:51:55 | COMPROU: Hecarim (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Vanguarda | DA_18_Diana | 0.7800 |  |
| Jogador 7 | 4-5 | 22:51:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Vanguarda | DA_18_Diana | 0.2700 |  |
| Jogador 7 | 4-5 | 22:51:55 | VENDEU: Teemo (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Vanguarda | DA_18_Diana | 0.0600 |  |
| Jogador 7 | 4-5 | 22:51:55 | COMPROU: Malphite (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_18_Diana | -0.1500 |  |
| Jogador 7 | 4-5 | 22:51:58 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_18_Diana | -0.1600 |  |
| Jogador 7 | 4-5 | 22:51:59 | VENDEU: Aronguejo (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_18_Diana | 0.0600 |  |
| Jogador 7 | 4-5 | 22:51:59 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Vanguarda | DA_18_Diana | -0.0700 |  |
| Jogador 7 | 4-5 | 22:51:59 | VENDEU: Kha'Zix (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_18_Diana | 0.0700 |  |
| Jogador 7 | 4-5 | 22:51:59 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Vanguarda | DA_18_Diana | -0.2800 |  |
| Jogador 7 | 4-5 | 22:51:59 | VENDEU: Cassiopeia (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_18_Diana | 0.0800 |  |
| Jogador 7 | 4-5 | 22:52:00 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 4-6 | 22:52:07 | COMPROU: Elise (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Vanguarda | DA_18_Diana | 0.7800 |  |
| Jogador 7 | 4-6 | 22:52:07 | VENDEU: Malphite (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Vanguarda | DA_18_Diana | 0.0700 |  |
| Jogador 7 | 4-6 | 22:52:07 | COMPROU: Ashe (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Vanguarda | DA_18_Diana | -0.3500 |  |
| Jogador 7 | 4-6 | 22:52:07 | VENDEU: Lillia (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 0 | Vanguarda | DA_18_Diana | 0.1600 |  |
| Jogador 7 | 4-6 | 22:52:08 | COMPROU: Rengar (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Vanguarda | DA_18_Diana | 0.3600 |  |
| Jogador 7 | 4-6 | 22:52:08 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Vanguarda | DA_18_Diana | -0.2400 |  |
| Jogador 7 | 4-6 | 22:52:08 | VENDEU: Rengar (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Vanguarda | DA_18_Diana | -0.0300 |  |
| Jogador 7 | 4-6 | 22:52:08 | COMPROU: Hecarim (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Vanguarda | DA_18_Diana | 0.7300 |  |
| Jogador 7 | 4-6 | 22:52:08 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Vanguarda | DA_18_Diana | 0.6700 |  |
| Jogador 7 | 4-6 | 22:52:11 | MOVE Bench -> Board: Ashe (i:10.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Vanguarda | DA_18_Diana | 0.4000 |  |
| Jogador 7 | 4-6 | 22:52:12 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 7 | 4-7 | 22:52:17 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Vanguarda | DA_18_Diana | -0.1400 |  |
| Jogador 7 | 4-7 | 22:52:17 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Vanguarda | DA_18_Diana | 0.0600 |  |
| Jogador 7 | 4-7 | 22:52:20 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_TearOfTheGoddess -> Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Vanguarda | DA_18_Diana | 0.0800 |  |
| Jogador 7 | 4-7 | 22:52:20 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Vanguarda | DA_18_Diana | -0.1600 |  |
| Jogador 7 | 4-7 | 22:52:20 | VENDEU: Kha'Zix (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Vanguarda | DA_18_Diana | 0.1500 |  |
| Jogador 7 | 4-7 | 22:52:21 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Vanguarda | DA_18_Diana | 0.7300 |  |
| Jogador 7 | 4-7 | 22:52:21 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_Brambleback18 | 0.7800 |  |
| Jogador 7 | 4-7 | 22:52:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_Brambleback18 | 0.0900 |  |
| Jogador 7 | 4-7 | 22:52:22 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_Brambleback18 | 0.0000 |  |
| Jogador 7 | 4-7 | 22:52:22 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_Brambleback18 | 0.5600 |  |
| Jogador 7 | 5-1 | 22:52:29 | COMPROU: Malphite (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Vanguarda | DA_Brambleback18 | -0.1900 |  |
| Jogador 7 | 5-1 | 22:52:29 | COMPROU: Krugue (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Vanguarda | DA_Brambleback18 | 0.1000 |  |
| Jogador 7 | 5-1 | 22:52:29 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Vanguarda | DA_Brambleback18 | -0.1600 |  |
| Jogador 7 | 5-1 | 22:52:29 | VENDEU: Krugue (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Vanguarda | DA_Brambleback18 | 0.0600 |  |
| Jogador 7 | 5-1 | 22:52:29 | COMPROU: Morgana (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Vanguarda | DA_Brambleback18 | 0.1200 |  |
| Jogador 7 | 5-1 | 22:52:30 | VENDEU: Aronguejo (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Vanguarda | DA_Brambleback18 | 0.0600 |  |
| Jogador 7 | 5-1 | 22:52:30 | COMPROU: Kayle (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Vanguarda | DA_Brambleback18 | -0.0400 |  |
| Jogador 7 | 5-1 | 22:52:30 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Vanguarda | DA_Brambleback18 | 0.0000 |  |
| Jogador 7 | 5-2 | 22:52:38 | VENDEU: Kayle (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Vanguarda | DA_Brambleback18 | 0.1500 |  |
| Jogador 7 | 5-2 | 22:52:38 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Vanguarda | DA_Brambleback18 | 0.7000 |  |
| Jogador 7 | 5-2 | 22:52:42 | VENDEU: Kog'Maw (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 0 | Vanguarda | DA_Brambleback18 | -0.0900 |  |
| Jogador 7 | 5-2 | 22:52:42 | COMPROU: Ahri (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Vanguarda | DA_Brambleback18 | -0.2100 |  |
| Jogador 7 | 5-2 | 22:52:42 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Vanguarda | DA_Brambleback18 | -0.1600 |  |
| Jogador 7 | 5-2 | 22:52:42 | VENDEU: Ahri (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Vanguarda | DA_Brambleback18 | 0.0800 |  |
| Jogador 7 | 5-2 | 22:52:42 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Vanguarda | DA_Brambleback18 | 0.6500 |  |
| Jogador 7 | 5-2 | 22:52:43 | VENDEU: Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 0 | Vanguarda | DA_Brambleback18 | -0.1600 |  |
| Jogador 7 | 5-2 | 22:52:43 | COMPROU: Ezreal (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Vanguarda | DA_Brambleback18 | -0.0400 |  |
| Jogador 7 | 5-2 | 22:52:43 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Vanguarda | DA_Brambleback18 | -0.1600 |  |
| Jogador 7 | 5-2 | 22:52:43 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Vanguarda | DA_Brambleback18 | 0.0000 |  |
| Jogador 7 | 5-3 | 22:52:50 | VENDEU: Malphite (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 26 | 1 | Vanguarda | DA_Brambleback18 | 0.0700 |  |
| Jogador 7 | 5-3 | 22:52:50 | COMPROU: Azuporã (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Vanguarda | DA_Sentinel18 | 0.8600 |  |
| Jogador 7 | 5-3 | 22:52:50 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Soraka (i:8.0) (tabuleiro slot 24) | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Vanguarda | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 5-3 | 22:52:50 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rengar (i:6.0) (tabuleiro slot 2) | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Vanguarda | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 5-3 | 22:52:51 | MOVE Bench -> Board: Soraka (i:8.0) <-> Ashe (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Vanguarda | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 5-3 | 22:52:51 | MOVE Bench -> Board: Ashe (i:10.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Vanguarda | DA_Sentinel18 | 0.1900 |  |
| Jogador 7 | 5-3 | 22:52:51 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 19 | 1 | Vanguarda | DA_Sentinel18 | 0.7800 |  |
| Jogador 7 | 5-3 | 22:52:51 | COMPROU: Master Yi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 1 | Vanguarda | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-3 | 22:52:51 | MOVE Bench -> Board: Mamãe Bicuda (i:12.0) <-> Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 1 | Vanguarda | DA_Sentinel18 | 0.1100 |  |
| Jogador 7 | 5-3 | 22:52:55 | MOVE Bench -> Board: Soraka (i:8.0) <-> Ashe (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 1 | Vanguarda | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 5-3 | 22:52:55 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 1 | Vanguarda | DA_Sentinel18 | -0.1200 |  |
| Jogador 7 | 5-4 | 22:52:59 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Vanguarda | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 5-4 | 22:52:59 | MOVE Bench -> Board: Ashe (i:10.0) <-> Mamãe Bicuda (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Vanguarda | DA_Sentinel18 | -0.8300 |  |
| Jogador 7 | 5-4 | 22:53:00 | MOVE Bench -> Board: Mamãe Bicuda (i:12.0) <-> Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Vanguarda | DA_Sentinel18 | -0.1200 |  |
| Jogador 7 | 5-4 | 22:53:00 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Vanguarda | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-4 | 22:53:04 | MOVE Bench -> Board: Azuporã (i:16.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Vanguarda | DA_Sentinel18 | 0.8300 |  |
| Jogador 7 | 5-5 | 22:53:12 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 2 | Vanguarda | DA_Sentinel18 | 0.2700 |  |
| Jogador 7 | 5-5 | 22:53:12 | MOVE Board -> Board: Ashe (i:10.0) <-> Diana (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 2 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-5 | 22:53:12 | MOVE Board -> Board: Diana (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 2 | Vanguarda | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 5-5 | 22:53:13 | VENDEU: Master Yi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 2 | Vanguarda | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 5-5 | 22:53:13 | COMPROU: Cascalho (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 31 | 2 | Vanguarda | DA_Sentinel18 | 0.3100 |  |
| Jogador 7 | 5-5 | 22:53:13 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 2 | Vanguarda | DA_Sentinel18 | -0.2400 |  |
| Jogador 7 | 5-5 | 22:53:13 | VENDEU: Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 33 | 2 | Vanguarda | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 5-5 | 22:53:14 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 30 | 2 | Vanguarda | DA_Sentinel18 | 0.8700 |  |
| Jogador 7 | 5-5 | 22:53:14 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 28 | 2 | Vanguarda | DA_Sentinel18 | -0.2400 |  |
| Jogador 7 | 5-5 | 22:53:18 | VENDEU: Rakan (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 2 | Vanguarda | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 5-6 | 22:53:22 | COMPROU: Ezreal (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 37 | 3 | Vanguarda | DA_Sentinel18 | -0.1400 |  |
| Jogador 7 | 5-6 | 22:53:22 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 3 | Vanguarda | DA_Sentinel18 | -0.1600 |  |
| Jogador 7 | 5-6 | 22:53:22 | VENDEU: Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 39 | 3 | Vanguarda | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 5-6 | 22:53:22 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 36 | 3 | Vanguarda | DA_Sentinel18 | 0.3500 |  |
| Jogador 7 | 5-6 | 22:53:22 | VENDEU: Morgana (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 40 | 3 | Vanguarda | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 5-6 | 22:53:23 | COMPROU: Morgana (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 36 | 3 | Vanguarda | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-6 | 22:53:23 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 34 | 3 | Vanguarda | DA_Sentinel18 | -0.1600 |  |
| Jogador 7 | 5-6 | 22:53:23 | VENDEU: Morgana (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 38 | 3 | Vanguarda | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 5-6 | 22:53:27 | COMPROU: Ezreal (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 34 | 3 | Vanguarda | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 5-6 | 22:53:27 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 3 | Vanguarda | DA_Sentinel18 | -0.1600 |  |
| Jogador 7 | 5-6 | 22:53:27 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 3 | Vanguarda | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 5-7 | 22:53:31 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Rengar (i:6.0) (tabuleiro slot 2) | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 3 | Vanguarda | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 5-7 | 22:53:31 | VENDEU: Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 47 | 3 | Vanguarda | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 5-7 | 22:53:32 | COMPROU: Morgana (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 3 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-7 | 22:53:32 | VENDEU: Morgana (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 47 | 3 | Vanguarda | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 5-7 | 22:53:35 | COMPROU: Azir (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 44 | 3 | Vanguarda | DA_Sentinel18 | 0.1700 |  |
| Jogador 7 | 5-7 | 22:53:36 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 42 | 3 | Vanguarda | DA_Sentinel18 | -0.1600 |  |
| Jogador 7 | 5-7 | 22:53:36 | VENDEU: Azir (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Vanguarda | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 5-7 | 22:53:36 | COMPROU: Morgana (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-7 | 22:53:36 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 39 | 3 | Vanguarda | DA_Sentinel18 | -0.2400 |  |
| Jogador 7 | 5-7 | 22:53:36 | VENDEU: Morgana (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 3 | Vanguarda | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 5-7 | 22:53:37 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 3 | Vanguarda | DA_Sentinel18 | -0.2200 |  |
| Jogador 7 | 6-1 | 22:53:41 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 51 | 4 | Vanguarda | DA_Sentinel18 | 0.9800 |  |
| Jogador 7 | 6-1 | 22:53:41 | COMPROU: Sivir (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 47 | 4 | Vanguarda | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 6-1 | 22:53:41 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 4 | Vanguarda | DA_Sentinel18 | -0.1600 |  |
| Jogador 7 | 6-1 | 22:53:41 | VENDEU: Soraka (i:16.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 56 | 4 | Vanguarda | DA_Sentinel18 | 0.1300 |  |
| Jogador 7 | 6-1 | 22:53:42 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Rengar (i:6.0) (tabuleiro slot 2) | WINSTREAK | WINSTREAK: preservar vantagem atual | 56 | 4 | Vanguarda | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 6-1 | 22:53:42 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Diana (i:12.0) (tabuleiro slot 9) | WINSTREAK | WINSTREAK: preservar vantagem atual | 56 | 4 | Vanguarda | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 6-1 | 22:53:42 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Diana (i:12.0) (tabuleiro slot 9) | WINSTREAK | WINSTREAK: preservar vantagem atual | 56 | 4 | Vanguarda | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 6-1 | 22:53:42 | COMPROU: Aphelios (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 52 | 4 | Vanguarda | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 6-1 | 22:53:43 | VENDEU: Sivir (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 56 | 4 | Vanguarda | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 6-1 | 22:53:43 | COMPROU: Hecarim (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 53 | 4 | Vanguarda | DA_Sentinel18 | 0.4100 |  |
| Jogador 7 | 6-2 | 22:53:51 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 63 | 5 | Vanguarda | DA_Sentinel18 | 0.4400 |  |
| Jogador 7 | 6-2 | 22:53:51 | COMPROU: Sett (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 59 | 5 | Vanguarda | DA_Sentinel18 | -0.2400 |  |
| Jogador 7 | 6-2 | 22:53:51 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 57 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-2 | 22:53:51 | VENDEU: Sett (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 61 | 5 | Vanguarda | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 6-2 | 22:53:52 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 57 | 5 | Vanguarda | DA_Sentinel18 | 1.0500 |  |
| Jogador 7 | 6-2 | 22:53:52 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 53 | 5 | Vanguarda | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 6-2 | 22:53:52 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 51 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-2 | 22:53:52 | VENDEU: Cascalho (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 52 | 5 | Vanguarda | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 6-2 | 22:53:53 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 48 | 5 | Vanguarda | DA_Sentinel18 | 0.4200 |  |
| Jogador 7 | 6-2 | 22:53:56 | VENDEU: Ahri (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 52 | 5 | Vanguarda | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 6-2 | 22:53:57 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 52 | 5 | Vanguarda | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 6-3 | 22:54:01 | COMPROU: Ivern (Custo 5 \| i:10.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 58 | 5 | Vanguarda | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-3 | 22:54:01 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 56 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-3 | 22:54:01 | MOVE Bench -> Board: Aphelios (i:16.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 56 | 5 | Vanguarda | DA_Sentinel18 | 0.5600 |  |
| Jogador 7 | 6-3 | 22:54:02 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 52 | 5 | Vanguarda | DA_Sentinel18 | 0.4100 |  |
| Jogador 7 | 6-3 | 22:54:02 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 50 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-3 | 22:54:02 | VENDEU: Ivern (i:10.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 55 | 5 | Vanguarda | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 6-3 | 22:54:02 | COMPROU: Sivir (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 51 | 5 | Vanguarda | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 6-3 | 22:54:06 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 49 | 5 | Vanguarda | DA_Sentinel18 | -0.1700 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 6-3 | 22:54:06 | VENDEU: Sivir (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 53 | 5 | Vanguarda | DA_Sentinel18 | 0.1400 |  |
| Jogador 7 | 6-3 | 22:54:07 | COMPROU: Lux (Inferno) (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 48 | 5 | Vanguarda | DA_Sentinel18 | -0.2300 |  |
| Jogador 7 | 6-4 | 22:54:11 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 56 | 4 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-4 | 22:54:11 | VENDEU: Lux (Inferno) (i:10.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 61 | 4 | Vanguarda | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 6-4 | 22:54:11 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 58 | 4 | Vanguarda | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 6-4 | 22:54:12 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 56 | 4 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-4 | 22:54:12 | VENDEU: Rubrivira (i:16.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 67 | 4 | Vanguarda | DA_Sentinel18 | -0.1400 |  |
| Jogador 7 | 6-4 | 22:54:12 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 63 | 4 | Vanguarda | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 6-4 | 22:54:17 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 61 | 4 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-5 | 22:54:21 | VENDEU: Diana (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 75 | 5 | Vanguarda | DA_Sentinel18 | -0.1900 |  |
| Jogador 7 | 6-5 | 22:54:22 | COMPROU: Elise (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 73 | 5 | Vanguarda | DA_Sentinel18 | 1.0500 |  |
| Jogador 7 | 6-5 | 22:54:22 | COMPROU: Malphite (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 69 | 5 | Vanguarda | DA_Sentinel18 | -0.1800 |  |
| Jogador 7 | 6-5 | 22:54:22 | MOVE Board -> Board: Aphelios (i:16.0) <-> Diana (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 69 | 5 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-5 | 22:54:23 | MOVE Board -> Board: Diana (i:12.0) <-> Ashe (i:10.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 69 | 5 | Vanguarda | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-5 | 22:54:23 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 69 | 5 | Vanguarda | DA_Sentinel18 | -0.1200 |  |
| Jogador 7 | 6-6 | 22:54:34 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 77 | 5 | Vanguarda | DA_Sentinel18 | 0.4900 |  |
| Jogador 7 | 6-6 | 22:54:34 | VENDEU: Elise (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 82 | 5 | Vanguarda | DA_Sentinel18 | -0.1600 |  |
| Jogador 7 | 6-6 | 22:54:34 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 79 | 5 | Vanguarda | DA_Sentinel18 | 1.0100 |  |
| Jogador 7 | 6-6 | 22:54:35 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 77 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-6 | 22:54:35 | VENDEU: Malphite (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 81 | 5 | Vanguarda | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 6-6 | 22:54:35 | COMPROU: Morgana (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 77 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-6 | 22:54:35 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 75 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-6 | 22:54:36 | VENDEU: Morgana (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 79 | 5 | Vanguarda | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 6-6 | 22:54:36 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Vanguarda | DA_Sentinel18 | 0.3700 |  |
| Jogador 7 | 6-7 | 22:54:44 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Hecarim (i:6.0) (tabuleiro slot 24) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 86 | 5 | Vanguarda | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 6-7 | 22:54:45 | VENDEU: Diana (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 89 | 5 | Vanguarda | DA_Sentinel18 | -0.3900 |  |
| Jogador 7 | 6-7 | 22:54:45 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 86 | 5 | Vanguarda | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 6-7 | 22:54:45 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-7 | 22:54:45 | VENDEU: Diana (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 87 | 5 | Vanguarda | DA_Sentinel18 | -0.2100 |  |
| Jogador 7 | 6-7 | 22:54:46 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 83 | 5 | Vanguarda | DA_Sentinel18 | 0.9700 |  |
| Jogador 7 | 6-7 | 22:54:46 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 81 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-7 | 22:54:46 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 79 | 5 | Vanguarda | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 6-7 | 22:54:46 | VENDEU: Kog'Maw (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 82 | 5 | Vanguarda | DA_Sentinel18 | -0.2800 |  |
| Jogador 8 | ? | 22:48:49 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 8 | ? | 22:48:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 8 | ? | 22:48:50 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.6000 |  |
| Jogador 8 | ? | 22:48:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.3000 |  |
| Jogador 8 | ? | 22:48:51 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.5900 |  |
| Jogador 8 | ? | 22:48:51 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | -0.0100 |  |
| Jogador 8 | ? | 22:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.0000 |  |
| Jogador 8 | 1-1 | 22:48:56 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 8 | 1-1 | 22:48:56 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_RekSai | -0.1300 |  |
| Jogador 8 | 1-1 | 22:48:56 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_RekSai | 0.0800 |  |
| Jogador 8 | 1-1 | 22:48:57 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_RekSai | 0.1700 |  |
| Jogador 8 | 1-1 | 22:48:57 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Leona | 1.0200 |  |
| Jogador 8 | 1-1 | 22:48:58 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Leona | 0.5200 |  |
| Jogador 8 | 1-1 | 22:48:58 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 1-1 | 22:48:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 1-2 | 22:49:02 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Leona | 0.2000 |  |
| Jogador 8 | 1-2 | 22:49:02 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Leona | -0.1000 |  |
| Jogador 8 | 1-2 | 22:49:03 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.1700 |  |
| Jogador 8 | 1-2 | 22:49:03 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 1-2 | 22:49:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 8 | 1-2 | 22:49:04 | MOVE Board -> Board: Leona (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 8 | 1-2 | 22:49:04 | MOVE Board -> Board: Leona (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 8 | 1-2 | 22:49:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 8 | 1-3 | 22:49:09 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Leona | -0.0900 |  |
| Jogador 8 | 1-3 | 22:49:09 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 1.1200 |  |
| Jogador 8 | 1-3 | 22:49:09 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.2300 |  |
| Jogador 8 | 1-3 | 22:49:10 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_RekSai | -0.2700 |  |
| Jogador 8 | 1-3 | 22:49:10 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_RekSai | 1.0400 |  |
| Jogador 8 | 1-3 | 22:49:10 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_RekSai | 0.0000 |  |
| Jogador 8 | 1-3 | 22:49:11 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.1700 |  |
| Jogador 8 | 1-3 | 22:49:11 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_RekSai | -0.3900 |  |
| Jogador 8 | 1-3 | 22:49:11 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.1600 |  |
| Jogador 8 | 1-3 | 22:49:12 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 1-3 | 22:49:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 1-4 | 22:49:15 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_RekSai | -0.0100 |  |
| Jogador 8 | 1-4 | 22:49:16 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Teemo | 0.0000 |  |
| Jogador 8 | 1-4 | 22:49:16 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Teemo | 0.1700 |  |
| Jogador 8 | 1-4 | 22:49:17 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | 0.3000 |  |
| Jogador 8 | 1-4 | 22:49:17 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | 0.0000 |  |
| Jogador 8 | 1-4 | 22:49:18 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | 0.4500 |  |
| Jogador 8 | 1-4 | 22:49:18 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_BFSword -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | 0.2100 |  |
| Jogador 8 | 1-4 | 22:49:19 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | 0.1300 |  |
| Jogador 8 | 1-4 | 22:49:19 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Teemo | 0.1400 |  |
| Jogador 8 | 1-4 | 22:49:19 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | -0.3900 |  |
| Jogador 8 | 1-4 | 22:49:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | 0.0000 |  |
| Jogador 8 | 2-1 | 22:49:22 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Teemo | 1.0400 |  |
| Jogador 8 | 2-1 | 22:49:22 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Teemo | -0.7500 |  |
| Jogador 8 | 2-1 | 22:49:23 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | 0.2400 |  |
| Jogador 8 | 2-1 | 22:49:23 | MOVE Bench -> Board: Krugue (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | -0.0100 |  |
| Jogador 8 | 2-1 | 22:49:24 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Krug18 | 0.0100 |  |
| Jogador 8 | 2-1 | 22:49:24 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Krugue (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Krug18 | 0.1400 |  |
| Jogador 8 | 2-1 | 22:49:24 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Krugue (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Krug18 | 0.0800 |  |
| Jogador 8 | 2-1 | 22:49:25 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Krug18 | 0.2200 |  |
| Jogador 8 | 2-1 | 22:49:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Krug18 | -0.0400 |  |
| Jogador 8 | 2-1 | 22:49:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | 0.0500 |  |
| Jogador 8 | 2-1 | 22:49:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-2 | 22:49:29 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Krug18 | -0.2600 |  |
| Jogador 8 | 2-2 | 22:49:30 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_Krug18 | 0.0900 |  |
| Jogador 8 | 2-2 | 22:49:30 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Krug18 | -0.3800 |  |
| Jogador 8 | 2-2 | 22:49:30 | COMPROU: Veigar (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_Krug18 | 0.3400 |  |
| Jogador 8 | 2-2 | 22:49:30 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Krug18 | -0.3200 |  |
| Jogador 8 | 2-2 | 22:49:31 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_Krug18 | 0.0800 |  |
| Jogador 8 | 2-2 | 22:49:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | -0.2000 |  |
| Jogador 8 | 2-2 | 22:49:31 | MOVE Board -> Board: Krugue (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-2 | 22:49:31 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Krug18 | -0.0800 |  |
| Jogador 8 | 2-2 | 22:49:32 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_Krug18 | 0.1400 |  |
| Jogador 8 | 2-2 | 22:49:32 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-3 | 22:49:36 | VENDEU: Rubrivirim (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_Krug18 | 0.0500 |  |
| Jogador 8 | 2-3 | 22:49:37 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_Krug18 | 0.0400 |  |
| Jogador 8 | 2-3 | 22:49:37 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Teemo (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 7 | 0 | — | DA_Krug18 | -0.3400 |  |
| Jogador 8 | 2-3 | 22:49:38 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 7 | 0 | — | DA_Krug18 | 0.3900 |  |
| Jogador 8 | 2-3 | 22:49:38 | COMPROU: Master Yi (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_Krug18 | 0.0600 |  |
| Jogador 8 | 2-3 | 22:49:39 | MOVE Board -> Board: Teemo (i:4.0) <-> Krugue (i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_Krug18 | 0.0100 |  |
| Jogador 8 | 2-3 | 22:49:39 | MOVE Board -> Board: Krugue (i:6.0) <-> Rek'Sai (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_Krug18 | -0.0100 |  |
| Jogador 8 | 2-3 | 22:49:39 | BUY XP | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_Krug18 | -0.0400 |  |
| Jogador 8 | 2-3 | 22:49:39 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Rek'Sai (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-3 | 22:49:40 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_Krug18 | -0.0100 |  |
| Jogador 8 | 2-3 | 22:49:40 | PASSOU TURNO | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-4 | 22:49:43 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Kha'Zix (i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 6 | 0 | Lutador | DA_Krug18 | -0.6000 |  |
| Jogador 8 | 2-4 | 22:49:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rek'Sai (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Lutador | DA_Krug18 | -0.4100 |  |
| Jogador 8 | 2-4 | 22:49:44 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Lutador | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-5 | 22:49:50 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Lutador | DA_Krug18 | -0.7900 |  |
| Jogador 8 | 2-5 | 22:49:51 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 0 | Lutador | DA_Krug18 | 1.0400 |  |
| Jogador 8 | 2-5 | 22:49:51 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Lutador | DA_Krug18 | -0.7900 |  |
| Jogador 8 | 2-5 | 22:49:51 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Lutador | DA_Krug18 | 0.3800 |  |
| Jogador 8 | 2-5 | 22:49:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Lutador | DA_Krug18 | -0.0700 |  |
| Jogador 8 | 2-5 | 22:49:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Lutador | DA_Krug18 | -0.0600 |  |
| Jogador 8 | 2-5 | 22:49:53 | MOVE Bench -> Board: Grompe (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Lutador | DA_Krug18 | -0.3600 |  |
| Jogador 8 | 2-5 | 22:49:53 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_Krug18 | 0.4800 |  |
| Jogador 8 | 2-5 | 22:49:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Tristana | 0.1200 |  |
| Jogador 8 | 2-5 | 22:49:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 2-6 | 22:49:58 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lutador | DA_Krug18 | -0.0200 |  |
| Jogador 8 | 2-6 | 22:49:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Lutador | DA_18_Tristana | 0.0500 |  |
| Jogador 8 | 2-6 | 22:49:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Tristana | -0.0400 |  |
| Jogador 8 | 2-6 | 22:49:58 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Lutador | DA_Krug18 | -0.1000 |  |
| Jogador 8 | 2-6 | 22:49:59 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_Krug18 | 0.3200 |  |
| Jogador 8 | 2-6 | 22:49:59 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_Krug18 | -0.0400 |  |
| Jogador 8 | 2-6 | 22:50:00 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-7 | 22:50:05 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Lutador | DA_Krug18 | -0.1400 |  |
| Jogador 8 | 2-7 | 22:50:05 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Lillia | -0.1400 |  |
| Jogador 8 | 2-7 | 22:50:06 | MOVE Bench -> Board: Lillia (i:8.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Lillia | -0.4000 |  |
| Jogador 8 | 2-7 | 22:50:06 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_SparringGloves -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Lillia | 0.0700 |  |
| Jogador 8 | 2-7 | 22:50:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 2-7 | 22:50:06 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-1 | 22:50:13 | COMPROU: Sett (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_Lillia | 0.2000 |  |
| Jogador 8 | 3-1 | 22:50:13 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Lillia | 0.7300 |  |
| Jogador 8 | 3-1 | 22:50:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-2 | 22:50:21 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Lillia | 0.2800 |  |
| Jogador 8 | 3-2 | 22:50:21 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Lutador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-2 | 22:50:21 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-2 | 22:50:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-3 | 22:50:30 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Lutador | DA_18_Lillia | 0.1300 |  |
| Jogador 8 | 3-3 | 22:50:30 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Lutador | DA_18_Lillia | 0.2800 |  |
| Jogador 8 | 3-3 | 22:50:30 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_Lillia | 0.0700 |  |
| Jogador 8 | 3-3 | 22:50:30 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-3 | 22:50:35 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_Lillia | 0.5600 |  |
| Jogador 8 | 3-4 | 22:50:39 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Lutador | DA_18_Lillia | 0.8000 |  |
| Jogador 8 | 3-4 | 22:50:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Lutador | DA_18_Lillia | 0.2800 |  |
| Jogador 8 | 3-4 | 22:50:39 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_Lillia | 0.0600 |  |
| Jogador 8 | 3-4 | 22:50:39 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-5 | 22:50:48 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Lutador | DA_18_Lillia | 0.2800 |  |
| Jogador 8 | 3-5 | 22:50:49 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_Lillia | -0.0900 |  |
| Jogador 8 | 3-5 | 22:50:49 | MOVE Board -> Board: Lillia (i:8.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-5 | 22:50:49 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Lutador | DA_18_Lillia | 0.0700 |  |
| Jogador 8 | 3-5 | 22:50:50 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_Lillia | 0.0900 |  |
| Jogador 8 | 3-5 | 22:50:50 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Lutador | DA_18_Lillia | 0.0600 |  |
| Jogador 8 | 3-5 | 22:50:50 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_Lillia | 0.0100 |  |
| Jogador 8 | 3-5 | 22:50:50 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-5 | 22:50:50 | MOVE Board -> Board: Teemo (i:4.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_Lillia | -0.0200 |  |
| Jogador 8 | 3-5 | 22:50:53 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-5 | 22:50:53 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-6 | 22:50:56 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Lutador | DA_18_Lillia | 0.0700 |  |
| Jogador 8 | 3-6 | 22:50:57 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Lutador | DA_18_Lillia | 0.8000 |  |
| Jogador 8 | 3-6 | 22:50:57 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Lutador | DA_18_Lillia | 0.0900 |  |
| Jogador 8 | 3-6 | 22:50:57 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Lutador | DA_18_Lillia | -0.4100 |  |
| Jogador 8 | 3-6 | 22:50:57 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Lutador | DA_18_Lillia | -0.1100 |  |
| Jogador 8 | 3-6 | 22:50:58 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Lutador | DA_18_Lillia | 0.8100 |  |
| Jogador 8 | 3-6 | 22:50:58 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Lutador | DA_18_Lillia | -0.0900 |  |
| Jogador 8 | 3-6 | 22:50:58 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Lutador | DA_18_Lillia | -0.1100 |  |
| Jogador 8 | 3-6 | 22:50:59 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Lutador | DA_Gromp18_AP | 0.8400 |  |
| Jogador 8 | 3-6 | 22:50:59 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_Gromp18_AP | 0.1800 |  |
| Jogador 8 | 3-6 | 22:51:01 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Lutador | DA_Gromp18_AP | 0.0000 |  |
| Jogador 8 | 3-7 | 22:51:05 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Lutador | DA_Gromp18_AP | 0.5900 |  |
| Jogador 8 | 3-7 | 22:51:07 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_Gromp18_AP | -0.0700 |  |
| Jogador 8 | 3-7 | 22:51:07 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_SparringGloves -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_Gromp18_AP | 0.1000 |  |
| Jogador 8 | 3-7 | 22:51:08 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_BFSword -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_Gromp18_AP | 0.0800 |  |
| Jogador 8 | 3-7 | 22:51:08 | MOVE Bench -> Board: Soraka (i:8.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_Gromp18_AP | -0.3900 |  |
| Jogador 8 | 3-7 | 22:51:08 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Lutador | DA_Gromp18_AP | 0.0000 |  |
| Jogador 8 | 4-1 | 22:51:14 | VENDEU: Grompe (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Lutador | DA_18_Lillia | -0.0800 |  |
| Jogador 8 | 4-1 | 22:51:15 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 9 | 0 | Lutador | DA_18_Lillia | 0.1500 |  |
| Jogador 8 | 4-1 | 22:51:15 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Lutador | DA_18_Lillia | -0.0900 |  |
| Jogador 8 | 4-1 | 22:51:15 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Lutador | DA_18_Lillia | 0.1400 |  |
| Jogador 8 | 4-1 | 22:51:15 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Lutador | DA_KogMaw18_AD | 0.7100 |  |
| Jogador 8 | 4-1 | 22:51:15 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Lutador | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 8 | 4-1 | 22:51:16 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Lutador | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 8 | 4-1 | 22:51:16 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Lutador | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 8 | 4-1 | 22:51:16 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Lutador | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 8 | 4-1 | 22:51:18 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Lutador | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 8 | 4-1 | 22:51:19 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Lutador | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 8 | 4-2 | 22:51:25 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Lutador | DA_18_Sett | 0.7100 |  |
| Jogador 8 | 4-2 | 22:51:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Lutador | DA_18_Sett | -0.0900 |  |
| Jogador 8 | 4-2 | 22:51:25 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Lutador | DA_18_Sett | -0.3100 |  |
| Jogador 8 | 4-2 | 22:51:26 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Lutador | DA_18_Sett | 0.1600 |  |
| Jogador 8 | 4-2 | 22:51:26 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Lutador | DA_18_Sett | -0.0900 |  |
| Jogador 8 | 4-2 | 22:51:26 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Lutador | DA_18_Sett | -0.0900 |  |
| Jogador 8 | 4-2 | 22:51:26 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Lutador | DA_18_Sett | 0.0600 |  |
| Jogador 8 | 4-2 | 22:51:27 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Lutador | DA_18_Sett | 0.2200 |  |
| Jogador 8 | 4-2 | 22:51:27 | MOVE Board -> Board: Soraka (i:8.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Lutador | DA_18_Sett | 0.0000 |  |
| Jogador 8 | 4-2 | 22:51:30 | MOVE Board -> Board: Lillia (i:8.0) <-> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Lutador | DA_18_Sett | -0.0100 |  |
| Jogador 8 | 4-2 | 22:51:30 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Lutador | DA_18_Sett | -0.0500 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 21 | 24 | 120 | 21 | 13 | 170 | 12 | 21 |
| Jogador 2 | 38 | 48 | 240 | 38 | 19 | 301 | 10 | 32 |
| Jogador 3 | 21 | 30 | 150 | 21 | 12 | 166 | 10 | 18 |
| Jogador 4 | 31 | 47 | 235 | 31 | 16 | 240 | 16 | 37 |
| Jogador 5 | 40 | 54 | 270 | 40 | 18 | 289 | 19 | 35 |
| Jogador 6 | 27 | 39 | 195 | 27 | 16 | 221 | 22 | 34 |
| Jogador 7 | 40 | 67 | 335 | 40 | 18 | 333 | 14 | 46 |
| Jogador 8 | 21 | 29 | 145 | 21 | 12 | 170 | 27 | 17 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 170 | 170 | 170 | 0 | 165 | 0 | 170 | 170 | 170 | 46/31 |
| Jogador 2 | 301 | 301 | 301 | 0 | 283 | 0 | 301 | 301 | 301 | 75/60 |
| Jogador 3 | 166 | 166 | 166 | 0 | 159 | 0 | 166 | 166 | 166 | 41/27 |
| Jogador 4 | 240 | 240 | 240 | 0 | 230 | 0 | 240 | 240 | 240 | 70/56 |
| Jogador 5 | 289 | 289 | 289 | 0 | 277 | 0 | 289 | 289 | 289 | 80/64 |
| Jogador 6 | 221 | 221 | 221 | 0 | 212 | 0 | 221 | 221 | 221 | 58/43 |
| Jogador 7 | 333 | 333 | 333 | 0 | 317 | 0 | 333 | 333 | 333 | 98/83 |
| Jogador 8 | 170 | 170 | 170 | 0 | 163 | 0 | 170 | 170 | 170 | 52/37 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +a8111a04-3067-4ce6-9a4b-4f5bb205f413 / -— |
| Jogador 1 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.010813108645379543 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0420212745666504 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 32 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43606460094451904 | 0.0 | 0.0 | +— / -cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16422347724437714 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16107149422168732 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 35 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 1.037848949432373 | 0.0 | 0.0 | +679fe281-674a-438b-bdcf-57229a283d44 / -— |
| Jogador 1 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001769986585713923 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5139204263687134 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2561686038970947 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 58 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12074161320924759 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2298053652048111 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 60 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.116797536611557 | 0.0 | 0.0 | +— / -cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 1-3 | 61 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.005341030657291412 | 0.0 | 0.0 | +8189d616-2d10-437f-86ce-218e11038acc / -— |
| Jogador 1 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002674856805242598 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7631890177726746 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 64 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11858195811510086 | 0.0 | 0.0 | +— / -a8111a04-3067-4ce6-9a4b-4f5bb205f413 |
| Jogador 1 | 1-3 | 65 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0031931400299072 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 67 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 83 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.303732305765152 | 0.0 | 0.0 | +— / -8189d616-2d10-437f-86ce-218e11038acc |
| Jogador 1 | 1-4 | 84 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1179225444793701 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -2718f555-b782-4fea-a68f-31395ad34232,679fe281-674a-438b-bdcf-57229a283d44 |
| Jogador 1 | 1-4 | 85 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38566645979881287 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 7 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2464548647403717 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 87 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 6 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25161847472190857 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1320265233516693 | 0.0 | 0.0 | +50fd90d6-9c1c-467f-bb3c-e88ca8815ef7 / -— |
| Jogador 1 | 1-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017987156752496958 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 90 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44245752692222595 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 91 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 92 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BOARD, PASS | True | True | 0.2823280096054077 | 0.0 | 0.0 | +9a936ebd-aacd-4366-a1c8-78534d5a253b / -— |
| Jogador 1 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 106 | SELL | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.25028616189956665 | 0.0 | 0.0 | +— / -9a936ebd-aacd-4366-a1c8-78534d5a253b |
| Jogador 1 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.0242080688476562 | 0.0 | 0.0 | +6770b090-e992-44c8-9223-f5cd6e92f19a / -— |
| Jogador 1 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 109 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014879242517054081 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 110 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 121 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5657782554626465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 127 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.25920891761779785 | 0.0 | 0.0 | +e76c0caf-1c3d-493f-9a21-659dd8587fc2 / -— |
| Jogador 1 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.29159125685691833 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 129 | SELL | STABILIZE | 95.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05647692456841469 | 0.0 | 0.0 | +— / -6465b229-8025-4e7d-94de-1cd49fa76167 |
| Jogador 1 | 2-2 | 130 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3219042122364044 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 131 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09845324605703354 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 132 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1377149224281311 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 133 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07080506533384323 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 134 | SELL | STABILIZE | 95.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 135 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20285102725028992 | 0.0 | 0.0 | +4fc25524-9d8f-46f0-a145-ba3de2642229 / -— |
| Jogador 1 | 2-2 | 136 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 137 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 152 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44149520993232727 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 153 | BUY | STABILIZE | 89.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.18549175560474396 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -— |
| Jogador 1 | 2-3 | 154 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04302069544792175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 155 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014901629649102688 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 156 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09872128069400787 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 157 | PASS | STABILIZE | 89.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 176 | SELL | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3439147472381592 | 0.0 | 0.0 | +— / -6770b090-e992-44c8-9223-f5cd6e92f19a |
| Jogador 1 | 2-4 | 177 | BUY | LOSS_STREAK | 84.0 | 5 | 10 | 1 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22247183322906494 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 178 | SELL | LOSS_STREAK | 84.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2648353576660156 | 0.0 | 0.0 | +— / -d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 2-4 | 179 | BUY | LOSS_STREAK | 84.0 | 5 | 10 | 1 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.057314321398735046 | 0.0 | 0.0 | +8c5a0cda-86da-4f36-bee3-c2eae934e263 / -— |
| Jogador 1 | 2-4 | 180 | SELL | LOSS_STREAK | 84.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24638544023036957 | 0.0 | 0.0 | +— / -8c5a0cda-86da-4f36-bee3-c2eae934e263 |
| Jogador 1 | 2-4 | 181 | BUY | LOSS_STREAK | 84.0 | 5 | 10 | 1 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05688611790537834 | 0.0 | 0.0 | +6bd83e05-f1a5-46e0-9d00-661cb843c7dc / -— |
| Jogador 1 | 2-4 | 182 | BUY_XP | LOSS_STREAK | 84.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 183 | BUY_XP | LOSS_STREAK | 84.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 184 | MOVE_BOARD | LOSS_STREAK | 84.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 185 | SELL | LOSS_STREAK | 84.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0031538461335003376 | 0.0 | 0.0 | +— / -6bd83e05-f1a5-46e0-9d00-661cb843c7dc |
| Jogador 1 | 2-4 | 186 | PASS | LOSS_STREAK | 84.0 | 5 | 2 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 197 | BUY | LOSS_STREAK | 84.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8966079950332642 | 0.0 | 0.0 | +dafe41e7-f516-4032-84ea-233ff2ff6ae1 / -— |
| Jogador 1 | 2-5 | 198 | BUY_XP | LOSS_STREAK | 84.0 | 5 | 6 | 0 | 22.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 199 | MOVE_BOARD | SLOWROLL | 84.0 | 5 | 2 | 0 | 22.0 | Lutador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 200 | MOVE_BOARD | SLOWROLL | 84.0 | 5 | 2 | 0 | 22.0 | Lutador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014698603190481663 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 201 | PASS | SLOWROLL | 84.0 | 5 | 2 | 0 | 22.0 | Lutador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 217 | MOVE_BENCH | SLOWROLL | 77.0 | 6 | 8 | 0 | 22.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5899614095687866 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 218 | BUY | FAST8 | 77.0 | 6 | 8 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3179033100605011 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 219 | SELL | FAST8 | 77.0 | 6 | 5 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19292066991329193 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 2-6 | 220 | BUY | FAST8 | 77.0 | 6 | 8 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9165542125701904 | 0.0 | 0.0 | +b32c67a7-6903-403a-9ed6-519ac8487685 / -— |
| Jogador 1 | 2-6 | 221 | MOVE_BOARD | FAST8 | 77.0 | 6 | 6 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 222 | SELL | FAST8 | 77.0 | 6 | 6 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3517383933067322 | 0.0 | 0.0 | +— / -b32c67a7-6903-403a-9ed6-519ac8487685 |
| Jogador 1 | 2-6 | 223 | BUY | FAST8 | 77.0 | 6 | 8 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32039377093315125 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -— |
| Jogador 1 | 2-6 | 224 | BUY_XP | FAST8 | 77.0 | 6 | 7 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 225 | SELL | FAST8 | 77.0 | 6 | 3 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1549081653356552 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 2-6 | 226 | BUY_XP | FAST8 | 77.0 | 6 | 4 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 227 | PASS | FAST8 | 77.0 | 6 | 0 | 0 | 26.0 | Lutador/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 235 | BUY | FAST8 | 71.0 | 6 | 7 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.016739878803491592 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -— |
| Jogador 1 | 2-7 | 236 | BUY_XP | FAST8 | 71.0 | 6 | 5 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 237 | SELL | FAST8 | 71.0 | 6 | 1 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.583587492059451e-06 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 1 | 2-7 | 238 | MOVE_BOARD | FAST8 | 71.0 | 6 | 3 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 239 | MOVE_BOARD | FAST8 | 71.0 | 6 | 3 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.01498130802065134 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 240 | PASS | FAST8 | 71.0 | 6 | 3 | 0 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 254 | BUY | FAST8 | 71.0 | 6 | 10 | 1 | 26.0 | Lutador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.6859859824180603 | 0.0 | 0.0 | +dca8bf82-80ac-4054-9a77-3891a7de23e2 / -dafe41e7-f516-4032-84ea-233ff2ff6ae1,e76c0caf-1c3d-493f-9a21-659dd8587fc2 |
| Jogador 1 | 3-1 | 255 | MOVE_BENCH | SLOWROLL | 71.0 | 6 | 8 | 0 | 18.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.34981438517570496 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 256 | BUY | FAST8 | 71.0 | 6 | 8 | 0 | 26.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.7315480709075928 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 257 | MOVE_BENCH | FAST8 | 71.0 | 6 | 5 | 0 | 26.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5308934450149536 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 258 | CRAFT_AND_EQUIP | FAST8 | 71.0 | 6 | 5 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.16239476203918457 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 259 | MOVE_BOARD | FAST8 | 71.0 | 6 | 5 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 260 | MOVE_BOARD | FAST8 | 71.0 | 6 | 5 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 261 | PASS | FAST8 | 71.0 | 6 | 5 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 272 | BUY | FAST8 | 61.0 | 6 | 13 | 1 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6911235451698303 | 0.0 | 0.0 | +dc9a3df1-7032-4c92-a919-ca17ae7639ea / -— |
| Jogador 1 | 3-2 | 273 | MOVE_BOARD | FAST8 | 61.0 | 6 | 11 | 1 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.678175956651103e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 274 | BUY_XP | FAST8 | 61.0 | 6 | 11 | 1 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 275 | BUY_XP | FAST8 | 61.0 | 6 | 7 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 276 | MOVE_BENCH | FAST8 | 61.0 | 6 | 3 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 277 | MOVE_BOARD | FAST8 | 61.0 | 6 | 3 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 278 | PASS | FAST8 | 61.0 | 6 | 3 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 292 | SELL | FAST8 | 61.0 | 6 | 9 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21967367827892303 | 0.0 | 0.0 | +— / -4fc25524-9d8f-46f0-a145-ba3de2642229 |
| Jogador 1 | 3-3 | 293 | BUY | FAST8 | 61.0 | 6 | 11 | 1 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13588549196720123 | 0.0 | 0.0 | +66b5ed5e-7fdf-4135-a334-e693715e302d / -— |
| Jogador 1 | 3-3 | 294 | MOVE_BENCH | FAST8 | 61.0 | 6 | 9 | 0 | 32.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059246405959129333 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 295 | MOVE_BENCH | FAST8 | 61.0 | 6 | 9 | 0 | 30.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4108133018016815 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 296 | BUY_XP | FAST8 | 61.0 | 6 | 9 | 0 | 28.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 297 | BUY_XP | FAST8 | 61.0 | 6 | 5 | 0 | 28.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09130000323057175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 298 | MOVE_BENCH | FAST8 | 61.0 | 7 | 1 | 0 | 28.0 | Lutador/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5924244523048401 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 299 | MOVE_BOARD | FAST8 | 61.0 | 7 | 1 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BOARD, PASS | True | True | -0.01498669944703579 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 300 | MOVE_BOARD | FAST8 | 61.0 | 7 | 1 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 301 | PASS | FAST8 | 61.0 | 7 | 1 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 312 | BUY | FAST8 | 50.0 | 7 | 6 | 0 | 36.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19187656044960022 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 313 | MOVE_BOARD | FAST8 | 50.0 | 7 | 4 | 0 | 36.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 314 | BUY_XP | FAST8 | 50.0 | 7 | 4 | 0 | 36.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 315 | MOVE_BOARD | FAST8 | 50.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 316 | MOVE_BOARD | FAST8 | 50.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015024229884147644 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 317 | PASS | FAST8 | 50.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 332 | BUY | FAST8 | 50.0 | 7 | 5 | 0 | 36.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7104009985923767 | 0.0 | 0.0 | +c5557e24-8174-4d79-9e22-c2cbbb8225a8 / -— |
| Jogador 1 | 3-5 | 333 | MOVE_BOARD | FAST8 | 50.0 | 7 | 3 | 0 | 36.0 | Lutador/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.588421557447873e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 334 | BUY | FAST8 | 50.0 | 7 | 3 | 0 | 36.0 | Lutador/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26723143458366394 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 335 | MOVE_BOARD | FAST8 | 50.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 336 | MOVE_BOARD | FAST8 | 50.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014962339773774147 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 337 | PASS | FAST8 | 50.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 352 | BUY | FAST8 | 39.0 | 7 | 6 | 0 | 36.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7637466192245483 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -7c218f01-e884-46da-8a1a-2d2db27a5ff1,ff10e482-7085-4e73-8a0c-fdd3f4938128 |
| Jogador 1 | 3-6 | 353 | MOVE_BENCH | STABILIZE | 39.0 | 7 | 3 | 0 | 24.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15171031653881073 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 354 | MOVE_BOARD | FAST8 | 39.0 | 7 | 3 | 0 | 28.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000347048044205 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 355 | MOVE_BENCH | FAST8 | 39.0 | 7 | 3 | 0 | 28.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39531224966049194 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 356 | BUY | FAST8 | 39.0 | 7 | 3 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28663548827171326 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 1 | 3-6 | 357 | MOVE_BOARD | FAST8 | 39.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 358 | MOVE_BOARD | FAST8 | 39.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015022318810224533 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 359 | PASS | FAST8 | 39.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 371 | BUY | STABILIZE | 27.0 | 7 | 7 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8035407066345215 | 0.0 | 0.0 | +e9d5f645-4afc-44f4-ae53-bc832c49f451 / -— |
| Jogador 1 | 3-7 | 372 | BUY | STABILIZE | 27.0 | 7 | 4 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2737331986427307 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 1 | 3-7 | 373 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.7236420616391115e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 374 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 375 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997483231127262 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 376 | PASS | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 390 | BUY | STABILIZE | 27.0 | 7 | 7 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.31366780400276184 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 1 | 4-1 | 391 | BUY | STABILIZE | 27.0 | 7 | 4 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07956434041261673 | 0.0 | 0.0 | +2c153083-6c43-425e-90d5-23f7f2058592 / -— |
| Jogador 1 | 4-1 | 392 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1623016744852066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 393 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18957822024822235 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 394 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.923293429077603e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 395 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 396 | PASS | STABILIZE | 27.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 402 | BUY | STABILIZE | 16.0 | 7 | 7 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2836940288543701 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 1 | 4-2 | 403 | BUY | STABILIZE | 16.0 | 7 | 4 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8063223958015442 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -— |
| Jogador 1 | 4-2 | 404 | SELL | STABILIZE | 16.0 | 7 | 3 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11136922985315323 | 0.0 | 0.0 | +— / -727765c8-7f02-491e-a6da-12b0dab59f6d |
| Jogador 1 | 4-2 | 405 | BUY | STABILIZE | 16.0 | 7 | 6 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27448704838752747 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 1 | 4-2 | 406 | REROLL | STABILIZE | 16.0 | 7 | 5 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 407 | SELL | STABILIZE | 16.0 | 7 | 3 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07601538300514221 | 0.0 | 0.0 | +— / -88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 1 | 4-2 | 408 | BUY | STABILIZE | 16.0 | 7 | 6 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25602108240127563 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 1 | 4-2 | 409 | REROLL | STABILIZE | 16.0 | 7 | 2 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 410 | SELL | STABILIZE | 16.0 | 7 | 0 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07900000363588333 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 1 | 4-2 | 411 | BUY | STABILIZE | 16.0 | 7 | 2 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021207062527537346 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 1 | 4-2 | 412 | PASS | STABILIZE | 16.0 | 7 | 0 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 422 | SELL | ALL_IN | 3.0 | 7 | 7 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059430770576000214 | 0.0 | 0.0 | +— / -ad19ac66-9f86-4c29-8ae7-7222164aece1 |
| Jogador 1 | 4-3 | 423 | BUY | ALL_IN | 3.0 | 7 | 9 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10650749504566193 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 1 | 4-3 | 424 | SELL | ALL_IN | 3.0 | 7 | 5 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057615384459495544 | 0.0 | 0.0 | +— / -ba7f039a-929c-4537-9eb6-f1dc4563cca8 |
| Jogador 1 | 4-3 | 425 | BUY | ALL_IN | 3.0 | 7 | 6 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08329826593399048 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 1 | 4-3 | 426 | REROLL | ALL_IN | 3.0 | 7 | 2 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 427 | SELL | ALL_IN | 3.0 | 7 | 0 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07709230482578278 | 0.0 | 0.0 | +— / -696f53ae-1413-47cc-b491-9870b7bcba51 |
| Jogador 1 | 4-3 | 428 | BUY | ALL_IN | 3.0 | 7 | 4 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07445283234119415 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 1 | 4-3 | 429 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04990766942501068 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 430 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 431 | PASS | ALL_IN | 3.0 | 7 | 1 | 0 | 32.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3124316334724426 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.597818911075592 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.010702039115130901 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.4452881411416456e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.01761229895055294 | 0.0 | 0.0 | +e0168c63-e704-4dde-8311-b514c6f4093b / -— |
| Jogador 2 | 1-2 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013737630797550082 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.399654358625412 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.26063358783721924 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 60 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 83 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.11784827709198 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -292ef825-d326-4dd8-9c42-c47cfc62116f,94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.388526976108551 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4350897967815399 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14850637316703796 | 0.0 | 0.0 | +9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 / -— |
| Jogador 2 | 1-4 | 87 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015042101964354515 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 89 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 106 | SELL | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10893038660287857 | 0.0 | 0.0 | +— / -9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 |
| Jogador 2 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.286196231842041 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4238637387752533 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.36612749099731445 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 110 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1743798404932022 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 111 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18333472311496735 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 112 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07501967251300812 | 0.0 | 0.0 | +— / -6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 2-1 | 113 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.06211361661553383 | 0.0 | 0.0 | +18082e05-51e8-4142-b541-c3d7d781b878 / -— |
| Jogador 2 | 2-1 | 114 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008661538362503052 | 0.0 | 0.0 | +— / -18082e05-51e8-4142-b541-c3d7d781b878 |
| Jogador 2 | 2-1 | 115 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 127 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0119812488555908 | 0.0 | 0.0 | +23a7be1c-afbc-4200-98c5-f6752ea11e7f / -— |
| Jogador 2 | 2-2 | 128 | SELL | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45907536149024963 | 0.0 | 0.0 | +— / -23a7be1c-afbc-4200-98c5-f6752ea11e7f |
| Jogador 2 | 2-2 | 129 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.25183090567588806 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 130 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 131 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.989531614934094e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 132 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014380855485796928 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-2 | 133 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 134 | BUY | SLOWROLL | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.06255064904689789 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 135 | SELL | SLOWROLL | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3158615529537201 | 0.0 | 0.0 | +— / -7ca9b803-76eb-4283-9648-7f98bfd81149 |
| Jogador 2 | 2-2 | 136 | BUY | SLOWROLL | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.06243351474404335 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -— |
| Jogador 2 | 2-2 | 137 | PASS | SLOWROLL | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 152 | SELL | SLOWROLL | 100.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-3 | 153 | BUY | SLOWROLL | 100.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08543127775192261 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 154 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6450667977333069 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 155 | SELL | SLOWROLL | 100.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4340954124927521 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-3 | 156 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11086228489875793 | 0.0 | 0.0 | +f75a22a6-8a32-4581-8724-bdb7712c21ee / -— |
| Jogador 2 | 2-3 | 157 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6318501830101013 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 158 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4103202819824219 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 159 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12822602689266205 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 2 | 2-3 | 160 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 22.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 161 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 22.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008661538362503052 | 0.0 | 0.0 | +— / -e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 2 | 2-3 | 162 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 22.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 176 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 22.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3695666491985321 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 177 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09848138689994812 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 178 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2170134037733078 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 179 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.5854729958373355e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 180 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 197 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21667760610580444 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 2 | 2-5 | 198 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.7728845023157191e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 199 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4087255597114563 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 200 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40911945700645447 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 201 | PASS | STABILIZE | 100.0 | 5 | 6 | 0 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 217 | SELL | STABILIZE | 100.0 | 5 | 13 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01899999938905239 | 0.0 | 0.0 | +— / -f75a22a6-8a32-4581-8724-bdb7712c21ee |
| Jogador 2 | 2-6 | 218 | SELL | STABILIZE | 100.0 | 5 | 15 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007591427303850651 | 0.0 | 0.0 | +— / -6a071ec5-c3f4-41b3-a0d8-c1aee62cffee |
| Jogador 2 | 2-6 | 219 | SELL | STABILIZE | 100.0 | 5 | 18 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13339880108833313 | 0.0 | 0.0 | +— / -e0168c63-e704-4dde-8311-b514c6f4093b |
| Jogador 2 | 2-6 | 220 | BUY | STABILIZE | 100.0 | 5 | 19 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0356618165969849 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 221 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 17 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09984941780567169 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 222 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 17 | 1 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41461506485939026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 223 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 17 | 1 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.413517028093338 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 224 | PASS | SLOWROLL | 100.0 | 5 | 17 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020357143133878708 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 235 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 26 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09985020011663437 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 236 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 26 | 2 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41462865471839905 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 237 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 26 | 2 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7199645638465881 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 238 | PASS | SLOWROLL | 100.0 | 5 | 26 | 2 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021964285522699356 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 254 | SELL | SLOWROLL | 100.0 | 5 | 35 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.40890777111053467 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 3-1 | 255 | BUY | SLOWROLL | 100.0 | 5 | 38 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.2537841200828552 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 256 | CRAFT_AND_EQUIP | SLOWROLL | 100.0 | 5 | 37 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16240090131759644 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 257 | SELL | SLOWROLL | 100.0 | 5 | 37 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.383104532957077 | 0.0 | 0.0 | +— / -a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 3-1 | 258 | BUY | SLOWROLL | 100.0 | 5 | 38 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10742674767971039 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 259 | BUY_XP | SLOWROLL | 100.0 | 5 | 35 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06814000010490417 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 260 | MOVE_BENCH | FAST8 | 100.0 | 6 | 31 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4043629765510559 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 261 | BUY | FAST8 | 100.0 | 6 | 31 | 3 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.14992019534111023 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 2 | 3-1 | 262 | BUY_XP | FAST8 | 100.0 | 6 | 29 | 2 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 263 | BUY_XP | FAST8 | 100.0 | 6 | 25 | 2 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 264 | PASS | FAST8 | 100.0 | 6 | 21 | 2 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05900000035762787 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 272 | BUY | FAST8 | 100.0 | 6 | 32 | 3 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2541183531284332 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 273 | BUY_XP | FAST8 | 100.0 | 6 | 31 | 3 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 274 | BUY_XP | FAST8 | 100.0 | 6 | 27 | 2 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 275 | BUY_XP | FAST8 | 100.0 | 6 | 23 | 2 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 276 | BUY_XP | FAST8 | 100.0 | 6 | 19 | 1 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 277 | BUY_XP | FAST8 | 100.0 | 6 | 15 | 1 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 278 | BUY_XP | FAST8 | 100.0 | 6 | 11 | 1 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 279 | BUY_XP | FAST8 | 100.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 280 | PASS | FAST8 | 100.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 290 | MOVE_BENCH | FAST8 | 100.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40081050992012024 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 292 | BUY | FAST8 | 100.0 | 7 | 12 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12326986342668533 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 293 | BUY | FAST8 | 100.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21248802542686462 | 0.0 | 0.0 | +c30a99f5-ce2d-4bbf-9aab-93017ad40255 / -— |
| Jogador 2 | 3-3 | 294 | MOVE_BOARD | FAST8 | 100.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 295 | BUY | FAST8 | 100.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07275798916816711 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 296 | MOVE_BENCH | FAST8 | 100.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3251281678676605 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 297 | MOVE_BENCH | FAST8 | 100.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08481220155954361 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 298 | MOVE_BENCH | FAST8 | 100.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7199872136116028 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 299 | MOVE_BOARD | FAST8 | 100.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 300 | PASS | FAST8 | 100.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 312 | BUY | FAST8 | 100.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6536133289337158 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 313 | BUY | FAST8 | 100.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7639195322990417 | 0.0 | 0.0 | +a15ff9dc-bf8a-49e0-9893-f92a212263d8 / -2ace989d-3e9e-483b-9b14-cd6b8f171f17,ff0d9869-c346-4210-be85-1e802a25dd8b |
| Jogador 2 | 3-4 | 314 | MOVE_BENCH | FAST8 | 100.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5939024686813354 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 315 | MOVE_BENCH | FAST8 | 100.0 | 7 | 4 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4047892987728119 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 316 | BUY | FAST8 | 100.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6030325293540955 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 317 | PASS | FAST8 | 100.0 | 7 | 1 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 332 | BUY | FAST8 | 100.0 | 7 | 9 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7475950717926025 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -8edef2b0-f5b3-4c01-ba2b-851be248676e,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 3-5 | 333 | BUY | FAST8 | 100.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5362250208854675 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 334 | BUY | FAST8 | 100.0 | 7 | 4 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19209317862987518 | 0.0 | 0.0 | +c946a8f3-ddcb-4e4a-8b00-a7bceead8633 / -— |
| Jogador 2 | 3-5 | 335 | MOVE_BOARD | FAST8 | 100.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.202226045890711e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 336 | MOVE_BENCH | FAST8 | 100.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4092198610305786 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 337 | BUY | FAST8 | 100.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028268078342080116 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 2 | 3-5 | 338 | PASS | FAST8 | 100.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 352 | BUY | FAST8 | 90.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.765909731388092 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -6f3f86ec-6928-4032-a1ef-533a68865516,de00430a-8a57-423c-887c-317d53c2cdd3 |
| Jogador 2 | 3-6 | 353 | BUY | FAST8 | 90.0 | 7 | 5 | 0 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21004599332809448 | 0.0 | 0.0 | +27102740-ce4d-4bec-a9eb-ed936f6bc364 / -— |
| Jogador 2 | 3-6 | 354 | MOVE_BENCH | FAST8 | 90.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11716021597385406 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 355 | MOVE_BENCH | FAST8 | 90.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.144318088889122 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 356 | MOVE_BENCH | FAST8 | 90.0 | 7 | 2 | 0 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3221515417098999 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 357 | BUY | FAST8 | 90.0 | 7 | 2 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07325106859207153 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 2 | 3-6 | 358 | MOVE_BOARD | FAST8 | 90.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007760247215628624 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 359 | MOVE_BOARD | FAST8 | 90.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 360 | PASS | FAST8 | 90.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 365 | MOVE_BENCH | FAST8 | 90.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6035284996032715 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 371 | BUY | FAST8 | 79.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14320093393325806 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 2 | 3-7 | 372 | SELL | FAST8 | 79.0 | 7 | 4 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060022007673978806 | 0.0 | 0.0 | +— / -0e31b1ec-3ead-480e-8577-f59bb5486d00 |
| Jogador 2 | 3-7 | 373 | BUY | FAST8 | 79.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18237192928791046 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 2 | 3-7 | 374 | MOVE_BOARD | FAST8 | 79.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 375 | MOVE_BOARD | FAST8 | 79.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012154330499470234 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 376 | PASS | FAST8 | 79.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 390 | SELL | FAST8 | 79.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.13576838374137878 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 4-1 | 391 | BUY | FAST8 | 79.0 | 7 | 9 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22660000622272491 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 2 | 4-1 | 392 | CRAFT_AND_EQUIP | FAST8 | 79.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07118778675794601 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 393 | CRAFT_AND_EQUIP | FAST8 | 79.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10265374183654785 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 394 | SELL | FAST8 | 79.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 4-1 | 395 | BUY | FAST8 | 79.0 | 7 | 9 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04808463528752327 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 2 | 4-1 | 396 | MOVE_BENCH | FAST8 | 79.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39807751774787903 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 397 | MOVE_BOARD | FAST8 | 79.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01366671547293663 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 398 | PASS | FAST8 | 79.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 402 | SELL | FAST8 | 79.0 | 7 | 12 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0729903057217598 | 0.0 | 0.0 | +— / -5af104f2-7959-4ca5-91a9-7d44494532ea |
| Jogador 2 | 4-2 | 403 | BUY | FAST8 | 79.0 | 7 | 15 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2167786806821823 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -— |
| Jogador 2 | 4-2 | 404 | SELL | FAST8 | 79.0 | 7 | 14 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013307692483067513 | 0.0 | 0.0 | +— / -6538f28f-845f-4f45-92bf-120931553bec |
| Jogador 2 | 4-2 | 405 | BUY | FAST8 | 79.0 | 7 | 15 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04197366535663605 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 2 | 4-2 | 406 | SELL | FAST8 | 79.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06570769101381302 | 0.0 | 0.0 | +— / -104aaac3-252c-4c1b-9ad8-fc10a35c6cda |
| Jogador 2 | 4-2 | 407 | BUY | FAST8 | 79.0 | 7 | 15 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15737347304821014 | 0.0 | 0.0 | +84886290-556f-45e9-805b-9ca86a80ba27 / -— |
| Jogador 2 | 4-2 | 408 | REROLL | FAST8 | 79.0 | 7 | 12 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 409 | SELL | FAST8 | 79.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07601538300514221 | 0.0 | 0.0 | +— / -84886290-556f-45e9-805b-9ca86a80ba27 |
| Jogador 2 | 4-2 | 410 | BUY | FAST8 | 79.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.732151210308075 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 2 | 4-2 | 411 | SELL | FAST8 | 79.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16640307009220123 | 0.0 | 0.0 | +— / -b75c9bc5-9bc7-465a-a97c-59156e5c482d |
| Jogador 2 | 4-2 | 412 | PASS | FAST8 | 79.0 | 7 | 15 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.10499999672174454 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 422 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08766782283782959 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 423 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0607096403837204 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 424 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10566116869449615 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 425 | BUY | FAST8 | 79.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6272179484367371 | 0.0 | 0.0 | +167110eb-b0d0-4873-9ffe-38286dcc5ca2 / -— |
| Jogador 2 | 4-3 | 426 | SELL | FAST8 | 79.0 | 7 | 20 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05231158807873726 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 2 | 4-3 | 427 | BUY | FAST8 | 79.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03896859660744667 | 0.0 | 0.0 | +cc9b5fff-2223-4721-a8b2-4f70e196b851 / -— |
| Jogador 2 | 4-3 | 428 | MOVE_BENCH | FAST8 | 79.0 | 7 | 20 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09992212057113647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 429 | REROLL | FAST8 | 79.0 | 7 | 20 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 430 | SELL | FAST8 | 79.0 | 7 | 18 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06401161849498749 | 0.0 | 0.0 | +— / -c946a8f3-ddcb-4e4a-8b00-a7bceead8633 |
| Jogador 2 | 4-3 | 431 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10586460679769516 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 432 | PASS | FAST8 | 79.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.10785714536905289 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 438 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 7 | 28 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1510981023311615 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 439 | BUY | FAST8 | 79.0 | 7 | 28 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23208607733249664 | 0.0 | 0.0 | +5c43307a-6d61-4493-a1ed-cb428d79a254 / -— |
| Jogador 2 | 4-4 | 440 | REROLL | FAST8 | 79.0 | 7 | 27 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 441 | SELL | FAST8 | 79.0 | 7 | 25 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013307692483067513 | 0.0 | 0.0 | +— / -5c43307a-6d61-4493-a1ed-cb428d79a254 |
| Jogador 2 | 4-4 | 442 | BUY | FAST8 | 79.0 | 7 | 26 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7411948442459106 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -— |
| Jogador 2 | 4-4 | 443 | REROLL | FAST8 | 79.0 | 7 | 25 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 444 | SELL | FAST8 | 79.0 | 7 | 23 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07299864292144775 | 0.0 | 0.0 | +— / -cc9b5fff-2223-4721-a8b2-4f70e196b851 |
| Jogador 2 | 4-4 | 445 | BUY | FAST8 | 79.0 | 7 | 26 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13871486485004425 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -— |
| Jogador 2 | 4-4 | 446 | MOVE_BENCH | FAST8 | 79.0 | 7 | 21 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5620163083076477 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 447 | MOVE_BENCH | FAST8 | 79.0 | 7 | 21 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08452533930540085 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 448 | PASS | FAST8 | 79.0 | 7 | 21 | 2 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029285714030265808 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 452 | MOVE_BENCH | FAST8 | 79.0 | 7 | 29 | 2 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3998585045337677 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 453 | SELL | FAST8 | 79.0 | 7 | 29 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04983076825737953 | 0.0 | 0.0 | +— / -167110eb-b0d0-4873-9ffe-38286dcc5ca2 |
| Jogador 2 | 4-5 | 454 | BUY | FAST8 | 79.0 | 7 | 32 | 3 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6932306289672852 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 2 | 4-5 | 455 | MOVE_BENCH | FAST8 | 79.0 | 7 | 28 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5577741861343384 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 456 | MOVE_BENCH | FAST8 | 79.0 | 7 | 28 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0841900184750557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 457 | MOVE_BENCH | FAST8 | 79.0 | 7 | 28 | 2 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.414517343044281 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 458 | MOVE_BENCH | FAST8 | 79.0 | 7 | 28 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5689507126808167 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 459 | PASS | FAST8 | 79.0 | 7 | 28 | 2 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034285712987184525 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 467 | MOVE_BENCH | FAST8 | 66.0 | 7 | 35 | 3 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09826734662055969 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 468 | MOVE_BENCH | FAST8 | 66.0 | 7 | 35 | 3 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025801626965403557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 469 | MOVE_BENCH | FAST8 | 66.0 | 7 | 35 | 3 | 36.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6550118327140808 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 470 | PASS | FAST8 | 66.0 | 7 | 35 | 3 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03928571566939354 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 482 | SELL | FAST8 | 66.0 | 7 | 44 | 4 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08263076841831207 | 0.0 | 0.0 | +— / -301afc05-ad23-4ed2-a835-108235c399e0 |
| Jogador 2 | 4-7 | 483 | BUY | FAST8 | 66.0 | 7 | 48 | 4 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8099037408828735 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 2 | 4-7 | 484 | SELL | FAST8 | 66.0 | 7 | 47 | 4 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0892215371131897 | 0.0 | 0.0 | +— / -a15ff9dc-bf8a-49e0-9893-f92a212263d8 |
| Jogador 2 | 4-7 | 485 | BUY | FAST8 | 66.0 | 7 | 55 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010024942457675934 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 2 | 4-7 | 486 | REROLL | FAST8 | 66.0 | 7 | 50 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 487 | SELL | FAST8 | 66.0 | 7 | 48 | 4 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05656307563185692 | 0.0 | 0.0 | +— / -cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 2 | 4-7 | 488 | BUY | FAST8 | 66.0 | 7 | 56 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8897174000740051 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -27102740-ce4d-4bec-a9eb-ed936f6bc364,29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 2 | 4-7 | 489 | BUY | FAST8 | 66.0 | 7 | 53 | 5 | 34.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09097355604171753 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 2 | 4-7 | 490 | MOVE_BENCH | FAST8 | 66.0 | 7 | 49 | 4 | 34.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.571837306022644 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 491 | BUY | FAST8 | 66.0 | 7 | 49 | 4 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012065639719367027 | 0.0 | 0.0 | +d2afd490-f89f-47c9-8279-a88acde5b1b6 / -— |
| Jogador 2 | 4-7 | 492 | PASS | FAST8 | 66.0 | 7 | 47 | 4 | 36.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047857142984867096 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 499 | CRAFT_AND_EQUIP | FAST8 | 66.0 | 7 | 56 | 5 | 36.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.0893205925822258 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 500 | CRAFT_AND_EQUIP | FAST8 | 66.0 | 7 | 56 | 5 | 36.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1177930012345314 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 501 | SELL | FAST8 | 66.0 | 7 | 56 | 5 | 36.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06096922978758812 | 0.0 | 0.0 | +— / -d2afd490-f89f-47c9-8279-a88acde5b1b6 |
| Jogador 2 | 5-1 | 502 | BUY | FAST8 | 66.0 | 7 | 58 | 5 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.062392380088567734 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 2 | 5-1 | 503 | MOVE_BENCH | FAST8 | 66.0 | 7 | 54 | 5 | 36.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39909395575523376 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 504 | SELL | FAST8 | 66.0 | 7 | 54 | 5 | 42.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16891999542713165 | 0.0 | 0.0 | +— / -2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d |
| Jogador 2 | 5-1 | 505 | EQUIP_FROM_INVENTORY | FAST8 | 66.0 | 7 | 62 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07814863324165344 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 506 | EQUIP_FROM_INVENTORY | FAST8 | 66.0 | 7 | 62 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08632630109786987 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 507 | BUY | FAST8 | 66.0 | 7 | 62 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.193030446767807 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 2 | 5-1 | 508 | REROLL | FAST8 | 66.0 | 7 | 59 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 509 | PASS | FAST8 | 66.0 | 7 | 57 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09242651611566544 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 512 | SELL | FAST8 | 66.0 | 7 | 67 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0382615402340889 | 0.0 | 0.0 | +— / -ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 |
| Jogador 2 | 5-2 | 513 | BUY | FAST8 | 66.0 | 7 | 70 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034034229815006256 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -— |
| Jogador 2 | 5-2 | 514 | MOVE_BOARD | FAST8 | 66.0 | 7 | 67 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002612141543067992 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 515 | REROLL | FAST8 | 66.0 | 7 | 67 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 516 | SELL | FAST8 | 66.0 | 7 | 65 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06690825521945953 | 0.0 | 0.0 | +— / -27079fe2-8808-47b7-8b10-9fb2834bb6ed |
| Jogador 2 | 5-2 | 517 | BUY | FAST8 | 66.0 | 7 | 68 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27042874693870544 | 0.0 | 0.0 | +e7c18780-1d70-4a15-ad72-2eaa0f81df8d / -— |
| Jogador 2 | 5-2 | 518 | SELL | FAST8 | 66.0 | 7 | 65 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04509230703115463 | 0.0 | 0.0 | +— / -76fcc4d0-4988-4e99-8ac0-c251f0b99dcd |
| Jogador 2 | 5-2 | 519 | BUY | FAST8 | 66.0 | 7 | 69 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16797111928462982 | 0.0 | 0.0 | +78adfe0a-b6d8-4cc4-a482-26451f95e788 / -— |
| Jogador 2 | 5-2 | 520 | REROLL | FAST8 | 66.0 | 7 | 67 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 521 | SELL | FAST8 | 66.0 | 7 | 65 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03936423733830452 | 0.0 | 0.0 | +— / -78adfe0a-b6d8-4cc4-a482-26451f95e788 |
| Jogador 2 | 5-2 | 522 | PASS | FAST8 | 66.0 | 7 | 67 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2537475526332855 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 529 | BUY | FAST8 | 50.0 | 7 | 77 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6363511085510254 | 0.0 | 0.0 | +d47034a1-8b51-4b82-b1b4-5f2aee8f959a / -— |
| Jogador 2 | 5-3 | 530 | SELL | FAST8 | 50.0 | 7 | 73 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35882148146629333 | 0.0 | 0.0 | +— / -e1055913-2340-4af0-8527-e175c8bc1ccb |
| Jogador 2 | 5-3 | 531 | BUY | FAST8 | 50.0 | 7 | 74 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1936480700969696 | 0.0 | 0.0 | +0f186e00-6f9d-4a22-a1ed-5ccd1b14613d / -— |
| Jogador 2 | 5-3 | 532 | MOVE_BENCH | FAST8 | 50.0 | 7 | 71 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09939385950565338 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 533 | MOVE_BENCH | FAST8 | 50.0 | 7 | 71 | 5 | 38.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19000335037708282 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 534 | MOVE_BENCH | FAST8 | 50.0 | 7 | 71 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4145062267780304 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 535 | PASS | FAST8 | 50.0 | 7 | 71 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10282160341739655 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 542 | SELL | STABILIZE | 34.0 | 7 | 82 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039000000804662704 | 0.0 | 0.0 | +— / -0f186e00-6f9d-4a22-a1ed-5ccd1b14613d |
| Jogador 2 | 5-4 | 543 | BUY | STABILIZE | 34.0 | 7 | 85 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38656938076019287 | 0.0 | 0.0 | +d8ca1093-815c-4f3e-af3e-fd6c4ab6ecd8 / -— |
| Jogador 2 | 5-4 | 544 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 82 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09939045459032059 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 545 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 82 | 5 | 38.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18928447365760803 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 546 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 82 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4145105183124542 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 547 | PASS | STABILIZE | 34.0 | 7 | 82 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1330680549144745 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 557 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 93 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09939078986644745 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 558 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 93 | 5 | 38.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18928447365760803 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 559 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 93 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4126078486442566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 560 | PASS | STABILIZE | 34.0 | 7 | 93 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14211498200893402 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 572 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 104 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6816877126693726 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 573 | SELL | STABILIZE | 34.0 | 7 | 104 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14303076267242432 | 0.0 | 0.0 | +— / -d47034a1-8b51-4b82-b1b4-5f2aee8f959a |
| Jogador 2 | 5-6 | 574 | BUY | STABILIZE | 34.0 | 7 | 108 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18667607009410858 | 0.0 | 0.0 | +0ba913e1-85ac-49ec-b800-33f13e98bc32 / -— |
| Jogador 2 | 5-6 | 575 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 105 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09960540384054184 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 576 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 105 | 5 | 38.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28706732392311096 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 577 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 105 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6942414045333862 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 578 | PASS | STABILIZE | 34.0 | 7 | 105 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1522529274225235 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 583 | SELL | STABILIZE | 34.0 | 7 | 117 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05376923084259033 | 0.0 | 0.0 | +— / -0ba913e1-85ac-49ec-b800-33f13e98bc32 |
| Jogador 2 | 5-7 | 584 | BUY | STABILIZE | 34.0 | 7 | 120 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.70600426197052 | 0.0 | 0.0 | +b1e222db-5292-4836-a0b4-2fe583bea359 / -— |
| Jogador 2 | 5-7 | 585 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 117 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09959419071674347 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 586 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 117 | 5 | 38.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2872346341609955 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 587 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 117 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6979691982269287 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 588 | PASS | STABILIZE | 34.0 | 7 | 117 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16261620819568634 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 597 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 7 | 128 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08372140675783157 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 598 | SELL | STABILIZE | 34.0 | 7 | 128 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14274045825004578 | 0.0 | 0.0 | +— / -b1e222db-5292-4836-a0b4-2fe583bea359 |
| Jogador 2 | 6-1 | 599 | BUY | STABILIZE | 34.0 | 7 | 131 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0011800527572632 | 0.0 | 0.0 | +224d16ae-530b-4d3a-b5a6-fa13f0ac246f / -— |
| Jogador 2 | 6-1 | 600 | SELL | STABILIZE | 34.0 | 7 | 130 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37227270007133484 | 0.0 | 0.0 | +— / -224d16ae-530b-4d3a-b5a6-fa13f0ac246f |
| Jogador 2 | 6-1 | 601 | BUY | STABILIZE | 34.0 | 7 | 131 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2643737196922302 | 0.0 | 0.0 | +a9fca874-b1ad-4bf2-a301-c25d11a7a4ad / -— |
| Jogador 2 | 6-1 | 602 | REROLL | STABILIZE | 34.0 | 7 | 128 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 603 | SELL | STABILIZE | 34.0 | 7 | 126 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039000000804662704 | 0.0 | 0.0 | +— / -a9fca874-b1ad-4bf2-a301-c25d11a7a4ad |
| Jogador 2 | 6-1 | 604 | BUY | STABILIZE | 34.0 | 7 | 129 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9389114379882812 | 0.0 | 0.0 | +d63a72f0-dcab-454e-afad-17ddc66b5b3d / -— |
| Jogador 2 | 6-1 | 605 | SELL | STABILIZE | 34.0 | 7 | 126 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26817458868026733 | 0.0 | 0.0 | +— / -362f7357-283e-4f88-bff3-ffa6314af821 |
| Jogador 2 | 6-1 | 606 | BUY | STABILIZE | 34.0 | 7 | 127 | 5 | 42.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4067549705505371 | 0.0 | 0.0 | +2ed313e3-0e1b-44b6-b254-f539d3f80a06 / -— |
| Jogador 2 | 6-1 | 607 | PASS | STABILIZE | 34.0 | 7 | 125 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18505248427391052 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 611 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 135 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09173636883497238 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 612 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 135 | 5 | 38.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007730151526629925 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 613 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 135 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41504862904548645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 614 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 135 | 5 | 42.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07673637568950653 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 615 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 135 | 5 | 38.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007530825678259134 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 616 | SELL | ALL_IN | 15.0 | 7 | 135 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06724421679973602 | 0.0 | 0.0 | +— / -d1840f93-35b0-4e88-b58e-eea7267beedc |
| Jogador 2 | 6-2 | 617 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 7 | 138 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0741400197148323 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 618 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 7 | 138 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08836904913187027 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 619 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 7 | 138 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.070328488945961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 620 | BUY | ALL_IN | 15.0 | 7 | 138 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24563826620578766 | 0.0 | 0.0 | +2ed60268-d2b1-4e41-bae7-43a89060e325 / -— |
| Jogador 2 | 6-3 | 622 | SELL | ALL_IN | 15.0 | 7 | 146 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038746919482946396 | 0.0 | 0.0 | +— / -2ed60268-d2b1-4e41-bae7-43a89060e325 |
| Jogador 2 | 6-3 | 623 | BUY | ALL_IN | 15.0 | 7 | 148 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.947738766670227 | 0.0 | 0.0 | +2b9c96b0-47c3-4330-894e-c42471aef448 / -— |
| Jogador 2 | 6-3 | 624 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 146 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09913048148155212 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 625 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 146 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41486579179763794 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 626 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 146 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 627 | PASS | ALL_IN | 15.0 | 7 | 146 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29604801535606384 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 634 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 157 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09913576394319534 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 635 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 157 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4148717224597931 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 636 | SELL | ALL_IN | 15.0 | 7 | 157 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05399581789970398 | 0.0 | 0.0 | +— / -e7c18780-1d70-4a15-ad72-2eaa0f81df8d |
| Jogador 2 | 6-4 | 637 | BUY | ALL_IN | 15.0 | 7 | 160 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37064746022224426 | 0.0 | 0.0 | +722c4076-6e3d-4b6c-aa0d-398e801d7224 / -— |
| Jogador 2 | 6-4 | 638 | REROLL | ALL_IN | 15.0 | 7 | 157 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 639 | SELL | ALL_IN | 15.0 | 7 | 155 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06062069535255432 | 0.0 | 0.0 | +— / -c5a8f36d-74b1-4944-a3db-bfb601a89b59 |
| Jogador 2 | 6-4 | 640 | BUY | ALL_IN | 15.0 | 7 | 156 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19912798702716827 | 0.0 | 0.0 | +922ab25c-c204-42a4-8e12-c58153e71efe / -— |
| Jogador 2 | 6-4 | 641 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 153 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 642 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 153 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08457525074481964 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 643 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 153 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41495266556739807 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 645 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 163 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 646 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 163 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08457532525062561 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 647 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 163 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20904876291751862 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 648 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 163 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41485264897346497 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 649 | PASS | ALL_IN | 15.0 | 7 | 163 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31295058131217957 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 653 | SELL | ALL_IN | 15.0 | 7 | 175 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057067692279815674 | 0.0 | 0.0 | +— / -922ab25c-c204-42a4-8e12-c58153e71efe |
| Jogador 2 | 6-6 | 654 | BUY | ALL_IN | 15.0 | 7 | 178 | 5 | 40.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0085877180099487 | 0.0 | 0.0 | +3863766f-09fc-48e0-9711-04ff7c1a0436 / -— |
| Jogador 2 | 6-6 | 655 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 177 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 656 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 177 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08486282080411911 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 657 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 177 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4147820770740509 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 658 | MOVE_BENCH | ALL_IN | 15.0 | 7 | 177 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 659 | PASS | ALL_IN | 15.0 | 7 | 177 | 5 | 40.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3270648717880249 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3026348650455475 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5972556471824646 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | -0.0104712825268507 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.038241982460022 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 32 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3872276842594147 | 0.0 | 0.0 | +— / -bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1454828530550003 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17799420654773712 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 35 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.061160679906606674 | 0.0 | 0.0 | +54a7d128-a897-4695-8240-9583c367fe28 / -— |
| Jogador 3 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014596588909626007 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40499091148376465 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10469050705432892 | 0.0 | 0.0 | +405de1b8-45c1-4b7f-b044-f12b819507c3 / -— |
| Jogador 3 | 1-3 | 58 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 83 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -405de1b8-45c1-4b7f-b044-f12b819507c3 |
| Jogador 3 | 1-4 | 84 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24201266467571259 | 0.0 | 0.0 | +d15ca853-2585-49d0-9d7f-339dae104062 / -— |
| Jogador 3 | 1-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37096086144447327 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 86 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008982628583908081 | 0.0 | 0.0 | +— / -2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 |
| Jogador 3 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19353166222572327 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 88 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10164615511894226 | 0.0 | 0.0 | +— / -ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 3 | 1-4 | 89 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 90 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 106 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.0263357162475586 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5220156908035278 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 108 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3445838689804077 | 0.0 | 0.0 | +70d8224e-5996-4629-b4f6-761ef5f01525 / -— |
| Jogador 3 | 2-1 | 109 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2202868014574051 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 110 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13803088665008545 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 112 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014600909315049648 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 113 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 127 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.115674614906311 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -c70251e8-af44-4466-808f-d49e9e5f57e9,d15ca853-2585-49d0-9d7f-339dae104062 |
| Jogador 3 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 4.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6280017495155334 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 129 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03388028219342232 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 130 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019894925877451897 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 131 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 145 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49138104915618896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 152 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0372810363769531 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 153 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0065115368925035 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 154 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0074280016124248505 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 155 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012025927193462849 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 156 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.297868013381958 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 157 | PASS | STABILIZE | 95.0 | 4 | 7 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 176 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 13 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5068042874336243 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 177 | BUY | SLOWROLL | 90.0 | 5 | 13 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1342233270406723 | 0.0 | 0.0 | +4c8a9a18-68d8-4672-a96d-bb09816257dc / -— |
| Jogador 3 | 2-4 | 178 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 10 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05808392912149429 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 179 | SELL | SLOWROLL | 90.0 | 5 | 10 | 1 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07244043052196503 | 0.0 | 0.0 | +— / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef |
| Jogador 3 | 2-4 | 180 | BUY | SLOWROLL | 90.0 | 5 | 11 | 1 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03791797161102295 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 181 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04608997330069542 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 182 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 183 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 184 | PASS | SLOWROLL | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 197 | BUY | SLOWROLL | 90.0 | 5 | 14 | 1 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3259197771549225 | 0.0 | 0.0 | +226a1062-8e9a-4652-9da7-a2f215fa46ae / -— |
| Jogador 3 | 2-5 | 198 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 12 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5187708139419556 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 199 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 12 | 1 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08289356529712677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 200 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 12 | 1 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4122178554534912 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 201 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 12 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 202 | PASS | SLOWROLL | 90.0 | 5 | 12 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 217 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 19 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06364872306585312 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 218 | BUY | SLOWROLL | 90.0 | 5 | 19 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0159910917282104 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 219 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5777773857116699 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 220 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 17 | 1 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031972967088222504 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 221 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014532062225043774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 222 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05011465772986412 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 223 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5902265906333923 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 224 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 17 | 1 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04630639776587486 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 225 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06464950740337372 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 226 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5772379636764526 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 227 | PASS | SLOWROLL | 90.0 | 5 | 17 | 1 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020357143133878708 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 235 | SELL | SLOWROLL | 84.0 | 5 | 23 | 2 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5550000071525574 | 0.0 | 0.0 | +— / -e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-7 | 236 | EQUIP_FROM_INVENTORY | SLOWROLL | 84.0 | 5 | 28 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18151476979255676 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 237 | EQUIP_FROM_INVENTORY | SLOWROLL | 84.0 | 5 | 28 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12468458712100983 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 238 | MOVE_BENCH | SLOWROLL | 84.0 | 5 | 28 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2661290764808655 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 239 | SELL | SLOWROLL | 84.0 | 5 | 28 | 2 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010118062607944012 | 0.0 | 0.0 | +— / -4c8a9a18-68d8-4672-a96d-bb09816257dc |
| Jogador 3 | 2-7 | 240 | SELL | SLOWROLL | 84.0 | 5 | 31 | 3 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9098096489906311 | 0.0 | 0.0 | +— / -70d8224e-5996-4629-b4f6-761ef5f01525 |
| Jogador 3 | 2-7 | 241 | BUY | SLOWROLL | 84.0 | 5 | 33 | 3 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0459840297698975 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0,226a1062-8e9a-4652-9da7-a2f215fa46ae |
| Jogador 3 | 2-7 | 242 | MOVE_BENCH | SLOWROLL | 84.0 | 5 | 31 | 3 | 12.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35112279653549194 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 243 | BUY | SLOWROLL | 84.0 | 5 | 31 | 3 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11048054695129395 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 244 | MOVE_BENCH | SLOWROLL | 84.0 | 5 | 28 | 2 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4227343201637268 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 245 | PASS | SLOWROLL | 84.0 | 5 | 28 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0223214291036129 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 254 | BUY | SLOWROLL | 84.0 | 5 | 35 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.22960790991783142 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 255 | MOVE_BOARD | SLOWROLL | 84.0 | 5 | 32 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 256 | MOVE_BOARD | SLOWROLL | 84.0 | 5 | 32 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.01481547299772501 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 257 | PASS | SLOWROLL | 84.0 | 5 | 32 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10649999976158142 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 272 | MOVE_BENCH | SLOWROLL | 73.0 | 5 | 41 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3996657431125641 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 273 | MOVE_BENCH | SLOWROLL | 73.0 | 5 | 41 | 4 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08312596380710602 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 274 | MOVE_BENCH | SLOWROLL | 73.0 | 5 | 41 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4127967357635498 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 275 | MOVE_BENCH | SLOWROLL | 73.0 | 5 | 41 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6085580587387085 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 276 | PASS | SLOWROLL | 73.0 | 5 | 41 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11100000143051147 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 292 | BUY | SLOWROLL | 62.0 | 5 | 51 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2810395359992981 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-3 | 293 | MOVE_BENCH | SLOWROLL | 62.0 | 5 | 49 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.097524493932724 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 294 | MOVE_BENCH | SLOWROLL | 62.0 | 5 | 49 | 4 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.41428011655807495 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 295 | CRAFT_AND_EQUIP | SLOWROLL | 62.0 | 5 | 49 | 4 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13481886684894562 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 296 | MOVE_BENCH | SLOWROLL | 62.0 | 5 | 49 | 4 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3992694318294525 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 297 | MOVE_BENCH | SLOWROLL | 62.0 | 5 | 49 | 4 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08328776806592941 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 298 | MOVE_BENCH | SLOWROLL | 62.0 | 5 | 49 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09622632712125778 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 299 | MOVE_BOARD | SLOWROLL | 62.0 | 5 | 49 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 300 | PASS | SLOWROLL | 62.0 | 5 | 49 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 312 | BUY | SLOWROLL | 51.0 | 5 | 59 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3476774990558624 | 0.0 | 0.0 | +c2c83d3a-8db0-4a0f-a896-4227c10a8d6a / -— |
| Jogador 3 | 3-4 | 313 | MOVE_BOARD | SLOWROLL | 51.0 | 5 | 58 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 314 | BUY | SLOWROLL | 51.0 | 5 | 58 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11623739451169968 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 315 | BUY_XP | SLOWROLL | 51.0 | 5 | 56 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 316 | BUY_XP | SLOWROLL | 51.0 | 5 | 52 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03669000044465065 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 317 | MOVE_BENCH | FAST8 | 51.0 | 6 | 48 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5940478444099426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 318 | BUY | FAST8 | 51.0 | 6 | 48 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15695375204086304 | 0.0 | 0.0 | +fe8191d8-bc21-499a-aff7-31c3ca9b2e64 / -— |
| Jogador 3 | 3-4 | 319 | MOVE_BOARD | FAST8 | 51.0 | 6 | 46 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.772286800085567e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 320 | MOVE_BOARD | FAST8 | 51.0 | 6 | 46 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 321 | PASS | FAST8 | 51.0 | 6 | 46 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 332 | BUY | FAST8 | 51.0 | 6 | 56 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8373099565505981 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 3 | 3-5 | 333 | BUY | FAST8 | 51.0 | 6 | 53 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3154107928276062 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 334 | BUY | FAST8 | 51.0 | 6 | 49 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02498440071940422 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 335 | BUY | FAST8 | 51.0 | 6 | 46 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2719808518886566 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -— |
| Jogador 3 | 3-5 | 336 | BUY | FAST8 | 51.0 | 6 | 44 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2791721522808075 | 0.0 | 0.0 | +5a16a58c-7001-4448-8ca5-6293f35e2c94 / -— |
| Jogador 3 | 3-5 | 337 | REROLL | FAST8 | 51.0 | 6 | 42 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 338 | SELL | FAST8 | 51.0 | 6 | 40 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07900000363588333 | 0.0 | 0.0 | +— / -5a16a58c-7001-4448-8ca5-6293f35e2c94 |
| Jogador 3 | 3-5 | 339 | BUY | FAST8 | 51.0 | 6 | 42 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7799372673034668 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 3 | 3-5 | 340 | MOVE_BOARD | FAST8 | 51.0 | 6 | 40 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.86941493768245e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 341 | MOVE_BOARD | FAST8 | 51.0 | 6 | 40 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01493627019226551 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 342 | PASS | FAST8 | 51.0 | 6 | 40 | 4 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 352 | SELL | FAST8 | 41.0 | 6 | 51 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07040232419967651 | 0.0 | 0.0 | +— / -fe8191d8-bc21-499a-aff7-31c3ca9b2e64 |
| Jogador 3 | 3-6 | 353 | BUY | FAST8 | 41.0 | 6 | 53 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8283341526985168 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -a9c52953-4532-455b-851f-04079adfd354,c3f8419e-a450-4247-bb65-8de8dba1c8ee |
| Jogador 3 | 3-6 | 354 | BUY | FAST8 | 41.0 | 6 | 50 | 5 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30508601665496826 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 3 | 3-6 | 355 | BUY | FAST8 | 41.0 | 6 | 47 | 4 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008047997951507568 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 3 | 3-6 | 356 | REROLL | FAST8 | 41.0 | 6 | 46 | 4 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 357 | SELL | FAST8 | 41.0 | 6 | 44 | 4 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05777249485254288 | 0.0 | 0.0 | +— / -23f4d10f-2614-47b2-bfb2-4fb276764b5e |
| Jogador 3 | 3-6 | 358 | BUY | FAST8 | 41.0 | 6 | 45 | 4 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24887816607952118 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-6 | 359 | MOVE_BOARD | FAST8 | 41.0 | 6 | 42 | 4 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 360 | MOVE_BOARD | FAST8 | 41.0 | 6 | 42 | 4 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 361 | PASS | FAST8 | 41.0 | 6 | 42 | 4 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03597777709364891 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 371 | SELL | STABILIZE | 29.0 | 6 | 54 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11815837025642395 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 3 | 3-7 | 372 | BUY | STABILIZE | 29.0 | 6 | 56 | 5 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31243330240249634 | 0.0 | 0.0 | +3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 / -— |
| Jogador 3 | 3-7 | 373 | REROLL | STABILIZE | 29.0 | 6 | 53 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 374 | SELL | STABILIZE | 29.0 | 6 | 51 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06934966892004013 | 0.0 | 0.0 | +— / -65a6d68c-90ae-4e31-8bbc-82e8ec75b3de |
| Jogador 3 | 3-7 | 375 | BUY | STABILIZE | 29.0 | 6 | 53 | 5 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7699676156044006 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 3 | 3-7 | 376 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 50 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6206324100494385 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 377 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 50 | 5 | 32.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05455330014228821 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 378 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 50 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2900799810886383 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 379 | REROLL | STABILIZE | 29.0 | 6 | 50 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 380 | REROLL | STABILIZE | 29.0 | 6 | 48 | 4 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 381 | PASS | STABILIZE | 29.0 | 6 | 46 | 4 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05291111022233963 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 390 | SELL | STABILIZE | 29.0 | 6 | 58 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1744338423013687 | 0.0 | 0.0 | +— / -320038b5-88c4-48fe-a7fa-a30823d674c0 |
| Jogador 3 | 4-1 | 391 | BUY | STABILIZE | 29.0 | 6 | 66 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8934925198554993 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 3 | 4-1 | 392 | CRAFT_AND_EQUIP | STABILIZE | 29.0 | 6 | 64 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20157520473003387 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 393 | CRAFT_AND_EQUIP | STABILIZE | 29.0 | 6 | 64 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22109615802764893 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 394 | SELL | STABILIZE | 29.0 | 6 | 64 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01647692359983921 | 0.0 | 0.0 | +— / -bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-1 | 395 | BUY | STABILIZE | 29.0 | 6 | 67 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05312388762831688 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -— |
| Jogador 3 | 4-1 | 396 | REROLL | STABILIZE | 29.0 | 6 | 64 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 397 | SELL | STABILIZE | 29.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05376923084259033 | 0.0 | 0.0 | +— / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9 |
| Jogador 3 | 4-1 | 398 | BUY | STABILIZE | 29.0 | 6 | 65 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8294291496276855 | 0.0 | 0.0 | +fb7e519a-8419-414a-8bdc-706c584ddeed / -— |
| Jogador 3 | 4-1 | 399 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0038340811152011156 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 400 | PASS | STABILIZE | 29.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11572493612766266 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 402 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 75 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39317721128463745 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 403 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 75 | 5 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3144972026348114 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 404 | PASS | STABILIZE | 17.0 | 6 | 75 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14610059559345245 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 422 | SELL | ALL_IN | 5.0 | 6 | 88 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06780000030994415 | 0.0 | 0.0 | +— / -8e1a5a7a-d27d-47c9-a197-b383c1c3da3b |
| Jogador 3 | 4-3 | 423 | BUY | ALL_IN | 5.0 | 6 | 91 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0481765270233154 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -4518ad1d-87e7-4110-830a-96183c533201,f0b6c16b-7610-454c-929d-7152f0a041d3 |
| Jogador 3 | 4-3 | 424 | BUY | ALL_IN | 5.0 | 6 | 89 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9522039890289307 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 3 | 4-3 | 425 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 88 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5607121586799622 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 426 | BUY | ALL_IN | 5.0 | 6 | 88 | 5 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033218394964933395 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 3 | 4-3 | 427 | REROLL | ALL_IN | 5.0 | 6 | 85 | 5 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 428 | SELL | ALL_IN | 5.0 | 6 | 83 | 5 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06078461557626724 | 0.0 | 0.0 | +— / -ddae48a6-5360-4660-9fa1-143ac35635ee |
| Jogador 3 | 4-3 | 429 | BUY | ALL_IN | 5.0 | 6 | 86 | 5 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03341292217373848 | 0.0 | 0.0 | +a11208a9-96bf-468e-ab92-2ead6308be26 / -— |
| Jogador 3 | 4-3 | 430 | REROLL | ALL_IN | 5.0 | 6 | 83 | 5 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 431 | REROLL | ALL_IN | 5.0 | 6 | 81 | 5 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 432 | PASS | ALL_IN | 5.0 | 6 | 79 | 5 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2203287035226822 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +1903eae4-bd37-4ed8-bbae-28177e859592 / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.010813108645379543 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1957342028617859 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15879949927330017 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.159445121884346 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0014473445480689406 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 35 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39271482825279236 | 0.0 | 0.0 | +— / -9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 1-2 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.06108194962143898 | 0.0 | 0.0 | +d4bb9e7b-2bfb-471f-8b71-e419aebe62d9 / -— |
| Jogador 4 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4055265486240387 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0168529748916626 | 0.0 | 0.0 | +e21ea220-ea66-4430-93a5-5b248b0f2b0b / -— |
| Jogador 4 | 1-3 | 58 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33166879415512085 | 0.0 | 0.0 | +— / -e21ea220-ea66-4430-93a5-5b248b0f2b0b |
| Jogador 4 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25182488560676575 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 60 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11724766343832016 | 0.0 | 0.0 | +— / -a19fc47b-fc81-49b2-bc25-d25d58b8deef |
| Jogador 4 | 1-3 | 61 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22071830928325653 | 0.0 | 0.0 | +3224c4b3-14ed-42e7-a497-24e0be0a691c / -— |
| Jogador 4 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01466921716928482 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 64 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 83 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11604660004377365 | 0.0 | 0.0 | +— / -3224c4b3-14ed-42e7-a497-24e0be0a691c |
| Jogador 4 | 1-4 | 84 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0395286083221436 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 85 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8335771560668945 | 0.0 | 0.0 | +— / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793 |
| Jogador 4 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0395349264144897 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 87 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8340904116630554 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0298265218734741 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 89 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33417877554893494 | 0.0 | 0.0 | +— / -4fbb2e46-1524-47c6-85a1-79266fd4da28 |
| Jogador 4 | 1-4 | 90 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 91 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.1775769144296646 | 0.0 | 0.0 | +b29f76e2-456d-4abf-b9a2-a4a80b577187 / -— |
| Jogador 4 | 1-4 | 92 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39143693447113037 | 0.0 | 0.0 | +— / -b29f76e2-456d-4abf-b9a2-a4a80b577187 |
| Jogador 4 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 106 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.23687030375003815 | 0.0 | 0.0 | +c05579e6-aa73-434f-8a91-c58d68a81ced / -— |
| Jogador 4 | 2-1 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.46077847480773926 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 108 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.0304925441741943 | 0.0 | 0.0 | +9819422b-1f51-47b5-89b7-9d6e906ddff2 / -— |
| Jogador 4 | 2-1 | 109 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17422634363174438 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 110 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11809605360031128 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 111 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33792632818222046 | 0.0 | 0.0 | +— / -9819422b-1f51-47b5-89b7-9d6e906ddff2 |
| Jogador 4 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2523517310619354 | 0.0 | 0.0 | +b166276e-305e-4945-8398-7c8b4b86ca9e / -— |
| Jogador 4 | 2-1 | 113 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41664308309555054 | 0.0 | 0.0 | +— / -b166276e-305e-4945-8398-7c8b4b86ca9e |
| Jogador 4 | 2-1 | 114 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00012845409219153225 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 115 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 127 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29838600754737854 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08352065831422806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 129 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05108056217432022 | 0.0 | 0.0 | +— / -95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-2 | 130 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8900741338729858 | 0.0 | 0.0 | +1acf3411-8f1a-4ee8-8a90-50013f260db3 / -— |
| Jogador 4 | 2-2 | 131 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025839999318122864 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 132 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6816775798797607 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 133 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42021992802619934 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 134 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09479250758886337 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 135 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08965739607810974 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 136 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497654803097248 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 137 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 152 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4263044595718384 | 0.0 | 0.0 | +— / -1acf3411-8f1a-4ee8-8a90-50013f260db3 |
| Jogador 4 | 2-3 | 153 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.382443368434906 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 154 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1695767641067505 | 0.0 | 0.0 | +— / -9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 4 | 2-3 | 155 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.038284182548523 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 156 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49065855145454407 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 157 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9472041130065918 | 0.0 | 0.0 | +e98ea24f-414b-4ccd-a19a-d98965ccc21c / -— |
| Jogador 4 | 2-3 | 158 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4263349175453186 | 0.0 | 0.0 | +— / -e98ea24f-414b-4ccd-a19a-d98965ccc21c |
| Jogador 4 | 2-3 | 159 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.30252110958099365 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -— |
| Jogador 4 | 2-3 | 160 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3525211215019226 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 161 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 162 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 176 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0370891094207764 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 177 | SELL | SLOWROLL | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.74892657995224 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 178 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19680918753147125 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 179 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09249874204397202 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 180 | SELL | STABILIZE | 95.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07811782509088516 | 0.0 | 0.0 | +— / -1903eae4-bd37-4ed8-bbae-28177e859592 |
| Jogador 4 | 2-4 | 181 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32929959893226624 | 0.0 | 0.0 | +27c9bbc9-ca0c-4ce7-bc7a-fcefe868e847 / -— |
| Jogador 4 | 2-4 | 182 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 183 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04392307624220848 | 0.0 | 0.0 | +— / -27c9bbc9-ca0c-4ce7-bc7a-fcefe868e847 |
| Jogador 4 | 2-4 | 184 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 24.0 | —/DA_18_Aphelios | BUY, MOVE_BOARD, PASS | True | True | 2.8618131182156503e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 185 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 24.0 | —/DA_18_Aphelios | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 197 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0345429182052612 | 0.0 | 0.0 | +3825a7ba-319f-48f8-ad2d-8c24eabbc1cc / -— |
| Jogador 4 | 2-5 | 198 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 3 | 0 | 24.0 | Lutador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09801603853702545 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 199 | SELL | SLOWROLL | 95.0 | 5 | 3 | 0 | 28.0 | Lutador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14184923470020294 | 0.0 | 0.0 | +— / -d4bb9e7b-2bfb-471f-8b71-e419aebe62d9 |
| Jogador 4 | 2-5 | 200 | BUY | SLOWROLL | 95.0 | 5 | 4 | 0 | 28.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2673555016517639 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 201 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 1 | 0 | 28.0 | Lutador/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 202 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 1 | 0 | 28.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014975041151046753 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 203 | PASS | SLOWROLL | 95.0 | 5 | 1 | 0 | 28.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 217 | MOVE_BENCH | SLOWROLL | 88.0 | 5 | 6 | 0 | 28.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07790166884660721 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 218 | SELL | SLOWROLL | 88.0 | 5 | 6 | 0 | 30.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18514153361320496 | 0.0 | 0.0 | +— / -c05579e6-aa73-434f-8a91-c58d68a81ced |
| Jogador 4 | 2-6 | 219 | EQUIP_FROM_INVENTORY | SLOWROLL | 88.0 | 5 | 8 | 0 | 30.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11766837537288666 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 220 | EQUIP_FROM_INVENTORY | SLOWROLL | 88.0 | 5 | 8 | 0 | 30.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07834838330745697 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 221 | BUY | SLOWROLL | 88.0 | 5 | 8 | 0 | 30.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3080466091632843 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 222 | BUY_XP | SLOWROLL | 88.0 | 5 | 5 | 0 | 30.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01384000014513731 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 223 | MOVE_BENCH | FAST8 | 88.0 | 6 | 1 | 0 | 30.0 | Lunar/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5473621487617493 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 224 | BUY | FAST8 | 88.0 | 6 | 1 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, MOVE_BOARD, PASS | True | True | 0.13106481730937958 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 225 | PASS | FAST8 | 88.0 | 6 | 0 | 0 | 36.0 | Lunar/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 235 | SELL | FAST8 | 88.0 | 6 | 6 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0341230109333992 | 0.0 | 0.0 | +— / -814d07bd-0296-44af-9626-26a8a224d86f |
| Jogador 4 | 2-7 | 236 | BUY | FAST8 | 88.0 | 6 | 7 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09937340766191483 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 237 | MOVE_BENCH | FAST8 | 88.0 | 6 | 4 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7890210747718811 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 238 | BUY_XP | FAST8 | 88.0 | 6 | 4 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 239 | PASS | FAST8 | 88.0 | 6 | 0 | 0 | 36.0 | Lunar/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 254 | CRAFT_AND_EQUIP | FAST8 | 88.0 | 6 | 5 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16015774011611938 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 255 | SELL | FAST8 | 88.0 | 6 | 5 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16448330879211426 | 0.0 | 0.0 | +— / -b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 3-1 | 256 | BUY | FAST8 | 88.0 | 6 | 8 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17639674246311188 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 257 | BUY_XP | FAST8 | 88.0 | 6 | 6 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 258 | PASS | FAST8 | 88.0 | 6 | 2 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 272 | SELL | FAST8 | 88.0 | 6 | 9 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03891022130846977 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-2 | 273 | BUY | FAST8 | 88.0 | 6 | 11 | 1 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.009026577696204185 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 274 | MOVE_BENCH | FAST8 | 88.0 | 6 | 8 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08758208155632019 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 275 | BUY_XP | FAST8 | 88.0 | 6 | 8 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 276 | BUY_XP | FAST8 | 88.0 | 6 | 4 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 277 | MOVE_BOARD | FAST8 | 88.0 | 6 | 0 | 0 | 36.0 | Lunar/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 278 | MOVE_BOARD | FAST8 | 88.0 | 6 | 0 | 0 | 36.0 | Lunar/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 279 | PASS | FAST8 | 88.0 | 6 | 0 | 0 | 36.0 | Lunar/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 292 | MOVE_BENCH | FAST8 | 88.0 | 6 | 7 | 0 | 36.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6282147169113159 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 293 | SELL | FAST8 | 88.0 | 6 | 7 | 0 | 38.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10558605194091797 | 0.0 | 0.0 | +— / -e989a0cc-848a-4c45-b153-315877aee8f7 |
| Jogador 4 | 3-3 | 294 | BUY | FAST8 | 88.0 | 6 | 9 | 0 | 38.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21144378185272217 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 295 | BUY_XP | FAST8 | 88.0 | 6 | 6 | 0 | 38.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 296 | PASS | FAST8 | 88.0 | 6 | 2 | 0 | 38.0 | Lunar/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 312 | BUY | FAST8 | 76.0 | 6 | 7 | 0 | 38.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5217028260231018 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 313 | BUY_XP | FAST8 | 76.0 | 6 | 4 | 0 | 38.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 314 | PASS | FAST8 | 76.0 | 6 | 0 | 0 | 38.0 | Lunar/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 332 | MOVE_BENCH | FAST8 | 76.0 | 7 | 5 | 0 | 38.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0670623704791069 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 333 | BUY | FAST8 | 76.0 | 7 | 5 | 0 | 44.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.761659562587738 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-5 | 334 | MOVE_BENCH | FAST8 | 76.0 | 7 | 2 | 0 | 32.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2652953565120697 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 335 | MOVE_BENCH | FAST8 | 76.0 | 7 | 2 | 0 | 44.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4039345681667328 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 336 | MOVE_BENCH | FAST8 | 76.0 | 7 | 2 | 0 | 38.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.551361620426178 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 337 | BUY | FAST8 | 76.0 | 7 | 2 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.013580839149653912 | 0.0 | 0.0 | +661b176a-5963-4715-b9dd-aca29f552fa9 / -— |
| Jogador 4 | 3-5 | 338 | MOVE_BOARD | FAST8 | 76.0 | 7 | 0 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.31410044857239e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 339 | PASS | FAST8 | 76.0 | 7 | 0 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 352 | BUY | FAST8 | 76.0 | 7 | 6 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7338544130325317 | 0.0 | 0.0 | +ee0b17ab-70b6-45db-8475-edb945dba9e0 / -— |
| Jogador 4 | 3-6 | 353 | BUY | FAST8 | 76.0 | 7 | 3 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49452266097068787 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 4 | 3-6 | 354 | MOVE_BOARD | FAST8 | 76.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 355 | MOVE_BOARD | FAST8 | 76.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 356 | PASS | FAST8 | 76.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 371 | BUY | FAST8 | 76.0 | 7 | 8 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21360352635383606 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 4 | 3-7 | 372 | BUY | FAST8 | 76.0 | 7 | 5 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6416803002357483 | 0.0 | 0.0 | +328e1a7d-391c-48e0-b268-64d26b4db788 / -661b176a-5963-4715-b9dd-aca29f552fa9,82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 4 | 3-7 | 373 | BUY | FAST8 | 76.0 | 7 | 3 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10649730265140533 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 4 | 3-7 | 374 | MOVE_BOARD | FAST8 | 76.0 | 7 | 0 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 375 | MOVE_BOARD | FAST8 | 76.0 | 7 | 0 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 376 | PASS | FAST8 | 76.0 | 7 | 0 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 390 | BUY | FAST8 | 76.0 | 7 | 6 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7339626550674438 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 4 | 4-1 | 391 | BUY | FAST8 | 76.0 | 7 | 3 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15203700959682465 | 0.0 | 0.0 | +967ab606-d775-468a-9c11-5ad0fd0e92f8 / -— |
| Jogador 4 | 4-1 | 392 | CRAFT_AND_EQUIP | FAST8 | 76.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23602049052715302 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 393 | CRAFT_AND_EQUIP | FAST8 | 76.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1566765010356903 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 394 | MOVE_BOARD | FAST8 | 76.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.5438112888641626e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 395 | PASS | FAST8 | 76.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 402 | BUY | FAST8 | 64.0 | 7 | 6 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04743579402565956 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-2 | 403 | BUY | FAST8 | 64.0 | 7 | 2 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1153528094291687 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 4 | 4-2 | 404 | PASS | FAST8 | 64.0 | 7 | 0 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 422 | BUY | FAST8 | 64.0 | 7 | 6 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16268666088581085 | 0.0 | 0.0 | +11b28280-bb53-4ca7-81b7-5ce8705303a5 / -— |
| Jogador 4 | 4-3 | 423 | SELL | FAST8 | 64.0 | 7 | 3 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06496923416852951 | 0.0 | 0.0 | +— / -26462e09-ab6e-4b87-85a8-6bda974b0c45 |
| Jogador 4 | 4-3 | 424 | BUY | FAST8 | 64.0 | 7 | 5 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03311071917414665 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 4 | 4-3 | 425 | MOVE_BOARD | FAST8 | 64.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.393644084809694e-09 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 426 | MOVE_BOARD | FAST8 | 64.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015003719367086887 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 427 | MOVE_BOARD | FAST8 | 64.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 428 | PASS | FAST8 | 64.0 | 7 | 1 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 438 | SELL | FAST8 | 64.0 | 7 | 8 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15232308208942413 | 0.0 | 0.0 | +— / -21135c93-ae87-47a0-899c-7eaa0c2c30b8 |
| Jogador 4 | 4-4 | 439 | BUY | FAST8 | 64.0 | 7 | 11 | 1 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32045450806617737 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -— |
| Jogador 4 | 4-4 | 440 | REROLL | FAST8 | 64.0 | 7 | 8 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 441 | SELL | FAST8 | 64.0 | 7 | 6 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07601538300514221 | 0.0 | 0.0 | +— / -4aa5d560-d9d3-45f9-802a-bdbe95788762 |
| Jogador 4 | 4-4 | 442 | BUY | FAST8 | 64.0 | 7 | 9 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43911391496658325 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 4 | 4-4 | 443 | MOVE_BENCH | FAST8 | 64.0 | 7 | 5 | 0 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39990735054016113 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 444 | MOVE_BENCH | FAST8 | 64.0 | 7 | 5 | 0 | 46.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2906840145587921 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 445 | PASS | FAST8 | 64.0 | 7 | 5 | 0 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 452 | MOVE_BENCH | FAST8 | 64.0 | 7 | 11 | 1 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09157618880271912 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 453 | SELL | FAST8 | 64.0 | 7 | 11 | 1 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.049371734261512756 | 0.0 | 0.0 | +— / -967ab606-d775-468a-9c11-5ad0fd0e92f8 |
| Jogador 4 | 4-5 | 454 | BUY | FAST8 | 64.0 | 7 | 13 | 1 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7295652627944946 | 0.0 | 0.0 | +685fc2a9-6a67-445e-ab34-59ec1f986f8e / -— |
| Jogador 4 | 4-5 | 455 | MOVE_BENCH | FAST8 | 64.0 | 7 | 10 | 1 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3999045193195343 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 456 | MOVE_BENCH | FAST8 | 64.0 | 7 | 10 | 1 | 46.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28220152854919434 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 457 | PASS | FAST8 | 64.0 | 7 | 10 | 1 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 467 | MOVE_BENCH | FAST8 | 64.0 | 7 | 17 | 1 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09151782840490341 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 468 | MOVE_BENCH | FAST8 | 64.0 | 7 | 17 | 1 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4149073660373688 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 469 | MOVE_BENCH | FAST8 | 64.0 | 7 | 17 | 1 | 46.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2810342609882355 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 470 | PASS | FAST8 | 64.0 | 7 | 17 | 1 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026428570970892906 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 482 | MOVE_BENCH | FAST8 | 51.0 | 7 | 23 | 2 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0948801040649414 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 483 | MOVE_BENCH | FAST8 | 51.0 | 7 | 23 | 2 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037797704339027405 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 484 | SELL | FAST8 | 51.0 | 7 | 23 | 2 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08382344245910645 | 0.0 | 0.0 | +— / -328e1a7d-391c-48e0-b268-64d26b4db788 |
| Jogador 4 | 4-7 | 485 | BUY | FAST8 | 51.0 | 7 | 28 | 2 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.750342607498169 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -— |
| Jogador 4 | 4-7 | 486 | MOVE_BENCH | FAST8 | 51.0 | 7 | 25 | 2 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39990153908729553 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 487 | MOVE_BENCH | FAST8 | 51.0 | 7 | 25 | 2 | 46.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08465247601270676 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 488 | REROLL | FAST8 | 51.0 | 7 | 25 | 2 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 489 | SELL | FAST8 | 51.0 | 7 | 23 | 2 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12762080132961273 | 0.0 | 0.0 | +— / -3825a7ba-319f-48f8-ad2d-8c24eabbc1cc |
| Jogador 4 | 4-7 | 490 | BUY | FAST8 | 51.0 | 7 | 26 | 2 | 52.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7551758289337158 | 0.0 | 0.0 | +8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 / -— |
| Jogador 4 | 4-7 | 491 | MOVE_BENCH | FAST8 | 51.0 | 7 | 23 | 2 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5179963111877441 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 492 | PASS | FAST8 | 51.0 | 7 | 23 | 2 | 46.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030714286491274834 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 499 | MOVE_BENCH | FAST8 | 51.0 | 7 | 30 | 3 | 46.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09986133128404617 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 500 | CRAFT_AND_EQUIP | FAST8 | 51.0 | 7 | 30 | 3 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20004533231258392 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 501 | CRAFT_AND_EQUIP | FAST8 | 51.0 | 7 | 30 | 3 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12081070244312286 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 502 | MOVE_BENCH | FAST8 | 51.0 | 7 | 30 | 3 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.399947851896286 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 503 | MOVE_BENCH | FAST8 | 51.0 | 7 | 30 | 3 | 52.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5329970717430115 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 504 | PASS | FAST8 | 51.0 | 7 | 30 | 3 | 46.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03928571566939354 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 512 | MOVE_BENCH | STABILIZE | 35.0 | 7 | 39 | 3 | 46.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09972667694091797 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 513 | SELL | STABILIZE | 35.0 | 7 | 39 | 3 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1392451375722885 | 0.0 | 0.0 | +— / -60138930-82d5-4f1c-a5fe-a22ea4b70d36 |
| Jogador 4 | 5-2 | 514 | BUY | STABILIZE | 35.0 | 7 | 43 | 4 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9689282774925232 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -8756c125-e3d6-4f40-80d2-a6bf20e7b1c7,8a52858d-da47-4de9-8e91-8612788cb8fd |
| Jogador 4 | 5-2 | 515 | BUY | STABILIZE | 35.0 | 7 | 40 | 4 | 44.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13490284979343414 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -— |
| Jogador 4 | 5-2 | 516 | MOVE_BENCH | STABILIZE | 35.0 | 7 | 37 | 3 | 44.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5651957392692566 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 517 | BUY | STABILIZE | 35.0 | 7 | 37 | 3 | 56.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2451004683971405 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 4 | 5-2 | 518 | REROLL | STABILIZE | 35.0 | 7 | 34 | 3 | 56.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 519 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 32 | 3 | 56.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.830090685776668e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 520 | SELL | STABILIZE | 35.0 | 7 | 32 | 3 | 56.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0737999975681305 | 0.0 | 0.0 | +— / -40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 4 | 5-2 | 521 | BUY | STABILIZE | 35.0 | 7 | 35 | 3 | 56.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9239708185195923 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0,a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 5-2 | 522 | PASS | STABILIZE | 35.0 | 7 | 32 | 3 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20919787883758545 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 529 | BUY | STABILIZE | 35.0 | 7 | 41 | 4 | 50.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32141098380088806 | 0.0 | 0.0 | +8c4772c9-83f1-4021-b83f-a9ff1773bea0 / -— |
| Jogador 4 | 5-3 | 530 | MOVE_BENCH | STABILIZE | 35.0 | 7 | 38 | 3 | 50.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5953188538551331 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 531 | BUY | STABILIZE | 35.0 | 7 | 38 | 3 | 62.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1783744990825653 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 4 | 5-3 | 532 | REROLL | STABILIZE | 35.0 | 7 | 36 | 3 | 62.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 533 | SELL | STABILIZE | 35.0 | 7 | 34 | 3 | 62.0 | Lunar/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07232307642698288 | 0.0 | 0.0 | +— / -c2bf43be-e6e1-47ed-bcb4-606e37f26671 |
| Jogador 4 | 5-3 | 534 | BUY | STABILIZE | 35.0 | 7 | 37 | 3 | 62.0 | Lunar/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9233778715133667 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -421bcbcb-ecb2-4af8-88d4-7be6cd284d27,ee0b17ab-70b6-45db-8475-edb945dba9e0 |
| Jogador 4 | 5-3 | 535 | BUY | STABILIZE | 35.0 | 7 | 34 | 3 | 56.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3360765874385834 | 0.0 | 0.0 | +a5247b50-831c-4600-bac0-e9bcdfa3ce1c / -— |
| Jogador 4 | 5-3 | 536 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 30 | 3 | 56.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0060511380434036255 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 537 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 30 | 3 | 56.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015001201070845127 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 538 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 30 | 3 | 56.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998533762991428 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 539 | PASS | STABILIZE | 35.0 | 7 | 30 | 3 | 56.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05232275277376175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 542 | MOVE_BENCH | STABILIZE | 18.0 | 7 | 39 | 3 | 56.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4164574146270752 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 543 | BUY | STABILIZE | 18.0 | 7 | 39 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8980894088745117 | 0.0 | 0.0 | +bf33b437-04ac-4dd7-8c7d-ad48546675b8 / -11b28280-bb53-4ca7-81b7-5ce8705303a5,39b89fbe-9520-4eaa-80f9-81e03232c83c |
| Jogador 4 | 5-4 | 544 | BUY | STABILIZE | 18.0 | 7 | 36 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04774601384997368 | 0.0 | 0.0 | +051d83d1-972e-42b2-ab59-376c753ad24e / -— |
| Jogador 4 | 5-4 | 545 | BUY | STABILIZE | 18.0 | 7 | 33 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.606800990179181e-06 | 0.0 | 0.0 | +db7ea53f-4df7-4c05-9462-75b527575615 / -— |
| Jogador 4 | 5-4 | 546 | REROLL | STABILIZE | 18.0 | 7 | 31 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 547 | REROLL | STABILIZE | 18.0 | 7 | 29 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 548 | REROLL | STABILIZE | 18.0 | 7 | 27 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 549 | REROLL | STABILIZE | 18.0 | 7 | 25 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 550 | REROLL | STABILIZE | 18.0 | 7 | 23 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 551 | SELL | STABILIZE | 18.0 | 7 | 21 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029773060232400894 | 0.0 | 0.0 | +— / -bf33b437-04ac-4dd7-8c7d-ad48546675b8 |
| Jogador 4 | 5-4 | 552 | PASS | STABILIZE | 18.0 | 7 | 29 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15994000434875488 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 557 | BUY | STABILIZE | 18.0 | 7 | 37 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3793807327747345 | 0.0 | 0.0 | +47b7832a-ef8a-436e-9e2e-84a5160ff6d5 / -— |
| Jogador 4 | 5-5 | 558 | REROLL | STABILIZE | 18.0 | 7 | 34 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 559 | SELL | STABILIZE | 18.0 | 7 | 32 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12178642302751541 | 0.0 | 0.0 | +— / -051d83d1-972e-42b2-ab59-376c753ad24e |
| Jogador 4 | 5-5 | 560 | BUY | STABILIZE | 18.0 | 7 | 35 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36492881178855896 | 0.0 | 0.0 | +41cebf65-3d00-41d3-bc56-d1d126a6e261 / -— |
| Jogador 4 | 5-5 | 561 | REROLL | STABILIZE | 18.0 | 7 | 32 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 562 | REROLL | STABILIZE | 18.0 | 7 | 30 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 563 | SELL | STABILIZE | 18.0 | 7 | 28 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15232308208942413 | 0.0 | 0.0 | +— / -47b7832a-ef8a-436e-9e2e-84a5160ff6d5 |
| Jogador 4 | 5-5 | 564 | BUY | STABILIZE | 18.0 | 7 | 31 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.760154664516449 | 0.0 | 0.0 | +88249896-79bb-4f76-94a3-131d12f9fc3d / -— |
| Jogador 4 | 5-5 | 565 | REROLL | STABILIZE | 18.0 | 7 | 27 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 566 | REROLL | STABILIZE | 18.0 | 7 | 25 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 567 | PASS | STABILIZE | 18.0 | 7 | 23 | 2 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05666571483016014 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 572 | SELL | ALL_IN | 3.0 | 7 | 31 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15134461224079132 | 0.0 | 0.0 | +— / -497fbcb9-9d15-43f0-ad71-96eeceeee99d |
| Jogador 4 | 5-6 | 573 | EQUIP_FROM_INVENTORY | ALL_IN | 3.0 | 7 | 39 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09565772861242294 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 574 | BUY | ALL_IN | 3.0 | 7 | 39 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9020633101463318 | 0.0 | 0.0 | +09105a4a-c4d1-43c0-b1fb-08df25bcafd5 / -— |
| Jogador 4 | 5-6 | 575 | REROLL | ALL_IN | 3.0 | 7 | 36 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 576 | SELL | ALL_IN | 3.0 | 7 | 34 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058430131524801254 | 0.0 | 0.0 | +— / -db7ea53f-4df7-4c05-9462-75b527575615 |
| Jogador 4 | 5-6 | 577 | BUY | ALL_IN | 3.0 | 7 | 36 | 3 | 60.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9374387860298157 | 0.0 | 0.0 | +9658df1d-f821-4560-b2b0-79ab4e1f14d9 / -09105a4a-c4d1-43c0-b1fb-08df25bcafd5,41cebf65-3d00-41d3-bc56-d1d126a6e261 |
| Jogador 4 | 5-6 | 578 | BUY | ALL_IN | 3.0 | 7 | 33 | 3 | 60.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.936393678188324 | 0.0 | 0.0 | +3c65e9e8-ff81-499f-8145-953bbcd0531e / -409b32b9-5280-4d79-b5b2-871ed597ba56,685fc2a9-6a67-445e-ab34-59ec1f986f8e |
| Jogador 4 | 5-6 | 579 | BUY | ALL_IN | 3.0 | 7 | 30 | 3 | 54.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07253415137529373 | 0.0 | 0.0 | +f488c144-76bf-48ab-b73a-92d1c650ecb6 / -— |
| Jogador 4 | 5-6 | 580 | BUY | ALL_IN | 3.0 | 7 | 26 | 2 | 54.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25266310572624207 | 0.0 | 0.0 | +316b1635-e9c1-41c2-a26f-e64625e1c743 / -— |
| Jogador 4 | 5-6 | 581 | REROLL | ALL_IN | 3.0 | 7 | 23 | 2 | 54.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +a05f4164-724c-4182-bafc-82ef354cea0b / -— |
| Jogador 5 | 1-1 | 3 | SELL | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | -0.5991230607032776 | 0.0 | 0.0 | +— / -a05f4164-724c-4182-bafc-82ef354cea0b |
| Jogador 5 | 1-1 | 4 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.24146294593811035 | 0.0 | 0.0 | +186434e2-f277-43a0-8eb2-ad1928a0427b / -— |
| Jogador 5 | 1-1 | 5 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Ornn | MOVE_BENCH, SELL, PASS | True | True | 0.5594962239265442 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 6 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | -0.010351459495723248 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 7 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0279690027236938 | 0.0 | 0.0 | +cd0ce7f1-5e14-4819-b275-2fab0e63d320 / -— |
| Jogador 5 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005744089838117361 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Ornn | BUY, MOVE_BOARD, PASS | True | True | 0.13407567143440247 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4538510739803314 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | -0.012188653461635113 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.07969730347394943 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 58 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10615991801023483 | 0.0 | 0.0 | +4a7ac9c5-c110-4566-80e5-25d9e6033799 / -— |
| Jogador 5 | 1-3 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 62 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 83 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00033658870961517096 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4071178138256073 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 85 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3582592010498047 | 0.0 | 0.0 | +— / -cd0ce7f1-5e14-4819-b275-2fab0e63d320 |
| Jogador 5 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12161863595247269 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 87 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37419962882995605 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 88 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3998391628265381 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 89 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 106 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.012907692231237888 | 0.0 | 0.0 | +— / -02c39b42-90d5-4e01-9380-460b6c1cb993 |
| Jogador 5 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.13875913619995117 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4459162950515747 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.32615458965301514 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -— |
| Jogador 5 | 2-1 | 110 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18136164546012878 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 111 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1198018491268158 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 112 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02302171103656292 | 0.0 | 0.0 | +— / -a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 |
| Jogador 5 | 2-1 | 113 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31121623516082764 | 0.0 | 0.0 | +c1362110-700c-4ff7-9347-eaa6d512081b / -— |
| Jogador 5 | 2-1 | 114 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015728211030364037 | 0.0 | 0.0 | +— / -c1362110-700c-4ff7-9347-eaa6d512081b |
| Jogador 5 | 2-1 | 115 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 116 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 16.0 | —/DA_18_Cassiopeia | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 127 | BUY | STABILIZE | 94.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3203972578048706 | 0.0 | 0.0 | +9bb3da58-fe6f-4298-8529-859cceb4857e / -— |
| Jogador 5 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04301479086279869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 129 | SELL | STABILIZE | 94.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764092281460762 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 2-2 | 130 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07752978056669235 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 131 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11034180968999863 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 132 | BUY | STABILIZE | 94.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2873683571815491 | 0.0 | 0.0 | +0debca82-3a2a-44ba-af48-83211d5e5243 / -— |
| Jogador 5 | 2-2 | 133 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005468133604153991 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 134 | PASS | STABILIZE | 94.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 152 | SELL | STABILIZE | 94.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1741630733013153 | 0.0 | 0.0 | +— / -0debca82-3a2a-44ba-af48-83211d5e5243 |
| Jogador 5 | 2-3 | 153 | BUY | STABILIZE | 94.0 | 4 | 11 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3370670676231384 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 154 | BUY_XP | STABILIZE | 94.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058435000479221344 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 155 | SELL | STABILIZE | 94.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0579538457095623 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 156 | BUY | STABILIZE | 94.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20024260878562927 | 0.0 | 0.0 | +c5f2f75f-c083-4bb0-b3eb-d234e782b1f5 / -— |
| Jogador 5 | 2-3 | 157 | SELL | STABILIZE | 94.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3254615366458893 | 0.0 | 0.0 | +— / -c5f2f75f-c083-4bb0-b3eb-d234e782b1f5 |
| Jogador 5 | 2-3 | 158 | BUY | STABILIZE | 94.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20013903081417084 | 0.0 | 0.0 | +79aec946-44a4-498c-b903-3b0707189713 / -— |
| Jogador 5 | 2-3 | 159 | BUY_XP | STABILIZE | 94.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 160 | SELL | STABILIZE | 94.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3254615366458893 | 0.0 | 0.0 | +— / -79aec946-44a4-498c-b903-3b0707189713 |
| Jogador 5 | 2-3 | 161 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 162 | PASS | STABILIZE | 94.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 176 | BUY | STABILIZE | 94.0 | 5 | 10 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16087178885936737 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 177 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012992930598556995 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 178 | SELL | STABILIZE | 94.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06185642629861832 | 0.0 | 0.0 | +— / -186434e2-f277-43a0-8eb2-ad1928a0427b |
| Jogador 5 | 2-4 | 179 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1856880933046341 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 180 | SELL | STABILIZE | 94.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3083707392215729 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 181 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15114432573318481 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 182 | BUY_XP | STABILIZE | 94.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 183 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 191 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40651077032089233 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 197 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 24.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0303643941879272 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 198 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 5 | 0 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0931360125541687 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 199 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 5 | 0 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4085792899131775 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 200 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 5 | 0 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 201 | PASS | SLOWROLL | 94.0 | 5 | 5 | 0 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 217 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 10 | 1 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.093620665371418 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 218 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 10 | 1 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40891996026039124 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 219 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 10 | 1 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08343140780925751 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 220 | BUY_XP | SLOWROLL | 89.0 | 5 | 10 | 1 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08884000033140182 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 221 | MOVE_BENCH | FAST8 | 89.0 | 6 | 6 | 0 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7149189114570618 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 222 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 6 | 0 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44610127806663513 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 223 | BUY | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.029964547604322433 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 224 | BUY_XP | FAST8 | 89.0 | 6 | 4 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 225 | PASS | FAST8 | 89.0 | 6 | 0 | 0 | 30.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 235 | SELL | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019605228677392006 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-7 | 236 | BUY | FAST8 | 89.0 | 6 | 8 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7811882495880127 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 237 | BUY_XP | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 238 | MOVE_BOARD | FAST8 | 89.0 | 6 | 2 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 239 | MOVE_BOARD | FAST8 | 89.0 | 6 | 2 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014905317686498165 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 240 | PASS | FAST8 | 89.0 | 6 | 2 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 254 | SELL | FAST8 | 89.0 | 6 | 7 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3123186528682709 | 0.0 | 0.0 | +— / -6eee9a92-4235-46af-ae42-c38acd6847ef |
| Jogador 5 | 3-1 | 255 | BUY | FAST8 | 89.0 | 6 | 9 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.18049246072769165 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 256 | CRAFT_AND_EQUIP | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14328204095363617 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 257 | MOVE_BOARD | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 258 | BUY_XP | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 259 | MOVE_BOARD | FAST8 | 89.0 | 6 | 2 | 0 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002230727404821664 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 260 | PASS | FAST8 | 89.0 | 6 | 2 | 0 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 272 | SELL | FAST8 | 89.0 | 6 | 9 | 0 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06779772788286209 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-2 | 273 | BUY | FAST8 | 89.0 | 6 | 12 | 1 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2149098813533783 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 274 | MOVE_BENCH | FAST8 | 89.0 | 6 | 10 | 1 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06993773579597473 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 275 | MOVE_BENCH | FAST8 | 89.0 | 6 | 10 | 1 | 28.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07013566046953201 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 276 | BUY_XP | FAST8 | 89.0 | 6 | 10 | 1 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 277 | BUY_XP | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 278 | MOVE_BENCH | FAST8 | 89.0 | 6 | 2 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39888179302215576 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 279 | MOVE_BOARD | FAST8 | 89.0 | 6 | 2 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 280 | PASS | FAST8 | 89.0 | 6 | 2 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 292 | MOVE_BENCH | FAST8 | 79.0 | 6 | 7 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.707696259021759 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 293 | MOVE_BENCH | FAST8 | 79.0 | 6 | 7 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4107188582420349 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 294 | PASS | FAST8 | 79.0 | 6 | 7 | 0 | 28.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 312 | MOVE_BENCH | FAST8 | 79.0 | 6 | 13 | 1 | 28.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09904297441244125 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 313 | BUY_XP | FAST8 | 79.0 | 6 | 13 | 1 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 314 | BUY_XP | FAST8 | 79.0 | 6 | 9 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 315 | MOVE_BENCH | FAST8 | 79.0 | 7 | 5 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4035591185092926 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 316 | BUY | FAST8 | 79.0 | 7 | 5 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.019778648391366005 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 317 | MOVE_BOARD | FAST8 | 79.0 | 7 | 3 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 318 | MOVE_BOARD | FAST8 | 79.0 | 7 | 3 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 319 | PASS | FAST8 | 79.0 | 7 | 3 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 332 | MOVE_BOARD | FAST8 | 79.0 | 7 | 8 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 333 | MOVE_BOARD | FAST8 | 79.0 | 7 | 8 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014737911522388458 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 334 | PASS | FAST8 | 79.0 | 7 | 8 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 352 | BUY | FAST8 | 79.0 | 7 | 15 | 1 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7338691353797913 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 5 | 3-6 | 353 | BUY_XP | FAST8 | 79.0 | 7 | 13 | 1 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 354 | BUY_XP | FAST8 | 79.0 | 7 | 9 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 355 | BUY_XP | FAST8 | 79.0 | 7 | 5 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 356 | PASS | FAST8 | 79.0 | 7 | 1 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 371 | SELL | FAST8 | 79.0 | 7 | 8 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05868096277117729 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-7 | 372 | SELL | FAST8 | 79.0 | 7 | 10 | 1 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36820924282073975 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 5 | 3-7 | 373 | BUY | FAST8 | 79.0 | 7 | 12 | 1 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.18338344991207123 | 0.0 | 0.0 | +014c92c3-e588-4e8b-b4bd-93cee45d74af / -— |
| Jogador 5 | 3-7 | 374 | MOVE_BENCH | FAST8 | 79.0 | 7 | 9 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3999118506908417 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 375 | MOVE_BENCH | FAST8 | 79.0 | 7 | 9 | 0 | 34.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08412473648786545 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 376 | BUY_XP | FAST8 | 79.0 | 7 | 9 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 377 | BUY_XP | FAST8 | 79.0 | 7 | 5 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 378 | PASS | FAST8 | 79.0 | 7 | 1 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 390 | BUY | FAST8 | 79.0 | 7 | 7 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7158045768737793 | 0.0 | 0.0 | +55944609-f4df-4e53-a1d1-31c79a148b22 / -— |
| Jogador 5 | 4-1 | 391 | CRAFT_AND_EQUIP | FAST8 | 79.0 | 7 | 4 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21365289390087128 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 392 | CRAFT_AND_EQUIP | FAST8 | 79.0 | 7 | 4 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19358769059181213 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 393 | BUY_XP | FAST8 | 79.0 | 7 | 4 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 394 | PASS | FAST8 | 79.0 | 7 | 0 | 0 | 36.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 402 | BUY | FAST8 | 79.0 | 7 | 7 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.763992965221405 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -486e92ad-4dcf-4c0e-a470-e0b87777d380,9bb3da58-fe6f-4298-8529-859cceb4857e |
| Jogador 5 | 4-2 | 403 | EQUIP_FROM_INVENTORY | STABILIZE | 79.0 | 7 | 4 | 0 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07119273394346237 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 404 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 4 | 0 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09249869734048843 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 405 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 4 | 0 | 24.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15286311507225037 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 406 | MOVE_BENCH | FAST8 | 79.0 | 7 | 4 | 0 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08487937599420547 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 407 | MOVE_BOARD | FAST8 | 79.0 | 7 | 4 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 408 | MOVE_BENCH | FAST8 | 79.0 | 7 | 4 | 0 | 36.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0114706140011549 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 409 | BUY | FAST8 | 79.0 | 7 | 4 | 0 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21395473182201385 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-2 | 410 | MOVE_BOARD | FAST8 | 79.0 | 7 | 1 | 0 | 38.0 | Defendente/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001721528678899631 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 411 | MOVE_BENCH | FAST8 | 79.0 | 7 | 1 | 0 | 38.0 | Defendente/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5839329957962036 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 412 | PASS | FAST8 | 79.0 | 7 | 1 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 422 | BUY | FAST8 | 68.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7339953780174255 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 5 | 4-3 | 423 | MOVE_BOARD | FAST8 | 68.0 | 7 | 3 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00010356936400057748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 424 | MOVE_BOARD | FAST8 | 68.0 | 7 | 3 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 425 | PASS | FAST8 | 68.0 | 7 | 3 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 438 | BUY | FAST8 | 68.0 | 7 | 9 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4676951467990875 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 5 | 4-4 | 439 | MOVE_BOARD | FAST8 | 68.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00010356936400057748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 440 | MOVE_BOARD | FAST8 | 68.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 441 | MOVE_BOARD | FAST8 | 68.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014738956466317177 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 442 | PASS | FAST8 | 68.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 452 | BUY | FAST8 | 68.0 | 7 | 11 | 1 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23059119284152985 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 5 | 4-5 | 453 | BUY_XP | FAST8 | 68.0 | 7 | 10 | 1 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 454 | BUY_XP | FAST8 | 68.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 455 | PASS | FAST8 | 68.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 467 | BUY | FAST8 | 68.0 | 7 | 9 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7289392948150635 | 0.0 | 0.0 | +99857cfa-b422-4167-bb01-d9fd94a55d88 / -— |
| Jogador 5 | 4-6 | 468 | BUY_XP | FAST8 | 68.0 | 7 | 8 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08269374817609787 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 469 | BUY | ECON | 68.0 | 8 | 4 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21939989924430847 | 0.0 | 0.0 | +4432f76a-94cc-4a96-b72b-1cf35b310dca / -— |
| Jogador 5 | 4-6 | 470 | MOVE_BENCH | ECON | 68.0 | 8 | 0 | 0 | 44.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40220946073532104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 471 | PASS | ECON | 68.0 | 8 | 0 | 0 | 52.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 482 | BUY | ECON | 68.0 | 8 | 6 | 0 | 52.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2139279991388321 | 0.0 | 0.0 | +33e9808b-2f92-49e7-ac35-1f6f9388edef / -— |
| Jogador 5 | 4-7 | 483 | BUY | ECON | 68.0 | 8 | 3 | 0 | 52.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.432257741689682 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 5 | 4-7 | 484 | PASS | ECON | 68.0 | 8 | 1 | 0 | 52.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 499 | BUY | ECON | 68.0 | 8 | 7 | 0 | 52.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7194868326187134 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -0f1b15a2-9978-4691-a15e-483ccd03db7f,55944609-f4df-4e53-a1d1-31c79a148b22 |
| Jogador 5 | 5-1 | 500 | MOVE_BENCH | ECON | 68.0 | 8 | 4 | 0 | 40.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.33722564578056335 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 501 | BUY | ECON | 68.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.041976265609264374 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 5 | 5-1 | 502 | CRAFT_AND_EQUIP | ECON | 68.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.142116978764534 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 503 | CRAFT_AND_EQUIP | ECON | 68.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08975096046924591 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 504 | MOVE_BOARD | ECON | 68.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 505 | MOVE_BOARD | ECON | 68.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 506 | PASS | ECON | 68.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 509 | MOVE_BENCH | ECON | 68.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4001293182373047 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 512 | BUY | ECON | 52.0 | 8 | 5 | 0 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7270293831825256 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -— |
| Jogador 5 | 5-2 | 513 | MOVE_BOARD | ECON | 52.0 | 8 | 1 | 0 | 50.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 514 | MOVE_BOARD | ECON | 52.0 | 8 | 1 | 0 | 50.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000687912106514 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 515 | PASS | ECON | 52.0 | 8 | 1 | 0 | 50.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 529 | SELL | ECON | 52.0 | 8 | 7 | 0 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07900000363588333 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 5-3 | 530 | BUY | ECON | 52.0 | 8 | 9 | 0 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7355222702026367 | 0.0 | 0.0 | +b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 / -— |
| Jogador 5 | 5-3 | 531 | MOVE_BOARD | ECON | 52.0 | 8 | 7 | 0 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 532 | MOVE_BOARD | ECON | 52.0 | 8 | 7 | 0 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01502988114953041 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 533 | PASS | ECON | 52.0 | 8 | 7 | 0 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 542 | SELL | ECON | 52.0 | 8 | 14 | 1 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12167692184448242 | 0.0 | 0.0 | +— / -908d49c8-626c-44b5-9b03-6a85442f358b |
| Jogador 5 | 5-4 | 543 | BUY | ECON | 52.0 | 8 | 16 | 1 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1326078325510025 | 0.0 | 0.0 | +52799e57-7b54-4dc5-b7f8-c39c8f57e7fa / -— |
| Jogador 5 | 5-4 | 544 | REROLL | ECON | 52.0 | 8 | 13 | 1 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 545 | SELL | ECON | 52.0 | 8 | 11 | 1 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04426153749227524 | 0.0 | 0.0 | +— / -52799e57-7b54-4dc5-b7f8-c39c8f57e7fa |
| Jogador 5 | 5-4 | 546 | BUY | ECON | 52.0 | 8 | 14 | 1 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16182000935077667 | 0.0 | 0.0 | +a960f5cb-d806-4d73-9146-244e1ecde6f2 / -— |
| Jogador 5 | 5-4 | 547 | SELL | ECON | 52.0 | 8 | 9 | 0 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04054392874240875 | 0.0 | 0.0 | +— / -18e21ac6-f873-4310-95c8-bd8e62612479 |
| Jogador 5 | 5-4 | 548 | BUY | ECON | 52.0 | 8 | 12 | 1 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10708443075418472 | 0.0 | 0.0 | +edd9f925-ac58-4285-a53c-ca70b782c682 / -— |
| Jogador 5 | 5-4 | 549 | REROLL | ECON | 52.0 | 8 | 8 | 0 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 550 | SELL | ECON | 52.0 | 8 | 6 | 0 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00822396483272314 | 0.0 | 0.0 | +— / -c07a17cf-e9e7-42be-b925-cb4f699593de |
| Jogador 5 | 5-4 | 551 | BUY | ECON | 52.0 | 8 | 14 | 1 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7658125162124634 | 0.0 | 0.0 | +699b59c7-1237-472b-a4d1-18a35e88b7c2 / -35a674f6-a230-480b-a93f-f7ec76d78658,b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 |
| Jogador 5 | 5-4 | 552 | PASS | ECON | 52.0 | 8 | 12 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 557 | BUY | ECON | 52.0 | 8 | 19 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16825130581855774 | 0.0 | 0.0 | +1932532c-8c2d-45c1-bdcc-77fc7d6bb4a8 / -— |
| Jogador 5 | 5-5 | 558 | MOVE_BENCH | ECON | 52.0 | 8 | 16 | 1 | 46.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40064704418182373 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 559 | BUY | ECON | 52.0 | 8 | 16 | 1 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21888460218906403 | 0.0 | 0.0 | +c06a964e-4ad5-444a-8800-0410c94f5c1f / -— |
| Jogador 5 | 5-5 | 560 | REROLL | ECON | 52.0 | 8 | 12 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 561 | SELL | ECON | 52.0 | 8 | 10 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07709230482578278 | 0.0 | 0.0 | +— / -c06a964e-4ad5-444a-8800-0410c94f5c1f |
| Jogador 5 | 5-5 | 562 | BUY | ECON | 52.0 | 8 | 14 | 1 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7639964818954468 | 0.0 | 0.0 | +8ec344bd-ba9a-47e6-ba65-a4c832038b18 / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5,45da6d00-829e-4e2e-a1a5-318498fd007b |
| Jogador 5 | 5-5 | 563 | BUY | ECON | 52.0 | 8 | 11 | 1 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03602791577577591 | 0.0 | 0.0 | +6e40ac88-b1d5-4294-b92e-5bc3902fc385 / -— |
| Jogador 5 | 5-5 | 564 | MOVE_BOARD | ECON | 52.0 | 8 | 6 | 0 | 48.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 565 | MOVE_BENCH | ECON | 52.0 | 8 | 6 | 0 | 48.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5657379031181335 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 566 | BUY | ECON | 52.0 | 8 | 6 | 0 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1983892023563385 | 0.0 | 0.0 | +af23c553-04de-4813-87d0-bb7e4becafe4 / -— |
| Jogador 5 | 5-5 | 567 | PASS | ECON | 52.0 | 8 | 5 | 0 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 572 | MOVE_BOARD | STABILIZE | 36.0 | 8 | 10 | 1 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.879349479684606e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 573 | SELL | STABILIZE | 36.0 | 8 | 10 | 1 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05277938395738602 | 0.0 | 0.0 | +— / -1932532c-8c2d-45c1-bdcc-77fc7d6bb4a8 |
| Jogador 5 | 5-6 | 574 | BUY | STABILIZE | 36.0 | 8 | 13 | 1 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19353950023651123 | 0.0 | 0.0 | +c5f81113-0e4a-4d08-beab-f19d808ef10c / -— |
| Jogador 5 | 5-6 | 575 | MOVE_BOARD | STABILIZE | 36.0 | 8 | 9 | 0 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 576 | SELL | STABILIZE | 36.0 | 8 | 9 | 0 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06889676302671432 | 0.0 | 0.0 | +— / -699b59c7-1237-472b-a4d1-18a35e88b7c2 |
| Jogador 5 | 5-6 | 577 | BUY | STABILIZE | 36.0 | 8 | 14 | 1 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13899391889572144 | 0.0 | 0.0 | +2adb37ce-c46e-4c3a-a715-443bdb688103 / -— |
| Jogador 5 | 5-6 | 578 | REROLL | STABILIZE | 36.0 | 8 | 11 | 1 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 579 | SELL | STABILIZE | 36.0 | 8 | 9 | 0 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14136935770511627 | 0.0 | 0.0 | +— / -2adb37ce-c46e-4c3a-a715-443bdb688103 |
| Jogador 5 | 5-6 | 580 | BUY | STABILIZE | 36.0 | 8 | 12 | 1 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2850343883037567 | 0.0 | 0.0 | +36a593e6-6199-441a-907d-77b9ea835889 / -— |
| Jogador 5 | 5-6 | 581 | SELL | STABILIZE | 36.0 | 8 | 10 | 1 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -edd9f925-ac58-4285-a53c-ca70b782c682 |
| Jogador 5 | 5-7 | 583 | BUY | STABILIZE | 20.0 | 8 | 21 | 2 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7599707841873169 | 0.0 | 0.0 | +4accaece-f84d-43da-967c-8c733bb95174 / -— |
| Jogador 5 | 5-7 | 584 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 18 | 1 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 585 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 18 | 1 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014971942640841007 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 586 | PASS | STABILIZE | 20.0 | 8 | 18 | 1 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04289418086409569 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 597 | EQUIP_FROM_INVENTORY | STABILIZE | 20.0 | 8 | 25 | 2 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08781424164772034 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 598 | SELL | STABILIZE | 20.0 | 8 | 25 | 2 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2095441222190857 | 0.0 | 0.0 | +— / -8ec344bd-ba9a-47e6-ba65-a4c832038b18 |
| Jogador 5 | 6-1 | 599 | BUY | STABILIZE | 20.0 | 8 | 33 | 3 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3830983340740204 | 0.0 | 0.0 | +b57fc469-d037-4ac4-9e70-645f71fb6399 / -— |
| Jogador 5 | 6-1 | 600 | SELL | STABILIZE | 20.0 | 8 | 30 | 3 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2665753960609436 | 0.0 | 0.0 | +— / -d381c462-a17f-4192-b694-66a7c3aaee4f |
| Jogador 5 | 6-1 | 601 | BUY | STABILIZE | 20.0 | 8 | 31 | 3 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13619156181812286 | 0.0 | 0.0 | +3b98edb7-348f-47b4-85fd-66ee3f1a7af5 / -— |
| Jogador 5 | 6-1 | 602 | REROLL | STABILIZE | 20.0 | 8 | 28 | 2 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 603 | SELL | STABILIZE | 20.0 | 8 | 26 | 2 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05127692222595215 | 0.0 | 0.0 | +— / -3b98edb7-348f-47b4-85fd-66ee3f1a7af5 |
| Jogador 5 | 6-1 | 604 | BUY | STABILIZE | 20.0 | 8 | 29 | 2 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8165587782859802 | 0.0 | 0.0 | +703b70a3-3aca-4ecd-86da-0a1b34e4bb3a / -— |
| Jogador 5 | 6-1 | 605 | SELL | STABILIZE | 20.0 | 8 | 25 | 2 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07082153856754303 | 0.0 | 0.0 | +— / -99857cfa-b422-4167-bb01-d9fd94a55d88 |
| Jogador 5 | 6-1 | 606 | BUY | STABILIZE | 20.0 | 8 | 26 | 2 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8883883953094482 | 0.0 | 0.0 | +b9b2c784-d8ee-4a31-978f-58a686f22af2 / -703b70a3-3aca-4ecd-86da-0a1b34e4bb3a,c5f81113-0e4a-4d08-beab-f19d808ef10c |
| Jogador 5 | 6-1 | 607 | PASS | STABILIZE | 20.0 | 8 | 22 | 2 | 56.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15333333611488342 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 611 | BUY | STABILIZE | 20.0 | 8 | 30 | 3 | 56.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8230910897254944 | 0.0 | 0.0 | +5268c681-31fe-4973-9d93-cd1413b64383 / -— |
| Jogador 5 | 6-2 | 612 | BUY | STABILIZE | 20.0 | 8 | 27 | 2 | 56.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.74298495054245 | 0.0 | 0.0 | +f074442b-5ccc-4174-ac90-ef9eb358f8c1 / -— |
| Jogador 5 | 6-2 | 613 | REROLL | STABILIZE | 20.0 | 8 | 23 | 2 | 56.0 | Defendente/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 614 | SELL | STABILIZE | 20.0 | 8 | 21 | 2 | 56.0 | Defendente/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05471076816320419 | 0.0 | 0.0 | +— / -b9b2c784-d8ee-4a31-978f-58a686f22af2 |
| Jogador 5 | 6-2 | 615 | BUY | STABILIZE | 20.0 | 8 | 32 | 3 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.873975932598114 | 0.0 | 0.0 | +7c0c0d58-bcc6-4872-a709-8dd702f67800 / -33e9808b-2f92-49e7-ac35-1f6f9388edef,4accaece-f84d-43da-967c-8c733bb95174 |
| Jogador 5 | 6-2 | 616 | BUY | STABILIZE | 20.0 | 8 | 29 | 2 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.845533013343811 | 0.0 | 0.0 | +eb0046fd-392b-47c4-add2-fc669b031a3c / -— |
| Jogador 5 | 6-2 | 617 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 27 | 2 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.5662280172109604e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 618 | MOVE_BENCH | STABILIZE | 20.0 | 8 | 27 | 2 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5847062468528748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 619 | BUY | STABILIZE | 20.0 | 8 | 27 | 2 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03466171398758888 | 0.0 | 0.0 | +6f89a47a-1ab1-48ed-ba66-bcbaa3e74231 / -— |
| Jogador 5 | 6-2 | 620 | REROLL | STABILIZE | 20.0 | 8 | 22 | 2 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 622 | SELL | STABILIZE | 20.0 | 8 | 29 | 2 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11900000274181366 | 0.0 | 0.0 | +— / -7c0c0d58-bcc6-4872-a709-8dd702f67800 |
| Jogador 5 | 6-3 | 623 | BUY | STABILIZE | 20.0 | 8 | 37 | 3 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9539840817451477 | 0.0 | 0.0 | +530cb5ca-dea2-47db-ba63-38133c49eb12 / -5268c681-31fe-4973-9d93-cd1413b64383,b57fc469-d037-4ac4-9e70-645f71fb6399 |
| Jogador 5 | 6-3 | 624 | BUY | STABILIZE | 20.0 | 8 | 34 | 3 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14607220888137817 | 0.0 | 0.0 | +dbe39ade-b405-44db-9289-c7dd9e840754 / -— |
| Jogador 5 | 6-3 | 625 | MOVE_BENCH | STABILIZE | 20.0 | 8 | 29 | 2 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4900670051574707 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 626 | BUY | STABILIZE | 20.0 | 8 | 29 | 2 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07533051073551178 | 0.0 | 0.0 | +52c442e6-4e35-4e6f-8887-eff560f7b259 / -— |
| Jogador 5 | 6-3 | 627 | REROLL | STABILIZE | 20.0 | 8 | 25 | 2 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 628 | SELL | STABILIZE | 20.0 | 8 | 23 | 2 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -52c442e6-4e35-4e6f-8887-eff560f7b259 |
| Jogador 5 | 6-3 | 629 | BUY | STABILIZE | 20.0 | 8 | 27 | 2 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3070743978023529 | 0.0 | 0.0 | +94f20892-cf66-4256-9159-a295f6054b8f / -— |
| Jogador 5 | 6-3 | 630 | REROLL | STABILIZE | 20.0 | 8 | 23 | 2 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 631 | SELL | STABILIZE | 20.0 | 8 | 21 | 2 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3058857023715973 | 0.0 | 0.0 | +— / -530cb5ca-dea2-47db-ba63-38133c49eb12 |
| Jogador 5 | 6-3 | 632 | PASS | STABILIZE | 20.0 | 8 | 29 | 2 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17177778482437134 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 634 | BUY | STABILIZE | 20.0 | 8 | 37 | 3 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3898938298225403 | 0.0 | 0.0 | +22f5b2d1-9395-4a0a-9c44-b1dacd066c63 / -— |
| Jogador 5 | 6-4 | 635 | SELL | STABILIZE | 20.0 | 8 | 34 | 3 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07447692006826401 | 0.0 | 0.0 | +— / -a960f5cb-d806-4d73-9146-244e1ecde6f2 |
| Jogador 5 | 6-4 | 636 | BUY | STABILIZE | 20.0 | 8 | 39 | 3 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9350307583808899 | 0.0 | 0.0 | +4dd42303-55f8-4677-9669-f8f7ecf895ae / -8486b8a9-20fe-4234-bbba-0efa031c3b76,f074442b-5ccc-4174-ac90-ef9eb358f8c1 |
| Jogador 5 | 6-4 | 637 | BUY | STABILIZE | 20.0 | 8 | 35 | 3 | 52.0 | Defendente/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2219841182231903 | 0.0 | 0.0 | +e50e0ccc-eb5c-46e0-9049-d5c4d8ea471e / -— |
| Jogador 5 | 6-4 | 638 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 31 | 3 | 52.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 639 | MOVE_BENCH | STABILIZE | 20.0 | 8 | 31 | 3 | 52.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5441679954528809 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 640 | BUY | STABILIZE | 20.0 | 8 | 31 | 3 | 60.0 | Defendente/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009087523445487022 | 0.0 | 0.0 | +2900e5fd-1259-430c-ba65-d6a6122b6a08 / -— |
| Jogador 5 | 6-4 | 641 | REROLL | STABILIZE | 20.0 | 8 | 28 | 2 | 60.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 642 | SELL | STABILIZE | 20.0 | 8 | 26 | 2 | 60.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06830225884914398 | 0.0 | 0.0 | +— / -2900e5fd-1259-430c-ba65-d6a6122b6a08 |
| Jogador 5 | 6-4 | 643 | BUY | STABILIZE | 20.0 | 8 | 29 | 2 | 60.0 | Defendente/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7034054398536682 | 0.0 | 0.0 | +ae36e82c-bcac-4ad8-b7b1-063966ecc411 / -— |
| Jogador 5 | 6-5 | 645 | SELL | STABILIZE | 20.0 | 8 | 32 | 3 | 60.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08263076841831207 | 0.0 | 0.0 | +— / -e50e0ccc-eb5c-46e0-9049-d5c4d8ea471e |
| Jogador 5 | 6-5 | 646 | BUY | STABILIZE | 20.0 | 8 | 36 | 3 | 60.0 | Defendente/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1630675047636032 | 0.0 | 0.0 | +8b7968ee-f664-4b2a-b9e8-9b0ad6e81d79 / -— |
| Jogador 5 | 6-5 | 647 | SELL | STABILIZE | 20.0 | 8 | 33 | 3 | 60.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06050769239664078 | 0.0 | 0.0 | +— / -8b7968ee-f664-4b2a-b9e8-9b0ad6e81d79 |
| Jogador 5 | 6-5 | 648 | BUY | STABILIZE | 20.0 | 8 | 36 | 3 | 60.0 | Defendente/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5542470216751099 | 0.0 | 0.0 | +d6d15e43-3f39-40c6-8a07-a05854ef835d / -— |
| Jogador 5 | 6-5 | 649 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 34 | 3 | 60.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 650 | REROLL | STABILIZE | 20.0 | 8 | 34 | 3 | 60.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 651 | SELL | STABILIZE | 20.0 | 8 | 32 | 3 | 60.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12167692184448242 | 0.0 | 0.0 | +— / -d6d15e43-3f39-40c6-8a07-a05854ef835d |
| Jogador 5 | 6-6 | 653 | BUY | STABILIZE | 20.0 | 8 | 43 | 4 | 60.0 | Defendente/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19327835738658905 | 0.0 | 0.0 | +54779dda-333a-4f96-a05f-350c5c303a9c / -— |
| Jogador 5 | 6-6 | 654 | SELL | STABILIZE | 20.0 | 8 | 38 | 3 | 60.0 | Defendente/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018335308879613876 | 0.0 | 0.0 | +— / -4dd42303-55f8-4677-9669-f8f7ecf895ae |
| Jogador 5 | 6-6 | 655 | BUY | STABILIZE | 20.0 | 8 | 49 | 4 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24081724882125854 | 0.0 | 0.0 | +30adc860-f40e-4899-b3fe-a5fefb4a472a / -— |
| Jogador 5 | 6-6 | 656 | REROLL | STABILIZE | 20.0 | 8 | 46 | 4 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 657 | SELL | STABILIZE | 20.0 | 8 | 44 | 4 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04965873807668686 | 0.0 | 0.0 | +— / -30adc860-f40e-4899-b3fe-a5fefb4a472a |
| Jogador 5 | 6-6 | 658 | BUY | STABILIZE | 20.0 | 8 | 47 | 4 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7879277467727661 | 0.0 | 0.0 | +cd89b8b5-89d4-4703-94b5-930bf6deebb0 / -— |
| Jogador 5 | 6-6 | 659 | REROLL | STABILIZE | 20.0 | 8 | 46 | 4 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 660 | SELL | STABILIZE | 20.0 | 8 | 44 | 4 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23979385197162628 | 0.0 | 0.0 | +— / -af23c553-04de-4813-87d0-bb7e4becafe4 |
| Jogador 5 | 6-7 | 662 | BUY | STABILIZE | 20.0 | 8 | 55 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12077067047357559 | 0.0 | 0.0 | +184fd23e-e7de-4450-b114-831f6a9e8251 / -— |
| Jogador 5 | 6-7 | 663 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 50 | 5 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-7 | 664 | MOVE_BOARD | STABILIZE | 20.0 | 8 | 50 | 5 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015038996003568172 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-7 | 665 | PASS | STABILIZE | 20.0 | 8 | 50 | 5 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14933332800865173 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 672 | EQUIP_FROM_INVENTORY | STABILIZE | 20.0 | 8 | 61 | 5 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 673 | SELL | STABILIZE | 20.0 | 8 | 61 | 5 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04603999853134155 | 0.0 | 0.0 | +— / -cd89b8b5-89d4-4703-94b5-930bf6deebb0 |
| Jogador 5 | 7-1 | 674 | BUY | STABILIZE | 20.0 | 8 | 62 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9261998534202576 | 0.0 | 0.0 | +31f86c34-a81d-4ba0-9136-c9106b0fbec5 / -— |
| Jogador 5 | 7-1 | 675 | MOVE_BENCH | STABILIZE | 20.0 | 8 | 58 | 5 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07456403970718384 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 676 | REROLL | STABILIZE | 20.0 | 8 | 58 | 5 | 62.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 677 | SELL | STABILIZE | 20.0 | 8 | 56 | 5 | 62.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -184fd23e-e7de-4450-b114-831f6a9e8251 |
| Jogador 5 | 7-1 | 678 | BUY | STABILIZE | 20.0 | 8 | 61 | 5 | 62.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11537124216556549 | 0.0 | 0.0 | +48db898e-cf31-47c7-aab7-fd47be1938a1 / -— |
| Jogador 5 | 7-1 | 679 | SELL | STABILIZE | 20.0 | 8 | 57 | 5 | 62.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05986153706908226 | 0.0 | 0.0 | +— / -48db898e-cf31-47c7-aab7-fd47be1938a1 |
| Jogador 5 | 7-1 | 680 | BUY | STABILIZE | 20.0 | 8 | 61 | 5 | 62.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16451005637645721 | 0.0 | 0.0 | +97dab4e7-7d36-411a-b756-07231aa5fe03 / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +5fb26eae-800c-4f7a-8caa-e94d36794159 / -— |
| Jogador 6 | 1-1 | 3 | SELL | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | -0.5991230607032776 | 0.0 | 0.0 | +— / -5fb26eae-800c-4f7a-8caa-e94d36794159 |
| Jogador 6 | 1-1 | 4 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 5 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6106581687927246 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 6 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.01072696503251791 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 7 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2651718258857727 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 32 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1288224756717682 | 0.0 | 0.0 | +— / -425b1e77-5887-40b3-875e-c1f60dc6c513 |
| Jogador 6 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2664465010166168 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1715412437915802 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 35 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.283282071352005 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 36 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4290271997451782 | 0.0 | 0.0 | +— / -3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 1-2 | 37 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.19463565945625305 | 0.0 | 0.0 | +c733a654-69b5-4b02-979e-21ef1dd5d04b / -— |
| Jogador 6 | 1-2 | 38 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3976670205593109 | 0.0 | 0.0 | +— / -c733a654-69b5-4b02-979e-21ef1dd5d04b |
| Jogador 6 | 1-2 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0002887017617467791 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 40 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.07116799801588058 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 58 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.07027789950370789 | 0.0 | 0.0 | +f29b0444-8dd6-44a6-9a04-824febf737a0 / -— |
| Jogador 6 | 1-3 | 60 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Caitlyn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -f29b0444-8dd6-44a6-9a04-824febf737a0 |
| Jogador 6 | 1-3 | 61 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2731436789035797 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 62 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 79 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4167895019054413 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 83 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09107298403978348 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.752895712852478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 85 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050473909825086594 | 0.0 | 0.0 | +— / -9002992e-4dcd-4fec-939c-87393464a41d |
| Jogador 6 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2193932682275772 | 0.0 | 0.0 | +4fe99bfe-6eaa-4a36-b06e-60005fb92d30 / -— |
| Jogador 6 | 1-4 | 87 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009552054107189178 | 0.0 | 0.0 | +— / -4fe99bfe-6eaa-4a36-b06e-60005fb92d30 |
| Jogador 6 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2216135561466217 | 0.0 | 0.0 | +66f2e88b-7964-4bbe-a320-941bba893d3d / -— |
| Jogador 6 | 1-4 | 89 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009748236276209354 | 0.0 | 0.0 | +— / -66f2e88b-7964-4bbe-a320-941bba893d3d |
| Jogador 6 | 1-4 | 90 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 91 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 106 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3310193717479706 | 0.0 | 0.0 | +c8b72b14-11a4-48e6-8135-41efdbc347cb / -— |
| Jogador 6 | 2-1 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5369076728820801 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 108 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.38183945417404175 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 109 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1026465967297554 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 110 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13244496285915375 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004366036970168352 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 112 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04094364866614342 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-1 | 113 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3822813332080841 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 114 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0011895991628989577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 115 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 127 | SELL | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10068861395120621 | 0.0 | 0.0 | +— / -185ee377-0917-4209-905b-9486d5be0193 |
| Jogador 6 | 2-2 | 128 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31896883249282837 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 129 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3186202347278595 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 130 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 131 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4516366124153137 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 132 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Tristana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 152 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0360846519470215 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 153 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.054265666753053665 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 154 | SELL | SLOWROLL | 95.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12760049104690552 | 0.0 | 0.0 | +— / -c19cf6a8-c66e-4670-b0fc-fb83453f22e7 |
| Jogador 6 | 2-3 | 155 | BUY | SLOWROLL | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07548168301582336 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 156 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3983446955680847 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 157 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 158 | PASS | SLOWROLL | 95.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 176 | SELL | SLOWROLL | 90.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6042029857635498 | 0.0 | 0.0 | +— / -c8b72b14-11a4-48e6-8135-41efdbc347cb |
| Jogador 6 | 2-4 | 177 | EQUIP_FROM_INVENTORY | STABILIZE | 90.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06996548175811768 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 178 | EQUIP_FROM_INVENTORY | STABILIZE | 90.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09117859601974487 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 179 | BUY | STABILIZE | 90.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.953097939491272 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 180 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 181 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06207899749279022 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 182 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014878788031637669 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 183 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01606055535376072 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 184 | PASS | SLOWROLL | 90.0 | 5 | 7 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 197 | SELL | SLOWROLL | 90.0 | 5 | 12 | 1 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04184025898575783 | 0.0 | 0.0 | +— / -908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-5 | 198 | BUY | SLOWROLL | 90.0 | 5 | 13 | 1 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.278478741645813 | 0.0 | 0.0 | +f957e607-dd51-492b-9186-252da4e0c12f / -— |
| Jogador 6 | 2-5 | 199 | SELL | SLOWROLL | 90.0 | 5 | 12 | 1 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1040399968624115 | 0.0 | 0.0 | +— / -f957e607-dd51-492b-9186-252da4e0c12f |
| Jogador 6 | 2-5 | 200 | BUY | SLOWROLL | 90.0 | 5 | 13 | 1 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03698376566171646 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 201 | BUY_XP | SLOWROLL | 90.0 | 5 | 11 | 1 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 202 | BUY_XP | SLOWROLL | 90.0 | 5 | 7 | 0 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 203 | SELL | SLOWROLL | 90.0 | 5 | 3 | 0 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09384586662054062 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 204 | BUY_XP | SLOWROLL | 90.0 | 5 | 5 | 0 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 205 | PASS | SLOWROLL | 90.0 | 5 | 1 | 0 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 217 | BUY | SLOWROLL | 90.0 | 6 | 7 | 0 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0022253026254475117 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 218 | MOVE_BENCH | SLOWROLL | 90.0 | 6 | 4 | 0 | 24.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05393442511558533 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 219 | MOVE_BENCH | FAST8 | 90.0 | 6 | 4 | 0 | 26.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.386186420917511 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 220 | BUY | FAST8 | 90.0 | 6 | 4 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20432381331920624 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 221 | MOVE_BOARD | FAST8 | 90.0 | 6 | 1 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 222 | MOVE_BOARD | FAST8 | 90.0 | 6 | 1 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014303102158010006 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 223 | PASS | FAST8 | 90.0 | 6 | 1 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 235 | SELL | FAST8 | 90.0 | 6 | 8 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034564703702926636 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-7 | 236 | BUY | FAST8 | 90.0 | 6 | 11 | 1 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12406092882156372 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 237 | SELL | FAST8 | 90.0 | 6 | 8 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3344748020172119 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 238 | BUY | FAST8 | 90.0 | 6 | 11 | 1 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04472436010837555 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 239 | MOVE_BOARD | FAST8 | 90.0 | 6 | 8 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.063377365237102e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 240 | BUY_XP | FAST8 | 90.0 | 6 | 8 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 241 | BUY_XP | FAST8 | 90.0 | 6 | 4 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 242 | MOVE_BENCH | FAST8 | 90.0 | 6 | 0 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005021241493523121 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 243 | MOVE_BOARD | FAST8 | 90.0 | 6 | 0 | 0 | 32.0 | Sabugueiro/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 244 | MOVE_BENCH | FAST8 | 90.0 | 6 | 0 | 0 | 32.0 | Sabugueiro/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4148973822593689 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 245 | PASS | FAST8 | 90.0 | 6 | 0 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 254 | MOVE_BENCH | FAST8 | 90.0 | 6 | 6 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0999150276184082 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 255 | MOVE_BENCH | FAST8 | 90.0 | 6 | 6 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6466132402420044 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 256 | SELL | FAST8 | 90.0 | 6 | 6 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.009037199430167675 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-1 | 257 | BUY | FAST8 | 90.0 | 6 | 9 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.21356093883514404 | 0.0 | 0.0 | +91f05e8c-f467-4f22-9cb0-c814ffa93198 / -— |
| Jogador 6 | 3-1 | 258 | MOVE_BENCH | FAST8 | 90.0 | 6 | 7 | 0 | 30.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3949349820613861 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 259 | MOVE_BENCH | FAST8 | 90.0 | 6 | 7 | 0 | 28.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08326065540313721 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 260 | CRAFT_AND_EQUIP | FAST8 | 90.0 | 6 | 7 | 0 | 28.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24258458614349365 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 261 | BUY_XP | FAST8 | 90.0 | 6 | 7 | 0 | 28.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 262 | SELL | FAST8 | 90.0 | 6 | 3 | 0 | 28.0 | Sabugueiro/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12608134746551514 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 3-1 | 263 | BUY | FAST8 | 90.0 | 6 | 6 | 0 | 28.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2791838049888611 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 264 | PASS | FAST8 | 90.0 | 6 | 2 | 0 | 28.0 | Sabugueiro/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 272 | SELL | FAST8 | 80.0 | 6 | 7 | 0 | 28.0 | Sabugueiro/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015163714997470379 | 0.0 | 0.0 | +— / -4eedd873-e4ec-41e5-9f5e-48e443e80f86 |
| Jogador 6 | 3-2 | 273 | BUY | FAST8 | 80.0 | 6 | 11 | 1 | 28.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5537629723548889 | 0.0 | 0.0 | +6e096b30-0b49-4a98-8596-8b05089793ae / -— |
| Jogador 6 | 3-2 | 274 | MOVE_BENCH | FAST8 | 80.0 | 6 | 8 | 0 | 28.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7489871978759766 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 275 | MOVE_BENCH | FAST8 | 80.0 | 6 | 8 | 0 | 30.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4090973436832428 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 276 | PASS | FAST8 | 80.0 | 6 | 8 | 0 | 28.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 292 | MOVE_BENCH | FAST8 | 70.0 | 6 | 14 | 1 | 28.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09936994314193726 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 293 | MOVE_BENCH | FAST8 | 70.0 | 6 | 14 | 1 | 28.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 294 | MOVE_BENCH | FAST8 | 70.0 | 6 | 14 | 1 | 28.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6535558104515076 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 295 | PASS | FAST8 | 70.0 | 6 | 14 | 1 | 28.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 312 | MOVE_BENCH | FAST8 | 70.0 | 6 | 21 | 2 | 28.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09936347603797913 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 313 | MOVE_BENCH | FAST8 | 70.0 | 6 | 21 | 2 | 28.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 314 | MOVE_BENCH | FAST8 | 70.0 | 6 | 21 | 2 | 28.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7569478154182434 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 315 | PASS | FAST8 | 70.0 | 6 | 21 | 2 | 30.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05900000035762787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 332 | MOVE_BENCH | FAST8 | 70.0 | 6 | 28 | 2 | 30.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07514793425798416 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 333 | MOVE_BENCH | FAST8 | 70.0 | 6 | 28 | 2 | 28.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6543236970901489 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 334 | MOVE_BENCH | FAST8 | 70.0 | 6 | 28 | 2 | 28.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05002722516655922 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 335 | SELL | FAST8 | 70.0 | 6 | 28 | 2 | 30.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07455204427242279 | 0.0 | 0.0 | +— / -91f05e8c-f467-4f22-9cb0-c814ffa93198 |
| Jogador 6 | 3-5 | 336 | BUY | FAST8 | 70.0 | 6 | 30 | 3 | 30.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16789445281028748 | 0.0 | 0.0 | +9443e3b5-f0a2-4ab7-8378-907a3d2bccaa / -— |
| Jogador 6 | 3-5 | 337 | SELL | FAST8 | 70.0 | 6 | 28 | 2 | 30.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07455126196146011 | 0.0 | 0.0 | +— / -9443e3b5-f0a2-4ab7-8378-907a3d2bccaa |
| Jogador 6 | 3-5 | 338 | BUY | FAST8 | 70.0 | 6 | 30 | 3 | 30.0 | Sabugueiro/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.06134863570332527 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 339 | BUY_XP | FAST8 | 70.0 | 6 | 27 | 2 | 30.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 340 | BUY_XP | FAST8 | 70.0 | 6 | 23 | 2 | 30.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 341 | BUY_XP | FAST8 | 70.0 | 6 | 19 | 1 | 30.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08860000222921371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 342 | PASS | FAST8 | 70.0 | 7 | 15 | 1 | 30.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0560000017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 352 | MOVE_BENCH | FAST8 | 58.0 | 7 | 21 | 2 | 30.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4057629704475403 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 353 | BUY | FAST8 | 58.0 | 7 | 21 | 2 | 36.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.050161637365818024 | 0.0 | 0.0 | +a1aa0280-2379-4d0b-a475-143c1a2f6c25 / -— |
| Jogador 6 | 3-6 | 354 | BUY | FAST8 | 58.0 | 7 | 18 | 1 | 36.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012311968952417374 | 0.0 | 0.0 | +69ccc61a-403b-4025-8359-b2061dc6ad10 / -— |
| Jogador 6 | 3-6 | 355 | BUY_XP | FAST8 | 58.0 | 7 | 15 | 1 | 36.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 356 | BUY_XP | FAST8 | 58.0 | 7 | 11 | 1 | 36.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 357 | BUY_XP | FAST8 | 58.0 | 7 | 7 | 0 | 36.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 358 | PASS | FAST8 | 58.0 | 7 | 3 | 0 | 36.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 371 | BUY | FAST8 | 58.0 | 7 | 9 | 0 | 36.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20974501967430115 | 0.0 | 0.0 | +75d9034d-80ed-40d3-a330-44554cc2bb9e / -— |
| Jogador 6 | 3-7 | 372 | BUY | FAST8 | 58.0 | 7 | 4 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09330525994300842 | 0.0 | 0.0 | +8ff9f97f-9d27-44d5-ae97-a6d618c568a1 / -— |
| Jogador 6 | 3-7 | 373 | MOVE_BOARD | FAST8 | 58.0 | 7 | 0 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.744241106091067e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 374 | MOVE_BOARD | FAST8 | 58.0 | 7 | 0 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 375 | PASS | FAST8 | 58.0 | 7 | 0 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 390 | BUY | FAST8 | 58.0 | 7 | 5 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7609997987747192 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -2938180d-94e5-4bb7-832e-baa51f820ba2,6e096b30-0b49-4a98-8596-8b05089793ae |
| Jogador 6 | 4-1 | 391 | MOVE_BENCH | STABILIZE | 58.0 | 7 | 2 | 0 | 24.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.39934849739074707 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 392 | MOVE_BENCH | STABILIZE | 58.0 | 7 | 2 | 0 | 24.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.32845965027809143 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 393 | MOVE_BENCH | FAST8 | 58.0 | 7 | 2 | 0 | 30.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.38862255215644836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 394 | BUY | FAST8 | 58.0 | 7 | 2 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2139013111591339 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 6 | 4-1 | 395 | MOVE_BOARD | FAST8 | 58.0 | 7 | 0 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.012705466710031033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 396 | MOVE_BOARD | FAST8 | 58.0 | 7 | 0 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.004341583698987961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 397 | PASS | FAST8 | 58.0 | 7 | 0 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 402 | BUY | FAST8 | 58.0 | 7 | 7 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0886283740401268 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 6 | 4-2 | 403 | MOVE_BENCH | FAST8 | 58.0 | 7 | 3 | 0 | 36.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.019701998680830002 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 404 | BUY | FAST8 | 58.0 | 7 | 3 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21393385529518127 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-2 | 405 | CRAFT_AND_EQUIP | FAST8 | 58.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12551262974739075 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 406 | CRAFT_AND_EQUIP | FAST8 | 58.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07882995903491974 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 407 | MOVE_BOARD | FAST8 | 58.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 408 | MOVE_BOARD | FAST8 | 58.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014961476437747478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 409 | PASS | FAST8 | 58.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 422 | BUY | FAST8 | 45.0 | 7 | 6 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.733649730682373 | 0.0 | 0.0 | +9d2d95f2-c079-43eb-a4cd-37b224a473a8 / -— |
| Jogador 6 | 4-3 | 423 | BUY | FAST8 | 45.0 | 7 | 4 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012772220186889172 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 6 | 4-3 | 424 | MOVE_BOARD | FAST8 | 45.0 | 7 | 0 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012871279614046216 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 425 | MOVE_BOARD | FAST8 | 45.0 | 7 | 0 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0146390525624156 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 426 | PASS | FAST8 | 45.0 | 7 | 0 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 438 | BUY | STABILIZE | 33.0 | 7 | 6 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28718143701553345 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -— |
| Jogador 6 | 4-4 | 439 | REROLL | STABILIZE | 33.0 | 7 | 5 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 440 | SELL | STABILIZE | 33.0 | 7 | 3 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04374641925096512 | 0.0 | 0.0 | +— / -a1aa0280-2379-4d0b-a475-143c1a2f6c25 |
| Jogador 6 | 4-4 | 441 | BUY | STABILIZE | 33.0 | 7 | 6 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2594490945339203 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 6 | 4-4 | 442 | REROLL | STABILIZE | 33.0 | 7 | 3 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 443 | SELL | STABILIZE | 33.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08100000023841858 | 0.0 | 0.0 | +— / -755060be-13bb-4686-9ee9-e53fef2d75b2 |
| Jogador 6 | 4-4 | 444 | BUY | STABILIZE | 33.0 | 7 | 4 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7743605375289917 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 6 | 4-4 | 445 | MOVE_BOARD | STABILIZE | 33.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 446 | MOVE_BOARD | STABILIZE | 33.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 447 | PASS | STABILIZE | 33.0 | 7 | 1 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 452 | SELL | STABILIZE | 33.0 | 7 | 7 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024870770052075386 | 0.0 | 0.0 | +— / -fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 6 | 4-5 | 453 | BUY | STABILIZE | 33.0 | 7 | 15 | 1 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8347975015640259 | 0.0 | 0.0 | +55cd39c0-65d5-410e-917e-501f584115fa / -9d2d95f2-c079-43eb-a4cd-37b224a473a8,d9fdb961-a3e3-4e39-9970-e46ffd59fc3b |
| Jogador 6 | 4-5 | 454 | BUY | STABILIZE | 33.0 | 7 | 13 | 1 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04519543796777725 | 0.0 | 0.0 | +c7a7408a-e7bd-428d-9935-4d5a002d8d9f / -— |
| Jogador 6 | 4-5 | 455 | BUY | STABILIZE | 33.0 | 7 | 10 | 1 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1393207162618637 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 6 | 4-5 | 456 | REROLL | STABILIZE | 33.0 | 7 | 7 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 457 | SELL | STABILIZE | 33.0 | 7 | 5 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05976923182606697 | 0.0 | 0.0 | +— / -98b600a1-736b-437d-a69e-8a7f7235d9c3 |
| Jogador 6 | 4-5 | 458 | BUY | STABILIZE | 33.0 | 7 | 8 | 0 | 38.0 | Sabugueiro/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8338295221328735 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1,a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 4-5 | 459 | MOVE_BENCH | STABILIZE | 33.0 | 7 | 5 | 0 | 26.0 | Sabugueiro/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40740275382995605 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 460 | BUY | STABILIZE | 33.0 | 7 | 5 | 0 | 38.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7518047094345093 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 6 | 4-5 | 461 | REROLL | STABILIZE | 33.0 | 7 | 2 | 0 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 462 | PASS | STABILIZE | 33.0 | 7 | 0 | 0 | 38.0 | Sabugueiro/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 467 | SELL | STABILIZE | 21.0 | 7 | 6 | 0 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14586976170539856 | 0.0 | 0.0 | +— / -d78561b4-3dcc-42fb-9983-2ed5d62f8606 |
| Jogador 6 | 4-6 | 468 | BUY | STABILIZE | 21.0 | 7 | 9 | 0 | 38.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8339043259620667 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4,80130f72-2d7c-49db-8d6f-4c0a962260e8 |
| Jogador 6 | 4-6 | 469 | BUY | STABILIZE | 21.0 | 7 | 6 | 0 | 32.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28385815024375916 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -— |
| Jogador 6 | 4-6 | 470 | MOVE_BENCH | STABILIZE | 21.0 | 7 | 3 | 0 | 32.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35080552101135254 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 471 | BUY | STABILIZE | 21.0 | 7 | 3 | 0 | 44.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.807959794998169 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 6 | 4-6 | 472 | MOVE_BOARD | STABILIZE | 21.0 | 7 | 2 | 0 | 44.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 473 | REROLL | STABILIZE | 21.0 | 7 | 2 | 0 | 44.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 474 | MOVE_BOARD | STABILIZE | 21.0 | 7 | 0 | 0 | 44.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 475 | MOVE_BOARD | STABILIZE | 21.0 | 7 | 0 | 0 | 44.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014031526632606983 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 476 | PASS | STABILIZE | 21.0 | 7 | 0 | 0 | 44.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 477 | MOVE_BENCH | STABILIZE | 21.0 | 7 | 0 | 0 | 44.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4007883369922638 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 482 | BUY | ALL_IN | 9.0 | 7 | 6 | 0 | 50.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028478480875492096 | 0.0 | 0.0 | +987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 / -— |
| Jogador 6 | 4-7 | 483 | REROLL | ALL_IN | 9.0 | 7 | 3 | 0 | 50.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 484 | SELL | ALL_IN | 9.0 | 7 | 1 | 0 | 50.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06050769239664078 | 0.0 | 0.0 | +— / -987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 |
| Jogador 6 | 4-7 | 485 | BUY | ALL_IN | 9.0 | 7 | 4 | 0 | 50.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.827986478805542 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,7a48aa2d-a43b-4e49-8230-77f4f2860cb2 |
| Jogador 6 | 4-7 | 486 | BUY | ALL_IN | 9.0 | 7 | 3 | 0 | 48.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7545793652534485 | 0.0 | 0.0 | +0c96798c-ee23-488b-974f-74e8e3da6aa6 / -— |
| Jogador 6 | 4-7 | 487 | MOVE_BOARD | ALL_IN | 9.0 | 7 | 0 | 0 | 48.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0003817154502030462 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 488 | MOVE_BOARD | ALL_IN | 9.0 | 7 | 0 | 0 | 48.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 489 | MOVE_BOARD | ALL_IN | 9.0 | 7 | 0 | 0 | 48.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 490 | PASS | ALL_IN | 9.0 | 7 | 0 | 0 | 48.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 492 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 0 | 0 | 48.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5996841192245483 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 499 | BUY | ALL_IN | 9.0 | 7 | 6 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7916423678398132 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 6 | 5-1 | 500 | CRAFT_AND_EQUIP | ALL_IN | 9.0 | 7 | 5 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09705184400081635 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 501 | CRAFT_AND_EQUIP | ALL_IN | 9.0 | 7 | 5 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1337098628282547 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 502 | REROLL | ALL_IN | 9.0 | 7 | 5 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 503 | REROLL | ALL_IN | 9.0 | 7 | 3 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 504 | MOVE_BOARD | ALL_IN | 9.0 | 7 | 1 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001057083354680799 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 505 | MOVE_BOARD | ALL_IN | 9.0 | 7 | 1 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 506 | PASS | ALL_IN | 9.0 | 7 | 1 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 512 | REROLL | ALL_IN | 9.0 | 7 | 7 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 513 | REROLL | ALL_IN | 9.0 | 7 | 5 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 514 | SELL | ALL_IN | 9.0 | 7 | 3 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1454601138830185 | 0.0 | 0.0 | +— / -0c96798c-ee23-488b-974f-74e8e3da6aa6 |
| Jogador 6 | 5-2 | 515 | BUY | ALL_IN | 9.0 | 7 | 6 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27580726146698 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 6 | 5-2 | 516 | REROLL | ALL_IN | 9.0 | 7 | 4 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 517 | SELL | ALL_IN | 9.0 | 7 | 2 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15773771703243256 | 0.0 | 0.0 | +— / -55cd39c0-65d5-410e-917e-501f584115fa |
| Jogador 6 | 5-2 | 518 | BUY | ALL_IN | 9.0 | 7 | 7 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7899388074874878 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -— |
| Jogador 6 | 5-2 | 519 | REROLL | ALL_IN | 9.0 | 7 | 2 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 520 | SELL | ALL_IN | 9.0 | 7 | 0 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06158461421728134 | 0.0 | 0.0 | +— / -111acae7-a889-409f-a15e-419d250fccd0 |
| Jogador 6 | 5-2 | 521 | BUY | ALL_IN | 9.0 | 7 | 4 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27798718214035034 | 0.0 | 0.0 | +663beb45-28d7-42de-b6b8-a81e8676f55f / -— |
| Jogador 6 | 5-2 | 522 | PASS | ALL_IN | 9.0 | 7 | 3 | 0 | 52.0 | Sabugueiro/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.010813108645379543 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0808350220322609 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15921883285045624 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 1.029914379119873 | 0.0 | 0.0 | +a529e9b4-89c2-47e0-b821-7269b112f8ef / -— |
| Jogador 7 | 1-2 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0019182112300768495 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 35 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.724852442741394 | 0.0 | 0.0 | +— / -a529e9b4-89c2-47e0-b821-7269b112f8ef |
| Jogador 7 | 1-2 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.1839684247970581 | 0.0 | 0.0 | +00a1ebb3-acfd-44df-9190-4f51a47d48c7 / -— |
| Jogador 7 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4098913371562958 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.24741895496845245 | 0.0 | 0.0 | +42edb83f-b613-45e2-95e2-d603ddf9d104 / -— |
| Jogador 7 | 1-3 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 59 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11742693930864334 | 0.0 | 0.0 | +— / -42edb83f-b613-45e2-95e2-d603ddf9d104 |
| Jogador 7 | 1-3 | 60 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.24492418766021729 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014677979052066803 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 63 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29548144340515137 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 84 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015796177089214325 | 0.0 | 0.0 | +— / -00a1ebb3-acfd-44df-9190-4f51a47d48c7 |
| Jogador 7 | 1-4 | 85 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23439829051494598 | 0.0 | 0.0 | +a179e7d4-31e2-4a74-9905-0daede16517e / -— |
| Jogador 7 | 1-4 | 86 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02201906405389309 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 87 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030503705143928528 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17326398193836212 | 0.0 | 0.0 | +f13ddeb7-2025-4413-9c31-be5e4f907fff / -— |
| Jogador 7 | 1-4 | 89 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3254615366458893 | 0.0 | 0.0 | +— / -f13ddeb7-2025-4413-9c31-be5e4f907fff |
| Jogador 7 | 1-4 | 90 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 106 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1732930690050125 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.42959335446357727 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 108 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1558547168970108 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 109 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14152906835079193 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 110 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13152796030044556 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.541065234458074e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 112 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4641275703907013 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 113 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05098002031445503 | 0.0 | 0.0 | +— / -c2a4318c-af60-41e2-8e14-c3ad967569a0 |
| Jogador 7 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20700842142105103 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 7 | 2-1 | 115 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0031538461335003376 | 0.0 | 0.0 | +— / -42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 7 | 2-1 | 116 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 127 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.25715482234954834 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09166020154953003 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 129 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 130 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 131 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0064229886047542095 | 0.0 | 0.0 | +— / -de82e676-8d8b-4437-958e-a8398a3cfade |
| Jogador 7 | 2-2 | 132 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.33640745282173157 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -— |
| Jogador 7 | 2-2 | 133 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 134 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0579538457095623 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 135 | BUY | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | 0.19806934893131256 | 0.0 | 0.0 | +5db33b7c-1844-4f4f-8317-ac08f66d4c1e / -— |
| Jogador 7 | 2-2 | 136 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3254615366458893 | 0.0 | 0.0 | +— / -5db33b7c-1844-4f4f-8317-ac08f66d4c1e |
| Jogador 7 | 2-2 | 137 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 152 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.031955599784851 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -— |
| Jogador 7 | 2-3 | 153 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0959211140871048 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 154 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38921767473220825 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 155 | BUY | SLOWROLL | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12600776553153992 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 156 | SELL | SLOWROLL | 100.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10161538422107697 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-3 | 157 | BUY | SLOWROLL | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13689671456813812 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 7 | 2-3 | 158 | BUY_XP | SLOWROLL | 100.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 159 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 160 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014880295842885971 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 161 | PASS | SLOWROLL | 100.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 176 | SELL | SLOWROLL | 100.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029227308928966522 | 0.0 | 0.0 | +— / -4367c039-e64e-4a3c-a49f-57cb2674a08f |
| Jogador 7 | 2-4 | 177 | BUY | SLOWROLL | 100.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2789350748062134 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 178 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 5 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0917995497584343 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 179 | SELL | SLOWROLL | 100.0 | 5 | 5 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028987079858779907 | 0.0 | 0.0 | +— / -734c75dd-d0f3-4b9f-abe8-a228e23557a2 |
| Jogador 7 | 2-4 | 180 | BUY | SLOWROLL | 100.0 | 5 | 7 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28903040289878845 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 181 | BUY_XP | SLOWROLL | 100.0 | 5 | 4 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 182 | PASS | ECON | 100.0 | 5 | 0 | 0 | 26.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 197 | MOVE_BENCH | ECON | 100.0 | 5 | 6 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36729687452316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 198 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08540935814380646 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 199 | SELL | STABILIZE | 100.0 | 5 | 6 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14149034023284912 | 0.0 | 0.0 | +— / -a179e7d4-31e2-4a74-9905-0daede16517e |
| Jogador 7 | 2-5 | 200 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.36586809158325195 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 201 | SELL | STABILIZE | 100.0 | 5 | 5 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15045230090618134 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 2-5 | 202 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.040548428893089294 | 0.0 | 0.0 | +1d709136-338f-4fef-90fc-b2aa1b83d879 / -— |
| Jogador 7 | 2-5 | 203 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 5 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39691510796546936 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 204 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 205 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 217 | BUY | FAST8 | 100.0 | 6 | 8 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9657316207885742 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 218 | MOVE_BENCH | FAST8 | 100.0 | 6 | 5 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5973259210586548 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 219 | SELL | FAST8 | 100.0 | 6 | 5 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37503838539123535 | 0.0 | 0.0 | +— / -2c7e844d-925a-43bb-8be8-65a71d11f964 |
| Jogador 7 | 2-6 | 220 | BUY | FAST8 | 100.0 | 6 | 8 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0009413957595825 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -3394d5fc-ee48-4a08-8669-05984c804b53,5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-6 | 221 | MOVE_BENCH | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09739740937948227 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 222 | MOVE_BENCH | FAST8 | 100.0 | 6 | 6 | 0 | 28.0 | Vanguarda/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6583306193351746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 223 | MOVE_BENCH | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Vanguarda/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08430761098861694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 224 | MOVE_BENCH | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15688732266426086 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 225 | MOVE_BOARD | FAST8 | 100.0 | 6 | 6 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.01497575081884861 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 226 | BUY | FAST8 | 100.0 | 6 | 6 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31722038984298706 | 0.0 | 0.0 | +19cba1be-95ae-4cf0-a600-0c5eb8d081b0 / -— |
| Jogador 7 | 2-6 | 227 | PASS | FAST8 | 100.0 | 6 | 4 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 235 | MOVE_BENCH | FAST8 | 93.0 | 6 | 9 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7043549418449402 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 236 | MOVE_BENCH | FAST8 | 93.0 | 6 | 9 | 0 | 30.0 | Vanguarda/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08498086780309677 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 237 | MOVE_BENCH | FAST8 | 93.0 | 6 | 9 | 0 | 32.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4148290455341339 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 238 | MOVE_BENCH | FAST8 | 93.0 | 6 | 9 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7704010009765625 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 239 | PASS | FAST8 | 93.0 | 6 | 9 | 0 | 32.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 251 | MOVE_BENCH | FAST8 | 93.0 | 6 | 9 | 0 | 32.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5703555941581726 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 254 | CRAFT_AND_EQUIP | FAST8 | 93.0 | 6 | 14 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.16312724351882935 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 255 | BUY | FAST8 | 93.0 | 6 | 14 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21155114471912384 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 256 | BUY_XP | FAST8 | 93.0 | 6 | 11 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 257 | BUY_XP | FAST8 | 93.0 | 6 | 7 | 0 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 258 | MOVE_BOARD | FAST8 | 93.0 | 6 | 3 | 0 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 259 | MOVE_BOARD | FAST8 | 93.0 | 6 | 3 | 0 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014972587116062641 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 260 | PASS | FAST8 | 93.0 | 6 | 3 | 0 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 272 | MOVE_BENCH | FAST8 | 93.0 | 6 | 9 | 0 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09962941706180573 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 273 | MOVE_BENCH | FAST8 | 93.0 | 6 | 9 | 0 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41459357738494873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 274 | MOVE_BENCH | FAST8 | 93.0 | 6 | 9 | 0 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7495312690734863 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 275 | PASS | FAST8 | 93.0 | 6 | 9 | 0 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 292 | MOVE_BENCH | FAST8 | 93.0 | 6 | 17 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.345925509929657 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 293 | MOVE_BENCH | FAST8 | 93.0 | 6 | 17 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3372915983200073 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 294 | PASS | FAST8 | 93.0 | 6 | 17 | 1 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 312 | SELL | FAST8 | 93.0 | 6 | 25 | 2 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16242678463459015 | 0.0 | 0.0 | +— / -19cba1be-95ae-4cf0-a600-0c5eb8d081b0 |
| Jogador 7 | 3-4 | 313 | BUY | FAST8 | 93.0 | 6 | 27 | 2 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7670682668685913 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 314 | MOVE_BENCH | FAST8 | 93.0 | 6 | 24 | 2 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09886534512042999 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 315 | MOVE_BENCH | FAST8 | 93.0 | 6 | 24 | 2 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08474704623222351 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 316 | MOVE_BENCH | FAST8 | 93.0 | 6 | 24 | 2 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41498637199401855 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 317 | MOVE_BENCH | FAST8 | 93.0 | 6 | 24 | 2 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 318 | PASS | FAST8 | 93.0 | 6 | 24 | 2 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 332 | MOVE_BENCH | FAST8 | 93.0 | 6 | 32 | 3 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09999046474695206 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 333 | MOVE_BENCH | FAST8 | 93.0 | 6 | 32 | 3 | 40.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6607131361961365 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 334 | SELL | FAST8 | 93.0 | 6 | 32 | 3 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.108249232172966 | 0.0 | 0.0 | +— / -a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 7 | 3-5 | 335 | EQUIP_FROM_INVENTORY | FAST8 | 93.0 | 6 | 37 | 3 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15567366778850555 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 336 | EQUIP_FROM_INVENTORY | FAST8 | 93.0 | 6 | 37 | 3 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13697555661201477 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 337 | BUY | FAST8 | 93.0 | 6 | 37 | 3 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8189589381217957 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -86c1ac55-598e-426a-86ea-64249f82b085,ad1693cd-1ab5-43a9-8164-25929b8bd68e |
| Jogador 7 | 3-5 | 338 | MOVE_BENCH | FAST8 | 93.0 | 6 | 34 | 3 | 26.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3445766270160675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 339 | MOVE_BOARD | FAST8 | 93.0 | 6 | 34 | 3 | 38.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 340 | MOVE_BOARD | FAST8 | 93.0 | 6 | 34 | 3 | 38.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 341 | PASS | FAST8 | 93.0 | 6 | 34 | 3 | 38.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.125 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 352 | BUY | FAST8 | 93.0 | 6 | 44 | 4 | 38.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07099879533052444 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 7 | 3-6 | 353 | MOVE_BENCH | FAST8 | 93.0 | 6 | 40 | 4 | 38.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40279310941696167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 354 | BUY | FAST8 | 93.0 | 6 | 40 | 4 | 46.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6795406341552734 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 7 | 3-6 | 355 | BUY_XP | FAST8 | 93.0 | 6 | 36 | 3 | 46.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 356 | BUY_XP | FAST8 | 93.0 | 6 | 32 | 3 | 46.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 357 | BUY_XP | FAST8 | 93.0 | 6 | 28 | 2 | 46.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 358 | BUY_XP | FAST8 | 93.0 | 6 | 24 | 2 | 46.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10930000245571136 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 359 | MOVE_BENCH | FAST8 | 93.0 | 7 | 20 | 2 | 46.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5299438834190369 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 360 | MOVE_BENCH | FAST8 | 93.0 | 7 | 20 | 2 | 48.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3418482840061188 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 361 | PASS | FAST8 | 93.0 | 7 | 20 | 2 | 46.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05849999934434891 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 365 | MOVE_BENCH | FAST8 | 93.0 | 7 | 20 | 2 | 46.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42393210530281067 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 371 | BUY | FAST8 | 93.0 | 7 | 30 | 3 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.706994354724884 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 7 | 3-7 | 372 | MOVE_BENCH | FAST8 | 93.0 | 7 | 26 | 2 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09992298483848572 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 373 | BUY | FAST8 | 93.0 | 7 | 26 | 2 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3056754171848297 | 0.0 | 0.0 | +f00503d7-4e8f-4514-acc1-d3206151acc2 / -— |
| Jogador 7 | 3-7 | 374 | BUY_XP | FAST8 | 93.0 | 7 | 23 | 2 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 375 | BUY_XP | FAST8 | 93.0 | 7 | 19 | 1 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 376 | BUY_XP | FAST8 | 93.0 | 7 | 15 | 1 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 377 | BUY_XP | FAST8 | 93.0 | 7 | 11 | 1 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 378 | BUY_XP | FAST8 | 93.0 | 7 | 7 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 379 | PASS | FAST8 | 93.0 | 7 | 3 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 390 | CRAFT_AND_EQUIP | FAST8 | 93.0 | 7 | 10 | 1 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17182108759880066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 391 | CRAFT_AND_EQUIP | FAST8 | 93.0 | 7 | 10 | 1 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17436330020427704 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 392 | BUY_XP | FAST8 | 93.0 | 7 | 10 | 1 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 393 | BUY_XP | FAST8 | 93.0 | 7 | 6 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 394 | PASS | FAST8 | 93.0 | 7 | 2 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 402 | BUY_XP | FAST8 | 93.0 | 7 | 11 | 1 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 403 | BUY_XP | FAST8 | 93.0 | 7 | 7 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 404 | MOVE_BOARD | FAST8 | 93.0 | 7 | 3 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.945440079813125e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 405 | SELL | FAST8 | 93.0 | 7 | 3 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17429734766483307 | 0.0 | 0.0 | +— / -f00503d7-4e8f-4514-acc1-d3206151acc2 |
| Jogador 7 | 4-2 | 406 | BUY_XP | FAST8 | 93.0 | 7 | 6 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 407 | SELL | FAST8 | 93.0 | 7 | 2 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3131488263607025 | 0.0 | 0.0 | +— / -b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 7 | 4-2 | 408 | BUY | FAST8 | 93.0 | 7 | 6 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09392444044351578 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 7 | 4-2 | 409 | BUY_XP | FAST8 | 93.0 | 7 | 4 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 410 | PASS | FAST8 | 93.0 | 7 | 0 | 0 | 54.0 | Vanguarda/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 422 | SELL | FAST8 | 93.0 | 7 | 9 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0414000004529953 | 0.0 | 0.0 | +— / -c7841e00-91da-410b-b00f-62f4bf32f666 |
| Jogador 7 | 4-3 | 423 | BUY | FAST8 | 93.0 | 7 | 11 | 1 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.24422141909599304 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 7 | 4-3 | 424 | BUY_XP | FAST8 | 93.0 | 7 | 7 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0853937491774559 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 425 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 3 | 0 | 54.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40017959475517273 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 426 | BUY | WINSTREAK | 93.0 | 8 | 3 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.060869261622428894 | 0.0 | 0.0 | +477a3c7c-70fe-4f67-ab00-8c9c397365bf / -— |
| Jogador 7 | 4-3 | 427 | PASS | WINSTREAK | 93.0 | 8 | 1 | 0 | 62.0 | Vanguarda/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 438 | BUY | WINSTREAK | 93.0 | 8 | 10 | 1 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1812940388917923 | 0.0 | 0.0 | +5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 / -— |
| Jogador 7 | 4-4 | 439 | BUY | WINSTREAK | 93.0 | 8 | 7 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17036093771457672 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -— |
| Jogador 7 | 4-4 | 440 | BUY | WINSTREAK | 93.0 | 8 | 3 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2609962522983551 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 7 | 4-4 | 441 | PASS | WINSTREAK | 93.0 | 8 | 1 | 0 | 62.0 | Vanguarda/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 452 | BUY | WINSTREAK | 93.0 | 8 | 9 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7784923911094666 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 7 | 4-5 | 453 | BUY | WINSTREAK | 93.0 | 8 | 6 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2378195971250534 | 0.0 | 0.0 | +eeb774dc-b3d1-4a90-8a93-b71a9b754169 / -— |
| Jogador 7 | 4-5 | 454 | BUY | WINSTREAK | 93.0 | 8 | 2 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018858516588807106 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -— |
| Jogador 7 | 4-5 | 455 | PASS | WINSTREAK | 93.0 | 8 | 0 | 0 | 62.0 | Vanguarda/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 467 | BUY | WINSTREAK | 93.0 | 8 | 9 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7811561822891235 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 7 | 4-6 | 468 | BUY | WINSTREAK | 93.0 | 8 | 6 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2664954364299774 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 7 | 4-6 | 469 | SELL | WINSTREAK | 93.0 | 8 | 5 | 0 | 62.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06260059773921967 | 0.0 | 0.0 | +— / -5a6985d6-5377-425c-b4a3-c53dc138b288 |
| Jogador 7 | 4-6 | 470 | BUY | WINSTREAK | 93.0 | 8 | 7 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1498178392648697 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 7 | 4-6 | 471 | REROLL | WINSTREAK | 93.0 | 8 | 3 | 0 | 62.0 | Vanguarda/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 472 | SELL | WINSTREAK | 93.0 | 8 | 1 | 0 | 62.0 | Vanguarda/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059430770576000214 | 0.0 | 0.0 | +— / -477a3c7c-70fe-4f67-ab00-8c9c397365bf |
| Jogador 7 | 4-6 | 473 | BUY | WINSTREAK | 93.0 | 8 | 3 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07318238168954849 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 7 | 4-6 | 474 | SELL | WINSTREAK | 93.0 | 8 | 0 | 0 | 62.0 | Vanguarda/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07316509634256363 | 0.0 | 0.0 | +— / -aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 7 | 4-6 | 475 | BUY | WINSTREAK | 93.0 | 8 | 3 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27778366208076477 | 0.0 | 0.0 | +5e843c10-0a8b-4781-983a-8e6e6f28253e / -— |
| Jogador 7 | 4-6 | 476 | SELL | WINSTREAK | 93.0 | 8 | 0 | 0 | 62.0 | Vanguarda/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08100000023841858 | 0.0 | 0.0 | +— / -5e843c10-0a8b-4781-983a-8e6e6f28253e |
| Jogador 7 | 4-6 | 477 | PASS | WINSTREAK | 93.0 | 8 | 3 | 0 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 482 | BUY | WINSTREAK | 93.0 | 8 | 12 | 1 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7801797986030579 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 7 | 4-7 | 483 | SELL | WINSTREAK | 93.0 | 8 | 10 | 1 | 62.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 7 | 4-7 | 484 | BUY | WINSTREAK | 93.0 | 8 | 14 | 1 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35249167680740356 | 0.0 | 0.0 | +f0264dc3-6749-4682-929e-fab42383532a / -— |
| Jogador 7 | 4-7 | 485 | SELL | WINSTREAK | 93.0 | 8 | 9 | 0 | 62.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15709230303764343 | 0.0 | 0.0 | +— / -eeb774dc-b3d1-4a90-8a93-b71a9b754169 |
| Jogador 7 | 4-7 | 486 | BUY | WINSTREAK | 93.0 | 8 | 13 | 1 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.355801522731781 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 7 | 4-7 | 487 | REROLL | WINSTREAK | 93.0 | 8 | 10 | 1 | 62.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 488 | SELL | WINSTREAK | 93.0 | 8 | 8 | 0 | 62.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03425483778119087 | 0.0 | 0.0 | +— / -64d87de4-68df-4a72-8b8d-f78039ae4ce5 |
| Jogador 7 | 4-7 | 489 | BUY | WINSTREAK | 93.0 | 8 | 11 | 1 | 62.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.732887864112854 | 0.0 | 0.0 | +3329c812-11fa-4335-a982-f03e6ab28ee0 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,7313188a-ce84-4a52-b2d0-a94b2c420cdb |
| Jogador 7 | 4-7 | 490 | BUY | WINSTREAK | 93.0 | 8 | 8 | 0 | 56.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6718334555625916 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 7 | 4-7 | 491 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 4 | 0 | 56.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4000779688358307 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 492 | PASS | WINSTREAK | 93.0 | 8 | 4 | 0 | 66.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 499 | BUY | WINSTREAK | 93.0 | 8 | 12 | 1 | 66.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.13968273997306824 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -— |
| Jogador 7 | 5-1 | 500 | CRAFT_AND_EQUIP | WINSTREAK | 93.0 | 8 | 9 | 0 | 66.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.058997783809900284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 501 | CRAFT_AND_EQUIP | WINSTREAK | 93.0 | 8 | 9 | 0 | 66.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07542234659194946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 502 | REROLL | WINSTREAK | 93.0 | 8 | 9 | 0 | 66.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 503 | SELL | WINSTREAK | 93.0 | 8 | 7 | 0 | 66.0 | Vanguarda/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15303191542625427 | 0.0 | 0.0 | +— / -e978e901-0a52-4f01-ba52-a83fbcc3b439 |
| Jogador 7 | 5-1 | 504 | BUY | WINSTREAK | 93.0 | 8 | 10 | 1 | 66.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7321307063102722 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -6c691ca5-c042-46de-8d64-493514f2d793,f32e50e0-1430-4549-a1dd-a8473ffe0bd4 |
| Jogador 7 | 5-1 | 505 | BUY | WINSTREAK | 93.0 | 8 | 7 | 0 | 60.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7750917673110962 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -6eecc806-dcf8-47df-bc1d-bc5bc5f07099,f6000a82-1241-4220-9362-c8d788472db0 |
| Jogador 7 | 5-1 | 506 | BUY | WINSTREAK | 93.0 | 8 | 3 | 0 | 60.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08878286927938461 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 7 | 5-1 | 507 | PASS | WINSTREAK | 93.0 | 8 | 1 | 0 | 60.0 | Vanguarda/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 509 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 1 | 0 | 60.0 | Vanguarda/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.558914303779602 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 512 | BUY | WINSTREAK | 93.0 | 8 | 10 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1902047097682953 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 7 | 5-2 | 513 | BUY | WINSTREAK | 93.0 | 8 | 6 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10414767265319824 | 0.0 | 0.0 | +194da7dc-39b4-40e3-869d-326ace65137b / -— |
| Jogador 7 | 5-2 | 514 | REROLL | WINSTREAK | 93.0 | 8 | 3 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 515 | SELL | WINSTREAK | 93.0 | 8 | 1 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06050769239664078 | 0.0 | 0.0 | +— / -194da7dc-39b4-40e3-869d-326ace65137b |
| Jogador 7 | 5-2 | 516 | BUY | WINSTREAK | 93.0 | 8 | 4 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12020323425531387 | 0.0 | 0.0 | +b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 / -— |
| Jogador 7 | 5-2 | 517 | SELL | WINSTREAK | 93.0 | 8 | 0 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059430770576000214 | 0.0 | 0.0 | +— / -0a29573e-2a7b-4719-9b6e-49c2f476bc04 |
| Jogador 7 | 5-2 | 518 | BUY | WINSTREAK | 93.0 | 8 | 2 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03947179764509201 | 0.0 | 0.0 | +17279599-f3fc-4cf2-874f-da62a23ac238 / -— |
| Jogador 7 | 5-2 | 519 | PASS | WINSTREAK | 93.0 | 8 | 0 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 529 | SELL | WINSTREAK | 93.0 | 8 | 9 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15124616026878357 | 0.0 | 0.0 | +— / -17279599-f3fc-4cf2-874f-da62a23ac238 |
| Jogador 7 | 5-3 | 530 | BUY | WINSTREAK | 93.0 | 8 | 11 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7017490267753601 | 0.0 | 0.0 | +c71adf7d-8d74-439d-8863-dac0f4f20cd1 / -— |
| Jogador 7 | 5-3 | 531 | SELL | WINSTREAK | 93.0 | 8 | 8 | 0 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09428004175424576 | 0.0 | 0.0 | +— / -2d5214b0-3e0c-4e71-8664-2459bf616650 |
| Jogador 7 | 5-3 | 532 | BUY | WINSTREAK | 93.0 | 8 | 16 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21129782497882843 | 0.0 | 0.0 | +f1ece814-0986-421f-b5df-0b457ebaa484 / -— |
| Jogador 7 | 5-3 | 533 | REROLL | WINSTREAK | 93.0 | 8 | 12 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 534 | SELL | WINSTREAK | 93.0 | 8 | 10 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07709230482578278 | 0.0 | 0.0 | +— / -f1ece814-0986-421f-b5df-0b457ebaa484 |
| Jogador 7 | 5-3 | 535 | BUY | WINSTREAK | 93.0 | 8 | 14 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.648041844367981 | 0.0 | 0.0 | +94e47e85-54f4-4546-af6a-3700e3c325a8 / -— |
| Jogador 7 | 5-3 | 536 | SELL | WINSTREAK | 93.0 | 8 | 10 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16237230598926544 | 0.0 | 0.0 | +— / -3329c812-11fa-4335-a982-f03e6ab28ee0 |
| Jogador 7 | 5-3 | 537 | BUY | WINSTREAK | 93.0 | 8 | 18 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038772907108068466 | 0.0 | 0.0 | +40263a7a-96e9-4752-b149-8235892508e0 / -— |
| Jogador 7 | 5-3 | 538 | REROLL | WINSTREAK | 93.0 | 8 | 14 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 539 | PASS | WINSTREAK | 93.0 | 8 | 12 | 1 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 542 | SELL | WINSTREAK | 93.0 | 8 | 22 | 2 | 64.0 | Vanguarda/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -c93990ff-0a6f-46bc-8fc1-12623d55abc1 |
| Jogador 7 | 5-4 | 543 | BUY | WINSTREAK | 93.0 | 8 | 26 | 2 | 64.0 | Vanguarda/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8569982647895813 | 0.0 | 0.0 | +7fd34ef6-a124-4d23-a166-9f7ad919c826 / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164,fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 5-4 | 544 | EQUIP_FROM_INVENTORY | WINSTREAK | 93.0 | 8 | 22 | 2 | 48.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1005135104060173 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 545 | EQUIP_FROM_INVENTORY | WINSTREAK | 93.0 | 8 | 22 | 2 | 48.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04542454704642296 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 546 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 22 | 2 | 48.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039507217705249786 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 547 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 22 | 2 | 46.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18980367481708527 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 548 | BUY | WINSTREAK | 93.0 | 8 | 22 | 2 | 56.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7764672636985779 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -5b97084e-3b94-485f-bc9b-e5c6cbe90dd0,c71adf7d-8d74-439d-8863-dac0f4f20cd1 |
| Jogador 7 | 5-4 | 549 | BUY | WINSTREAK | 93.0 | 8 | 19 | 1 | 56.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019145922735333443 | 0.0 | 0.0 | +f5a067a8-3eba-4efb-a5cf-76571eb8516e / -— |
| Jogador 7 | 5-4 | 550 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 16 | 1 | 56.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11073867976665497 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 551 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 16 | 1 | 60.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05806199088692665 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 552 | PASS | WINSTREAK | 93.0 | 8 | 16 | 1 | 58.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11628571152687073 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 557 | BUY | WINSTREAK | 93.0 | 8 | 25 | 2 | 58.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2777893543243408 | 0.0 | 0.0 | +c339a5f7-66d9-4d5f-b331-4bac23a83a4a / -— |
| Jogador 7 | 5-5 | 558 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 21 | 2 | 58.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8337365388870239 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 559 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 21 | 2 | 56.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12350787222385406 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 560 | PASS | WINSTREAK | 93.0 | 8 | 21 | 2 | 60.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03221428394317627 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 565 | MOVE_BENCH | WINSTREAK | 93.0 | 8 | 21 | 2 | 60.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8252938389778137 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 572 | BUY | WINSTREAK | 93.0 | 8 | 32 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2653244435787201 | 0.0 | 0.0 | +0cc45cdb-a81e-4f84-b496-8222c6307ff4 / -— |
| Jogador 7 | 5-6 | 573 | MOVE_BOARD | WINSTREAK | 93.0 | 8 | 29 | 2 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 574 | MOVE_BOARD | WINSTREAK | 93.0 | 8 | 29 | 2 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05637215077877045 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 575 | SELL | WINSTREAK | 93.0 | 8 | 29 | 2 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15601538121700287 | 0.0 | 0.0 | +— / -f5a067a8-3eba-4efb-a5cf-76571eb8516e |
| Jogador 7 | 5-6 | 576 | BUY | WINSTREAK | 93.0 | 8 | 32 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31220895051956177 | 0.0 | 0.0 | +40cd6861-e205-4eb7-900f-d5364fc3c439 / -— |
| Jogador 7 | 5-6 | 577 | REROLL | WINSTREAK | 93.0 | 8 | 31 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 578 | SELL | WINSTREAK | 93.0 | 8 | 29 | 2 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1534000039100647 | 0.0 | 0.0 | +— / -40263a7a-96e9-4752-b149-8235892508e0 |
| Jogador 7 | 5-6 | 579 | BUY | WINSTREAK | 93.0 | 8 | 33 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.870930552482605 | 0.0 | 0.0 | +4bb25db6-fab7-4bf2-89e8-1a43cc6eb6a6 / -— |
| Jogador 7 | 5-6 | 580 | REROLL | WINSTREAK | 93.0 | 8 | 30 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 581 | SELL | WINSTREAK | 93.0 | 8 | 28 | 2 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12832307815551758 | 0.0 | 0.0 | +— / -6c338d19-b3d3-49a7-b61e-4732249ee457 |
| Jogador 7 | 5-7 | 583 | BUY | WINSTREAK | 93.0 | 8 | 41 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13974590599536896 | 0.0 | 0.0 | +f8177556-bc54-4860-a7cf-90a94b0e6c96 / -— |
| Jogador 7 | 5-7 | 584 | REROLL | WINSTREAK | 93.0 | 8 | 37 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 585 | SELL | WINSTREAK | 93.0 | 8 | 35 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07339999824762344 | 0.0 | 0.0 | +— / -f8177556-bc54-4860-a7cf-90a94b0e6c96 |
| Jogador 7 | 5-7 | 586 | BUY | WINSTREAK | 93.0 | 8 | 39 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35108742117881775 | 0.0 | 0.0 | +c184c7c4-0cf6-4101-ac4d-cea12a7b4607 / -— |
| Jogador 7 | 5-7 | 587 | SELL | WINSTREAK | 93.0 | 8 | 36 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1478615403175354 | 0.0 | 0.0 | +— / -b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 |
| Jogador 7 | 5-7 | 588 | BUY | WINSTREAK | 93.0 | 8 | 40 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08062242716550827 | 0.0 | 0.0 | +266ee11d-6e5b-4c48-8f89-769fb12dfd1a / -— |
| Jogador 7 | 5-7 | 589 | REROLL | WINSTREAK | 93.0 | 8 | 36 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 590 | SELL | WINSTREAK | 93.0 | 8 | 34 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -266ee11d-6e5b-4c48-8f89-769fb12dfd1a |
| Jogador 7 | 5-7 | 591 | BUY | WINSTREAK | 93.0 | 8 | 38 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059756938368082047 | 0.0 | 0.0 | +ed77113d-b6af-4207-92c3-c4b4e1fcda54 / -— |
| Jogador 7 | 5-7 | 592 | REROLL | WINSTREAK | 93.0 | 8 | 34 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 593 | PASS | WINSTREAK | 93.0 | 8 | 32 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04085714370012283 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 597 | EQUIP_FROM_INVENTORY | WINSTREAK | 93.0 | 8 | 43 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08228020370006561 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 598 | SELL | WINSTREAK | 93.0 | 8 | 43 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07339999824762344 | 0.0 | 0.0 | +— / -ed77113d-b6af-4207-92c3-c4b4e1fcda54 |
| Jogador 7 | 6-1 | 599 | BUY | WINSTREAK | 93.0 | 8 | 47 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006250469596125185 | 0.0 | 0.0 | +c2de293a-fa44-4161-8593-47b3feca588d / -— |
| Jogador 7 | 6-1 | 600 | SELL | WINSTREAK | 93.0 | 8 | 43 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -c2de293a-fa44-4161-8593-47b3feca588d |
| Jogador 7 | 6-1 | 601 | BUY | WINSTREAK | 93.0 | 8 | 47 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16734127700328827 | 0.0 | 0.0 | +aac54d95-6848-43d9-b837-d2189beede69 / -— |
| Jogador 7 | 6-1 | 602 | REROLL | WINSTREAK | 93.0 | 8 | 44 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 603 | SELL | WINSTREAK | 93.0 | 8 | 42 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04426153749227524 | 0.0 | 0.0 | +— / -aac54d95-6848-43d9-b837-d2189beede69 |
| Jogador 7 | 6-1 | 604 | BUY | WINSTREAK | 93.0 | 8 | 45 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015341037651523948 | 0.0 | 0.0 | +23181987-d0b2-4e8c-a1a7-48a1e28179f7 / -— |
| Jogador 7 | 6-1 | 605 | REROLL | WINSTREAK | 93.0 | 8 | 41 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 606 | SELL | WINSTREAK | 93.0 | 8 | 39 | 3 | 76.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1478615403175354 | 0.0 | 0.0 | +— / -23181987-d0b2-4e8c-a1a7-48a1e28179f7 |
| Jogador 7 | 6-1 | 607 | PASS | WINSTREAK | 93.0 | 8 | 43 | 4 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22200000286102295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 611 | BUY | WINSTREAK | 93.0 | 8 | 55 | 5 | 76.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.978721022605896 | 0.0 | 0.0 | +e00cb4c6-0784-4be7-b937-2b2b4775be1c / -94e47e85-54f4-4546-af6a-3700e3c325a8,b1efce8c-0cb0-47fc-a361-c50a76c0f9de |
| Jogador 7 | 6-2 | 612 | BUY | WINSTREAK | 93.0 | 8 | 51 | 5 | 68.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09575287252664566 | 0.0 | 0.0 | +64f5c6ab-e024-4d80-b770-dee94530827e / -— |
| Jogador 7 | 6-2 | 613 | REROLL | WINSTREAK | 93.0 | 8 | 47 | 4 | 68.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 614 | SELL | WINSTREAK | 93.0 | 8 | 45 | 4 | 68.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1258615404367447 | 0.0 | 0.0 | +— / -e00cb4c6-0784-4be7-b937-2b2b4775be1c |
| Jogador 7 | 6-2 | 615 | EQUIP_FROM_INVENTORY | WINSTREAK | 93.0 | 8 | 56 | 5 | 68.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.03788450360298157 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 616 | EQUIP_FROM_INVENTORY | WINSTREAK | 93.0 | 8 | 56 | 5 | 68.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09548033028841019 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 617 | EQUIP_FROM_INVENTORY | WINSTREAK | 93.0 | 8 | 56 | 5 | 68.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15167170763015747 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 618 | BUY | WINSTREAK | 93.0 | 8 | 56 | 5 | 68.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9066464900970459 | 0.0 | 0.0 | +559d1b79-d4c7-470c-912e-fe30541195ec / -— |
| Jogador 7 | 6-2 | 619 | SELL | WINSTREAK | 93.0 | 8 | 52 | 5 | 68.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05986153706908226 | 0.0 | 0.0 | +— / -64f5c6ab-e024-4d80-b770-dee94530827e |
| Jogador 7 | 6-2 | 620 | BUY | WINSTREAK | 93.0 | 8 | 56 | 5 | 68.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40703442692756653 | 0.0 | 0.0 | +114f5f14-ddb4-41ed-89bb-ca3d0eb32ab9 / -— |
| Jogador 7 | 6-3 | 622 | MOVE_BENCH | ECON | 76.0 | 8 | 63 | 5 | 68.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43827202916145325 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 623 | BUY | ECON | 76.0 | 8 | 63 | 5 | 74.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23565220832824707 | 0.0 | 0.0 | +4bc5b602-fe82-4525-b854-33dc5ab88a32 / -— |
| Jogador 7 | 6-3 | 624 | REROLL | ECON | 76.0 | 8 | 59 | 5 | 74.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 625 | SELL | ECON | 76.0 | 8 | 57 | 5 | 74.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06909231096506119 | 0.0 | 0.0 | +— / -4bc5b602-fe82-4525-b854-33dc5ab88a32 |
| Jogador 7 | 6-3 | 626 | BUY | ECON | 76.0 | 8 | 61 | 5 | 74.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479838848114014 | 0.0 | 0.0 | +d4fd64a7-2945-4d09-ab2e-5bd475ff0f04 / -559d1b79-d4c7-470c-912e-fe30541195ec,a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 7 | 6-3 | 627 | BUY | ECON | 76.0 | 8 | 57 | 5 | 66.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09755632281303406 | 0.0 | 0.0 | +68e8df20-cef6-4099-9daa-8fd4180c1a0d / -— |
| Jogador 7 | 6-3 | 628 | REROLL | ECON | 76.0 | 8 | 53 | 5 | 66.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 629 | SELL | ECON | 76.0 | 8 | 51 | 5 | 66.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.046370845288038254 | 0.0 | 0.0 | +— / -40cd6861-e205-4eb7-900f-d5364fc3c439 |
| Jogador 7 | 6-3 | 630 | BUY | ECON | 76.0 | 8 | 52 | 5 | 66.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4159979820251465 | 0.0 | 0.0 | +4869a6d9-9cd7-4ee7-93ae-ae4b2a0c8233 / -— |
| Jogador 7 | 6-3 | 631 | SELL | ECON | 76.0 | 8 | 48 | 4 | 66.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15309230983257294 | 0.0 | 0.0 | +— / -68e8df20-cef6-4099-9daa-8fd4180c1a0d |
| Jogador 7 | 6-3 | 632 | PASS | ECON | 76.0 | 8 | 52 | 5 | 66.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26521724462509155 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 634 | BUY | ECON | 58.0 | 8 | 63 | 5 | 66.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07220380753278732 | 0.0 | 0.0 | +f9eeb0ec-e42e-49da-ba81-ebc50f8abafd / -— |
| Jogador 7 | 6-4 | 635 | REROLL | ECON | 58.0 | 8 | 58 | 5 | 66.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 636 | MOVE_BENCH | ECON | 58.0 | 8 | 56 | 5 | 66.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5588569641113281 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 637 | BUY | ECON | 58.0 | 8 | 56 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4093532860279083 | 0.0 | 0.0 | +9db714e5-6351-482b-a263-282320af3345 / -— |
| Jogador 7 | 6-4 | 638 | REROLL | ECON | 58.0 | 8 | 52 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 639 | SELL | ECON | 58.0 | 8 | 50 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06595384329557419 | 0.0 | 0.0 | +— / -f9eeb0ec-e42e-49da-ba81-ebc50f8abafd |
| Jogador 7 | 6-4 | 640 | BUY | ECON | 58.0 | 8 | 55 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019425049424171448 | 0.0 | 0.0 | +7e7c4e12-3188-4c38-9be3-590db10b6330 / -— |
| Jogador 7 | 6-4 | 641 | REROLL | ECON | 58.0 | 8 | 51 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1720000058412552 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 642 | SELL | ECON | 58.0 | 8 | 49 | 4 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14186154305934906 | 0.0 | 0.0 | +— / -7e7c4e12-3188-4c38-9be3-590db10b6330 |
| Jogador 7 | 6-4 | 643 | BUY | ECON | 58.0 | 8 | 53 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2339055985212326 | 0.0 | 0.0 | +d3dda9b6-13bb-47e1-af12-521aed1576d6 / -— |
| Jogador 7 | 6-5 | 645 | REROLL | ECON | 58.0 | 8 | 58 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 646 | SELL | ECON | 58.0 | 8 | 56 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058938462287187576 | 0.0 | 0.0 | +— / -d3dda9b6-13bb-47e1-af12-521aed1576d6 |
| Jogador 7 | 6-5 | 647 | BUY | ECON | 58.0 | 8 | 61 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9084542393684387 | 0.0 | 0.0 | +3d7b58af-0df4-452d-b82e-049660a817ec / -— |
| Jogador 7 | 6-5 | 648 | REROLL | ECON | 58.0 | 8 | 58 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 649 | SELL | ECON | 58.0 | 8 | 56 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13776709139347076 | 0.0 | 0.0 | +— / -d4c27edc-9b7e-4a31-a967-3aa80766b470 |
| Jogador 7 | 6-5 | 650 | BUY | ECON | 58.0 | 8 | 67 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8938966989517212 | 0.0 | 0.0 | +71a71643-507c-4266-9f74-1fd7802fe094 / -— |
| Jogador 7 | 6-5 | 651 | REROLL | ECON | 58.0 | 8 | 63 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 653 | SELL | ECON | 40.0 | 8 | 72 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18703648447990417 | 0.0 | 0.0 | +— / -c184c7c4-0cf6-4101-ac4d-cea12a7b4607 |
| Jogador 7 | 6-6 | 654 | BUY | ECON | 40.0 | 8 | 75 | 5 | 82.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0484124422073364 | 0.0 | 0.0 | +16c43ccb-19ff-428d-9560-24f14aa83aad / -b2517873-8317-401b-8461-1d86969edbd7,bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 7 | 6-6 | 655 | BUY | ECON | 40.0 | 8 | 73 | 5 | 78.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17750518023967743 | 0.0 | 0.0 | +6375ddab-b4ed-4bec-b6fd-1178b2bc1843 / -— |
| Jogador 7 | 6-6 | 656 | MOVE_BOARD | ECON | 40.0 | 8 | 69 | 5 | 78.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 657 | MOVE_BOARD | ECON | 40.0 | 8 | 69 | 5 | 78.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 658 | PASS | ECON | 40.0 | 8 | 69 | 5 | 78.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12115009874105453 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 662 | BUY | ECON | 40.0 | 8 | 80 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49054229259490967 | 0.0 | 0.0 | +64b3ef70-cd08-48bc-95a8-e85929176d5c / -— |
| Jogador 7 | 6-7 | 663 | SELL | ECON | 40.0 | 8 | 77 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15671077370643616 | 0.0 | 0.0 | +— / -16c43ccb-19ff-428d-9560-24f14aa83aad |
| Jogador 7 | 6-7 | 664 | BUY | ECON | 40.0 | 8 | 82 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.010704517364502 | 0.0 | 0.0 | +12e4262b-f19f-4b25-b401-acf685f81d79 / -— |
| Jogador 7 | 6-7 | 665 | REROLL | ECON | 40.0 | 8 | 79 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 666 | SELL | ECON | 40.0 | 8 | 77 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05986153706908226 | 0.0 | 0.0 | +— / -6375ddab-b4ed-4bec-b6fd-1178b2bc1843 |
| Jogador 7 | 6-7 | 667 | BUY | ECON | 40.0 | 8 | 81 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08873846381902695 | 0.0 | 0.0 | +fdc17360-8d79-44b4-8b7e-4fc1f86a76b7 / -— |
| Jogador 7 | 6-7 | 668 | REROLL | ECON | 40.0 | 8 | 77 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 669 | SELL | ECON | 40.0 | 8 | 75 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06539999693632126 | 0.0 | 0.0 | +— / -fdc17360-8d79-44b4-8b7e-4fc1f86a76b7 |
| Jogador 7 | 6-7 | 670 | BUY | ECON | 40.0 | 8 | 79 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36984333395957947 | 0.0 | 0.0 | +f88e593a-bc21-43b4-afac-fdfb5c3afb35 / -— |
| Jogador 7 | 7-1 | 672 | EQUIP_FROM_INVENTORY | ECON | 40.0 | 8 | 86 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07164006680250168 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 673 | SELL | ECON | 40.0 | 8 | 86 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38528576493263245 | 0.0 | 0.0 | +— / -64b3ef70-cd08-48bc-95a8-e85929176d5c |
| Jogador 7 | 7-1 | 674 | BUY | ECON | 40.0 | 8 | 89 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8893229365348816 | 0.0 | 0.0 | +6de561d2-7853-4c3f-b971-64a82c3eccd8 / -— |
| Jogador 7 | 7-1 | 675 | REROLL | ECON | 40.0 | 8 | 86 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 676 | SELL | ECON | 40.0 | 8 | 84 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2075827419757843 | 0.0 | 0.0 | +— / -12e4262b-f19f-4b25-b401-acf685f81d79 |
| Jogador 7 | 7-1 | 677 | BUY | ECON | 40.0 | 8 | 87 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9729551672935486 | 0.0 | 0.0 | +0088ca46-2bd7-4e4e-a102-8cfdc86bc494 / -— |
| Jogador 7 | 7-1 | 678 | REROLL | ECON | 40.0 | 8 | 83 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 679 | REROLL | ECON | 40.0 | 8 | 81 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 680 | SELL | ECON | 40.0 | 8 | 79 | 5 | 84.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28039076924324036 | 0.0 | 0.0 | +— / -6de561d2-7853-4c3f-b971-64a82c3eccd8 |
| Jogador 8 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02 |
| Jogador 8 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +d40a14f6-4b32-4cf9-8eb7-2778414b099a / -— |
| Jogador 8 | 1-1 | 3 | SELL | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | -0.5991230607032776 | 0.0 | 0.0 | +— / -d40a14f6-4b32-4cf9-8eb7-2778414b099a |
| Jogador 8 | 1-1 | 4 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3026348650455475 | 0.0 | 0.0 | +4382679e-4d9a-4ab8-8157-632147a13749 / -— |
| Jogador 8 | 1-1 | 5 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5933651924133301 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 6 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | -0.0104712825268507 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 7 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.29856643080711365 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 32 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1288224756717682 | 0.0 | 0.0 | +— / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08487014472484589 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17361731827259064 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 35 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | 1.0209729671478271 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5159425139427185 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Leona | MOVE_BOARD, PASS | True | True | -0.012302667833864689 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Leona | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2018411010503769 | 0.0 | 0.0 | +f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 / -— |
| Jogador 8 | 1-3 | 58 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09722807258367538 | 0.0 | 0.0 | +— / -f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 |
| Jogador 8 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.169730082154274 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 60 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09143692255020142 | 0.0 | 0.0 | +— / -74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 1-3 | 61 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16958120465278625 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 64 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 83 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09143692255020142 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 84 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1153583526611328 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -78019889-2624-4adb-917b-619681f23053,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 1-4 | 85 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22871491312980652 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 86 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2683415412902832 | 0.0 | 0.0 | +— / -64f24363-3325-4538-972e-a6d8260b3787 |
| Jogador 8 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 7 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0362094640731812 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 88 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 6 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.688049011747353e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 89 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16663791239261627 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 90 | SELL | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39143693447113037 | 0.0 | 0.0 | +— / -4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 1-4 | 91 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16451770067214966 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 92 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026148573961108923 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 106 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.011436923407018185 | 0.0 | 0.0 | +— / -322e9047-623a-4fec-a0f9-d21d2fbcd88a |
| Jogador 8 | 2-1 | 107 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.0018703773384913802 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 4.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.16614538431167603 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.2966617941856384 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.002343906555324793 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 111 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4500555992126465 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 112 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.20768511295318604 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 113 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.1252308487892151 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13916490972042084 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -— |
| Jogador 8 | 2-1 | 115 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39143693447113037 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-1 | 116 | PASS | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 127 | BUY | STABILIZE | 94.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0387097597122192 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 128 | SELL | STABILIZE | 94.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7534320950508118 | 0.0 | 0.0 | +— / -ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 2-2 | 129 | BUY | STABILIZE | 94.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24029023945331573 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 130 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 9 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006234230939298868 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 131 | SELL | STABILIZE | 94.0 | 4 | 9 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006193892098963261 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 132 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 4 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1361468881368637 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 133 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 4 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07718836516141891 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 134 | BUY | STABILIZE | 94.0 | 4 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2215232253074646 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 135 | BUY_XP | STABILIZE | 94.0 | 4 | 8 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 136 | BUY_XP | STABILIZE | 94.0 | 4 | 4 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 137 | PASS | STABILIZE | 94.0 | 5 | 0 | 0 | 14.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 152 | SELL | STABILIZE | 89.0 | 5 | 6 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2642623782157898 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-3 | 153 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09260860085487366 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 154 | SELL | SLOWROLL | 89.0 | 5 | 5 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37847939133644104 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-3 | 155 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3413084149360657 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 156 | SELL | SLOWROLL | 89.0 | 5 | 7 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31600329279899597 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-3 | 157 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0836060419678688 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 158 | BUY_XP | SLOWROLL | 89.0 | 5 | 6 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1979999989271164 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 159 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 2 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.801317067584023e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 160 | SELL | STABILIZE | 89.0 | 5 | 2 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -5de56114-806a-4f58-8241-b3b8434a2154 |
| Jogador 8 | 2-3 | 161 | BUY | STABILIZE | 89.0 | 5 | 4 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13987626135349274 | 0.0 | 0.0 | +491eb6b6-54f4-4de8-bc63-d96c6c1d9cce / -— |
| Jogador 8 | 2-3 | 162 | PASS | SLOWROLL | 89.0 | 5 | 3 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 176 | SELL | SLOWROLL | 82.0 | 5 | 9 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050238337367773056 | 0.0 | 0.0 | +— / -491eb6b6-54f4-4de8-bc63-d96c6c1d9cce |
| Jogador 8 | 2-4 | 177 | BUY | SLOWROLL | 82.0 | 5 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03612042963504791 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 178 | MOVE_BENCH | SLOWROLL | 82.0 | 5 | 7 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33544427156448364 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 179 | MOVE_BENCH | LOSS_STREAK | 82.0 | 5 | 7 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3927798867225647 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 180 | BUY | LOSS_STREAK | 82.0 | 5 | 7 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05871998146176338 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 181 | MOVE_BOARD | LOSS_STREAK | 82.0 | 5 | 4 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007219257298856974 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 182 | MOVE_BOARD | LOSS_STREAK | 82.0 | 5 | 4 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01498147938400507 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 183 | BUY_XP | LOSS_STREAK | 82.0 | 5 | 4 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 184 | MOVE_BOARD | LOSS_STREAK | 82.0 | 5 | 0 | 0 | 20.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 185 | MOVE_BOARD | LOSS_STREAK | 82.0 | 5 | 0 | 0 | 20.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014967955648899078 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 186 | PASS | LOSS_STREAK | 82.0 | 5 | 0 | 0 | 20.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 197 | MOVE_BENCH | LOSS_STREAK | 82.0 | 5 | 6 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5991564989089966 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 198 | MOVE_BENCH | LOSS_STREAK | 82.0 | 5 | 6 | 0 | 20.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40811997652053833 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 199 | PASS | SLOWROLL | 82.0 | 5 | 6 | 0 | 24.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 217 | SELL | SLOWROLL | 75.0 | 5 | 12 | 1 | 24.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7879310846328735 | 0.0 | 0.0 | +— / -4382679e-4d9a-4ab8-8157-632147a13749 |
| Jogador 8 | 2-6 | 218 | BUY | STABILIZE | 75.0 | 5 | 13 | 1 | 24.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0391514301300049 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 8 | 2-6 | 219 | SELL | SLOWROLL | 75.0 | 5 | 12 | 1 | 24.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7878464460372925 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 8 | 2-6 | 220 | BUY | STABILIZE | 75.0 | 5 | 13 | 1 | 24.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.38168853521347046 | 0.0 | 0.0 | +c9a1ea77-662a-469a-ba7f-eac0713c0c52 / -— |
| Jogador 8 | 2-6 | 221 | BUY_XP | STABILIZE | 75.0 | 5 | 11 | 1 | 24.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07297000288963318 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 222 | BUY_XP | STABILIZE | 75.0 | 6 | 7 | 0 | 24.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 223 | MOVE_BENCH | STABILIZE | 75.0 | 6 | 3 | 0 | 24.0 | Lutador/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35639166831970215 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 224 | MOVE_BENCH | STABILIZE | 75.0 | 6 | 3 | 0 | 22.0 | Lutador/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4828062355518341 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 225 | BUY | FAST8 | 75.0 | 6 | 3 | 0 | 28.0 | Lutador/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12166672199964523 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 226 | PASS | FAST8 | 75.0 | 6 | 0 | 0 | 28.0 | Lutador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 235 | SELL | FAST8 | 68.0 | 6 | 7 | 0 | 28.0 | Lutador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01597827486693859 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 2-7 | 236 | BUY | FAST8 | 68.0 | 6 | 10 | 1 | 28.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.051562901586294174 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 237 | BUY_XP | FAST8 | 68.0 | 6 | 7 | 0 | 28.0 | Lutador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 238 | SELL | FAST8 | 68.0 | 6 | 3 | 0 | 28.0 | Lutador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09631777554750443 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 2-7 | 239 | BUY | FAST8 | 68.0 | 6 | 6 | 0 | 28.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31591564416885376 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 240 | BUY_XP | FAST8 | 68.0 | 6 | 5 | 0 | 28.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 241 | PASS | FAST8 | 68.0 | 6 | 1 | 0 | 28.0 | Lutador/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 254 | SELL | FAST8 | 68.0 | 6 | 8 | 0 | 28.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.13893909752368927 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 3-1 | 255 | BUY | FAST8 | 68.0 | 6 | 9 | 0 | 28.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.14123211801052094 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 256 | MOVE_BENCH | FAST8 | 68.0 | 6 | 5 | 0 | 28.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3952280580997467 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 257 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 6 | 5 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06784448027610779 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 258 | BUY_XP | FAST8 | 68.0 | 6 | 5 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 259 | PASS | FAST8 | 68.0 | 6 | 1 | 0 | 32.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 272 | BUY | FAST8 | 57.0 | 6 | 9 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20385251939296722 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 273 | BUY | FAST8 | 57.0 | 6 | 5 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7303328514099121 | 0.0 | 0.0 | +ece93d63-49d6-472c-9a10-7ece135feacc / -— |
| Jogador 8 | 3-2 | 274 | PASS | FAST8 | 57.0 | 6 | 3 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 292 | BUY | FAST8 | 46.0 | 6 | 11 | 1 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.282434344291687 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 293 | BUY_XP | FAST8 | 46.0 | 6 | 8 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 294 | BUY_XP | FAST8 | 46.0 | 6 | 4 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 295 | PASS | FAST8 | 46.0 | 6 | 0 | 0 | 32.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 312 | BUY | STABILIZE | 36.0 | 6 | 8 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13035748898983002 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 313 | BUY | STABILIZE | 36.0 | 6 | 5 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27840954065322876 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -— |
| Jogador 8 | 3-4 | 314 | BUY_XP | STABILIZE | 36.0 | 6 | 4 | 0 | 32.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0658862516283989 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 315 | PASS | STABILIZE | 36.0 | 7 | 0 | 0 | 32.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 328 | MOVE_BENCH | STABILIZE | 36.0 | 7 | 0 | 0 | 32.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5622594356536865 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 332 | BUY | STABILIZE | 36.0 | 7 | 8 | 0 | 36.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8036928772926331 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -— |
| Jogador 8 | 3-5 | 333 | BUY | STABILIZE | 36.0 | 7 | 5 | 0 | 36.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28344061970710754 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 334 | BUY | STABILIZE | 36.0 | 7 | 2 | 0 | 36.0 | Lutador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0602245032787323 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -— |
| Jogador 8 | 3-5 | 335 | PASS | STABILIZE | 36.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 352 | BUY | STABILIZE | 36.0 | 7 | 6 | 0 | 36.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2768409252166748 | 0.0 | 0.0 | +68d2cec6-d29b-4173-a696-ac20ccb1f079 / -— |
| Jogador 8 | 3-6 | 353 | REROLL | STABILIZE | 36.0 | 7 | 2 | 0 | 36.0 | Lutador/DA_18_Lillia | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 354 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.215361049224157e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 355 | SELL | STABILIZE | 36.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06570769101381302 | 0.0 | 0.0 | +— / -fa5dc86b-f736-4083-b9df-5cc174b726f2 |
| Jogador 8 | 3-6 | 356 | BUY | STABILIZE | 36.0 | 7 | 2 | 0 | 36.0 | Lutador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09147453308105469 | 0.0 | 0.0 | +813260b6-a1b8-4a5c-978e-acd60b6b1082 / -— |
| Jogador 8 | 3-6 | 357 | SELL | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06315384805202484 | 0.0 | 0.0 | +— / -813260b6-a1b8-4a5c-978e-acd60b6b1082 |
| Jogador 8 | 3-6 | 358 | BUY | STABILIZE | 36.0 | 7 | 2 | 0 | 36.0 | Lutador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009411410428583622 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 8 | 3-6 | 359 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.3970810869068373e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 360 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015585267916321754 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 361 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014835643582046032 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 362 | PASS | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Lutador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 371 | SELL | STABILIZE | 24.0 | 7 | 6 | 0 | 36.0 | Lutador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07016923278570175 | 0.0 | 0.0 | +— / -74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 8 | 3-7 | 372 | BUY | STABILIZE | 24.0 | 7 | 7 | 0 | 36.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7999902367591858 | 0.0 | 0.0 | +48be5cb2-e7b3-41f8-b212-79e21249fa6a / -— |
| Jogador 8 | 3-7 | 373 | MOVE_BENCH | STABILIZE | 24.0 | 7 | 4 | 0 | 36.0 | Lutador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09006448835134506 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 374 | MOVE_BENCH | STABILIZE | 24.0 | 7 | 4 | 0 | 36.0 | Lutador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.412215918302536 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 375 | SELL | STABILIZE | 24.0 | 7 | 4 | 0 | 40.0 | Lutador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11446759104728699 | 0.0 | 0.0 | +— / -e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 3-7 | 376 | BUY | STABILIZE | 24.0 | 7 | 7 | 0 | 40.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8073081374168396 | 0.0 | 0.0 | +d885db3e-3cc6-466d-8a25-37f632c5db40 / -— |
| Jogador 8 | 3-7 | 377 | REROLL | STABILIZE | 24.0 | 7 | 6 | 0 | 40.0 | Lutador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 378 | SELL | STABILIZE | 24.0 | 7 | 4 | 0 | 40.0 | Lutador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11046265065670013 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 3-7 | 379 | BUY | STABILIZE | 24.0 | 7 | 5 | 0 | 40.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8356481790542603 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -c9a1ea77-662a-469a-ba7f-eac0713c0c52,ece93d63-49d6-472c-9a10-7ece135feacc |
| Jogador 8 | 3-7 | 380 | BUY | STABILIZE | 24.0 | 7 | 3 | 0 | 36.0 | Lutador/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18332508206367493 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 8 | 3-7 | 381 | PASS | STABILIZE | 24.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 390 | MOVE_BENCH | STABILIZE | 24.0 | 7 | 5 | 0 | 36.0 | Lutador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5887513160705566 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 391 | BUY | STABILIZE | 24.0 | 7 | 5 | 0 | 38.0 | Lutador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07158694416284561 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 8 | 4-1 | 392 | CRAFT_AND_EQUIP | STABILIZE | 24.0 | 7 | 1 | 0 | 38.0 | Lutador/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09545955061912537 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 393 | CRAFT_AND_EQUIP | STABILIZE | 24.0 | 7 | 1 | 0 | 38.0 | Lutador/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08371833711862564 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 394 | MOVE_BENCH | STABILIZE | 24.0 | 7 | 1 | 0 | 38.0 | Lutador/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3925347626209259 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 395 | PASS | STABILIZE | 24.0 | 7 | 1 | 0 | 44.0 | Lutador/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 402 | SELL | ALL_IN | 12.0 | 7 | 7 | 0 | 44.0 | Lutador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08148778975009918 | 0.0 | 0.0 | +— / -60255a84-4f78-49f0-a4f1-d598704c7ee7 |
| Jogador 8 | 4-2 | 403 | BUY | ALL_IN | 12.0 | 7 | 12 | 1 | 44.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14636960625648499 | 0.0 | 0.0 | +579b987a-fedf-45d8-92fc-634a041d3d4f / -— |
| Jogador 8 | 4-2 | 404 | REROLL | ALL_IN | 12.0 | 7 | 9 | 0 | 44.0 | Lutador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 405 | SELL | ALL_IN | 12.0 | 7 | 7 | 0 | 44.0 | Lutador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13976922631263733 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 8 | 4-2 | 406 | BUY | ALL_IN | 12.0 | 7 | 10 | 1 | 44.0 | Lutador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7110975384712219 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 8 | 4-2 | 407 | REROLL | ALL_IN | 12.0 | 7 | 7 | 0 | 44.0 | Lutador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 408 | SELL | ALL_IN | 12.0 | 7 | 5 | 0 | 44.0 | Lutador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05053846165537834 | 0.0 | 0.0 | +— / -579b987a-fedf-45d8-92fc-634a041d3d4f |
| Jogador 8 | 4-2 | 409 | BUY | ALL_IN | 12.0 | 7 | 8 | 0 | 44.0 | Lutador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21975040435791016 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -— |
| Jogador 8 | 4-2 | 410 | REROLL | ALL_IN | 12.0 | 7 | 5 | 0 | 44.0 | Lutador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 411 | SELL | ALL_IN | 12.0 | 7 | 3 | 0 | 44.0 | Lutador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05053846165537834 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 8 | 4-2 | 412 | PASS | ALL_IN | 12.0 | 7 | 6 | 0 | 44.0 | Lutador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 422 | BUY | ALL_IN | 12.0 | 7 | 12 | 1 | 44.0 | Lutador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7114732265472412 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 8 | 4-3 | 423 | REROLL | ALL_IN | 12.0 | 7 | 8 | 0 | 44.0 | Lutador/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 424 | SELL | ALL_IN | 12.0 | 7 | 6 | 0 | 44.0 | Lutador/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30911076068878174 | 0.0 | 0.0 | +— / -d885db3e-3cc6-466d-8a25-37f632c5db40 |
| Jogador 8 | 4-3 | 425 | BUY | ALL_IN | 12.0 | 7 | 7 | 0 | 44.0 | Lutador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15892213582992554 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 8 | 4-3 | 426 | REROLL | ALL_IN | 12.0 | 7 | 4 | 0 | 44.0 | Lutador/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 427 | REROLL | ALL_IN | 12.0 | 7 | 2 | 0 | 44.0 | Lutador/DA_18_Sett | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 428 | SELL | ALL_IN | 12.0 | 7 | 0 | 0 | 44.0 | Lutador/DA_18_Sett | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05976923182606697 | 0.0 | 0.0 | +— / -bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 8 | 4-3 | 429 | BUY | ALL_IN | 12.0 | 7 | 3 | 0 | 44.0 | Lutador/DA_18_Sett | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.223240464925766 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -— |
| Jogador 8 | 4-3 | 430 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 0 | 0 | 44.0 | Lutador/DA_18_Sett | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 431 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 0 | 0 | 44.0 | Lutador/DA_18_Sett | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 432 | PASS | ALL_IN | 12.0 | 7 | 0 | 0 | 44.0 | Lutador/DA_18_Sett | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 170 | 154 | 46 | 6 | 10 | 2 | 3 | 0 | 1 | 32.0 |
- Jogador 1 — gasto por ação: BUY: 96g, BUY_XP: 52g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 6g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 17g, stage 2: 56g, stage 3: 47g, stage 4: 34g
| Jogador 2 | 301 | 255 | 131 | 10 | 10 | 2 | 10 | 1 | 177 | 40.0 |
- Jogador 2 — gasto por ação: BUY: 183g, BUY_XP: 52g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 20g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 8g, stage 2: 41g, stage 3: 87g, stage 4: 58g, stage 5: 37g, stage 6: 24g
| Jogador 3 | 166 | 122 | 47 | 7 | 1 | 1 | 9 | 2 | 79 | 32.0 |
- Jogador 3 — gasto por ação: BUY: 92g, BUY_XP: 12g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 18g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 14g, stage 2: 23g, stage 3: 60g, stage 4: 25g
| Jogador 4 | 240 | 247 | 89 | 8 | 8 | 1 | 16 | 1 | 21 | 54.0 |
- Jogador 4 — gasto por ação: BUY: 171g, BUY_XP: 44g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 32g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 17g, stage 2: 57g, stage 3: 49g, stage 4: 38g, stage 5: 86g
| Jogador 5 | 289 | 340 | 155 | 20 | 17 | 1 | 14 | 0 | 58 | 62.0 |
- Jogador 5 — gasto por ação: BUY: 228g, BUY_XP: 84g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 28g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 10g, stage 2: 57g, stage 3: 52g, stage 4: 42g, stage 5: 63g, stage 6: 103g, stage 7: 13g
| Jogador 6 | 221 | 215 | 77 | 11 | 11 | 2 | 12 | 1 | 3 | 52.0 |
- Jogador 6 — gasto por ação: BUY: 135g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 24g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 19g, stage 2: 54g, stage 3: 57g, stage 4: 64g, stage 5: 21g
| Jogador 7 | 333 | 445 | 209 | 29 | 20 | 2 | 27 | 2 | 82 | 84.0 |
- Jogador 7 — gasto por ação: BUY: 299g, BUY_XP: 92g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 54g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 11g, stage 2: 58g, stage 3: 68g, stage 4: 89g, stage 5: 94g, stage 6: 112g, stage 7: 13g
| Jogador 8 | 170 | 172 | 58 | 10 | 9 | 2 | 8 | 0 | 0 | 44.0 |
- Jogador 8 — gasto por ação: BUY: 108g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 16g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 12g, stage 2: 65g, stage 3: 60g, stage 4: 35g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 13 | 3 |
- Jogador 1 · 2-1 · step 110: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 1 · 3-1 · step 261: PASS com 5g, HP 71, nível 6/8 (FAST8).
- Jogador 1 · 4-2 · step 406: REROLL com 5g, HP 16, nível 7/8 (STABILIZE).
| Jogador 2 | 13 | 30 |
- Jogador 2 · 2-5 · step 201: PASS com 6g, HP 100, nível 5/8 (STABILIZE).
- Jogador 2 · 3-1 · step 264: PASS com 21g, HP 100, nível 6/8 (FAST8).
- Jogador 2 · 4-1 · step 398: PASS com 6g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-2 · step 408: REROLL com 12g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-2 · step 412: PASS com 15g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-3 · step 429: REROLL com 20g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-3 · step 432: PASS com 19g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-4 · step 440: REROLL com 27g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-4 · step 443: REROLL com 25g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-4 · step 448: PASS com 21g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-5 · step 459: PASS com 28g, HP 79, nível 7/8 (FAST8).
- Jogador 2 · 4-6 · step 470: PASS com 35g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 4-7 · step 486: REROLL com 50g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 4-7 · step 492: PASS com 47g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 5-1 · step 508: REROLL com 59g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 5-1 · step 509: PASS com 57g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 5-2 · step 515: REROLL com 67g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 5-2 · step 520: REROLL com 67g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 5-2 · step 522: PASS com 67g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 5-3 · step 535: PASS com 71g, HP 50, nível 7/8 (FAST8).
- Jogador 2 · 5-4 · step 547: PASS com 82g, HP 34, nível 7/8 (STABILIZE).
- Jogador 2 · 5-5 · step 560: PASS com 93g, HP 34, nível 7/8 (STABILIZE).
- Jogador 2 · 5-6 · step 578: PASS com 105g, HP 34, nível 7/8 (STABILIZE).
- Jogador 2 · 5-7 · step 588: PASS com 117g, HP 34, nível 7/8 (STABILIZE).
- Jogador 2 · 6-1 · step 602: REROLL com 128g, HP 34, nível 7/8 (STABILIZE).
- Jogador 2 · 6-1 · step 607: PASS com 125g, HP 34, nível 7/8 (STABILIZE).
- Jogador 2 · 6-3 · step 627: PASS com 146g, HP 15, nível 7/8 (ALL_IN).
- Jogador 2 · 6-4 · step 638: REROLL com 157g, HP 15, nível 7/8 (ALL_IN).
- Jogador 2 · 6-5 · step 649: PASS com 163g, HP 15, nível 7/8 (ALL_IN).
- Jogador 2 · 6-6 · step 659: PASS com 177g, HP 15, nível 7/8 (ALL_IN).
| Jogador 3 | 3 | 18 |
- Jogador 3 · 2-2 · step 131: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 3 · 2-3 · step 157: PASS com 7g, HP 95, nível 4/8 (STABILIZE).
- Jogador 3 · 3-4 · step 321: PASS com 46g, HP 51, nível 6/8 (FAST8).
- Jogador 3 · 3-5 · step 337: REROLL com 42g, HP 51, nível 6/8 (FAST8).
- Jogador 3 · 3-5 · step 342: PASS com 40g, HP 51, nível 6/8 (FAST8).
- Jogador 3 · 3-6 · step 356: REROLL com 46g, HP 41, nível 6/8 (FAST8).
- Jogador 3 · 3-6 · step 361: PASS com 42g, HP 41, nível 6/8 (FAST8).
- Jogador 3 · 3-7 · step 373: REROLL com 53g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 3-7 · step 379: REROLL com 50g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 3-7 · step 380: REROLL com 48g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 3-7 · step 381: PASS com 46g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 4-1 · step 396: REROLL com 64g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 4-1 · step 400: PASS com 62g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 4-2 · step 404: PASS com 75g, HP 17, nível 6/8 (STABILIZE).
- Jogador 3 · 4-3 · step 427: REROLL com 85g, HP 5, nível 6/8 (ALL_IN).
- Jogador 3 · 4-3 · step 430: REROLL com 83g, HP 5, nível 6/8 (ALL_IN).
- Jogador 3 · 4-3 · step 431: REROLL com 81g, HP 5, nível 6/8 (ALL_IN).
- Jogador 3 · 4-3 · step 432: PASS com 79g, HP 5, nível 6/8 (ALL_IN).
| Jogador 4 | 11 | 25 |
- Jogador 4 · 4-4 · step 440: REROLL com 8g, HP 64, nível 7/8 (FAST8).
- Jogador 4 · 4-4 · step 445: PASS com 5g, HP 64, nível 7/8 (FAST8).
- Jogador 4 · 4-5 · step 457: PASS com 10g, HP 64, nível 7/8 (FAST8).
- Jogador 4 · 4-6 · step 470: PASS com 17g, HP 64, nível 7/8 (FAST8).
- Jogador 4 · 4-7 · step 488: REROLL com 25g, HP 51, nível 7/8 (FAST8).
- Jogador 4 · 4-7 · step 492: PASS com 23g, HP 51, nível 7/8 (FAST8).
- Jogador 4 · 5-1 · step 504: PASS com 30g, HP 51, nível 7/8 (FAST8).
- Jogador 4 · 5-2 · step 518: REROLL com 34g, HP 35, nível 7/8 (STABILIZE).
- Jogador 4 · 5-2 · step 522: PASS com 32g, HP 35, nível 7/8 (STABILIZE).
- Jogador 4 · 5-3 · step 532: REROLL com 36g, HP 35, nível 7/8 (STABILIZE).
- Jogador 4 · 5-3 · step 539: PASS com 30g, HP 35, nível 7/8 (STABILIZE).
- Jogador 4 · 5-4 · step 546: REROLL com 31g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-4 · step 547: REROLL com 29g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-4 · step 548: REROLL com 27g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-4 · step 549: REROLL com 25g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-4 · step 550: REROLL com 23g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-4 · step 552: PASS com 29g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-5 · step 558: REROLL com 34g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-5 · step 561: REROLL com 32g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-5 · step 562: REROLL com 30g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-5 · step 565: REROLL com 27g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-5 · step 566: REROLL com 25g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-5 · step 567: PASS com 23g, HP 18, nível 7/8 (STABILIZE).
- Jogador 4 · 5-6 · step 575: REROLL com 36g, HP 3, nível 7/8 (ALL_IN).
- Jogador 4 · 5-6 · step 581: REROLL com 23g, HP 3, nível 7/8 (ALL_IN).
| Jogador 5 | 21 | 3 |
- Jogador 5 · 3-3 · step 294: PASS com 7g, HP 79, nível 6/8 (FAST8).
- Jogador 5 · 3-5 · step 334: PASS com 8g, HP 79, nível 7/8 (FAST8).
- Jogador 5 · 4-4 · step 442: PASS com 6g, HP 68, nível 7/8 (FAST8).
| Jogador 6 | 14 | 10 |
- Jogador 6 · 3-2 · step 276: PASS com 8g, HP 80, nível 6/8 (FAST8).
- Jogador 6 · 3-3 · step 295: PASS com 14g, HP 70, nível 6/8 (FAST8).
- Jogador 6 · 3-4 · step 315: PASS com 21g, HP 70, nível 6/8 (FAST8).
- Jogador 6 · 3-5 · step 342: PASS com 15g, HP 70, nível 7/8 (FAST8).
- Jogador 6 · 4-4 · step 439: REROLL com 5g, HP 33, nível 7/8 (STABILIZE).
- Jogador 6 · 4-5 · step 456: REROLL com 7g, HP 33, nível 7/8 (STABILIZE).
- Jogador 6 · 5-1 · step 502: REROLL com 5g, HP 9, nível 7/8 (ALL_IN).
- Jogador 6 · 5-2 · step 512: REROLL com 7g, HP 9, nível 7/8 (ALL_IN).
- Jogador 6 · 5-2 · step 513: REROLL com 5g, HP 9, nível 7/8 (ALL_IN).
- Jogador 6 · 5-2 · step 516: REROLL com 4g, HP 9, nível 7/8 (ALL_IN).
| Jogador 7 | 23 | 8 |
- Jogador 7 · 2-1 · step 116: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 7 · 2-6 · step 227: PASS com 4g, HP 100, nível 6/8 (FAST8).
- Jogador 7 · 2-7 · step 239: PASS com 9g, HP 93, nível 6/8 (FAST8).
- Jogador 7 · 3-2 · step 275: PASS com 9g, HP 93, nível 6/8 (FAST8).
- Jogador 7 · 3-3 · step 294: PASS com 17g, HP 93, nível 6/8 (FAST8).
- Jogador 7 · 3-4 · step 318: PASS com 24g, HP 93, nível 6/8 (FAST8).
- Jogador 7 · 3-5 · step 341: PASS com 34g, HP 93, nível 6/8 (FAST8).
- Jogador 7 · 3-6 · step 361: PASS com 20g, HP 93, nível 7/8 (FAST8).
| Jogador 8 | 12 | 9 |
- Jogador 8 · 1-4 · step 93: PASS com 5g, HP 100, nível 3/8 (STABILIZE).
- Jogador 8 · 2-1 · step 116: PASS com 7g, HP 100, nível 4/8 (STABILIZE).
- Jogador 8 · 3-7 · step 377: REROLL com 6g, HP 24, nível 7/8 (STABILIZE).
- Jogador 8 · 4-2 · step 404: REROLL com 9g, HP 12, nível 7/8 (ALL_IN).
- Jogador 8 · 4-2 · step 407: REROLL com 7g, HP 12, nível 7/8 (ALL_IN).
- Jogador 8 · 4-2 · step 410: REROLL com 5g, HP 12, nível 7/8 (ALL_IN).
- Jogador 8 · 4-2 · step 412: PASS com 6g, HP 12, nível 7/8 (ALL_IN).
- Jogador 8 · 4-3 · step 423: REROLL com 8g, HP 12, nível 7/8 (ALL_IN).
- Jogador 8 · 4-3 · step 426: REROLL com 4g, HP 12, nível 7/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 4 | 4 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 170 | 43 | 36 | 91 | 0.0009 | 0.3878 | -0.0009 | 0.3894 | 0.0018 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0265 (46 ações), BUY_XP: Δ 0.0074 (13 ações), CRAFT_AND_EQUIP: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0523 (23 ações), MOVE_BOARD: Δ -0.0123 (34 ações), PASS: Δ 0.0000 (21 ações), REROLL: Δ 0.0000 (3 ações), SELL: Δ 0.0194 (25 ações)
| Jogador 2 | 301 | 62 | 60 | 179 | 0.0045 | 0.3667 | 0.0030 | 0.4938 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0257 (75 ações), BUY_XP: Δ 0.0048 (13 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (11 ações), MOVE_BENCH: Δ 0.0316 (81 ações), MOVE_BOARD: Δ -0.0142 (18 ações), PASS: Δ 0.0000 (36 ações), REROLL: Δ 0.0000 (10 ações), SELL: Δ 0.0179 (50 ações)
| Jogador 3 | 166 | 44 | 37 | 85 | 0.0071 | 0.2695 | 0.0038 | 0.4068 | 0.0033 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0373 (41 ações), BUY_XP: Δ 0.0214 (3 ações), CRAFT_AND_EQUIP: Δ 0.0000 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0382 (42 ações), MOVE_BOARD: Δ 0.0277 (24 ações), PASS: Δ 0.0000 (21 ações), REROLL: Δ 0.0000 (9 ações), SELL: Δ 0.0194 (19 ações)
| Jogador 4 | 240 | 64 | 44 | 132 | 0.0051 | 0.5686 | 0.0027 | 0.4620 | 0.0024 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0293 (70 ações), BUY_XP: Δ 0.0082 (11 ações), CRAFT_AND_EQUIP: Δ -0.0543 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0416 (39 ações), MOVE_BOARD: Δ 0.0413 (24 ações), PASS: Δ 0.0001 (30 ações), REROLL: Δ 0.0001 (16 ações), SELL: Δ 0.0233 (40 ações)
| Jogador 5 | 289 | 61 | 51 | 177 | 0.0035 | 0.4070 | 0.0020 | 0.4468 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0298 (80 ações), BUY_XP: Δ 0.0083 (21 ações), CRAFT_AND_EQUIP: Δ 0.0010 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0689 (41 ações), MOVE_BOARD: Δ -0.0166 (39 ações), PASS: Δ 0.0000 (34 ações), REROLL: Δ 0.0000 (14 ações), SELL: Δ 0.0215 (48 ações)
| Jogador 6 | 221 | 48 | 38 | 135 | 0.0036 | 0.1535 | 0.0011 | 0.5137 | 0.0025 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0095 (58 ações), BUY_XP: Δ 0.0104 (14 ações), CRAFT_AND_EQUIP: Δ -0.0003 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0441 (41 ações), MOVE_BOARD: Δ -0.0203 (27 ações), PASS: Δ -0.0001 (27 ações), REROLL: Δ 0.0000 (12 ações), SELL: Δ -0.0014 (33 ações)
| Jogador 7 | 333 | 57 | 50 | 226 | 0.0009 | 0.2695 | -0.0001 | 0.4261 | 0.0010 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0301 (98 ações), BUY_XP: Δ 0.0056 (23 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (9 ações), MOVE_BENCH: Δ 0.0171 (53 ações), MOVE_BOARD: Δ 0.0730 (19 ações), PASS: Δ 0.0003 (34 ações), REROLL: Δ 0.0000 (27 ações), SELL: Δ 0.0132 (63 ações)
| Jogador 8 | 170 | 40 | 30 | 100 | 0.0017 | 0.2910 | -0.0004 | 0.4247 | 0.0021 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0211 (52 ações), BUY_XP: Δ 0.0121 (12 ações), CRAFT_AND_EQUIP: Δ 0.0021 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ -0.0540 (19 ações), MOVE_BOARD: Δ 0.1001 (18 ações), PASS: Δ 0.0000 (21 ações), REROLL: Δ 0.0000 (8 ações), SELL: Δ 0.0137 (33 ações)
- Jogador 1 — rounds avaliados: 21; correlação estrutural/combate: -0.042; posicional/combate: -0.012.
- Jogador 1 — combate positive: score estrutural prévio 0.491
  score posicional prévio 0.444
- Jogador 1 — combate negative: score estrutural prévio 0.395
  score posicional prévio 0.396
- Jogador 2 — rounds avaliados: 38; correlação estrutural/combate: 0.160; posicional/combate: 0.145.
- Jogador 2 — combate positive: score estrutural prévio 0.420
  score posicional prévio 0.514
- Jogador 2 — combate negative: score estrutural prévio 0.360
  score posicional prévio 0.495
- Jogador 3 — rounds avaliados: 21; correlação estrutural/combate: -0.025; posicional/combate: -0.364.
- Jogador 3 — combate positive: score estrutural prévio 0.262
  score posicional prévio 0.366
- Jogador 3 — combate negative: score estrutural prévio 0.269
  score posicional prévio 0.435
- Jogador 4 — rounds avaliados: 31; correlação estrutural/combate: 0.039; posicional/combate: -0.056.
- Jogador 4 — combate positive: score estrutural prévio 0.665
  score posicional prévio 0.487
- Jogador 4 — combate negative: score estrutural prévio 0.639
  score posicional prévio 0.497
- Jogador 5 — rounds avaliados: 40; correlação estrutural/combate: -0.195; posicional/combate: 0.290.
- Jogador 5 — combate positive: score estrutural prévio 0.326
  score posicional prévio 0.503
- Jogador 5 — combate negative: score estrutural prévio 0.452
  score posicional prévio 0.450
- Jogador 6 — rounds avaliados: 27; correlação estrutural/combate: -0.048; posicional/combate: 0.077.
- Jogador 6 — combate positive: score estrutural prévio 0.128
  score posicional prévio 0.572
- Jogador 6 — combate negative: score estrutural prévio 0.151
  score posicional prévio 0.547
- Jogador 7 — rounds avaliados: 40; correlação estrutural/combate: 0.174; posicional/combate: 0.194.
- Jogador 7 — combate positive: score estrutural prévio 0.337
  score posicional prévio 0.459
- Jogador 7 — combate negative: score estrutural prévio 0.203
  score posicional prévio 0.386
- Jogador 8 — rounds avaliados: 21; correlação estrutural/combate: -0.378; posicional/combate: -0.155.
- Jogador 8 — combate positive: score estrutural prévio 0.169
  score posicional prévio 0.450
- Jogador 8 — combate negative: score estrutural prévio 0.457
  score posicional prévio 0.477

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 190 | OK (190) | 4 | 1 | 0 | 1 | 5 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_InfinityEdge, TFT_Item_MadredsBloodrazor, TFT_Item_RunaansHurricane, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 338 | OK (338) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 2 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_FrozenHeart, TFT_Item_GargoyleStoneplate, TFT_Item_LastWhisper, TFT_Item_Quicksilver, TFT_Item_RunaansHurricane, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 186 | OK (186) | 4 | 1 | 0 | 1 | 5 | 2 |
- Jogador 3 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_FrozenHeart, TFT_Item_InfinityEdge, TFT_Item_Leviathan, TFT_Item_Redemption; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 270 | OK (270) | 7 | 0 | 0 | 0 | 7 | 2 |
- Jogador 4 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_InfinityEdge, TFT_Item_PowerGauntlet, TFT_Item_Redemption, TFT_Item_RunaansHurricane; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 328 | OK (328) | 7 | 2 | 0 | 0 | 9 | 2 |
- Jogador 5 — IDs equipados observados: DA_18_EmblemSlayer, TFT_Item_Crownguard, TFT_Item_GargoyleStoneplate, TFT_Item_LastWhisper, TFT_Item_Leviathan, TFT_Item_MadredsBloodrazor, TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 247 | OK (247) | 7 | 0 | 0 | 0 | 7 | 2 |
- Jogador 6 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_FrozenHeart, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_RabadonsDeathcap, TFT_Item_SpearOfShojin, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 373 | OK (373) | 9 | 0 | 0 | 0 | 9 | 3 |
- Jogador 7 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_RunaansHurricane, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 190 | OK (190) | 5 | 0 | 0 | 1 | 5 | 2 |
- Jogador 8 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_LastWhisper, TFT_Item_Redemption; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 1 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.011 | 0.000 |
| Jogador 1 | 1-3 | 12 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 2 → 4 | 5 | 3 → 3 | 0.002 | 0.000 |
| Jogador 1 | 1-4 | 12 | 0.000 | 0.000 | 0 → 0 | 2 → 0 | 11% → 11% | 4 → 4 | 8 | 3 → 4 | -0.001 | 0.000 |
| Jogador 1 | 2-1 | 7 | 2.000 | -2.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 9 | 1 | 4 → 4 | -0.015 | -0.346 |
| Jogador 1 | 2-2 | 12 | 6.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 6 | 11 | 4 → 5 | 0.014 | -0.211 |
| Jogador 1 | 2-3 | 7 | 8.000 | -2.000 | 0 → 0 | 1 → 1 | 14% → 18% | 6 → 9 | 3 | 5 → 5 | 0.003 | -0.339 |
| Jogador 1 | 2-4 | 12 | 0.000 | -2.000 | 0 → 0 | 1 → 0 | 18% → 18% | 9 → 8 | 15 | 5 → 5 | 0.000 | 0.000 |
| Jogador 1 | 2-5 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 18% → 18% | 8 → 8 | 6 | 5 → 6 | 0.037 | -0.439 |
| Jogador 1 | 2-6 | 12 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 21% | 8 → 7 | 14 | 6 → 6 | -0.004 | -0.198 |
| Jogador 1 | 2-7 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 10 | 6 | 6 → 6 | 0.005 | 0.000 |
| Jogador 1 | 3-1 | 9 | 6.000 | 0.000 | 0 → 1 | 1 → 1 | 21% → 21% | 10 → 13 | 5 | 6 → 6 | 0.007 | -0.293 |
| Jogador 1 | 3-2 | 8 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 21% → 21% | 13 → 9 | 10 | 6 → 6 | -0.005 | 0.356 |
| Jogador 1 | 3-3 | 11 | 4.000 | -4.000 | 1 → 1 | 2 → 1 | 21% → 25% | 9 → 6 | 10 | 6 → 7 | -0.002 | -0.239 |
| Jogador 1 | 3-4 | 7 | 0.000 | 4.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | -0.013 | 0.000 |
| Jogador 1 | 3-5 | 7 | 0.000 | 10.000 | 1 → 1 | 1 → 2 | 25% → 25% | 5 → 6 | 5 | 7 → 7 | -0.002 | -0.396 |
| Jogador 1 | 3-6 | 9 | -4.000 | 8.000 | 1 → 1 | 2 → 1 | 25% → 25% | 6 → 7 | 5 | 7 → 7 | 0.018 | -0.307 |
| Jogador 1 | 3-7 | 7 | 0.000 | 12.000 | 1 → 1 | 1 → 2 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | 0.006 | 0.000 |
| Jogador 1 | 4-1 | 8 | 0.000 | 12.000 | 1 → 1 | 2 → 3 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | -0.000 | -0.334 |
| Jogador 1 | 4-2 | 12 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 7 → 7 | 15 | 7 → 7 | 0.000 | -0.229 |
| Jogador 1 | 4-3 | 11 | -32.000 | -52.000 | 1 → 0 | 3 → 0 | 25% → 0% | 7 → 1 | 13 | 7 → 7 | -0.092 | -0.257 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 13, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 45 ações e piorou em 38.
- Jogador 1 — estado final: ouro 1, nível 7, vida 3.0, colocação 8.
| Jogador 2 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 2 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.013 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.012 | 0.000 |
| Jogador 2 | 1-4 | 8 | 4.000 | 0.000 | 0 → 1 | 1 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.042 | 0.000 |
| Jogador 2 | 2-1 | 11 | 6.000 | -4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 9 | 6 | 4 → 4 | -0.002 | 0.244 |
| Jogador 2 | 2-2 | 12 | 0.000 | 2.000 | 1 → 1 | 0 → 0 | 14% → 14% | 9 → 7 | 13 | 4 → 5 | 0.003 | 0.224 |
| Jogador 2 | 2-3 | 12 | 6.000 | -2.000 | 1 → 0 | 0 → 0 | 14% → 18% | 7 → 9 | 11 | 5 → 5 | 0.007 | 0.209 |
| Jogador 2 | 2-4 | 6 | 2.000 | 10.000 | 0 → 0 | 0 → 0 | 18% → 18% | 9 → 9 | 6 | 5 → 5 | 0.017 | 0.000 |
| Jogador 2 | 2-5 | 6 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 9 → 13 | 3 | 5 → 5 | 0.009 | 0.410 |
| Jogador 2 | 2-6 | 9 | 0.000 | -8.000 | 0 → 0 | 0 → 1 | 18% → 18% | 13 → 26 | 2 | 5 → 5 | 0.000 | 0.293 |
| Jogador 2 | 2-7 | 5 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 26 → 35 | 0 | 5 → 5 | -0.009 | 0.000 |
| Jogador 2 | 3-1 | 12 | 6.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 21% | 35 → 32 | 18 | 5 → 6 | -0.001 | 0.238 |
| Jogador 2 | 3-2 | 11 | 4.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 25% | 32 → 12 | 29 | 6 → 7 | -0.014 | 0.264 |
| Jogador 2 | 3-3 | 10 | 0.000 | 22.000 | 0 → 0 | 1 → 1 | 25% → 25% | 12 → 10 | 11 | 7 → 7 | -0.002 | 0.303 |
| Jogador 2 | 3-4 | 7 | 2.000 | 10.000 | 0 → 0 | 1 → 2 | 25% → 25% | 10 → 9 | 9 | 7 → 7 | -0.010 | 0.000 |
| Jogador 2 | 3-5 | 8 | -4.000 | 12.000 | 0 → 0 | 2 → 2 | 25% → 25% | 9 → 7 | 7 | 7 → 7 | -0.014 | -0.329 |
| Jogador 2 | 3-6 | 11 | 0.000 | 8.000 | 0 → 0 | 2 → 1 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | -0.023 | -0.261 |
| Jogador 2 | 3-7 | 7 | 0.000 | 12.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | 0.013 | 0.000 |
| Jogador 2 | 4-1 | 10 | 2.000 | 0.000 | 0 → 0 | 1 → 0 | 25% → 25% | 7 → 12 | 7 | 7 → 7 | 0.002 | 0.288 |
| Jogador 2 | 4-2 | 12 | 0.000 | -8.000 | 0 → 0 | 0 → 1 | 25% → 25% | 12 → 23 | 11 | 7 → 7 | 0.011 | 0.233 |
| Jogador 2 | 4-3 | 12 | 4.000 | 0.000 | 0 → 0 | 1 → 2 | 25% → 25% | 23 → 28 | 8 | 7 → 7 | 0.045 | 0.244 |
| Jogador 2 | 4-4 | 12 | -6.000 | 12.000 | 0 → 0 | 2 → 3 | 25% → 25% | 28 → 29 | 11 | 7 → 7 | -0.011 | 0.000 |
| Jogador 2 | 4-5 | 9 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 29 → 35 | 4 | 7 → 7 | 0.006 | -0.317 |
| Jogador 2 | 4-6 | 5 | 4.000 | -4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 35 → 44 | 0 | 7 → 7 | -0.010 | 0.617 |
| Jogador 2 | 4-7 | 12 | -4.000 | -4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 44 → 56 | 17 | 7 → 7 | -0.034 | 0.000 |
| Jogador 2 | 5-1 | 12 | 6.000 | -8.000 | 0 → 0 | 3 → 3 | 25% → 25% | 56 → 67 | 9 | 7 → 7 | 0.041 | 0.000 |
| Jogador 2 | 5-2 | 12 | 0.000 | -8.000 | 0 → 0 | 3 → 3 | 25% → 25% | 67 → 77 | 12 | 7 → 7 | -0.037 | -0.233 |
| Jogador 2 | 5-3 | 8 | 0.000 | 12.000 | 0 → 0 | 3 → 3 | 25% → 25% | 77 → 82 | 7 | 7 → 7 | 0.018 | -0.350 |
| Jogador 2 | 5-4 | 7 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 82 → 93 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 5 | -6.000 | 6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 93 → 104 | 0 | 7 → 7 | 0.091 | 0.621 |
| Jogador 2 | 5-6 | 8 | 6.000 | -8.000 | 0 → 0 | 3 → 2 | 25% → 25% | 104 → 117 | 3 | 7 → 7 | -0.075 | 0.392 |
| Jogador 2 | 5-7 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 25% → 25% | 117 → 128 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 12 | 0.000 | 2.000 | 0 → 0 | 3 → 2 | 25% → 25% | 128 → 135 | 11 | 7 → 7 | 0.000 | -0.233 |
| Jogador 2 | 6-2 | 11 | -2.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 135 → 146 | 2 | 7 → 7 | 0.013 | 0.000 |
| Jogador 2 | 6-3 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 25% → 25% | 146 → 157 | 2 | 7 → 7 | 0.000 | 0.442 |
| Jogador 2 | 6-4 | 11 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 157 → 163 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-5 | 6 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 163 → 175 | 0 | 7 → 7 | 0.000 | 0.508 |
| Jogador 2 | 6-6 | 8 | -40.000 | -62.000 | 0 → 0 | 3 → 0 | 25% → 0% | 175 → 177 | 1 | 7 → 7 | -0.108 | -0.356 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 26, COMPOSITION_COMPATIBILITY: 27, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 17; mudanças de composição: 0; posicionamento melhorou em 65 ações e piorou em 62.
- Jogador 2 — estado final: ouro 177, nível 7, vida 15.0, colocação 3.
| Jogador 3 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.081 | 0.000 |
| Jogador 3 | 1-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.008 | 0.000 |
| Jogador 3 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.002 | 0.000 |
| Jogador 3 | 1-4 | 9 | 2.000 | -4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 8 | 3 → 4 | 0.020 | 0.000 |
| Jogador 3 | 2-1 | 9 | 4.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.015 | 0.279 |
| Jogador 3 | 2-2 | 7 | 4.000 | -4.000 | 0 → 1 | 1 → 0 | 14% → 14% | 6 → 9 | 2 | 4 → 4 | -0.053 | -0.332 |
| Jogador 3 | 2-3 | 7 | 2.000 | 2.000 | 1 → 1 | 0 → 1 | 14% → 14% | 9 → 13 | 2 | 4 → 5 | 0.069 | -0.339 |
| Jogador 3 | 2-4 | 10 | 6.000 | 4.000 | 1 → 1 | 1 → 1 | 14% → 18% | 13 → 14 | 6 | 5 → 5 | -0.006 | 0.000 |
| Jogador 3 | 2-5 | 7 | 0.000 | 4.000 | 1 → 1 | 1 → 1 | 18% → 18% | 14 → 19 | 2 | 5 → 5 | 0.001 | 0.386 |
| Jogador 3 | 2-6 | 12 | -4.000 | 8.000 | 1 → 0 | 1 → 2 | 18% → 18% | 19 → 23 | 2 | 5 → 5 | 0.010 | -0.207 |
| Jogador 3 | 2-7 | 12 | 6.000 | -18.000 | 0 → 1 | 2 → 0 | 18% → 18% | 23 → 35 | 5 | 5 → 5 | -0.004 | 0.000 |
| Jogador 3 | 3-1 | 5 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 18% → 18% | 35 → 41 | 3 | 5 → 5 | 0.024 | -0.545 |
| Jogador 3 | 3-2 | 6 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 18% | 41 → 51 | 0 | 5 → 5 | -0.008 | -0.446 |
| Jogador 3 | 3-3 | 10 | 0.000 | 4.000 | 1 → 1 | 0 → 0 | 18% → 18% | 51 → 59 | 2 | 5 → 5 | 0.005 | -0.268 |
| Jogador 3 | 3-4 | 11 | 4.000 | 6.000 | 1 → 1 | 0 → 0 | 18% → 21% | 59 → 56 | 13 | 5 → 6 | -0.006 | 0.000 |
| Jogador 3 | 3-5 | 12 | 0.000 | 28.000 | 1 → 1 | 0 → 3 | 21% → 21% | 56 → 51 | 18 | 6 → 6 | 0.000 | -0.219 |
| Jogador 3 | 3-6 | 11 | 0.000 | 8.000 | 1 → 1 | 3 → 2 | 21% → 21% | 51 → 54 | 12 | 6 → 6 | -0.006 | -0.256 |
| Jogador 3 | 3-7 | 12 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 54 → 58 | 12 | 6 → 6 | -0.005 | 0.000 |
| Jogador 3 | 4-1 | 12 | 0.000 | -8.000 | 1 → 1 | 2 → 4 | 21% → 21% | 58 → 75 | 10 | 6 → 6 | -0.046 | -0.226 |
| Jogador 3 | 4-2 | 4 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 21% → 21% | 75 → 88 | 0 | 6 → 6 | 0.153 | -0.666 |
| Jogador 3 | 4-3 | 12 | -30.000 | -48.000 | 1 → 0 | 4 → 0 | 21% → 0% | 88 → 79 | 15 | 6 → 6 | -0.060 | -0.242 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 46 ações e piorou em 38.
- Jogador 3 — estado final: ouro 79, nível 6, vida 5.0, colocação 7.
| Jogador 4 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 4 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.016 | 0.000 |
| Jogador 4 | 1-3 | 9 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 5 | 3 → 3 | -0.003 | 0.000 |
| Jogador 4 | 1-4 | 12 | 0.000 | -4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 8 | 3 → 4 | 0.009 | 0.000 |
| Jogador 4 | 2-1 | 11 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 9 | 5 | 4 → 4 | -0.008 | 0.233 |
| Jogador 4 | 2-2 | 12 | 8.000 | 2.000 | 0 → 0 | 0 → 1 | 14% → 18% | 9 → 5 | 10 | 4 → 5 | 0.020 | -0.202 |
| Jogador 4 | 2-3 | 12 | 0.000 | -2.000 | 0 → 0 | 1 → 0 | 18% → 18% | 5 → 8 | 10 | 5 → 5 | -0.000 | 0.234 |
| Jogador 4 | 2-4 | 11 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 6 | 11 | 5 → 5 | 0.003 | 0.000 |
| Jogador 4 | 2-5 | 8 | 4.000 | 6.000 | 0 → 0 | 0 → 1 | 18% → 18% | 6 → 6 | 6 | 5 → 5 | 0.001 | -0.323 |
| Jogador 4 | 2-6 | 10 | 8.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 6 | 8 | 5 → 6 | 0.053 | 0.254 |
| Jogador 4 | 2-7 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 5 | 7 | 6 → 6 | -0.099 | 0.000 |
| Jogador 4 | 3-1 | 6 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 5 → 9 | 6 | 6 → 6 | 0.011 | 0.483 |
| Jogador 4 | 3-2 | 9 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 7 | 11 | 6 → 6 | 0.009 | 0.312 |
| Jogador 4 | 3-3 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 7 | 7 | 6 → 6 | -0.010 | -0.477 |
| Jogador 4 | 3-4 | 4 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 7 → 5 | 7 | 6 → 7 | 0.004 | 0.000 |
| Jogador 4 | 3-5 | 9 | 12.000 | -8.000 | 0 → 1 | 2 → 1 | 21% → 25% | 5 → 6 | 5 | 7 → 7 | 0.062 | 0.328 |
| Jogador 4 | 3-6 | 6 | 0.000 | 10.000 | 1 → 1 | 1 → 3 | 25% → 25% | 6 → 8 | 5 | 7 → 7 | 0.000 | 0.489 |
| Jogador 4 | 3-7 | 7 | 0.000 | 12.000 | 1 → 1 | 3 → 2 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | -0.009 | 0.000 |
| Jogador 4 | 4-1 | 7 | 0.000 | 10.000 | 1 → 1 | 2 → 3 | 25% → 25% | 6 → 6 | 5 | 7 → 7 | -0.002 | -0.409 |
| Jogador 4 | 4-2 | 4 | 0.000 | 12.000 | 1 → 1 | 3 → 3 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | 0.000 | 0.708 |
| Jogador 4 | 4-3 | 8 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 25% → 25% | 6 → 8 | 7 | 7 → 7 | -0.035 | 0.373 |
| Jogador 4 | 4-4 | 9 | 2.000 | 0.000 | 1 → 1 | 3 → 4 | 25% → 25% | 8 → 11 | 9 | 7 → 7 | -0.004 | 0.000 |
| Jogador 4 | 4-5 | 7 | 0.000 | 2.000 | 1 → 1 | 4 → 5 | 25% → 25% | 11 → 17 | 3 | 7 → 7 | 0.003 | 0.000 |
| Jogador 4 | 4-6 | 5 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 25% → 25% | 17 → 23 | 0 | 7 → 7 | -0.005 | -0.580 |
| Jogador 4 | 4-7 | 12 | -6.000 | 4.000 | 1 → 0 | 5 → 6 | 25% → 25% | 23 → 30 | 8 | 7 → 7 | 0.001 | 0.000 |
| Jogador 4 | 5-1 | 7 | 0.000 | 0.000 | 0 → 0 | 6 → 6 | 25% → 25% | 30 → 39 | 0 | 7 → 7 | -0.003 | -0.407 |
| Jogador 4 | 5-2 | 12 | 4.000 | -6.000 | 0 → 2 | 6 → 4 | 25% → 21% | 39 → 41 | 14 | 7 → 7 | -0.010 | 0.000 |
| Jogador 4 | 5-3 | 12 | 6.000 | 6.000 | 2 → 3 | 4 → 3 | 21% → 21% | 41 → 39 | 14 | 7 → 7 | 0.027 | -0.237 |
| Jogador 4 | 5-4 | 12 | 4.000 | -6.000 | 3 → 3 | 3 → 2 | 21% → 25% | 39 → 37 | 18 | 7 → 7 | 0.005 | 0.000 |
| Jogador 4 | 5-5 | 12 | 0.000 | 8.000 | 3 → 3 | 2 → 3 | 25% → 25% | 37 → 31 | 20 | 7 → 7 | 0.000 | -0.246 |
| Jogador 4 | 5-6 | 11 | -60.000 | -66.000 | 3 → 0 | 3 → 0 | 25% → 0% | 31 → 21 | 20 | 7 → 7 | -0.123 | -0.268 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 13, COMPOSITION_COMPATIBILITY: 28, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 21; mudanças de composição: 3; posicionamento melhorou em 66 ações e piorou em 45.
- Jogador 4 — estado final: ouro 21, nível 7, vida 3.0, colocação 4.
| Jogador 5 | 1-1 | 8 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 2 | 2 → 3 | 0.060 | 0.000 |
| Jogador 5 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.012 | 0.000 |
| Jogador 5 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 4 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 8 | 4.000 | -2.000 | 0 → 0 | 1 → 0 | 11% → 11% | 3 → 6 | 2 | 3 → 4 | 0.022 | 0.000 |
| Jogador 5 | 2-1 | 12 | 6.000 | -2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 6 → 5 | 10 | 4 → 4 | 0.014 | -0.211 |
| Jogador 5 | 2-2 | 9 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 14% → 14% | 5 → 8 | 6 | 4 → 4 | -0.032 | 0.285 |
| Jogador 5 | 2-3 | 12 | 0.000 | -6.000 | 0 → 0 | 0 → 0 | 14% → 14% | 8 → 10 | 11 | 4 → 5 | 0.008 | 0.209 |
| Jogador 5 | 2-4 | 10 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 10 → 8 | 11 | 5 → 5 | -0.022 | 0.000 |
| Jogador 5 | 2-5 | 6 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 18% → 18% | 8 → 10 | 3 | 5 → 5 | 0.000 | -0.387 |
| Jogador 5 | 2-6 | 10 | 6.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 21% | 10 → 6 | 10 | 5 → 6 | 0.010 | 0.275 |
| Jogador 5 | 2-7 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 2 | 21% → 21% | 6 → 7 | 6 | 6 → 6 | 0.002 | 0.000 |
| Jogador 5 | 3-1 | 8 | 0.000 | 2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 7 → 9 | 7 | 6 → 6 | 0.005 | 0.363 |
| Jogador 5 | 3-2 | 10 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 7 | 10 | 6 → 6 | 0.003 | -0.263 |
| Jogador 5 | 3-3 | 4 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 13 | 0 | 6 → 6 | 0.007 | 0.713 |
| Jogador 5 | 3-4 | 9 | 6.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 25% | 13 → 8 | 10 | 6 → 7 | -0.002 | 0.000 |
| Jogador 5 | 3-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 15 | 0 | 7 → 7 | 0.046 | 0.733 |
| Jogador 5 | 3-6 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 25% → 25% | 15 → 8 | 14 | 7 → 7 | 0.000 | 0.489 |
| Jogador 5 | 3-7 | 9 | 2.000 | -4.000 | 0 → 0 | 2 → 1 | 25% → 25% | 8 → 7 | 11 | 7 → 7 | -0.001 | 0.000 |
| Jogador 5 | 4-1 | 6 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | 0.000 | 0.481 |
| Jogador 5 | 4-2 | 12 | 8.000 | -2.000 | 0 → 1 | 2 → 1 | 25% → 25% | 7 → 6 | 6 | 7 → 7 | -0.015 | -0.219 |
| Jogador 5 | 4-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 25% → 25% | 6 → 9 | 3 | 7 → 7 | -0.006 | 0.612 |
| Jogador 5 | 4-4 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 9 → 11 | 3 | 7 → 7 | 0.035 | 0.000 |
| Jogador 5 | 4-5 | 5 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 11 → 9 | 9 | 7 → 7 | 0.000 | 0.597 |
| Jogador 5 | 4-6 | 6 | 8.000 | 2.000 | 1 → 1 | 3 → 4 | 25% → 29% | 9 → 6 | 9 | 7 → 8 | 0.006 | 0.000 |
| Jogador 5 | 4-7 | 4 | 0.000 | 10.000 | 1 → 1 | 4 → 5 | 29% → 29% | 6 → 7 | 5 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 10 | -2.000 | 10.000 | 1 → 1 | 5 → 4 | 29% → 29% | 7 → 5 | 7 | 8 → 8 | 0.028 | -0.280 |
| Jogador 5 | 5-2 | 5 | 0.000 | 8.000 | 1 → 1 | 4 → 5 | 29% → 29% | 5 → 7 | 4 | 8 → 8 | -0.006 | 0.584 |
| Jogador 5 | 5-3 | 6 | 0.000 | 0.000 | 1 → 1 | 5 → 6 | 29% → 29% | 7 → 14 | 2 | 8 → 8 | -0.041 | 0.506 |
| Jogador 5 | 5-4 | 12 | -4.000 | 0.000 | 1 → 1 | 6 → 3 | 29% → 25% | 14 → 19 | 18 | 8 → 8 | -0.005 | 0.000 |
| Jogador 5 | 5-5 | 12 | 10.000 | 8.000 | 1 → 1 | 3 → 2 | 25% → 29% | 19 → 10 | 18 | 8 → 8 | 0.030 | -0.233 |
| Jogador 5 | 5-6 | 11 | 0.000 | -10.000 | 1 → 1 | 2 → 2 | 29% → 29% | 10 → 21 | 11 | 8 → 8 | -0.031 | -0.255 |
| Jogador 5 | 5-7 | 5 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 29% → 29% | 21 → 25 | 3 | 8 → 8 | 0.017 | 0.000 |
| Jogador 5 | 6-1 | 12 | 0.000 | -2.000 | 1 → 1 | 3 → 2 | 29% → 29% | 25 → 30 | 16 | 8 → 8 | 0.000 | 0.251 |
| Jogador 5 | 6-2 | 11 | 0.000 | 12.000 | 1 → 1 | 2 → 4 | 29% → 29% | 30 → 29 | 21 | 8 → 8 | 0.001 | 0.280 |
| Jogador 5 | 6-3 | 12 | 4.000 | -10.000 | 1 → 1 | 4 → 3 | 29% → 29% | 29 → 37 | 20 | 8 → 8 | 0.006 | 0.000 |
| Jogador 5 | 6-4 | 11 | 0.000 | 14.000 | 1 → 1 | 3 → 3 | 29% → 29% | 37 → 32 | 21 | 8 → 8 | 0.014 | 0.000 |
| Jogador 5 | 6-5 | 8 | 0.000 | -8.000 | 1 → 1 | 3 → 3 | 29% → 29% | 32 → 43 | 7 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 6-6 | 9 | 0.000 | -6.000 | 1 → 1 | 3 → 3 | 29% → 29% | 43 → 55 | 13 | 8 → 8 | 0.007 | 0.000 |
| Jogador 5 | 6-7 | 5 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 29% → 29% | 55 → 61 | 5 | 8 → 8 | -0.069 | 0.000 |
| Jogador 5 | 7-1 | 10 | -60.000 | -66.000 | 1 → 0 | 3 → 0 | 29% → 0% | 61 → 58 | 13 | 8 → 8 | -0.091 | -0.275 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 22, COMPOSITION_COMPATIBILITY: 30, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 20; mudanças de composição: 0; posicionamento melhorou em 63 ações e piorou em 53.
- Jogador 5 — estado final: ouro 58, nível 8, vida 20.0, colocação 2.
| Jogador 6 | 1-1 | 8 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 2 | 2 → 3 | 0.061 | 0.000 |
| Jogador 6 | 1-2 | 11 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 4 | 3 → 3 | 0.021 | 0.000 |
| Jogador 6 | 1-3 | 8 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 5 | 5 | 3 → 3 | -0.030 | 0.000 |
| Jogador 6 | 1-4 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 5 → 4 | 8 | 3 → 4 | -0.002 | 0.000 |
| Jogador 6 | 2-1 | 11 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.002 | -0.216 |
| Jogador 6 | 2-2 | 7 | 6.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 18% | 6 → 6 | 7 | 4 → 5 | 0.029 | 0.366 |
| Jogador 6 | 2-3 | 8 | 2.000 | 4.000 | 0 → 0 | 0 → 1 | 18% → 18% | 6 → 8 | 5 | 5 → 5 | 0.002 | -0.290 |
| Jogador 6 | 2-4 | 10 | 4.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 12 | 3 | 5 → 5 | -0.003 | 0.000 |
| Jogador 6 | 2-5 | 10 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 12 → 7 | 15 | 5 → 6 | -0.011 | 0.280 |
| Jogador 6 | 2-6 | 8 | 6.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 7 → 8 | 6 | 6 → 6 | 0.028 | 0.344 |
| Jogador 6 | 2-7 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 8 → 6 | 14 | 6 → 6 | 0.010 | 0.000 |
| Jogador 6 | 3-1 | 12 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 7 | 10 | 6 → 6 | -0.005 | -0.224 |
| Jogador 6 | 3-2 | 6 | 0.000 | -2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 7 → 14 | 3 | 6 → 6 | 0.001 | -0.430 |
| Jogador 6 | 3-3 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 14 → 21 | 0 | 6 → 6 | 0.000 | 0.560 |
| Jogador 6 | 3-4 | 5 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 21% → 21% | 21 → 28 | 0 | 6 → 6 | -0.011 | 0.000 |
| Jogador 6 | 3-5 | 12 | 0.000 | 2.000 | 0 → 0 | 2 → 2 | 21% → 21% | 28 → 21 | 17 | 6 → 7 | 0.004 | -0.230 |
| Jogador 6 | 3-6 | 8 | 6.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 25% | 21 → 9 | 18 | 7 → 7 | 0.013 | 0.373 |
| Jogador 6 | 3-7 | 6 | 0.000 | 18.000 | 0 → 0 | 2 → 2 | 25% → 25% | 9 → 5 | 9 | 7 → 7 | -0.021 | 0.000 |
| Jogador 6 | 4-1 | 9 | 0.000 | 4.000 | 0 → 0 | 2 → 1 | 25% → 25% | 5 → 7 | 5 | 7 → 7 | -0.030 | 0.317 |
| Jogador 6 | 4-2 | 9 | 2.000 | 10.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 6 | 6 | 7 → 7 | 0.043 | -0.322 |
| Jogador 6 | 4-3 | 6 | 0.000 | 12.000 | 0 → 0 | 1 → 2 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | -0.052 | -0.461 |
| Jogador 6 | 4-4 | 11 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 25% → 25% | 6 → 7 | 11 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 12 | 0.000 | 0.000 | 0 → 1 | 3 → 2 | 25% → 21% | 7 → 6 | 18 | 7 → 7 | -0.015 | -0.235 |
| Jogador 6 | 4-6 | 12 | 12.000 | -10.000 | 1 → 2 | 2 → 1 | 21% → 25% | 6 → 6 | 9 | 7 → 7 | 0.023 | -0.243 |
| Jogador 6 | 4-7 | 11 | 2.000 | 4.000 | 2 → 3 | 1 → 1 | 25% → 25% | 6 → 6 | 9 | 7 → 7 | 0.039 | 0.000 |
| Jogador 6 | 5-1 | 9 | 0.000 | 2.000 | 3 → 3 | 1 → 2 | 25% → 25% | 6 → 7 | 5 | 7 → 7 | -0.033 | 0.336 |
| Jogador 6 | 5-2 | 12 | -52.000 | -54.000 | 3 → 0 | 2 → 0 | 25% → 0% | 7 → 3 | 16 | 7 → 7 | -0.068 | -0.229 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 33, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 50 ações e piorou em 41.
- Jogador 6 — estado final: ouro 3, nível 7, vida 9.0, colocação 5.
| Jogador 7 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.016 | 0.000 |
| Jogador 7 | 1-3 | 8 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 4 | 3 → 3 | -0.004 | 0.000 |
| Jogador 7 | 1-4 | 9 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 3 | 3 → 4 | 0.034 | 0.000 |
| Jogador 7 | 2-1 | 12 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 10 | 6 | 4 → 4 | -0.018 | 0.224 |
| Jogador 7 | 2-2 | 12 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 10 → 8 | 13 | 4 → 5 | 0.006 | 0.205 |
| Jogador 7 | 2-3 | 11 | 4.000 | 4.000 | 0 → 0 | 0 → 1 | 14% → 18% | 8 → 7 | 11 | 5 → 5 | 0.021 | 0.224 |
| Jogador 7 | 2-4 | 8 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 6 | 11 | 5 → 5 | -0.007 | 0.000 |
| Jogador 7 | 2-5 | 10 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 8 | 10 | 5 → 6 | 0.003 | 0.275 |
| Jogador 7 | 2-6 | 12 | 6.000 | -2.000 | 0 → 1 | 1 → 0 | 18% → 18% | 8 → 9 | 7 | 6 → 6 | 0.048 | -0.215 |
| Jogador 7 | 2-7 | 7 | 4.000 | -4.000 | 1 → 1 | 0 → 0 | 18% → 21% | 9 → 14 | 0 | 6 → 6 | -0.095 | 0.000 |
| Jogador 7 | 3-1 | 8 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 14 → 9 | 11 | 6 → 6 | 0.008 | 0.351 |
| Jogador 7 | 3-2 | 5 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 21% | 9 → 17 | 0 | 6 → 6 | 0.000 | 0.552 |
| Jogador 7 | 3-3 | 4 | 2.000 | -2.000 | 1 → 1 | 0 → 0 | 21% → 21% | 17 → 25 | 0 | 6 → 6 | 0.002 | 0.715 |
| Jogador 7 | 3-4 | 8 | 0.000 | 2.000 | 1 → 1 | 0 → 1 | 21% → 21% | 25 → 32 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 3-5 | 11 | -2.000 | -6.000 | 1 → 1 | 1 → 0 | 21% → 18% | 32 → 44 | 3 | 6 → 6 | -0.011 | 0.256 |
| Jogador 7 | 3-6 | 12 | 16.000 | 0.000 | 1 → 1 | 0 → 1 | 18% → 25% | 44 → 30 | 24 | 6 → 7 | 0.016 | 0.254 |
| Jogador 7 | 3-7 | 10 | 0.000 | 14.000 | 1 → 1 | 1 → 3 | 25% → 25% | 30 → 10 | 27 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 6 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 10 → 11 | 8 | 7 → 7 | 0.000 | 0.506 |
| Jogador 7 | 4-2 | 10 | 0.000 | -10.000 | 1 → 1 | 3 → 1 | 25% → 25% | 11 → 9 | 18 | 7 → 7 | 0.006 | 0.306 |
| Jogador 7 | 4-3 | 7 | 8.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 29% | 9 → 10 | 10 | 7 → 8 | 0.004 | 0.434 |
| Jogador 7 | 4-4 | 5 | 0.000 | 18.000 | 1 → 1 | 1 → 1 | 29% → 29% | 10 → 9 | 9 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 5 | 0.000 | 18.000 | 1 → 1 | 1 → 2 | 29% → 29% | 9 → 9 | 9 | 8 → 8 | 0.000 | 0.602 |
| Jogador 7 | 4-6 | 12 | 0.000 | 8.000 | 1 → 1 | 2 → 3 | 29% → 29% | 9 → 12 | 16 | 8 → 8 | 0.000 | 0.255 |
| Jogador 7 | 4-7 | 12 | 4.000 | 2.000 | 1 → 1 | 3 → 4 | 29% → 29% | 12 → 12 | 19 | 8 → 8 | 0.025 | 0.000 |
| Jogador 7 | 5-1 | 11 | -2.000 | 6.000 | 1 → 1 | 4 → 2 | 29% → 29% | 12 → 10 | 14 | 8 → 8 | -0.065 | 0.270 |
| Jogador 7 | 5-2 | 9 | 0.000 | 16.000 | 1 → 1 | 2 → 2 | 29% → 29% | 10 → 9 | 15 | 8 → 8 | -0.007 | 0.330 |
| Jogador 7 | 5-3 | 12 | 0.000 | -6.000 | 1 → 1 | 2 → 4 | 29% → 29% | 9 → 22 | 19 | 8 → 8 | 0.014 | 0.248 |
| Jogador 7 | 5-4 | 12 | -6.000 | 4.000 | 1 → 2 | 4 → 2 | 29% → 25% | 22 → 25 | 10 | 8 → 8 | -0.028 | 0.000 |
| Jogador 7 | 5-5 | 6 | 18.000 | -10.000 | 2 → 3 | 2 → 2 | 25% → 29% | 25 → 32 | 4 | 8 → 8 | -0.059 | 0.495 |
| Jogador 7 | 5-6 | 11 | 0.000 | -2.000 | 3 → 3 | 2 → 3 | 29% → 29% | 32 → 41 | 11 | 8 → 8 | 0.015 | 0.270 |
| Jogador 7 | 5-7 | 12 | 0.000 | 6.000 | 3 → 3 | 3 → 3 | 29% → 29% | 41 → 43 | 21 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 12 | 0.000 | -8.000 | 3 → 3 | 3 → 3 | 29% → 29% | 43 → 55 | 15 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-2 | 11 | -8.000 | 6.000 | 3 → 3 | 3 → 3 | 29% → 25% | 55 → 63 | 17 | 8 → 8 | -0.001 | -0.264 |
| Jogador 7 | 6-3 | 12 | -2.000 | 8.000 | 3 → 3 | 3 → 2 | 25% → 25% | 63 → 63 | 20 | 8 → 8 | -0.004 | -0.242 |
| Jogador 7 | 6-4 | 11 | 16.000 | 2.000 | 3 → 4 | 2 → 2 | 25% → 29% | 63 → 58 | 24 | 8 → 8 | 0.009 | 0.000 |
| Jogador 7 | 6-5 | 8 | 0.000 | -12.000 | 4 → 4 | 2 → 4 | 29% → 29% | 58 → 72 | 13 | 8 → 8 | 0.008 | -0.356 |
| Jogador 7 | 6-6 | 7 | 2.000 | 0.000 | 4 → 4 | 4 → 3 | 29% → 29% | 72 → 80 | 6 | 8 → 8 | 0.001 | 0.434 |
| Jogador 7 | 6-7 | 10 | 0.000 | 2.000 | 4 → 4 | 3 → 4 | 29% → 29% | 80 → 86 | 17 | 8 → 8 | 0.006 | 0.000 |
| Jogador 7 | 7-1 | 10 | 0.000 | -4.000 | 4 → 4 | 4 → 4 | 29% → 29% | 86 → 83 | 13 | 8 → 8 | 0.000 | 0.297 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 36, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 21; mudanças de composição: 0; posicionamento melhorou em 61 ações e piorou em 50.
- Jogador 7 — estado final: ouro 83, nível 8, vida 40.0, colocação 1.
| Jogador 8 | 1-1 | 8 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 2 | 2 → 3 | 0.061 | 0.000 |
| Jogador 8 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.010 | 0.000 |
| Jogador 8 | 1-3 | 9 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 4 | 3 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 12 | -2.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 7% | 4 → 9 | 4 | 3 → 4 | -0.005 | 0.000 |
| Jogador 8 | 2-1 | 12 | 6.000 | -2.000 | 0 → 0 | 1 → 1 | 7% → 14% | 9 → 12 | 4 | 4 → 4 | 0.023 | -0.211 |
| Jogador 8 | 2-2 | 12 | 4.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 14% | 12 → 6 | 14 | 4 → 5 | 0.004 | -0.202 |
| Jogador 8 | 2-3 | 12 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 6 → 9 | 11 | 5 → 5 | 0.017 | -0.220 |
| Jogador 8 | 2-4 | 12 | 6.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 18% | 9 → 6 | 10 | 5 → 5 | 0.004 | 0.000 |
| Jogador 8 | 2-5 | 4 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 12 | 0 | 5 → 5 | 0.040 | -0.634 |
| Jogador 8 | 2-6 | 11 | 4.000 | 4.000 | 0 → 0 | 1 → 0 | 18% → 21% | 12 → 7 | 14 | 5 → 6 | -0.027 | -0.235 |
| Jogador 8 | 2-7 | 8 | 0.000 | -4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 7 → 8 | 12 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 7 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 9 | 8 | 6 → 6 | 0.061 | -0.389 |
| Jogador 8 | 3-2 | 4 | 0.000 | 12.000 | 0 → 0 | 0 → 1 | 21% → 21% | 9 → 11 | 6 | 6 → 6 | -0.000 | -0.681 |
| Jogador 8 | 3-3 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 11 → 8 | 11 | 6 → 6 | 0.000 | -0.537 |
| Jogador 8 | 3-4 | 6 | 4.000 | 4.000 | 0 → 0 | 2 → 2 | 21% → 25% | 8 → 8 | 8 | 6 → 7 | -0.078 | 0.000 |
| Jogador 8 | 3-5 | 5 | 0.000 | 16.000 | 0 → 0 | 2 → 3 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | 0.000 | 0.562 |
| Jogador 8 | 3-6 | 12 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 6 | 8 | 7 → 7 | -0.020 | -0.230 |
| Jogador 8 | 3-7 | 12 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 25% → 21% | 6 → 5 | 11 | 7 → 7 | -0.033 | 0.000 |
| Jogador 8 | 4-1 | 7 | 8.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 25% | 5 → 7 | 4 | 7 → 7 | 0.001 | -0.388 |
| Jogador 8 | 4-2 | 12 | 0.000 | -8.000 | 0 → 0 | 3 → 4 | 25% → 25% | 7 → 12 | 15 | 7 → 7 | 0.005 | 0.243 |
| Jogador 8 | 4-3 | 12 | -44.000 | -44.000 | 0 → 0 | 4 → 0 | 25% → 0% | 12 → 0 | 16 | 7 → 7 | -0.028 | -0.240 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 42 ações e piorou em 31.
- Jogador 8 — estado final: ouro 0, nível 7, vida 12.0, colocação 6.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 46 | 25 | 2 | 3 | 4 | 3 | 0 | 1 | 1 | 2 | 2 | 0 |
| Jogador 2 | 75 | 50 | 1 | 2 | 3 | 1 | 0 | 0 | 10 | 2 | 2 | 0 |
| Jogador 3 | 41 | 19 | 0 | 0 | 1 | 1 | 0 | 0 | 3 | 1 | 0 | 0 |
| Jogador 4 | 70 | 40 | 2 | 3 | 3 | 7 | 0 | 0 | 3 | 3 | 4 | 0 |
| Jogador 5 | 80 | 48 | 1 | 3 | 4 | 0 | 0 | 1 | 10 | 3 | 2 | 0 |
| Jogador 6 | 58 | 33 | 3 | 3 | 4 | 0 | 0 | 2 | 4 | 5 | 4 | 0 |
| Jogador 7 | 98 | 63 | 4 | 4 | 5 | 0 | 0 | 0 | 18 | 4 | 0 | 0 |
| Jogador 8 | 52 | 33 | 4 | 4 | 8 | 3 | 0 | 0 | 3 | 2 | 4 | 0 |
- Jogador 1 — venda DA_KogMaw18_AD (2-6, step 219): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Elise (2-6, step 222): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Elise (3-3, step 292): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Vi18 (4-2, step 404): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Vi18 (3-1, step 254): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Teemo (4-1, step 390): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Sejuani (4-2, step 411): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_MasterYi_AD (4-5, step 453): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Fiddlesticks18 (4-7, step 484): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rammus (4-7, step 487): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_CrimsonRaptor18 (5-1, step 504): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Yorick (5-3, step 530): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Lillia (5-6, step 573): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_MasterYi_AD (6-1, step 598): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Yorick (6-1, step 600): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Varus (6-1, step 605): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Sejuani (2-7, step 240): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Elise (3-7, step 371): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_CrimsonRaptor18 (3-1, step 255): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Scuttlecrab18 (4-7, step 484): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_Krug18 (4-7, step 489): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Hecarim (5-5, step 559): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Fiddlesticks18 (5-6, step 572): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Caitlyn (3-1, step 254): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-2, step 272): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_Murkwolf18 (3-7, step 372): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Caitlyn (5-4, step 542): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Rengar (5-4, step 547): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Rammus (6-1, step 598): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Akali_AD (6-1, step 600): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Lillia (6-2, step 614): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_Fiddlesticks18 (6-3, step 622): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=True, compensações posteriores=3.
- Jogador 5 — venda DA_18_Rammus (6-3, step 631): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Caitlyn (6-5, step 651): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Morgana (6-6, step 654): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Karma18 (6-6, step 660): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (2-7, step 235): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (2-7, step 237): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Tristana (3-1, step 262): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Ahri (3-2, step 272): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 6 — venda DA_18_Rammus (4-5, step 452): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_Diana (4-6, step 467): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_Diana (5-2, step 514): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_CrimsonRaptor18 (2-5, step 201): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (2-6, step 219): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_Shen (3-5, step 334): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 7 — venda DA_18_Rengar (4-2, step 405): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Aphelios (4-2, step 407): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rengar (4-7, step 488): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_KogMaw18_AD (5-3, step 531): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (5-3, step 536): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Diana (7-1, step 673): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (7-1, step 680): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_RekSai (2-6, step 217): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_RekSai (2-6, step 219): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (2-7, step 235): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (2-7, step 238): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_KhaZix (3-7, step 375): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Gromp18_AP (4-2, step 402): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_RekSai (4-3, step 424): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **60**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 1-3 | 60 | PURCHASE_SALE_REVIEW | Compra de DA_18_Xayah foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 1 | 2-1 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Veigar) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 1 | 2-4 | 178 | PURCHASE_SALE_REVIEW | Compra de DA_KogMaw18_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 1 | 2-4 | 180 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 1 | 2-6 | 219 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 2-6 | 219 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 2-6 | 222 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 2-7 | 237 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 3-3 | 292 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-2 | 404 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-3 | 857 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-4 | 1013 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-5 | 1098 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 1253 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1347 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1474 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1581 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1731 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1829 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1931 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 2055 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 2056 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 2155 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 2156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 2268 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 2269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 2429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2430 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 2581 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 4-3 | 2582 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 2-4 | 1038 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 1 | 1-2 | 273 | TEXT_MOVE_OSCILLATION | Possível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados. |
| LOW | Jogador 2 | 2-1 | 112 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 2-1 | 114 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-3 | 152 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Veigar) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-3 | 161 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 2 | 3-1 | 254 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-1 | 257 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yorick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 4-1 | 390 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-2 | 411 | SOLD_CORE_UNIT | Venda de 'DA_18_Sejuani' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-5 | 453 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-7 | 484 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 5-1 | 504 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-3 | 530 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-6 | 573 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Lillia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-1 | 598 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-1 | 600 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-1 | 605 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Varus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-4 | 355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-3 | 811 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 2-5 | 977 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 2-6 | 1097 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 2-7 | 1168 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-1 | 1324 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-2 | 1461 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-3 | 1592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-4 | 1691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1947 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 2179 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 2343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2508 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2797 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2871 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 3031 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 3194 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 3354 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 3469 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 3570 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 3649 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3767 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-7 | 3872 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-1 | 4034 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-2 | 4195 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-3 | 4298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-4 | 4453 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-5 | 4544 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-6 | 4660 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 6-6 | 4661 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-1 | 586 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-1 | 2267 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-2 | 2445 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-3 | 2546 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-3 | 2583 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-6 | 2934 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-7 | 3159 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-1 | 3244 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-1 | 3306 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-3 | 3547 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-4 | 3626 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-5 | 3744 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-6 | 3849 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 4011 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 2 | 1-1 | 128 | TEXT_MOVE_OSCILLATION | Possível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados. |
| MEDIUM | Jogador 3 | 1-4 | 83 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 3 | 3-7 | 371 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-2 | 603 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-2 | 604 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-3 | 702 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-4 | 835 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 935 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 1105 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1568 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1713 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1876 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 2024 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 2184 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 2347 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-1 | 2348 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2411 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 2577 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 4-3 | 2578 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 3-3 | 1618 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-4 | 1788 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-5 | 1938 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-6 | 2161 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-7 | 2324 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-1 | 2388 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 1-4 | 92 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 4 | 2-1 | 113 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Veigar) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 4 | 2-3 | 154 | PURCHASE_SALE_REVIEW | Compra de DA_KogMaw18_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 4 | 2-3 | 160 | PURCHASE_SALE_REVIEW | Compra de DA_18_Camille foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 2-4 | 183 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 4 | 2-7 | 235 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 4 | 3-1 | 255 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 3-2 | 272 | PURCHASE_SALE_REVIEW | Compra de DA_Gromp18_AP foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 4-7 | 489 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Krug18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 5-5 | 559 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 5-6 | 572 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 2-6 | 222 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 4 | 3-5 | 333 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 4 | 5-1 | 511 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 4 | 5-3 | 534 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 4 | 5-5 | 571 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| LOW | Jogador 4 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 2-4 | 1091 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-5 | 1205 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-6 | 1344 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-7 | 1427 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-7 | 1428 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-1 | 1513 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-1 | 1514 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-2 | 1632 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-2 | 1633 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-3 | 1715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 1775 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1776 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 1897 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 1980 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 1981 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 2080 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 2081 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 2182 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-1 | 2183 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2243 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-2 | 2244 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2356 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 2477 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2478 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2575 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 2647 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 2648 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 2808 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-1 | 2907 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-1 | 2908 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-2 | 3072 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-2 | 3073 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-6 | 3714 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-6 | 3715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 4-3 | 2394 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-6 | 2734 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-1 | 3049 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-2 | 3215 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-3 | 3374 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-4 | 3537 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 5 | 2-1 | 112 | PURCHASE_SALE_REVIEW | Compra de DA_18_LeBlanc foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 2-3 | 155 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rakan) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-3 | 157 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-3 | 160 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 2-4 | 180 | PURCHASE_SALE_REVIEW | Compra de DA_18_LeBlanc foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 2-7 | 235 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-1 | 254 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-4 | 542 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-4 | 547 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-1 | 598 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-1 | 600 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-3 | 631 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-5 | 651 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 6-6 | 654 | SOLD_CORE_UNIT | Venda de 'DA_18_Morgana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-6 | 660 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Karma18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 104 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-4 | 967 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-5 | 1054 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-6 | 1187 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-7 | 1281 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-1 | 1393 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-2 | 1529 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-3 | 1593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-4 | 1717 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-5 | 1777 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-6 | 1859 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-7 | 1982 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-1 | 2068 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-2 | 2242 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-3 | 2318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 2478 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2564 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2625 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 2763 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 2843 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 2934 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3098 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3258 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3409 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 3485 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 3650 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-2 | 3805 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-3 | 3966 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-4 | 4117 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-5 | 4234 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-6 | 4363 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-7 | 4437 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 7-1 | 4577 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 7-1 | 4578 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 4-5 | 2506 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-3 | 2975 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-3 | 3038 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-4 | 3150 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-6 | 3462 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-7 | 3627 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 6-2 | 3943 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 6-6 | 4414 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 1-2 | 32 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yorick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 1-2 | 38 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 1-3 | 60 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 6 | 1-4 | 87 | PURCHASE_SALE_REVIEW | Compra de DA_18_Camille foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 2-5 | 199 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Varus) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 2-7 | 235 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 2-7 | 237 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 2-7 | 237 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 3-1 | 262 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 3-2 | 272 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ahri) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 6 | 3-5 | 337 | PURCHASE_SALE_REVIEW | Compra de DA_18_LeBlanc foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 5-2 | 514 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 1-1 | 104 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 247 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 2-2 | 729 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 841 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 842 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-4 | 983 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 984 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-5 | 1112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 1113 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-6 | 1224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-7 | 1379 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1380 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-1 | 1541 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-2 | 1624 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-3 | 1695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1766 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1918 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 2023 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 2108 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 2109 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2353 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2438 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2439 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2756 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2757 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 2926 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 3079 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 3080 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 3206 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 3207 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 3372 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-2 | 3373 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 2-4 | 1044 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 1055 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 1078 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 1-4 | 89 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-1 | 115 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-2 | 136 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 7 | 2-5 | 201 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 2-5 | 201 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_CrimsonRaptor18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 4-2 | 405 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-2 | 407 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Aphelios' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-3 | 422 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 7 | 5-3 | 531 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-3 | 536 | SOLD_CORE_UNIT | Venda de 'DA_18_Hecarim' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 7-1 | 673 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 7-1 | 680 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 2-1 | 584 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-2 | 737 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-3 | 879 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-4 | 986 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-5 | 1117 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 1285 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1380 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1486 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1618 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1726 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1876 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 2155 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2238 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2467 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2539 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2611 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2768 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2925 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 3072 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 3197 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 3357 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 3521 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 3609 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 3610 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 3761 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-6 | 3762 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 3929 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 3930 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 4099 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-1 | 4100 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-2 | 4254 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-2 | 4255 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-3 | 4412 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-3 | 4413 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-4 | 4559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-4 | 4560 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 4670 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-5 | 4671 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-6 | 4772 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-6 | 4773 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-7 | 4910 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-7 | 4911 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 7-1 | 5048 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 7-1 | 5049 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| MEDIUM | Jogador 7 | 2-2 | 821 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-3 | 952 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 6-3 | 4511 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-2 | 32 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 1-3 | 58 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 1-3 | 60 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 1-4 | 90 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-1 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-1 | 115 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-3 | 154 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 2-3 | 156 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-3 | 160 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-4 | 176 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-6 | 217 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-6 | 219 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 2-7 | 235 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-7 | 235 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Tristana) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 8 | 2-7 | 238 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 3-1 | 254 | PURCHASE_SALE_REVIEW | Compra de DA_18_Akali_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 3-7 | 375 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-2 | 402 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-3 | 424 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 104 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-4 | 497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 2-4 | 1134 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-5 | 1193 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-1 | 1539 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1602 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1672 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1755 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1827 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 2148 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 2149 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2247 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2248 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2408 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2569 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 4-3 | 2570 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
