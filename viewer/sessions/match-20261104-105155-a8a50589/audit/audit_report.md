# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5158**
- Achados: **526**
- CRITICAL: 0 | HIGH: 32 | MEDIUM: 213 | LOW: 281

## Metadados da sessão

- Match ID: a8a50589-4471-4a2d-be8c-c176d8e53733
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: d93d307394469a36a4193b2b3355d6af76e1605d4e74763f494123bd6059e230
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4358**
- Entradas posteriores à eliminação ignoradas: **800**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 106 | 7 | 13 | 29 | 111 | 14 | 5 | não/inconclusivo | 0 |
| Jogador 6 | 0 | 8 | 23 | 4 | 65 | 6 | 6 | não/inconclusivo | 0 |
| Jogador 7 | 90 | 7 | 12 | 17 | 91 | 15 | 1 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 170 | 59 | 42 | 18 | 0 | 9 | 37 | 0.0391 | 9 | 22 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::MOVE_BOARD: 3, ALL_IN::PASS: 1, FAST8::BUY: 13, FAST8::BUY_XP: 13, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 8, FAST8::PASS: 2, FAST8::SELL: 11, LOSS_STREAK::BUY: 4, LOSS_STREAK::BUY_XP: 1, LOSS_STREAK::MOVE_BOARD: 1, LOSS_STREAK::SELL: 4, SLOWROLL::BUY: 2, STABILIZE::BUY: 37, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 11, STABILIZE::PASS: 6, STABILIZE::SELL: 27
- Jogador 1 — recompensas por ação: BUY: média 0.3085 (n=59), BUY_XP: média -0.0261 (n=18), ITEM: média 0.1020 (n=5), MOVE_BENCH: média -0.0164 (n=14), MOVE_BOARD: média -0.0070 (n=23), PASS: média -0.0078 (n=9), SELL: média -0.2650 (n=42)
| Jogador 2 | 192 | 65 | 37 | 0 | 14 | 14 | 53 | 0.0544 | 25 | 20 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 4, ALL_IN::PASS: 1, ALL_IN::REROLL: 6, ALL_IN::SELL: 3, FAST8::BUY: 3, FAST8::MOVE_BENCH: 1, FAST8::REROLL: 2, FAST8::SELL: 3, SLOWROLL::BUY: 11, SLOWROLL::ITEM: 2, SLOWROLL::MOVE_BENCH: 10, SLOWROLL::MOVE_BOARD: 2, SLOWROLL::PASS: 3, SLOWROLL::SELL: 1, STABILIZE::BUY: 42, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 29, STABILIZE::MOVE_BOARD: 7, STABILIZE::PASS: 10, STABILIZE::REROLL: 6, STABILIZE::SELL: 30
- Jogador 2 — recompensas por ação: BUY: média 0.3657 (n=65), ITEM: média 0.0978 (n=9), MOVE_BENCH: média -0.0952 (n=44), MOVE_BOARD: média -0.0067 (n=9), PASS: média -0.1021 (n=14), REROLL: média -0.0900 (n=14), SELL: média -0.1962 (n=37)
| Jogador 3 | 163 | 64 | 43 | 6 | 8 | 5 | 30 | 0.0874 | 7 | 16 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 2, FAST8::BUY: 12, FAST8::BUY_XP: 3, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 4, FAST8::PASS: 2, FAST8::REROLL: 1, FAST8::SELL: 2, LOSS_STREAK::BUY: 3, LOSS_STREAK::MOVE_BENCH: 2, LOSS_STREAK::MOVE_BOARD: 2, LOSS_STREAK::SELL: 3, SLOWROLL::BUY: 13, SLOWROLL::BUY_XP: 3, SLOWROLL::ITEM: 1, SLOWROLL::MOVE_BENCH: 2, SLOWROLL::MOVE_BOARD: 3, SLOWROLL::SELL: 12, STABILIZE::BUY: 31, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 3, STABILIZE::PASS: 3, STABILIZE::REROLL: 6, STABILIZE::SELL: 24
- Jogador 3 — recompensas por ação: BUY: média 0.3398 (n=64), BUY_XP: média -0.0233 (n=6), ITEM: média 0.1329 (n=7), MOVE_BENCH: média 0.0644 (n=18), MOVE_BOARD: média -0.0075 (n=12), PASS: média -0.0320 (n=5), REROLL: média -0.1087 (n=8), SELL: média -0.1937 (n=43)
| Jogador 4 | 313 | 111 | 68 | 13 | 27 | 9 | 66 | 0.1343 | 19 | 55 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 4, ALL_IN::SELL: 1, FAST8::BUY: 68, FAST8::BUY_XP: 9, FAST8::ITEM: 14, FAST8::MOVE_BENCH: 22, FAST8::MOVE_BOARD: 25, FAST8::PASS: 7, FAST8::REROLL: 17, FAST8::SELL: 35, SLOWROLL::BUY: 8, SLOWROLL::BUY_XP: 3, SLOWROLL::MOVE_BENCH: 2, SLOWROLL::MOVE_BOARD: 2, SLOWROLL::SELL: 6, STABILIZE::BUY: 32, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 4, STABILIZE::PASS: 2, STABILIZE::REROLL: 6, STABILIZE::SELL: 26
- Jogador 4 — recompensas por ação: BUY: média 0.4135 (n=111), BUY_XP: média -0.0515 (n=13), ITEM: média 0.1132 (n=19), MOVE_BENCH: média 0.1554 (n=35), MOVE_BOARD: média 0.0123 (n=31), PASS: média 0.0000 (n=9), REROLL: média -0.1056 (n=27), SELL: média -0.1225 (n=68)
| Jogador 5 | 253 | 77 | 53 | 24 | 4 | 16 | 70 | 0.0426 | 12 | 41 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 5, ALL_IN::PASS: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 4, ECON::BUY: 19, ECON::BUY_XP: 2, ECON::ITEM: 2, ECON::MOVE_BENCH: 5, ECON::MOVE_BOARD: 18, ECON::PASS: 6, ECON::REROLL: 2, ECON::SELL: 10, FAST8::BUY: 20, FAST8::BUY_XP: 18, FAST8::ITEM: 3, FAST8::MOVE_BENCH: 6, FAST8::MOVE_BOARD: 9, FAST8::PASS: 3, FAST8::SELL: 17, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 3, SLOWROLL::MOVE_BENCH: 9, SLOWROLL::MOVE_BOARD: 2, SLOWROLL::PASS: 2, SLOWROLL::SELL: 1, STABILIZE::BUY: 25, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 4, STABILIZE::PASS: 3, STABILIZE::SELL: 21, WINSTREAK::BUY: 2, WINSTREAK::MOVE_BOARD: 2, WINSTREAK::PASS: 1
- Jogador 5 — recompensas por ação: BUY: média 0.2292 (n=77), BUY_XP: média -0.0387 (n=24), ITEM: média 0.1189 (n=9), MOVE_BENCH: média 0.0317 (n=35), MOVE_BOARD: média -0.0103 (n=35), PASS: média -0.0200 (n=16), REROLL: média -0.1450 (n=4), SELL: média -0.1294 (n=53)
| Jogador 6 | 223 | 65 | 47 | 23 | 0 | 17 | 60 | 0.0450 | 32 | 27 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::MOVE_BOARD: 3, ALL_IN::PASS: 1, ECON::BUY: 5, ECON::BUY_XP: 2, ECON::MOVE_BENCH: 1, ECON::MOVE_BOARD: 4, ECON::PASS: 2, ECON::SELL: 3, FAST8::BUY: 24, FAST8::BUY_XP: 15, FAST8::ITEM: 7, FAST8::MOVE_BENCH: 15, FAST8::MOVE_BOARD: 17, FAST8::PASS: 8, FAST8::SELL: 20, SLOWROLL::BUY: 7, SLOWROLL::BUY_XP: 5, SLOWROLL::MOVE_BENCH: 1, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::SELL: 6, STABILIZE::BUY: 27, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 8, STABILIZE::MOVE_BOARD: 10, STABILIZE::PASS: 6, STABILIZE::SELL: 18
- Jogador 6 — recompensas por ação: BUY: média 0.2409 (n=65), BUY_XP: média -0.0261 (n=23), ITEM: média 0.1245 (n=11), MOVE_BENCH: média 0.0544 (n=25), MOVE_BOARD: média -0.0049 (n=35), PASS: média -0.0029 (n=17), SELL: média -0.1602 (n=47)
| Jogador 7 | 238 | 91 | 73 | 12 | 13 | 6 | 34 | 0.0591 | 9 | 20 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::REROLL: 2, ALL_IN::SELL: 4, FAST8::BUY: 39, FAST8::BUY_XP: 8, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 6, FAST8::MOVE_BOARD: 10, FAST8::PASS: 2, FAST8::REROLL: 7, FAST8::SELL: 28, SLOWROLL::BUY: 1, STABILIZE::BUY: 48, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 4, STABILIZE::PASS: 4, STABILIZE::REROLL: 4, STABILIZE::SELL: 41
- Jogador 7 — recompensas por ação: BUY: média 0.2630 (n=91), BUY_XP: média -0.0267 (n=12), ITEM: média 0.1278 (n=9), MOVE_BENCH: média 0.0645 (n=20), MOVE_BOARD: média -0.0064 (n=14), PASS: média -0.0367 (n=6), REROLL: média -0.1231 (n=13), SELL: média -0.1379 (n=73)
| Jogador 8 | 312 | 119 | 76 | 16 | 25 | 8 | 54 | 0.1067 | 40 | 28 |
- Jogador 8 — ações por estratégia: FAST8::BUY: 63, FAST8::BUY_XP: 11, FAST8::ITEM: 9, FAST8::MOVE_BENCH: 9, FAST8::MOVE_BOARD: 19, FAST8::OTHER: 1, FAST8::PASS: 6, FAST8::REROLL: 20, FAST8::SELL: 37, SLOWROLL::BUY: 1, SLOWROLL::BUY_XP: 1, STABILIZE::BUY: 35, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 7, STABILIZE::PASS: 2, STABILIZE::SELL: 29, WINSTREAK::BUY: 20, WINSTREAK::ITEM: 1, WINSTREAK::MOVE_BENCH: 7, WINSTREAK::MOVE_BOARD: 1, WINSTREAK::OTHER: 1, WINSTREAK::REROLL: 5, WINSTREAK::SELL: 10
- Jogador 8 — recompensas por ação: BUY: média 0.3377 (n=119), BUY_XP: média -0.0381 (n=16), ITEM: média 0.1417 (n=12), MOVE_BENCH: média 0.2082 (n=27), MOVE_BOARD: média 0.0019 (n=27), OTHER: média -0.0100 (n=2), PASS: média -0.0075 (n=8), REROLL: média -0.1268 (n=25), SELL: média -0.1368 (n=76)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 10:51:57 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | 0.0000 |  |
| Jogador 1 | ? | 10:51:58 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 1 | ? | 10:51:58 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 1 | ? | 10:51:59 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 1 | ? | 10:52:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-1 | 10:52:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 1 | 1-1 | 10:52:05 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.4400 |  |
| Jogador 1 | 1-1 | 10:52:05 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 1 | 1-1 | 10:52:06 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1100 |  |
| Jogador 1 | 1-1 | 10:52:07 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 1 | 1-1 | 10:52:07 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 1 | 1-1 | 10:52:08 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 1 | 1-1 | 10:52:09 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.3800 |  |
| Jogador 1 | 1-1 | 10:52:09 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 1 | 1-2 | 10:52:11 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.3800 |  |
| Jogador 1 | 1-2 | 10:52:12 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.0800 |  |
| Jogador 1 | 1-2 | 10:52:12 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 1 | 1-2 | 10:52:13 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.3100 |  |
| Jogador 1 | 1-2 | 10:52:14 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.1400 |  |
| Jogador 1 | 1-2 | 10:52:14 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 1 | 1-2 | 10:52:15 | MOVE Bench -> Board: Leona (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.5700 |  |
| Jogador 1 | 1-2 | 10:52:16 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 1 | 1-2 | 10:52:17 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 1 | 1-3 | 10:52:18 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | -0.3300 |  |
| Jogador 1 | 1-3 | 10:52:19 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.1900 |  |
| Jogador 1 | 1-3 | 10:52:19 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | -0.4100 |  |
| Jogador 1 | 1-3 | 10:52:20 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 1 | 1-3 | 10:52:21 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | -0.4100 |  |
| Jogador 1 | 1-3 | 10:52:21 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 1 | 1-3 | 10:52:22 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | -0.5600 |  |
| Jogador 1 | 1-3 | 10:52:23 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 1 | 1-3 | 10:52:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.2300 |  |
| Jogador 1 | 1-4 | 10:52:25 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Rakan | -0.3400 |  |
| Jogador 1 | 1-4 | 10:52:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 1 | 1-4 | 10:52:26 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Rakan | -0.8000 |  |
| Jogador 1 | 1-4 | 10:52:27 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | 0.9300 |  |
| Jogador 1 | 1-4 | 10:52:28 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | -0.4000 |  |
| Jogador 1 | 1-4 | 10:52:28 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | -0.0700 |  |
| Jogador 1 | 1-4 | 10:52:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-1 | 10:52:33 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 10:52:33 | MOVE Bench -> Board: Diana (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | -0.2900 |  |
| Jogador 1 | 2-1 | 10:52:34 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Diana | -0.3300 |  |
| Jogador 1 | 2-1 | 10:52:35 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Diana | 0.2500 |  |
| Jogador 1 | 2-1 | 10:52:36 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Diana | -0.7200 |  |
| Jogador 1 | 2-1 | 10:52:36 | MOVE Bench -> Board: Diana (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Diana | 0.0800 |  |
| Jogador 1 | 2-1 | 10:52:37 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-1 | 10:52:38 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Diana | 0.1600 |  |
| Jogador 1 | 2-1 | 10:52:38 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Diana | -0.0800 |  |
| Jogador 1 | 2-2 | 10:52:40 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Diana | 1.0200 |  |
| Jogador 1 | 2-2 | 10:52:41 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-2 | 10:52:42 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Diana | -0.3200 |  |
| Jogador 1 | 2-2 | 10:52:43 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Diana | 0.1500 |  |
| Jogador 1 | 2-2 | 10:52:43 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Diana | -0.3100 |  |
| Jogador 1 | 2-2 | 10:52:44 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Diana | 0.0800 |  |
| Jogador 1 | 2-2 | 10:52:45 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Diana | -0.3000 |  |
| Jogador 1 | 2-2 | 10:52:45 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Diana | 0.1300 |  |
| Jogador 1 | 2-2 | 10:52:46 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NeedlesslyLargeRod -> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Diana | 0.0700 |  |
| Jogador 1 | 2-3 | 10:52:48 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 19 | 1 | — | DA_18_Diana | 0.1700 |  |
| Jogador 1 | 2-3 | 10:52:49 | VENDEU: Kog'Maw (i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 22 | 1 | — | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-3 | 10:52:50 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 20 | 1 | — | DA_18_Diana | 0.0900 |  |
| Jogador 1 | 2-3 | 10:52:50 | VENDEU: Caitlyn (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 22 | 1 | — | DA_18_Diana | -0.3300 |  |
| Jogador 1 | 2-3 | 10:52:51 | COMPROU: Kayle (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 20 | 1 | — | DA_18_Diana | 0.0800 |  |
| Jogador 1 | 2-3 | 10:52:52 | VENDEU: Kayle (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 22 | 1 | — | DA_18_Diana | -0.3300 |  |
| Jogador 1 | 2-3 | 10:52:52 | MOVE Board -> Board: Diana (i:6.0) <-> Sejuani (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 22 | 1 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 10:52:53 | BUY XP | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 18 | 1 | — | DA_18_Diana | -0.0500 |  |
| Jogador 1 | 2-3 | 10:52:54 | COMPROU: Veigar (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 17 | 1 | — | DA_18_Diana | 0.0900 |  |
| Jogador 1 | 2-4 | 10:52:56 | VENDEU: Veigar (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 25 | 1 | Vanguarda | DA_18_Diana | -0.3200 |  |
| Jogador 1 | 2-4 | 10:52:57 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Vanguarda | DA_18_Diana | 0.1200 |  |
| Jogador 1 | 2-4 | 10:52:57 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Vanguarda | DA_18_Diana | 0.4000 |  |
| Jogador 1 | 2-4 | 10:52:58 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Vanguarda | DA_18_Diana | 0.3300 |  |
| Jogador 1 | 2-4 | 10:52:59 | MOVE Board -> Board: Vi (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Vanguarda | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 10:52:59 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-4 | 10:53:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Vanguarda | DA_18_Diana | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 2-5 | 10:53:04 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Vanguarda | DA_18_Diana | -0.0200 |  |
| Jogador 1 | 2-5 | 10:53:04 | COMPROU: Elise (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 2 | Vanguarda | DA_18_Diana | 0.9600 |  |
| Jogador 1 | 2-5 | 10:53:05 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Vanguarda | DA_18_Diana | -0.3400 |  |
| Jogador 1 | 2-5 | 10:53:06 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Vanguarda | DA_18_Diana | 0.2500 |  |
| Jogador 1 | 2-5 | 10:53:06 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Vanguarda | DA_18_Diana | -0.0600 |  |
| Jogador 1 | 2-5 | 10:53:07 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Vanguarda | DA_18_Diana | 0.2900 |  |
| Jogador 1 | 2-5 | 10:53:08 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Vanguarda | DA_18_Diana | -0.0800 |  |
| Jogador 1 | 2-5 | 10:53:09 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Vanguarda | DA_18_Diana | -0.1000 |  |
| Jogador 1 | 2-5 | 10:53:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Vanguarda | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-6 | 10:53:11 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Vanguarda | DA_18_Diana | -0.2900 |  |
| Jogador 1 | 2-6 | 10:53:12 | COMPROU: Rakan (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 34 | 2 | Vanguarda | DA_18_Diana | 1.0700 |  |
| Jogador 1 | 2-6 | 10:53:13 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Vanguarda | DA_18_Diana | -0.9200 |  |
| Jogador 1 | 2-6 | 10:53:14 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Vanguarda | DA_18_Diana | 0.1000 |  |
| Jogador 1 | 2-6 | 10:53:14 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Vanguarda | DA_18_Diana | -0.3200 |  |
| Jogador 1 | 2-6 | 10:53:15 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Vanguarda | DA_18_Diana | 0.0400 |  |
| Jogador 1 | 2-6 | 10:53:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Vanguarda | DA_18_Diana | -0.1200 |  |
| Jogador 1 | 2-6 | 10:53:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Vanguarda | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-6 | 10:53:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Vanguarda | DA_18_Diana | 0.0400 |  |
| Jogador 1 | 2-7 | 10:53:19 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vanguarda | DA_18_Diana | -0.3200 |  |
| Jogador 1 | 2-7 | 10:53:20 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Vanguarda | DA_18_Diana | -0.1600 |  |
| Jogador 1 | 2-7 | 10:53:21 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Vanguarda | DA_18_Diana | 0.4000 |  |
| Jogador 1 | 2-7 | 10:53:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-7 | 10:53:22 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_18_Diana | 0.1000 |  |
| Jogador 1 | 2-7 | 10:53:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Vanguarda | DA_18_Diana | 0.0100 |  |
| Jogador 1 | 2-7 | 10:53:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 2 | Vanguarda | DA_18_Diana | -0.0900 |  |
| Jogador 1 | 2-7 | 10:53:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-7 | 10:53:25 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 2 | Vanguarda | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 3-1 | 10:53:27 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Vanguarda | DA_18_Diana | -0.3300 |  |
| Jogador 1 | 3-1 | 10:53:28 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Vanguarda | DA_18_Diana | 0.7700 |  |
| Jogador 1 | 3-1 | 10:53:28 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Vanguarda | DA_18_Diana | -0.3800 |  |
| Jogador 1 | 3-1 | 10:53:29 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Vanguarda | DA_18_Ezreal | -0.3100 |  |
| Jogador 1 | 3-1 | 10:53:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-1 | 10:53:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-1 | 10:53:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 1 | Vanguarda | DA_18_Ezreal | -0.0900 |  |
| Jogador 1 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 1 | Vanguarda | DA_18_Ezreal | 0.0800 |  |
| Jogador 1 | 3-1 | 10:53:32 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 1 | Vanguarda | DA_18_Ezreal | 0.4000 |  |
| Jogador 1 | 3-2 | 10:53:35 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Ezreal | 0.7300 |  |
| Jogador 1 | 3-2 | 10:53:35 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vanguarda | DA_18_Ezreal | -0.3900 |  |
| Jogador 1 | 3-2 | 10:53:36 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Ezreal | 0.2100 |  |
| Jogador 1 | 3-2 | 10:53:37 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Ezreal | 0.1200 |  |
| Jogador 1 | 3-2 | 10:53:37 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-2 | 10:53:38 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-2 | 10:53:39 | MOVE Board -> Board: Sejuani (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-2 | 10:53:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-3 | 10:53:43 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vanguarda | DA_18_Ezreal | -0.0300 |  |
| Jogador 1 | 3-3 | 10:53:44 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Vanguarda | DA_18_Ezreal | -0.4100 |  |
| Jogador 1 | 3-3 | 10:53:44 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vanguarda | DA_18_Ezreal | 0.1800 |  |
| Jogador 1 | 3-3 | 10:53:45 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Vanguarda | DA_18_Ezreal | -0.1000 |  |
| Jogador 1 | 3-3 | 10:53:46 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Vanguarda | DA_18_Ezreal | 0.2000 |  |
| Jogador 1 | 3-3 | 10:53:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-3 | 10:53:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Ezreal | -0.0900 |  |
| Jogador 1 | 3-3 | 10:53:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-3 | 10:53:49 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Ezreal | -0.1300 |  |
| Jogador 1 | 3-4 | 10:53:51 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Ezreal | 0.7300 |  |
| Jogador 1 | 3-4 | 10:53:52 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vanguarda | DA_18_Ezreal | -0.3900 |  |
| Jogador 1 | 3-4 | 10:53:53 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vanguarda | DA_18_Ezreal | 0.1900 |  |
| Jogador 1 | 3-4 | 10:53:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-4 | 10:53:54 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vanguarda | DA_18_Ezreal | -0.1200 |  |
| Jogador 1 | 3-4 | 10:53:55 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Vanguarda | DA_18_Ezreal | 0.2000 |  |
| Jogador 1 | 3-4 | 10:53:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-4 | 10:53:56 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vanguarda | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-4 | 10:53:57 | MOVE Board -> Board: Vi (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vanguarda | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-5 | 10:54:00 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Ezreal | -0.1200 |  |
| Jogador 1 | 3-5 | 10:54:01 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Vanguarda | DA_18_Ezreal | 0.0900 |  |
| Jogador 1 | 3-5 | 10:54:01 | VENDEU: Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vanguarda | DA_18_Ezreal | -0.1200 |  |
| Jogador 1 | 3-5 | 10:54:02 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Ezreal | 0.4400 |  |
| Jogador 1 | 3-5 | 10:54:03 | MOVE Board -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-5 | 10:54:03 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Ezreal | -0.0200 |  |
| Jogador 1 | 3-5 | 10:54:04 | MOVE Board -> Board: Rakan (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Ezreal | -0.0200 |  |
| Jogador 1 | 3-5 | 10:54:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vanguarda | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-6 | 10:54:08 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Vanguarda | DA_18_Diana | 0.8000 |  |
| Jogador 1 | 3-6 | 10:54:09 | COMPROU: Lux (Feérica) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_18_Lux_Fae | 0.1500 |  |
| Jogador 1 | 3-6 | 10:54:10 | MOVE Board -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_18_Lux_Fae | 0.0000 |  |
| Jogador 1 | 3-6 | 10:54:10 | MOVE Board -> Board: Sejuani (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_18_Lux_Fae | -0.0100 |  |
| Jogador 1 | 3-6 | 10:54:11 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_18_Lux_Fae | 0.0000 |  |
| Jogador 1 | 3-7 | 10:54:17 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Vanguarda | DA_18_Lux_Fae | 0.8000 |  |
| Jogador 1 | 3-7 | 10:54:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | 0.8300 |  |
| Jogador 1 | 3-7 | 10:54:18 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | 0.4100 |  |
| Jogador 1 | 3-7 | 10:54:19 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_RecurveBow -> Lux (Feérica) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | 0.0900 |  |
| Jogador 1 | 3-7 | 10:54:20 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Lux (Feérica) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | 0.1200 |  |
| Jogador 1 | 3-7 | 10:54:20 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 3-7 | 10:54:21 | MOVE Board -> Board: Rakan (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | -0.0200 |  |
| Jogador 1 | 3-7 | 10:54:22 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 3-7 | 10:54:22 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-1 | 10:54:26 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Vanguarda | DA_Vi18 | 0.2700 |  |
| Jogador 1 | 4-1 | 10:54:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vanguarda | DA_Vi18 | -0.2500 |  |
| Jogador 1 | 4-1 | 10:54:27 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Vanguarda | DA_Vi18 | 0.2500 |  |
| Jogador 1 | 4-1 | 10:54:28 | MOVE Board -> Board: Diana (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Vanguarda | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-1 | 10:54:29 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Vanguarda | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-1 | 10:54:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Vanguarda | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-2 | 10:54:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Vanguarda | DA_Vi18 | 0.8200 |  |
| Jogador 1 | 4-2 | 10:54:36 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Vanguarda | DA_Vi18 | -0.2000 |  |
| Jogador 1 | 4-2 | 10:54:36 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Vi18 | 0.0400 |  |
| Jogador 1 | 4-2 | 10:54:37 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Vi18 | 0.0000 |  |
| Jogador 1 | 4-2 | 10:54:38 | MOVE Board -> Board: Master Yi (i:6.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-2 | 10:54:39 | MOVE Board -> Board: Diana (i:6.0) <-> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-2 | 10:54:39 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vanguarda | DA_Vi18 | -0.0500 |  |
| Jogador 2 | ? | 10:51:57 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0200 |  |
| Jogador 2 | ? | 10:51:58 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.3100 |  |
| Jogador 2 | ? | 10:51:58 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.6000 |  |
| Jogador 2 | ? | 10:51:59 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 2 | ? | 10:52:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-1 | 10:52:04 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 2 | 1-1 | 10:52:05 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 2 | 1-1 | 10:52:05 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2600 |  |
| Jogador 2 | 1-1 | 10:52:06 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4200 |  |
| Jogador 2 | 1-1 | 10:52:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 2 | 1-1 | 10:52:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 2 | 1-1 | 10:52:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-2 | 10:52:11 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2400 |  |
| Jogador 2 | 1-2 | 10:52:12 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | -0.4000 |  |
| Jogador 2 | 1-2 | 10:52:12 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | -0.1500 |  |
| Jogador 2 | 1-2 | 10:52:13 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0800 |  |
| Jogador 2 | 1-2 | 10:52:14 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | -0.3900 |  |
| Jogador 2 | 1-2 | 10:52:14 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 1-2 | 10:52:15 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 1-2 | 10:52:16 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | -0.3800 |  |
| Jogador 2 | 1-2 | 10:52:17 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 1-3 | 10:52:18 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Sejuani | -0.0800 |  |
| Jogador 2 | 1-3 | 10:52:19 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.1200 |  |
| Jogador 2 | 1-3 | 10:52:19 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | -0.2100 |  |
| Jogador 2 | 1-3 | 10:52:20 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Sejuani | 0.1600 |  |
| Jogador 2 | 1-3 | 10:52:21 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | -0.3800 |  |
| Jogador 2 | 1-3 | 10:52:21 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Sejuani | 0.2000 |  |
| Jogador 2 | 1-3 | 10:52:22 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | -0.3900 |  |
| Jogador 2 | 1-3 | 10:52:23 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Sejuani | 0.2000 |  |
| Jogador 2 | 1-3 | 10:52:24 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Sejuani | 0.2200 |  |
| Jogador 2 | 1-4 | 10:52:25 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Sejuani | 1.0400 |  |
| Jogador 2 | 1-4 | 10:52:26 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Sejuani | -0.7700 |  |
| Jogador 2 | 1-4 | 10:52:26 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Vi18 | 0.3300 |  |
| Jogador 2 | 1-4 | 10:52:27 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Vi18 | 0.2600 |  |
| Jogador 2 | 1-4 | 10:52:28 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Vi18 | 0.2200 |  |
| Jogador 2 | 1-4 | 10:52:28 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Vi18 | -0.4100 |  |
| Jogador 2 | 1-4 | 10:52:29 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | 0.3500 |  |
| Jogador 2 | 1-4 | 10:52:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | 0.4200 |  |
| Jogador 2 | 1-4 | 10:52:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | -0.0100 |  |
| Jogador 2 | 2-1 | 10:52:33 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Vi18 | 1.0100 |  |
| Jogador 2 | 2-1 | 10:52:33 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Vi18 | -0.7500 |  |
| Jogador 2 | 2-1 | 10:52:34 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Vi18 | 0.0700 |  |
| Jogador 2 | 2-1 | 10:52:35 | MOVE Bench -> Board: Shen (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Vi18 | -0.4000 |  |
| Jogador 2 | 2-1 | 10:52:36 | MOVE Bench -> Board: Vi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Vi18 | -0.3100 |  |
| Jogador 2 | 2-1 | 10:52:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-2 | 10:52:40 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | — | DA_Vi18 | -0.1100 |  |
| Jogador 2 | 2-2 | 10:52:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_Vi18 | 0.1300 |  |
| Jogador 2 | 2-2 | 10:52:42 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_Vi18 | -0.3800 |  |
| Jogador 2 | 2-2 | 10:52:43 | MOVE Bench -> Board: Shen (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_MasterYi_AD | -0.6400 |  |
| Jogador 2 | 2-2 | 10:52:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_MasterYi_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 2-3 | 10:52:48 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | — | DA_18_MasterYi_AD | -0.3100 |  |
| Jogador 2 | 2-3 | 10:52:49 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | — | DA_18_MasterYi_AD | 0.2400 |  |
| Jogador 2 | 2-3 | 10:52:50 | MOVE Bench -> Board: Elise (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | — | DA_18_MasterYi_AD | -0.3000 |  |
| Jogador 2 | 2-3 | 10:52:50 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | — | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 2 | 2-3 | 10:52:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | — | DA_18_MasterYi_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 2-4 | 10:52:56 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Vanguarda | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 2 | 2-4 | 10:52:57 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vanguarda | DA_18_Tristana | 0.3700 |  |
| Jogador 2 | 2-4 | 10:52:57 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Vanguarda | DA_18_MasterYi_AD | -0.1900 |  |
| Jogador 2 | 2-4 | 10:52:58 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vanguarda | DA_18_Azir | 0.3700 |  |
| Jogador 2 | 2-4 | 10:52:59 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Vanguarda | DA_18_MasterYi_AD | -0.1700 |  |
| Jogador 2 | 2-4 | 10:52:59 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vanguarda | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 2 | 2-4 | 10:53:00 | MOVE Bench -> Board: Rengar (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vanguarda | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 2 | 2-4 | 10:53:01 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vanguarda | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 2 | 2-4 | 10:53:02 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vanguarda | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 2 | 2-5 | 10:53:04 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Vanguarda | DA_18_MasterYi_AD | 0.5900 |  |
| Jogador 2 | 2-5 | 10:53:04 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Vanguarda | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 2 | 2-5 | 10:53:05 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Vanguarda | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 2 | 2-5 | 10:53:06 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Vanguarda | DA_18_MasterYi_AD | 0.0500 |  |
| Jogador 2 | 2-5 | 10:53:06 | MOVE Board -> Board: Elise (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Vanguarda | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 2-5 | 10:53:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Vanguarda | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 2 | 2-5 | 10:53:08 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Vanguarda | DA_18_MasterYi_AD | -0.6100 |  |
| Jogador 2 | 2-5 | 10:53:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Vanguarda | DA_18_MasterYi_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 2-6 | 10:53:11 | MOVE Bench -> Board: Rengar (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Vanguarda | DA_18_MasterYi_AD | -0.3400 |  |
| Jogador 2 | 2-6 | 10:53:12 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Vanguarda | DA_18_Rengar | 0.0300 |  |
| Jogador 2 | 2-6 | 10:53:13 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rengar (i:6.0) (tabuleiro slot 2) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Vanguarda | DA_18_Rengar | 0.0700 |  |
| Jogador 2 | 2-6 | 10:53:14 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Rengar (i:6.0) (tabuleiro slot 2) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Vanguarda | DA_18_Rengar | 0.0800 |  |
| Jogador 2 | 2-6 | 10:53:14 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Vanguarda | DA_18_Rengar | -0.0900 |  |
| Jogador 2 | 2-6 | 10:53:15 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Vanguarda | DA_18_Rengar | -0.2800 |  |
| Jogador 2 | 2-6 | 10:53:16 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Vanguarda | DA_18_Rengar | -0.0100 |  |
| Jogador 2 | 2-6 | 10:53:16 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Vanguarda | DA_18_Rengar | 0.1500 |  |
| Jogador 2 | 2-6 | 10:53:17 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Vanguarda | DA_18_Rengar | -0.3200 |  |
| Jogador 2 | 2-7 | 10:53:19 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Vanguarda | DA_18_MasterYi_AD | -0.2400 |  |
| Jogador 2 | 2-7 | 10:53:20 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Vanguarda | DA_18_MasterYi_AD | -0.2900 |  |
| Jogador 2 | 2-7 | 10:53:21 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Vanguarda | DA_18_MasterYi_AD | -0.4100 |  |
| Jogador 2 | 2-7 | 10:53:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Vanguarda | DA_18_MasterYi_AD | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-1 | 10:53:27 | MOVE Bench -> Board: Rengar (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Vanguarda | DA_18_MasterYi_AD | -0.3000 |  |
| Jogador 2 | 3-1 | 10:53:28 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Vanguarda | DA_18_MasterYi_AD | -0.4100 |  |
| Jogador 2 | 3-1 | 10:53:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Vanguarda | DA_18_MasterYi_AD | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-2 | 10:53:35 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 77 | 5 | Vanguarda | DA_18_MasterYi_AD | -0.4400 |  |
| Jogador 2 | 3-2 | 10:53:35 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Vanguarda | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 2 | 3-2 | 10:53:36 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 77 | 5 | Vanguarda | DA_18_MasterYi_AD | -0.4200 |  |
| Jogador 2 | 3-2 | 10:53:37 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Vanguarda | DA_CrimsonRaptor18 | -0.1400 |  |
| Jogador 2 | 3-2 | 10:53:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Vanguarda | DA_CrimsonRaptor18 | 0.0800 |  |
| Jogador 2 | 3-2 | 10:53:38 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Vanguarda | DA_CrimsonRaptor18 | -0.1200 |  |
| Jogador 2 | 3-2 | 10:53:39 | MOVE Bench -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Vanguarda | DA_CrimsonRaptor18 | -0.6000 |  |
| Jogador 2 | 3-2 | 10:53:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Vanguarda | DA_CrimsonRaptor18 | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-3 | 10:53:43 | COMPROU: Elise (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 83 | 5 | Vanguarda | DA_CrimsonRaptor18 | 0.9800 |  |
| Jogador 2 | 3-3 | 10:53:44 | MOVE Bench -> Board: Elise (i:4.0) <-> Mamãe Bicuda (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 83 | 5 | Vanguarda | DA_CrimsonRaptor18 | 0.3000 |  |
| Jogador 2 | 3-3 | 10:53:44 | COMPROU: Elise (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 81 | 5 | Vanguarda | DA_18_Elise | 0.9600 |  |
| Jogador 2 | 3-3 | 10:53:45 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 81 | 5 | Vanguarda | DA_18_Elise | -0.0700 |  |
| Jogador 2 | 3-3 | 10:53:46 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Mamãe Bicuda (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 81 | 5 | Vanguarda | DA_18_Elise | -0.1400 |  |
| Jogador 2 | 3-3 | 10:53:47 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 81 | 5 | Vanguarda | DA_18_Elise | -0.1400 |  |
| Jogador 2 | 3-3 | 10:53:49 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 81 | 5 | Vanguarda | DA_18_Elise | 0.5100 |  |
| Jogador 2 | 3-4 | 10:53:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 91 | 5 | Vanguarda | DA_18_Elise | 0.9000 |  |
| Jogador 2 | 3-4 | 10:53:52 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 91 | 5 | Vanguarda | DA_18_Elise | 0.0000 |  |
| Jogador 2 | 3-4 | 10:53:53 | VENDEU: Elise (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 96 | 5 | Vanguarda | DA_CrimsonRaptor18 | -0.4700 |  |
| Jogador 2 | 3-4 | 10:53:54 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 97 | 5 | Rival | DA_CrimsonRaptor18 | -0.7500 |  |
| Jogador 2 | 3-4 | 10:53:54 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 95 | 5 | Rival | DA_CrimsonRaptor18 | 0.2300 |  |
| Jogador 2 | 3-4 | 10:53:55 | MOVE Bench -> Board: Shen (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 95 | 5 | Rival | DA_CrimsonRaptor18 | -0.3400 |  |
| Jogador 2 | 3-4 | 10:53:56 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 95 | 5 | Rival | DA_CrimsonRaptor18 | -0.4100 |  |
| Jogador 2 | 3-4 | 10:53:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 95 | 5 | Rival | DA_CrimsonRaptor18 | -0.1800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-5 | 10:54:00 | MOVE Bench -> Board: Rengar (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 106 | 5 | Rival | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 2 | 3-5 | 10:54:01 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 103 | 5 | Rival | DA_CrimsonRaptor18 | 1.0000 |  |
| Jogador 2 | 3-5 | 10:54:01 | MOVE Bench -> Board: Shen (i:4.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 103 | 5 | Rival | DA_CrimsonRaptor18 | -0.2700 |  |
| Jogador 2 | 3-5 | 10:54:02 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 103 | 5 | Rival | DA_CrimsonRaptor18 | -0.4100 |  |
| Jogador 2 | 3-5 | 10:54:03 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 103 | 5 | Rival | DA_CrimsonRaptor18 | -0.1500 |  |
| Jogador 2 | 3-6 | 10:54:08 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 112 | 5 | Rival | DA_CrimsonRaptor18 | 0.9500 |  |
| Jogador 2 | 3-6 | 10:54:09 | MOVE Bench -> Board: Rengar (i:6.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 112 | 5 | Rival | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 2 | 3-6 | 10:54:10 | COMPROU: Veigar (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 111 | 5 | Rival | DA_CrimsonRaptor18 | 0.9300 |  |
| Jogador 2 | 3-6 | 10:54:10 | MOVE Bench -> Board: Shen (i:4.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 111 | 5 | Rival | DA_CrimsonRaptor18 | -0.3000 |  |
| Jogador 2 | 3-6 | 10:54:11 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 111 | 5 | Rival | DA_CrimsonRaptor18 | -0.4100 |  |
| Jogador 2 | 3-6 | 10:54:12 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 111 | 5 | Rival | DA_CrimsonRaptor18 | -0.1600 |  |
| Jogador 2 | 3-7 | 10:54:17 | COMPROU: Hecarim (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 120 | 5 | Rival | DA_CrimsonRaptor18 | -0.2700 |  |
| Jogador 2 | 3-7 | 10:54:18 | MOVE Bench -> Board: Rengar (i:6.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 120 | 5 | Rival | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 2 | 3-7 | 10:54:18 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_ChainVest -> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 120 | 5 | Rival | DA_CrimsonRaptor18 | 0.1200 |  |
| Jogador 2 | 3-7 | 10:54:19 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 120 | 5 | Rival | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 2 | 3-7 | 10:54:20 | COMPROU: Teemo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 118 | 5 | Rival | DA_CrimsonRaptor18 | -0.0600 |  |
| Jogador 2 | 3-7 | 10:54:20 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 116 | 5 | Rival | DA_CrimsonRaptor18 | -0.1200 |  |
| Jogador 2 | 3-7 | 10:54:21 | COMPROU: Kobuko (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 115 | 5 | Rival | DA_CrimsonRaptor18 | -0.0700 |  |
| Jogador 2 | 3-7 | 10:54:22 | COMPROU: Leona (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 114 | 5 | Rival | DA_CrimsonRaptor18 | -0.2700 |  |
| Jogador 2 | 3-7 | 10:54:22 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 114 | 5 | Rival | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 2 | 4-1 | 10:54:26 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 125 | 5 | Rival | DA_CrimsonRaptor18 | 0.4000 |  |
| Jogador 2 | 4-1 | 10:54:27 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Rival | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 2 | 4-1 | 10:54:27 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 2 | 4-1 | 10:54:28 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Rival | DA_CrimsonRaptor18 | 0.0800 |  |
| Jogador 2 | 4-1 | 10:54:29 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 119 | 5 | Rival | DA_CrimsonRaptor18 | 0.6500 |  |
| Jogador 2 | 4-1 | 10:54:29 | VENDEU: Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Rival | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 2 | 4-1 | 10:54:30 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 118 | 5 | Rival | DA_CrimsonRaptor18 | 0.1500 |  |
| Jogador 2 | 4-1 | 10:54:31 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 116 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 2 | 4-1 | 10:54:32 | VENDEU: Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 118 | 5 | Rival | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 2 | 4-2 | 10:54:35 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Rival | DA_CrimsonRaptor18 | 0.3500 |  |
| Jogador 2 | 4-2 | 10:54:36 | REROLL | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 2 | 4-2 | 10:54:36 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Rival | DA_CrimsonRaptor18 | -0.1400 |  |
| Jogador 2 | 4-2 | 10:54:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 124 | 5 | Rival | DA_18_Veigar | 0.9600 |  |
| Jogador 2 | 4-2 | 10:54:38 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 122 | 5 | Rival | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 4-2 | 10:54:39 | MOVE Bench -> Board: Krugue (i:6.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 122 | 5 | Rival | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 4-2 | 10:54:39 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 122 | 5 | Rival | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 4-2 | 10:54:40 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 121 | 5 | Rival | DA_18_Veigar | -0.1900 |  |
| Jogador 2 | 4-2 | 10:54:41 | REROLL | STABILIZE | STABILIZE: pressão de vida | 119 | 5 | Rival | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 4-3 | 10:54:44 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Rival | DA_CrimsonRaptor18 | -0.1200 |  |
| Jogador 2 | 4-3 | 10:54:45 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Rival | DA_CrimsonRaptor18 | 0.6600 |  |
| Jogador 2 | 4-3 | 10:54:46 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Rival | DA_CrimsonRaptor18 | 0.0800 |  |
| Jogador 2 | 4-3 | 10:54:46 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Rival | DA_CrimsonRaptor18 | 0.6500 |  |
| Jogador 2 | 4-3 | 10:54:47 | REROLL | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 2 | 4-3 | 10:54:48 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Rival | DA_CrimsonRaptor18 | -0.1300 |  |
| Jogador 2 | 4-3 | 10:54:48 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Rival | DA_Gromp18_AP | 0.9300 |  |
| Jogador 2 | 4-3 | 10:54:49 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Rival | DA_Gromp18_AP | -0.2300 |  |
| Jogador 2 | 4-3 | 10:54:50 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Rival | DA_Gromp18_AP | -0.1600 |  |
| Jogador 2 | 4-4 | 10:54:53 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 2 | 4-4 | 10:54:54 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Rival | DA_CrimsonRaptor18 | 0.8800 |  |
| Jogador 2 | 4-4 | 10:54:55 | REROLL | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 2 | 4-4 | 10:54:56 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 136 | 5 | Rival | DA_CrimsonRaptor18 | 0.0800 |  |
| Jogador 2 | 4-4 | 10:54:56 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 134 | 5 | Rival | DA_CrimsonRaptor18 | 0.7600 |  |
| Jogador 2 | 4-4 | 10:54:57 | REROLL | STABILIZE | STABILIZE: pressão de vida | 132 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 2 | 4-4 | 10:54:58 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Rival | DA_CrimsonRaptor18 | 0.0800 |  |
| Jogador 2 | 4-4 | 10:54:58 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Rival | DA_CrimsonRaptor18 | 0.2500 |  |
| Jogador 2 | 4-4 | 10:54:59 | REROLL | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 2 | 4-5 | 10:55:03 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Rival | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 2 | 4-5 | 10:55:03 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Rival | DA_18_Shen | 0.9900 |  |
| Jogador 2 | 4-5 | 10:55:04 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Rival | DA_18_Shen | 0.1800 |  |
| Jogador 2 | 4-5 | 10:55:05 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Rival | DA_18_Shen | 0.5700 |  |
| Jogador 2 | 4-5 | 10:55:05 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Rival | DA_18_Shen | -0.0900 |  |
| Jogador 2 | 4-5 | 10:55:06 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Rival | DA_18_Shen | -0.0900 |  |
| Jogador 2 | 4-5 | 10:55:07 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Rival | DA_18_Shen | -0.0900 |  |
| Jogador 2 | 4-5 | 10:55:07 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Rival | DA_18_Shen | -0.0900 |  |
| Jogador 2 | 4-5 | 10:55:08 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Rival | DA_18_Shen | -0.0900 |  |
| Jogador 2 | 4-6 | 10:55:12 | VENDEU: Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Rival | DA_CrimsonRaptor18 | -0.1200 |  |
| Jogador 2 | 4-6 | 10:55:13 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Rival | DA_CrimsonRaptor18 | 1.0000 |  |
| Jogador 2 | 4-6 | 10:55:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Rival | DA_CrimsonRaptor18 | -0.1400 |  |
| Jogador 2 | 4-6 | 10:55:14 | MOVE Bench -> Board: Karma (i:2.0) <-> Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Rival | DA_CrimsonRaptor18 | -0.2000 |  |
| Jogador 2 | 4-6 | 10:55:15 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Rival | DA_CrimsonRaptor18 | -0.2500 |  |
| Jogador 2 | 4-6 | 10:55:16 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Rival | DA_CrimsonRaptor18 | -0.2400 |  |
| Jogador 2 | 4-6 | 10:55:18 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Rival | DA_CrimsonRaptor18 | 0.5300 |  |
| Jogador 2 | 4-7 | 10:55:22 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Rival | DA_CrimsonRaptor18 | 0.4200 |  |
| Jogador 2 | 4-7 | 10:55:22 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_ChainVest -> Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Rival | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 2 | 4-7 | 10:55:23 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_ChainVest -> Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Rival | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 2 | 4-7 | 10:55:24 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Rival | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 2 | 4-7 | 10:55:24 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Rival | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 2 | 4-7 | 10:55:25 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Rival | DA_CrimsonRaptor18 | 1.0100 |  |
| Jogador 2 | 4-7 | 10:55:26 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Rival | DA_CrimsonRaptor18 | 0.9900 |  |
| Jogador 2 | 4-7 | 10:55:26 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Rival | DA_CrimsonRaptor18 | 0.1700 |  |
| Jogador 2 | 4-7 | 10:55:27 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Rival | DA_CrimsonRaptor18 | 0.1700 |  |
| Jogador 3 | ? | 10:51:57 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 3 | ? | 10:51:58 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.3000 |  |
| Jogador 3 | ? | 10:51:58 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.6000 |  |
| Jogador 3 | ? | 10:51:59 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | -0.0100 |  |
| Jogador 3 | ? | 10:52:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_RekSai | 0.0000 |  |
| Jogador 3 | 1-1 | 10:52:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_RekSai | 1.0400 |  |
| Jogador 3 | 1-1 | 10:52:05 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_RekSai | -0.3900 |  |
| Jogador 3 | 1-1 | 10:52:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1500 |  |
| Jogador 3 | 1-1 | 10:52:06 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1800 |  |
| Jogador 3 | 1-1 | 10:52:07 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0600 |  |
| Jogador 3 | 1-1 | 10:52:07 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 3 | 1-1 | 10:52:08 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 3 | 1-1 | 10:52:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 1-2 | 10:52:11 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.1000 |  |
| Jogador 3 | 1-2 | 10:52:12 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | -0.3600 |  |
| Jogador 3 | 1-2 | 10:52:12 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | 0.0100 |  |
| Jogador 3 | 1-2 | 10:52:13 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.3200 |  |
| Jogador 3 | 1-2 | 10:52:14 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | -0.2900 |  |
| Jogador 3 | 1-2 | 10:52:14 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.3200 |  |
| Jogador 3 | 1-2 | 10:52:15 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | -0.2900 |  |
| Jogador 3 | 1-2 | 10:52:16 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Murkwolf18 | 0.3200 |  |
| Jogador 3 | 1-2 | 10:52:17 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | -0.2900 |  |
| Jogador 3 | 1-3 | 10:52:18 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Murkwolf18 | 0.2800 |  |
| Jogador 3 | 1-3 | 10:52:19 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 1-3 | 10:52:19 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 1-3 | 10:52:20 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 3 | 1-3 | 10:52:21 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 1-3 | 10:52:21 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 3 | 1-3 | 10:52:22 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 1-3 | 10:52:23 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.1800 |  |
| Jogador 3 | 1-3 | 10:52:24 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 1-4 | 10:52:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | 1.0200 |  |
| Jogador 3 | 1-4 | 10:52:26 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 1-4 | 10:52:26 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 1-4 | 10:52:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-1 | 10:52:33 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Scuttlecrab18 | 1.0400 |  |
| Jogador 3 | 2-1 | 10:52:33 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Scuttlecrab18 | 0.2900 |  |
| Jogador 3 | 2-1 | 10:52:34 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | 0.2400 |  |
| Jogador 3 | 2-1 | 10:52:35 | MOVE Bench -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | -0.3900 |  |
| Jogador 3 | 2-1 | 10:52:36 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | 0.5500 |  |
| Jogador 3 | 2-1 | 10:52:36 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_BFSword -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | 0.2000 |  |
| Jogador 3 | 2-1 | 10:52:37 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | 0.1200 |  |
| Jogador 3 | 2-1 | 10:52:38 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.1800 |  |
| Jogador 3 | 2-1 | 10:52:38 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | -0.4100 |  |
| Jogador 3 | 2-2 | 10:52:40 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 2-2 | 10:52:41 | MOVE Bench -> Board: Rammus (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Scuttlecrab18 | -0.7400 |  |
| Jogador 3 | 2-2 | 10:52:42 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-2 | 10:52:43 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Rammus (i:6.0) (tabuleiro slot 0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Scuttlecrab18 | 0.1200 |  |
| Jogador 3 | 2-2 | 10:52:43 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Rammus (i:6.0) (tabuleiro slot 0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 2-2 | 10:52:44 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Scuttlecrab18 | 0.2700 |  |
| Jogador 3 | 2-2 | 10:52:45 | MOVE Board -> Board: Rammus (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-2 | 10:52:45 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Scuttlecrab18 | -0.0500 |  |
| Jogador 3 | 2-2 | 10:52:46 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Scuttlecrab18 | -0.0500 |  |
| Jogador 3 | 2-3 | 10:52:48 | COMPROU: Rengar (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 15 | 1 | — | DA_Scuttlecrab18 | 0.1500 |  |
| Jogador 3 | 2-3 | 10:52:49 | MOVE Bench -> Board: Rengar (i:6.0) <-> Sejuani (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 15 | 1 | — | DA_Scuttlecrab18 | 0.0300 |  |
| Jogador 3 | 2-3 | 10:52:50 | VENDEU: Sejuani (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 17 | 1 | — | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-3 | 10:52:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 16 | 1 | — | DA_Scuttlecrab18 | 0.9400 |  |
| Jogador 3 | 2-3 | 10:52:51 | VENDEU: Rek'Sai (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 17 | 1 | — | DA_Scuttlecrab18 | -0.4600 |  |
| Jogador 3 | 2-3 | 10:52:52 | COMPROU: Hecarim (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 14 | 1 | — | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 2-3 | 10:52:52 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rengar (i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 14 | 1 | — | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 2-3 | 10:52:53 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rek'Sai (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 14 | 1 | — | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-3 | 10:52:54 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 14 | 1 | — | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-4 | 10:52:56 | VENDEU: Rengar (i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 24 | 1 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-4 | 10:52:57 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Scuttlecrab18 | 0.3400 |  |
| Jogador 3 | 2-4 | 10:52:57 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_Scuttlecrab18 | -0.5300 |  |
| Jogador 3 | 2-4 | 10:52:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_Scuttlecrab18 | 0.3500 |  |
| Jogador 3 | 2-4 | 10:52:59 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_Scuttlecrab18 | -0.1500 |  |
| Jogador 3 | 2-4 | 10:52:59 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_Scuttlecrab18 | 0.4000 |  |
| Jogador 3 | 2-4 | 10:53:00 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Colosso | DA_Scuttlecrab18 | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-4 | 10:53:01 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Colosso | DA_Scuttlecrab18 | 0.5700 |  |
| Jogador 3 | 2-4 | 10:53:02 | COMPROU: Cascalho (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | Colosso | DA_Scuttlecrab18 | 0.0900 |  |
| Jogador 3 | 2-5 | 10:53:04 | VENDEU: Cascalho (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Scuttlecrab18 | -0.3200 |  |
| Jogador 3 | 2-5 | 10:53:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 24 | 1 | Colosso | DA_Scuttlecrab18 | 0.3400 |  |
| Jogador 3 | 2-5 | 10:53:05 | VENDEU: Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Scuttlecrab18 | -0.5000 |  |
| Jogador 3 | 2-5 | 10:53:06 | COMPROU: Yorick (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 25 | 1 | Colosso | DA_Scuttlecrab18 | 0.9700 |  |
| Jogador 3 | 2-5 | 10:53:06 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Scuttlecrab18 | -0.8500 |  |
| Jogador 3 | 2-5 | 10:53:07 | COMPROU: Yunara (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 24 | 1 | Colosso | DA_Scuttlecrab18 | 0.0300 |  |
| Jogador 3 | 2-5 | 10:53:08 | VENDEU: Yunara (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Scuttlecrab18 | -0.3200 |  |
| Jogador 3 | 2-5 | 10:53:09 | COMPROU: Karma (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 25 | 1 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 2-5 | 10:53:09 | VENDEU: Karma (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 1 | Colosso | DA_Scuttlecrab18 | -0.3200 |  |
| Jogador 3 | 2-6 | 10:53:11 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 2 | Colosso | DA_Scuttlecrab18 | 0.3400 |  |
| Jogador 3 | 2-6 | 10:53:12 | VENDEU: Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 33 | 2 | Colosso | DA_Scuttlecrab18 | -0.5000 |  |
| Jogador 3 | 2-6 | 10:53:13 | COMPROU: Yorick (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 32 | 2 | Colosso | DA_Scuttlecrab18 | 0.9700 |  |
| Jogador 3 | 2-6 | 10:53:14 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 33 | 2 | Colosso | DA_Scuttlecrab18 | -0.8500 |  |
| Jogador 3 | 2-6 | 10:53:14 | COMPROU: Diana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Colosso | DA_Scuttlecrab18 | 0.2100 |  |
| Jogador 3 | 2-6 | 10:53:15 | MOVE Bench -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Colosso | DA_Scuttlecrab18 | -0.3900 |  |
| Jogador 3 | 2-6 | 10:53:16 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.1900 |  |
| Jogador 3 | 2-6 | 10:53:16 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.1900 |  |
| Jogador 3 | 2-6 | 10:53:17 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-7 | 10:53:19 | VENDEU: LeBlanc (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 2-7 | 10:53:20 | COMPROU: Vi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 35 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.1200 |  |
| Jogador 3 | 2-7 | 10:53:21 | VENDEU: Vi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.3200 |  |
| Jogador 3 | 2-7 | 10:53:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.5800 |  |
| Jogador 3 | 2-7 | 10:53:22 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_SparringGloves -> Diana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.2200 |  |
| Jogador 3 | 2-7 | 10:53:23 | MOVE Board -> Board: Rammus (i:6.0) <-> Rek'Sai (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-7 | 10:53:23 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-7 | 10:53:24 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 33 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0500 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-7 | 10:53:25 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.1300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-1 | 10:53:27 | VENDEU: Rek'Sai (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.4300 |  |
| Jogador 3 | 3-1 | 10:53:28 | COMPROU: Tristana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 35 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0600 |  |
| Jogador 3 | 3-1 | 10:53:28 | VENDEU: Tristana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.3900 |  |
| Jogador 3 | 3-1 | 10:53:29 | COMPROU: Alistar (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 36 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0300 |  |
| Jogador 3 | 3-1 | 10:53:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 3-1 | 10:53:30 | MOVE Bench -> Board: Alistar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.4000 |  |
| Jogador 3 | 3-1 | 10:53:31 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.5600 |  |
| Jogador 3 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 3-2 | 10:53:35 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.1800 |  |
| Jogador 3 | 3-2 | 10:53:35 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.2300 |  |
| Jogador 3 | 3-2 | 10:53:36 | MOVE Board -> Board: Alistar (i:4.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-2 | 10:53:37 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-2 | 10:53:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 3 | 3-3 | 10:53:43 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.6400 |  |
| Jogador 3 | 3-3 | 10:53:44 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 3-3 | 10:53:44 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.1500 |  |
| Jogador 3 | 3-3 | 10:53:45 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-3 | 10:53:46 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-3 | 10:53:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 3 | 3-4 | 10:53:51 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.7600 |  |
| Jogador 3 | 3-4 | 10:53:52 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 3-4 | 10:53:53 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.2900 |  |
| Jogador 3 | 3-4 | 10:53:54 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 3 | 3-4 | 10:53:54 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.1300 |  |
| Jogador 3 | 3-4 | 10:53:55 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.7500 |  |
| Jogador 3 | 3-4 | 10:53:56 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 3-4 | 10:53:56 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.7800 |  |
| Jogador 3 | 3-4 | 10:53:57 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 3-5 | 10:54:00 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 3-5 | 10:54:01 | VENDEU: Elise (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 3 | 3-5 | 10:54:01 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.3100 |  |
| Jogador 3 | 3-5 | 10:54:02 | REROLL | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 3-5 | 10:54:03 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 3-5 | 10:54:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.6300 |  |
| Jogador 3 | 3-5 | 10:54:04 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.1400 |  |
| Jogador 3 | 3-5 | 10:54:05 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.1700 |  |
| Jogador 3 | 3-5 | 10:54:06 | REROLL | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 3-6 | 10:54:08 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 40 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.1600 |  |
| Jogador 3 | 3-6 | 10:54:09 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.8000 |  |
| Jogador 3 | 3-6 | 10:54:10 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 40 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.1300 |  |
| Jogador 3 | 3-6 | 10:54:10 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 3-6 | 10:54:11 | REROLL | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 3-6 | 10:54:12 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 3-6 | 10:54:13 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Vanguarda | DA_Scuttlecrab18 | 0.8300 |  |
| Jogador 3 | 3-6 | 10:54:13 | REROLL | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 3-6 | 10:54:14 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Vanguarda | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 3 | 3-7 | 10:54:17 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Vanguarda | DA_Scuttlecrab18 | -0.1800 |  |
| Jogador 3 | 3-7 | 10:54:18 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_ChainVest -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Vanguarda | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 3-7 | 10:54:18 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Vanguarda | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 3-7 | 10:54:19 | REROLL | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Vanguarda | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 3-7 | 10:54:20 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Vanguarda | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 3-7 | 10:54:20 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Vanguarda | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 3-7 | 10:54:21 | REROLL | STABILIZE | STABILIZE: pressão de vida | 39 | 3 | Vanguarda | DA_Scuttlecrab18 | -0.1700 |  |
| Jogador 3 | 3-7 | 10:54:22 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Vanguarda | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 3-7 | 10:54:22 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Vanguarda | DA_Scuttlecrab18 | 0.3400 |  |
| Jogador 3 | 4-1 | 10:54:26 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 54 | 4 | Vanguarda | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 3 | 4-1 | 10:54:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Vanguarda | DA_Scuttlecrab18 | 1.0300 |  |
| Jogador 3 | 4-1 | 10:54:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 4 | Vanguarda | DA_Scuttlecrab18 | 0.4400 |  |
| Jogador 3 | 4-1 | 10:54:28 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 48 | 4 | Vanguarda | DA_Scuttlecrab18 | 0.3800 |  |
| Jogador 3 | 4-1 | 10:54:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 46 | 4 | Vanguarda | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-1 | 10:54:29 | VENDEU: Aronguejo (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Vanguarda | DA_Scuttlecrab18 | -0.1800 |  |
| Jogador 3 | 4-1 | 10:54:30 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 48 | 4 | Vanguarda | DA_18_Rammus | 0.8600 |  |
| Jogador 3 | 4-1 | 10:54:31 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 4 | Vanguarda | DA_18_Rammus | 0.0100 |  |
| Jogador 3 | 4-1 | 10:54:32 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 45 | 4 | Vanguarda | DA_18_Rammus | 0.4000 |  |
| Jogador 4 | ? | 10:51:57 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 4 | ? | 10:51:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 4 | ? | 10:51:58 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6100 |  |
| Jogador 4 | ? | 10:51:59 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | ? | 10:52:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-1 | 10:52:04 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 4 | 1-1 | 10:52:05 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 4 | 1-1 | 10:52:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 4 | 1-1 | 10:52:06 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 4 | 1-1 | 10:52:07 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0400 |  |
| Jogador 4 | 1-1 | 10:52:07 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 4 | 1-1 | 10:52:08 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 4 | 1-1 | 10:52:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-2 | 10:52:11 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0100 |  |
| Jogador 4 | 1-2 | 10:52:12 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.3300 |  |
| Jogador 4 | 1-2 | 10:52:12 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Gromp18_AP | 0.2600 |  |
| Jogador 4 | 1-2 | 10:52:13 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 4 | 1-2 | 10:52:14 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Alistar | 0.1600 |  |
| Jogador 4 | 1-2 | 10:52:14 | MOVE Bench -> Board: Alistar (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Alistar | 0.0500 |  |
| Jogador 4 | 1-2 | 10:52:15 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Alistar | -0.0300 |  |
| Jogador 4 | 1-2 | 10:52:16 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Alistar | 0.1900 |  |
| Jogador 4 | 1-2 | 10:52:17 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Alistar | -0.3300 |  |
| Jogador 4 | 1-3 | 10:52:18 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Alistar | 1.0400 |  |
| Jogador 4 | 1-3 | 10:52:19 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Alistar | -0.4300 |  |
| Jogador 4 | 1-3 | 10:52:19 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Alistar | 1.0400 |  |
| Jogador 4 | 1-3 | 10:52:20 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Alistar | -0.4300 |  |
| Jogador 4 | 1-3 | 10:52:21 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Alistar | 1.0400 |  |
| Jogador 4 | 1-3 | 10:52:21 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Alistar | -0.3900 |  |
| Jogador 4 | 1-3 | 10:52:22 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Alistar | 0.0900 |  |
| Jogador 4 | 1-3 | 10:52:23 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Alistar | -0.0800 |  |
| Jogador 4 | 1-3 | 10:52:24 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Alistar | 0.2500 |  |
| Jogador 4 | 1-4 | 10:52:25 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Alistar | -0.3400 |  |
| Jogador 4 | 1-4 | 10:52:26 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Alistar | 1.0400 |  |
| Jogador 4 | 1-4 | 10:52:26 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Alistar | -0.7900 |  |
| Jogador 4 | 1-4 | 10:52:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Alistar | 0.2500 |  |
| Jogador 4 | 1-4 | 10:52:28 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Alistar | -0.4200 |  |
| Jogador 4 | 1-4 | 10:52:28 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Alistar | 0.2500 |  |
| Jogador 4 | 1-4 | 10:52:29 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Gromp18_AP | 0.2000 |  |
| Jogador 4 | 1-4 | 10:52:30 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Gromp18_AP | 0.1600 |  |
| Jogador 4 | 1-4 | 10:52:31 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Gromp18_AP | 0.1600 |  |
| Jogador 4 | 2-1 | 10:52:33 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Gromp18_AP | -0.3300 |  |
| Jogador 4 | 2-1 | 10:52:33 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | 0.2000 |  |
| Jogador 4 | 2-1 | 10:52:34 | MOVE Bench -> Board: Krugue (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | -0.0800 |  |
| Jogador 4 | 2-1 | 10:52:35 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Krug18 | -0.0700 |  |
| Jogador 4 | 2-1 | 10:52:36 | EQUIP_FROM_INVENTORY: TFT_Item_RunaansHurricane -> Krugue (i:6.0) (tabuleiro slot 0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Krug18 | 0.1000 |  |
| Jogador 4 | 2-1 | 10:52:36 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | 0.0400 |  |
| Jogador 4 | 2-1 | 10:52:37 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | 0.0800 |  |
| Jogador 4 | 2-1 | 10:52:38 | MOVE Board -> Board: Krugue (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 4 | 2-1 | 10:52:38 | MOVE Bench -> Board: Elise (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | -0.0900 |  |
| Jogador 4 | 2-2 | 10:52:40 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_Krug18 | -0.0300 |  |
| Jogador 4 | 2-2 | 10:52:41 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | — | DA_Krug18 | 1.0400 |  |
| Jogador 4 | 2-2 | 10:52:42 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_Krug18 | -0.5100 |  |
| Jogador 4 | 2-2 | 10:52:43 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_Krug18 | 0.2000 |  |
| Jogador 4 | 2-2 | 10:52:43 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_Krug18 | -0.3300 |  |
| Jogador 4 | 2-2 | 10:52:44 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | — | DA_Krug18 | 0.3200 |  |
| Jogador 4 | 2-2 | 10:52:45 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_Krug18 | -0.3700 |  |
| Jogador 4 | 2-2 | 10:52:45 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | — | DA_Krug18 | 0.2000 |  |
| Jogador 4 | 2-2 | 10:52:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_Krug18 | -0.0400 |  |
| Jogador 4 | 2-3 | 10:52:48 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_Krug18 | -0.2500 |  |
| Jogador 4 | 2-3 | 10:52:49 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_Aphelios | 0.1400 |  |
| Jogador 4 | 2-3 | 10:52:50 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_Aphelios | -0.3400 |  |
| Jogador 4 | 2-3 | 10:52:50 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-3 | 10:52:51 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_Aphelios | 0.3300 |  |
| Jogador 4 | 2-3 | 10:52:52 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Aphelios | -0.0700 |  |
| Jogador 4 | 2-3 | 10:52:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | — | DA_18_Aphelios | 0.3300 |  |
| Jogador 4 | 2-3 | 10:52:53 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Aphelios | -0.0700 |  |
| Jogador 4 | 2-3 | 10:52:54 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | — | DA_18_Aphelios | 0.3300 |  |
| Jogador 4 | 2-4 | 10:52:56 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Lutador | DA_18_Aphelios | -0.0700 |  |
| Jogador 4 | 2-4 | 10:52:57 | COMPROU: Krugue (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 21 | 1 | Lutador | DA_18_Aphelios | 1.0400 |  |
| Jogador 4 | 2-4 | 10:52:57 | MOVE Bench -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 21 | 1 | Lutador | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 2-4 | 10:52:58 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 21 | 1 | Lutador | DA_18_Aphelios | 0.3900 |  |
| Jogador 4 | 2-4 | 10:52:59 | COMPROU: Diana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | Lutador | DA_18_Aphelios | 0.2400 |  |
| Jogador 4 | 2-4 | 10:52:59 | MOVE Board -> Board: Krugue (i:6.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | Lutador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-4 | 10:53:00 | VENDEU: Diana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 21 | 1 | Lutador | DA_18_Aphelios | -0.1200 |  |
| Jogador 4 | 2-4 | 10:53:01 | COMPROU: Varus (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Lutador | DA_18_Aphelios | 0.2900 |  |
| Jogador 4 | 2-4 | 10:53:02 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 16 | 1 | Lutador | DA_18_Aphelios | -0.1600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-5 | 10:53:04 | VENDEU: Varus (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 24 | 1 | Lutador | DA_18_Aphelios | -0.0600 |  |
| Jogador 4 | 2-5 | 10:53:04 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 21 | 1 | Lutador | DA_18_Aphelios | 0.2800 |  |
| Jogador 4 | 2-5 | 10:53:05 | VENDEU: Mamãe Bicuda (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 24 | 1 | Lutador | DA_18_Aphelios | -0.1700 |  |
| Jogador 4 | 2-5 | 10:53:06 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 1 | Lutador | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 2-5 | 10:53:06 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 1 | Lutador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-5 | 10:53:07 | VENDEU: Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 24 | 1 | Lutador | DA_18_Aphelios | -0.3400 |  |
| Jogador 4 | 2-5 | 10:53:08 | COMPROU: Ornn (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Lutador | DA_18_Aphelios | 0.2500 |  |
| Jogador 4 | 2-5 | 10:53:09 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Lutador | DA_18_Aphelios | -0.1600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-5 | 10:53:09 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 15 | 1 | Lutador | DA_18_Aphelios | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-6 | 10:53:11 | VENDEU: Ornn (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 24 | 1 | Lutador | DA_18_Aphelios | -0.1000 |  |
| Jogador 4 | 2-6 | 10:53:12 | COMPROU: Akali (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Lutador | DA_18_Aphelios | 0.9400 |  |
| Jogador 4 | 2-6 | 10:53:13 | VENDEU: Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 24 | 1 | Lutador | DA_18_Aphelios | -0.3800 |  |
| Jogador 4 | 2-6 | 10:53:14 | COMPROU: Master Yi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 21 | 1 | Lutador | DA_18_Aphelios | 0.0200 |  |
| Jogador 4 | 2-6 | 10:53:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lutador | DA_18_Aphelios | -0.0500 |  |
| Jogador 4 | 2-6 | 10:53:15 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lutador | DA_18_Aphelios | -0.4000 |  |
| Jogador 4 | 2-6 | 10:53:16 | MOVE Bench -> Board: Alistar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lutador | DA_18_Aphelios | 0.4500 |  |
| Jogador 4 | 2-6 | 10:53:16 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Lutador | DA_18_Aphelios | 0.2300 |  |
| Jogador 4 | 2-6 | 10:53:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Lutador | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-7 | 10:53:19 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Lutador | DA_18_Aphelios | 0.0300 |  |
| Jogador 4 | 2-7 | 10:53:20 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Lutador | DA_18_Aphelios | 0.6700 |  |
| Jogador 4 | 2-7 | 10:53:21 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Lutador | DA_18_Aphelios | 0.1600 |  |
| Jogador 4 | 2-7 | 10:53:21 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Lutador | DA_18_Aphelios | -0.3000 |  |
| Jogador 4 | 2-7 | 10:53:22 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Lutador | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 2-7 | 10:53:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Lutador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-7 | 10:53:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Lutador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-7 | 10:53:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 1 | Lutador | DA_18_Aphelios | -0.0900 |  |
| Jogador 4 | 2-7 | 10:53:25 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 1 | Lutador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-1 | 10:53:27 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lutador | DA_18_Aphelios | 0.0300 |  |
| Jogador 4 | 3-1 | 10:53:28 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Aphelios | 0.1200 |  |
| Jogador 4 | 3-1 | 10:53:28 | MOVE Board -> Board: Aphelios (i:8.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-1 | 10:53:29 | MOVE Board -> Board: Krugue (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-1 | 10:53:30 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-2 | 10:53:35 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Lutador | DA_18_Aphelios | 0.1700 |  |
| Jogador 4 | 3-2 | 10:53:35 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lutador | DA_18_Aphelios | 0.7200 |  |
| Jogador 4 | 3-2 | 10:53:36 | MOVE Board -> Board: Krugue (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Lutador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 3-2 | 10:53:37 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Lutador | DA_18_Aphelios | -0.0900 |  |
| Jogador 4 | 3-2 | 10:53:37 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 3-2 | 10:53:38 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Aphelios | 0.4200 |  |
| Jogador 4 | 3-2 | 10:53:39 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Aphelios | 0.0200 |  |
| Jogador 4 | 3-2 | 10:53:40 | MOVE Board -> Board: Aphelios (i:8.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-2 | 10:53:40 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 3-3 | 10:53:43 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Lutador | DA_18_Aphelios | 0.4900 |  |
| Jogador 4 | 3-3 | 10:53:44 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Lutador | DA_18_Akali_AD | 0.7600 |  |
| Jogador 4 | 3-3 | 10:53:44 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Lutador | DA_18_Akali_AD | 0.4000 |  |
| Jogador 4 | 3-3 | 10:53:45 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 3-3 | 10:53:46 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Akali_AD | -0.0800 |  |
| Jogador 4 | 3-3 | 10:53:47 | MOVE Board -> Board: Alistar (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 10:53:47 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 4 | 3-3 | 10:53:48 | MOVE Board -> Board: Aphelios (i:8.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 3-3 | 10:53:49 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 10:53:51 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_MasterYi_AD | 0.7400 |  |
| Jogador 4 | 3-4 | 10:53:52 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_MasterYi_AD | 0.1400 |  |
| Jogador 4 | 3-4 | 10:53:53 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Lutador | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 4 | 3-4 | 10:53:54 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_MasterYi_AD | 0.7400 |  |
| Jogador 4 | 3-4 | 10:53:54 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.1000 |  |
| Jogador 4 | 3-4 | 10:53:55 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 10:53:56 | MOVE Board -> Board: Alistar (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.1600 |  |
| Jogador 4 | 3-4 | 10:53:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 10:53:57 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.4200 |  |
| Jogador 4 | 3-5 | 10:54:00 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Lutador | DA_18_MasterYi_AD | 0.7300 |  |
| Jogador 4 | 3-5 | 10:54:01 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_MasterYi_AD | 0.3200 |  |
| Jogador 4 | 3-5 | 10:54:01 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 4 | 3-5 | 10:54:02 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 3-5 | 10:54:03 | MOVE Board -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 10:54:03 | MOVE Board -> Board: Aphelios (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 4 | 3-5 | 10:54:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 10:54:08 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 4 | 3-6 | 10:54:09 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.5200 |  |
| Jogador 4 | 3-6 | 10:54:10 | MOVE Board -> Board: Aphelios (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 10:54:10 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.4200 |  |
| Jogador 4 | 3-6 | 10:54:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 10:54:17 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Lutador | DA_18_MasterYi_AD | 0.7700 |  |
| Jogador 4 | 3-7 | 10:54:18 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 3-7 | 10:54:18 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.6000 |  |
| Jogador 4 | 3-7 | 10:54:19 | MOVE Board -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-7 | 10:54:20 | MOVE Board -> Board: Aphelios (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 3-7 | 10:54:20 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_BFSword -> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 4 | 3-7 | 10:54:21 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 4 | 3-7 | 10:54:22 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 10:54:22 | MOVE Board -> Board: Aphelios (i:8.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-1 | 10:54:26 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Lutador | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 4 | 4-1 | 10:54:27 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 4-1 | 10:54:27 | MOVE Board -> Board: Krugue (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.3100 |  |
| Jogador 4 | 4-1 | 10:54:28 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-1 | 10:54:29 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-1 | 10:54:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 10:54:35 | VENDEU: Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Lutador | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 4-2 | 10:54:36 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Lutador | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 4 | 4-2 | 10:54:36 | VENDEU: Cassiopeia (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Lutador | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 4-2 | 10:54:37 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lutador | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 4 | 4-2 | 10:54:38 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 10:54:39 | MOVE Board -> Board: Aphelios (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lutador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-2 | 10:54:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-3 | 10:54:44 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Lutador | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 4 | 4-3 | 10:54:45 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lutador | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 4 | 4-3 | 10:54:46 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Lutador | DA_18_MasterYi_AD | 0.1400 |  |
| Jogador 4 | 4-3 | 10:54:46 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lutador | DA_18_MasterYi_AD | -0.1900 |  |
| Jogador 4 | 4-3 | 10:54:47 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Lutador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-3 | 10:54:48 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Lutador | DA_18_MasterYi_AD | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 4 | 4-3 | 10:54:48 | VENDEU: Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Lutador | DA_18_MasterYi_AD | -0.1100 |  |
| Jogador 4 | 4-3 | 10:54:49 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Krugue (i:6.0) (tabuleiro slot 2) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Lutador | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 4 | 4-3 | 10:54:50 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Lutador | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 4-4 | 10:54:53 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Lutador | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 4 | 4-4 | 10:54:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Lutador | DA_18_MasterYi_AD | 0.6600 |  |
| Jogador 4 | 4-4 | 10:54:55 | VENDEU: Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 1 | Lutador | DA_18_Aphelios | 0.0100 |  |
| Jogador 4 | 4-4 | 10:54:56 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Lutador | DA_18_Aphelios | -0.2200 |  |
| Jogador 4 | 4-4 | 10:54:56 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 1 | Lutador | DA_18_Aphelios | 0.1500 |  |
| Jogador 4 | 4-4 | 10:54:57 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Lutador | DA_18_Aphelios | 0.5000 |  |
| Jogador 4 | 4-4 | 10:54:58 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Lutador | DA_18_Aphelios | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 4 | 4-4 | 10:54:58 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Lutador | DA_18_Aphelios | -0.1300 |  |
| Jogador 4 | 4-4 | 10:54:59 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Lutador | DA_18_Aphelios | 0.2300 |  |
| Jogador 4 | 4-5 | 10:55:03 | VENDEU: Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Lutador | DA_18_Aphelios | 0.0600 |  |
| Jogador 4 | 4-5 | 10:55:03 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Lutador | DA_18_Aphelios | 0.7700 |  |
| Jogador 4 | 4-5 | 10:55:04 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Lutador | DA_18_Aphelios | 0.0700 |  |
| Jogador 4 | 4-5 | 10:55:05 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Lutador | DA_18_Aphelios | 0.6500 |  |
| Jogador 4 | 4-5 | 10:55:05 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Lutador | DA_18_Aphelios | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 4 | 4-5 | 10:55:06 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Lutador | DA_18_Aphelios | -0.1400 |  |
| Jogador 4 | 4-5 | 10:55:07 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Lutador | DA_18_Aphelios | 0.6600 |  |
| Jogador 4 | 4-5 | 10:55:07 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Lutador | DA_18_Aphelios | -0.1400 |  |
| Jogador 4 | 4-5 | 10:55:08 | COMPROU: Kobuko (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Lutador | DA_18_Aphelios | 0.2500 |  |
| Jogador 4 | 4-6 | 10:55:12 | VENDEU: Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Lutador | DA_18_Aphelios | -0.0900 |  |
| Jogador 4 | 4-6 | 10:55:13 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Lutador | DA_KogMaw18_AD | 0.8500 |  |
| Jogador 4 | 4-6 | 10:55:14 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Lutador | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 4 | 4-6 | 10:55:14 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Lutador | DA_KogMaw18_AD | 0.5500 |  |
| Jogador 4 | 4-6 | 10:55:15 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Lutador | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 4 | 4-6 | 10:55:16 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Lutador | DA_KogMaw18_AD | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 4 | 4-6 | 10:55:17 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Lutador | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 4-6 | 10:55:17 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Lutador | DA_18_Aphelios | -0.0500 |  |
| Jogador 4 | 4-6 | 10:55:18 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Lutador | DA_18_Aphelios | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 4 | 4-7 | 10:55:22 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_SparringGloves -> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Lutador | DA_18_Aphelios | 0.1800 |  |
| Jogador 4 | 4-7 | 10:55:22 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Lutador | DA_18_Aphelios | 0.1500 |  |
| Jogador 4 | 4-7 | 10:55:23 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Lutador | DA_18_Aphelios | 0.1400 |  |
| Jogador 4 | 4-7 | 10:55:24 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Lutador | DA_18_Aphelios | 0.3300 |  |
| Jogador 4 | 4-7 | 10:55:24 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Lutador | DA_18_Aphelios | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 4 | 4-7 | 10:55:25 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Lutador | DA_18_Aphelios | -0.1200 |  |
| Jogador 4 | 4-7 | 10:55:26 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 4 | Lutador | DA_18_Aphelios | 0.8300 |  |
| Jogador 4 | 4-7 | 10:55:26 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Lutador | DA_18_Aphelios | 0.1500 |  |
| Jogador 4 | 4-7 | 10:55:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 4 | Lutador | DA_18_Aphelios | -0.1000 |  |
| Jogador 4 | 5-1 | 10:55:31 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 4 | Lutador | DA_18_Aphelios | 0.0600 |  |
| Jogador 4 | 5-1 | 10:55:32 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 4 | Lutador | DA_18_Aphelios | 0.6500 |  |
| Jogador 4 | 5-1 | 10:55:33 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Lutador | DA_18_Aphelios | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-1 | 10:55:33 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Lutador | DA_18_Aphelios | -0.1400 |  |
| Jogador 4 | 5-1 | 10:55:34 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 4 | Lutador | DA_18_Aphelios | 0.2800 |  |
| Jogador 4 | 5-1 | 10:55:35 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Lutador | DA_18_Aphelios | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-1 | 10:55:36 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Lutador | DA_18_Aphelios | 0.0500 |  |
| Jogador 4 | 5-1 | 10:55:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 4 | Lutador | DA_18_Aphelios | 0.9500 |  |
| Jogador 4 | 5-1 | 10:55:37 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 4 | Lutador | DA_18_Aphelios | 0.6000 |  |
| Jogador 4 | 5-2 | 10:55:41 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Lutador | DA_18_Ezreal | 0.6600 |  |
| Jogador 4 | 5-2 | 10:55:42 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Lutador | DA_18_Ezreal | -0.1900 |  |
| Jogador 4 | 5-2 | 10:55:43 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Lutador | DA_18_Ezreal | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-2 | 10:55:43 | VENDEU: Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Lutador | DA_18_Ezreal | -0.1500 |  |
| Jogador 4 | 5-2 | 10:55:44 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Krugue (i:6.0) (tabuleiro slot 17) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Lutador | DA_18_Ezreal | 0.1200 |  |
| Jogador 4 | 5-2 | 10:55:45 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Krugue (i:6.0) (tabuleiro slot 17) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Lutador | DA_18_Ezreal | 0.1000 |  |
| Jogador 4 | 5-2 | 10:55:45 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Lutador | DA_18_Ezreal | 0.8200 |  |
| Jogador 4 | 5-2 | 10:55:46 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Lutador | DA_18_Ezreal | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-2 | 10:55:47 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Lutador | DA_18_Ezreal | 0.0700 |  |
| Jogador 4 | 5-3 | 10:55:52 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Lutador | DA_18_Alistar | 0.9500 |  |
| Jogador 4 | 5-3 | 10:55:52 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Lutador | DA_18_Alistar | -0.0300 |  |
| Jogador 4 | 5-3 | 10:55:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Lutador | DA_18_Alistar | 0.4200 |  |
| Jogador 4 | 5-3 | 10:55:54 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Lutador | DA_18_Alistar | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-3 | 10:55:55 | VENDEU: Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Lutador | DA_18_Ezreal | -0.2000 |  |
| Jogador 4 | 5-3 | 10:55:55 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Lutador | DA_Krug18 | 0.9500 |  |
| Jogador 4 | 5-3 | 10:55:56 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Soraka (i:8.0) (banco slot 4) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Lutador | DA_Krug18 | 0.0700 |  |
| Jogador 4 | 5-3 | 10:55:57 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Soraka (i:8.0) (banco slot 4) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Lutador | DA_Krug18 | 0.0400 |  |
| Jogador 4 | 5-3 | 10:55:57 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Lutador | DA_Krug18 | 0.1900 |  |
| Jogador 4 | 5-4 | 10:56:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Lutador | DA_Krug18 | 0.9500 |  |
| Jogador 4 | 5-4 | 10:56:03 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Lutador | DA_Krug18 | -0.0500 |  |
| Jogador 4 | 5-4 | 10:56:04 | MOVE Bench -> Board: Krugue (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Lutador | DA_Krug18 | 0.3700 |  |
| Jogador 4 | 5-4 | 10:56:04 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Lutador | DA_Krug18 | 0.0100 |  |
| Jogador 4 | 5-4 | 10:56:05 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Lutador | DA_Krug18 | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-4 | 10:56:06 | VENDEU: LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Lutador | DA_Krug18 | -0.1700 |  |
| Jogador 4 | 5-4 | 10:56:07 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Lutador | DA_Krug18 | 0.3900 |  |
| Jogador 4 | 5-4 | 10:56:07 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Krugue (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Lutador | DA_Krug18 | -0.6500 |  |
| Jogador 4 | 5-5 | 10:56:14 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Lutador | DA_Krug18 | 0.1600 |  |
| Jogador 4 | 5-5 | 10:56:18 | VENDEU: Krugue (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 83 | 5 | Lutador | DA_18_Ezreal | -0.2100 |  |
| Jogador 4 | 5-5 | 10:56:19 | EQUIP_FROM_INVENTORY: TFT_Item_RunaansHurricane -> Aphelios (i:8.0) (tabuleiro slot 9) | FAST8 | FAST8: composição planejada exige nível 8 | 83 | 5 | Lutador | DA_18_Ezreal | 0.0900 |  |
| Jogador 4 | 5-5 | 10:56:19 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Aphelios (i:8.0) (tabuleiro slot 9) | FAST8 | FAST8: composição planejada exige nível 8 | 83 | 5 | Lutador | DA_18_Ezreal | 0.0600 |  |
| Jogador 4 | 5-6 | 10:56:23 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Aphelios (i:8.0) (tabuleiro slot 9) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Lutador | DA_18_Ezreal | 0.1300 |  |
| Jogador 4 | 5-6 | 10:56:24 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 91 | 5 | Lutador | DA_18_Ezreal | 0.9400 |  |
| Jogador 4 | 5-6 | 10:56:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 89 | 5 | Lutador | DA_18_Ezreal | 0.5900 |  |
| Jogador 4 | 5-6 | 10:56:26 | MOVE Bench -> Board: Ezreal (i:16.0) <-> Rubrivira (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 89 | 5 | Lutador | DA_18_Ezreal | -0.2700 |  |
| Jogador 4 | 5-6 | 10:56:26 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Lutador | DA_18_Ezreal | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-6 | 10:56:27 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 89 | 5 | Lutador | DA_18_Ezreal | -0.1400 |  |
| Jogador 4 | 5-7 | 10:56:34 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Soraka (i:8.0) (banco slot 4) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Lutador | DA_18_Ezreal | 0.1000 |  |
| Jogador 4 | 5-7 | 10:56:35 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 97 | 5 | Lutador | DA_18_Ezreal | 0.8900 |  |
| Jogador 4 | 5-7 | 10:56:35 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Lutador | DA_18_Ezreal | 0.4600 |  |
| Jogador 4 | 5-7 | 10:56:36 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 91 | 5 | Lutador | DA_18_Ezreal | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-7 | 10:56:37 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Lutador | DA_18_Ezreal | -0.1200 |  |
| Jogador 4 | 5-7 | 10:56:37 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Lutador | DA_18_Ezreal | 0.0200 |  |
| Jogador 4 | 5-7 | 10:56:38 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Lutador | DA_18_Ezreal | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 5-7 | 10:56:39 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 91 | 5 | Lutador | DA_18_Ezreal | 0.0600 |  |
| Jogador 4 | 5-7 | 10:56:40 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Lutador | DA_18_Ezreal | 0.3200 |  |
| Jogador 4 | 6-1 | 10:56:48 | VENDEU: Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Lutador | DA_18_Ezreal | 0.0600 |  |
| Jogador 4 | 6-1 | 10:56:48 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Lutador | DA_18_Ezreal | 1.0100 |  |
| Jogador 4 | 6-1 | 10:56:49 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Ezreal (i:16.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Lutador | DA_18_Ezreal | -0.6300 |  |
| Jogador 4 | 6-1 | 10:56:49 | MOVE Bench -> Board: Ezreal (i:16.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Lutador | DA_18_Ezreal | 0.2200 |  |
| Jogador 4 | 6-1 | 10:56:50 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Lutador | DA_18_Ezreal | 0.8400 |  |
| Jogador 4 | 6-1 | 10:56:51 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Lutador | DA_18_Ezreal | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 6-1 | 10:56:52 | VENDEU: Fiddlesticks (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Lutador | DA_18_Ezreal | -0.1700 |  |
| Jogador 4 | 6-1 | 10:56:52 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Lutador | DA_18_Ezreal | 0.3300 |  |
| Jogador 4 | 6-1 | 10:56:53 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Fera do Rift | DA_18_Ezreal | 0.6000 |  |
| Jogador 4 | 6-2 | 10:57:01 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Fera do Rift | DA_18_Ezreal | -0.1900 |  |
| Jogador 4 | 6-2 | 10:57:01 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 4 | 6-2 | 10:57:02 | VENDEU: Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 104 | 5 | Fera do Rift | DA_18_Ezreal | 0.0700 |  |
| Jogador 4 | 6-2 | 10:57:03 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Fera do Rift | DA_18_Ezreal | 1.0100 |  |
| Jogador 4 | 6-2 | 10:57:04 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Rubrivira (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Fera do Rift | DA_18_Ezreal | -0.0500 |  |
| Jogador 4 | 6-2 | 10:57:04 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Fera do Rift | DA_18_Ezreal | 0.3700 |  |
| Jogador 4 | 6-2 | 10:57:05 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Fera do Rift | DA_18_Ezreal | 0.9100 |  |
| Jogador 4 | 6-2 | 10:57:06 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Fera do Rift | DA_18_Ezreal | -0.3600 |  |
| Jogador 4 | 6-2 | 10:57:06 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Fera do Rift | DA_18_Ezreal | 0.3900 |  |
| Jogador 4 | 6-3 | 10:57:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Fera do Rift | DA_18_Ezreal | 1.0800 |  |
| Jogador 4 | 6-3 | 10:57:15 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Fera do Rift | DA_18_Ezreal | 0.1000 |  |
| Jogador 4 | 6-3 | 10:57:15 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Fera do Rift | DA_18_Ezreal | 0.6000 |  |
| Jogador 4 | 6-3 | 10:57:16 | REROLL | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-3 | 10:57:17 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Fera do Rift | DA_18_Ezreal | 0.2500 |  |
| Jogador 4 | 6-3 | 10:57:18 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Fera do Rift | DA_18_Ezreal | 0.3900 |  |
| Jogador 4 | 6-3 | 10:57:18 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Fera do Rift | DA_18_Ezreal | 0.4000 |  |
| Jogador 4 | 6-3 | 10:57:19 | REROLL | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-3 | 10:57:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-4 | 10:57:28 | REROLL | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-4 | 10:57:29 | REROLL | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-4 | 10:57:30 | VENDEU: Krugue (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Fera do Rift | DA_18_Ezreal | -0.1900 |  |
| Jogador 4 | 6-4 | 10:57:30 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Fera do Rift | DA_18_Ezreal | 0.9200 |  |
| Jogador 4 | 6-4 | 10:57:31 | REROLL | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-4 | 10:57:32 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Fera do Rift | DA_18_Ezreal | -0.1900 |  |
| Jogador 4 | 6-4 | 10:57:32 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Rubrivira (i:8.0) (banco slot 2) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Fera do Rift | DA_18_Ezreal | 0.1500 |  |
| Jogador 4 | 6-4 | 10:57:33 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Rubrivira (i:8.0) (banco slot 2) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Fera do Rift | DA_18_Ezreal | 0.0900 |  |
| Jogador 4 | 6-4 | 10:57:34 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Fera do Rift | DA_18_Ezreal | 0.4200 |  |
| Jogador 4 | 6-5 | 10:57:42 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-5 | 10:57:43 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Fera do Rift | DA_18_Ezreal | 0.0600 |  |
| Jogador 4 | 6-5 | 10:57:44 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Fera do Rift | DA_18_Ezreal | 1.0600 |  |
| Jogador 4 | 6-5 | 10:57:44 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Fera do Rift | DA_18_Ezreal | 0.9300 |  |
| Jogador 4 | 6-5 | 10:57:45 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-5 | 10:57:46 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Fera do Rift | DA_18_Ezreal | 0.5400 |  |
| Jogador 4 | 6-5 | 10:57:46 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fera do Rift | DA_18_Ezreal | 0.2300 |  |
| Jogador 4 | 6-5 | 10:57:47 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 4 | 6-5 | 10:57:48 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Fera do Rift | DA_18_Ezreal | -0.0900 |  |
| Jogador 5 | ? | 10:51:57 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0200 |  |
| Jogador 5 | ? | 10:51:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 5 | ? | 10:51:58 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6100 |  |
| Jogador 5 | ? | 10:51:59 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 5 | ? | 10:52:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 5 | 1-1 | 10:52:04 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0300 |  |
| Jogador 5 | 1-1 | 10:52:05 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.3000 |  |
| Jogador 5 | 1-1 | 10:52:05 | MOVE Board -> Board: Elise (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | -0.0200 |  |
| Jogador 5 | 1-1 | 10:52:06 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | -0.0100 |  |
| Jogador 5 | 1-1 | 10:52:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 1-2 | 10:52:11 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.2500 |  |
| Jogador 5 | 1-2 | 10:52:12 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | -0.1200 |  |
| Jogador 5 | 1-2 | 10:52:12 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0800 |  |
| Jogador 5 | 1-2 | 10:52:13 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | -0.0800 |  |
| Jogador 5 | 1-2 | 10:52:14 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | 0.0600 |  |
| Jogador 5 | 1-2 | 10:52:14 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | -0.0800 |  |
| Jogador 5 | 1-2 | 10:52:15 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | 0.0600 |  |
| Jogador 5 | 1-2 | 10:52:16 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | 0.4100 |  |
| Jogador 5 | 1-2 | 10:52:17 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0800 |  |
| Jogador 5 | 1-3 | 10:52:18 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | 0.0100 |  |
| Jogador 5 | 1-3 | 10:52:19 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | 0.1700 |  |
| Jogador 5 | 1-3 | 10:52:19 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | -0.1000 |  |
| Jogador 5 | 1-3 | 10:52:20 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | 0.1700 |  |
| Jogador 5 | 1-3 | 10:52:21 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | -0.1000 |  |
| Jogador 5 | 1-3 | 10:52:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | 0.3300 |  |
| Jogador 5 | 1-3 | 10:52:22 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | -0.1400 |  |
| Jogador 5 | 1-3 | 10:52:23 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | 0.0800 |  |
| Jogador 5 | 1-3 | 10:52:24 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | 0.0100 |  |
| Jogador 5 | 1-4 | 10:52:25 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.2000 |  |
| Jogador 5 | 1-4 | 10:52:26 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Elise | -0.4100 |  |
| Jogador 5 | 1-4 | 10:52:26 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Elise | 0.1000 |  |
| Jogador 5 | 1-4 | 10:52:27 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Elise | -0.3800 |  |
| Jogador 5 | 1-4 | 10:52:28 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Elise | 0.3100 |  |
| Jogador 5 | 1-4 | 10:52:28 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Elise | -0.3600 |  |
| Jogador 5 | 1-4 | 10:52:29 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Elise | 0.1600 |  |
| Jogador 5 | 1-4 | 10:52:30 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Elise | -0.3900 |  |
| Jogador 5 | 1-4 | 10:52:31 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Elise | 0.3900 |  |
| Jogador 5 | 2-1 | 10:52:33 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 5 | 2-1 | 10:52:33 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 5 | 2-1 | 10:52:34 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 5 | 2-1 | 10:52:35 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 5 | 2-1 | 10:52:36 | MOVE Bench -> Board: Rammus (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rammus | -0.5300 |  |
| Jogador 5 | 2-1 | 10:52:36 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rammus | -0.1000 |  |
| Jogador 5 | 2-1 | 10:52:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 2-2 | 10:52:40 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 2-2 | 10:52:41 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 0.3500 |  |
| Jogador 5 | 2-2 | 10:52:42 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Rammus | -0.0600 |  |
| Jogador 5 | 2-2 | 10:52:43 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 0.2800 |  |
| Jogador 5 | 2-2 | 10:52:43 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Rammus | -0.3400 |  |
| Jogador 5 | 2-2 | 10:52:44 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 2-2 | 10:52:45 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 0.1000 |  |
| Jogador 5 | 2-2 | 10:52:45 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 0.1400 |  |
| Jogador 5 | 2-2 | 10:52:46 | MOVE Board -> Board: Rammus (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-3 | 10:52:48 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-3 | 10:52:49 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | — | DA_18_MasterYi_AD | 0.1700 |  |
| Jogador 5 | 2-3 | 10:52:50 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | — | DA_18_MasterYi_AD | 0.0400 |  |
| Jogador 5 | 2-3 | 10:52:50 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | — | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 5 | 2-3 | 10:52:51 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | — | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 5 | 2-3 | 10:52:52 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | — | DA_18_MasterYi_AD | -0.2200 |  |
| Jogador 5 | 2-3 | 10:52:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_18_MasterYi_AD | 0.2900 |  |
| Jogador 5 | 2-3 | 10:52:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_MasterYi_AD | -0.0300 |  |
| Jogador 5 | 2-3 | 10:52:54 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_MasterYi_AD | 0.4500 |  |
| Jogador 5 | 2-4 | 10:52:56 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Defendente | DA_18_Rammus | 1.0300 |  |
| Jogador 5 | 2-4 | 10:52:57 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Defendente | DA_18_Rammus | 0.1000 |  |
| Jogador 5 | 2-4 | 10:52:57 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Defendente | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 2-4 | 10:52:58 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Defendente | DA_18_Rammus | -0.4100 |  |
| Jogador 5 | 2-4 | 10:52:59 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 2-4 | 10:52:59 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Defendente | DA_18_Rammus | -0.3500 |  |
| Jogador 5 | 2-4 | 10:53:00 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Defendente | DA_18_Rammus | -0.4000 |  |
| Jogador 5 | 2-4 | 10:53:01 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 2-5 | 10:53:04 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kha'Zix (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Defendente | DA_18_Rammus | 0.1000 |  |
| Jogador 5 | 2-5 | 10:53:04 | MOVE Board -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 2-5 | 10:53:05 | MOVE Board -> Board: Rammus (i:6.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 2-5 | 10:53:06 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 2-6 | 10:53:11 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Defendente | DA_18_Rammus | -0.4000 |  |
| Jogador 5 | 2-6 | 10:53:12 | MOVE Bench -> Board: Rammus (i:6.0) <-> Veigar (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 2-6 | 10:53:13 | VENDEU: Veigar (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 40 | 3 | Defendente | DA_18_Rammus | -0.0700 |  |
| Jogador 5 | 2-6 | 10:53:14 | COMPROU: Yunara (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 3 | Defendente | DA_18_Rammus | -0.1700 |  |
| Jogador 5 | 2-6 | 10:53:14 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 34 | 3 | Defendente | DA_18_Rammus | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 5 | 2-6 | 10:53:15 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 3 | Defendente | DA_18_Rammus | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 5 | 2-6 | 10:53:16 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 3 | Defendente | DA_18_Rammus | -0.1600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 5 | 2-6 | 10:53:16 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 3 | Defendente | DA_18_Rammus | 0.0200 |  |
| Jogador 5 | 2-6 | 10:53:17 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 3 | Defendente | DA_18_Rammus | 0.4000 |  |
| Jogador 5 | 2-7 | 10:53:19 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Defendente | DA_18_Rammus | 0.5700 |  |
| Jogador 5 | 2-7 | 10:53:20 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Defendente | DA_18_Rammus | -0.3400 |  |
| Jogador 5 | 2-7 | 10:53:21 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Defendente | DA_18_Tristana | 0.0200 |  |
| Jogador 5 | 2-7 | 10:53:21 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Defendente | DA_18_Rammus | -0.3300 |  |
| Jogador 5 | 2-7 | 10:53:22 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Defendente | DA_18_Rammus | 0.1700 |  |
| Jogador 5 | 2-7 | 10:53:23 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_ChainVest -> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Defendente | DA_18_Rammus | 0.0600 |  |
| Jogador 5 | 2-7 | 10:53:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Defendente | DA_18_Rammus | 0.0100 |  |
| Jogador 5 | 2-7 | 10:53:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Defendente | DA_18_Rammus | 0.0100 |  |
| Jogador 5 | 2-7 | 10:53:25 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 2 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 3-1 | 10:53:27 | VENDEU: Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Defendente | DA_18_Rammus | -0.1600 |  |
| Jogador 5 | 3-1 | 10:53:28 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Defendente | DA_18_Rammus | 0.2400 |  |
| Jogador 5 | 3-1 | 10:53:28 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-1 | 10:53:29 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Defendente | DA_18_Rammus | -0.1700 |  |
| Jogador 5 | 3-1 | 10:53:30 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Defendente | DA_18_Rammus | 0.6400 |  |
| Jogador 5 | 3-1 | 10:53:30 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Defendente | DA_18_Rammus | -0.4200 |  |
| Jogador 5 | 3-1 | 10:53:31 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Defendente | DA_18_Tristana | 0.1000 |  |
| Jogador 5 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Defendente | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Defendente | DA_18_Tristana | -0.0900 |  |
| Jogador 5 | 3-2 | 10:53:35 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Defendente | DA_18_Rammus | -0.4100 |  |
| Jogador 5 | 3-2 | 10:53:35 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 1 | Defendente | DA_18_Rammus | 0.8000 |  |
| Jogador 5 | 3-2 | 10:53:36 | MOVE Bench -> Board: Rammus (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Defendente | DA_18_Rammus | 0.3500 |  |
| Jogador 5 | 3-2 | 10:53:37 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Defendente | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 3-2 | 10:53:37 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Defendente | DA_18_Rammus | 0.4400 |  |
| Jogador 5 | 3-2 | 10:53:38 | MOVE Board -> Board: Ahri (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-2 | 10:53:39 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Defendente | DA_18_Rammus | 0.5800 |  |
| Jogador 5 | 3-2 | 10:53:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-2 | 10:53:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Defendente | DA_18_Rammus | -0.0300 |  |
| Jogador 5 | 3-3 | 10:53:43 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Defendente | DA_18_Rammus | -0.4100 |  |
| Jogador 5 | 3-3 | 10:53:44 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Defendente | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 3-3 | 10:53:44 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Defendente | DA_18_Rammus | -0.3900 |  |
| Jogador 5 | 3-3 | 10:53:45 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Defendente | DA_18_Rammus | -0.2500 |  |
| Jogador 5 | 3-3 | 10:53:46 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Defendente | DA_18_Rammus | 0.4000 |  |
| Jogador 5 | 3-3 | 10:53:47 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Defendente | DA_18_Rammus | 0.1400 |  |
| Jogador 5 | 3-3 | 10:53:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 3-3 | 10:53:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-3 | 10:53:49 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-4 | 10:53:51 | VENDEU: Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | -0.3400 |  |
| Jogador 5 | 3-4 | 10:53:52 | COMPROU: Morgana (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.2300 |  |
| Jogador 5 | 3-4 | 10:53:53 | MOVE Bench -> Board: Morgana (i:8.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | 0.0300 |  |
| Jogador 5 | 3-4 | 10:53:54 | MOVE Board -> Board: Morgana (i:8.0) <-> Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-4 | 10:53:54 | MOVE Board -> Board: Ahri (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-4 | 10:53:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-5 | 10:54:00 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Defendente | DA_18_Rammus | 0.1000 |  |
| Jogador 5 | 3-5 | 10:54:01 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | -0.1300 |  |
| Jogador 5 | 3-5 | 10:54:01 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-5 | 10:54:02 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-5 | 10:54:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-6 | 10:54:08 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 3-6 | 10:54:09 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-6 | 10:54:10 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Defendente | DA_18_Rammus | -0.2400 |  |
| Jogador 5 | 3-6 | 10:54:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 3-6 | 10:54:11 | MOVE Board -> Board: Rammus (i:12.0) <-> Morgana (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-6 | 10:54:12 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Defendente | DA_18_Rammus | -0.2400 |  |
| Jogador 5 | 3-6 | 10:54:13 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Defendente | DA_18_Rammus | -0.2700 |  |
| Jogador 5 | 3-6 | 10:54:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 3-6 | 10:54:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 3-7 | 10:54:17 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 0 | Defendente | DA_18_Rammus | -0.2900 |  |
| Jogador 5 | 3-7 | 10:54:18 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Defendente | DA_18_Rammus | 0.2500 |  |
| Jogador 5 | 3-7 | 10:54:18 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_ChainVest -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Defendente | DA_18_Rammus | 0.1300 |  |
| Jogador 5 | 3-7 | 10:54:19 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Defendente | DA_18_Rammus | 0.1200 |  |
| Jogador 5 | 3-7 | 10:54:20 | MOVE Board -> Board: Morgana (i:8.0) <-> Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 3-7 | 10:54:20 | MOVE Board -> Board: Ahri (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 3-7 | 10:54:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Defendente | DA_18_Rammus | -0.1000 |  |
| Jogador 5 | 4-1 | 10:54:26 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Defendente | DA_18_Rammus | -0.2200 |  |
| Jogador 5 | 4-1 | 10:54:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Defendente | DA_18_Rammus | 0.2800 |  |
| Jogador 5 | 4-1 | 10:54:27 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Defendente | DA_18_Rammus | -0.5000 |  |
| Jogador 5 | 4-1 | 10:54:28 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Defendente | DA_18_Rammus | 0.1200 |  |
| Jogador 5 | 4-1 | 10:54:29 | MOVE Bench -> Board: Soraka (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Defendente | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 4-1 | 10:54:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Defendente | DA_18_Rammus | -0.0800 |  |
| Jogador 5 | 4-1 | 10:54:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-1 | 10:54:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 4-1 | 10:54:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 1 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-2 | 10:54:35 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 4-2 | 10:54:36 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Defendente | DA_18_Rammus | 0.2500 |  |
| Jogador 5 | 4-2 | 10:54:36 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 4-2 | 10:54:37 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 4-2 | 10:54:38 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.6000 |  |
| Jogador 5 | 4-2 | 10:54:39 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | -0.1300 |  |
| Jogador 5 | 4-2 | 10:54:39 | MOVE Board -> Board: Rammus (i:6.0) <-> Rammus (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-2 | 10:54:40 | MOVE Board -> Board: Rammus (i:12.0) <-> Morgana (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-2 | 10:54:41 | MOVE Board -> Board: Morgana (i:8.0) <-> Kha'Zix (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-3 | 10:54:44 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 4-3 | 10:54:45 | COMPROU: Teemo (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.1300 |  |
| Jogador 5 | 4-3 | 10:54:46 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Ahri (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-3 | 10:54:46 | MOVE Board -> Board: Ahri (i:8.0) <-> Soraka (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-3 | 10:54:47 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-4 | 10:54:53 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Defendente | DA_18_Rammus | 0.2700 |  |
| Jogador 5 | 4-4 | 10:54:54 | MOVE Board -> Board: Soraka (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-4 | 10:54:55 | COMPROU: Akali (Custo 1 \| i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Defendente | DA_18_Rammus | 0.1800 |  |
| Jogador 5 | 4-4 | 10:54:56 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 4-4 | 10:54:56 | MOVE Board -> Board: Soraka (i:8.0) <-> Rammus (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-4 | 10:54:57 | MOVE Board -> Board: Rammus (i:6.0) <-> Rammus (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 4-4 | 10:54:58 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-5 | 10:55:03 | COMPROU: Morgana (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Defendente | DA_18_Rammus | 0.7200 |  |
| Jogador 5 | 4-5 | 10:55:03 | COMPROU: Azuporã (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Defendente | DA_18_Rammus | 0.1200 |  |
| Jogador 5 | 4-5 | 10:55:04 | MOVE Board -> Board: Rammus (i:12.0) <-> Kha'Zix (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-5 | 10:55:05 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Ahri (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-5 | 10:55:05 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-6 | 10:55:12 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.2100 |  |
| Jogador 5 | 4-6 | 10:55:13 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Defendente | DA_18_Rammus | 0.5000 |  |
| Jogador 5 | 4-6 | 10:55:14 | VENDEU: Sejuani (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Defendente | DA_18_Rammus | -0.1100 |  |
| Jogador 5 | 4-6 | 10:55:14 | COMPROU: Amumu (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | -0.2100 |  |
| Jogador 5 | 4-6 | 10:55:15 | MOVE Board -> Board: Ahri (i:8.0) <-> Morgana (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-6 | 10:55:16 | MOVE Board -> Board: Morgana (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-6 | 10:55:17 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-7 | 10:55:22 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Defendente | DA_18_Rammus | 0.1700 |  |
| Jogador 5 | 4-7 | 10:55:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.2200 |  |
| Jogador 5 | 4-7 | 10:55:23 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_RecurveBow -> Ahri (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.1600 |  |
| Jogador 5 | 4-7 | 10:55:24 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Ahri (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.1100 |  |
| Jogador 5 | 4-7 | 10:55:24 | MOVE Board -> Board: Morgana (i:8.0) <-> Soraka (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 4-7 | 10:55:25 | MOVE Board -> Board: Soraka (i:8.0) <-> Rammus (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 4-7 | 10:55:26 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-1 | 10:55:31 | VENDEU: Teemo (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 10 | 0 | Defendente | DA_18_Rammus | 0.1200 |  |
| Jogador 5 | 5-1 | 10:55:32 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Defendente | DA_18_Rammus | 0.6100 |  |
| Jogador 5 | 5-1 | 10:55:33 | VENDEU: Akali (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Defendente | DA_18_Rammus | -0.0500 |  |
| Jogador 5 | 5-1 | 10:55:33 | COMPROU: Teemo (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Defendente | DA_18_Rammus | 0.1700 |  |
| Jogador 5 | 5-1 | 10:55:34 | MOVE Board -> Board: Rammus (i:6.0) <-> Rammus (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-1 | 10:55:35 | MOVE Board -> Board: Rammus (i:12.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 5-1 | 10:55:36 | MOVE Board -> Board: Rammus (i:12.0) <-> Morgana (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 5 | 5-1 | 10:55:36 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-2 | 10:55:41 | VENDEU: Teemo (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 14 | 0 | Defendente | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 5-2 | 10:55:42 | COMPROU: Shen (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Defendente | DA_18_Rammus | 0.2200 |  |
| Jogador 5 | 5-2 | 10:55:43 | VENDEU: Master Yi (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 15 | 0 | Defendente | DA_18_Rammus | 0.0600 |  |
| Jogador 5 | 5-2 | 10:55:43 | COMPROU: Zyra (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 11 | 0 | Defendente | DA_18_Rammus | -0.1100 |  |
| Jogador 5 | 5-2 | 10:55:44 | MOVE Board -> Board: Morgana (i:8.0) <-> Soraka (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 11 | 0 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-2 | 10:55:45 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Defendente | DA_18_Rammus | -0.2400 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-2 | 10:55:45 | VENDEU: Kog'Maw (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Defendente | DA_18_Rammus | -0.0600 |  |
| Jogador 5 | 5-2 | 10:55:46 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Defendente | DA_18_Rammus | -0.2900 |  |
| Jogador 5 | 5-2 | 10:55:47 | VENDEU: Kog'Maw (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 11 | 0 | Defendente | DA_18_Rammus | 0.1200 |  |
| Jogador 5 | 5-3 | 10:55:52 | COMPROU: Alune (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 14 | 1 | Defendente | DA_18_Rammus | 0.1800 |  |
| Jogador 5 | 5-3 | 10:55:52 | VENDEU: Aphelios (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 18 | 1 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 5 | 5-3 | 10:55:53 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 15 | 1 | Defendente | DA_18_Rammus | 0.6900 |  |
| Jogador 5 | 5-3 | 10:55:54 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Soraka (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 15 | 1 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 5-3 | 10:55:55 | MOVE Bench -> Board: Soraka (i:8.0) <-> Kha'Zix (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 15 | 1 | Defendente | DA_18_Rammus | -0.3900 |  |
| Jogador 5 | 5-3 | 10:55:55 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Azuporã (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 15 | 1 | Defendente | DA_18_Rammus | -0.5700 |  |
| Jogador 5 | 5-3 | 10:55:56 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 15 | 1 | Defendente | DA_18_Rammus | -0.0300 |  |
| Jogador 5 | 5-4 | 10:56:02 | VENDEU: Zyra (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 26 | 1 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 5-4 | 10:56:03 | COMPROU: Shen (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 24 | 1 | Defendente | DA_18_Rammus | 0.7600 |  |
| Jogador 5 | 5-4 | 10:56:04 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Soraka (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 24 | 1 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 5-4 | 10:56:04 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rammus (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 24 | 1 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 5-4 | 10:56:05 | REROLL | ECON | ECON: acumular até o limite de juros de 50 | 22 | 1 | Defendente | DA_18_Rammus | -0.1600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 5 | 5-4 | 10:56:06 | VENDEU: Kha'Zix (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 1 | Defendente | DA_18_Rammus | -0.1100 |  |
| Jogador 5 | 5-4 | 10:56:07 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 21 | 1 | Defendente | DA_18_Rammus | -0.2200 |  |
| Jogador 5 | 5-4 | 10:56:07 | MOVE Board -> Board: Rammus (i:6.0) <-> Ahri (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 21 | 1 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 5 | 5-5 | 10:56:14 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Defendente | DA_18_Rammus | 0.1600 |  |
| Jogador 5 | 5-5 | 10:56:18 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Defendente | DA_18_Rammus | 0.8100 |  |
| Jogador 5 | 5-5 | 10:56:19 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Defendente | DA_18_Rammus | -0.0300 |  |
| Jogador 5 | 5-5 | 10:56:19 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 2 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 5-6 | 10:56:23 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Defendente | DA_18_Rammus | 0.0600 |  |
| Jogador 5 | 5-6 | 10:56:24 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Defendente | DA_18_Rammus | 0.3300 |  |
| Jogador 5 | 5-6 | 10:56:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 5-6 | 10:56:26 | VENDEU: Morgana (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Defendente | DA_18_Rammus | -0.1300 |  |
| Jogador 5 | 5-6 | 10:56:26 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Defendente | DA_18_Rammus | 0.9200 |  |
| Jogador 5 | 5-6 | 10:56:27 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 28 | 2 | Defendente | DA_18_Rammus | -0.0200 |  |
| Jogador 5 | 5-7 | 10:56:34 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Rammus (i:6.0) (tabuleiro slot 2) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Defendente | DA_18_Rammus | 0.1300 |  |
| Jogador 5 | 5-7 | 10:56:35 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Defendente | DA_18_Rammus | 0.8500 |  |
| Jogador 5 | 5-7 | 10:56:35 | MOVE Bench -> Board: Lillia (i:8.0) <-> Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Defendente | DA_18_Rammus | -0.2900 |  |
| Jogador 5 | 5-7 | 10:56:36 | MOVE Bench -> Board: Ahri (i:8.0) <-> Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Defendente | DA_18_Rammus | 0.0700 |  |
| Jogador 5 | 5-7 | 10:56:37 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Defendente | DA_18_Rammus | -0.4200 |  |
| Jogador 5 | 5-7 | 10:56:37 | MOVE Bench -> Board: Lillia (i:8.0) <-> Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Defendente | DA_18_Rammus | -0.3000 |  |
| Jogador 5 | 5-7 | 10:56:38 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Defendente | DA_18_Rammus | -0.1500 |  |
| Jogador 5 | 6-1 | 10:56:48 | VENDEU: Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Defendente | DA_18_Rammus | -0.1400 |  |
| Jogador 5 | 6-1 | 10:56:48 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Defendente | DA_18_Rammus | 1.0000 |  |
| Jogador 5 | 6-1 | 10:56:49 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 40 | 3 | Defendente | DA_18_Rammus | 0.0400 |  |
| Jogador 5 | 6-1 | 10:56:49 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 40 | 3 | Defendente | DA_18_Rammus | 0.5300 |  |
| Jogador 5 | 6-1 | 10:56:50 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 3 | Defendente | DA_18_Rammus | 0.3000 |  |
| Jogador 5 | 6-1 | 10:56:51 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 5 | 6-1 | 10:56:52 | VENDEU: Rammus (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 3 | Defendente | DA_18_Rammus | -0.2300 |  |
| Jogador 5 | 6-1 | 10:56:52 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Lillia (i:8.0) (tabuleiro slot 17) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 3 | Defendente | DA_18_Rammus | 0.1200 |  |
| Jogador 5 | 6-1 | 10:56:53 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Defendente | DA_18_Rammus | 0.9200 |  |
| Jogador 6 | ? | 10:51:57 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | 0.0000 |  |
| Jogador 6 | ? | 10:51:58 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 6 | ? | 10:51:58 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 6 | ? | 10:51:59 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | ? | 10:52:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 1-1 | 10:52:04 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 6 | 1-1 | 10:52:05 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1400 |  |
| Jogador 6 | 1-1 | 10:52:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 6 | 1-1 | 10:52:06 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1400 |  |
| Jogador 6 | 1-1 | 10:52:07 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0400 |  |
| Jogador 6 | 1-1 | 10:52:07 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 6 | 1-1 | 10:52:08 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 6 | 1-1 | 10:52:09 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1400 |  |
| Jogador 6 | 1-1 | 10:52:09 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0800 |  |
| Jogador 6 | 1-2 | 10:52:11 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.0900 |  |
| Jogador 6 | 1-2 | 10:52:12 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Teemo | 0.0300 |  |
| Jogador 6 | 1-2 | 10:52:12 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 6 | 1-2 | 10:52:13 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Caitlyn | 0.0300 |  |
| Jogador 6 | 1-2 | 10:52:14 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 6 | 1-2 | 10:52:14 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 6 | 1-2 | 10:52:15 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.1400 |  |
| Jogador 6 | 1-2 | 10:52:16 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0100 |  |
| Jogador 6 | 1-2 | 10:52:17 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1500 |  |
| Jogador 6 | 1-3 | 10:52:18 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | 0.0900 |  |
| Jogador 6 | 1-3 | 10:52:19 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | 0.4100 |  |
| Jogador 6 | 1-3 | 10:52:19 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | 0.2100 |  |
| Jogador 6 | 1-3 | 10:52:20 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 1-3 | 10:52:21 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | 0.2100 |  |
| Jogador 6 | 1-3 | 10:52:21 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 1-3 | 10:52:22 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 6 | 1-3 | 10:52:23 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Murkwolf18 | 0.1600 |  |
| Jogador 6 | 1-3 | 10:52:24 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 6 | 1-4 | 10:52:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 6 | 1-4 | 10:52:26 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Murkwolf18 | -0.8900 |  |
| Jogador 6 | 1-4 | 10:52:26 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rammus | 0.1800 |  |
| Jogador 6 | 1-4 | 10:52:27 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rammus | 0.4500 |  |
| Jogador 6 | 1-4 | 10:52:28 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | 0.3200 |  |
| Jogador 6 | 1-4 | 10:52:28 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | -0.2800 |  |
| Jogador 6 | 1-4 | 10:52:29 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | -0.1000 |  |
| Jogador 6 | 1-4 | 10:52:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-1 | 10:52:33 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 2-1 | 10:52:33 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-1 | 10:52:34 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Rammus | -0.2400 |  |
| Jogador 6 | 2-1 | 10:52:35 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | 0.1900 |  |
| Jogador 6 | 2-1 | 10:52:36 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | 0.1700 |  |
| Jogador 6 | 2-1 | 10:52:36 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NeedlesslyLargeRod -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | 0.0900 |  |
| Jogador 6 | 2-1 | 10:52:37 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-1 | 10:52:38 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | -0.0200 |  |
| Jogador 6 | 2-1 | 10:52:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-2 | 10:52:40 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Rammus | -0.3400 |  |
| Jogador 6 | 2-2 | 10:52:41 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 1.0400 |  |
| Jogador 6 | 2-2 | 10:52:42 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 0.0700 |  |
| Jogador 6 | 2-2 | 10:52:43 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Rammus | -0.1300 |  |
| Jogador 6 | 2-2 | 10:52:43 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 0.3200 |  |
| Jogador 6 | 2-2 | 10:52:44 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Rammus | -0.1300 |  |
| Jogador 6 | 2-2 | 10:52:45 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Rammus | 0.3200 |  |
| Jogador 6 | 2-2 | 10:52:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rammus | -0.1200 |  |
| Jogador 6 | 2-2 | 10:52:46 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Rammus | 0.0500 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-3 | 10:52:48 | VENDEU: Teemo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 0 | — | DA_18_Rammus | -0.1300 |  |
| Jogador 6 | 2-3 | 10:52:49 | COMPROU: Hecarim (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_18_Rammus | 0.0500 |  |
| Jogador 6 | 2-3 | 10:52:50 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_18_Hecarim | 0.4100 |  |
| Jogador 6 | 2-3 | 10:52:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | — | DA_18_Hecarim | 0.2300 |  |
| Jogador 6 | 2-3 | 10:52:51 | VENDEU: Rakan (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_18_Hecarim | -0.0200 |  |
| Jogador 6 | 2-3 | 10:52:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | — | DA_18_Hecarim | 0.2300 |  |
| Jogador 6 | 2-3 | 10:52:52 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Hecarim | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-3 | 10:52:53 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Hecarim | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-3 | 10:52:54 | VENDEU: Rakan (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_18_Hecarim | -0.0400 |  |
| Jogador 6 | 2-4 | 10:52:56 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_18_Hecarim | 0.2000 |  |
| Jogador 6 | 2-4 | 10:52:57 | VENDEU: Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Colosso | DA_18_Hecarim | -0.3300 |  |
| Jogador 6 | 2-4 | 10:52:57 | COMPROU: Yorick (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | Colosso | DA_18_Hecarim | 0.3200 |  |
| Jogador 6 | 2-4 | 10:52:58 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | Colosso | DA_18_Hecarim | -0.1600 |  |
| Jogador 6 | 2-4 | 10:52:59 | COMPROU: Kayle (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_18_Hecarim | 0.2400 |  |
| Jogador 6 | 2-4 | 10:52:59 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_18_Hecarim | -0.0800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-4 | 10:53:00 | VENDEU: Kayle (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | Colosso | DA_18_Hecarim | -0.0900 |  |
| Jogador 6 | 2-4 | 10:53:01 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Colosso | DA_18_Hecarim | 0.0100 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-4 | 10:53:02 | MOVE Board -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Colosso | DA_18_Hecarim | 0.0000 |  |
| Jogador 6 | 2-5 | 10:53:04 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Colosso | DA_18_Rammus | 0.9600 |  |
| Jogador 6 | 2-5 | 10:53:04 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_Rammus | -0.0500 |  |
| Jogador 6 | 2-5 | 10:53:05 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vivaz | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 6 | 2-5 | 10:53:06 | MOVE Board -> Board: Rammus (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Vivaz | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-5 | 10:53:06 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_Rammus | -0.1300 |  |
| Jogador 6 | 2-5 | 10:53:07 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vivaz | DA_18_Rammus | 0.0700 |  |
| Jogador 6 | 2-5 | 10:53:08 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-5 | 10:53:09 | MOVE Board -> Board: Rammus (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vivaz | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 2-5 | 10:53:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-6 | 10:53:11 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vivaz | DA_18_Rammus | -0.2300 |  |
| Jogador 6 | 2-6 | 10:53:12 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 6 | 2-6 | 10:53:13 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vivaz | DA_18_Rammus | -0.0500 |  |
| Jogador 6 | 2-6 | 10:53:14 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 2-6 | 10:53:14 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-6 | 10:53:15 | MOVE Bench -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-6 | 10:53:16 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_Rammus | -0.4000 |  |
| Jogador 6 | 2-6 | 10:53:16 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vivaz | DA_18_Rammus | 0.3300 |  |
| Jogador 6 | 2-6 | 10:53:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Vivaz | DA_18_Rammus | -0.0400 |  |
| Jogador 6 | 2-7 | 10:53:19 | VENDEU: Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Vivaz | DA_18_Rammus | -0.3600 |  |
| Jogador 6 | 2-7 | 10:53:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vivaz | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 6 | 2-7 | 10:53:21 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Vivaz | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 6 | 2-7 | 10:53:21 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Vivaz | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 6 | 2-7 | 10:53:22 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Ahri | -0.1700 |  |
| Jogador 6 | 2-7 | 10:53:23 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_BFSword -> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Ahri | 0.2200 |  |
| Jogador 6 | 2-7 | 10:53:23 | MOVE Bench -> Board: Ahri (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Ahri | -0.7600 |  |
| Jogador 6 | 2-7 | 10:53:24 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Ahri | -0.3900 |  |
| Jogador 6 | 2-7 | 10:53:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Ahri | 0.0000 |  |
| Jogador 6 | 3-1 | 10:53:27 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Vivaz | DA_18_Ahri | -0.8000 |  |
| Jogador 6 | 3-1 | 10:53:28 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Fiddlesticks (i:6.0) (tabuleiro slot 2) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Vivaz | DA_18_Ahri | 0.1300 |  |
| Jogador 6 | 3-1 | 10:53:28 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Vivaz | DA_18_Ahri | 0.2100 |  |
| Jogador 6 | 3-1 | 10:53:29 | MOVE Bench -> Board: Alistar (i:4.0) <-> Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Vivaz | DA_18_Ahri | 0.0700 |  |
| Jogador 6 | 3-1 | 10:53:30 | VENDEU: Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Vivaz | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 6 | 3-1 | 10:53:30 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Vivaz | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 6 | 3-1 | 10:53:31 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Vivaz | DA_Fiddlesticks18 | -0.7000 |  |
| Jogador 6 | 3-1 | 10:53:32 | MOVE Bench -> Board: Alistar (i:4.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Vivaz | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 6 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vivaz | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-2 | 10:53:35 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Vivaz | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 6 | 3-2 | 10:53:35 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Master Yi (i:6.0) (tabuleiro slot 4) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Vivaz | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 6 | 3-2 | 10:53:36 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Fiddlesticks (i:6.0) (tabuleiro slot 2) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Vivaz | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 6 | 3-2 | 10:53:37 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Vivaz | DA_Fiddlesticks18 | 0.6600 |  |
| Jogador 6 | 3-2 | 10:53:37 | MOVE Bench -> Board: Rammus (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Vivaz | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 6 | 3-2 | 10:53:38 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Vivaz | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 6 | 3-2 | 10:53:39 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Hecarim (i:6.0) (tabuleiro slot 22) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Vivaz | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 6 | 3-2 | 10:53:40 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Vivaz | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 6 | 3-2 | 10:53:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Vivaz | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-3 | 10:53:43 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Vivaz | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 6 | 3-3 | 10:53:44 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Vivaz | DA_18_Lillia | -0.0400 |  |
| Jogador 6 | 3-3 | 10:53:44 | MOVE Bench -> Board: Lillia (i:8.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Vivaz | DA_18_Lillia | -0.4000 |  |
| Jogador 6 | 3-3 | 10:53:45 | MOVE Bench -> Board: Rammus (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Vivaz | DA_18_Lillia | 0.0800 |  |
| Jogador 6 | 3-3 | 10:53:46 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Vivaz | DA_18_Lillia | -0.0500 |  |
| Jogador 6 | 3-3 | 10:53:47 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Vivaz | DA_18_Lillia | -0.0600 |  |
| Jogador 6 | 3-3 | 10:53:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Vivaz | DA_18_Lillia | -0.0100 |  |
| Jogador 6 | 3-3 | 10:53:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Vivaz | DA_18_Lillia | -0.0100 |  |
| Jogador 6 | 3-3 | 10:53:49 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 1 | Vivaz | DA_18_Lillia | -0.0200 |  |
| Jogador 6 | 3-4 | 10:53:51 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vivaz | DA_18_Lillia | 0.4100 |  |
| Jogador 6 | 3-4 | 10:53:52 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_Lillia | -0.1800 |  |
| Jogador 6 | 3-4 | 10:53:53 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vivaz | DA_18_Lillia | -0.2300 |  |
| Jogador 6 | 3-4 | 10:53:54 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_Lillia | -0.1800 |  |
| Jogador 6 | 3-4 | 10:53:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vivaz | DA_18_Lillia | -0.0100 |  |
| Jogador 6 | 3-4 | 10:53:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vivaz | DA_18_Lillia | -0.0100 |  |
| Jogador 6 | 3-4 | 10:53:56 | MOVE Board -> Board: Diana (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vivaz | DA_18_Lillia | 0.0000 |  |
| Jogador 6 | 3-4 | 10:53:56 | MOVE Board -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vivaz | DA_18_Lillia | -0.0100 |  |
| Jogador 6 | 3-4 | 10:53:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Vivaz | DA_18_Lillia | 0.0000 |  |
| Jogador 6 | 3-5 | 10:54:00 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vivaz | DA_18_Lillia | -0.2300 |  |
| Jogador 6 | 3-5 | 10:54:01 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Lillia | 0.6500 |  |
| Jogador 6 | 3-5 | 10:54:01 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vivaz | DA_18_Lillia | -0.2500 |  |
| Jogador 6 | 3-5 | 10:54:02 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_Lillia | 0.6500 |  |
| Jogador 6 | 3-5 | 10:54:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_Lillia | -0.0100 |  |
| Jogador 6 | 3-5 | 10:54:03 | MOVE Board -> Board: Rammus (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_Lillia | 0.0000 |  |
| Jogador 6 | 3-5 | 10:54:04 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_Lillia | -0.0100 |  |
| Jogador 6 | 3-5 | 10:54:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_Lillia | 0.0000 |  |
| Jogador 6 | 3-6 | 10:54:08 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vivaz | DA_18_Lillia | -0.2500 |  |
| Jogador 6 | 3-6 | 10:54:09 | COMPROU: Gnar (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_GnarSmall | 0.1300 |  |
| Jogador 6 | 3-6 | 10:54:10 | MOVE Bench -> Board: Gnar (i:10.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Vivaz | DA_18_GnarSmall | 0.0900 |  |
| Jogador 6 | 3-6 | 10:54:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-6 | 10:54:11 | MOVE Board -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-6 | 10:54:12 | MOVE Board -> Board: Diana (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-6 | 10:54:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 10:54:17 | VENDEU: Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Vivaz | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 3-7 | 10:54:18 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_GnarSmall | 0.6800 |  |
| Jogador 6 | 3-7 | 10:54:18 | MOVE Bench -> Board: Rammus (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_Rammus | 0.3500 |  |
| Jogador 6 | 3-7 | 10:54:19 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_Rammus | 0.5300 |  |
| Jogador 6 | 3-7 | 10:54:20 | MOVE Board -> Board: Rammus (i:12.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 10:54:20 | MOVE Board -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-7 | 10:54:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 10:54:22 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_GnarSmall | -0.1000 |  |
| Jogador 6 | 4-1 | 10:54:26 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_GnarSmall | -0.1000 |  |
| Jogador 6 | 4-1 | 10:54:27 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-1 | 10:54:27 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_GnarSmall | 0.1700 |  |
| Jogador 6 | 4-1 | 10:54:28 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_NeedlesslyLargeRod -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_GnarSmall | 0.1300 |  |
| Jogador 6 | 4-1 | 10:54:29 | MOVE Board -> Board: Gnar (i:10.0) <-> Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-1 | 10:54:29 | MOVE Board -> Board: Rammus (i:12.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 4-1 | 10:54:30 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-2 | 10:54:35 | COMPROU: Kobuko (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Vivaz | DA_18_Rammus | 0.7800 |  |
| Jogador 6 | 4-2 | 10:54:36 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Vivaz | DA_18_Rammus | -0.2200 |  |
| Jogador 6 | 4-2 | 10:54:36 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Vivaz | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-2 | 10:54:37 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 1 | Vivaz | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 4-2 | 10:54:38 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Vivaz | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 4-2 | 10:54:39 | MOVE Board -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-2 | 10:54:39 | MOVE Board -> Board: Diana (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Vivaz | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 4-2 | 10:54:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-3 | 10:54:44 | VENDEU: Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Vivaz | DA_18_Rammus | -0.3500 |  |
| Jogador 6 | 4-3 | 10:54:45 | VENDEU: Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Vivaz | DA_18_Rammus | 0.0900 |  |
| Jogador 6 | 4-3 | 10:54:46 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Vivaz | DA_18_Rammus | -0.0800 |  |
| Jogador 6 | 4-3 | 10:54:46 | COMPROU: Kobuko (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Vivaz | DA_18_Rammus | 0.7800 |  |
| Jogador 6 | 4-3 | 10:54:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Vivaz | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-3 | 10:54:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Vivaz | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 4-3 | 10:54:48 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Vivaz | DA_18_Rammus | 0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 6 | 4-3 | 10:54:49 | VENDEU: Kobuko (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Vivaz | DA_18_Rammus | -0.3500 |  |
| Jogador 6 | 4-3 | 10:54:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Vivaz | DA_18_Rammus | 0.1500 |  |
| Jogador 6 | 4-4 | 10:54:53 | VENDEU: Rakan (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Vivaz | DA_18_Rammus | -0.0500 |  |
| Jogador 6 | 4-4 | 10:54:54 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Vivaz | DA_18_Rammus | -0.1000 |  |
| Jogador 6 | 4-4 | 10:54:55 | VENDEU: Cassiopeia (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Vivaz | DA_18_Rammus | -0.3000 |  |
| Jogador 6 | 4-4 | 10:54:56 | COMPROU: Teemo (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Vivaz | DA_18_Rammus | 0.2000 |  |
| Jogador 6 | 4-4 | 10:54:56 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Vivaz | DA_18_Rammus | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 6 | 4-4 | 10:54:57 | MOVE Board -> Board: Hecarim (i:6.0) <-> Gnar (i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-4 | 10:54:58 | MOVE Board -> Board: Gnar (i:10.0) <-> Rammus (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Vivaz | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-4 | 10:54:58 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 10:54:59 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Vivaz | DA_18_GnarSmall | 0.4200 |  |
| Jogador 6 | 4-5 | 10:55:03 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Vivaz | DA_18_GnarSmall | 0.7100 |  |
| Jogador 6 | 4-5 | 10:55:03 | COMPROU: Lillia (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Vivaz | DA_18_GnarSmall | 0.1700 |  |
| Jogador 6 | 4-5 | 10:55:04 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-5 | 10:55:05 | MOVE Board -> Board: Hecarim (i:6.0) <-> Gnar (i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Vivaz | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-5 | 10:55:05 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-6 | 10:55:12 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_GnarSmall | 0.0200 |  |
| Jogador 6 | 4-6 | 10:55:13 | MOVE Board -> Board: Gnar (i:10.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-6 | 10:55:14 | MOVE Board -> Board: Diana (i:6.0) <-> Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 4-6 | 10:55:14 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-7 | 10:55:22 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Vivaz | DA_18_Diana | 0.8900 |  |
| Jogador 6 | 4-7 | 10:55:22 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | -0.2800 |  |
| Jogador 6 | 4-7 | 10:55:23 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_ChainVest -> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | 0.1200 |  |
| Jogador 6 | 4-7 | 10:55:24 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NeedlesslyLargeRod -> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | 0.0600 |  |
| Jogador 6 | 4-7 | 10:55:24 | MOVE Board -> Board: Rammus (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | 0.0000 |  |
| Jogador 6 | 4-7 | 10:55:25 | MOVE Board -> Board: Rammus (i:12.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | -0.0100 |  |
| Jogador 6 | 4-7 | 10:55:26 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | 0.0000 |  |
| Jogador 6 | 4-7 | 10:55:27 | MOVE Bench -> Board: Kayle (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | 0.4000 |  |
| Jogador 6 | 5-1 | 10:55:31 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Vivaz | DA_18_Diana | 0.3200 |  |
| Jogador 6 | 5-1 | 10:55:32 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | 0.3200 |  |
| Jogador 6 | 5-1 | 10:55:33 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | 0.0000 |  |
| Jogador 6 | 5-1 | 10:55:33 | MOVE Board -> Board: Hecarim (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | -0.0100 |  |
| Jogador 6 | 5-1 | 10:55:34 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Vivaz | DA_18_Diana | 0.0000 |  |
| Jogador 6 | 5-2 | 10:55:41 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Vivaz | DA_18_Diana | 0.1300 |  |
| Jogador 6 | 5-2 | 10:55:42 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vivaz | DA_18_Diana | 0.0400 |  |
| Jogador 6 | 5-2 | 10:55:43 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vivaz | DA_18_Diana | 0.0000 |  |
| Jogador 6 | 5-2 | 10:55:43 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rammus (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vivaz | DA_18_Diana | -0.0100 |  |
| Jogador 6 | 5-2 | 10:55:44 | MOVE Board -> Board: Rammus (i:12.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vivaz | DA_18_Diana | -0.0100 |  |
| Jogador 6 | 5-2 | 10:55:45 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Vivaz | DA_18_Diana | -0.0500 |  |
| Jogador 7 | ? | 10:51:57 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 7 | ? | 10:51:58 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 7 | ? | 10:51:58 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 7 | ? | 10:51:59 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 7 | ? | 10:52:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-1 | 10:52:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0800 |  |
| Jogador 7 | 1-1 | 10:52:05 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.0900 |  |
| Jogador 7 | 1-1 | 10:52:05 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 7 | 1-1 | 10:52:06 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 7 | 1-1 | 10:52:07 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 7 | 1-1 | 10:52:07 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4100 |  |
| Jogador 7 | 1-1 | 10:52:08 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0200 |  |
| Jogador 7 | 1-1 | 10:52:09 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 7 | 1-1 | 10:52:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-2 | 10:52:11 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.2600 |  |
| Jogador 7 | 1-2 | 10:52:12 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 7 | 1-2 | 10:52:12 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.2600 |  |
| Jogador 7 | 1-2 | 10:52:13 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | -0.2700 |  |
| Jogador 7 | 1-2 | 10:52:14 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 7 | 1-2 | 10:52:14 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.2900 |  |
| Jogador 7 | 1-2 | 10:52:15 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 1-2 | 10:52:16 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | -0.4200 |  |
| Jogador 7 | 1-2 | 10:52:17 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.2400 |  |
| Jogador 7 | 1-3 | 10:52:18 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 7 | 1-3 | 10:52:19 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Scuttlecrab18 | 0.2500 |  |
| Jogador 7 | 1-3 | 10:52:19 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.1200 |  |
| Jogador 7 | 1-3 | 10:52:20 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.2800 |  |
| Jogador 7 | 1-3 | 10:52:21 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.1300 |  |
| Jogador 7 | 1-3 | 10:52:21 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.2800 |  |
| Jogador 7 | 1-3 | 10:52:22 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.1300 |  |
| Jogador 7 | 1-3 | 10:52:23 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.1500 |  |
| Jogador 7 | 1-3 | 10:52:24 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 1-4 | 10:52:25 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | 0.2400 |  |
| Jogador 7 | 1-4 | 10:52:26 | MOVE Bench -> Board: Alistar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | 0.4500 |  |
| Jogador 7 | 1-4 | 10:52:26 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.1900 |  |
| Jogador 7 | 1-4 | 10:52:27 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 7 | 1-4 | 10:52:28 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.1900 |  |
| Jogador 7 | 1-4 | 10:52:28 | MOVE Bench -> Board: Shen (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.3500 |  |
| Jogador 7 | 1-4 | 10:52:29 | MOVE Bench -> Board: Alistar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | -0.0700 |  |
| Jogador 7 | 1-4 | 10:52:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 2-1 | 10:52:33 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 7 | 2-1 | 10:52:33 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Hecarim | 0.1600 |  |
| Jogador 7 | 2-1 | 10:52:34 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Hecarim | -0.3400 |  |
| Jogador 7 | 2-1 | 10:52:35 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Hecarim | 0.0700 |  |
| Jogador 7 | 2-1 | 10:52:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Hecarim | 0.9200 |  |
| Jogador 7 | 2-1 | 10:52:36 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_ChainVest -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Hecarim | 0.1500 |  |
| Jogador 7 | 2-1 | 10:52:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-1 | 10:52:38 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Hecarim | -0.3700 |  |
| Jogador 7 | 2-1 | 10:52:38 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Hecarim (i:6.0) (tabuleiro slot 4) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Hecarim | 0.1200 |  |
| Jogador 7 | 2-2 | 10:52:40 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Hecarim (i:6.0) (tabuleiro slot 4) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 10:52:41 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_Hecarim | 1.0400 |  |
| Jogador 7 | 2-2 | 10:52:42 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Hecarim | -0.7100 |  |
| Jogador 7 | 2-2 | 10:52:43 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | — | DA_18_Hecarim | 1.0100 |  |
| Jogador 7 | 2-2 | 10:52:43 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Hecarim | -0.4500 |  |
| Jogador 7 | 2-2 | 10:52:44 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | — | DA_18_Hecarim | 0.1200 |  |
| Jogador 7 | 2-2 | 10:52:45 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Hecarim | -0.3800 |  |
| Jogador 7 | 2-2 | 10:52:45 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-2 | 10:52:46 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_18_Hecarim | -0.3100 |  |
| Jogador 7 | 2-3 | 10:52:48 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | — | DA_18_Hecarim | 1.0300 |  |
| Jogador 7 | 2-3 | 10:52:49 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | — | DA_18_Hecarim | -0.7000 |  |
| Jogador 7 | 2-3 | 10:52:50 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | — | DA_Fiddlesticks18 | 0.3300 |  |
| Jogador 7 | 2-3 | 10:52:50 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | — | DA_Fiddlesticks18 | -0.3500 |  |
| Jogador 7 | 2-3 | 10:52:51 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | — | DA_Fiddlesticks18 | -0.3300 |  |
| Jogador 7 | 2-3 | 10:52:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | — | DA_Fiddlesticks18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-4 | 10:52:56 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Lutador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 2-4 | 10:52:57 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Lutador | DA_Fiddlesticks18 | 0.3900 |  |
| Jogador 7 | 2-4 | 10:52:57 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Lutador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 2-4 | 10:52:58 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Lutador | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 7 | 2-4 | 10:52:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Lutador | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 7 | 2-4 | 10:52:59 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Lutador | DA_Fiddlesticks18 | 0.4100 |  |
| Jogador 7 | 2-4 | 10:53:00 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Lutador | DA_Fiddlesticks18 | 0.3200 |  |
| Jogador 7 | 2-4 | 10:53:01 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Lutador | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 7 | 2-4 | 10:53:02 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Lutador | DA_Fiddlesticks18 | 0.2500 |  |
| Jogador 7 | 2-5 | 10:53:04 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Lutador | DA_Fiddlesticks18 | -0.3400 |  |
| Jogador 7 | 2-5 | 10:53:04 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Lutador | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 7 | 2-5 | 10:53:05 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Lutador | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 7 | 2-5 | 10:53:06 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Lutador | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 7 | 2-5 | 10:53:06 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Lutador | DA_Fiddlesticks18 | -0.3200 |  |
| Jogador 7 | 2-5 | 10:53:07 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Lutador | DA_Fiddlesticks18 | 0.3500 |  |
| Jogador 7 | 2-5 | 10:53:08 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Lutador | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 7 | 2-5 | 10:53:09 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Lutador | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 7 | 2-5 | 10:53:09 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Lutador | DA_Fiddlesticks18 | -0.2800 |  |
| Jogador 7 | 2-6 | 10:53:11 | COMPROU: Warwick (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 41 | 3 | Lutador | DA_Fiddlesticks18 | 1.0200 |  |
| Jogador 7 | 2-6 | 10:53:12 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Lutador | DA_Fiddlesticks18 | -0.3600 |  |
| Jogador 7 | 2-6 | 10:53:13 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Lutador | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 7 | 2-6 | 10:53:14 | MOVE Bench -> Board: Rammus (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Lutador | DA_Fiddlesticks18 | -0.7700 |  |
| Jogador 7 | 2-6 | 10:53:14 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Lutador | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 7 | 2-6 | 10:53:15 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Lutador | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 7 | 2-6 | 10:53:16 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Lutador | DA_Fiddlesticks18 | 0.3900 |  |
| Jogador 7 | 2-6 | 10:53:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Lutador | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 7 | 2-6 | 10:53:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Lutador | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 7 | 2-7 | 10:53:19 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NeedlesslyLargeRod -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Lutador | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 7 | 2-7 | 10:53:20 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Lutador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 2-7 | 10:53:21 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Lutador | DA_Fiddlesticks18 | 0.2600 |  |
| Jogador 7 | 2-7 | 10:53:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Lutador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 2-7 | 10:53:22 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Lutador | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 7 | 2-7 | 10:53:23 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Lutador | DA_Fiddlesticks18 | 0.1700 |  |
| Jogador 7 | 2-7 | 10:53:23 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Lutador | DA_Fiddlesticks18 | -0.3400 |  |
| Jogador 7 | 2-7 | 10:53:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Lutador | DA_Fiddlesticks18 | -0.2700 |  |
| Jogador 7 | 2-7 | 10:53:25 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Lutador | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 7 | 3-1 | 10:53:27 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Lutador | DA_Fiddlesticks18 | -0.1900 |  |
| Jogador 7 | 3-1 | 10:53:28 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Lutador | DA_Fiddlesticks18 | -0.3700 |  |
| Jogador 7 | 3-1 | 10:53:28 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Lutador | DA_Fiddlesticks18 | -0.2100 |  |
| Jogador 7 | 3-1 | 10:53:29 | MOVE Board -> Board: Rammus (i:6.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Lutador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-1 | 10:53:30 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Lutador | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-1 | 10:53:30 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Lutador | DA_Fiddlesticks18 | -0.2900 |  |
| Jogador 7 | 3-1 | 10:53:31 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Lutador | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 7 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Lutador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Lutador | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 7 | 3-2 | 10:53:35 | VENDEU: Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Lutador | DA_Fiddlesticks18 | -0.3400 |  |
| Jogador 7 | 3-2 | 10:53:35 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Lutador | DA_Fiddlesticks18 | 0.7900 |  |
| Jogador 7 | 3-2 | 10:53:36 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Lutador | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 7 | 3-2 | 10:53:37 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Lutador | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 3-2 | 10:53:37 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Lutador | DA_Fiddlesticks18 | -0.3800 |  |
| Jogador 7 | 3-2 | 10:53:38 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Lutador | DA_Fiddlesticks18 | 0.8000 |  |
| Jogador 7 | 3-2 | 10:53:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Lutador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 3-2 | 10:53:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Lutador | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 7 | 3-2 | 10:53:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Lutador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 3-3 | 10:53:43 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Lutador | DA_Fiddlesticks18 | -0.8100 |  |
| Jogador 7 | 3-3 | 10:53:44 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Lutador | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 3-3 | 10:53:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Lutador | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 7 | 3-3 | 10:53:45 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 3 | Lutador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 3-3 | 10:53:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 3 | Lutador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-3 | 10:53:47 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 3 | Lutador | DA_Fiddlesticks18 | 0.4500 |  |
| Jogador 7 | 3-3 | 10:53:47 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 3 | Lutador | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 7 | 3-3 | 10:53:48 | MOVE Board -> Board: Diana (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 3 | Lutador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-3 | 10:53:49 | MOVE Board -> Board: Rammus (i:6.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 3 | Lutador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-4 | 10:53:51 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Lutador | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 7 | 3-4 | 10:53:52 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Lutador | DA_Fiddlesticks18 | 0.7700 |  |
| Jogador 7 | 3-4 | 10:53:53 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lutador | DA_Fiddlesticks18 | 0.2500 |  |
| Jogador 7 | 3-4 | 10:53:54 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lutador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-4 | 10:53:54 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lutador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-4 | 10:53:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lutador | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 7 | 3-5 | 10:54:00 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 3 | Lutador | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 3-5 | 10:54:01 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 3 | Lutador | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 3-5 | 10:54:01 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 3 | Lutador | DA_Sentinel18 | 0.5100 |  |
| Jogador 7 | 3-5 | 10:54:02 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 3 | Lutador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-5 | 10:54:03 | MOVE Board -> Board: Diana (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 3 | Lutador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-5 | 10:54:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 3 | Lutador | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 3-6 | 10:54:08 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Lutador | DA_Sentinel18 | 0.7100 |  |
| Jogador 7 | 3-6 | 10:54:09 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Lutador | DA_Sentinel18 | -0.2400 |  |
| Jogador 7 | 3-6 | 10:54:10 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Lutador | DA_Sentinel18 | -0.2400 |  |
| Jogador 7 | 3-6 | 10:54:10 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Lutador | DA_Sentinel18 | -0.2400 |  |
| Jogador 7 | 3-6 | 10:54:11 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Lutador | DA_Sentinel18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 7 | 3-6 | 10:54:12 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Lutador | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 3-6 | 10:54:13 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 2 | Lutador | DA_Sentinel18 | 0.1800 |  |
| Jogador 7 | 3-6 | 10:54:13 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 2 | Lutador | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 3-6 | 10:54:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Lutador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-7 | 10:54:17 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Lutador | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 3-7 | 10:54:18 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lutador | DA_Sentinel18 | 0.2400 |  |
| Jogador 7 | 3-7 | 10:54:18 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_ChainVest -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lutador | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 3-7 | 10:54:19 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_RecurveBow -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lutador | DA_Sentinel18 | 0.1100 |  |
| Jogador 7 | 3-7 | 10:54:20 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Lutador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-7 | 10:54:20 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Lutador | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 3-7 | 10:54:21 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Lutador | DA_Sentinel18 | 0.4800 |  |
| Jogador 7 | 3-7 | 10:54:22 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Lutador | DA_Sentinel18 | -0.2400 | FAST8_REROLL_REVIEW |
| Jogador 7 | 3-7 | 10:54:22 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Lutador | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 4-1 | 10:54:26 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Lutador | DA_Fiddlesticks18 | 0.7700 |  |
| Jogador 7 | 4-1 | 10:54:27 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Lutador | DA_Fiddlesticks18 | 0.3500 |  |
| Jogador 7 | 4-1 | 10:54:27 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 3 | Lutador | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 7 | 4-1 | 10:54:28 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 3 | Lutador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 4-1 | 10:54:29 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 3 | Lutador | DA_Fiddlesticks18 | 0.3900 |  |
| Jogador 7 | 4-1 | 10:54:29 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 3 | Lutador | DA_Fiddlesticks18 | 0.4800 |  |
| Jogador 7 | 4-1 | 10:54:30 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 3 | Lutador | DA_Fiddlesticks18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 7 | 4-1 | 10:54:31 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 3 | Lutador | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 7 | 4-1 | 10:54:32 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 3 | Lutador | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 7 | 4-2 | 10:54:35 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Lutador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 4-2 | 10:54:36 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Lutador | DA_Fiddlesticks18 | 0.7600 |  |
| Jogador 7 | 4-2 | 10:54:36 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Lutador | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 7 | 4-2 | 10:54:37 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Lutador | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 7 | 4-2 | 10:54:38 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Lutador | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 7 | 4-2 | 10:54:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Lutador | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 7 | 4-2 | 10:54:39 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Lutador | DA_Fiddlesticks18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 7 | 4-2 | 10:54:40 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Lutador | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 4-2 | 10:54:41 | COMPROU: Sett (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Lutador | DA_Fiddlesticks18 | 0.2400 |  |
| Jogador 7 | 4-3 | 10:54:44 | VENDEU: Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Lutador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 4-3 | 10:54:45 | COMPROU: Ashe (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Lutador | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 7 | 4-3 | 10:54:46 | VENDEU: Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Lutador | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 7 | 4-3 | 10:54:46 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Lutador | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-3 | 10:54:47 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Lutador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 4-3 | 10:54:48 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Lutador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 4-3 | 10:54:48 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Lutador | DA_Fiddlesticks18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 7 | 4-3 | 10:54:49 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Lutador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 4-3 | 10:54:50 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Lutador | DA_Fiddlesticks18 | 0.2000 |  |
| Jogador 7 | 4-4 | 10:54:53 | VENDEU: Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Lutador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 4-4 | 10:54:54 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 4 | Lutador | DA_Fiddlesticks18 | 0.2000 |  |
| Jogador 7 | 4-4 | 10:54:55 | VENDEU: Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Lutador | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 7 | 4-4 | 10:54:56 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Lutador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 4-4 | 10:54:56 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Lutador | DA_Fiddlesticks18 | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 7 | 4-4 | 10:54:57 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Lutador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 4-4 | 10:54:58 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Lutador | DA_Fiddlesticks18 | 0.1700 |  |
| Jogador 7 | 4-4 | 10:54:58 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Lutador | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 7 | 4-4 | 10:54:59 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Lutador | DA_Fiddlesticks18 | 0.4800 |  |
| Jogador 7 | 4-5 | 10:55:03 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Lutador | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 7 | 4-5 | 10:55:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Lutador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 4-5 | 10:55:04 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Lutador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 4-5 | 10:55:05 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Lutador | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 7 | 4-5 | 10:55:05 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Lutador | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 4-5 | 10:55:06 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Lutador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 4-5 | 10:55:07 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 5 | Lutador | DA_Fiddlesticks18 | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 7 | 4-5 | 10:55:07 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Lutador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 4-5 | 10:55:08 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 5 | Lutador | DA_Fiddlesticks18 | 0.3000 |  |
| Jogador 7 | 4-6 | 10:55:12 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Lutador | DA_Fiddlesticks18 | -0.2900 |  |
| Jogador 7 | 4-6 | 10:55:13 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Lutador | DA_Fiddlesticks18 | 0.7800 |  |
| Jogador 7 | 4-6 | 10:55:14 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Lutador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 4-6 | 10:55:14 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Lutador | DA_Fiddlesticks18 | 0.3600 |  |
| Jogador 7 | 4-6 | 10:55:15 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Lutador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 4-6 | 10:55:16 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Lutador | DA_Fiddlesticks18 | 0.4100 |  |
| Jogador 7 | 4-6 | 10:55:17 | REROLL | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Lutador | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-6 | 10:55:17 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Lutador | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 7 | 4-6 | 10:55:18 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Lutador | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 7 | 4-7 | 10:55:22 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Lutador | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 4-7 | 10:55:22 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Lutador | DA_Fiddlesticks18 | 1.0200 |  |
| Jogador 7 | 4-7 | 10:55:23 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Lutador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 4-7 | 10:55:24 | MOVE Bench -> Board: Ashe (i:10.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Lutador | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 7 | 4-7 | 10:55:24 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Lutador | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 7 | 4-7 | 10:55:25 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_RecurveBow -> Ashe (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Lutador | DA_Fiddlesticks18 | 0.1700 |  |
| Jogador 7 | 4-7 | 10:55:26 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Ashe (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Lutador | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 7 | 4-7 | 10:55:26 | REROLL | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Lutador | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-7 | 10:55:27 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Lutador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 5-1 | 10:55:31 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Lutador | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 7 | 5-1 | 10:55:32 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Lutador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 5-1 | 10:55:33 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Lutador | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 7 | 5-1 | 10:55:33 | REROLL | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Lutador | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 5-1 | 10:55:34 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Lutador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 5-1 | 10:55:35 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Lutador | DA_Fiddlesticks18 | 0.8800 |  |
| Jogador 7 | 5-1 | 10:55:36 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Lutador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 5-1 | 10:55:36 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Lutador | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 7 | 5-1 | 10:55:37 | REROLL | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Lutador | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 5-2 | 10:55:41 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Lutador | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 5-2 | 10:55:42 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Lutador | DA_Fiddlesticks18 | 0.7800 |  |
| Jogador 7 | 5-2 | 10:55:43 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Lutador | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 5-2 | 10:55:43 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Lutador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 5-2 | 10:55:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Lutador | DA_Fiddlesticks18 | 0.9200 |  |
| Jogador 7 | 5-2 | 10:55:45 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Lutador | DA_Fiddlesticks18 | -0.3300 |  |
| Jogador 7 | 5-2 | 10:55:45 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Lutador | DA_Fiddlesticks18 | 0.5800 |  |
| Jogador 7 | 5-2 | 10:55:46 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Lutador | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 5-2 | 10:55:47 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Lutador | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 8 | ? | 10:51:57 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 8 | ? | 10:51:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 8 | ? | 10:51:58 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6100 |  |
| Jogador 8 | ? | 10:51:59 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 8 | ? | 10:52:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 8 | 1-1 | 10:52:04 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 8 | 1-1 | 10:52:05 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 8 | 1-1 | 10:52:05 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 8 | 1-1 | 10:52:06 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 8 | 1-1 | 10:52:07 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4300 |  |
| Jogador 8 | 1-1 | 10:52:07 | MOVE Board -> Board: Leona (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 8 | 1-1 | 10:52:08 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 8 | 1-1 | 10:52:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 8 | 1-2 | 10:52:11 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 8 | 1-2 | 10:52:12 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1300 |  |
| Jogador 8 | 1-2 | 10:52:12 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 8 | 1-2 | 10:52:13 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0900 |  |
| Jogador 8 | 1-2 | 10:52:14 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 8 | 1-2 | 10:52:14 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0900 |  |
| Jogador 8 | 1-2 | 10:52:15 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0400 |  |
| Jogador 8 | 1-2 | 10:52:16 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0800 |  |
| Jogador 8 | 1-2 | 10:52:17 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0400 |  |
| Jogador 8 | 1-3 | 10:52:18 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.3800 |  |
| Jogador 8 | 1-3 | 10:52:19 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 1.1200 |  |
| Jogador 8 | 1-3 | 10:52:19 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.1400 |  |
| Jogador 8 | 1-3 | 10:52:20 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 8 | 1-3 | 10:52:21 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 8 | 1-3 | 10:52:21 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 8 | 1-3 | 10:52:22 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | -0.3900 |  |
| Jogador 8 | 1-3 | 10:52:23 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 8 | 1-3 | 10:52:24 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 8 | 1-4 | 10:52:25 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | -0.3100 |  |
| Jogador 8 | 1-4 | 10:52:26 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Teemo | 0.0000 |  |
| Jogador 8 | 1-4 | 10:52:26 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Teemo | -0.1800 |  |
| Jogador 8 | 1-4 | 10:52:27 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | 0.1800 |  |
| Jogador 8 | 1-4 | 10:52:28 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | 0.4400 |  |
| Jogador 8 | 1-4 | 10:52:28 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Teemo | 0.1700 |  |
| Jogador 8 | 1-4 | 10:52:29 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Teemo | -0.3300 |  |
| Jogador 8 | 1-4 | 10:52:30 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Teemo | 0.1900 |  |
| Jogador 8 | 1-4 | 10:52:31 | MOVE Board -> Board: Teemo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Teemo | 0.3000 |  |
| Jogador 8 | 2-1 | 10:52:33 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Teemo | -0.3200 |  |
| Jogador 8 | 2-1 | 10:52:33 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 8 | 2-1 | 10:52:34 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Teemo | -0.8600 |  |
| Jogador 8 | 2-1 | 10:52:35 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | 0.1500 |  |
| Jogador 8 | 2-1 | 10:52:36 | MOVE Bench -> Board: Krugue (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Krug18 | 0.0400 |  |
| Jogador 8 | 2-1 | 10:52:36 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Krug18 | 0.0400 |  |
| Jogador 8 | 2-1 | 10:52:37 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Krug18 | 0.2300 |  |
| Jogador 8 | 2-1 | 10:52:38 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Krug18 | 0.0200 |  |
| Jogador 8 | 2-1 | 10:52:38 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_BFSword -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Krug18 | 0.2000 |  |
| Jogador 8 | 2-2 | 10:52:40 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | — | DA_Krug18 | -0.4300 |  |
| Jogador 8 | 2-2 | 10:52:41 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_Krug18 | 0.1300 |  |
| Jogador 8 | 2-2 | 10:52:42 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | — | DA_Krug18 | -0.3800 |  |
| Jogador 8 | 2-2 | 10:52:43 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_Krug18 | 0.2800 |  |
| Jogador 8 | 2-2 | 10:52:43 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | — | DA_Krug18 | -0.3600 |  |
| Jogador 8 | 2-2 | 10:52:44 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_Krug18 | 0.2600 |  |
| Jogador 8 | 2-2 | 10:52:45 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | — | DA_Krug18 | -0.3400 |  |
| Jogador 8 | 2-2 | 10:52:45 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | — | DA_Krug18 | 0.1400 |  |
| Jogador 8 | 2-2 | 10:52:46 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_Krug18 | 0.1800 |  |
| Jogador 8 | 2-3 | 10:52:48 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | — | DA_Krug18 | -0.3300 |  |
| Jogador 8 | 2-3 | 10:52:49 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_Krug18 | 0.2200 |  |
| Jogador 8 | 2-3 | 10:52:50 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_Krug18 | -0.0200 |  |
| Jogador 8 | 2-3 | 10:52:50 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | — | DA_Krug18 | -0.0200 |  |
| Jogador 8 | 2-3 | 10:52:51 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | — | DA_Krug18 | 0.2600 |  |
| Jogador 8 | 2-3 | 10:52:52 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | — | DA_Krug18 | 0.0200 |  |
| Jogador 8 | 2-3 | 10:52:52 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_Krug18 | 0.2900 |  |
| Jogador 8 | 2-3 | 10:52:53 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | — | DA_Krug18 | -0.3600 |  |
| Jogador 8 | 2-3 | 10:52:54 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | — | DA_Krug18 | 0.2900 |  |
| Jogador 8 | 2-4 | 10:52:56 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Rival | DA_Krug18 | -0.3600 |  |
| Jogador 8 | 2-4 | 10:52:57 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Rival | DA_Krug18 | 0.3500 |  |
| Jogador 8 | 2-4 | 10:52:57 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Vivaz | DA_18_Rammus | -0.6000 |  |
| Jogador 8 | 2-4 | 10:52:58 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Vivaz | DA_18_Rammus | 0.0700 |  |
| Jogador 8 | 2-4 | 10:52:59 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Vivaz | DA_18_Rammus | -0.0700 |  |
| Jogador 8 | 2-4 | 10:52:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Vivaz | DA_18_Rammus | 0.3700 |  |
| Jogador 8 | 2-4 | 10:53:00 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Vivaz | DA_18_Rammus | -0.1200 |  |
| Jogador 8 | 2-4 | 10:53:01 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Vivaz | DA_18_Rammus | 0.3800 |  |
| Jogador 8 | 2-4 | 10:53:02 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Vivaz | DA_18_Rammus | -0.0900 |  |
| Jogador 8 | 2-5 | 10:53:04 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vivaz | DA_18_Tristana | 0.4000 |  |
| Jogador 8 | 2-5 | 10:53:04 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Vivaz | DA_18_Rammus | -0.5000 |  |
| Jogador 8 | 2-5 | 10:53:05 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vivaz | DA_18_Diana | 0.2800 |  |
| Jogador 8 | 2-5 | 10:53:06 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Devastador | DA_18_Diana | 0.4300 |  |
| Jogador 8 | 2-5 | 10:53:06 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Devastador | DA_18_Diana | 0.3500 |  |
| Jogador 8 | 2-5 | 10:53:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Diana | -0.1200 |  |
| Jogador 8 | 2-5 | 10:53:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Devastador | DA_18_Diana | -0.0400 |  |
| Jogador 8 | 2-5 | 10:53:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 2 | Devastador | DA_18_Diana | -0.1200 |  |
| Jogador 8 | 2-5 | 10:53:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 2 | Devastador | DA_18_Diana | -0.0400 |  |
| Jogador 8 | 2-6 | 10:53:11 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Devastador | DA_18_Diana | -0.1200 |  |
| Jogador 8 | 2-6 | 10:53:12 | COMPROU: Akali (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 1 | Devastador | DA_18_Diana | 1.0600 |  |
| Jogador 8 | 2-6 | 10:53:13 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | Devastador | DA_18_Diana | -0.0500 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-6 | 10:53:14 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Devastador | DA_18_Diana | -0.8900 |  |
| Jogador 8 | 2-6 | 10:53:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Devastador | DA_18_Diana | 0.3200 |  |
| Jogador 8 | 2-6 | 10:53:15 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Devastador | DA_18_Diana | -0.1300 |  |
| Jogador 8 | 2-6 | 10:53:16 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Devastador | DA_18_Diana | 0.0800 |  |
| Jogador 8 | 2-6 | 10:53:16 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Devastador | DA_18_Diana | 0.4000 |  |
| Jogador 8 | 2-6 | 10:53:17 | MOVE Board -> Board: Diana (i:6.0) <-> Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Devastador | DA_18_Diana | -0.0500 |  |
| Jogador 8 | 2-7 | 10:53:19 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_18_Lillia | -0.0200 |  |
| Jogador 8 | 2-7 | 10:53:20 | MOVE Bench -> Board: Lillia (i:8.0) <-> Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_18_Lillia | -0.3200 |  |
| Jogador 8 | 2-7 | 10:53:21 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_SparringGloves -> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_18_Lillia | 0.1500 |  |
| Jogador 8 | 2-7 | 10:53:21 | MOVE Board -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 2-7 | 10:53:22 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 2-7 | 10:53:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_18_Lillia | -0.0600 |  |
| Jogador 8 | 3-1 | 10:53:27 | VENDEU: Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Devastador | DA_18_Lillia | -0.1000 |  |
| Jogador 8 | 3-1 | 10:53:28 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Devastador | DA_18_Lillia | 0.7700 |  |
| Jogador 8 | 3-1 | 10:53:28 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Devastador | DA_18_Lillia | -0.8800 |  |
| Jogador 8 | 3-1 | 10:53:29 | COMPROU: Sett (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Devastador | DA_18_Lillia | -0.2500 |  |
| Jogador 8 | 3-1 | 10:53:30 | MOVE Bench -> Board: Sett (i:8.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Devastador | DA_18_Sett | -0.4000 |  |
| Jogador 8 | 3-1 | 10:53:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Devastador | DA_18_Sett | 0.0100 |  |
| Jogador 8 | 3-1 | 10:53:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Devastador | DA_18_Sett | -0.0900 |  |
| Jogador 8 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Devastador | DA_18_Sett | -0.0100 |  |
| Jogador 8 | 3-1 | 10:53:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Devastador | DA_18_Sett | -0.0900 |  |
| Jogador 8 | 3-2 | 10:53:35 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_18_Sett | -0.2000 |  |
| Jogador 8 | 3-2 | 10:53:35 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Vi (i:6.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_18_Sett | 0.1100 |  |
| Jogador 8 | 3-2 | 10:53:36 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Vi (i:6.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_18_Sett | 0.0500 |  |
| Jogador 8 | 3-2 | 10:53:37 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Devastador | DA_18_Sett | 0.7000 |  |
| Jogador 8 | 3-2 | 10:53:37 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Devastador | DA_18_Sett | -0.0900 |  |
| Jogador 8 | 3-2 | 10:53:38 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Devastador | DA_18_Sett | -0.0100 |  |
| Jogador 8 | 3-2 | 10:53:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Sett | 0.0800 |  |
| Jogador 8 | 3-2 | 10:53:40 | MOVE Board -> Board: Sett (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-2 | 10:53:40 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.5100 |  |
| Jogador 8 | 3-3 | 10:53:43 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Devastador | DA_18_Lillia | -0.0900 |  |
| Jogador 8 | 3-3 | 10:53:44 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Devastador | DA_18_Lillia | -0.3000 |  |
| Jogador 8 | 3-3 | 10:53:44 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Devastador | DA_18_Lillia | -0.0900 |  |
| Jogador 8 | 3-3 | 10:53:45 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-3 | 10:53:46 | MOVE Board -> Board: Sett (i:8.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-3 | 10:53:47 | MOVE Board -> Board: Diana (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Sett | -0.0100 |  |
| Jogador 8 | 3-3 | 10:53:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Sett | 0.0000 |  |
| Jogador 8 | 3-4 | 10:53:51 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Devastador | DA_18_Sett | 0.0100 |  |
| Jogador 8 | 3-4 | 10:53:52 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Devastador | DA_18_Sett | 0.6200 |  |
| Jogador 8 | 3-4 | 10:53:53 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Devastador | DA_18_Sett | -0.4200 |  |
| Jogador 8 | 3-4 | 10:53:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Devastador | DA_18_Sett | 0.2100 |  |
| Jogador 8 | 3-4 | 10:53:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_18_Sett | -0.0100 |  |
| Jogador 8 | 3-4 | 10:53:55 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Devastador | DA_18_Sett | -0.1300 |  |
| Jogador 8 | 3-4 | 10:53:56 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_18_Sett | 0.0300 |  |
| Jogador 8 | 3-4 | 10:53:56 | MOVE Board -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-4 | 10:53:57 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-5 | 10:54:00 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Devastador | DA_18_Lillia | 0.2200 |  |
| Jogador 8 | 3-5 | 10:54:01 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Devastador | DA_18_Lillia | 0.1600 |  |
| Jogador 8 | 3-5 | 10:54:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-5 | 10:54:02 | MOVE Board -> Board: Rammus (i:6.0) <-> Sett (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-5 | 10:54:03 | MOVE Board -> Board: Sett (i:8.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-5 | 10:54:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-6 | 10:54:08 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Devastador | DA_18_Lillia | 0.6000 |  |
| Jogador 8 | 3-6 | 10:54:09 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-6 | 10:54:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-6 | 10:54:10 | MOVE Board -> Board: Diana (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-6 | 10:54:11 | MOVE Board -> Board: Vi (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-6 | 10:54:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-7 | 10:54:17 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Devastador | DA_18_Lillia | 0.1100 |  |
| Jogador 8 | 3-7 | 10:54:18 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Devastador | DA_18_Lillia | 0.2400 |  |
| Jogador 8 | 3-7 | 10:54:18 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_NeedlesslyLargeRod -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Devastador | DA_18_Lillia | 0.2000 |  |
| Jogador 8 | 3-7 | 10:54:19 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0200 |  |
| Jogador 8 | 3-7 | 10:54:20 | MOVE Board -> Board: Diana (i:6.0) <-> Sett (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-7 | 10:54:20 | MOVE Board -> Board: Sett (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-7 | 10:54:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 4-1 | 10:54:26 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Devastador | DA_18_Lillia | 0.7400 |  |
| Jogador 8 | 4-1 | 10:54:27 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_18_Lillia | 0.0500 |  |
| Jogador 8 | 4-1 | 10:54:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.2000 |  |
| Jogador 8 | 4-1 | 10:54:28 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 4-1 | 10:54:29 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 4-1 | 10:54:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Devastador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 4-2 | 10:54:35 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Devastador | DA_18_Lillia | -0.0400 |  |
| Jogador 8 | 4-2 | 10:54:36 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Devastador | DA_18_Lillia | 0.6500 |  |
| Jogador 8 | 4-2 | 10:54:36 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Devastador | DA_18_Lillia | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-2 | 10:54:37 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Devastador | DA_18_Lillia | 0.1400 |  |
| Jogador 8 | 4-2 | 10:54:38 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Devastador | DA_18_Diana | 0.6800 |  |
| Jogador 8 | 4-2 | 10:54:39 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Devastador | DA_18_Diana | 0.0800 |  |
| Jogador 8 | 4-2 | 10:54:39 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Devastador | DA_18_Diana | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-2 | 10:54:40 | VENDEU: Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Devastador | DA_18_Lillia | -0.1000 |  |
| Jogador 8 | 4-2 | 10:54:41 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Devastador | DA_18_Lillia | 0.4400 |  |
| Jogador 8 | 4-3 | 10:54:44 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Sett (i:8.0) (tabuleiro slot 17) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Devastador | DA_18_Lillia | 0.0800 |  |
| Jogador 8 | 4-3 | 10:54:45 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Lillia (i:8.0) (tabuleiro slot 2) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Devastador | DA_18_Lillia | 0.0800 |  |
| Jogador 8 | 4-3 | 10:54:46 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Devastador | DA_18_Lillia | 0.1500 |  |
| Jogador 8 | 4-3 | 10:54:46 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Devastador | DA_18_Lillia | -0.1800 |  |
| Jogador 8 | 4-3 | 10:54:47 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Devastador | DA_18_Lillia | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-3 | 10:54:48 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Devastador | DA_18_Lillia | 0.0800 |  |
| Jogador 8 | 4-3 | 10:54:48 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Devastador | DA_18_Lillia | 0.6100 |  |
| Jogador 8 | 4-3 | 10:54:49 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Devastador | DA_18_Lillia | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-3 | 10:54:50 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Devastador | DA_18_Lillia | 0.0600 |  |
| Jogador 8 | 4-4 | 10:54:53 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_18_Lillia | 0.6700 |  |
| Jogador 8 | 4-4 | 10:54:54 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Devastador | DA_18_Lillia | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-4 | 10:54:55 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Devastador | DA_18_Lillia | -0.0500 |  |
| Jogador 8 | 4-4 | 10:54:56 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Devastador | DA_18_Diana | 0.7100 |  |
| Jogador 8 | 4-4 | 10:54:56 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Devastador | DA_18_Diana | -0.1800 |  |
| Jogador 8 | 4-4 | 10:54:57 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Devastador | DA_18_Diana | -0.1900 |  |
| Jogador 8 | 4-4 | 10:54:58 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Devastador | DA_18_Diana | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-4 | 10:54:58 | VENDEU: Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Devastador | DA_18_Lillia | -0.1800 |  |
| Jogador 8 | 4-4 | 10:54:59 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Devastador | DA_18_Lillia | 0.6900 |  |
| Jogador 8 | 4-5 | 10:55:03 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Devastador | DA_18_Lillia | 0.0700 |  |
| Jogador 8 | 4-5 | 10:55:03 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Devastador | DA_18_Lillia | -0.0600 |  |
| Jogador 8 | 4-5 | 10:55:04 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Devastador | DA_18_Lillia | 0.0600 |  |
| Jogador 8 | 4-5 | 10:55:05 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Devastador | DA_18_Lillia | 0.2200 |  |
| Jogador 8 | 4-5 | 10:55:05 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Devastador | DA_18_Lillia | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-5 | 10:55:06 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Devastador | DA_18_Lillia | 0.0300 |  |
| Jogador 8 | 4-5 | 10:55:07 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Devastador | DA_18_Lillia | 0.1900 |  |
| Jogador 8 | 4-5 | 10:55:07 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Devastador | DA_18_Lillia | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-5 | 10:55:08 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Devastador | DA_18_Lillia | 0.0800 |  |
| Jogador 8 | 4-6 | 10:55:12 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Devastador | DA_Murkwolf18 | 0.8300 |  |
| Jogador 8 | 4-6 | 10:55:13 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Devastador | DA_Murkwolf18 | 0.1700 |  |
| Jogador 8 | 4-6 | 10:55:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Devastador | DA_Murkwolf18 | 0.6000 |  |
| Jogador 8 | 4-6 | 10:55:14 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Devastador | DA_Murkwolf18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-6 | 10:55:15 | VENDEU: Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Defendente | DA_18_Lillia | -0.1000 |  |
| Jogador 8 | 4-6 | 10:55:16 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Defendente | DA_18_Lillia | 0.1600 |  |
| Jogador 8 | 4-6 | 10:55:17 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Defendente | DA_18_Lillia | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-6 | 10:55:17 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Defendente | DA_18_Lillia | 0.0700 |  |
| Jogador 8 | 4-6 | 10:55:18 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Defendente | DA_18_Lillia | 0.7100 |  |
| Jogador 8 | 4-7 | 10:55:22 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Defendente | DA_18_Lillia | 0.1600 |  |
| Jogador 8 | 4-7 | 10:55:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Defendente | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 8 | 4-7 | 10:55:23 | COMPROU: Sett (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Defendente | DA_Fiddlesticks18 | 0.7000 |  |
| Jogador 8 | 4-7 | 10:55:24 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Defendente | DA_Fiddlesticks18 | 0.2600 |  |
| Jogador 8 | 4-7 | 10:55:24 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Defendente | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 8 | 4-7 | 10:55:25 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Defendente | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 8 | 4-7 | 10:55:26 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Defendente | DA_Fiddlesticks18 | -0.2400 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-7 | 10:55:26 | VENDEU: Fiddlesticks (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Defendente | DA_18_Sett | -0.1200 |  |
| Jogador 8 | 4-7 | 10:55:27 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Defendente | DA_18_Sett | -0.0300 |  |
| Jogador 8 | 5-1 | 10:55:31 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Defendente | DA_18_Sett | -0.0800 |  |
| Jogador 8 | 5-1 | 10:55:32 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Defendente | DA_18_Sett | 0.8100 |  |
| Jogador 8 | 5-1 | 10:55:33 | VENDEU: Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Defendente | DA_18_Sett | 0.0700 |  |
| Jogador 8 | 5-1 | 10:55:33 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Defendente | DA_18_KhaZix | 0.5800 |  |
| Jogador 8 | 5-1 | 10:55:34 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Defendente | DA_18_KhaZix | 0.1600 |  |
| Jogador 8 | 5-1 | 10:55:35 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Defendente | DA_18_KhaZix | 0.0300 |  |
| Jogador 8 | 5-1 | 10:55:36 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Defendente | DA_18_KhaZix | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-1 | 10:55:36 | VENDEU: Kha'Zix (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 3 | Defendente | DA_18_Sett | -0.1100 |  |
| Jogador 8 | 5-1 | 10:55:37 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 3 | Defendente | DA_18_Sett | 0.5400 |  |
| Jogador 8 | 5-2 | 10:55:41 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Defendente | DA_18_Sett | 0.4600 |  |
| Jogador 8 | 5-2 | 10:55:42 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Defendente | DA_18_Sett | 0.3200 |  |
| Jogador 8 | 5-2 | 10:55:43 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Defendente | DA_18_Sett | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-2 | 10:55:43 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Defendente | DA_18_Sett | -0.1300 |  |
| Jogador 8 | 5-2 | 10:55:44 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Defendente | DA_18_Sett | 0.3600 |  |
| Jogador 8 | 5-2 | 10:55:45 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 5 | Defendente | DA_18_Sett | -0.1000 |  |
| Jogador 8 | 5-2 | 10:55:45 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Defendente | DA_18_Teemo | 0.9400 |  |
| Jogador 8 | 5-2 | 10:55:46 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 5 | Defendente | DA_18_Teemo | -0.2000 |  |
| Jogador 8 | 5-2 | 10:55:47 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 5 | Defendente | DA_18_Teemo | -0.1000 |  |
| Jogador 8 | 5-3 | 10:55:52 | VENDEU: Teemo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Defendente | DA_18_Sett | -0.1500 |  |
| Jogador 8 | 5-3 | 10:55:52 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Defendente | DA_18_Tristana | 0.9500 |  |
| Jogador 8 | 5-3 | 10:55:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Defendente | DA_18_Tristana | -0.2500 |  |
| Jogador 8 | 5-3 | 10:55:54 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Defendente | DA_18_Tristana | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-3 | 10:55:55 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Defendente | DA_18_Tristana | 0.0500 |  |
| Jogador 8 | 5-3 | 10:55:55 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Defendente | DA_18_Tristana | 0.8600 |  |
| Jogador 8 | 5-3 | 10:55:56 | MOVE Board -> Board: Rammus (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Defendente | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 5-3 | 10:55:57 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Defendente | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 5-3 | 10:55:57 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Defendente | DA_18_Tristana | 0.5800 |  |
| Jogador 8 | 5-4 | 10:56:02 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Defendente | DA_18_Tristana | 0.3600 |  |
| Jogador 8 | 5-4 | 10:56:03 | VENDEU: Tristana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Defendente | DA_18_Sett | -0.1800 |  |
| Jogador 8 | 5-4 | 10:56:04 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Defendente | DA_18_Sett | 0.6900 |  |
| Jogador 8 | 5-4 | 10:56:04 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 74 | 5 | Defendente | DA_18_Sett | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-4 | 10:56:05 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Defendente | DA_18_Sett | 0.0800 |  |
| Jogador 8 | 5-4 | 10:56:06 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Defendente | DA_18_Sett | 0.0100 |  |
| Jogador 8 | 5-4 | 10:56:07 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Defendente | DA_18_Sett | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-4 | 10:56:07 | VENDEU: Sivir (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Defendente | DA_18_Sett | 0.0600 |  |
| Jogador 8 | 5-5 | 10:56:14 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Defendente | DA_18_Sett | 0.1800 |  |
| Jogador 8 | 5-5 | 10:56:18 | VENDEU: Rubrivira (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Defendente | DA_18_Sett | 0.0700 |  |
| Jogador 8 | 5-5 | 10:56:19 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Defendente | DA_18_Sett | 0.4000 |  |
| Jogador 8 | 5-5 | 10:56:19 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Defendente | DA_18_Sett | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-6 | 10:56:23 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Defendente | DA_18_Sett | 0.0500 |  |
| Jogador 8 | 5-6 | 10:56:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Defendente | DA_Scuttlecrab18 | 0.7600 |  |
| Jogador 8 | 5-6 | 10:56:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Defendente | DA_Scuttlecrab18 | 0.2800 |  |
| Jogador 8 | 5-6 | 10:56:26 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Defendente | DA_Scuttlecrab18 | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-6 | 10:56:26 | VENDEU: Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Defendente | DA_18_Sett | -0.0800 |  |
| Jogador 8 | 5-6 | 10:56:27 | COMPROU: Lux (Inferno) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Defendente | DA_18_Lux_Inferno | 0.3000 |  |
| Jogador 8 | 5-7 | 10:56:34 | EQUIP_FROM_INVENTORY: DA_18_EmblemHunter -> Sett (i:8.0) (tabuleiro slot 17) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Defendente | DA_18_Lux_Inferno | -0.0300 |  |
| Jogador 8 | 5-7 | 10:56:35 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 107 | 5 | Defendente | DA_18_Lux_Inferno | 0.4200 |  |
| Jogador 8 | 5-7 | 10:56:35 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Defendente | DA_18_Lux_Inferno | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-7 | 10:56:36 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 107 | 5 | Defendente | DA_18_Lux_Inferno | -0.1300 |  |
| Jogador 8 | 5-7 | 10:56:37 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 104 | 5 | Defendente | DA_18_Rammus | 1.0100 |  |
| Jogador 8 | 5-7 | 10:56:37 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Defendente | DA_18_Rammus | -0.0100 |  |
| Jogador 8 | 5-7 | 10:56:38 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Defendente | DA_18_Rammus | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 8 | 5-7 | 10:56:39 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Defendente | DA_18_Rammus | 0.0600 |  |
| Jogador 8 | 5-7 | 10:56:40 | MOVE Bench -> Board: Rammus (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Defendente | DA_18_Rammus | 0.6000 |  |
| Jogador 8 | 6-1 | 10:56:48 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 111 | 5 | Defendente | DA_18_Rammus | 0.9900 |  |
| Jogador 8 | 6-1 | 10:56:48 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 107 | 5 | Defendente | DA_18_Rammus | -0.2700 |  |
| Jogador 8 | 6-1 | 10:56:49 | MOVE Board -> Board: Rammus (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 107 | 5 | Defendente | DA_18_Rammus | 0.0000 |  |
| Jogador 8 | 6-1 | 10:56:49 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 107 | 5 | Defendente | DA_18_Rammus | 0.4000 |  |
| Jogador 8 | 6-1 | 10:56:50 | COMPROU: Leona (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 106 | 5 | Defendente | DA_18_Rammus | 0.3800 |  |
| Jogador 8 | 6-1 | 10:56:51 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 104 | 5 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 8 | 6-1 | 10:56:52 | VENDEU: Leona (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 105 | 5 | Defendente | DA_18_Rammus | -0.0800 |  |
| Jogador 8 | 6-1 | 10:56:52 | COMPROU: Shen (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 103 | 5 | Defendente | DA_18_Rammus | 1.0600 |  |
| Jogador 8 | 6-1 | 10:56:53 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 103 | 5 | Defendente | DA_18_Rammus | 0.6000 |  |
| Jogador 8 | 6-2 | 10:57:01 | COMPROU: Sett (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 112 | 5 | Defendente | DA_18_Sett | 0.9100 |  |
| Jogador 8 | 6-2 | 10:57:01 | COMPROU: Sivir (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 108 | 5 | Defendente | DA_18_Sett | 0.1200 |  |
| Jogador 8 | 6-2 | 10:57:02 | COMPROU: Vi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 105 | 5 | Defendente | DA_18_Sett | 0.6100 |  |
| Jogador 8 | 6-2 | 10:57:03 | MOVE Bench -> Board: Shen (i:8.0) <-> LeBlanc (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 105 | 5 | Defendente | DA_18_Sett | 0.1000 |  |
| Jogador 8 | 6-2 | 10:57:04 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 103 | 5 | Defendente | DA_18_Sett | -0.0900 |  |
| Jogador 8 | 6-2 | 10:57:04 | VENDEU: Vi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 106 | 5 | Defendente | DA_18_Sett | -0.1400 |  |
| Jogador 8 | 6-2 | 10:57:05 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 103 | 5 | Defendente | DA_18_Sett | -0.2500 |  |
| Jogador 8 | 6-2 | 10:57:06 | VENDEU: Sett (i:16.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 114 | 5 | Defendente | DA_18_Rammus | -0.0500 |  |
| Jogador 8 | 6-2 | 10:57:06 | MOVE Bench -> Board: Amumu (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 114 | 5 | Defendente | DA_18_Rammus | 0.4100 |  |
| Jogador 8 | 6-3 | 10:57:14 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Shen (i:8.0) (tabuleiro slot 24) | WINSTREAK | WINSTREAK: preservar vantagem atual | 128 | 5 | Defendente | DA_18_Rammus | 0.1400 |  |
| Jogador 8 | 6-3 | 10:57:15 | EQUIP_FROM_INVENTORY: DA_18_EmblemHunter -> Shen (i:8.0) (tabuleiro slot 24) | WINSTREAK | WINSTREAK: preservar vantagem atual | 128 | 5 | Defendente | DA_18_Rammus | 0.0100 |  |
| Jogador 8 | 6-3 | 10:57:15 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 126 | 5 | Defendente | DA_18_Rammus | 1.0200 |  |
| Jogador 8 | 6-3 | 10:57:16 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 122 | 5 | Defendente | DA_18_Rammus | 0.3200 |  |
| Jogador 8 | 6-3 | 10:57:17 | COMPROU: Dragão Ancião (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 117 | 5 | Defendente | DA_18_Rammus | -0.0600 |  |
| Jogador 8 | 6-3 | 10:57:18 | COMPROU: Master Yi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 114 | 5 | Defendente | DA_18_Rammus | -0.2700 |  |
| Jogador 8 | 6-3 | 10:57:18 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 112 | 5 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 8 | 6-3 | 10:57:19 | VENDEU: LeBlanc (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 117 | 5 | Defendente | DA_18_Rammus | -0.0800 |  |
| Jogador 8 | 6-3 | 10:57:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 114 | 5 | Defendente | DA_Fiddlesticks18 | 1.0600 |  |
| Jogador 8 | 6-4 | 10:57:28 | VENDEU: Fiddlesticks (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 135 | 5 | Defendente | DA_18_Rammus | -0.2200 |  |
| Jogador 8 | 6-4 | 10:57:29 | COMPROU: Azir (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 132 | 5 | Defendente | DA_18_Rammus | -0.1800 |  |
| Jogador 8 | 6-4 | 10:57:30 | VENDEU: Master Yi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 135 | 5 | Defendente | DA_18_Rammus | 0.0800 |  |
| Jogador 8 | 6-4 | 10:57:30 | COMPROU: Leona (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 134 | 5 | Defendente | DA_18_Rammus | 0.4000 |  |
| Jogador 8 | 6-4 | 10:57:31 | VENDEU: Azir (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 137 | 5 | Defendente | DA_18_Rammus | 0.0600 |  |
| Jogador 8 | 6-4 | 10:57:32 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 134 | 5 | Defendente | DA_18_Rammus | -0.1800 |  |
| Jogador 8 | 6-4 | 10:57:32 | MOVE Bench -> Board: Leona (i:2.0) <-> Shen (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 134 | 5 | Defendente | DA_18_Rammus | -0.7500 |  |
| Jogador 8 | 6-4 | 10:57:33 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 134 | 5 | Defendente | DA_18_Rammus | 0.3300 |  |
| Jogador 8 | 6-4 | 10:57:34 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 134 | 5 | Defendente | DA_18_Rammus | 0.3900 |  |
| Jogador 8 | 6-5 | 10:57:42 | COMPROU: Vi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 145 | 5 | Defendente | DA_18_Rammus | 0.5000 |  |
| Jogador 8 | 6-5 | 10:57:43 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 142 | 5 | Defendente | DA_18_Rammus | -0.2100 |  |
| Jogador 8 | 6-5 | 10:57:44 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 140 | 5 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 8 | 6-5 | 10:57:44 | VENDEU: Vi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 143 | 5 | Defendente | DA_18_Rammus | -0.1300 |  |
| Jogador 8 | 6-5 | 10:57:45 | COMPROU: Lillia (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 139 | 5 | Defendente | DA_18_Rammus | 0.9400 |  |
| Jogador 8 | 6-5 | 10:57:46 | VENDEU: Mamãe Bicuda (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 142 | 5 | Defendente | DA_18_Rammus | 0.0600 |  |
| Jogador 8 | 6-5 | 10:57:46 | COMPROU: Amumu (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 138 | 5 | Defendente | DA_18_Rammus | 0.8800 |  |
| Jogador 8 | 6-5 | 10:57:47 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 136 | 5 | Defendente | DA_18_Rammus | -0.0900 |  |
| Jogador 8 | 6-5 | 10:57:48 | VENDEU: Kha'Zix (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 139 | 5 | Defendente | DA_18_Rammus | 0.0700 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 21 | 21 | 105 | 21 | 14 | 170 | 9 | 22 |
| Jogador 2 | 26 | 40 | 200 | 26 | 20 | 192 | 25 | 20 |
| Jogador 3 | 20 | 28 | 140 | 20 | 12 | 163 | 7 | 16 |
| Jogador 4 | 38 | 65 | 325 | 38 | 19 | 313 | 19 | 55 |
| Jogador 5 | 34 | 38 | 190 | 34 | 19 | 253 | 12 | 41 |
| Jogador 6 | 28 | 28 | 140 | 28 | 17 | 223 | 32 | 27 |
| Jogador 7 | 28 | 41 | 205 | 28 | 18 | 238 | 9 | 20 |
| Jogador 8 | 38 | 63 | 315 | 38 | 21 | 312 | 40 | 28 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 170 | 170 | 170 | 0 | 165 | 0 | 170 | 170 | 170 | 59/44 |
| Jogador 2 | 192 | 192 | 192 | 0 | 183 | 0 | 192 | 192 | 192 | 65/53 |
| Jogador 3 | 163 | 163 | 163 | 0 | 156 | 0 | 163 | 163 | 163 | 64/51 |
| Jogador 4 | 313 | 313 | 313 | 0 | 294 | 0 | 313 | 313 | 313 | 111/96 |
| Jogador 5 | 253 | 253 | 253 | 0 | 244 | 0 | 253 | 253 | 253 | 77/61 |
| Jogador 6 | 223 | 223 | 223 | 0 | 212 | 0 | 223 | 223 | 223 | 65/51 |
| Jogador 7 | 238 | 238 | 238 | 0 | 229 | 0 | 238 | 238 | 238 | 91/77 |
| Jogador 8 | 312 | 312 | 312 | 0 | 298 | 0 | 312 | 312 | 312 | 119/104 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +a8111a04-3067-4ce6-9a4b-4f5bb205f413 / -— |
| Jogador 1 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.010813108645379543 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0420212745666504 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 12 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43606460094451904 | 0.0 | 0.0 | +— / -cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16422347724437714 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 14 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10533468425273895 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.03157453238964081 | 0.0 | 0.0 | +679fe281-674a-438b-bdcf-57229a283d44 / -— |
| Jogador 1 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1580381840467453 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.061160679906606674 | 0.0 | 0.0 | +ba9a7a46-a9ca-437f-b286-abb9eb5f9fbb / -— |
| Jogador 1 | 1-2 | 18 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37647077441215515 | 0.0 | 0.0 | +— / -ba9a7a46-a9ca-437f-b286-abb9eb5f9fbb |
| Jogador 1 | 1-2 | 19 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.061160679906606674 | 0.0 | 0.0 | +fa2c1f3d-6692-44d4-b94d-1e1e55bdba8c / -— |
| Jogador 1 | 1-3 | 21 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37647077441215515 | 0.0 | 0.0 | +— / -fa2c1f3d-6692-44d4-b94d-1e1e55bdba8c |
| Jogador 1 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08435463905334473 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 23 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3095271587371826 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13635088503360748 | 0.0 | 0.0 | +— / -cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.061160679906606674 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 27 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5746720433235168 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 28 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08167664706707001 | 0.0 | 0.0 | +— / -679fe281-674a-438b-bdcf-57229a283d44 |
| Jogador 1 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.013991355895996 | 0.0 | 0.0 | +8189d616-2d10-437f-86ce-218e11038acc / -— |
| Jogador 1 | 1-4 | 31 | SELL | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3305138349533081 | 0.0 | 0.0 | +— / -8189d616-2d10-437f-86ce-218e11038acc |
| Jogador 1 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.18978425860404968 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4095538556575775 | 0.0 | 0.0 | +— / -6465b229-8025-4e7d-94de-1cd49fa76167 |
| Jogador 1 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24149078130722046 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 35 | SELL | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4060458242893219 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06431453675031662 | 0.0 | 0.0 | +50fd90d6-9c1c-467f-bb3c-e88ca8815ef7 / -— |
| Jogador 1 | 1-4 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5593688488006592 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 38 | SELL | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764707699418068 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2284279614686966 | 0.0 | 0.0 | +9a936ebd-aacd-4366-a1c8-78534d5a253b / -— |
| Jogador 1 | 2-1 | 41 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3366430699825287 | 0.0 | 0.0 | +— / -9a936ebd-aacd-4366-a1c8-78534d5a253b |
| Jogador 1 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.9601004123687744 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 43 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.8027387857437134 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.9339319467544556 | 0.0 | 0.0 | +6770b090-e992-44c8-9223-f5cd6e92f19a / -— |
| Jogador 1 | 2-1 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06833002716302872 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 47 | PASS | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 51 | BUY | STABILIZE | 95.0 | 4 | 14 | 1 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3446756899356842 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 11 | 1 | 6.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.28567883372306824 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 53 | SELL | STABILIZE | 95.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3305138349533081 | 0.0 | 0.0 | +— / -6770b090-e992-44c8-9223-f5cd6e92f19a |
| Jogador 1 | 2-2 | 54 | BUY | STABILIZE | 95.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.24911782145500183 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7187753319740295 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 56 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08403106033802032 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 57 | SELL | STABILIZE | 95.0 | 4 | 10 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -50fd90d6-9c1c-467f-bb3c-e88ca8815ef7 |
| Jogador 1 | 2-2 | 58 | BUY | STABILIZE | 95.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.15591686964035034 | 0.0 | 0.0 | +4fc25524-9d8f-46f0-a145-ba3de2642229 / -— |
| Jogador 1 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07559920847415924 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 61 | BUY | STABILIZE | 90.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.0199733972549438 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -— |
| Jogador 1 | 2-3 | 62 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.00016414404672104865 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 63 | SELL | STABILIZE | 90.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3235498070716858 | 0.0 | 0.0 | +— / -ff10e482-7085-4e73-8a0c-fdd3f4938128 |
| Jogador 1 | 2-3 | 64 | BUY | STABILIZE | 90.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.15127749741077423 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 65 | SELL | STABILIZE | 90.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3127538561820984 | 0.0 | 0.0 | +— / -73185d11-22d3-4a1d-803a-b37e82272098 |
| Jogador 1 | 2-3 | 66 | BUY | STABILIZE | 90.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.08493559807538986 | 0.0 | 0.0 | +6951a681-f5b9-4c22-9182-46b4d2c3cbb3 / -— |
| Jogador 1 | 2-3 | 67 | SELL | STABILIZE | 90.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3016769289970398 | 0.0 | 0.0 | +— / -6951a681-f5b9-4c22-9182-46b4d2c3cbb3 |
| Jogador 1 | 2-3 | 68 | CRAFT_AND_EQUIP | STABILIZE | 90.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.13344721496105194 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 69 | CRAFT_AND_EQUIP | STABILIZE | 90.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.06657997518777847 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 71 | BUY | LOSS_STREAK | 84.0 | 4 | 22 | 2 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1678830236196518 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 72 | SELL | LOSS_STREAK | 84.0 | 4 | 19 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04288307577371597 | 0.0 | 0.0 | +— / -d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 2-4 | 73 | BUY | LOSS_STREAK | 84.0 | 4 | 22 | 2 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09468130767345428 | 0.0 | 0.0 | +8c5a0cda-86da-4f36-bee3-c2eae934e263 / -— |
| Jogador 1 | 2-4 | 74 | SELL | LOSS_STREAK | 84.0 | 4 | 20 | 2 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3278774917125702 | 0.0 | 0.0 | +— / -8c5a0cda-86da-4f36-bee3-c2eae934e263 |
| Jogador 1 | 2-4 | 75 | BUY | LOSS_STREAK | 84.0 | 4 | 22 | 2 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08027680963277817 | 0.0 | 0.0 | +7d8f4f6b-4eba-4c31-9834-bd81a3765520 / -— |
| Jogador 1 | 2-4 | 76 | SELL | LOSS_STREAK | 84.0 | 4 | 20 | 2 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.325307697057724 | 0.0 | 0.0 | +— / -7d8f4f6b-4eba-4c31-9834-bd81a3765520 |
| Jogador 1 | 2-4 | 77 | MOVE_BOARD | LOSS_STREAK | 84.0 | 4 | 22 | 2 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 78 | BUY_XP | LOSS_STREAK | 84.0 | 4 | 22 | 2 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04600000008940697 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 79 | BUY | LOSS_STREAK | 84.0 | 5 | 18 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08885373920202255 | 0.0 | 0.0 | +6bd83e05-f1a5-46e0-9d00-661cb843c7dc / -— |
| Jogador 1 | 2-5 | 81 | SELL | LOSS_STREAK | 84.0 | 5 | 24 | 2 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3158615529537201 | 0.0 | 0.0 | +— / -6bd83e05-f1a5-46e0-9d00-661cb843c7dc |
| Jogador 1 | 2-5 | 82 | BUY | LOSS_STREAK | 84.0 | 5 | 25 | 2 | 16.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11532920598983765 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 1 | 2-5 | 83 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 22 | 2 | 16.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40245407819747925 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 84 | BUY | STABILIZE | 84.0 | 5 | 22 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3268570601940155 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 85 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 20 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 86 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 20 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014520658180117607 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 87 | PASS | STABILIZE | 84.0 | 5 | 20 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020892856642603874 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 91 | SELL | STABILIZE | 78.0 | 5 | 28 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01837775483727455 | 0.0 | 0.0 | +— / -f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 2-6 | 92 | BUY | STABILIZE | 78.0 | 5 | 30 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9571738243103027 | 0.0 | 0.0 | +b32c67a7-6903-403a-9ed6-519ac8487685 / -— |
| Jogador 1 | 2-6 | 93 | SELL | SLOWROLL | 78.0 | 5 | 28 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3428948223590851 | 0.0 | 0.0 | +— / -b32c67a7-6903-403a-9ed6-519ac8487685 |
| Jogador 1 | 2-6 | 94 | BUY | STABILIZE | 78.0 | 5 | 30 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24534718692302704 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 95 | SELL | STABILIZE | 78.0 | 5 | 27 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0602976493537426 | 0.0 | 0.0 | +— / -15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 1 | 2-6 | 96 | BUY | STABILIZE | 78.0 | 5 | 30 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28529128432273865 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 97 | SELL | STABILIZE | 78.0 | 5 | 27 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08027098327875137 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 2-6 | 98 | BUY | STABILIZE | 78.0 | 5 | 30 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09734751284122467 | 0.0 | 0.0 | +f095cd70-c807-4086-a3f1-ddda4f6aa574 / -— |
| Jogador 1 | 2-6 | 99 | BUY_XP | STABILIZE | 78.0 | 5 | 28 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 101 | SELL | STABILIZE | 72.0 | 5 | 33 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29490628838539124 | 0.0 | 0.0 | +— / -f095cd70-c807-4086-a3f1-ddda4f6aa574 |
| Jogador 1 | 2-7 | 102 | BUY | STABILIZE | 72.0 | 5 | 35 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0714809894561768 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -— |
| Jogador 1 | 2-7 | 103 | SELL | SLOWROLL | 72.0 | 5 | 34 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9229999780654907 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 1 | 2-7 | 104 | BUY | STABILIZE | 72.0 | 5 | 35 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10333729535341263 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -— |
| Jogador 1 | 2-7 | 105 | SELL | STABILIZE | 72.0 | 5 | 33 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31829118728637695 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 1 | 2-7 | 106 | BUY | STABILIZE | 72.0 | 5 | 35 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04041847586631775 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 107 | BUY_XP | STABILIZE | 72.0 | 5 | 33 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 108 | BUY_XP | STABILIZE | 72.0 | 5 | 29 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 109 | BUY_XP | STABILIZE | 72.0 | 5 | 25 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03695499897003174 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 111 | SELL | STABILIZE | 72.0 | 6 | 30 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3202780783176422 | 0.0 | 0.0 | +— / -b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 3-1 | 112 | BUY | STABILIZE | 72.0 | 6 | 32 | 3 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.16221338510513306 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 113 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 29 | 2 | 22.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4003611207008362 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 114 | BUY | FAST8 | 72.0 | 6 | 29 | 2 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.046608567237854004 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 115 | CRAFT_AND_EQUIP | FAST8 | 72.0 | 6 | 27 | 2 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10240187495946884 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 116 | BUY_XP | FAST8 | 72.0 | 6 | 27 | 2 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 117 | BUY_XP | FAST8 | 72.0 | 6 | 23 | 2 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 118 | BUY_XP | FAST8 | 72.0 | 6 | 19 | 1 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 119 | BUY_XP | FAST8 | 72.0 | 6 | 15 | 1 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 121 | SELL | FAST8 | 61.0 | 6 | 20 | 2 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3301478922367096 | 0.0 | 0.0 | +— / -8e819ba6-a356-4d9b-a8c9-7493332900fb |
| Jogador 1 | 3-2 | 122 | BUY | FAST8 | 61.0 | 6 | 22 | 2 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7655791640281677 | 0.0 | 0.0 | +dc9a3df1-7032-4c92-a919-ca17ae7639ea / -— |
| Jogador 1 | 3-2 | 123 | SELL | FAST8 | 61.0 | 6 | 20 | 2 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3834705948829651 | 0.0 | 0.0 | +— / -dc9a3df1-7032-4c92-a919-ca17ae7639ea |
| Jogador 1 | 3-2 | 124 | BUY | FAST8 | 61.0 | 6 | 22 | 2 | 28.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3090650141239166 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 125 | BUY_XP | FAST8 | 61.0 | 6 | 18 | 1 | 28.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 126 | BUY_XP | FAST8 | 61.0 | 6 | 14 | 1 | 28.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 127 | BUY_XP | FAST8 | 61.0 | 6 | 10 | 1 | 28.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 128 | BUY_XP | FAST8 | 61.0 | 6 | 6 | 0 | 28.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08229999989271164 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 129 | MOVE_BENCH | FAST8 | 61.0 | 7 | 2 | 0 | 28.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40129968523979187 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 131 | BUY | FAST8 | 61.0 | 7 | 8 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7301713824272156 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 132 | SELL | FAST8 | 61.0 | 7 | 5 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39176061749458313 | 0.0 | 0.0 | +— / -c30e7bdb-41d6-423c-9d7d-2e146472e724 |
| Jogador 1 | 3-3 | 133 | BUY | FAST8 | 61.0 | 7 | 8 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.208995059132576 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-3 | 134 | BUY | FAST8 | 61.0 | 7 | 5 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11790197342634201 | 0.0 | 0.0 | +45450b46-63b4-488f-9469-3348c6da8f4b / -— |
| Jogador 1 | 3-3 | 135 | MOVE_BOARD | FAST8 | 61.0 | 7 | 2 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00012612795399036258 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 136 | MOVE_BOARD | FAST8 | 61.0 | 7 | 2 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014852713793516159 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 137 | MOVE_BOARD | FAST8 | 61.0 | 7 | 2 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 138 | PASS | FAST8 | 61.0 | 7 | 2 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 141 | SELL | FAST8 | 61.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02962852269411087 | 0.0 | 0.0 | +— / -e6ee6b15-d413-4678-8ffb-29272199a53d |
| Jogador 1 | 3-4 | 142 | SELL | FAST8 | 61.0 | 7 | 12 | 1 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41319528222084045 | 0.0 | 0.0 | +— / -45450b46-63b4-488f-9469-3348c6da8f4b |
| Jogador 1 | 3-4 | 143 | BUY | FAST8 | 61.0 | 7 | 15 | 1 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1797364056110382 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 144 | SELL | FAST8 | 61.0 | 7 | 12 | 1 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09964626282453537 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-4 | 145 | BUY | FAST8 | 61.0 | 7 | 15 | 1 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20265652239322662 | 0.0 | 0.0 | +54b47885-6cb9-42e7-a9bb-049e0e2d2956 / -— |
| Jogador 1 | 3-4 | 146 | BUY_XP | FAST8 | 61.0 | 7 | 14 | 1 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 147 | BUY_XP | FAST8 | 61.0 | 7 | 10 | 1 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 148 | BUY_XP | FAST8 | 61.0 | 7 | 6 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 149 | SELL | FAST8 | 61.0 | 7 | 2 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13148006796836853 | 0.0 | 0.0 | +— / -54b47885-6cb9-42e7-a9bb-049e0e2d2956 |
| Jogador 1 | 3-5 | 151 | BUY | FAST8 | 61.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7293567061424255 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 152 | SELL | FAST8 | 61.0 | 7 | 6 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.388572633266449 | 0.0 | 0.0 | +— / -727765c8-7f02-491e-a6da-12b0dab59f6d |
| Jogador 1 | 3-5 | 153 | BUY | FAST8 | 61.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19114527106285095 | 0.0 | 0.0 | +c5557e24-8174-4d79-9e22-c2cbbb8225a8 / -— |
| Jogador 1 | 3-5 | 154 | BUY_XP | FAST8 | 61.0 | 7 | 7 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 155 | SELL | FAST8 | 61.0 | 7 | 3 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11959166079759598 | 0.0 | 0.0 | +— / -c5557e24-8174-4d79-9e22-c2cbbb8225a8 |
| Jogador 1 | 3-5 | 156 | BUY | FAST8 | 61.0 | 7 | 5 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2019120752811432 | 0.0 | 0.0 | +f6e6e08d-ecfe-4c84-acfa-6ad8292968ee / -— |
| Jogador 1 | 3-5 | 157 | BUY_XP | FAST8 | 61.0 | 7 | 4 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 158 | MOVE_BOARD | FAST8 | 61.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 159 | MOVE_BOARD | FAST8 | 61.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 161 | SELL | FAST8 | 48.0 | 7 | 5 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1196860745549202 | 0.0 | 0.0 | +— / -f6e6e08d-ecfe-4c84-acfa-6ad8292968ee |
| Jogador 1 | 3-6 | 162 | BUY | FAST8 | 48.0 | 7 | 6 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08798268437385559 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 1 | 3-6 | 163 | SELL | FAST8 | 48.0 | 7 | 2 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11677155643701553 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 1 | 3-6 | 164 | BUY | FAST8 | 48.0 | 7 | 6 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.442422479391098 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -— |
| Jogador 1 | 3-6 | 165 | MOVE_BOARD | FAST8 | 48.0 | 7 | 3 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.70380444615148e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 166 | MOVE_BOARD | FAST8 | 48.0 | 7 | 3 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015114955604076385 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 167 | MOVE_BOARD | FAST8 | 48.0 | 7 | 3 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015004003420472145 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 168 | PASS | FAST8 | 48.0 | 7 | 3 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 171 | BUY | STABILIZE | 36.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8039959073066711 | 0.0 | 0.0 | +e9d5f645-4afc-44f4-ae53-bc832c49f451 / -— |
| Jogador 1 | 3-7 | 172 | BUY | STABILIZE | 36.0 | 7 | 6 | 0 | 36.0 | Vanguarda/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15370677411556244 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -— |
| Jogador 1 | 3-7 | 173 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_18_Lux_Fae | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 174 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_18_Lux_Fae | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 175 | PASS | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_18_Lux_Fae | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 181 | BUY | STABILIZE | 36.0 | 7 | 7 | 0 | 36.0 | Vanguarda/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7992251515388489 | 0.0 | 0.0 | +626c50be-ec88-444f-84bb-9b8d41100085 / -— |
| Jogador 1 | 4-1 | 182 | BUY | STABILIZE | 36.0 | 7 | 4 | 0 | 36.0 | Vanguarda/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8330150246620178 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -0c9ac713-08bd-4fa7-a94a-2ab70d7815ff,626c50be-ec88-444f-84bb-9b8d41100085 |
| Jogador 1 | 4-1 | 183 | MOVE_BENCH | STABILIZE | 36.0 | 7 | 1 | 0 | 30.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.40738990902900696 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 184 | CRAFT_AND_EQUIP | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09092347323894501 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 185 | CRAFT_AND_EQUIP | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1182214692234993 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 186 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001297323906328529 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 187 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015214969404041767 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 188 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014882580377161503 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 189 | PASS | STABILIZE | 36.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 191 | BUY | STABILIZE | 24.0 | 7 | 7 | 0 | 36.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2668589949607849 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 1 | 4-2 | 192 | BUY | STABILIZE | 24.0 | 7 | 4 | 0 | 36.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25259730219841003 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 1 | 4-2 | 193 | BUY | STABILIZE | 24.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24795997142791748 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -— |
| Jogador 1 | 4-2 | 194 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 195 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014842416159808636 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 196 | PASS | STABILIZE | 24.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 201 | BUY | ALL_IN | 12.0 | 7 | 6 | 0 | 36.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8226613998413086 | 0.0 | 0.0 | +15c93ffb-d63e-43e6-aa46-ba2beed9cb53 / -— |
| Jogador 1 | 4-3 | 202 | BUY | ALL_IN | 12.0 | 7 | 5 | 0 | 36.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20435009896755219 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 1 | 4-3 | 203 | BUY | ALL_IN | 12.0 | 7 | 1 | 0 | 36.0 | Vanguarda/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037774257361888885 | 0.0 | 0.0 | +677ea844-e1bf-4c68-a0b0-136abb86ba7b / -— |
| Jogador 1 | 4-3 | 204 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002785149961709976 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 205 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 206 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 207 | PASS | ALL_IN | 12.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3124316334724426 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.597818911075592 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.010702039115130901 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25156158208847046 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.25811290740966797 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42424601316452026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.01504808571189642 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2396460771560669 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4013516306877136 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 23 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15446770191192627 | 0.0 | 0.0 | +— / -5a1572b3-8b27-4d87-b885-f342b91c0854 |
| Jogador 2 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.07838590443134308 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -— |
| Jogador 2 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39143693447113037 | 0.0 | 0.0 | +— / -11a1c814-5357-4f19-944f-aa11d6bf8384 |
| Jogador 2 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | -0.0016283477889373899 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.290877404855564e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 28 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37647077441215515 | 0.0 | 0.0 | +— / -046de242-84d0-4f44-a171-345f16a6e719 |
| Jogador 2 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | -0.001893182285130024 | 0.0 | 0.0 | +18770ba0-b5a0-4c41-92a5-de4d5e3078b9 / -— |
| Jogador 2 | 1-4 | 31 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764707699418068 | 0.0 | 0.0 | +— / -18770ba0-b5a0-4c41-92a5-de4d5e3078b9 |
| Jogador 2 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1179685592651367 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -292ef825-d326-4dd8-9c42-c47cfc62116f,94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20823819935321808 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1643960326910019 | 0.0 | 0.0 | +9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 / -— |
| Jogador 2 | 1-4 | 35 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 4.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3837999999523163 | 0.0 | 0.0 | +— / -9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 |
| Jogador 2 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1994355171918869 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 37 | SELL | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39143693447113037 | 0.0 | 0.0 | +— / -9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19924846291542053 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22071923315525055 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.0361746549606323 | 0.0 | 0.0 | +e2e6d682-b207-4a6c-858b-9a3c5c11a38d / -— |
| Jogador 2 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7741261720657349 | 0.0 | 0.0 | +— / -e2e6d682-b207-4a6c-858b-9a3c5c11a38d |
| Jogador 2 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3331805169582367 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2598924934864044 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.22134187817573547 | 0.0 | 0.0 | +18082e05-51e8-4142-b541-c3d7d781b878 / -— |
| Jogador 2 | 2-1 | 46 | SELL | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.409523069858551 | 0.0 | 0.0 | +— / -18082e05-51e8-4142-b541-c3d7d781b878 |
| Jogador 2 | 2-1 | 47 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.35393649339675903 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 48 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.42209944128990173 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.013170243240892887 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.0073522329330444 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -— |
| Jogador 2 | 2-2 | 52 | SELL | STABILIZE | 100.0 | 4 | 10 | 1 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7473446130752563 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 53 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.07328608632087708 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3955386281013489 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3095403015613556 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 56 | PASS | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 61 | SELL | STABILIZE | 100.0 | 4 | 17 | 1 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11232192069292068 | 0.0 | 0.0 | +— / -de00430a-8a57-423c-887c-317d53c2cdd3 |
| Jogador 2 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 4 | 19 | 1 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.13420358300209045 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 16 | 1 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.38130226731300354 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 16 | 1 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6361159682273865 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 65 | PASS | STABILIZE | 100.0 | 4 | 16 | 1 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.020178571343421936 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 71 | SELL | STABILIZE | 100.0 | 4 | 24 | 2 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.30788472294807434 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-4 | 72 | BUY | STABILIZE | 100.0 | 4 | 27 | 2 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.23909690976142883 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 25 | 2 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3017675578594208 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 25 | 2 | 12.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.39584940671920776 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 75 | PASS | STABILIZE | 100.0 | 4 | 25 | 2 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.021785713732242584 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 81 | SELL | STABILIZE | 100.0 | 4 | 33 | 3 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0882553830742836 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-5 | 82 | BUY | STABILIZE | 100.0 | 4 | 35 | 3 | 14.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.37358754873275757 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 83 | SELL | STABILIZE | 100.0 | 4 | 32 | 3 | 14.0 | Vanguarda/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18680158257484436 | 0.0 | 0.0 | +— / -0c15e414-bc67-46de-a087-fb7708db0dfe |
| Jogador 2 | 2-5 | 84 | BUY | STABILIZE | 100.0 | 4 | 35 | 3 | 14.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3720097243785858 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 85 | SELL | STABILIZE | 100.0 | 4 | 32 | 3 | 14.0 | Vanguarda/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.17285723984241486 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-5 | 86 | BUY | STABILIZE | 100.0 | 4 | 35 | 3 | 14.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.055134501308202744 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 2 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 32 | 3 | 14.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3990173041820526 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 88 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 32 | 3 | 16.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11421520262956619 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 89 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 32 | 3 | 16.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12293384224176407 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 91 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 40 | 4 | 16.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5916147232055664 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 92 | BUY | STABILIZE | 94.0 | 5 | 40 | 4 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23049485683441162 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 93 | SELL | STABILIZE | 94.0 | 5 | 37 | 3 | 20.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05277634784579277 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 94 | BUY | STABILIZE | 94.0 | 5 | 40 | 4 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05173226818442345 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 95 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 38 | 3 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004964168183505535 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 38 | 3 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011724689044058323 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 97 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 38 | 3 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6118408441543579 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 98 | PASS | STABILIZE | 94.0 | 5 | 38 | 3 | 18.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03910714387893677 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 101 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 47 | 4 | 18.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33564817905426025 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 102 | SELL | STABILIZE | 94.0 | 5 | 47 | 4 | 18.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026868091896176338 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 2-7 | 103 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 5 | 50 | 5 | 18.0 | Vanguarda/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07476919889450073 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 104 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 5 | 50 | 5 | 18.0 | Vanguarda/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08114210516214371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 105 | BUY | STABILIZE | 94.0 | 5 | 50 | 5 | 18.0 | Vanguarda/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09167913347482681 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 106 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 47 | 4 | 18.0 | Vanguarda/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28328418731689453 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 107 | SELL | STABILIZE | 94.0 | 5 | 47 | 4 | 20.0 | Vanguarda/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01125556044280529 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 2-7 | 108 | BUY | STABILIZE | 94.0 | 5 | 49 | 4 | 20.0 | Vanguarda/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1469602733850479 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 109 | SELL | STABILIZE | 94.0 | 5 | 47 | 4 | 20.0 | Vanguarda/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3218846321105957 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 3-1 | 111 | BUY | STABILIZE | 94.0 | 5 | 58 | 5 | 20.0 | Vanguarda/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.24395938217639923 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 112 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 55 | 5 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2949795424938202 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 113 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 55 | 5 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 114 | PASS | STABILIZE | 94.0 | 5 | 55 | 5 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.15594547986984253 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 121 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 65 | 5 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.30153945088386536 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 122 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 65 | 5 | 20.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.41496995091438293 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 123 | PASS | STABILIZE | 83.0 | 5 | 65 | 5 | 24.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16051417589187622 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 131 | SELL | STABILIZE | 73.0 | 5 | 76 | 5 | 24.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4380433261394501 | 0.0 | 0.0 | +— / -6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 3-3 | 132 | BUY | STABILIZE | 73.0 | 5 | 77 | 5 | 24.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.11762238293886185 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 133 | SELL | STABILIZE | 73.0 | 5 | 74 | 5 | 24.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4175790250301361 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 2 | 3-3 | 134 | BUY | STABILIZE | 73.0 | 5 | 77 | 5 | 24.0 | Vanguarda/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.14416247606277466 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 135 | CRAFT_AND_EQUIP | STABILIZE | 73.0 | 5 | 74 | 5 | 24.0 | Vanguarda/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08394528925418854 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 136 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 74 | 5 | 24.0 | Vanguarda/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11794483661651611 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 137 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 74 | 5 | 24.0 | Vanguarda/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5977826118469238 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 138 | PASS | STABILIZE | 73.0 | 5 | 74 | 5 | 24.0 | Vanguarda/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1649242490530014 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 141 | BUY | STABILIZE | 63.0 | 5 | 85 | 5 | 24.0 | Vanguarda/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9763526320457458 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 142 | MOVE_BENCH | SLOWROLL | 63.0 | 5 | 83 | 5 | 24.0 | Vanguarda/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29879030585289 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 143 | BUY | SLOWROLL | 63.0 | 5 | 83 | 5 | 22.0 | Vanguarda/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9582438468933105 | 0.0 | 0.0 | +a15ff9dc-bf8a-49e0-9893-f92a212263d8 / -2ace989d-3e9e-483b-9b14-cd6b8f171f17,ff0d9869-c346-4210-be85-1e802a25dd8b |
| Jogador 2 | 3-4 | 144 | MOVE_BENCH | SLOWROLL | 63.0 | 5 | 81 | 5 | 14.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06883739680051804 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 145 | MOVE_BENCH | SLOWROLL | 63.0 | 5 | 81 | 5 | 20.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14268717169761658 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 146 | PASS | SLOWROLL | 63.0 | 5 | 81 | 5 | 20.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13697628676891327 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 149 | MOVE_BENCH | SLOWROLL | 63.0 | 5 | 81 | 5 | 20.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5103181004524231 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 151 | BUY | SLOWROLL | 63.0 | 5 | 92 | 5 | 26.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.904078483581543 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 152 | MOVE_BOARD | SLOWROLL | 63.0 | 5 | 91 | 5 | 26.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0027355568017810583 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 153 | SELL | SLOWROLL | 63.0 | 5 | 91 | 5 | 26.0 | Vanguarda/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4747348129749298 | 0.0 | 0.0 | +— / -a15ff9dc-bf8a-49e0-9893-f92a212263d8 |
| Jogador 2 | 3-5 | 154 | SELL | SLOWROLL | 63.0 | 5 | 96 | 5 | 26.0 | Vanguarda/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.748572826385498 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-5 | 155 | BUY | STABILIZE | 63.0 | 5 | 97 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23099835216999054 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 156 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 95 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33883222937583923 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 157 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 95 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41427281498908997 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 158 | PASS | STABILIZE | 63.0 | 5 | 95 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17581187188625336 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 161 | MOVE_BENCH | STABILIZE | 51.0 | 5 | 106 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.054183341562747955 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 162 | BUY | STABILIZE | 51.0 | 5 | 106 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0006554126739502 | 0.0 | 0.0 | +27102740-ce4d-4bec-a9eb-ed936f6bc364 / -— |
| Jogador 2 | 3-6 | 163 | MOVE_BENCH | SLOWROLL | 51.0 | 5 | 103 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26963698863983154 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 164 | MOVE_BENCH | SLOWROLL | 51.0 | 5 | 103 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.414272665977478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 165 | PASS | SLOWROLL | 51.0 | 5 | 103 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1486133635044098 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 171 | BUY | SLOWROLL | 40.0 | 5 | 115 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9489696621894836 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 2 | 3-7 | 172 | MOVE_BENCH | SLOWROLL | 40.0 | 5 | 112 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0558042973279953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 173 | BUY | SLOWROLL | 40.0 | 5 | 112 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9297662973403931 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 2 | 3-7 | 174 | MOVE_BENCH | SLOWROLL | 40.0 | 5 | 111 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3009848892688751 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 175 | MOVE_BENCH | SLOWROLL | 40.0 | 5 | 111 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4098982512950897 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 176 | PASS | SLOWROLL | 40.0 | 5 | 111 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1592027246952057 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 181 | BUY | SLOWROLL | 40.0 | 5 | 123 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2661316692829132 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 2 | 4-1 | 182 | MOVE_BENCH | SLOWROLL | 40.0 | 5 | 120 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07305871695280075 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 183 | CRAFT_AND_EQUIP | SLOWROLL | 40.0 | 5 | 120 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12463437765836716 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 184 | CRAFT_AND_EQUIP | SLOWROLL | 40.0 | 5 | 120 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10186784714460373 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 185 | BUY | SLOWROLL | 40.0 | 5 | 120 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0642513781785965 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 2 | 4-1 | 186 | BUY | SLOWROLL | 40.0 | 5 | 118 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12020020931959152 | 0.0 | 0.0 | +2c153083-6c43-425e-90d5-23f7f2058592 / -— |
| Jogador 2 | 4-1 | 187 | BUY | SLOWROLL | 40.0 | 5 | 116 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07415813207626343 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 2 | 4-1 | 188 | BUY | SLOWROLL | 40.0 | 5 | 115 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26672282814979553 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 2 | 4-1 | 189 | MOVE_BOARD | SLOWROLL | 40.0 | 5 | 114 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.931016064801952e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 191 | MOVE_BENCH | FAST8 | 40.0 | 6 | 125 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4006783962249756 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 192 | BUY | FAST8 | 40.0 | 6 | 125 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0708368718624115 | 0.0 | 0.0 | +506f421d-7a3c-46d7-9cac-6c107bc35e31 / -— |
| Jogador 2 | 4-2 | 193 | REROLL | FAST8 | 40.0 | 6 | 122 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 194 | SELL | FAST8 | 40.0 | 6 | 120 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -b2a77bec-e150-4d98-847c-9f2cfb50cbe7 |
| Jogador 2 | 4-2 | 195 | BUY | FAST8 | 40.0 | 6 | 121 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6517476439476013 | 0.0 | 0.0 | +157648c2-e9b6-4eb2-b42c-19c554a3a41e / -— |
| Jogador 2 | 4-2 | 196 | SELL | FAST8 | 40.0 | 6 | 119 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06558461487293243 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 2 | 4-2 | 197 | BUY | FAST8 | 40.0 | 6 | 120 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14565718173980713 | 0.0 | 0.0 | +e1867f53-f97a-4c7a-bce3-24aa037ce27f / -— |
| Jogador 2 | 4-2 | 198 | REROLL | FAST8 | 40.0 | 6 | 118 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 199 | SELL | FAST8 | 40.0 | 6 | 116 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06466154009103775 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 2 | 4-3 | 201 | BUY | STABILIZE | 28.0 | 6 | 128 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3529137969017029 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 2 | 4-3 | 202 | REROLL | STABILIZE | 28.0 | 6 | 125 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 203 | SELL | STABILIZE | 28.0 | 6 | 123 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14197580516338348 | 0.0 | 0.0 | +— / -157648c2-e9b6-4eb2-b42c-19c554a3a41e |
| Jogador 2 | 4-3 | 204 | BUY | STABILIZE | 28.0 | 6 | 125 | 5 | 30.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9581074714660645 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -43759c90-bd65-4632-8aa4-56ab63ae84fe,8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 2 | 4-3 | 205 | BUY | STABILIZE | 28.0 | 6 | 124 | 5 | 28.0 | Rival/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07374414056539536 | 0.0 | 0.0 | +8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e / -— |
| Jogador 2 | 4-3 | 206 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 122 | 5 | 28.0 | Rival/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042187824845314026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 207 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 122 | 5 | 30.0 | Rival/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3901755213737488 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 208 | BUY | STABILIZE | 28.0 | 6 | 122 | 5 | 34.0 | Rival/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1927882432937622 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 2 | 4-3 | 209 | REROLL | STABILIZE | 28.0 | 6 | 121 | 5 | 34.0 | Rival/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 211 | SELL | STABILIZE | 28.0 | 6 | 130 | 5 | 34.0 | Rival/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12008307874202728 | 0.0 | 0.0 | +— / -b1efce8c-0cb0-47fc-a361-c50a76c0f9de |
| Jogador 2 | 4-4 | 212 | BUY | STABILIZE | 28.0 | 6 | 133 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6616188883781433 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 2 | 4-4 | 213 | SELL | STABILIZE | 28.0 | 6 | 131 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e |
| Jogador 2 | 4-4 | 214 | BUY | STABILIZE | 28.0 | 6 | 133 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6536294221878052 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 2 | 4-4 | 215 | REROLL | STABILIZE | 28.0 | 6 | 131 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 216 | SELL | STABILIZE | 28.0 | 6 | 129 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.133205384016037 | 0.0 | 0.0 | +— / -ded275a3-9551-4816-8112-f0a25524412c |
| Jogador 2 | 4-4 | 217 | BUY | STABILIZE | 28.0 | 6 | 131 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9275672435760498 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -42aa4dc8-e388-40dd-a210-4c59e358afcd,e1867f53-f97a-4c7a-bce3-24aa037ce27f |
| Jogador 2 | 4-4 | 218 | BUY | STABILIZE | 28.0 | 6 | 129 | 5 | 34.0 | Rival/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22507736086845398 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 2 | 4-4 | 219 | BUY | STABILIZE | 28.0 | 6 | 126 | 5 | 34.0 | Rival/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15819956362247467 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 2 | 4-5 | 221 | SELL | STABILIZE | 28.0 | 6 | 133 | 5 | 34.0 | Rival/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09493483603000641 | 0.0 | 0.0 | +— / -6ea982ab-292d-42fc-99e6-d67c89f9f4fe |
| Jogador 2 | 4-5 | 222 | BUY | STABILIZE | 28.0 | 6 | 138 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8843629956245422 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 2 | 4-5 | 223 | REROLL | STABILIZE | 28.0 | 6 | 135 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 224 | SELL | STABILIZE | 28.0 | 6 | 133 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -b0c1aba5-b1bd-48df-abec-19efa8e49d6d |
| Jogador 2 | 4-5 | 225 | BUY | STABILIZE | 28.0 | 6 | 136 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7603204846382141 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 2 | 4-5 | 226 | REROLL | STABILIZE | 28.0 | 6 | 134 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 227 | SELL | STABILIZE | 28.0 | 6 | 132 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 2 | 4-5 | 228 | BUY | STABILIZE | 28.0 | 6 | 135 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24535930156707764 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 2 | 4-5 | 229 | REROLL | STABILIZE | 28.0 | 6 | 131 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 231 | SELL | ALL_IN | 15.0 | 6 | 139 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06853846460580826 | 0.0 | 0.0 | +— / -84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 2 | 4-6 | 232 | BUY | ALL_IN | 15.0 | 6 | 142 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9853833913803101 | 0.0 | 0.0 | +c8706680-2712-4914-b6c0-59bf92a2796d / -cce8de69-f877-4e86-b720-6aea91e68f47,e5f38fbd-826a-4067-a33f-86cf7eb98f30 |
| Jogador 2 | 4-6 | 233 | BUY | ALL_IN | 15.0 | 6 | 140 | 5 | 34.0 | Rival/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18470612168312073 | 0.0 | 0.0 | +99857cfa-b422-4167-bb01-d9fd94a55d88 / -— |
| Jogador 2 | 4-6 | 234 | BUY | ALL_IN | 15.0 | 6 | 136 | 5 | 34.0 | Rival/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5652244091033936 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 2 | 4-6 | 235 | REROLL | ALL_IN | 15.0 | 6 | 133 | 5 | 34.0 | Rival/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 236 | REROLL | ALL_IN | 15.0 | 6 | 131 | 5 | 34.0 | Rival/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 237 | REROLL | ALL_IN | 15.0 | 6 | 129 | 5 | 34.0 | Rival/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 238 | REROLL | ALL_IN | 15.0 | 6 | 127 | 5 | 34.0 | Rival/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 239 | REROLL | ALL_IN | 15.0 | 6 | 125 | 5 | 34.0 | Rival/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 241 | SELL | ALL_IN | 15.0 | 6 | 134 | 5 | 34.0 | Rival/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11890153586864471 | 0.0 | 0.0 | +— / -c8706680-2712-4914-b6c0-59bf92a2796d |
| Jogador 2 | 4-7 | 242 | BUY | ALL_IN | 15.0 | 6 | 139 | 5 | 34.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.004529356956482 | 0.0 | 0.0 | +edd2748e-d629-4a8a-8174-4c1ef3f5f852 / -27102740-ce4d-4bec-a9eb-ed936f6bc364,4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 4-7 | 243 | BUY | ALL_IN | 15.0 | 6 | 136 | 5 | 28.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14043743908405304 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -— |
| Jogador 2 | 4-7 | 244 | MOVE_BENCH | ALL_IN | 15.0 | 6 | 133 | 5 | 28.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20042474567890167 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 245 | MOVE_BENCH | ALL_IN | 15.0 | 6 | 133 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24587078392505646 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 246 | PASS | ALL_IN | 15.0 | 6 | 133 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2444341778755188 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 249 | MOVE_BENCH | ALL_IN | 15.0 | 6 | 133 | 5 | 24.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5294469594955444 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 251 | BUY | ALL_IN | 15.0 | 6 | 143 | 5 | 32.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4200741648674011 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -— |
| Jogador 2 | 5-1 | 252 | CRAFT_AND_EQUIP | ALL_IN | 15.0 | 6 | 140 | 5 | 32.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09908410161733627 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 253 | CRAFT_AND_EQUIP | ALL_IN | 15.0 | 6 | 140 | 5 | 32.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.0991600751876831 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 254 | REROLL | ALL_IN | 15.0 | 6 | 140 | 5 | 32.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 255 | SELL | ALL_IN | 15.0 | 6 | 138 | 5 | 32.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05392776057124138 | 0.0 | 0.0 | +— / -506f421d-7a3c-46d7-9cac-6c107bc35e31 |
| Jogador 2 | 5-1 | 256 | BUY | ALL_IN | 15.0 | 6 | 141 | 5 | 32.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0076625347137451 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -729ccd5b-adc5-4bca-9523-dcb532e93ecb,bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 2 | 5-1 | 257 | BUY | ALL_IN | 15.0 | 6 | 138 | 5 | 26.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9864208102226257 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -217a3ebb-1953-4f1e-bfdd-a3c9438e791e,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 5-1 | 258 | BUY | ALL_IN | 15.0 | 6 | 135 | 5 | 20.0 | Rival/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17084741592407227 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -— |
| Jogador 2 | 5-1 | 259 | MOVE_BENCH | ALL_IN | 15.0 | 6 | 133 | 5 | 20.0 | Rival/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16566209495067596 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3026348650455475 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5972556471824646 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | -0.0104712825268507 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.038241982460022 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 12 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3872276842594147 | 0.0 | 0.0 | +— / -bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1454828530550003 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17799420654773712 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.061160679906606674 | 0.0 | 0.0 | +54a7d128-a897-4695-8240-9583c367fe28 / -— |
| Jogador 3 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.405935674905777 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.015159313566982746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10469050705432892 | 0.0 | 0.0 | +405de1b8-45c1-4b7f-b044-f12b819507c3 / -— |
| Jogador 3 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3634546995162964 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 23 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007584615610539913 | 0.0 | 0.0 | +— / -54a7d128-a897-4695-8240-9583c367fe28 |
| Jogador 3 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, MOVE_BOARD, PASS | True | True | 0.3205741047859192 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28967076539993286 | 0.0 | 0.0 | +— / -5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, MOVE_BOARD, PASS | True | True | 0.3205741047859192 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -— |
| Jogador 3 | 1-3 | 27 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28967076539993286 | 0.0 | 0.0 | +— / -8a384047-bcc4-4d79-8896-30170e9313cd |
| Jogador 3 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, MOVE_BOARD, PASS | True | True | 0.3205741047859192 | 0.0 | 0.0 | +477d3aa4-2130-4a0e-8254-2688ac860569 / -— |
| Jogador 3 | 1-3 | 29 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28967076539993286 | 0.0 | 0.0 | +— / -477d3aa4-2130-4a0e-8254-2688ac860569 |
| Jogador 3 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28437772393226624 | 0.0 | 0.0 | +d15ca853-2585-49d0-9d7f-339dae104062 / -— |
| Jogador 3 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04115734249353409 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10164615511894226 | 0.0 | 0.0 | +— / -405de1b8-45c1-4b7f-b044-f12b819507c3 |
| Jogador 3 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17497596144676208 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 35 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10164615511894226 | 0.0 | 0.0 | +— / -ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 3 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16508683562278748 | 0.0 | 0.0 | +1ae45649-74e3-49be-bdb6-0d9f38e396ab / -— |
| Jogador 3 | 1-4 | 37 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0042307693511247635 | 0.0 | 0.0 | +— / -1ae45649-74e3-49be-bdb6-0d9f38e396ab |
| Jogador 3 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.18262557685375214 | 0.0 | 0.0 | +e0d7b71a-2c4b-4907-b11d-4c25d39fe3d0 / -— |
| Jogador 3 | 1-4 | 39 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09143692255020142 | 0.0 | 0.0 | +— / -e0d7b71a-2c4b-4907-b11d-4c25d39fe3d0 |
| Jogador 3 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.0200796127319336 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 43 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.029831059277057648 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 44 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 51 | BUY | STABILIZE | 95.0 | 4 | 11 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.035409688949585 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -c70251e8-af44-4466-808f-d49e9e5f57e9,d15ca853-2585-49d0-9d7f-339dae104062 |
| Jogador 3 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 9 | 0 | 4.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.29126134514808655 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 53 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.2380194216966629 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3913504183292389 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5461840033531189 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 56 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 4 | 6 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.2016870528459549 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 57 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 4 | 6 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.12264402210712433 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 58 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17816667258739471 | 0.0 | 0.0 | +1ced81e2-6b0b-4414-85f0-a630c56c0fe0 / -— |
| Jogador 3 | 2-2 | 59 | SELL | STABILIZE | 95.0 | 4 | 4 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4055931270122528 | 0.0 | 0.0 | +— / -1ced81e2-6b0b-4414-85f0-a630c56c0fe0 |
| Jogador 3 | 2-3 | 61 | BUY | STABILIZE | 89.0 | 4 | 12 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.018663348630070686 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 3 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 9 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7416631579399109 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 63 | SELL | STABILIZE | 89.0 | 4 | 9 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02319076843559742 | 0.0 | 0.0 | +— / -8a68772c-3f02-4f2e-882b-4fa69fbb6750 |
| Jogador 3 | 2-3 | 64 | EQUIP_FROM_INVENTORY | STABILIZE | 89.0 | 4 | 12 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1187480241060257 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 65 | EQUIP_FROM_INVENTORY | STABILIZE | 89.0 | 4 | 12 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06228872016072273 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 66 | BUY | STABILIZE | 89.0 | 4 | 12 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27285096049308777 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 67 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 10 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.9219978639739566e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 10 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047352876514196396 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 69 | SELL | STABILIZE | 89.0 | 4 | 10 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053033497184515 | 0.0 | 0.0 | +— / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef |
| Jogador 3 | 2-4 | 71 | BUY | LOSS_STREAK | 83.0 | 4 | 18 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15285111963748932 | 0.0 | 0.0 | +4c8a9a18-68d8-4672-a96d-bb09816257dc / -— |
| Jogador 3 | 2-4 | 72 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03350994735956192 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 73 | SELL | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015936795622110367 | 0.0 | 0.0 | +— / -41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 2-4 | 74 | BUY | LOSS_STREAK | 83.0 | 4 | 17 | 1 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9434505701065063 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 75 | SELL | LOSS_STREAK | 83.0 | 4 | 16 | 1 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4622842073440552 | 0.0 | 0.0 | +— / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63 |
| Jogador 3 | 2-4 | 76 | BUY | LOSS_STREAK | 83.0 | 4 | 17 | 1 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06644584238529205 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 77 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 14 | 1 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05135895684361458 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 78 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 14 | 1 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01491693127900362 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 79 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 14 | 1 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014823036268353462 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 81 | SELL | LOSS_STREAK | 83.0 | 4 | 21 | 2 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01703076995909214 | 0.0 | 0.0 | +— / -4c8a9a18-68d8-4672-a96d-bb09816257dc |
| Jogador 3 | 2-5 | 82 | BUY | LOSS_STREAK | 83.0 | 4 | 24 | 2 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3415301740169525 | 0.0 | 0.0 | +226a1062-8e9a-4652-9da7-a2f215fa46ae / -— |
| Jogador 3 | 2-5 | 83 | SELL | STABILIZE | 83.0 | 4 | 22 | 2 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.530467689037323 | 0.0 | 0.0 | +— / -226a1062-8e9a-4652-9da7-a2f215fa46ae |
| Jogador 3 | 2-5 | 84 | BUY | STABILIZE | 83.0 | 4 | 24 | 2 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35267820954322815 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 85 | SELL | STABILIZE | 83.0 | 4 | 21 | 2 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1520276963710785 | 0.0 | 0.0 | +— / -cdb48eea-209d-4833-9a68-79df61990332 |
| Jogador 3 | 2-5 | 86 | BUY | STABILIZE | 83.0 | 4 | 24 | 2 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.401398241519928 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 87 | BUY_XP | STABILIZE | 83.0 | 4 | 23 | 2 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032784998416900635 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 88 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 19 | 1 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5740097761154175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 89 | BUY | SLOWROLL | 83.0 | 5 | 19 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08737070113420486 | 0.0 | 0.0 | +492fa74a-22b8-4f7d-a4f9-346fdcf565be / -— |
| Jogador 3 | 2-6 | 91 | SELL | SLOWROLL | 83.0 | 5 | 25 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31968632340431213 | 0.0 | 0.0 | +— / -492fa74a-22b8-4f7d-a4f9-346fdcf565be |
| Jogador 3 | 2-6 | 92 | BUY | SLOWROLL | 83.0 | 5 | 26 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3397983908653259 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 93 | SELL | SLOWROLL | 83.0 | 5 | 24 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5012723803520203 | 0.0 | 0.0 | +— / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 |
| Jogador 3 | 2-6 | 94 | BUY | SLOWROLL | 83.0 | 5 | 26 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9728262424468994 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -— |
| Jogador 3 | 2-6 | 95 | SELL | SLOWROLL | 83.0 | 5 | 25 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8475771546363831 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 2-6 | 96 | BUY | SLOWROLL | 83.0 | 5 | 26 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.031397681683301926 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 3 | 2-6 | 97 | SELL | SLOWROLL | 83.0 | 5 | 24 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3209100663661957 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 3 | 2-6 | 98 | BUY | SLOWROLL | 83.0 | 5 | 26 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.024923933669924736 | 0.0 | 0.0 | +14bbd76c-fca8-4017-89b5-e586bb1cae70 / -— |
| Jogador 3 | 2-6 | 99 | SELL | SLOWROLL | 83.0 | 5 | 25 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31960490345954895 | 0.0 | 0.0 | +— / -14bbd76c-fca8-4017-89b5-e586bb1cae70 |
| Jogador 3 | 2-7 | 101 | BUY | SLOWROLL | 77.0 | 5 | 33 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3396332561969757 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 102 | SELL | SLOWROLL | 77.0 | 5 | 31 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5001336336135864 | 0.0 | 0.0 | +— / -bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 3 | 2-7 | 103 | BUY | SLOWROLL | 77.0 | 5 | 33 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9735890626907349 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 104 | SELL | SLOWROLL | 77.0 | 5 | 32 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8481477499008179 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 2-7 | 105 | BUY | SLOWROLL | 77.0 | 5 | 33 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2129048854112625 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 106 | MOVE_BENCH | SLOWROLL | 77.0 | 5 | 30 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39333418011665344 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 107 | SELL | SLOWROLL | 77.0 | 5 | 30 | 3 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18975500762462616 | 0.0 | 0.0 | +— / -d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-7 | 108 | BUY | SLOWROLL | 77.0 | 5 | 31 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19191190600395203 | 0.0 | 0.0 | +60c8a84d-7243-462c-a452-5901135c78b8 / -— |
| Jogador 3 | 2-7 | 109 | MOVE_BOARD | SLOWROLL | 77.0 | 5 | 29 | 2 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 111 | SELL | SLOWROLL | 77.0 | 5 | 36 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10035913437604904 | 0.0 | 0.0 | +— / -60c8a84d-7243-462c-a452-5901135c78b8 |
| Jogador 3 | 3-1 | 112 | BUY | SLOWROLL | 77.0 | 5 | 38 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.11652056127786636 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 113 | SELL | SLOWROLL | 77.0 | 5 | 35 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.32232561707496643 | 0.0 | 0.0 | +— / -c3f8419e-a450-4247-bb65-8de8dba1c8ee |
| Jogador 3 | 3-1 | 114 | BUY | SLOWROLL | 77.0 | 5 | 38 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.575536847114563 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-1 | 115 | CRAFT_AND_EQUIP | SLOWROLL | 77.0 | 5 | 37 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2170610874891281 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 116 | MOVE_BOARD | SLOWROLL | 77.0 | 5 | 37 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.069018177688122e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 117 | MOVE_BOARD | SLOWROLL | 77.0 | 5 | 37 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01502174325287342 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 118 | BUY_XP | SLOWROLL | 77.0 | 5 | 37 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 119 | BUY_XP | SLOWROLL | 77.0 | 5 | 33 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 121 | SELL | SLOWROLL | 66.0 | 5 | 37 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42827045917510986 | 0.0 | 0.0 | +— / -2fa86b11-4e28-4652-890e-f00a79068223 |
| Jogador 3 | 3-2 | 122 | BUY | SLOWROLL | 66.0 | 5 | 38 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.05701075866818428 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 123 | SELL | SLOWROLL | 66.0 | 5 | 35 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3923495411872864 | 0.0 | 0.0 | +— / -6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 |
| Jogador 3 | 3-2 | 124 | BUY | SLOWROLL | 66.0 | 5 | 38 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.030966149643063545 | 0.0 | 0.0 | +fd3ab6e7-a3e5-4a03-8aa6-a80f6c0c1f47 / -— |
| Jogador 3 | 3-2 | 125 | BUY_XP | SLOWROLL | 66.0 | 5 | 36 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06571000069379807 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 126 | MOVE_BENCH | FAST8 | 66.0 | 6 | 32 | 3 | 28.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4026346206665039 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 127 | BUY | FAST8 | 66.0 | 6 | 32 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5580959320068359 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -— |
| Jogador 3 | 3-2 | 128 | BUY_XP | FAST8 | 66.0 | 6 | 31 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044319998472929 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 129 | BUY_XP | FAST8 | 66.0 | 6 | 27 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035679999738931656 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 131 | BUY | FAST8 | 54.0 | 6 | 31 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1763862818479538 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-3 | 132 | BUY | FAST8 | 54.0 | 6 | 29 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23441335558891296 | 0.0 | 0.0 | +ffdee27e-2d30-40b5-9937-92be68ab1390 / -— |
| Jogador 3 | 3-3 | 133 | MOVE_BOARD | FAST8 | 54.0 | 6 | 27 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 134 | MOVE_BOARD | FAST8 | 54.0 | 6 | 27 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014967722818255424 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 135 | PASS | FAST8 | 54.0 | 6 | 27 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0794999971985817 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 141 | BUY | FAST8 | 43.0 | 6 | 35 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6406590342521667 | 0.0 | 0.0 | +fe8191d8-bc21-499a-aff7-31c3ca9b2e64 / -— |
| Jogador 3 | 3-4 | 142 | BUY | FAST8 | 43.0 | 6 | 33 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1398974359035492 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 143 | BUY | FAST8 | 43.0 | 6 | 30 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1495453268289566 | 0.0 | 0.0 | +c2c83d3a-8db0-4a0f-a896-4227c10a8d6a / -— |
| Jogador 3 | 3-4 | 144 | MOVE_BOARD | FAST8 | 43.0 | 6 | 28 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.316553041571751e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 145 | MOVE_BOARD | FAST8 | 43.0 | 6 | 28 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01481221430003643 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 146 | PASS | FAST8 | 43.0 | 6 | 28 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0814933329820633 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 151 | BUY | FAST8 | 43.0 | 6 | 36 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7568293213844299 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -— |
| Jogador 3 | 3-5 | 152 | BUY | FAST8 | 43.0 | 6 | 34 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05588756874203682 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 3 | 3-5 | 153 | BUY | FAST8 | 43.0 | 6 | 31 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28794676065444946 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 154 | REROLL | FAST8 | 43.0 | 6 | 27 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 155 | SELL | FAST8 | 43.0 | 6 | 25 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13060544431209564 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 3-5 | 156 | BUY | FAST8 | 43.0 | 6 | 26 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7457488179206848 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 3 | 3-5 | 157 | SELL | FAST8 | 43.0 | 6 | 24 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05992106348276138 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-5 | 158 | BUY | FAST8 | 43.0 | 6 | 27 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7794656753540039 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -65a6d68c-90ae-4e31-8bbc-82e8ec75b3de,ffdee27e-2d30-40b5-9937-92be68ab1390 |
| Jogador 3 | 3-5 | 159 | BUY | FAST8 | 43.0 | 6 | 25 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022745082154870033 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 3 | 3-6 | 161 | BUY | STABILIZE | 32.0 | 6 | 31 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0576803982257843 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -— |
| Jogador 3 | 3-6 | 162 | SELL | STABILIZE | 32.0 | 6 | 28 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08482769131660461 | 0.0 | 0.0 | +— / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 |
| Jogador 3 | 3-6 | 163 | BUY | STABILIZE | 32.0 | 6 | 33 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3052435517311096 | 0.0 | 0.0 | +f722cd46-0c4e-42e7-80ff-4b910c28d572 / -— |
| Jogador 3 | 3-6 | 164 | REROLL | STABILIZE | 32.0 | 6 | 32 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 165 | SELL | STABILIZE | 32.0 | 6 | 30 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05973559245467186 | 0.0 | 0.0 | +— / -320038b5-88c4-48fe-a7fa-a30823d674c0 |
| Jogador 3 | 3-6 | 166 | BUY | STABILIZE | 32.0 | 6 | 33 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6272006034851074 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 3 | 3-6 | 167 | SELL | STABILIZE | 32.0 | 6 | 30 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1361304521560669 | 0.0 | 0.0 | +— / -fe8191d8-bc21-499a-aff7-31c3ca9b2e64 |
| Jogador 3 | 3-6 | 168 | BUY | STABILIZE | 32.0 | 6 | 32 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16669751703739166 | 0.0 | 0.0 | +813260b6-a1b8-4a5c-978e-acd60b6b1082 / -— |
| Jogador 3 | 3-6 | 169 | REROLL | STABILIZE | 32.0 | 6 | 28 | 2 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 171 | SELL | STABILIZE | 20.0 | 6 | 36 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15709230303764343 | 0.0 | 0.0 | +— / -ccdd8153-af58-4fe7-994c-d49f0a7a17f8 |
| Jogador 3 | 3-7 | 172 | BUY | STABILIZE | 20.0 | 6 | 40 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8015919327735901 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 3 | 3-7 | 173 | SELL | STABILIZE | 20.0 | 6 | 37 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1305384635925293 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 3 | 3-7 | 174 | BUY | STABILIZE | 20.0 | 6 | 40 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06988770514726639 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 3 | 3-7 | 175 | REROLL | STABILIZE | 20.0 | 6 | 37 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 176 | SELL | STABILIZE | 20.0 | 6 | 35 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05976923182606697 | 0.0 | 0.0 | +— / -665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 3 | 3-7 | 177 | BUY | STABILIZE | 20.0 | 6 | 38 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8269783854484558 | 0.0 | 0.0 | +5637ca02-9946-4d1a-9679-e5c316ef566b / -— |
| Jogador 3 | 3-7 | 178 | REROLL | STABILIZE | 20.0 | 6 | 36 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 179 | SELL | STABILIZE | 20.0 | 6 | 34 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07556378096342087 | 0.0 | 0.0 | +— / -f722cd46-0c4e-42e7-80ff-4b910c28d572 |
| Jogador 3 | 4-1 | 181 | BUY | STABILIZE | 20.0 | 6 | 46 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.17954888939857483 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 3 | 4-1 | 182 | CRAFT_AND_EQUIP | STABILIZE | 20.0 | 6 | 43 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07062031328678131 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 183 | CRAFT_AND_EQUIP | STABILIZE | 20.0 | 6 | 43 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13847698271274567 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 184 | REROLL | STABILIZE | 20.0 | 6 | 43 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 185 | SELL | STABILIZE | 20.0 | 6 | 41 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0737999975681305 | 0.0 | 0.0 | +— / -6fa83356-562b-4a26-a77d-3e989089e70a |
| Jogador 3 | 4-1 | 186 | BUY | STABILIZE | 20.0 | 6 | 44 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14001183211803436 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 3 | 4-1 | 187 | REROLL | STABILIZE | 20.0 | 6 | 41 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 188 | SELL | STABILIZE | 20.0 | 6 | 39 | 3 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13992498815059662 | 0.0 | 0.0 | +— / -f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 3 | 4-1 | 189 | BUY | STABILIZE | 20.0 | 6 | 42 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3355882167816162 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 3 | 4-2 | 191 | SELL | ALL_IN | 10.0 | 6 | 53 | 5 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07757136970758438 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 3 | 4-2 | 192 | BUY | ALL_IN | 10.0 | 6 | 54 | 5 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0262219905853271 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -4518ad1d-87e7-4110-830a-96183c533201,f0b6c16b-7610-454c-929d-7152f0a041d3 |
| Jogador 3 | 4-2 | 193 | BUY | ALL_IN | 10.0 | 6 | 52 | 5 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44489622116088867 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 3 | 4-2 | 194 | BUY | ALL_IN | 10.0 | 6 | 49 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3838272988796234 | 0.0 | 0.0 | +7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed / -— |
| Jogador 3 | 4-2 | 195 | REROLL | ALL_IN | 10.0 | 6 | 48 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 196 | SELL | ALL_IN | 10.0 | 6 | 46 | 4 | 32.0 | Vanguarda/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18322481215000153 | 0.0 | 0.0 | +— / -7b3e8122-3b51-46b5-94a8-68fb77156e0e |
| Jogador 3 | 4-2 | 197 | BUY | ALL_IN | 10.0 | 6 | 51 | 5 | 32.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8625158071517944 | 0.0 | 0.0 | +30d2995a-d9b8-4424-af46-8766734e440c / -29f10cb7-6575-47ca-b583-057992a08253,3bbd7105-b508-437d-ac84-11e01a499779 |
| Jogador 3 | 4-2 | 198 | BUY | ALL_IN | 10.0 | 6 | 48 | 4 | 26.0 | Vanguarda/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012923536822199821 | 0.0 | 0.0 | +d974e68a-e978-4335-8827-a94a9219be58 / -— |
| Jogador 3 | 4-2 | 199 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 45 | 4 | 26.0 | Vanguarda/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40186047554016113 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +1903eae4-bd37-4ed8-bbae-28177e859592 / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.010813108645379543 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1957342028617859 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 12 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12328261137008667 | 0.0 | 0.0 | +— / -95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09774187207221985 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.160903662443161 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0407843217253685 | 0.0 | 0.0 | +75da0978-cc05-4bcc-aefd-fb265a4c80c3 / -— |
| Jogador 4 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40239015221595764 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.015150077641010284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0143970251083374 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3305138349533081 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2602514624595642 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 24 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12129109352827072 | 0.0 | 0.0 | +— / -a19fc47b-fc81-49b2-bc25-d25d58b8deef |
| Jogador 4 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.15608324110507965 | 0.0 | 0.0 | +3224c4b3-14ed-42e7-a497-24e0be0a691c / -— |
| Jogador 4 | 1-3 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05123443529009819 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 27 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025461537763476372 | 0.0 | 0.0 | +— / -75da0978-cc05-4bcc-aefd-fb265a4c80c3 |
| Jogador 4 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Alistar | BUY, MOVE_BOARD, PASS | True | True | 0.1910124123096466 | 0.0 | 0.0 | +e21ea220-ea66-4430-93a5-5b248b0f2b0b / -— |
| Jogador 4 | 1-3 | 29 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33284616470336914 | 0.0 | 0.0 | +— / -e21ea220-ea66-4430-93a5-5b248b0f2b0b |
| Jogador 4 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0396888256072998 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4317445158958435 | 0.0 | 0.0 | +— / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793 |
| Jogador 4 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0396850109100342 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 34 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4315151870250702 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0366395711898804 | 0.0 | 0.0 | +b29f76e2-456d-4abf-b9a2-a4a80b577187 / -— |
| Jogador 4 | 1-4 | 36 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3854424059391022 | 0.0 | 0.0 | +— / -b29f76e2-456d-4abf-b9a2-a4a80b577187 |
| Jogador 4 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08870601654052734 | 0.0 | 0.0 | +df71e10d-846b-4b12-8eb4-53633834303f / -— |
| Jogador 4 | 1-4 | 38 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -df71e10d-846b-4b12-8eb4-53633834303f |
| Jogador 4 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24785339832305908 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 2-1 | 41 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3432724177837372 | 0.0 | 0.0 | +— / -4fbb2e46-1524-47c6-85a1-79266fd4da28 |
| Jogador 4 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.036878228187561 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 43 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7907135486602783 | 0.0 | 0.0 | +— / -0e9aa759-0538-4168-a523-02a5f8e09e0a |
| Jogador 4 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.25255244970321655 | 0.0 | 0.0 | +c05579e6-aa73-434f-8a91-c58d68a81ced / -— |
| Jogador 4 | 2-1 | 45 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.41982537508010864 | 0.0 | 0.0 | +— / -c05579e6-aa73-434f-8a91-c58d68a81ced |
| Jogador 4 | 2-1 | 46 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.2530626058578491 | 0.0 | 0.0 | +9819422b-1f51-47b5-89b7-9d6e906ddff2 / -— |
| Jogador 4 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20119352638721466 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1608915477991104 | 0.0 | 0.0 | +838eb81f-88a4-41a2-b2e5-7d6784d86773 / -— |
| Jogador 4 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1585528552532196 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 51 | SELL | STABILIZE | 100.0 | 4 | 11 | 1 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3254615366458893 | 0.0 | 0.0 | +— / -838eb81f-88a4-41a2-b2e5-7d6784d86773 |
| Jogador 4 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1974194496870041 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07547714561223984 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 54 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06790485233068466 | 0.0 | 0.0 | +— / -9819422b-1f51-47b5-89b7-9d6e906ddff2 |
| Jogador 4 | 2-2 | 55 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.09645206481218338 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 56 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.03909876197576523 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.0830952450633049 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.362922896281816e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08508752286434174 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 61 | SELL | STABILIZE | 100.0 | 4 | 17 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025410855188965797 | 0.0 | 0.0 | +— / -9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0380244255065918 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 63 | SELL | STABILIZE | 100.0 | 4 | 17 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5099048614501953 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 64 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20117060840129852 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 65 | SELL | STABILIZE | 100.0 | 4 | 16 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.325307697057724 | 0.0 | 0.0 | +— / -9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 4 | 2-3 | 66 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31810542941093445 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -— |
| Jogador 4 | 2-3 | 67 | SELL | STABILIZE | 100.0 | 4 | 17 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3681054413318634 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 68 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20086568593978882 | 0.0 | 0.0 | +e98ea24f-414b-4ccd-a19a-d98965ccc21c / -— |
| Jogador 4 | 2-3 | 69 | BUY_XP | STABILIZE | 100.0 | 4 | 17 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 71 | SELL | STABILIZE | 95.0 | 5 | 19 | 1 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2508656978607178 | 0.0 | 0.0 | +— / -e98ea24f-414b-4ccd-a19a-d98965ccc21c |
| Jogador 4 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 20 | 2 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13814356923103333 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 16 | 1 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33742988109588623 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 74 | SELL | STABILIZE | 95.0 | 5 | 16 | 1 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0016769231297075748 | 0.0 | 0.0 | +— / -e989a0cc-848a-4c45-b153-315877aee8f7 |
| Jogador 4 | 2-4 | 75 | BUY | STABILIZE | 95.0 | 5 | 18 | 1 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3264455795288086 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 76 | SELL | STABILIZE | 95.0 | 5 | 16 | 1 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06794845312833786 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 77 | BUY | STABILIZE | 95.0 | 5 | 18 | 1 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.33037784695625305 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 78 | SELL | STABILIZE | 95.0 | 5 | 17 | 1 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07050769031047821 | 0.0 | 0.0 | +— / -8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-4 | 79 | BUY | STABILIZE | 95.0 | 5 | 18 | 1 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.33035752177238464 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 81 | SELL | STABILIZE | 95.0 | 5 | 23 | 2 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07050769031047821 | 0.0 | 0.0 | +— / -86c535a4-a22b-4667-bc0f-46b4843d97cc |
| Jogador 4 | 2-5 | 82 | BUY | STABILIZE | 95.0 | 5 | 24 | 2 | 20.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0350786447525024 | 0.0 | 0.0 | +3825a7ba-319f-48f8-ad2d-8c24eabbc1cc / -— |
| Jogador 4 | 2-5 | 83 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 21 | 2 | 20.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08406547456979752 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 84 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 21 | 2 | 18.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38703522086143494 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 85 | BUY | SLOWROLL | 95.0 | 5 | 21 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23695991933345795 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 86 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 18 | 1 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00016219612734857947 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 87 | SELL | SLOWROLL | 95.0 | 5 | 18 | 1 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11536592245101929 | 0.0 | 0.0 | +— / -a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 2-5 | 88 | BUY | SLOWROLL | 95.0 | 5 | 21 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29498806595802307 | 0.0 | 0.0 | +a72d427f-f2f7-46dd-97bf-d28999772db0 / -— |
| Jogador 4 | 2-5 | 89 | BUY_XP | SLOWROLL | 95.0 | 5 | 20 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 91 | SELL | SLOWROLL | 95.0 | 5 | 23 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0588039793074131 | 0.0 | 0.0 | +— / -a72d427f-f2f7-46dd-97bf-d28999772db0 |
| Jogador 4 | 2-6 | 92 | BUY | SLOWROLL | 95.0 | 5 | 24 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28446486592292786 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 93 | SELL | SLOWROLL | 95.0 | 5 | 21 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16611993312835693 | 0.0 | 0.0 | +— / -b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 2-6 | 94 | BUY | SLOWROLL | 95.0 | 5 | 24 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08304176479578018 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 95 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 22 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002962826984003186 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 96 | SELL | SLOWROLL | 95.0 | 5 | 22 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33674341440200806 | 0.0 | 0.0 | +— / -f71a7192-663d-46a0-93ef-b900c59c3bde |
| Jogador 4 | 2-6 | 97 | BUY | SLOWROLL | 95.0 | 5 | 24 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24554499983787537 | 0.0 | 0.0 | +4709c817-7def-40f8-9dae-baa913e0fc07 / -— |
| Jogador 4 | 2-6 | 98 | BUY_XP | SLOWROLL | 95.0 | 5 | 23 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 99 | BUY_XP | SLOWROLL | 95.0 | 5 | 19 | 1 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 101 | SELL | SLOWROLL | 95.0 | 5 | 23 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09990766644477844 | 0.0 | 0.0 | +— / -4709c817-7def-40f8-9dae-baa913e0fc07 |
| Jogador 4 | 2-7 | 102 | BUY | SLOWROLL | 95.0 | 5 | 24 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9379035234451294 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -— |
| Jogador 4 | 2-7 | 103 | SELL | SLOWROLL | 95.0 | 5 | 23 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37754377722740173 | 0.0 | 0.0 | +— / -764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 4 | 2-7 | 104 | BUY | SLOWROLL | 95.0 | 5 | 24 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.023971624672412872 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 105 | BUY_XP | SLOWROLL | 95.0 | 5 | 21 | 2 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045910000801086426 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 106 | MOVE_BENCH | FAST8 | 95.0 | 6 | 17 | 1 | 26.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3968970775604248 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 107 | MOVE_BENCH | FAST8 | 95.0 | 6 | 17 | 1 | 28.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4451102912425995 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 108 | BUY | FAST8 | 95.0 | 6 | 17 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2286151796579361 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 4 | 2-7 | 109 | BUY_XP | FAST8 | 95.0 | 6 | 16 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 111 | SELL | FAST8 | 95.0 | 6 | 19 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02855786681175232 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 4 | 3-1 | 112 | BUY | FAST8 | 95.0 | 6 | 20 | 2 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.6653807163238525 | 0.0 | 0.0 | +6bbf1aa9-e129-45c6-8668-699425d97c5d / -— |
| Jogador 4 | 3-1 | 113 | CRAFT_AND_EQUIP | FAST8 | 95.0 | 6 | 18 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1641761213541031 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 114 | SELL | FAST8 | 95.0 | 6 | 18 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30200061202049255 | 0.0 | 0.0 | +— / -6bbf1aa9-e129-45c6-8668-699425d97c5d |
| Jogador 4 | 3-1 | 115 | BUY | FAST8 | 95.0 | 6 | 20 | 2 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08206333965063095 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 116 | BUY_XP | FAST8 | 95.0 | 6 | 18 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 117 | BUY_XP | FAST8 | 95.0 | 6 | 14 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 118 | BUY_XP | FAST8 | 95.0 | 6 | 10 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 119 | BUY_XP | FAST8 | 95.0 | 6 | 6 | 0 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 121 | SELL | FAST8 | 95.0 | 6 | 9 | 0 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02581522800028324 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-2 | 122 | BUY | FAST8 | 95.0 | 6 | 11 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11953942477703094 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 123 | MOVE_BOARD | FAST8 | 95.0 | 6 | 8 | 0 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 124 | MOVE_BOARD | FAST8 | 95.0 | 6 | 8 | 0 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 125 | PASS | FAST8 | 95.0 | 6 | 8 | 0 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 131 | BUY | FAST8 | 95.0 | 6 | 15 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16900381445884705 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 132 | BUY | FAST8 | 95.0 | 6 | 12 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7171851992607117 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 133 | MOVE_BOARD | FAST8 | 95.0 | 6 | 11 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.104090036591515e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 134 | BUY_XP | FAST8 | 95.0 | 6 | 11 | 1 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 135 | BUY_XP | FAST8 | 95.0 | 6 | 7 | 0 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 136 | MOVE_BENCH | FAST8 | 95.0 | 7 | 3 | 0 | 32.0 | Lutador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4233829379081726 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 137 | MOVE_BOARD | FAST8 | 95.0 | 7 | 3 | 0 | 38.0 | Lutador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015359836630523205 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 138 | MOVE_BOARD | FAST8 | 95.0 | 7 | 3 | 0 | 38.0 | Lutador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 139 | MOVE_BOARD | FAST8 | 95.0 | 7 | 3 | 0 | 38.0 | Lutador/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999260194599628 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 141 | BUY | FAST8 | 95.0 | 7 | 11 | 1 | 38.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48776566982269287 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 142 | BUY | FAST8 | 95.0 | 7 | 8 | 0 | 38.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7625528573989868 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -1903eae4-bd37-4ed8-bbae-28177e859592,ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 3-4 | 143 | MOVE_BENCH | FAST8 | 95.0 | 7 | 7 | 0 | 36.0 | Lutador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4037748873233795 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 144 | BUY_XP | FAST8 | 95.0 | 7 | 7 | 0 | 42.0 | Lutador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 145 | BUY | FAST8 | 95.0 | 7 | 3 | 0 | 42.0 | Lutador/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0775502398610115 | 0.0 | 0.0 | +e01be6cf-34fe-4057-aef3-c08c504794cf / -— |
| Jogador 4 | 3-4 | 146 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 42.0 | Lutador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.675047596767399e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 147 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 42.0 | Lutador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015009013004601002 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 148 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 42.0 | Lutador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 149 | PASS | FAST8 | 95.0 | 7 | 1 | 0 | 42.0 | Lutador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 151 | BUY | FAST8 | 95.0 | 7 | 8 | 0 | 42.0 | Lutador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.736807644367218 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-5 | 152 | MOVE_BENCH | FAST8 | 95.0 | 7 | 5 | 0 | 30.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1409124732017517 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 153 | MOVE_BENCH | FAST8 | 95.0 | 7 | 5 | 0 | 34.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08678389340639114 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 154 | BUY | FAST8 | 95.0 | 7 | 5 | 0 | 36.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.735473096370697 | 0.0 | 0.0 | +661b176a-5963-4715-b9dd-aca29f552fa9 / -— |
| Jogador 4 | 3-5 | 155 | BUY | FAST8 | 95.0 | 7 | 3 | 0 | 36.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10162489861249924 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 4 | 3-5 | 156 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 157 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16396203637123108 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 158 | PASS | FAST8 | 95.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 159 | MOVE_BENCH | FAST8 | 95.0 | 7 | 0 | 0 | 36.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4163798391819 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 161 | BUY | FAST8 | 95.0 | 7 | 9 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7301562428474426 | 0.0 | 0.0 | +ee0b17ab-70b6-45db-8475-edb945dba9e0 / -— |
| Jogador 4 | 3-6 | 162 | BUY | FAST8 | 95.0 | 7 | 6 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32062023878097534 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 4 | 3-6 | 163 | BUY | FAST8 | 95.0 | 7 | 3 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03885631635785103 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 4 | 3-6 | 164 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10124941170215607 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 165 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 166 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022898240014910698 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 167 | PASS | FAST8 | 95.0 | 7 | 1 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 171 | BUY | FAST8 | 84.0 | 7 | 6 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2004946619272232 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 4 | 3-7 | 172 | BUY | FAST8 | 84.0 | 7 | 3 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5224179625511169 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2,750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 4 | 3-7 | 173 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.71445146547012e-17 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 174 | MOVE_BENCH | FAST8 | 84.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42356565594673157 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 175 | PASS | FAST8 | 84.0 | 7 | 0 | 0 | 38.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 181 | BUY | FAST8 | 84.0 | 7 | 5 | 0 | 38.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7658733129501343 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -3224c4b3-14ed-42e7-a497-24e0be0a691c,661b176a-5963-4715-b9dd-aca29f552fa9 |
| Jogador 4 | 4-1 | 182 | BUY | FAST8 | 84.0 | 7 | 3 | 0 | 34.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.10025690495967865 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 4 | 4-1 | 183 | MOVE_BENCH | FAST8 | 84.0 | 7 | 0 | 0 | 34.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.602481484413147 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 184 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 185 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.031441304832696915 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 186 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1498885303735733 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 187 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06535406410694122 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 188 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 189 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 191 | BUY | FAST8 | 72.0 | 7 | 6 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1081966757774353 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -— |
| Jogador 4 | 4-2 | 192 | BUY | FAST8 | 72.0 | 7 | 2 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04900128394365311 | 0.0 | 0.0 | +16acc555-c819-4f7c-b406-2f48f11ffc87 / -— |
| Jogador 4 | 4-2 | 193 | MOVE_BOARD | FAST8 | 72.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3083210587501526 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 194 | MOVE_BOARD | FAST8 | 72.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014838502742350101 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 195 | MOVE_BOARD | FAST8 | 72.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 196 | PASS | FAST8 | 72.0 | 7 | 0 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 201 | SELL | FAST8 | 72.0 | 7 | 6 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030551470816135406 | 0.0 | 0.0 | +— / -d754fcfc-6d22-4bc0-8643-8f4bef9afda5 |
| Jogador 4 | 4-3 | 202 | BUY | FAST8 | 72.0 | 7 | 9 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1470213234424591 | 0.0 | 0.0 | +cc9b5fff-2223-4721-a8b2-4f70e196b851 / -— |
| Jogador 4 | 4-3 | 203 | SELL | FAST8 | 72.0 | 7 | 6 | 0 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031322307884693146 | 0.0 | 0.0 | +— / -21135c93-ae87-47a0-899c-7eaa0c2c30b8 |
| Jogador 4 | 4-3 | 204 | BUY | FAST8 | 72.0 | 7 | 14 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07110662758350372 | 0.0 | 0.0 | +8995f621-b355-44ec-816e-797184bdc266 / -— |
| Jogador 4 | 4-3 | 205 | MOVE_BOARD | FAST8 | 72.0 | 7 | 10 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.653068703599274e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 206 | MOVE_BOARD | FAST8 | 72.0 | 7 | 10 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 207 | PASS | FAST8 | 72.0 | 7 | 10 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 211 | SELL | FAST8 | 72.0 | 7 | 18 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15124616026878357 | 0.0 | 0.0 | +— / -16acc555-c819-4f7c-b406-2f48f11ffc87 |
| Jogador 4 | 4-4 | 212 | BUY | FAST8 | 72.0 | 7 | 20 | 2 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05899316072463989 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -— |
| Jogador 4 | 4-4 | 213 | SELL | FAST8 | 72.0 | 7 | 17 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13976922631263733 | 0.0 | 0.0 | +— / -c617e958-b482-40ce-ab24-acff4dc48bc0 |
| Jogador 4 | 4-4 | 214 | BUY | FAST8 | 72.0 | 7 | 20 | 2 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18525634706020355 | 0.0 | 0.0 | +738fea60-6b44-40f1-9936-43accf852bd7 / -— |
| Jogador 4 | 4-4 | 215 | MOVE_BOARD | FAST8 | 72.0 | 7 | 17 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.6495554518769495e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 216 | REROLL | FAST8 | 72.0 | 7 | 17 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 217 | SELL | FAST8 | 72.0 | 7 | 15 | 1 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11003384739160538 | 0.0 | 0.0 | +— / -b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 4 | 4-4 | 218 | EQUIP_FROM_INVENTORY | FAST8 | 72.0 | 7 | 20 | 2 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14578142762184143 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 219 | BUY | FAST8 | 72.0 | 7 | 20 | 2 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.054056450724601746 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -— |
| Jogador 4 | 4-5 | 221 | SELL | FAST8 | 72.0 | 7 | 23 | 2 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06678461283445358 | 0.0 | 0.0 | +— / -cba152f4-af54-4d82-a35d-67aa165174be |
| Jogador 4 | 4-5 | 222 | BUY | FAST8 | 72.0 | 7 | 26 | 2 | 40.0 | Lutador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6641427278518677 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 4 | 4-5 | 223 | SELL | FAST8 | 72.0 | 7 | 23 | 2 | 40.0 | Lutador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012853561900556087 | 0.0 | 0.0 | +— / -40f2a32f-1ace-4700-8a79-e6b5d3212036 |
| Jogador 4 | 4-5 | 224 | BUY | FAST8 | 72.0 | 7 | 31 | 3 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21857766807079315 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 4 | 4-5 | 225 | SELL | FAST8 | 72.0 | 7 | 27 | 2 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14900000393390656 | 0.0 | 0.0 | +— / -738fea60-6b44-40f1-9936-43accf852bd7 |
| Jogador 4 | 4-5 | 226 | BUY | FAST8 | 72.0 | 7 | 30 | 3 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4961104989051819 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 4 | 4-5 | 227 | REROLL | FAST8 | 72.0 | 7 | 28 | 2 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 228 | SELL | FAST8 | 72.0 | 7 | 26 | 2 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13024859130382538 | 0.0 | 0.0 | +— / -de8de4b5-48ea-4947-ae08-2b90d94b0fc1 |
| Jogador 4 | 4-5 | 229 | BUY | FAST8 | 72.0 | 7 | 28 | 2 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23240818083286285 | 0.0 | 0.0 | +678a6f43-ca48-46c9-8c5b-6790493f4841 / -— |
| Jogador 4 | 4-6 | 231 | SELL | FAST8 | 60.0 | 7 | 33 | 3 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06056051328778267 | 0.0 | 0.0 | +— / -333b0a0b-8868-40b2-96e9-71e468c5dd1f |
| Jogador 4 | 4-6 | 232 | BUY | FAST8 | 60.0 | 7 | 37 | 3 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7701694965362549 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -— |
| Jogador 4 | 4-6 | 233 | SELL | FAST8 | 60.0 | 7 | 35 | 3 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07232307642698288 | 0.0 | 0.0 | +— / -8a52858d-da47-4de9-8e91-8612788cb8fd |
| Jogador 4 | 4-6 | 234 | BUY | FAST8 | 60.0 | 7 | 38 | 3 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6519012451171875 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 4 | 4-6 | 235 | REROLL | FAST8 | 60.0 | 7 | 35 | 3 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 236 | SELL | FAST8 | 60.0 | 7 | 33 | 3 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1353117823600769 | 0.0 | 0.0 | +— / -cc9b5fff-2223-4721-a8b2-4f70e196b851 |
| Jogador 4 | 4-6 | 237 | BUY | FAST8 | 60.0 | 7 | 36 | 3 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6577322483062744 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 4 | 4-6 | 238 | SELL | FAST8 | 60.0 | 7 | 33 | 3 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1352963000535965 | 0.0 | 0.0 | +— / -64215569-2a69-410d-a2f9-172544bef858 |
| Jogador 4 | 4-6 | 239 | BUY | FAST8 | 60.0 | 7 | 36 | 3 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24821513891220093 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 4 | 4-7 | 241 | SELL | FAST8 | 60.0 | 7 | 44 | 4 | 40.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09366461634635925 | 0.0 | 0.0 | +— / -908d49c8-626c-44b5-9b03-6a85442f358b |
| Jogador 4 | 4-7 | 242 | BUY | FAST8 | 60.0 | 7 | 45 | 4 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8455727100372314 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -24b29fe6-466c-42d5-9f92-5d6114f0f98f,409b32b9-5280-4d79-b5b2-871ed597ba56 |
| Jogador 4 | 4-7 | 243 | BUY | FAST8 | 60.0 | 7 | 42 | 4 | 34.0 | Lutador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26422038674354553 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 4 | 4-7 | 244 | MOVE_BENCH | FAST8 | 60.0 | 7 | 41 | 4 | 34.0 | Lutador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5482720732688904 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 245 | BUY | FAST8 | 60.0 | 7 | 41 | 4 | 36.0 | Lutador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12451216578483582 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 4 | 4-7 | 246 | REROLL | FAST8 | 60.0 | 7 | 39 | 3 | 36.0 | Lutador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 247 | SELL | FAST8 | 60.0 | 7 | 37 | 3 | 36.0 | Lutador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001123076886869967 | 0.0 | 0.0 | +— / -c07a17cf-e9e7-42be-b925-cb4f699593de |
| Jogador 4 | 4-7 | 248 | BUY | FAST8 | 60.0 | 7 | 45 | 4 | 36.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04682450369000435 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 4 | 4-7 | 249 | REROLL | FAST8 | 60.0 | 7 | 42 | 4 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 251 | CRAFT_AND_EQUIP | FAST8 | 60.0 | 7 | 49 | 4 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1811891347169876 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 252 | CRAFT_AND_EQUIP | FAST8 | 60.0 | 7 | 49 | 4 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14588184654712677 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 253 | SELL | FAST8 | 60.0 | 7 | 49 | 4 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14442496001720428 | 0.0 | 0.0 | +— / -efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 |
| Jogador 4 | 5-1 | 254 | BUY | FAST8 | 60.0 | 7 | 51 | 5 | 36.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32686352729797363 | 0.0 | 0.0 | +1ad1f705-7e6b-4c1f-811c-2863dbf2db9e / -— |
| Jogador 4 | 5-1 | 255 | REROLL | FAST8 | 60.0 | 7 | 49 | 4 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 256 | SELL | FAST8 | 60.0 | 7 | 47 | 4 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1202840730547905 | 0.0 | 0.0 | +— / -1ad1f705-7e6b-4c1f-811c-2863dbf2db9e |
| Jogador 4 | 5-1 | 257 | BUY | FAST8 | 60.0 | 7 | 49 | 4 | 36.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8304955363273621 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -— |
| Jogador 4 | 5-1 | 258 | SELL | FAST8 | 60.0 | 7 | 48 | 4 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14716742932796478 | 0.0 | 0.0 | +— / -85fb6db6-e1b0-4fa1-b99a-2f205305ef0b |
| Jogador 4 | 5-1 | 259 | BUY | FAST8 | 60.0 | 7 | 51 | 5 | 36.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09952292591333389 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -— |
| Jogador 4 | 5-2 | 261 | SELL | FAST8 | 60.0 | 7 | 59 | 5 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06078461557626724 | 0.0 | 0.0 | +— / -425a58b3-d906-4381-9afc-00f9852c9982 |
| Jogador 4 | 5-2 | 262 | BUY | FAST8 | 60.0 | 7 | 62 | 5 | 36.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6494337320327759 | 0.0 | 0.0 | +04ebf9b8-7683-4270-b98a-a3bfb342dcf8 / -— |
| Jogador 4 | 5-2 | 263 | REROLL | FAST8 | 60.0 | 7 | 59 | 5 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 264 | SELL | FAST8 | 60.0 | 7 | 57 | 5 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14209768176078796 | 0.0 | 0.0 | +— / -04ebf9b8-7683-4270-b98a-a3bfb342dcf8 |
| Jogador 4 | 5-2 | 265 | BUY | FAST8 | 60.0 | 7 | 60 | 5 | 36.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2793220281600952 | 0.0 | 0.0 | +335c4988-791a-4579-a473-f387b986806c / -— |
| Jogador 4 | 5-2 | 266 | REROLL | FAST8 | 60.0 | 7 | 59 | 5 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 267 | SELL | FAST8 | 60.0 | 7 | 57 | 5 | 36.0 | Lutador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04617239907383919 | 0.0 | 0.0 | +— / -b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 |
| Jogador 4 | 5-2 | 268 | BUY | FAST8 | 60.0 | 7 | 60 | 5 | 36.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9498501420021057 | 0.0 | 0.0 | +ae89881d-8a08-4f60-ad51-1b0fe152958d / -8486b8a9-20fe-4234-bbba-0efa031c3b76,a810e10d-e7ef-4ece-8fb2-8b6471b557ec |
| Jogador 4 | 5-2 | 269 | MOVE_BENCH | FAST8 | 60.0 | 7 | 59 | 5 | 34.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5956940650939941 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 271 | BUY | FAST8 | 60.0 | 7 | 70 | 5 | 40.0 | Lutador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6615743041038513 | 0.0 | 0.0 | +e903e009-8dae-4fc9-b0ec-bc028c3f9f3e / -— |
| Jogador 4 | 5-3 | 272 | BUY | FAST8 | 60.0 | 7 | 66 | 5 | 40.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18585532903671265 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -— |
| Jogador 4 | 5-3 | 273 | REROLL | FAST8 | 60.0 | 7 | 63 | 5 | 40.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 274 | SELL | FAST8 | 60.0 | 7 | 61 | 5 | 40.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1468646228313446 | 0.0 | 0.0 | +— / -ae89881d-8a08-4f60-ad51-1b0fe152958d |
| Jogador 4 | 5-3 | 275 | EQUIP_FROM_INVENTORY | FAST8 | 60.0 | 7 | 64 | 5 | 40.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12437815219163895 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 276 | EQUIP_FROM_INVENTORY | FAST8 | 60.0 | 7 | 64 | 5 | 40.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09961794316768646 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 277 | BUY | FAST8 | 60.0 | 7 | 64 | 5 | 40.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8208114504814148 | 0.0 | 0.0 | +60290b49-92fb-48d4-a657-26afd1f3f662 / -— |
| Jogador 4 | 5-3 | 278 | REROLL | FAST8 | 60.0 | 7 | 62 | 5 | 40.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 279 | SELL | FAST8 | 60.0 | 7 | 60 | 5 | 40.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06780000030994415 | 0.0 | 0.0 | +— / -c3596d89-03d2-4fc7-afaf-591f10423252 |
| Jogador 4 | 5-4 | 281 | BUY | FAST8 | 60.0 | 7 | 74 | 5 | 40.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9495843052864075 | 0.0 | 0.0 | +5594beb6-a447-4be2-a6e0-ae5c4f94fe70 / -678a6f43-ca48-46c9-8c5b-6790493f4841,a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 4 | 5-4 | 282 | BUY | FAST8 | 60.0 | 7 | 72 | 5 | 40.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025834601372480392 | 0.0 | 0.0 | +2ce6c216-8ffa-4f9b-b78a-aed96adfa47b / -— |
| Jogador 4 | 5-4 | 283 | BUY | FAST8 | 60.0 | 7 | 69 | 5 | 40.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4228890836238861 | 0.0 | 0.0 | +b1e5b3b9-fda8-4d4a-9368-94fd558da4f7 / -— |
| Jogador 4 | 5-4 | 284 | REROLL | FAST8 | 60.0 | 7 | 66 | 5 | 40.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 285 | SELL | FAST8 | 60.0 | 7 | 64 | 5 | 40.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2017398178577423 | 0.0 | 0.0 | +— / -5594beb6-a447-4be2-a6e0-ae5c4f94fe70 |
| Jogador 4 | 5-4 | 286 | BUY | FAST8 | 60.0 | 7 | 69 | 5 | 40.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9494487643241882 | 0.0 | 0.0 | +e165ef09-0e2c-4d3f-8f49-fcf801db2777 / -3825a7ba-319f-48f8-ad2d-8c24eabbc1cc,4e00fb2f-75c1-4580-bd09-cb73c31af01f |
| Jogador 4 | 5-4 | 287 | EQUIP_FROM_INVENTORY | FAST8 | 60.0 | 7 | 66 | 5 | 28.0 | Lutador/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07449159771203995 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 288 | EQUIP_FROM_INVENTORY | FAST8 | 60.0 | 7 | 66 | 5 | 28.0 | Lutador/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.03622032701969147 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 289 | MOVE_BENCH | FAST8 | 60.0 | 7 | 66 | 5 | 28.0 | Lutador/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18991126120090485 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 291 | BUY | FAST8 | 60.0 | 7 | 77 | 5 | 36.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9496561884880066 | 0.0 | 0.0 | +6b0bead4-2978-41d5-a28d-a4c395f456a7 / -60290b49-92fb-48d4-a657-26afd1f3f662,e01be6cf-34fe-4057-aef3-c08c504794cf |
| Jogador 4 | 5-5 | 292 | BUY | FAST8 | 60.0 | 7 | 75 | 5 | 32.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04802330583333969 | 0.0 | 0.0 | +d925d9be-1d80-4347-93ba-4e5bc885dfc4 / -— |
| Jogador 4 | 5-5 | 293 | MOVE_BENCH | FAST8 | 60.0 | 7 | 71 | 5 | 32.0 | Lutador/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36649852991104126 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 294 | BUY | FAST8 | 60.0 | 7 | 71 | 5 | 44.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009794150479137897 | 0.0 | 0.0 | +a98c021a-415b-43eb-b741-97bdac39a598 / -— |
| Jogador 4 | 5-5 | 295 | REROLL | FAST8 | 60.0 | 7 | 67 | 5 | 44.0 | Lutador/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 296 | SELL | FAST8 | 60.0 | 7 | 65 | 5 | 44.0 | Lutador/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16558131575584412 | 0.0 | 0.0 | +— / -6b0bead4-2978-41d5-a28d-a4c395f456a7 |
| Jogador 4 | 5-5 | 297 | BUY | FAST8 | 60.0 | 7 | 70 | 5 | 44.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38768377900123596 | 0.0 | 0.0 | +c5f81113-0e4a-4d08-beab-f19d808ef10c / -— |
| Jogador 4 | 5-5 | 298 | MOVE_BENCH | FAST8 | 60.0 | 7 | 67 | 5 | 44.0 | Lutador/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6473362445831299 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 300 | BUY | FAST8 | 60.0 | 7 | 78 | 5 | 46.0 | Lutador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15540489554405212 | 0.0 | 0.0 | +61fe2c41-5cc2-4b6b-aa92-c83c3d900c07 / -— |
| Jogador 4 | 5-6 | 301 | SELL | FAST8 | 60.0 | 7 | 75 | 5 | 46.0 | Lutador/DA_Krug18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20820404589176178 | 0.0 | 0.0 | +— / -e165ef09-0e2c-4d3f-8f49-fcf801db2777 |
| Jogador 4 | 5-6 | 302 | EQUIP_FROM_INVENTORY | FAST8 | 60.0 | 7 | 83 | 5 | 46.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09338198602199554 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 303 | EQUIP_FROM_INVENTORY | FAST8 | 60.0 | 7 | 83 | 5 | 46.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0639243870973587 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 305 | EQUIP_FROM_INVENTORY | FAST8 | 60.0 | 7 | 95 | 5 | 46.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1269271820783615 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 306 | BUY | FAST8 | 60.0 | 7 | 95 | 5 | 46.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9410254955291748 | 0.0 | 0.0 | +b899f6f0-495e-490e-a4c5-3c81f7d7c739 / -b70671f9-0d78-4ae8-bd13-0267c96e7207,e903e009-8dae-4fc9-b0ec-bc028c3f9f3e |
| Jogador 4 | 5-7 | 307 | BUY | FAST8 | 60.0 | 7 | 91 | 5 | 38.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5877144932746887 | 0.0 | 0.0 | +5da8e90b-c813-43fb-8efb-3c32e2b9c4ed / -— |
| Jogador 4 | 5-7 | 308 | MOVE_BENCH | FAST8 | 60.0 | 7 | 89 | 5 | 38.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26623353362083435 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 309 | REROLL | FAST8 | 60.0 | 7 | 89 | 5 | 46.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 310 | SELL | FAST8 | 60.0 | 7 | 87 | 5 | 46.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1426408290863037 | 0.0 | 0.0 | +— / -5da8e90b-c813-43fb-8efb-3c32e2b9c4ed |
| Jogador 4 | 6-1 | 312 | EQUIP_FROM_INVENTORY | FAST8 | 60.0 | 7 | 100 | 5 | 52.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09869661182165146 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 313 | BUY | FAST8 | 60.0 | 7 | 100 | 5 | 52.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8855573534965515 | 0.0 | 0.0 | +42dcd971-9003-42c7-89f4-271ba5fe868d / -— |
| Jogador 4 | 6-1 | 314 | BUY | FAST8 | 60.0 | 7 | 97 | 5 | 52.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.459724485874176 | 0.0 | 0.0 | +0498225d-8106-4d05-8c91-f11b7c94904f / -— |
| Jogador 4 | 6-1 | 315 | REROLL | FAST8 | 60.0 | 7 | 93 | 5 | 52.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 316 | SELL | FAST8 | 60.0 | 7 | 91 | 5 | 52.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12364615499973297 | 0.0 | 0.0 | +— / -2ce6c216-8ffa-4f9b-b78a-aed96adfa47b |
| Jogador 4 | 6-1 | 317 | BUY | FAST8 | 60.0 | 7 | 94 | 5 | 52.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019938955083489418 | 0.0 | 0.0 | +703b70a3-3aca-4ecd-86da-0a1b34e4bb3a / -— |
| Jogador 4 | 6-1 | 318 | REROLL | FAST8 | 60.0 | 7 | 90 | 5 | 52.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 319 | SELL | FAST8 | 60.0 | 7 | 88 | 5 | 52.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06447692215442657 | 0.0 | 0.0 | +— / -b1e5b3b9-fda8-4d4a-9368-94fd558da4f7 |
| Jogador 4 | 6-1 | 320 | BUY | FAST8 | 60.0 | 7 | 91 | 5 | 52.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32232236862182617 | 0.0 | 0.0 | +1b5c89d2-f5ea-401f-bf8a-985023acf75c / -— |
| Jogador 4 | 6-2 | 322 | SELL | FAST8 | 41.0 | 7 | 97 | 5 | 52.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05986153706908226 | 0.0 | 0.0 | +— / -703b70a3-3aca-4ecd-86da-0a1b34e4bb3a |
| Jogador 4 | 6-2 | 323 | BUY | FAST8 | 41.0 | 7 | 101 | 5 | 52.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0072659254074097 | 0.0 | 0.0 | +0650ed76-f3bb-4dce-bd04-2ed294039e6d / -421bcbcb-ecb2-4af8-88d4-7be6cd284d27,ee0b17ab-70b6-45db-8475-edb945dba9e0 |
| Jogador 4 | 6-2 | 324 | MOVE_BENCH | FAST8 | 41.0 | 7 | 98 | 5 | 40.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6297334432601929 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 325 | MOVE_BENCH | FAST8 | 41.0 | 7 | 98 | 5 | 32.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2198019027709961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 326 | BUY | FAST8 | 41.0 | 7 | 98 | 5 | 48.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8417201638221741 | 0.0 | 0.0 | +de08b337-73c7-408b-8b57-b2f5fb036fe2 / -— |
| Jogador 4 | 6-2 | 327 | REROLL | FAST8 | 41.0 | 7 | 95 | 5 | 48.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 328 | SELL | FAST8 | 41.0 | 7 | 93 | 5 | 48.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17051129043102264 | 0.0 | 0.0 | +— / -0650ed76-f3bb-4dce-bd04-2ed294039e6d |
| Jogador 4 | 6-2 | 329 | BUY | FAST8 | 41.0 | 7 | 101 | 5 | 48.0 | Lutador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3265434205532074 | 0.0 | 0.0 | +42a24672-dcd0-4f0c-839a-82327962d77e / -— |
| Jogador 4 | 6-2 | 330 | MOVE_BENCH | FAST8 | 41.0 | 7 | 98 | 5 | 48.0 | Lutador/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5950873494148254 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 332 | BUY | FAST8 | 41.0 | 7 | 109 | 5 | 54.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1920057237148285 | 0.0 | 0.0 | +74ac117f-47a6-4d94-b6f7-8d42714571e5 / -— |
| Jogador 4 | 6-3 | 333 | REROLL | FAST8 | 41.0 | 7 | 105 | 5 | 54.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 334 | SELL | FAST8 | 41.0 | 7 | 103 | 5 | 54.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07038461416959763 | 0.0 | 0.0 | +— / -335c4988-791a-4579-a473-f387b986806c |
| Jogador 4 | 6-3 | 335 | BUY | FAST8 | 41.0 | 7 | 104 | 5 | 54.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0087785720825195 | 0.0 | 0.0 | +30d632db-738f-4a3c-84dc-ff4a4705ecdf / -42dcd971-9003-42c7-89f4-271ba5fe868d,c5f81113-0e4a-4d08-beab-f19d808ef10c |
| Jogador 4 | 6-3 | 336 | MOVE_BENCH | FAST8 | 41.0 | 7 | 101 | 5 | 42.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04758778586983681 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 337 | MOVE_BENCH | FAST8 | 41.0 | 7 | 101 | 5 | 40.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.366942822933197 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 338 | BUY | FAST8 | 41.0 | 7 | 101 | 5 | 48.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9062761068344116 | 0.0 | 0.0 | +fb7a5348-949c-42cf-9326-c4676d6b6960 / -— |
| Jogador 4 | 6-3 | 339 | MOVE_BENCH | FAST8 | 41.0 | 7 | 99 | 5 | 48.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3622496426105499 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 340 | MOVE_BENCH | FAST8 | 41.0 | 7 | 99 | 5 | 46.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.385113000869751 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 342 | BUY | STABILIZE | 22.0 | 7 | 109 | 5 | 54.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0795551538467407 | 0.0 | 0.0 | +94f20892-cf66-4256-9159-a295f6054b8f / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65,fb7a5348-949c-42cf-9326-c4676d6b6960 |
| Jogador 4 | 6-4 | 343 | MOVE_BENCH | STABILIZE | 22.0 | 7 | 107 | 5 | 46.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10434632748365402 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 344 | BUY | STABILIZE | 22.0 | 7 | 107 | 5 | 52.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.600249707698822 | 0.0 | 0.0 | +41b1dead-685f-4b66-b9b1-cc504a711c98 / -— |
| Jogador 4 | 6-4 | 345 | REROLL | STABILIZE | 22.0 | 7 | 104 | 5 | 52.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 346 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 102 | 5 | 52.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24641351401805878 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 347 | MOVE_BENCH | STABILIZE | 22.0 | 7 | 102 | 5 | 52.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3865799903869629 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 348 | BUY | STABILIZE | 22.0 | 7 | 102 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3996956944465637 | 0.0 | 0.0 | +bb2609fb-c8cb-4e7a-b308-8cd512ff870d / -— |
| Jogador 4 | 6-4 | 349 | REROLL | STABILIZE | 22.0 | 7 | 100 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 350 | REROLL | STABILIZE | 22.0 | 7 | 98 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 352 | REROLL | STABILIZE | 22.0 | 7 | 106 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 353 | REROLL | STABILIZE | 22.0 | 7 | 104 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 354 | SELL | STABILIZE | 22.0 | 7 | 102 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19018769264221191 | 0.0 | 0.0 | +— / -30d632db-738f-4a3c-84dc-ff4a4705ecdf |
| Jogador 4 | 6-5 | 355 | BUY | STABILIZE | 22.0 | 7 | 110 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9229791164398193 | 0.0 | 0.0 | +97593afb-3c61-420c-ab5c-3bd92e0f1c5f / -— |
| Jogador 4 | 6-5 | 356 | REROLL | STABILIZE | 22.0 | 7 | 106 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 357 | SELL | STABILIZE | 22.0 | 7 | 104 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18821845948696136 | 0.0 | 0.0 | +— / -94f20892-cf66-4256-9159-a295f6054b8f |
| Jogador 4 | 6-5 | 358 | EQUIP_FROM_INVENTORY | STABILIZE | 22.0 | 7 | 109 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1450742781162262 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 359 | EQUIP_FROM_INVENTORY | STABILIZE | 22.0 | 7 | 109 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08833889663219452 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 360 | BUY | STABILIZE | 22.0 | 7 | 109 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4163234829902649 | 0.0 | 0.0 | +d3dda9b6-13bb-47e1-af12-521aed1576d6 / -— |
| Jogador 4 | 6-6 | 362 | REROLL | ALL_IN | 3.0 | 7 | 118 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 363 | SELL | ALL_IN | 3.0 | 7 | 116 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05986153706908226 | 0.0 | 0.0 | +— / -d925d9be-1d80-4347-93ba-4e5bc885dfc4 |
| Jogador 4 | 6-6 | 364 | BUY | ALL_IN | 3.0 | 7 | 120 | 5 | 58.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0619555711746216 | 0.0 | 0.0 | +b9dd5592-1f2b-43f7-b094-7de5e406d4da / -41b1dead-685f-4b66-b9b1-cc504a711c98,42a24672-dcd0-4f0c-839a-82327962d77e |
| Jogador 4 | 6-6 | 365 | BUY | ALL_IN | 3.0 | 7 | 117 | 5 | 52.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9261927008628845 | 0.0 | 0.0 | +68251e71-5657-42da-9181-7351627204f6 / -— |
| Jogador 4 | 6-6 | 366 | REROLL | ALL_IN | 3.0 | 7 | 115 | 5 | 52.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 367 | MOVE_BENCH | ALL_IN | 3.0 | 7 | 113 | 5 | 52.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5365270972251892 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 368 | BUY | ALL_IN | 3.0 | 7 | 113 | 5 | 56.0 | Fera do Rift/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2297849804162979 | 0.0 | 0.0 | +71a71643-507c-4266-9f74-1fd7802fe094 / -— |
| Jogador 4 | 6-6 | 369 | REROLL | ALL_IN | 3.0 | 7 | 110 | 5 | 56.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 370 | REROLL | ALL_IN | 3.0 | 7 | 108 | 5 | 56.0 | Fera do Rift/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +a05f4164-724c-4182-bafc-82ef354cea0b / -— |
| Jogador 5 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.11927274614572525 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032908253371715546 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2966248393058777 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | -0.01536033395677805 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | -0.014424941502511501 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25498273968696594 | 0.0 | 0.0 | +4a7ac9c5-c110-4566-80e5-25d9e6033799 / -— |
| Jogador 5 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12135981023311615 | 0.0 | 0.0 | +— / -4a7ac9c5-c110-4566-80e5-25d9e6033799 |
| Jogador 5 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08310991525650024 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 24 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0599563904106617 | 0.0 | 0.0 | +3002832d-1e66-428b-a25e-007c716764a3 / -— |
| Jogador 5 | 1-3 | 26 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764707699418068 | 0.0 | 0.0 | +— / -3002832d-1e66-428b-a25e-007c716764a3 |
| Jogador 5 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0599563904106617 | 0.0 | 0.0 | +9c93476e-a7be-457d-8543-8802507a8d3f / -— |
| Jogador 5 | 1-3 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40578463673591614 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Elise | BUY, MOVE_BOARD, PASS | True | True | 0.08007753640413284 | 0.0 | 0.0 | +05bab539-ccde-4173-a658-22c50c34f59b / -— |
| Jogador 5 | 1-4 | 31 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007584615610539913 | 0.0 | 0.0 | +— / -05bab539-ccde-4173-a658-22c50c34f59b |
| Jogador 5 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17126254737377167 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10164615511894226 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17126254737377167 | 0.0 | 0.0 | +4c71fb0c-00db-4e1e-8563-2ca901248b7f / -— |
| Jogador 5 | 1-4 | 35 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10164615511894226 | 0.0 | 0.0 | +— / -4c71fb0c-00db-4e1e-8563-2ca901248b7f |
| Jogador 5 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3299463987350464 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 37 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14010746777057648 | 0.0 | 0.0 | +— / -634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08007753640413284 | 0.0 | 0.0 | +9f7fed06-4220-46d5-a6c9-a7cda1f846d6 / -— |
| Jogador 5 | 1-4 | 39 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007584615610539913 | 0.0 | 0.0 | +— / -9f7fed06-4220-46d5-a6c9-a7cda1f846d6 |
| Jogador 5 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.20218424499034882 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4057852327823639 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.10381602495908737 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -— |
| Jogador 5 | 2-1 | 44 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.37643998861312866 | 0.0 | 0.0 | +— / -a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 |
| Jogador 5 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3056727349758148 | 0.0 | 0.0 | +4a8986e4-45cf-42bc-866d-01c476dcb55b / -— |
| Jogador 5 | 2-1 | 46 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3556727170944214 | 0.0 | 0.0 | +— / -4a8986e4-45cf-42bc-866d-01c476dcb55b |
| Jogador 5 | 2-1 | 47 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.16192302107810974 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 48 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3896893262863159 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3851170539855957 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 51 | BUY | STABILIZE | 95.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.20302727818489075 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 9 | 0 | 10.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07182943820953369 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 53 | SELL | STABILIZE | 95.0 | 4 | 9 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08204615116119385 | 0.0 | 0.0 | +— / -eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-2 | 54 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.15281733870506287 | 0.0 | 0.0 | +9bb3da58-fe6f-4298-8529-859cceb4857e / -— |
| Jogador 5 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.5266016125679016 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 56 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09600730985403061 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 57 | PASS | STABILIZE | 95.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 61 | SELL | STABILIZE | 95.0 | 4 | 13 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08610983192920685 | 0.0 | 0.0 | +— / -a05f4164-724c-4182-bafc-82ef354cea0b |
| Jogador 5 | 2-3 | 62 | BUY | STABILIZE | 95.0 | 4 | 14 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3504487872123718 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 63 | SELL | STABILIZE | 95.0 | 4 | 13 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0626920610666275 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 64 | BUY | STABILIZE | 95.0 | 4 | 14 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.2783414423465729 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 65 | SELL | STABILIZE | 95.0 | 4 | 13 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3386690616607666 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-3 | 66 | BUY | STABILIZE | 95.0 | 4 | 14 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.21222077310085297 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 67 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 4 | 13 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10234956443309784 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 68 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 4 | 13 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14335888624191284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 69 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 13 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 71 | SELL | STABILIZE | 95.0 | 4 | 21 | 2 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0042307693511247635 | 0.0 | 0.0 | +— / -5627d898-cff3-4664-87d1-40a8f3656ab3 |
| Jogador 5 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 4 | 22 | 2 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17165711522102356 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 19 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03824610263109207 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 74 | SELL | STABILIZE | 95.0 | 4 | 19 | 1 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06712606549263 | 0.0 | 0.0 | +— / -df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 2-4 | 75 | BUY | STABILIZE | 95.0 | 4 | 21 | 2 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08281023800373077 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 76 | SELL | STABILIZE | 95.0 | 4 | 19 | 1 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22167691588401794 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 77 | BUY | STABILIZE | 95.0 | 4 | 21 | 2 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28851184248924255 | 0.0 | 0.0 | +32b7b452-7702-43a3-b3c4-8eda786225b9 / -— |
| Jogador 5 | 2-4 | 78 | BUY_XP | STABILIZE | 95.0 | 4 | 20 | 2 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032784998416900635 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 79 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 16 | 1 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44869041442871094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 81 | BUY | STABILIZE | 95.0 | 5 | 23 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0323295593261719 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 82 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 20 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09943849593400955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 83 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 20 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037358783185482025 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 84 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 20 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41484925150871277 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 85 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 20 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08394584059715271 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 86 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 20 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35208776593208313 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 87 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 20 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3998561203479767 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 88 | PASS | SLOWROLL | 95.0 | 5 | 20 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020892856642603874 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 91 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 29 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09893354773521423 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 92 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 29 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 93 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 29 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 94 | PASS | SLOWROLL | 95.0 | 5 | 29 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 101 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 39 | 3 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39895719289779663 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 102 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 39 | 3 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07398480921983719 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 103 | SELL | SLOWROLL | 95.0 | 5 | 39 | 3 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06743080914020538 | 0.0 | 0.0 | +— / -32b7b452-7702-43a3-b3c4-8eda786225b9 |
| Jogador 5 | 2-7 | 104 | BUY | SLOWROLL | 95.0 | 5 | 40 | 4 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16564203798770905 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 105 | BUY_XP | SLOWROLL | 95.0 | 5 | 38 | 3 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 106 | BUY_XP | SLOWROLL | 95.0 | 5 | 34 | 3 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 107 | BUY_XP | SLOWROLL | 95.0 | 5 | 30 | 3 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 108 | BUY_XP | SLOWROLL | 95.0 | 5 | 26 | 2 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019509999081492424 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 109 | MOVE_BENCH | FAST8 | 95.0 | 6 | 22 | 2 | 26.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40235236287117004 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 111 | BUY | FAST8 | 95.0 | 6 | 30 | 3 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.5654023885726929 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -— |
| Jogador 5 | 3-1 | 112 | SELL | FAST8 | 95.0 | 6 | 28 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.33537182211875916 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-1 | 113 | BUY | FAST8 | 95.0 | 6 | 30 | 3 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.01982863061130047 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 114 | SELL | FAST8 | 95.0 | 6 | 27 | 2 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.33225199580192566 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-1 | 115 | BUY | FAST8 | 95.0 | 6 | 30 | 3 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1718725711107254 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 5 | 3-1 | 116 | CRAFT_AND_EQUIP | FAST8 | 95.0 | 6 | 29 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06130806356668472 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 117 | BUY_XP | FAST8 | 95.0 | 6 | 29 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 118 | BUY_XP | FAST8 | 95.0 | 6 | 25 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 119 | BUY_XP | FAST8 | 95.0 | 6 | 21 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 121 | SELL | FAST8 | 95.0 | 6 | 26 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16247381269931793 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 5 | 3-2 | 122 | BUY | FAST8 | 95.0 | 6 | 27 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24029232561588287 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 123 | MOVE_BOARD | FAST8 | 95.0 | 6 | 25 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001107106581912376 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 124 | SELL | FAST8 | 95.0 | 6 | 25 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1742468774318695 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 5 | 3-2 | 125 | BUY | FAST8 | 95.0 | 6 | 27 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6405395269393921 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 126 | SELL | FAST8 | 95.0 | 6 | 25 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4155600666999817 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 3-2 | 127 | BUY | FAST8 | 95.0 | 6 | 27 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09961581230163574 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 128 | BUY_XP | FAST8 | 95.0 | 6 | 24 | 2 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 129 | BUY_XP | FAST8 | 95.0 | 6 | 20 | 2 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 131 | SELL | FAST8 | 84.0 | 6 | 22 | 2 | 30.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4133967459201813 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-3 | 132 | BUY | FAST8 | 84.0 | 6 | 25 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7993025183677673 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -486e92ad-4dcf-4c0e-a470-e0b87777d380,9bb3da58-fe6f-4298-8529-859cceb4857e |
| Jogador 5 | 3-3 | 133 | MOVE_BENCH | SLOWROLL | 84.0 | 6 | 22 | 2 | 18.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3506123721599579 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 134 | BUY | FAST8 | 84.0 | 6 | 22 | 2 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03697659820318222 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 135 | MOVE_BENCH | FAST8 | 84.0 | 6 | 18 | 1 | 30.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4424629807472229 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 136 | MOVE_BOARD | FAST8 | 84.0 | 6 | 18 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.014936789870262146 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 137 | BUY | FAST8 | 84.0 | 6 | 18 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5828285813331604 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 138 | BUY_XP | FAST8 | 84.0 | 6 | 16 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 139 | BUY_XP | FAST8 | 84.0 | 6 | 12 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025599999353289604 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 141 | SELL | FAST8 | 84.0 | 7 | 14 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41176843643188477 | 0.0 | 0.0 | +— / -8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 3-4 | 142 | BUY | FAST8 | 84.0 | 7 | 16 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.040244534611701965 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 143 | SELL | FAST8 | 84.0 | 7 | 13 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3923514783382416 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-4 | 144 | BUY | FAST8 | 84.0 | 7 | 16 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.24783658981323242 | 0.0 | 0.0 | +3a11170d-1b8e-4316-ad59-9a7e60071f12 / -— |
| Jogador 5 | 3-4 | 145 | MOVE_BENCH | FAST8 | 84.0 | 7 | 13 | 1 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4005042314529419 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 146 | BUY | FAST8 | 84.0 | 7 | 13 | 1 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1410914808511734 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 147 | BUY_XP | FAST8 | 84.0 | 7 | 12 | 1 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 148 | BUY_XP | FAST8 | 84.0 | 7 | 8 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 149 | BUY_XP | FAST8 | 84.0 | 7 | 4 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 151 | SELL | FAST8 | 84.0 | 7 | 5 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3391973376274109 | 0.0 | 0.0 | +— / -6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 3-5 | 152 | BUY | FAST8 | 84.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.23141267895698547 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 153 | MOVE_BENCH | FAST8 | 84.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0266865324229002 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 154 | MOVE_BOARD | FAST8 | 84.0 | 7 | 2 | 0 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 155 | MOVE_BOARD | FAST8 | 84.0 | 7 | 2 | 0 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 156 | PASS | FAST8 | 84.0 | 7 | 2 | 0 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 161 | SELL | FAST8 | 84.0 | 7 | 9 | 0 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10032866895198822 | 0.0 | 0.0 | +— / -3a11170d-1b8e-4316-ad59-9a7e60071f12 |
| Jogador 5 | 3-6 | 162 | BUY | FAST8 | 84.0 | 7 | 12 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13460782170295715 | 0.0 | 0.0 | +171724e7-58bd-404f-820b-2bb32c5c193e / -— |
| Jogador 5 | 3-6 | 163 | MOVE_BOARD | FAST8 | 84.0 | 7 | 9 | 0 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 164 | MOVE_BOARD | FAST8 | 84.0 | 7 | 9 | 0 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014939515851438046 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 165 | PASS | FAST8 | 84.0 | 7 | 9 | 0 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 171 | SELL | FAST8 | 84.0 | 7 | 17 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07215555012226105 | 0.0 | 0.0 | +— / -171724e7-58bd-404f-820b-2bb32c5c193e |
| Jogador 5 | 3-7 | 172 | BUY | FAST8 | 84.0 | 7 | 20 | 2 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0003660607908386737 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 5 | 3-7 | 173 | SELL | FAST8 | 84.0 | 7 | 17 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24190829694271088 | 0.0 | 0.0 | +— / -3625f791-4c9f-4b95-bdf7-4a322dcd55d3 |
| Jogador 5 | 3-7 | 174 | BUY | FAST8 | 84.0 | 7 | 20 | 2 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02295736037194729 | 0.0 | 0.0 | +014c92c3-e588-4e8b-b4bd-93cee45d74af / -— |
| Jogador 5 | 3-7 | 175 | MOVE_BOARD | FAST8 | 84.0 | 7 | 17 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 176 | SELL | FAST8 | 84.0 | 7 | 17 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23744884133338928 | 0.0 | 0.0 | +— / -014c92c3-e588-4e8b-b4bd-93cee45d74af |
| Jogador 5 | 3-7 | 177 | BUY | FAST8 | 84.0 | 7 | 20 | 2 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.26773586869239807 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 5 | 3-7 | 178 | BUY_XP | FAST8 | 84.0 | 7 | 17 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 179 | BUY_XP | FAST8 | 84.0 | 7 | 13 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 181 | SELL | FAST8 | 84.0 | 7 | 15 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2907482385635376 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 5 | 4-1 | 182 | BUY | FAST8 | 84.0 | 7 | 18 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.25028276443481445 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 5 | 4-1 | 183 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 15 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12823334336280823 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 184 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 15 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12312600761651993 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 185 | MOVE_BOARD | FAST8 | 84.0 | 7 | 15 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 186 | MOVE_BOARD | FAST8 | 84.0 | 7 | 15 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015088610351085663 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 187 | PASS | FAST8 | 84.0 | 7 | 15 | 1 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10499999672174454 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 191 | SELL | FAST8 | 72.0 | 7 | 21 | 2 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22341419756412506 | 0.0 | 0.0 | +— / -9bd6852a-b7a4-468c-a8cc-5318f7906eae |
| Jogador 5 | 4-2 | 192 | BUY | FAST8 | 72.0 | 7 | 24 | 2 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27792173624038696 | 0.0 | 0.0 | +840740a6-45be-4107-a4b7-b10cefe1a667 / -— |
| Jogador 5 | 4-2 | 193 | SELL | FAST8 | 72.0 | 7 | 21 | 2 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4987872242927551 | 0.0 | 0.0 | +— / -840740a6-45be-4107-a4b7-b10cefe1a667 |
| Jogador 5 | 4-2 | 194 | BUY | FAST8 | 72.0 | 7 | 24 | 2 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12001003324985504 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 5 | 4-2 | 195 | MOVE_BENCH | FAST8 | 72.0 | 7 | 20 | 2 | 46.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.044477686285972595 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 196 | BUY_XP | FAST8 | 72.0 | 7 | 20 | 2 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0758500024676323 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 197 | BUY_XP | FAST8 | 72.0 | 7 | 16 | 1 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004149999935179949 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 198 | BUY_XP | FAST8 | 72.0 | 7 | 12 | 1 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 199 | BUY_XP | FAST8 | 72.0 | 7 | 8 | 0 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 201 | SELL | FAST8 | 72.0 | 7 | 10 | 1 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02123168297111988 | 0.0 | 0.0 | +— / -68cd8ae3-399f-461f-89a8-189d7b0a6b59 |
| Jogador 5 | 4-3 | 202 | BUY | FAST8 | 72.0 | 7 | 13 | 1 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.25174978375434875 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 5 | 4-3 | 203 | BUY_XP | FAST8 | 72.0 | 7 | 10 | 1 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 204 | BUY_XP | FAST8 | 72.0 | 7 | 6 | 0 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08269374817609787 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 205 | MOVE_BENCH | ECON | 72.0 | 8 | 2 | 0 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5994415879249573 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 206 | BUY | ECON | 72.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.1292331963777542 | 0.0 | 0.0 | +5477420d-3b98-4863-b2e7-f414d3fa1f01 / -— |
| Jogador 5 | 4-3 | 207 | MOVE_BOARD | ECON | 72.0 | 8 | 0 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.390153349551838e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 208 | MOVE_BOARD | ECON | 72.0 | 8 | 0 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 209 | MOVE_BOARD | ECON | 72.0 | 8 | 0 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 211 | BUY | ECON | 72.0 | 8 | 7 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020818719640374184 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -— |
| Jogador 5 | 4-4 | 212 | BUY | ECON | 72.0 | 8 | 4 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12814165651798248 | 0.0 | 0.0 | +815aab3d-cea8-4ca6-aea3-3c9d656e6edd / -— |
| Jogador 5 | 4-4 | 213 | MOVE_BOARD | ECON | 72.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 214 | MOVE_BOARD | ECON | 72.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 215 | PASS | ECON | 72.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 221 | BUY | ECON | 72.0 | 8 | 8 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26547253131866455 | 0.0 | 0.0 | +bcd06176-e1d7-43fb-abd4-b6faea8c7927 / -— |
| Jogador 5 | 4-5 | 222 | MOVE_BOARD | ECON | 72.0 | 8 | 6 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.482606891542673e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 223 | BUY | ECON | 72.0 | 8 | 6 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18298405408859253 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 5 | 4-5 | 224 | BUY_XP | ECON | 72.0 | 8 | 5 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 225 | MOVE_BOARD | ECON | 72.0 | 8 | 1 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 226 | MOVE_BOARD | ECON | 72.0 | 8 | 1 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015038852579891682 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 227 | PASS | ECON | 72.0 | 8 | 1 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 231 | BUY | WINSTREAK | 72.0 | 8 | 8 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7168898582458496 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 5 | 4-6 | 232 | BUY | WINSTREAK | 72.0 | 8 | 4 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12029101699590683 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 5 | 4-6 | 233 | MOVE_BOARD | WINSTREAK | 72.0 | 8 | 0 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 234 | MOVE_BOARD | WINSTREAK | 72.0 | 8 | 0 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 235 | PASS | WINSTREAK | 72.0 | 8 | 0 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 241 | BUY | ECON | 60.0 | 8 | 5 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21397806704044342 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 5 | 4-7 | 242 | BUY | ECON | 60.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49895554780960083 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -5477420d-3b98-4863-b2e7-f414d3fa1f01,bcd06176-e1d7-43fb-abd4-b6faea8c7927 |
| Jogador 5 | 4-7 | 243 | SELL | ECON | 60.0 | 8 | 0 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.108249232172966 | 0.0 | 0.0 | +— / -2b89bd83-8449-4c63-9da2-62a46c68bdf5 |
| Jogador 5 | 4-7 | 244 | BUY | ECON | 60.0 | 8 | 5 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21260380744934082 | 0.0 | 0.0 | +674bcfdb-fddd-498c-ba65-ef3a3b989f07 / -— |
| Jogador 5 | 4-7 | 245 | MOVE_BOARD | ECON | 60.0 | 8 | 1 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 246 | MOVE_BOARD | ECON | 60.0 | 8 | 1 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014940223656594753 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 247 | PASS | ECON | 60.0 | 8 | 1 | 0 | 54.0 | Defendente/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 251 | BUY | ECON | 60.0 | 8 | 6 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17273551225662231 | 0.0 | 0.0 | +93581e04-3f00-4430-8e5b-c953196bc1de / -— |
| Jogador 5 | 5-1 | 252 | BUY | ECON | 60.0 | 8 | 3 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21648769080638885 | 0.0 | 0.0 | +d632ff66-a7c4-43d3-afb3-b83c174cda35 / -— |
| Jogador 5 | 5-1 | 253 | CRAFT_AND_EQUIP | ECON | 60.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1582794338464737 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 254 | CRAFT_AND_EQUIP | ECON | 60.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11375342309474945 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 255 | MOVE_BOARD | ECON | 60.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 256 | MOVE_BOARD | ECON | 60.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 257 | PASS | ECON | 60.0 | 8 | 2 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 261 | SELL | ECON | 44.0 | 8 | 8 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12314946949481964 | 0.0 | 0.0 | +— / -815aab3d-cea8-4ca6-aea3-3c9d656e6edd |
| Jogador 5 | 5-2 | 262 | BUY | ECON | 44.0 | 8 | 10 | 1 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.61003178358078 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 5 | 5-2 | 263 | SELL | ECON | 44.0 | 8 | 7 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05270461365580559 | 0.0 | 0.0 | +— / -3c59d736-011d-480c-a9af-1df7a3b4caab |
| Jogador 5 | 5-2 | 264 | BUY | ECON | 44.0 | 8 | 8 | 0 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16918626427650452 | 0.0 | 0.0 | +87902519-e44a-4d4c-9956-ac5aedc9b0c6 / -— |
| Jogador 5 | 5-2 | 265 | MOVE_BOARD | ECON | 44.0 | 8 | 6 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001442573993699625 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 266 | MOVE_BOARD | ECON | 44.0 | 8 | 6 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015270467847585678 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 267 | MOVE_BOARD | ECON | 44.0 | 8 | 6 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 268 | PASS | ECON | 44.0 | 8 | 6 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 271 | SELL | ECON | 44.0 | 8 | 12 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04266917705535889 | 0.0 | 0.0 | +— / -87902519-e44a-4d4c-9956-ac5aedc9b0c6 |
| Jogador 5 | 5-3 | 272 | BUY | ECON | 44.0 | 8 | 14 | 1 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21521799266338348 | 0.0 | 0.0 | +edd9f925-ac58-4285-a53c-ca70b782c682 / -— |
| Jogador 5 | 5-3 | 273 | SELL | ECON | 44.0 | 8 | 12 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06050769239664078 | 0.0 | 0.0 | +— / -772bccc4-15f4-4de2-95f8-82d0ed9a72d2 |
| Jogador 5 | 5-3 | 274 | BUY | ECON | 44.0 | 8 | 15 | 1 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11118422448635101 | 0.0 | 0.0 | +a960f5cb-d806-4d73-9146-244e1ecde6f2 / -— |
| Jogador 5 | 5-3 | 275 | MOVE_BOARD | ECON | 44.0 | 8 | 11 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 276 | REROLL | ECON | 44.0 | 8 | 11 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 277 | SELL | ECON | 44.0 | 8 | 9 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06429564207792282 | 0.0 | 0.0 | +— / -de590b22-a48c-4c78-a2f3-6ef39ce948fe |
| Jogador 5 | 5-3 | 278 | BUY | ECON | 44.0 | 8 | 12 | 1 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29214876890182495 | 0.0 | 0.0 | +b75d78d9-6080-40b3-ad63-30afae49e0a5 / -— |
| Jogador 5 | 5-3 | 279 | SELL | ECON | 44.0 | 8 | 8 | 0 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12358763813972473 | 0.0 | 0.0 | +— / -93581e04-3f00-4430-8e5b-c953196bc1de |
| Jogador 5 | 5-4 | 281 | BUY | ECON | 44.0 | 8 | 19 | 1 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17698563635349274 | 0.0 | 0.0 | +beed40ed-5b69-45eb-a675-b18cf2c9eb69 / -— |
| Jogador 5 | 5-4 | 282 | SELL | ECON | 44.0 | 8 | 14 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07709230482578278 | 0.0 | 0.0 | +— / -b75d78d9-6080-40b3-ad63-30afae49e0a5 |
| Jogador 5 | 5-4 | 283 | BUY | ECON | 44.0 | 8 | 18 | 1 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6888569593429565 | 0.0 | 0.0 | +4f487e34-c67d-489d-a21e-78b5642aefd4 / -— |
| Jogador 5 | 5-4 | 284 | MOVE_BENCH | ECON | 44.0 | 8 | 15 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06964274495840073 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 285 | MOVE_BENCH | ECON | 44.0 | 8 | 15 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3905124068260193 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 286 | MOVE_BENCH | ECON | 44.0 | 8 | 15 | 1 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5682127475738525 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 287 | PASS | ECON | 44.0 | 8 | 15 | 1 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02782592549920082 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 291 | SELL | ECON | 44.0 | 8 | 22 | 2 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -a960f5cb-d806-4d73-9146-244e1ecde6f2 |
| Jogador 5 | 5-5 | 292 | BUY | ECON | 44.0 | 8 | 26 | 2 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7630044221878052 | 0.0 | 0.0 | +24985c10-0eb6-40fa-9d1a-99ceb7213e06 / -— |
| Jogador 5 | 5-5 | 293 | MOVE_BENCH | ECON | 44.0 | 8 | 24 | 2 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07113806903362274 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 294 | MOVE_BOARD | ECON | 44.0 | 8 | 24 | 2 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015070749446749687 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 295 | REROLL | ECON | 44.0 | 8 | 24 | 2 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 296 | SELL | ECON | 44.0 | 8 | 22 | 2 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11435763537883759 | 0.0 | 0.0 | +— / -4f487e34-c67d-489d-a21e-78b5642aefd4 |
| Jogador 5 | 5-5 | 297 | BUY | ECON | 44.0 | 8 | 25 | 2 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21608906984329224 | 0.0 | 0.0 | +40cd6861-e205-4eb7-900f-d5364fc3c439 / -— |
| Jogador 5 | 5-5 | 298 | MOVE_BOARD | ECON | 44.0 | 8 | 21 | 2 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 300 | SELL | STABILIZE | 28.0 | 8 | 28 | 2 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15709230303764343 | 0.0 | 0.0 | +— / -40cd6861-e205-4eb7-900f-d5364fc3c439 |
| Jogador 5 | 5-6 | 301 | BUY | STABILIZE | 28.0 | 8 | 32 | 3 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8139965534210205 | 0.0 | 0.0 | +36a593e6-6199-441a-907d-77b9ea835889 / -— |
| Jogador 5 | 5-6 | 302 | SELL | STABILIZE | 28.0 | 8 | 29 | 2 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026792127639055252 | 0.0 | 0.0 | +— / -d632ff66-a7c4-43d3-afb3-b83c174cda35 |
| Jogador 5 | 5-6 | 303 | BUY | STABILIZE | 28.0 | 8 | 30 | 3 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01749429851770401 | 0.0 | 0.0 | +20ed6aae-dc87-406e-8bf9-a5afde4c9fef / -— |
| Jogador 5 | 5-7 | 305 | SELL | ALL_IN | 12.0 | 8 | 33 | 3 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05809829756617546 | 0.0 | 0.0 | +— / -badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 5 | 5-7 | 306 | BUY | ALL_IN | 12.0 | 8 | 37 | 3 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3308587968349457 | 0.0 | 0.0 | +dcc60ca2-ff4b-4d41-91b3-03a6cd3de0bb / -— |
| Jogador 5 | 5-7 | 307 | REROLL | ALL_IN | 12.0 | 8 | 33 | 3 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 308 | SELL | ALL_IN | 12.0 | 8 | 31 | 3 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12661775946617126 | 0.0 | 0.0 | +— / -b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 5 | 5-7 | 309 | BUY | ALL_IN | 12.0 | 8 | 35 | 3 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9196392893791199 | 0.0 | 0.0 | +c184c7c4-0cf6-4101-ac4d-cea12a7b4607 / -24985c10-0eb6-40fa-9d1a-99ceb7213e06,edd9f925-ac58-4285-a53c-ca70b782c682 |
| Jogador 5 | 5-7 | 310 | BUY | ALL_IN | 12.0 | 8 | 33 | 3 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018053825944662094 | 0.0 | 0.0 | +5aa6735d-7b0a-4358-b39f-e4adf477d11e / -— |
| Jogador 5 | 6-1 | 312 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 8 | 36 | 3 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13206958770751953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 313 | BUY | ALL_IN | 12.0 | 8 | 36 | 3 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8549818396568298 | 0.0 | 0.0 | +4aad2eba-6da2-4e1f-8350-7a645cf03109 / -— |
| Jogador 5 | 6-1 | 314 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 32 | 3 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2867072522640228 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 315 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 32 | 3 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07101163268089294 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 316 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 32 | 3 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41511988639831543 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 317 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 32 | 3 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3013705611228943 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 318 | PASS | ALL_IN | 12.0 | 8 | 32 | 3 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1461980938911438 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 322 | SELL | ALL_IN | 12.0 | 8 | 41 | 4 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13883385062217712 | 0.0 | 0.0 | +— / -c184c7c4-0cf6-4101-ac4d-cea12a7b4607 |
| Jogador 5 | 6-2 | 323 | BUY | ALL_IN | 12.0 | 8 | 46 | 4 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0039851665496826 | 0.0 | 0.0 | +f074442b-5ccc-4174-ac90-ef9eb358f8c1 / -36a593e6-6199-441a-907d-77b9ea835889,ddae48a6-5360-4660-9fa1-143ac35635ee |
| Jogador 5 | 6-2 | 324 | BUY | ALL_IN | 12.0 | 8 | 43 | 4 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03816833719611168 | 0.0 | 0.0 | +a882c3ee-af7e-400d-911c-a25555e368a5 / -— |
| Jogador 5 | 6-2 | 325 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 40 | 4 | 48.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5346550345420837 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 326 | BUY | ALL_IN | 12.0 | 8 | 40 | 4 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2983871102333069 | 0.0 | 0.0 | +5268c681-31fe-4973-9d93-cd1413b64383 / -— |
| Jogador 5 | 6-2 | 327 | REROLL | ALL_IN | 12.0 | 8 | 39 | 3 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 328 | SELL | ALL_IN | 12.0 | 8 | 37 | 3 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.230880007147789 | 0.0 | 0.0 | +— / -f074442b-5ccc-4174-ac90-ef9eb358f8c1 |
| Jogador 5 | 6-2 | 329 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 8 | 45 | 4 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1232592761516571 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 330 | BUY | ALL_IN | 12.0 | 8 | 45 | 4 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9197208285331726 | 0.0 | 0.0 | +e16e453d-d380-4b02-aaae-65f563be25e7 / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.010813108645379543 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 12 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13920184969902039 | 0.0 | 0.0 | +— / -908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2811388373374939 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 14 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13968460261821747 | 0.0 | 0.0 | +— / -425b1e77-5887-40b3-875e-c1f60dc6c513 |
| Jogador 6 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.03930075094103813 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 16 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07796266674995422 | 0.0 | 0.0 | +— / -4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 |
| Jogador 6 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2705819606781006 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 18 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13674388825893402 | 0.0 | 0.0 | +— / -3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 1-2 | 19 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08228474855422974 | 0.0 | 0.0 | +c733a654-69b5-4b02-979e-21ef1dd5d04b / -— |
| Jogador 6 | 1-3 | 21 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0882861539721489 | 0.0 | 0.0 | +— / -c733a654-69b5-4b02-979e-21ef1dd5d04b |
| Jogador 6 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.034025438129901886 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 23 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03400284796953201 | 0.0 | 0.0 | +f29b0444-8dd6-44a6-9a04-824febf737a0 / -— |
| Jogador 6 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Caitlyn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764399990439415 | 0.0 | 0.0 | +— / -f29b0444-8dd6-44a6-9a04-824febf737a0 |
| Jogador 6 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2713896334171295 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 27 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13695326447486877 | 0.0 | 0.0 | +— / -3cb4d077-df9a-4fd2-9a68-7301aff1b657 |
| Jogador 6 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.01292484998703003 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15401549637317657 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08599413186311722 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 4.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4089018404483795 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2076815664768219 | 0.0 | 0.0 | +66f2e88b-7964-4bbe-a320-941bba893d3d / -— |
| Jogador 6 | 1-4 | 34 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00792307686060667 | 0.0 | 0.0 | +— / -66f2e88b-7964-4bbe-a320-941bba893d3d |
| Jogador 6 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20767280459403992 | 0.0 | 0.0 | +4fe99bfe-6eaa-4a36-b06e-60005fb92d30 / -— |
| Jogador 6 | 1-4 | 36 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00792307686060667 | 0.0 | 0.0 | +— / -4fe99bfe-6eaa-4a36-b06e-60005fb92d30 |
| Jogador 6 | 1-4 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0007066824473440647 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16309164464473724 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 39 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004776569548994303 | 0.0 | 0.0 | +— / -3ad41699-a484-4178-be10-d8f72dfd1f35 |
| Jogador 6 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.041443943977356 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.8864746689796448 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.18111039698123932 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4474174678325653 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.3219885230064392 | 0.0 | 0.0 | +c8b72b14-11a4-48e6-8135-41efdbc347cb / -— |
| Jogador 6 | 2-1 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.284145325422287 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0980803370475769 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 51 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.010673965327441692 | 0.0 | 0.0 | +— / -9002992e-4dcd-4fec-939c-87393464a41d |
| Jogador 6 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.28758490085601807 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 53 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.23860926926136017 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-2 | 54 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1933528035879135 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16970020532608032 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09439218044281006 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0986111192323733e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015326596796512604 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 59 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 61 | SELL | STABILIZE | 95.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34376922249794006 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-3 | 62 | BUY | STABILIZE | 95.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0363173484802246 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0749814435839653 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 64 | SELL | STABILIZE | 95.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.127399742603302 | 0.0 | 0.0 | +— / -c19cf6a8-c66e-4670-b0fc-fb83453f22e7 |
| Jogador 6 | 2-3 | 65 | BUY | STABILIZE | 95.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32433319091796875 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 66 | SELL | STABILIZE | 95.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1277114450931549 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-3 | 67 | BUY | STABILIZE | 95.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31814318895339966 | 0.0 | 0.0 | +2ef60eed-d073-41a6-adec-4466c673b313 / -— |
| Jogador 6 | 2-3 | 68 | BUY_XP | STABILIZE | 95.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 69 | BUY_XP | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 71 | SELL | SLOWROLL | 90.0 | 5 | 11 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1269754022359848 | 0.0 | 0.0 | +— / -2ef60eed-d073-41a6-adec-4466c673b313 |
| Jogador 6 | 2-4 | 72 | BUY | SLOWROLL | 90.0 | 5 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.048998042941093445 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 73 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 10 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40970510244369507 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 74 | BUY | SLOWROLL | 90.0 | 5 | 10 | 1 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2301638424396515 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 75 | SELL | SLOWROLL | 90.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01610327884554863 | 0.0 | 0.0 | +— / -18934be2-4988-4f62-9f62-07ba151231f2 |
| Jogador 6 | 2-4 | 76 | BUY | SLOWROLL | 90.0 | 5 | 10 | 1 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23021085560321808 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 77 | BUY_XP | SLOWROLL | 90.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 78 | BUY_XP | SLOWROLL | 90.0 | 5 | 5 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 79 | SELL | SLOWROLL | 90.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Hecarim | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039724234491586685 | 0.0 | 0.0 | +— / -53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 2-5 | 81 | BUY | SLOWROLL | 90.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19693951308727264 | 0.0 | 0.0 | +0023f061-5310-4e39-849a-22ad49993d8c / -— |
| Jogador 6 | 2-5 | 82 | SELL | SLOWROLL | 90.0 | 5 | 6 | 0 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3349076807498932 | 0.0 | 0.0 | +— / -0023f061-5310-4e39-849a-22ad49993d8c |
| Jogador 6 | 2-5 | 83 | BUY | SLOWROLL | 90.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3234667479991913 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 84 | SELL | SLOWROLL | 90.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15681537985801697 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-5 | 85 | BUY | SLOWROLL | 90.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23857758939266205 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 86 | BUY_XP | SLOWROLL | 90.0 | 5 | 6 | 0 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 87 | SELL | SLOWROLL | 90.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08583714812994003 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 88 | BUY_XP | SLOWROLL | 90.0 | 5 | 4 | 0 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.006550000049173832 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 89 | MOVE_BOARD | SLOWROLL | 90.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Hecarim | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 91 | BUY | SLOWROLL | 90.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9587361812591553 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 92 | MOVE_BENCH | SLOWROLL | 90.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05359968915581703 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 93 | BUY | FAST8 | 90.0 | 6 | 3 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.24873733520507812 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 94 | MOVE_BOARD | FAST8 | 90.0 | 6 | 0 | 0 | 28.0 | Vivaz/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 95 | SELL | FAST8 | 90.0 | 6 | 0 | 0 | 28.0 | Vivaz/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12524615228176117 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 96 | BUY | FAST8 | 90.0 | 6 | 3 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.06962417811155319 | 0.0 | 0.0 | +2a7dd07f-3b48-489c-8822-9ec2434a01cf / -— |
| Jogador 6 | 2-6 | 97 | MOVE_BOARD | FAST8 | 90.0 | 6 | 1 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 98 | MOVE_BOARD | FAST8 | 90.0 | 6 | 1 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 99 | PASS | FAST8 | 90.0 | 6 | 1 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 101 | SELL | FAST8 | 90.0 | 6 | 8 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23135215044021606 | 0.0 | 0.0 | +— / -2a7dd07f-3b48-489c-8822-9ec2434a01cf |
| Jogador 6 | 2-7 | 102 | BUY | FAST8 | 90.0 | 6 | 10 | 1 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1676051914691925 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 103 | SELL | FAST8 | 90.0 | 6 | 7 | 0 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04617633670568466 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 104 | BUY | FAST8 | 90.0 | 6 | 10 | 1 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.032827552407979965 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 105 | MOVE_BOARD | FAST8 | 90.0 | 6 | 7 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.492781100561842e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 106 | MOVE_BENCH | FAST8 | 90.0 | 6 | 7 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012421754654496908 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 107 | SELL | FAST8 | 90.0 | 6 | 7 | 0 | 30.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3962647020816803 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-7 | 108 | BUY | FAST8 | 90.0 | 6 | 9 | 0 | 30.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32699400186538696 | 0.0 | 0.0 | +dc83202b-476c-4438-90aa-a615b764b7e4 / -— |
| Jogador 6 | 2-7 | 109 | BUY_XP | FAST8 | 90.0 | 6 | 8 | 0 | 30.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 111 | SELL | FAST8 | 90.0 | 6 | 10 | 1 | 30.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.35641416907310486 | 0.0 | 0.0 | +— / -dc83202b-476c-4438-90aa-a615b764b7e4 |
| Jogador 6 | 3-1 | 112 | BUY | FAST8 | 90.0 | 6 | 11 | 1 | 30.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.09366711229085922 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 113 | MOVE_BENCH | FAST8 | 90.0 | 6 | 8 | 0 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03878050297498703 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 114 | SELL | FAST8 | 90.0 | 6 | 8 | 0 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05847399681806564 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-1 | 115 | BUY | FAST8 | 90.0 | 6 | 11 | 1 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.16566380858421326 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 116 | CRAFT_AND_EQUIP | FAST8 | 90.0 | 6 | 7 | 0 | 30.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22318242490291595 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 117 | MOVE_BENCH | FAST8 | 90.0 | 6 | 7 | 0 | 30.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7609969973564148 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 118 | MOVE_BENCH | FAST8 | 90.0 | 6 | 7 | 0 | 32.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39126551151275635 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 119 | PASS | FAST8 | 90.0 | 6 | 7 | 0 | 32.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 121 | SELL | FAST8 | 90.0 | 6 | 14 | 1 | 32.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.798529326915741 | 0.0 | 0.0 | +— / -75005e9c-56d1-48d6-815e-573e489e3dd7 |
| Jogador 6 | 3-2 | 122 | EQUIP_FROM_INVENTORY | FAST8 | 90.0 | 6 | 17 | 1 | 32.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13006329536437988 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 123 | BUY | FAST8 | 90.0 | 6 | 17 | 1 | 32.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2052706778049469 | 0.0 | 0.0 | +9204a42c-6310-4b08-9bc7-8a2e786b077a / -— |
| Jogador 6 | 3-2 | 124 | MOVE_BENCH | FAST8 | 90.0 | 6 | 15 | 1 | 32.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06557948887348175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 125 | SELL | FAST8 | 90.0 | 6 | 15 | 1 | 28.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08764103800058365 | 0.0 | 0.0 | +— / -4eedd873-e4ec-41e5-9f5e-48e443e80f86 |
| Jogador 6 | 3-2 | 126 | BUY | FAST8 | 90.0 | 6 | 19 | 1 | 28.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2591376006603241 | 0.0 | 0.0 | +6e096b30-0b49-4a98-8596-8b05089793ae / -— |
| Jogador 6 | 3-2 | 127 | MOVE_BENCH | FAST8 | 90.0 | 6 | 16 | 1 | 28.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.703635573387146 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 128 | MOVE_BENCH | FAST8 | 90.0 | 6 | 16 | 1 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08273091912269592 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 129 | BUY_XP | FAST8 | 90.0 | 6 | 16 | 1 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 131 | SELL | FAST8 | 79.0 | 6 | 18 | 1 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0989999994635582 | 0.0 | 0.0 | +— / -c8b72b14-11a4-48e6-8135-41efdbc347cb |
| Jogador 6 | 3-3 | 132 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 6 | 20 | 2 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08548164367675781 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 133 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 6 | 20 | 2 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06019896641373634 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 134 | BUY | FAST8 | 79.0 | 6 | 20 | 2 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6641502380371094 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 135 | MOVE_BENCH | FAST8 | 79.0 | 6 | 17 | 1 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09964619576931 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 136 | SELL | FAST8 | 79.0 | 6 | 17 | 1 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10100000351667404 | 0.0 | 0.0 | +— / -6e096b30-0b49-4a98-8596-8b05089793ae |
| Jogador 6 | 3-3 | 137 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 6 | 20 | 2 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13009774684906006 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 138 | BUY | FAST8 | 79.0 | 6 | 20 | 2 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13394761085510254 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 139 | BUY_XP | FAST8 | 79.0 | 6 | 17 | 1 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 141 | SELL | FAST8 | 68.0 | 6 | 20 | 2 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17250768840312958 | 0.0 | 0.0 | +— / -ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b |
| Jogador 6 | 3-4 | 142 | BUY | FAST8 | 68.0 | 6 | 23 | 2 | 30.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04096226766705513 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 143 | MOVE_BENCH | FAST8 | 68.0 | 6 | 19 | 1 | 30.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39915093779563904 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 144 | MOVE_BENCH | FAST8 | 68.0 | 6 | 19 | 1 | 32.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08429010957479477 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 145 | SELL | FAST8 | 68.0 | 6 | 19 | 1 | 34.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05181436240673065 | 0.0 | 0.0 | +— / -9204a42c-6310-4b08-9bc7-8a2e786b077a |
| Jogador 6 | 3-4 | 146 | BUY | FAST8 | 68.0 | 6 | 21 | 2 | 34.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.05992135778069496 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 147 | BUY_XP | FAST8 | 68.0 | 6 | 18 | 1 | 34.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 148 | BUY_XP | FAST8 | 68.0 | 6 | 14 | 1 | 34.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 149 | BUY_XP | FAST8 | 68.0 | 6 | 10 | 1 | 34.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02290000021457672 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 151 | MOVE_BENCH | FAST8 | 68.0 | 7 | 12 | 1 | 34.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4136165678501129 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 152 | BUY | FAST8 | 68.0 | 7 | 12 | 1 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17619329690933228 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-5 | 153 | SELL | FAST8 | 68.0 | 7 | 9 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22835242748260498 | 0.0 | 0.0 | +— / -5b95b64a-b46a-4827-8613-307c8dadc072 |
| Jogador 6 | 3-5 | 154 | BUY | FAST8 | 68.0 | 7 | 12 | 1 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17623446881771088 | 0.0 | 0.0 | +9443e3b5-f0a2-4ab7-8378-907a3d2bccaa / -— |
| Jogador 6 | 3-5 | 155 | BUY_XP | FAST8 | 68.0 | 7 | 9 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 156 | BUY_XP | FAST8 | 68.0 | 7 | 5 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 157 | MOVE_BOARD | FAST8 | 68.0 | 7 | 1 | 0 | 40.0 | Vivaz/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 158 | MOVE_BOARD | FAST8 | 68.0 | 7 | 1 | 0 | 40.0 | Vivaz/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 159 | PASS | FAST8 | 68.0 | 7 | 1 | 0 | 40.0 | Vivaz/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 161 | SELL | FAST8 | 57.0 | 7 | 7 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22845743596553802 | 0.0 | 0.0 | +— / -9443e3b5-f0a2-4ab7-8378-907a3d2bccaa |
| Jogador 6 | 3-6 | 162 | BUY | FAST8 | 57.0 | 7 | 10 | 1 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6469922661781311 | 0.0 | 0.0 | +69ccc61a-403b-4025-8359-b2061dc6ad10 / -— |
| Jogador 6 | 3-6 | 163 | SELL | FAST8 | 57.0 | 7 | 7 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24924686551094055 | 0.0 | 0.0 | +— / -69ccc61a-403b-4025-8359-b2061dc6ad10 |
| Jogador 6 | 3-6 | 164 | BUY | FAST8 | 57.0 | 7 | 10 | 1 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6473046541213989 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 6 | 3-6 | 165 | BUY_XP | FAST8 | 57.0 | 7 | 7 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 166 | MOVE_BOARD | FAST8 | 57.0 | 7 | 3 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 167 | MOVE_BOARD | FAST8 | 57.0 | 7 | 3 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014894531108438969 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 168 | PASS | FAST8 | 57.0 | 7 | 3 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 171 | SELL | FAST8 | 57.0 | 7 | 9 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24947881698608398 | 0.0 | 0.0 | +— / -d69fa0dc-74b6-4ee7-90f7-aaca5405c59c |
| Jogador 6 | 3-7 | 172 | BUY | FAST8 | 57.0 | 7 | 12 | 1 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1296994537115097 | 0.0 | 0.0 | +75d9034d-80ed-40d3-a330-44554cc2bb9e / -— |
| Jogador 6 | 3-7 | 173 | MOVE_BENCH | FAST8 | 57.0 | 7 | 7 | 0 | 40.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08714817464351654 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 174 | BUY_XP | FAST8 | 57.0 | 7 | 7 | 0 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 175 | MOVE_BOARD | FAST8 | 57.0 | 7 | 3 | 0 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 176 | MOVE_BOARD | FAST8 | 57.0 | 7 | 3 | 0 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 177 | PASS | FAST8 | 57.0 | 7 | 3 | 0 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 181 | SELL | FAST8 | 57.0 | 7 | 8 | 0 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09147528558969498 | 0.0 | 0.0 | +— / -d056a271-6a74-4e71-bde6-087b97d2c527 |
| Jogador 6 | 4-1 | 182 | BUY | FAST8 | 57.0 | 7 | 12 | 1 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.6839182376861572 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -2938180d-94e5-4bb7-832e-baa51f820ba2,50f9a30c-27db-4ed0-804e-548f87950b17 |
| Jogador 6 | 4-1 | 183 | MOVE_BENCH | FAST8 | 57.0 | 7 | 9 | 0 | 30.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3498266339302063 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 184 | BUY | FAST8 | 57.0 | 7 | 9 | 0 | 42.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.5272338390350342 | 0.0 | 0.0 | +f394f34c-c68b-4213-9eb0-88f302976405 / -— |
| Jogador 6 | 4-1 | 185 | MOVE_BOARD | FAST8 | 57.0 | 7 | 6 | 0 | 42.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 186 | MOVE_BOARD | FAST8 | 57.0 | 7 | 6 | 0 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 187 | PASS | FAST8 | 57.0 | 7 | 6 | 0 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 189 | MOVE_BENCH | FAST8 | 57.0 | 7 | 6 | 0 | 42.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09731791913509369 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 191 | BUY | FAST8 | 57.0 | 7 | 13 | 1 | 48.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.10306613892316818 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 6 | 4-2 | 192 | MOVE_BOARD | FAST8 | 57.0 | 7 | 9 | 0 | 48.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.00017414905596524477 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 193 | CRAFT_AND_EQUIP | FAST8 | 57.0 | 7 | 9 | 0 | 48.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17166483402252197 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 194 | CRAFT_AND_EQUIP | FAST8 | 57.0 | 7 | 9 | 0 | 48.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13184474408626556 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 195 | MOVE_BOARD | FAST8 | 57.0 | 7 | 9 | 0 | 48.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 196 | MOVE_BOARD | FAST8 | 57.0 | 7 | 9 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 197 | PASS | FAST8 | 57.0 | 7 | 9 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 201 | BUY | FAST8 | 57.0 | 7 | 17 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7760111093521118 | 0.0 | 0.0 | +11b28280-bb53-4ca7-81b7-5ce8705303a5 / -— |
| Jogador 6 | 4-3 | 202 | BUY | FAST8 | 57.0 | 7 | 16 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22467227280139923 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 6 | 4-3 | 203 | BUY_XP | FAST8 | 57.0 | 7 | 12 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 204 | BUY_XP | FAST8 | 57.0 | 7 | 8 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 205 | BUY_XP | FAST8 | 57.0 | 7 | 4 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 206 | MOVE_BOARD | FAST8 | 57.0 | 7 | 0 | 0 | 48.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 207 | MOVE_BOARD | FAST8 | 57.0 | 7 | 0 | 0 | 48.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 208 | PASS | FAST8 | 57.0 | 7 | 0 | 0 | 48.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 211 | SELL | FAST8 | 44.0 | 7 | 5 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3513875901699066 | 0.0 | 0.0 | +— / -11b28280-bb53-4ca7-81b7-5ce8705303a5 |
| Jogador 6 | 4-4 | 212 | SELL | FAST8 | 44.0 | 7 | 6 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09118461608886719 | 0.0 | 0.0 | +— / -e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 |
| Jogador 6 | 4-4 | 213 | SELL | FAST8 | 44.0 | 7 | 10 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08458781242370605 | 0.0 | 0.0 | +— / -80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 6 | 4-4 | 214 | BUY | FAST8 | 44.0 | 7 | 14 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7758413553237915 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 6 | 4-4 | 215 | BUY_XP | FAST8 | 44.0 | 7 | 13 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 216 | BUY_XP | FAST8 | 44.0 | 7 | 9 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 217 | BUY_XP | FAST8 | 44.0 | 7 | 5 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0772937536239624 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 218 | SELL | ECON | 44.0 | 8 | 1 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35119494795799255 | 0.0 | 0.0 | +— / -c65dacb1-5745-49d1-b7d4-e45d8e24aa84 |
| Jogador 6 | 4-4 | 219 | BUY | ECON | 44.0 | 8 | 2 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14519260823726654 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 6 | 4-5 | 221 | SELL | ECON | 44.0 | 8 | 6 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04812810197472572 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 6 | 4-5 | 222 | BUY | ECON | 44.0 | 8 | 7 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10124099999666214 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 6 | 4-5 | 223 | SELL | ECON | 44.0 | 8 | 4 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29635384678840637 | 0.0 | 0.0 | +— / -ee67f5c6-559f-492e-9cc0-6bc19a203d6a |
| Jogador 6 | 4-5 | 224 | BUY | ECON | 44.0 | 8 | 7 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.201443612575531 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -— |
| Jogador 6 | 4-5 | 225 | BUY_XP | ECON | 44.0 | 8 | 5 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 226 | MOVE_BOARD | ECON | 44.0 | 8 | 1 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 227 | MOVE_BOARD | ECON | 44.0 | 8 | 1 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 228 | PASS | ECON | 44.0 | 8 | 1 | 0 | 48.0 | Vivaz/DA_18_GnarSmall | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 229 | MOVE_BENCH | ECON | 44.0 | 8 | 1 | 0 | 48.0 | Vivaz/DA_18_GnarSmall | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41997289657592773 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 231 | BUY | ECON | 44.0 | 8 | 7 | 0 | 52.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.711856484413147 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 6 | 4-6 | 232 | BUY | ECON | 44.0 | 8 | 4 | 0 | 52.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17319321632385254 | 0.0 | 0.0 | +5e843c10-0a8b-4781-983a-8e6e6f28253e / -— |
| Jogador 6 | 4-6 | 233 | MOVE_BOARD | ECON | 44.0 | 8 | 0 | 0 | 52.0 | Vivaz/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 234 | MOVE_BOARD | ECON | 44.0 | 8 | 0 | 0 | 52.0 | Vivaz/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 235 | PASS | ECON | 44.0 | 8 | 0 | 0 | 52.0 | Vivaz/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 241 | BUY | STABILIZE | 32.0 | 8 | 5 | 0 | 52.0 | Vivaz/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023122800514101982 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -— |
| Jogador 6 | 4-7 | 242 | MOVE_BOARD | STABILIZE | 32.0 | 8 | 1 | 0 | 52.0 | Vivaz/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 243 | MOVE_BOARD | STABILIZE | 32.0 | 8 | 1 | 0 | 52.0 | Vivaz/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 244 | PASS | STABILIZE | 32.0 | 8 | 1 | 0 | 52.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 251 | BUY | STABILIZE | 32.0 | 8 | 6 | 0 | 52.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8937788009643555 | 0.0 | 0.0 | +56332309-e8e8-464a-904f-e9253912cd2f / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 6 | 5-1 | 252 | BUY | STABILIZE | 32.0 | 8 | 3 | 0 | 46.0 | Vivaz/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2790781557559967 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 6 | 5-1 | 253 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 8 | 1 | 0 | 46.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11818765848875046 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 254 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 8 | 1 | 0 | 46.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06348345428705215 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 255 | MOVE_BOARD | STABILIZE | 32.0 | 8 | 1 | 0 | 46.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -7.100963443917863e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 256 | MOVE_BOARD | STABILIZE | 32.0 | 8 | 1 | 0 | 46.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 257 | PASS | STABILIZE | 32.0 | 8 | 1 | 0 | 46.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 259 | MOVE_BENCH | STABILIZE | 32.0 | 8 | 1 | 0 | 46.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40005552768707275 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 261 | BUY | STABILIZE | 17.0 | 8 | 7 | 0 | 50.0 | Vivaz/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31702712178230286 | 0.0 | 0.0 | +249d7b90-0660-4e4f-885a-7791c1cac21a / -— |
| Jogador 6 | 5-2 | 262 | BUY | STABILIZE | 17.0 | 8 | 4 | 0 | 50.0 | Vivaz/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32140815258026123 | 0.0 | 0.0 | +ffd44f6f-388e-4792-ae4f-77f2faa3e95f / -— |
| Jogador 6 | 5-2 | 263 | MOVE_BOARD | STABILIZE | 17.0 | 8 | 1 | 0 | 50.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 264 | MOVE_BOARD | STABILIZE | 17.0 | 8 | 1 | 0 | 50.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 265 | PASS | STABILIZE | 17.0 | 8 | 1 | 0 | 50.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 271 | BUY | ALL_IN | 1.0 | 8 | 7 | 0 | 50.0 | Vivaz/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1329917013645172 | 0.0 | 0.0 | +1cd4d2ae-a25f-4a8d-93e5-42284161b055 / -— |
| Jogador 6 | 5-3 | 272 | BUY | ALL_IN | 1.0 | 8 | 3 | 0 | 50.0 | Vivaz/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042625632137060165 | 0.0 | 0.0 | +533790d1-aca6-417d-b163-b0bda70d1500 / -— |
| Jogador 6 | 5-3 | 273 | MOVE_BOARD | ALL_IN | 1.0 | 8 | 0 | 0 | 50.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.646278277206875e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 274 | MOVE_BOARD | ALL_IN | 1.0 | 8 | 0 | 0 | 50.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 275 | MOVE_BOARD | ALL_IN | 1.0 | 8 | 0 | 0 | 50.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 276 | PASS | ALL_IN | 1.0 | 8 | 0 | 0 | 50.0 | Vivaz/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.010813108645379543 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0808350220322609 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 12 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09036853164434433 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09232266992330551 | 0.0 | 0.0 | +a529e9b4-89c2-47e0-b821-7269b112f8ef / -— |
| Jogador 7 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15925821661949158 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.180749773979187 | 0.0 | 0.0 | +00a1ebb3-acfd-44df-9190-4f51a47d48c7 / -— |
| Jogador 7 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4113059341907501 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.015600565820932388 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.26310592889785767 | 0.0 | 0.0 | +42edb83f-b613-45e2-95e2-d603ddf9d104 / -— |
| Jogador 7 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12002917379140854 | 0.0 | 0.0 | +— / -42edb83f-b613-45e2-95e2-d603ddf9d104 |
| Jogador 7 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2604559063911438 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2675572335720062 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0398356132209301 | 0.0 | 0.0 | +— / -00a1ebb3-acfd-44df-9190-4f51a47d48c7 |
| Jogador 7 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.2916627824306488 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009244980756193399 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 28 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4168032109737396 | 0.0 | 0.0 | +— / -7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.23583656549453735 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-4 | 31 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10325230658054352 | 0.0 | 0.0 | +— / -96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24890105426311493 | 0.0 | 0.0 | +a179e7d4-31e2-4a74-9905-0daede16517e / -— |
| Jogador 7 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11785625666379929 | 0.0 | 0.0 | +— / -a179e7d4-31e2-4a74-9905-0daede16517e |
| Jogador 7 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2838601768016815 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 35 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1275964081287384 | 0.0 | 0.0 | +— / -d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2849835753440857 | 0.0 | 0.0 | +29aac672-b25c-44e5-af34-82fd8b0744f6 / -— |
| Jogador 7 | 1-4 | 37 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12790270149707794 | 0.0 | 0.0 | +— / -29aac672-b25c-44e5-af34-82fd8b0744f6 |
| Jogador 7 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.151566281914711 | 0.0 | 0.0 | +f13ddeb7-2025-4413-9c31-be5e4f907fff / -— |
| Jogador 7 | 1-4 | 39 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0042307693511247635 | 0.0 | 0.0 | +— / -f13ddeb7-2025-4413-9c31-be5e4f907fff |
| Jogador 7 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.23557446897029877 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4504946172237396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1892126053571701 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 7 | 2-1 | 44 | SELL | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4016461670398712 | 0.0 | 0.0 | +— / -42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 7 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.18894699215888977 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.34887373447418213 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0724211037158966 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 51 | SELL | STABILIZE | 100.0 | 4 | 10 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08269321918487549 | 0.0 | 0.0 | +— / -c2a4318c-af60-41e2-8e14-c3ad967569a0 |
| Jogador 7 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.16293230652809143 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.34285202622413635 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 54 | SELL | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06724615395069122 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-2 | 55 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.9249387979507446 | 0.0 | 0.0 | +98558a52-389f-46fc-b370-6345603f4103 / -— |
| Jogador 7 | 2-2 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15364709496498108 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1658572405576706 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 58 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3673235774040222 | 0.0 | 0.0 | +— / -98558a52-389f-46fc-b370-6345603f4103 |
| Jogador 7 | 2-2 | 59 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12077309191226959 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 61 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1035635769367218 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.035640001296997 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 7 | 2-3 | 63 | SELL | STABILIZE | 100.0 | 4 | 16 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7103832364082336 | 0.0 | 0.0 | +— / -4367c039-e64e-4a3c-a49f-57cb2674a08f |
| Jogador 7 | 2-3 | 64 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.011751651763916 | 0.0 | 0.0 | +0547b747-1e37-49ba-a447-67c526a8cd50 / -— |
| Jogador 7 | 2-3 | 65 | SELL | STABILIZE | 100.0 | 4 | 17 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45027458667755127 | 0.0 | 0.0 | +— / -0547b747-1e37-49ba-a447-67c526a8cd50 |
| Jogador 7 | 2-3 | 66 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12440672516822815 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 67 | SELL | STABILIZE | 100.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37640923261642456 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-3 | 68 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17349739372730255 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -— |
| Jogador 7 | 2-3 | 69 | SELL | STABILIZE | 100.0 | 4 | 17 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31290769577026367 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 2-4 | 71 | BUY | STABILIZE | 100.0 | 4 | 26 | 2 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0257666110992432 | 0.0 | 0.0 | +3280b28e-bd8f-494b-a78d-111744e2178b / -— |
| Jogador 7 | 2-4 | 72 | SELL | STABILIZE | 100.0 | 4 | 24 | 2 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6980378031730652 | 0.0 | 0.0 | +— / -3280b28e-bd8f-494b-a78d-111744e2178b |
| Jogador 7 | 2-4 | 73 | BUY | STABILIZE | 100.0 | 4 | 26 | 2 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3315126597881317 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 23 | 2 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3523436188697815 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 75 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 23 | 2 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33453452587127686 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 76 | PASS | STABILIZE | 100.0 | 4 | 23 | 2 | 18.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02142857201397419 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 81 | SELL | STABILIZE | 100.0 | 4 | 31 | 3 | 18.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00959928147494793 | 0.0 | 0.0 | +— / -734c75dd-d0f3-4b9f-abe8-a228e23557a2 |
| Jogador 7 | 2-5 | 82 | BUY | STABILIZE | 100.0 | 4 | 33 | 3 | 18.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3872271776199341 | 0.0 | 0.0 | +bd48de5d-f06b-401c-83a0-2ca5ba1043a4 / -— |
| Jogador 7 | 2-5 | 83 | SELL | STABILIZE | 100.0 | 4 | 32 | 3 | 18.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15395741164684296 | 0.0 | 0.0 | +— / -bd48de5d-f06b-401c-83a0-2ca5ba1043a4 |
| Jogador 7 | 2-5 | 84 | BUY | STABILIZE | 100.0 | 4 | 33 | 3 | 18.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14948639273643494 | 0.0 | 0.0 | +1d709136-338f-4fef-90fc-b2aa1b83d879 / -— |
| Jogador 7 | 2-5 | 85 | BUY_XP | STABILIZE | 100.0 | 4 | 31 | 3 | 18.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021080000326037407 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 86 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 27 | 2 | 18.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4129343330860138 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 87 | BUY | STABILIZE | 100.0 | 5 | 27 | 2 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3247890770435333 | 0.0 | 0.0 | +67afd567-2757-4206-bb7e-0e5af22093b3 / -— |
| Jogador 7 | 2-5 | 88 | SELL | STABILIZE | 100.0 | 5 | 26 | 2 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10666001588106155 | 0.0 | 0.0 | +— / -67afd567-2757-4206-bb7e-0e5af22093b3 |
| Jogador 7 | 2-5 | 89 | BUY | STABILIZE | 100.0 | 5 | 27 | 2 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24574145674705505 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-6 | 91 | SELL | STABILIZE | 95.0 | 5 | 33 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3366127908229828 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-6 | 92 | BUY | STABILIZE | 95.0 | 5 | 34 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19147245585918427 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 93 | SELL | STABILIZE | 95.0 | 5 | 31 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3986389636993408 | 0.0 | 0.0 | +— / -6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 2-6 | 94 | BUY | STABILIZE | 95.0 | 5 | 34 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09727668017148972 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 7 | 2-6 | 95 | SELL | STABILIZE | 95.0 | 5 | 32 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3211161494255066 | 0.0 | 0.0 | +— / -a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 7 | 2-6 | 96 | BUY | STABILIZE | 95.0 | 5 | 34 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3512957692146301 | 0.0 | 0.0 | +19cba1be-95ae-4cf0-a600-0c5eb8d081b0 / -— |
| Jogador 7 | 2-6 | 97 | SELL | STABILIZE | 95.0 | 5 | 33 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10665836930274963 | 0.0 | 0.0 | +— / -19cba1be-95ae-4cf0-a600-0c5eb8d081b0 |
| Jogador 7 | 2-6 | 98 | BUY | STABILIZE | 95.0 | 5 | 34 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04045794531702995 | 0.0 | 0.0 | +aea66e45-dc49-4efb-ba64-e7961a96e4b7 / -— |
| Jogador 7 | 2-6 | 99 | SELL | STABILIZE | 95.0 | 5 | 32 | 3 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2809999883174896 | 0.0 | 0.0 | +— / -aea66e45-dc49-4efb-ba64-e7961a96e4b7 |
| Jogador 7 | 2-7 | 101 | BUY | STABILIZE | 89.0 | 5 | 43 | 4 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0211130380630493 | 0.0 | 0.0 | +1e0a3ead-540d-4169-a1fc-3e79592564a0 / -— |
| Jogador 7 | 2-7 | 102 | SELL | SLOWROLL | 89.0 | 5 | 41 | 4 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3555919826030731 | 0.0 | 0.0 | +— / -1e0a3ead-540d-4169-a1fc-3e79592564a0 |
| Jogador 7 | 2-7 | 103 | BUY | STABILIZE | 89.0 | 5 | 43 | 4 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.039139315485954285 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 104 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 40 | 4 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7688735127449036 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 105 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 40 | 4 | 22.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08306127786636353 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 106 | SELL | STABILIZE | 89.0 | 5 | 40 | 4 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1174086481332779 | 0.0 | 0.0 | +— / -1d709136-338f-4fef-90fc-b2aa1b83d879 |
| Jogador 7 | 2-7 | 107 | BUY | STABILIZE | 89.0 | 5 | 42 | 4 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3927445113658905 | 0.0 | 0.0 | +27d39010-0eed-4f1d-9d04-2f542a31415f / -— |
| Jogador 7 | 2-7 | 108 | BUY_XP | STABILIZE | 89.0 | 5 | 41 | 4 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 109 | BUY_XP | STABILIZE | 89.0 | 5 | 37 | 3 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 111 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 5 | 42 | 4 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1227162778377533 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 112 | SELL | STABILIZE | 89.0 | 5 | 42 | 4 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15477338433265686 | 0.0 | 0.0 | +— / -27d39010-0eed-4f1d-9d04-2f542a31415f |
| Jogador 7 | 3-1 | 113 | BUY | STABILIZE | 89.0 | 5 | 43 | 4 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.25838571786880493 | 0.0 | 0.0 | +dbe9f465-e302-46d0-9bd4-93969fde6ecb / -— |
| Jogador 7 | 3-1 | 114 | BUY_XP | STABILIZE | 89.0 | 5 | 42 | 4 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011335000395774841 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 115 | SELL | STABILIZE | 89.0 | 6 | 38 | 3 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10508665442466736 | 0.0 | 0.0 | +— / -dbe9f465-e302-46d0-9bd4-93969fde6ecb |
| Jogador 7 | 3-1 | 116 | BUY | STABILIZE | 89.0 | 6 | 39 | 3 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1747085154056549 | 0.0 | 0.0 | +c114a849-aa3b-4b7f-bc26-b5b699914f0b / -— |
| Jogador 7 | 3-1 | 117 | SELL | STABILIZE | 89.0 | 6 | 38 | 3 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33616429567337036 | 0.0 | 0.0 | +— / -c114a849-aa3b-4b7f-bc26-b5b699914f0b |
| Jogador 7 | 3-1 | 118 | BUY | STABILIZE | 89.0 | 6 | 39 | 3 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2691989839076996 | 0.0 | 0.0 | +5d00c8ab-55fb-42ec-b8ec-75011c7722fc / -— |
| Jogador 7 | 3-1 | 119 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 37 | 3 | 24.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39984333515167236 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 121 | BUY | FAST8 | 89.0 | 6 | 46 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1943664401769638 | 0.0 | 0.0 | +46320c4e-6bc0-49d6-b150-be378fa422cf / -— |
| Jogador 7 | 3-2 | 122 | SELL | FAST8 | 89.0 | 6 | 43 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36710304021835327 | 0.0 | 0.0 | +— / -46320c4e-6bc0-49d6-b150-be378fa422cf |
| Jogador 7 | 3-2 | 123 | BUY | FAST8 | 89.0 | 6 | 46 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20862926542758942 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 124 | MOVE_BOARD | FAST8 | 89.0 | 6 | 43 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.66081801278051e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 125 | MOVE_BOARD | FAST8 | 89.0 | 6 | 43 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01510695181787014 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 126 | SELL | FAST8 | 89.0 | 6 | 43 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28984469175338745 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 3-2 | 127 | BUY | FAST8 | 89.0 | 6 | 46 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12363867461681366 | 0.0 | 0.0 | +8043a64c-a04d-4399-b52d-2246fe74e470 / -— |
| Jogador 7 | 3-2 | 128 | BUY_XP | FAST8 | 89.0 | 6 | 45 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 129 | BUY_XP | FAST8 | 89.0 | 6 | 41 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06909999996423721 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 131 | SELL | FAST8 | 89.0 | 6 | 47 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3363465666770935 | 0.0 | 0.0 | +— / -8043a64c-a04d-4399-b52d-2246fe74e470 |
| Jogador 7 | 3-3 | 132 | BUY | FAST8 | 89.0 | 6 | 48 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7929424047470093 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 133 | MOVE_BENCH | FAST8 | 89.0 | 6 | 45 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 134 | MOVE_BENCH | FAST8 | 89.0 | 6 | 45 | 4 | 28.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059505168348550797 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 135 | SELL | FAST8 | 89.0 | 6 | 45 | 4 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3842668831348419 | 0.0 | 0.0 | +— / -de82e676-8d8b-4437-958e-a8398a3cfade |
| Jogador 7 | 3-3 | 136 | BUY | FAST8 | 89.0 | 6 | 47 | 4 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7953417897224426 | 0.0 | 0.0 | +2399a42a-332c-42ee-9bd8-5f52bb921ffa / -— |
| Jogador 7 | 3-3 | 137 | BUY_XP | FAST8 | 89.0 | 6 | 46 | 4 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 138 | BUY_XP | FAST8 | 89.0 | 6 | 42 | 4 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06909999996423721 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 139 | BUY_XP | FAST8 | 89.0 | 6 | 38 | 3 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 141 | SELL | FAST8 | 77.0 | 6 | 42 | 4 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8084810376167297 | 0.0 | 0.0 | +— / -2399a42a-332c-42ee-9bd8-5f52bb921ffa |
| Jogador 7 | 3-4 | 142 | BUY | FAST8 | 77.0 | 6 | 43 | 4 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06413477659225464 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 143 | BUY_XP | FAST8 | 77.0 | 6 | 40 | 4 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06909999996423721 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 144 | BUY_XP | FAST8 | 77.0 | 6 | 36 | 3 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 145 | BUY_XP | FAST8 | 77.0 | 6 | 32 | 3 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004100000020116568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 146 | MOVE_BENCH | FAST8 | 77.0 | 7 | 28 | 2 | 30.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45031633973121643 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 147 | BUY | FAST8 | 77.0 | 7 | 28 | 2 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07923227548599243 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 148 | MOVE_BOARD | FAST8 | 77.0 | 7 | 25 | 2 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 149 | MOVE_BOARD | FAST8 | 77.0 | 7 | 25 | 2 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014806424267590046 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 151 | SELL | FAST8 | 77.0 | 7 | 32 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39767691493034363 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 3-5 | 152 | BUY | FAST8 | 77.0 | 7 | 35 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7679421901702881 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 153 | BUY | FAST8 | 77.0 | 7 | 32 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2509598433971405 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 7 | 3-5 | 154 | MOVE_BOARD | FAST8 | 77.0 | 7 | 30 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002827198477461934 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 155 | MOVE_BOARD | FAST8 | 77.0 | 7 | 30 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014340385794639587 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 156 | PASS | FAST8 | 77.0 | 7 | 30 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12300000339746475 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 161 | BUY | FAST8 | 77.0 | 7 | 39 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011423028074204922 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 7 | 3-6 | 162 | BUY | FAST8 | 77.0 | 7 | 35 | 3 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01351806428283453 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 7 | 3-6 | 163 | BUY | FAST8 | 77.0 | 7 | 31 | 3 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5117554068565369 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 7 | 3-6 | 164 | MOVE_BOARD | FAST8 | 77.0 | 7 | 27 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 165 | MOVE_BOARD | FAST8 | 77.0 | 7 | 27 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 166 | PASS | FAST8 | 77.0 | 7 | 27 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0794999971985817 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 171 | BUY | FAST8 | 77.0 | 7 | 36 | 3 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7101595401763916 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 7 | 3-7 | 172 | BUY | FAST8 | 77.0 | 7 | 32 | 3 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24236087501049042 | 0.0 | 0.0 | +f00503d7-4e8f-4514-acc1-d3206151acc2 / -— |
| Jogador 7 | 3-7 | 173 | BUY | FAST8 | 77.0 | 7 | 29 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24173839390277863 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 7 | 3-7 | 174 | BUY | FAST8 | 77.0 | 7 | 27 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24135209619998932 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 7 | 3-7 | 175 | REROLL | FAST8 | 77.0 | 7 | 25 | 2 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 176 | SELL | FAST8 | 77.0 | 7 | 23 | 2 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07419999688863754 | 0.0 | 0.0 | +— / -1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 |
| Jogador 7 | 3-7 | 177 | BUY | FAST8 | 77.0 | 7 | 25 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18329675495624542 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 7 | 3-7 | 178 | SELL | FAST8 | 77.0 | 7 | 22 | 2 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07900000363588333 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 7 | 3-7 | 179 | BUY | FAST8 | 77.0 | 7 | 24 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007092130370438099 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 7 | 4-1 | 181 | SELL | FAST8 | 77.0 | 7 | 29 | 2 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14900000393390656 | 0.0 | 0.0 | +— / -f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 7 | 4-1 | 182 | BUY | FAST8 | 77.0 | 7 | 32 | 3 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24069088697433472 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 7 | 4-1 | 183 | CRAFT_AND_EQUIP | FAST8 | 77.0 | 7 | 30 | 3 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11589047312736511 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 184 | CRAFT_AND_EQUIP | FAST8 | 77.0 | 7 | 30 | 3 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1139117032289505 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 185 | MOVE_BOARD | FAST8 | 77.0 | 7 | 30 | 3 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001647848403081298 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 186 | SELL | FAST8 | 77.0 | 7 | 30 | 3 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0737999975681305 | 0.0 | 0.0 | +— / -f00503d7-4e8f-4514-acc1-d3206151acc2 |
| Jogador 7 | 4-1 | 187 | BUY | FAST8 | 77.0 | 7 | 33 | 3 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4772822856903076 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 7 | 4-1 | 188 | REROLL | FAST8 | 77.0 | 7 | 31 | 3 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 189 | SELL | FAST8 | 77.0 | 7 | 29 | 2 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041676923632621765 | 0.0 | 0.0 | +— / -fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 7 | 4-2 | 191 | BUY | FAST8 | 77.0 | 7 | 41 | 4 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.77182537317276 | 0.0 | 0.0 | +2e4c09f7-35e9-41f6-9570-45e67a1d8eaf / -f116ca4e-dbe8-457e-83a5-958525aa384a,fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 4-2 | 192 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 38 | 3 | 24.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3504151403903961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 193 | BUY | FAST8 | 77.0 | 7 | 38 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16841979324817657 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 7 | 4-2 | 194 | MOVE_BOARD | FAST8 | 77.0 | 7 | 35 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.503988177224528e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 195 | MOVE_BENCH | FAST8 | 77.0 | 7 | 35 | 3 | 36.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3873324990272522 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 196 | BUY | FAST8 | 77.0 | 7 | 35 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4793555736541748 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 7 | 4-2 | 197 | REROLL | FAST8 | 77.0 | 7 | 33 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 198 | SELL | FAST8 | 77.0 | 7 | 31 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12167692184448242 | 0.0 | 0.0 | +— / -e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 7 | 4-2 | 199 | BUY | FAST8 | 77.0 | 7 | 33 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23909281194210052 | 0.0 | 0.0 | +b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 / -— |
| Jogador 7 | 4-3 | 201 | SELL | FAST8 | 64.0 | 7 | 36 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15300717949867249 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 4-3 | 202 | BUY | FAST8 | 64.0 | 7 | 39 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.761035144329071 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 7 | 4-3 | 203 | SELL | FAST8 | 64.0 | 7 | 37 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11503076553344727 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 7 | 4-3 | 204 | BUY | FAST8 | 64.0 | 7 | 40 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17479127645492554 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 7 | 4-3 | 205 | SELL | FAST8 | 64.0 | 7 | 37 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14900000393390656 | 0.0 | 0.0 | +— / -734c25e1-eddf-4452-a04a-1b39db3b94d0 |
| Jogador 7 | 4-3 | 206 | BUY | FAST8 | 64.0 | 7 | 40 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07575706392526627 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 7 | 4-3 | 207 | REROLL | FAST8 | 64.0 | 7 | 37 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 208 | SELL | FAST8 | 64.0 | 7 | 35 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05976923182606697 | 0.0 | 0.0 | +— / -5f9e16e2-0766-403f-a85a-f6a735c04261 |
| Jogador 7 | 4-3 | 209 | BUY | FAST8 | 64.0 | 7 | 38 | 3 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23797494173049927 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 7 | 4-4 | 211 | SELL | FAST8 | 53.0 | 7 | 43 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07390568405389786 | 0.0 | 0.0 | +— / -b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 |
| Jogador 7 | 4-4 | 212 | BUY | FAST8 | 53.0 | 7 | 47 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05642804130911827 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 7 | 4-4 | 213 | SELL | FAST8 | 53.0 | 7 | 42 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1298910528421402 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 7 | 4-4 | 214 | BUY | FAST8 | 53.0 | 7 | 46 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09138702601194382 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -— |
| Jogador 7 | 4-4 | 215 | SELL | FAST8 | 53.0 | 7 | 43 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0689999982714653 | 0.0 | 0.0 | +— / -023f01af-91d0-4e07-8229-2b7cded83151 |
| Jogador 7 | 4-4 | 216 | BUY | FAST8 | 53.0 | 7 | 46 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1480223834514618 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 7 | 4-4 | 217 | REROLL | FAST8 | 53.0 | 7 | 43 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 218 | SELL | FAST8 | 53.0 | 7 | 41 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0737999975681305 | 0.0 | 0.0 | +— / -3bfc4626-3226-44b6-a401-ff9c18761448 |
| Jogador 7 | 4-4 | 219 | BUY | FAST8 | 53.0 | 7 | 44 | 4 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20103830099105835 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 7 | 4-5 | 221 | SELL | FAST8 | 53.0 | 7 | 52 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05063077062368393 | 0.0 | 0.0 | +— / -b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 7 | 4-5 | 222 | BUY | FAST8 | 53.0 | 7 | 56 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20079448819160461 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 7 | 4-5 | 223 | SELL | FAST8 | 53.0 | 7 | 55 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03456922993063927 | 0.0 | 0.0 | +— / -ecf369a7-649e-45fe-ad90-8f29e1714fe6 |
| Jogador 7 | 4-5 | 224 | BUY | FAST8 | 53.0 | 7 | 56 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14687871932983398 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 7 | 4-5 | 225 | REROLL | FAST8 | 53.0 | 7 | 53 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 226 | SELL | FAST8 | 53.0 | 7 | 51 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06780000030994415 | 0.0 | 0.0 | +— / -5754c4b4-0a7d-49e5-93e4-b144c3090a41 |
| Jogador 7 | 4-5 | 227 | BUY | FAST8 | 53.0 | 7 | 54 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1675650179386139 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -— |
| Jogador 7 | 4-5 | 228 | SELL | FAST8 | 53.0 | 7 | 50 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08048176765441895 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 7 | 4-5 | 229 | BUY | FAST8 | 53.0 | 7 | 52 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4841479957103729 | 0.0 | 0.0 | +eeb774dc-b3d1-4a90-8a93-b71a9b754169 / -— |
| Jogador 7 | 4-6 | 231 | SELL | FAST8 | 41.0 | 7 | 61 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13316674530506134 | 0.0 | 0.0 | +— / -eeb774dc-b3d1-4a90-8a93-b71a9b754169 |
| Jogador 7 | 4-6 | 232 | BUY | FAST8 | 41.0 | 7 | 63 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009473958984017372 | 0.0 | 0.0 | +45b96060-6eda-4d0b-9012-e80db31b71d2 / -— |
| Jogador 7 | 4-6 | 233 | SELL | FAST8 | 41.0 | 7 | 60 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05376923084259033 | 0.0 | 0.0 | +— / -45b96060-6eda-4d0b-9012-e80db31b71d2 |
| Jogador 7 | 4-6 | 234 | BUY | FAST8 | 41.0 | 7 | 63 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08659899234771729 | 0.0 | 0.0 | +4e6b6f57-7f94-46ba-b832-c3198d4a5949 / -— |
| Jogador 7 | 4-6 | 235 | SELL | FAST8 | 41.0 | 7 | 61 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05616923049092293 | 0.0 | 0.0 | +— / -4e6b6f57-7f94-46ba-b832-c3198d4a5949 |
| Jogador 7 | 4-6 | 236 | BUY | FAST8 | 41.0 | 7 | 63 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1463489681482315 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -— |
| Jogador 7 | 4-6 | 237 | REROLL | FAST8 | 41.0 | 7 | 60 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 238 | SELL | FAST8 | 41.0 | 7 | 58 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06780000030994415 | 0.0 | 0.0 | +— / -b6883c6a-7149-4088-8506-20bd8dfed6a5 |
| Jogador 7 | 4-6 | 239 | BUY | FAST8 | 41.0 | 7 | 61 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2995510399341583 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 7 | 4-7 | 241 | SELL | STABILIZE | 29.0 | 7 | 69 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.290677547454834 | 0.0 | 0.0 | +— / -45da6d00-829e-4e2e-a1a5-318498fd007b |
| Jogador 7 | 4-7 | 242 | BUY | STABILIZE | 29.0 | 7 | 71 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7827920913696289 | 0.0 | 0.0 | +551e9535-d584-4055-a544-ed78d65ecacb / -— |
| Jogador 7 | 4-7 | 243 | SELL | STABILIZE | 29.0 | 7 | 68 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05178721994161606 | 0.0 | 0.0 | +— / -d9fdb961-a3e3-4e39-9970-e46ffd59fc3b |
| Jogador 7 | 4-7 | 244 | BUY | STABILIZE | 29.0 | 7 | 70 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3631049394607544 | 0.0 | 0.0 | +d3fddd9d-ee81-418d-9c58-0baa4ed99f61 / -— |
| Jogador 7 | 4-7 | 245 | SELL | STABILIZE | 29.0 | 7 | 67 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052520547062158585 | 0.0 | 0.0 | +— / -5a6985d6-5377-425c-b4a3-c53dc138b288 |
| Jogador 7 | 4-7 | 246 | BUY | STABILIZE | 29.0 | 7 | 71 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40967684984207153 | 0.0 | 0.0 | +08731924-b808-4070-8c85-2c747847d835 / -— |
| Jogador 7 | 4-7 | 247 | REROLL | STABILIZE | 29.0 | 7 | 68 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 248 | SELL | STABILIZE | 29.0 | 7 | 66 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11843127012252808 | 0.0 | 0.0 | +— / -08731924-b808-4070-8c85-2c747847d835 |
| Jogador 7 | 4-7 | 249 | BUY | STABILIZE | 29.0 | 7 | 69 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10669194906949997 | 0.0 | 0.0 | +8068dc77-9528-4a1d-b4dc-5ac216e8684f / -— |
| Jogador 7 | 5-1 | 251 | SELL | STABILIZE | 29.0 | 7 | 76 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05986153706908226 | 0.0 | 0.0 | +— / -8068dc77-9528-4a1d-b4dc-5ac216e8684f |
| Jogador 7 | 5-1 | 252 | BUY | STABILIZE | 29.0 | 7 | 80 | 5 | 42.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0196927785873413 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -1fa69553-5270-4459-986b-600f748711b7,551e9535-d584-4055-a544-ed78d65ecacb |
| Jogador 7 | 5-1 | 253 | BUY | STABILIZE | 29.0 | 7 | 77 | 5 | 36.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.014283811673521996 | 0.0 | 0.0 | +85d35881-ba70-4310-8d5f-bae796309eed / -— |
| Jogador 7 | 5-1 | 254 | MOVE_BENCH | STABILIZE | 29.0 | 7 | 75 | 5 | 36.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.40390297770500183 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 255 | BUY | STABILIZE | 29.0 | 7 | 75 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.030102329328656197 | 0.0 | 0.0 | +b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 / -— |
| Jogador 7 | 5-1 | 256 | CRAFT_AND_EQUIP | STABILIZE | 29.0 | 7 | 73 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16883328557014465 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 257 | CRAFT_AND_EQUIP | STABILIZE | 29.0 | 7 | 73 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09044346213340759 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 258 | REROLL | STABILIZE | 29.0 | 7 | 73 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 259 | SELL | STABILIZE | 29.0 | 7 | 71 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06724615395069122 | 0.0 | 0.0 | +— / -b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 |
| Jogador 7 | 5-2 | 261 | BUY | STABILIZE | 29.0 | 7 | 84 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18784505128860474 | 0.0 | 0.0 | +5184a53b-fca3-448c-b5ab-7daa37b0c259 / -— |
| Jogador 7 | 5-2 | 262 | SELL | STABILIZE | 29.0 | 7 | 81 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06899028271436691 | 0.0 | 0.0 | +— / -85d35881-ba70-4310-8d5f-bae796309eed |
| Jogador 7 | 5-2 | 263 | BUY | STABILIZE | 29.0 | 7 | 83 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10675517469644547 | 0.0 | 0.0 | +f1ece814-0986-421f-b5df-0b457ebaa484 / -— |
| Jogador 7 | 5-2 | 264 | REROLL | STABILIZE | 29.0 | 7 | 80 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 265 | SELL | STABILIZE | 29.0 | 7 | 78 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.149454265832901 | 0.0 | 0.0 | +— / -bfe7ca8a-6e89-4673-b142-262e012398a9 |
| Jogador 7 | 5-2 | 266 | BUY | STABILIZE | 29.0 | 7 | 86 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8759722709655762 | 0.0 | 0.0 | +80241b75-9eb3-4b89-a754-8df65ec59786 / -— |
| Jogador 7 | 5-2 | 267 | SELL | STABILIZE | 29.0 | 7 | 83 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.053467508405447006 | 0.0 | 0.0 | +— / -f1ece814-0986-421f-b5df-0b457ebaa484 |
| Jogador 7 | 5-2 | 268 | BUY | STABILIZE | 29.0 | 7 | 86 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09499435126781464 | 0.0 | 0.0 | +6875f839-cf68-443f-9776-887087b375d3 / -— |
| Jogador 7 | 5-2 | 269 | REROLL | STABILIZE | 29.0 | 7 | 84 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 271 | SELL | ALL_IN | 13.0 | 7 | 92 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06096922978758812 | 0.0 | 0.0 | +— / -6875f839-cf68-443f-9776-887087b375d3 |
| Jogador 7 | 5-3 | 272 | BUY | ALL_IN | 13.0 | 7 | 94 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7755410671234131 | 0.0 | 0.0 | +280265b0-7892-4e7e-b654-e2cc7b0ea97b / -— |
| Jogador 7 | 5-3 | 273 | REROLL | ALL_IN | 13.0 | 7 | 91 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 274 | SELL | ALL_IN | 13.0 | 7 | 89 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1516755223274231 | 0.0 | 0.0 | +— / -280265b0-7892-4e7e-b654-e2cc7b0ea97b |
| Jogador 7 | 5-3 | 275 | BUY | ALL_IN | 13.0 | 7 | 92 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9233429431915283 | 0.0 | 0.0 | +19e8f3ef-c3a6-459e-bf05-a53f742ba05d / -— |
| Jogador 7 | 5-3 | 276 | SELL | ALL_IN | 13.0 | 7 | 91 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3308030664920807 | 0.0 | 0.0 | +— / -19e8f3ef-c3a6-459e-bf05-a53f742ba05d |
| Jogador 7 | 5-3 | 277 | BUY | ALL_IN | 13.0 | 7 | 92 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5751339793205261 | 0.0 | 0.0 | +6fe382fd-86c3-42ec-abb7-fb52c7a19c62 / -— |
| Jogador 7 | 5-3 | 278 | REROLL | ALL_IN | 13.0 | 7 | 89 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 279 | SELL | ALL_IN | 13.0 | 7 | 87 | 5 | 46.0 | Lutador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1276332288980484 | 0.0 | 0.0 | +— / -6fe382fd-86c3-42ec-abb7-fb52c7a19c62 |
| Jogador 8 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02 |
| Jogador 8 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +d40a14f6-4b32-4cf9-8eb7-2778414b099a / -— |
| Jogador 8 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.6126748323440552 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.11927274614572525 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.011937879957258701 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24794647097587585 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 1.0161010026931763 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0010617382358759642 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43499675393104553 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.014684098772704601 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2772522568702698 | 0.0 | 0.0 | +f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 / -— |
| Jogador 8 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13131938874721527 | 0.0 | 0.0 | +— / -f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 |
| Jogador 8 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.13651145994663239 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 24 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09143692255020142 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.13592779636383057 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 26 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09143692255020142 | 0.0 | 0.0 | +— / -74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.04102791100740433 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 28 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0764707699418068 | 0.0 | 0.0 | +— / -dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.04062199592590332 | 0.0 | 0.0 | +a8449841-8124-415a-bb0f-eac35a0bd605 / -— |
| Jogador 8 | 1-4 | 31 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37647077441215515 | 0.0 | 0.0 | +— / -a8449841-8124-415a-bb0f-eac35a0bd605 |
| Jogador 8 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1164112091064453 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -78019889-2624-4adb-917b-619681f23053,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1399749219417572 | 0.0 | 0.0 | +— / -64f24363-3325-4538-972e-a6d8260b3787 |
| Jogador 8 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 7 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09938959032297134 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 6 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16000747680664062 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15655004978179932 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 37 | SELL | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39143693447113037 | 0.0 | 0.0 | +— / -4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 1-4 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0007640905678272247 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15625016391277313 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 2-1 | 41 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3114369213581085 | 0.0 | 0.0 | +— / -322e9047-623a-4fec-a0f9-d21d2fbcd88a |
| Jogador 8 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.001320870011113584 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 43 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 4.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.17573541402816772 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1776883453130722 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -— |
| Jogador 8 | 2-1 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.44272592663764954 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 46 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.1728099286556244 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -— |
| Jogador 8 | 2-1 | 47 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3254615366458893 | 0.0 | 0.0 | +— / -76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.18571609258651733 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.29657885432243347 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 51 | SELL | STABILIZE | 95.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3157755732536316 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 52 | BUY | STABILIZE | 95.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.0396053791046143 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 53 | SELL | STABILIZE | 95.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.8636220693588257 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-2 | 54 | BUY | STABILIZE | 95.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.15325769782066345 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 9 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03548421710729599 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 56 | SELL | STABILIZE | 95.0 | 4 | 9 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.036076921969652176 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 2-2 | 57 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.23328055441379547 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 58 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.015613761730492115 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 59 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19911201298236847 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 61 | SELL | STABILIZE | 89.0 | 4 | 14 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4309878945350647 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-3 | 62 | BUY | STABILIZE | 89.0 | 4 | 16 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.12833523750305176 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 63 | SELL | STABILIZE | 89.0 | 4 | 13 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.37640923261642456 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-3 | 64 | BUY | STABILIZE | 89.0 | 4 | 16 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.2774842381477356 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 65 | SELL | STABILIZE | 89.0 | 4 | 15 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.35647693276405334 | 0.0 | 0.0 | +— / -5de56114-806a-4f58-8241-b3b8434a2154 |
| Jogador 8 | 2-3 | 66 | BUY | STABILIZE | 89.0 | 4 | 16 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.25657814741134644 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 67 | SELL | STABILIZE | 89.0 | 4 | 15 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3394923210144043 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-3 | 68 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 4 | 16 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.13791394233703613 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 69 | BUY | STABILIZE | 89.0 | 4 | 16 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17742502689361572 | 0.0 | 0.0 | +491eb6b6-54f4-4de8-bc63-d96c6c1d9cce / -— |
| Jogador 8 | 2-4 | 71 | SELL | STABILIZE | 89.0 | 4 | 22 | 2 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3254615366458893 | 0.0 | 0.0 | +— / -491eb6b6-54f4-4de8-bc63-d96c6c1d9cce |
| Jogador 8 | 2-4 | 72 | BUY | STABILIZE | 89.0 | 4 | 23 | 2 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22109432518482208 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 20 | 2 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015862226486206055 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 74 | SELL | STABILIZE | 89.0 | 4 | 20 | 2 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-4 | 75 | BUY | STABILIZE | 89.0 | 4 | 21 | 2 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2601664662361145 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 76 | SELL | STABILIZE | 89.0 | 4 | 19 | 1 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02037351205945015 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-4 | 77 | BUY | STABILIZE | 89.0 | 4 | 21 | 2 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28806567192077637 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 78 | SELL | STABILIZE | 89.0 | 4 | 20 | 2 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35647693276405334 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-4 | 79 | BUY | STABILIZE | 89.0 | 4 | 21 | 2 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2880215644836426 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-5 | 81 | SELL | STABILIZE | 89.0 | 4 | 27 | 2 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35647693276405334 | 0.0 | 0.0 | +— / -3644801e-2247-403d-8b81-d2d3f15c2f55 |
| Jogador 8 | 2-5 | 82 | BUY | STABILIZE | 89.0 | 4 | 28 | 2 | 18.0 | Rival/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3540542721748352 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 83 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 25 | 2 | 18.0 | Rival/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5987852811813354 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 84 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 25 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06678210943937302 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 85 | SELL | STABILIZE | 89.0 | 4 | 25 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06695692241191864 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 2-5 | 86 | BUY | STABILIZE | 89.0 | 4 | 28 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.36611098051071167 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 87 | SELL | STABILIZE | 89.0 | 4 | 26 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11988771706819534 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 2-5 | 88 | BUY | STABILIZE | 89.0 | 4 | 28 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3788760304450989 | 0.0 | 0.0 | +cf4575c2-3622-4493-91f1-c5efbe1fbd8b / -— |
| Jogador 8 | 2-5 | 89 | SELL | STABILIZE | 89.0 | 4 | 27 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09364542365074158 | 0.0 | 0.0 | +— / -cf4575c2-3622-4493-91f1-c5efbe1fbd8b |
| Jogador 8 | 2-6 | 91 | BUY | STABILIZE | 84.0 | 5 | 35 | 3 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3997802436351776 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 92 | SELL | STABILIZE | 84.0 | 5 | 32 | 3 | 18.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4962517321109772 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 2-6 | 93 | BUY | STABILIZE | 84.0 | 5 | 35 | 3 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27580487728118896 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 94 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 32 | 3 | 18.0 | Vivaz/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4300084412097931 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 95 | BUY | STABILIZE | 84.0 | 5 | 32 | 3 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3491990864276886 | 0.0 | 0.0 | +c9a1ea77-662a-469a-ba7f-eac0713c0c52 / -— |
| Jogador 8 | 2-6 | 96 | BUY_XP | STABILIZE | 84.0 | 5 | 30 | 3 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 97 | BUY_XP | STABILIZE | 84.0 | 5 | 26 | 2 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 98 | BUY_XP | STABILIZE | 84.0 | 5 | 22 | 2 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 99 | BUY_XP | STABILIZE | 84.0 | 5 | 18 | 1 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 101 | SELL | STABILIZE | 77.0 | 5 | 21 | 2 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12069549411535263 | 0.0 | 0.0 | +— / -c9a1ea77-662a-469a-ba7f-eac0713c0c52 |
| Jogador 8 | 2-7 | 102 | BUY | STABILIZE | 77.0 | 5 | 23 | 2 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.055786371231079 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 103 | BUY_XP | SLOWROLL | 77.0 | 5 | 22 | 2 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050769999623298645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 104 | SELL | SLOWROLL | 77.0 | 6 | 18 | 1 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8872566223144531 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 2-7 | 105 | BUY | STABILIZE | 77.0 | 6 | 19 | 1 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3189365863800049 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 106 | SELL | STABILIZE | 77.0 | 6 | 16 | 1 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1317744106054306 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 2-7 | 107 | BUY | STABILIZE | 77.0 | 6 | 19 | 1 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07669039070606232 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 108 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 16 | 1 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40234309434890747 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 109 | MOVE_BOARD | FAST8 | 77.0 | 6 | 16 | 1 | 30.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04968150332570076 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 111 | BUY | FAST8 | 77.0 | 6 | 23 | 2 | 30.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.024110285565257072 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 112 | MOVE_BENCH | FAST8 | 77.0 | 6 | 19 | 1 | 30.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.31678131222724915 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 113 | CRAFT_AND_EQUIP | FAST8 | 77.0 | 6 | 19 | 1 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1505950391292572 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 114 | MOVE_BOARD | FAST8 | 77.0 | 6 | 19 | 1 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 115 | MOVE_BOARD | FAST8 | 77.0 | 6 | 19 | 1 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 116 | PASS | FAST8 | 77.0 | 6 | 19 | 1 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 121 | SELL | FAST8 | 66.0 | 6 | 26 | 2 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09981276839971542 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 3-2 | 122 | BUY | FAST8 | 66.0 | 6 | 28 | 2 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7701748609542847 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 123 | SELL | FAST8 | 66.0 | 6 | 27 | 2 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8801143765449524 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 124 | BUY | FAST8 | 66.0 | 6 | 28 | 2 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.24659623205661774 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 125 | MOVE_BENCH | FAST8 | 66.0 | 6 | 24 | 2 | 34.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3999478220939636 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 126 | BUY_XP | FAST8 | 66.0 | 6 | 24 | 2 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 127 | BUY_XP | FAST8 | 66.0 | 6 | 20 | 2 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 128 | BUY_XP | FAST8 | 66.0 | 6 | 16 | 1 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 129 | BUY_XP | FAST8 | 66.0 | 6 | 12 | 1 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 131 | SELL | FAST8 | 66.0 | 6 | 14 | 1 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20249025523662567 | 0.0 | 0.0 | +— / -d40a14f6-4b32-4cf9-8eb7-2778414b099a |
| Jogador 8 | 3-3 | 132 | EQUIP_FROM_INVENTORY | FAST8 | 66.0 | 6 | 15 | 1 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10505809634923935 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 133 | EQUIP_FROM_INVENTORY | FAST8 | 66.0 | 6 | 15 | 1 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0457490012049675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 134 | BUY | FAST8 | 66.0 | 6 | 15 | 1 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.702340841293335 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 135 | BUY_XP | FAST8 | 66.0 | 6 | 12 | 1 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 136 | BUY_XP | FAST8 | 66.0 | 6 | 8 | 0 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 137 | BUY_XP | FAST8 | 66.0 | 6 | 4 | 0 | 40.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 138 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 40.0 | Devastador/DA_18_Sett | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1254262972215656e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 139 | MOVE_BENCH | FAST8 | 66.0 | 7 | 0 | 0 | 40.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5072765946388245 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 141 | BUY | FAST8 | 66.0 | 7 | 7 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09205860644578934 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 142 | SELL | FAST8 | 66.0 | 7 | 4 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30471640825271606 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-4 | 143 | BUY | FAST8 | 66.0 | 7 | 7 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09227010607719421 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 144 | BUY_XP | FAST8 | 66.0 | 7 | 4 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 145 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 146 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 147 | PASS | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Sett | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 151 | SELL | FAST8 | 66.0 | 7 | 6 | 0 | 46.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008030716329813004 | 0.0 | 0.0 | +— / -d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 3-5 | 152 | BUY | FAST8 | 66.0 | 7 | 9 | 0 | 46.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.621282696723938 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 153 | SELL | FAST8 | 66.0 | 7 | 6 | 0 | 46.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41510429978370667 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 3-5 | 154 | BUY | FAST8 | 66.0 | 7 | 9 | 0 | 46.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2104238122701645 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 155 | BUY_XP | FAST8 | 66.0 | 7 | 6 | 0 | 46.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 156 | SELL | FAST8 | 66.0 | 7 | 2 | 0 | 46.0 | Devastador/DA_18_Sett | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13075999915599823 | 0.0 | 0.0 | +— / -9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-5 | 157 | BUY | FAST8 | 66.0 | 7 | 5 | 0 | 46.0 | Devastador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0330011248588562 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -— |
| Jogador 8 | 3-5 | 158 | MOVE_BOARD | FAST8 | 66.0 | 7 | 2 | 0 | 46.0 | Devastador/DA_18_Sett | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 159 | MOVE_BOARD | FAST8 | 66.0 | 7 | 2 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014959576539695263 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 161 | BUY | FAST8 | 66.0 | 7 | 9 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21531307697296143 | 0.0 | 0.0 | +0d8cf876-2884-4724-ab79-246f8e0406f0 / -— |
| Jogador 8 | 3-6 | 162 | BUY | FAST8 | 66.0 | 7 | 7 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16406233608722687 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 8 | 3-6 | 163 | BUY_XP | FAST8 | 66.0 | 7 | 4 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 164 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 165 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 166 | PASS | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 171 | BUY | FAST8 | 66.0 | 7 | 7 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.601999819278717 | 0.0 | 0.0 | +f8d6cf7b-e18c-4a52-87c6-8858f03eef72 / -— |
| Jogador 8 | 3-7 | 172 | MOVE_BOARD | FAST8 | 66.0 | 7 | 4 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00012220362259540707 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 173 | BUY_XP | FAST8 | 66.0 | 7 | 4 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 174 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 175 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 176 | PASS | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 181 | BUY | FAST8 | 66.0 | 7 | 6 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.10852520912885666 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -— |
| Jogador 8 | 4-1 | 182 | CRAFT_AND_EQUIP | FAST8 | 66.0 | 7 | 3 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24443623423576355 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 183 | CRAFT_AND_EQUIP | FAST8 | 66.0 | 7 | 3 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.199350968003273 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 184 | BUY | FAST8 | 66.0 | 7 | 3 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024868294596672058 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 8 | 4-1 | 185 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 186 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 187 | PASS | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 191 | BUY | FAST8 | 66.0 | 7 | 8 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7352465987205505 | 0.0 | 0.0 | +2357a4df-3c61-4957-83c3-572bbb99ac5a / -— |
| Jogador 8 | 4-2 | 192 | BUY | FAST8 | 66.0 | 7 | 6 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04762643203139305 | 0.0 | 0.0 | +6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 / -— |
| Jogador 8 | 4-2 | 193 | BUY | FAST8 | 66.0 | 7 | 2 | 0 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19962167739868164 | 0.0 | 0.0 | +3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 / -— |
| Jogador 8 | 4-2 | 194 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 195 | MOVE_BOARD | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01469587441533804 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 196 | PASS | FAST8 | 66.0 | 7 | 0 | 0 | 46.0 | Devastador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 201 | SELL | FAST8 | 66.0 | 7 | 9 | 0 | 46.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04275989904999733 | 0.0 | 0.0 | +— / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 |
| Jogador 8 | 4-3 | 202 | BUY | FAST8 | 66.0 | 7 | 12 | 1 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6539559960365295 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 8 | 4-3 | 203 | REROLL | FAST8 | 66.0 | 7 | 9 | 0 | 46.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 204 | SELL | FAST8 | 66.0 | 7 | 7 | 0 | 46.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14448106288909912 | 0.0 | 0.0 | +— / -f8d6cf7b-e18c-4a52-87c6-8858f03eef72 |
| Jogador 8 | 4-3 | 205 | BUY | FAST8 | 66.0 | 7 | 10 | 1 | 46.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6839981079101562 | 0.0 | 0.0 | +652568b9-7093-4e77-8b9c-7ed286cf7f4c / -111acae7-a889-409f-a15e-419d250fccd0,6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 4-3 | 206 | BUY | FAST8 | 66.0 | 7 | 7 | 0 | 40.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0824229046702385 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -— |
| Jogador 8 | 4-3 | 207 | REROLL | FAST8 | 66.0 | 7 | 5 | 0 | 40.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 208 | SELL | FAST8 | 66.0 | 7 | 3 | 0 | 40.0 | Devastador/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10045728087425232 | 0.0 | 0.0 | +— / -652568b9-7093-4e77-8b9c-7ed286cf7f4c |
| Jogador 8 | 4-3 | 209 | MOVE_BENCH | FAST8 | 66.0 | 7 | 11 | 1 | 40.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.43559321761131287 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 211 | EQUIP_FROM_INVENTORY | FAST8 | 66.0 | 7 | 20 | 2 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08276107907295227 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 212 | EQUIP_FROM_INVENTORY | FAST8 | 66.0 | 7 | 20 | 2 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07730767875909805 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 213 | BUY | FAST8 | 66.0 | 7 | 20 | 2 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1503491848707199 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 8 | 4-4 | 214 | BUY | FAST8 | 66.0 | 7 | 17 | 1 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1843070685863495 | 0.0 | 0.0 | +5c931416-3aeb-40d4-9e6f-612b0d387226 / -— |
| Jogador 8 | 4-4 | 215 | REROLL | FAST8 | 66.0 | 7 | 14 | 1 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 216 | SELL | FAST8 | 66.0 | 7 | 12 | 1 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08100000023841858 | 0.0 | 0.0 | +— / -5c931416-3aeb-40d4-9e6f-612b0d387226 |
| Jogador 8 | 4-4 | 217 | BUY | FAST8 | 66.0 | 7 | 15 | 1 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.613051176071167 | 0.0 | 0.0 | +06332ba7-fc4e-431e-ab25-2fb284c08c33 / -— |
| Jogador 8 | 4-4 | 218 | REROLL | FAST8 | 66.0 | 7 | 12 | 1 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 219 | SELL | FAST8 | 66.0 | 7 | 10 | 1 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05976923182606697 | 0.0 | 0.0 | +— / -7fd8b302-97aa-4373-94f4-adfcad477ed2 |
| Jogador 8 | 4-5 | 221 | BUY | FAST8 | 66.0 | 7 | 22 | 2 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6709852814674377 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -— |
| Jogador 8 | 4-5 | 222 | REROLL | FAST8 | 66.0 | 7 | 19 | 1 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 223 | SELL | FAST8 | 66.0 | 7 | 17 | 1 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04562023654580116 | 0.0 | 0.0 | +— / -06332ba7-fc4e-431e-ab25-2fb284c08c33 |
| Jogador 8 | 4-5 | 224 | BUY | FAST8 | 66.0 | 7 | 20 | 2 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7139686942100525 | 0.0 | 0.0 | +58cbdbde-2151-438c-8897-902bef9bcd92 / -02e125a0-3563-47ec-a82a-cba5178731dd,db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 8 | 4-5 | 225 | BUY | FAST8 | 66.0 | 7 | 17 | 1 | 44.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18417659401893616 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 8 | 4-5 | 226 | BUY | FAST8 | 66.0 | 7 | 14 | 1 | 44.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19277743995189667 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 8 | 4-5 | 227 | REROLL | FAST8 | 66.0 | 7 | 12 | 1 | 44.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 228 | SELL | FAST8 | 66.0 | 7 | 10 | 1 | 44.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17997699975967407 | 0.0 | 0.0 | +— / -58cbdbde-2151-438c-8897-902bef9bcd92 |
| Jogador 8 | 4-5 | 229 | BUY | FAST8 | 66.0 | 7 | 18 | 1 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6879788637161255 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -— |
| Jogador 8 | 4-6 | 231 | SELL | FAST8 | 66.0 | 7 | 25 | 2 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07419999688863754 | 0.0 | 0.0 | +— / -ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 |
| Jogador 8 | 4-6 | 232 | BUY | FAST8 | 66.0 | 7 | 27 | 2 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05936543643474579 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 8 | 4-6 | 233 | SELL | FAST8 | 66.0 | 7 | 24 | 2 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061544619500637054 | 0.0 | 0.0 | +— / -ef54ddfd-f436-4813-9585-cb652488ffa3 |
| Jogador 8 | 4-6 | 234 | BUY | FAST8 | 66.0 | 7 | 27 | 2 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22035793960094452 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 8 | 4-6 | 235 | REROLL | FAST8 | 66.0 | 7 | 25 | 2 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 236 | SELL | FAST8 | 66.0 | 7 | 23 | 2 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03328026458621025 | 0.0 | 0.0 | +— / -4b1f1146-d580-41e9-987f-c32b1eb98b75 |
| Jogador 8 | 4-6 | 237 | BUY | FAST8 | 66.0 | 7 | 25 | 2 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19074660539627075 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -— |
| Jogador 8 | 4-6 | 238 | REROLL | FAST8 | 66.0 | 7 | 23 | 2 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 239 | SELL | FAST8 | 66.0 | 7 | 21 | 2 | 44.0 | Devastador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08100000023841858 | 0.0 | 0.0 | +— / -d381c462-a17f-4192-b694-66a7c3aaee4f |
| Jogador 8 | 4-7 | 241 | BUY | FAST8 | 66.0 | 7 | 35 | 3 | 44.0 | Devastador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8257626891136169 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -0d8cf876-2884-4724-ab79-246f8e0406f0,2357a4df-3c61-4957-83c3-572bbb99ac5a |
| Jogador 8 | 4-7 | 242 | BUY | FAST8 | 66.0 | 7 | 33 | 3 | 44.0 | Devastador/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17234110832214355 | 0.0 | 0.0 | +54574f38-262f-44ac-83da-03088b8bdea3 / -— |
| Jogador 8 | 4-7 | 243 | BUY | FAST8 | 66.0 | 7 | 30 | 3 | 44.0 | Devastador/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5973100066184998 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 8 | 4-7 | 244 | REROLL | FAST8 | 66.0 | 7 | 27 | 2 | 44.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 245 | SELL | FAST8 | 66.0 | 7 | 25 | 2 | 44.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10230047255754471 | 0.0 | 0.0 | +— / -d4c27edc-9b7e-4a31-a967-3aa80766b470 |
| Jogador 8 | 4-7 | 246 | BUY | FAST8 | 66.0 | 7 | 30 | 3 | 44.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1597651243209839 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -— |
| Jogador 8 | 4-7 | 247 | REROLL | FAST8 | 66.0 | 7 | 29 | 2 | 44.0 | Defendente/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 248 | SELL | FAST8 | 66.0 | 7 | 27 | 2 | 44.0 | Defendente/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07493846118450165 | 0.0 | 0.0 | +— / -3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 |
| Jogador 8 | 4-7 | 249 | BUY | FAST8 | 66.0 | 7 | 29 | 2 | 44.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7140180468559265 | 0.0 | 0.0 | +d58ebcea-d18b-42f8-a6ca-984d15656662 / -— |
| Jogador 8 | 5-1 | 251 | SELL | FAST8 | 66.0 | 7 | 37 | 3 | 44.0 | Defendente/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15601538121700287 | 0.0 | 0.0 | +— / -973ba75e-ffa8-41f5-a3fb-e238e34d0216 |
| Jogador 8 | 5-1 | 252 | BUY | FAST8 | 66.0 | 7 | 40 | 4 | 44.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8189353942871094 | 0.0 | 0.0 | +5098782d-1ec1-4a5b-a435-f3c84ab1be0d / -a492f78e-91f0-48cb-891a-6518551da328,c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 8 | 5-1 | 253 | BUY | FAST8 | 66.0 | 7 | 37 | 3 | 44.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6976949572563171 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -— |
| Jogador 8 | 5-1 | 254 | BUY | FAST8 | 66.0 | 7 | 33 | 3 | 44.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2637901306152344 | 0.0 | 0.0 | +63c47a3f-6712-4cfa-9376-6140da170089 / -— |
| Jogador 8 | 5-1 | 255 | CRAFT_AND_EQUIP | FAST8 | 66.0 | 7 | 31 | 3 | 44.0 | Defendente/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17556418478488922 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 256 | CRAFT_AND_EQUIP | FAST8 | 66.0 | 7 | 31 | 3 | 44.0 | Defendente/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12898992002010345 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 257 | REROLL | FAST8 | 66.0 | 7 | 31 | 3 | 44.0 | Defendente/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 258 | SELL | FAST8 | 66.0 | 7 | 29 | 2 | 44.0 | Defendente/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11900000274181366 | 0.0 | 0.0 | +— / -5098782d-1ec1-4a5b-a435-f3c84ab1be0d |
| Jogador 8 | 5-1 | 259 | BUY | FAST8 | 66.0 | 7 | 37 | 3 | 44.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030638331547379494 | 0.0 | 0.0 | +4b4293ce-1cca-473e-8c07-b441686985ac / -— |
| Jogador 8 | 5-2 | 261 | SELL | FAST8 | 66.0 | 7 | 45 | 4 | 44.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08184923231601715 | 0.0 | 0.0 | +— / -0a6e3194-ed55-43ad-ac66-31e08ccda7aa |
| Jogador 8 | 5-2 | 262 | BUY | FAST8 | 66.0 | 7 | 46 | 4 | 44.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8078761696815491 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 8 | 5-2 | 263 | SELL | FAST8 | 66.0 | 7 | 44 | 4 | 44.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06786154210567474 | 0.0 | 0.0 | +— / -4b4293ce-1cca-473e-8c07-b441686985ac |
| Jogador 8 | 5-2 | 264 | BUY | FAST8 | 66.0 | 7 | 48 | 4 | 44.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5775895118713379 | 0.0 | 0.0 | +b053a0fd-0f0b-4343-a920-f0a36d36e771 / -7915a339-3bda-4275-80ae-9941370ea609,e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 5-2 | 265 | MOVE_BENCH | FAST8 | 66.0 | 7 | 45 | 4 | 32.0 | Defendente/DA_18_KhaZix | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16255338490009308 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 266 | BUY | FAST8 | 66.0 | 7 | 45 | 4 | 38.0 | Defendente/DA_18_KhaZix | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033550430089235306 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -— |
| Jogador 8 | 5-2 | 267 | REROLL | FAST8 | 66.0 | 7 | 43 | 4 | 38.0 | Defendente/DA_18_KhaZix | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 268 | SELL | FAST8 | 66.0 | 7 | 41 | 4 | 38.0 | Defendente/DA_18_KhaZix | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11064396798610687 | 0.0 | 0.0 | +— / -b053a0fd-0f0b-4343-a920-f0a36d36e771 |
| Jogador 8 | 5-2 | 269 | MOVE_BENCH | FAST8 | 66.0 | 7 | 49 | 4 | 38.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5409548878669739 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 271 | BUY | FAST8 | 66.0 | 7 | 63 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4552517831325531 | 0.0 | 0.0 | +e32f79ba-6ddd-4e40-8150-666105cb09b7 / -— |
| Jogador 8 | 5-3 | 272 | BUY | FAST8 | 66.0 | 7 | 60 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.319966584444046 | 0.0 | 0.0 | +95113577-160e-425d-a355-0f82356246fc / -— |
| Jogador 8 | 5-3 | 273 | REROLL | FAST8 | 66.0 | 7 | 59 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 274 | SELL | FAST8 | 66.0 | 7 | 57 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12742584943771362 | 0.0 | 0.0 | +— / -e32f79ba-6ddd-4e40-8150-666105cb09b7 |
| Jogador 8 | 5-3 | 275 | BUY | FAST8 | 66.0 | 7 | 60 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35695087909698486 | 0.0 | 0.0 | +29c2eb81-6c39-41ff-96eb-a3b28d6e4b99 / -— |
| Jogador 8 | 5-3 | 276 | SELL | FAST8 | 66.0 | 7 | 57 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1035415381193161 | 0.0 | 0.0 | +— / -95113577-160e-425d-a355-0f82356246fc |
| Jogador 8 | 5-3 | 277 | BUY | FAST8 | 66.0 | 7 | 58 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9446613192558289 | 0.0 | 0.0 | +db79d601-4b72-43c1-a8e3-4755c3442aa0 / -d58ebcea-d18b-42f8-a6ca-984d15656662,d8392323-28e4-4e98-a466-5958bf400729 |
| Jogador 8 | 5-3 | 278 | BUY | FAST8 | 66.0 | 7 | 56 | 5 | 42.0 | Defendente/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20388196408748627 | 0.0 | 0.0 | +fa239e83-1e3e-45fc-8ad1-a5cee4e39b0a / -— |
| Jogador 8 | 5-3 | 279 | BUY | FAST8 | 66.0 | 7 | 52 | 5 | 42.0 | Defendente/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09590926021337509 | 0.0 | 0.0 | +bdee88f4-e5b5-48fb-9ae5-1fd155982995 / -— |
| Jogador 8 | 5-4 | 281 | SELL | FAST8 | 66.0 | 7 | 63 | 5 | 42.0 | Defendente/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1532411128282547 | 0.0 | 0.0 | +— / -db79d601-4b72-43c1-a8e3-4755c3442aa0 |
| Jogador 8 | 5-4 | 282 | BUY | FAST8 | 66.0 | 7 | 68 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499711394309998 | 0.0 | 0.0 | +6e40ac88-b1d5-4294-b92e-5bc3902fc385 / -54574f38-262f-44ac-83da-03088b8bdea3,f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 8 | 5-4 | 283 | BUY | FAST8 | 66.0 | 7 | 65 | 5 | 36.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24994060397148132 | 0.0 | 0.0 | +af23c553-04de-4813-87d0-bb7e4becafe4 / -— |
| Jogador 8 | 5-4 | 284 | REROLL | FAST8 | 66.0 | 7 | 62 | 5 | 36.0 | Defendente/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 285 | SELL | FAST8 | 66.0 | 7 | 60 | 5 | 36.0 | Defendente/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048230770975351334 | 0.0 | 0.0 | +— / -bdee88f4-e5b5-48fb-9ae5-1fd155982995 |
| Jogador 8 | 5-4 | 286 | BUY | FAST8 | 66.0 | 7 | 63 | 5 | 36.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8626089692115784 | 0.0 | 0.0 | +88249896-79bb-4f76-94a3-131d12f9fc3d / -— |
| Jogador 8 | 5-4 | 287 | MOVE_BOARD | FAST8 | 66.0 | 7 | 60 | 5 | 36.0 | Defendente/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 288 | MOVE_BOARD | FAST8 | 66.0 | 7 | 60 | 5 | 36.0 | Defendente/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010564552620053291 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 289 | MOVE_BENCH | FAST8 | 66.0 | 7 | 60 | 5 | 36.0 | Defendente/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5795155167579651 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 291 | BUY | FAST8 | 66.0 | 7 | 73 | 5 | 42.0 | Defendente/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36460787057876587 | 0.0 | 0.0 | +9b92b0ec-011f-487d-b6c8-5e95ee8b37ff / -— |
| Jogador 8 | 5-5 | 292 | SELL | FAST8 | 66.0 | 7 | 70 | 5 | 42.0 | Defendente/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18437698483467102 | 0.0 | 0.0 | +— / -6e40ac88-b1d5-4294-b92e-5bc3902fc385 |
| Jogador 8 | 5-5 | 293 | BUY | FAST8 | 66.0 | 7 | 78 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6940993070602417 | 0.0 | 0.0 | +77c36245-d5ea-4f94-bc0c-680d4a77794a / -— |
| Jogador 8 | 5-5 | 294 | REROLL | FAST8 | 66.0 | 7 | 76 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 295 | SELL | FAST8 | 66.0 | 7 | 74 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -af23c553-04de-4813-87d0-bb7e4becafe4 |
| Jogador 8 | 5-5 | 296 | BUY | FAST8 | 66.0 | 7 | 77 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009066966362297535 | 0.0 | 0.0 | +509928e4-3f42-4b0d-a71c-1a45fa23a781 / -— |
| Jogador 8 | 5-5 | 297 | REROLL | FAST8 | 66.0 | 7 | 73 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 298 | SELL | FAST8 | 66.0 | 7 | 71 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05986153706908226 | 0.0 | 0.0 | +— / -6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 |
| Jogador 8 | 5-6 | 300 | BUY | FAST8 | 66.0 | 7 | 89 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18413588404655457 | 0.0 | 0.0 | +19cbc95b-d098-4ce7-9cf5-41e4ac50d81b / -— |
| Jogador 8 | 5-6 | 301 | SELL | FAST8 | 66.0 | 7 | 86 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06909231096506119 | 0.0 | 0.0 | +— / -fa239e83-1e3e-45fc-8ad1-a5cee4e39b0a |
| Jogador 8 | 5-6 | 302 | BUY | FAST8 | 66.0 | 7 | 90 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3975985646247864 | 0.0 | 0.0 | +297d9911-9b62-421e-bb32-76d72c202f1a / -— |
| Jogador 8 | 5-6 | 303 | REROLL | FAST8 | 66.0 | 7 | 88 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 305 | SELL | FAST8 | 66.0 | 7 | 99 | 5 | 42.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05376923084259033 | 0.0 | 0.0 | +— / -19cbc95b-d098-4ce7-9cf5-41e4ac50d81b |
| Jogador 8 | 5-7 | 306 | BUY | FAST8 | 66.0 | 7 | 102 | 5 | 42.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7645125985145569 | 0.0 | 0.0 | +ea58e457-6e29-42e7-b60f-f8c157981c75 / -297d9911-9b62-421e-bb32-76d72c202f1a,61362365-2cf7-40e4-95f9-98e28728fd39 |
| Jogador 8 | 5-7 | 307 | BUY | FAST8 | 66.0 | 7 | 100 | 5 | 38.0 | Defendente/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27559152245521545 | 0.0 | 0.0 | +f8177556-bc54-4860-a7cf-90a94b0e6c96 / -— |
| Jogador 8 | 5-7 | 308 | REROLL | FAST8 | 66.0 | 7 | 98 | 5 | 38.0 | Defendente/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 309 | SELL | FAST8 | 66.0 | 7 | 96 | 5 | 38.0 | Defendente/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08064842224121094 | 0.0 | 0.0 | +— / -ea58e457-6e29-42e7-b60f-f8c157981c75 |
| Jogador 8 | 5-7 | 310 | BUY | FAST8 | 66.0 | 7 | 101 | 5 | 38.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3040573298931122 | 0.0 | 0.0 | +77742642-57e8-4594-8bb9-5b2e80a86ba1 / -— |
| Jogador 8 | 6-1 | 312 | EQUIP_FROM_INVENTORY | FAST8 | 66.0 | 7 | 109 | 5 | 44.0 | Defendente/DA_18_Lux_Inferno | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.025822460651397705 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 313 | BUY | FAST8 | 66.0 | 7 | 109 | 5 | 44.0 | Defendente/DA_18_Lux_Inferno | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4246440827846527 | 0.0 | 0.0 | +c2de293a-fa44-4161-8593-47b3feca588d / -— |
| Jogador 8 | 6-1 | 314 | REROLL | FAST8 | 66.0 | 7 | 107 | 5 | 44.0 | Defendente/DA_18_Lux_Inferno | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 315 | SELL | FAST8 | 66.0 | 7 | 105 | 5 | 44.0 | Defendente/DA_18_Lux_Inferno | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12690694630146027 | 0.0 | 0.0 | +— / -c2de293a-fa44-4161-8593-47b3feca588d |
| Jogador 8 | 6-1 | 316 | BUY | FAST8 | 66.0 | 7 | 107 | 5 | 44.0 | Defendente/DA_18_Lux_Inferno | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.009636402130127 | 0.0 | 0.0 | +d63a72f0-dcab-454e-afad-17ddc66b5b3d / -2e656a3d-eed0-40bb-a831-443d972d6588,88249896-79bb-4f76-94a3-131d12f9fc3d |
| Jogador 8 | 6-1 | 317 | BUY | FAST8 | 66.0 | 7 | 104 | 5 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014460221864283085 | 0.0 | 0.0 | +ac2e2c72-371d-478d-a3f2-32d51e71f567 / -— |
| Jogador 8 | 6-1 | 318 | REROLL | FAST8 | 66.0 | 7 | 100 | 5 | 38.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 319 | SELL | FAST8 | 66.0 | 7 | 98 | 5 | 38.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060449667274951935 | 0.0 | 0.0 | +— / -f8177556-bc54-4860-a7cf-90a94b0e6c96 |
| Jogador 8 | 6-1 | 320 | MOVE_BENCH | FAST8 | 66.0 | 7 | 100 | 5 | 38.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5991170406341553 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 322 | BUY | WINSTREAK | 66.0 | 8 | 114 | 5 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9866001605987549 | 0.0 | 0.0 | +64f5c6ab-e024-4d80-b770-dee94530827e / -— |
| Jogador 8 | 6-2 | 323 | BUY | WINSTREAK | 66.0 | 8 | 111 | 5 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26740849018096924 | 0.0 | 0.0 | +5d9c01d4-6ea7-4b98-8ab3-8e549d7e5906 / -— |
| Jogador 8 | 6-2 | 324 | MOVE_BOARD | WINSTREAK | 66.0 | 8 | 107 | 5 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.057439019154117e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 325 | MOVE_BENCH | WINSTREAK | 66.0 | 8 | 107 | 5 | 50.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39704516530036926 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 326 | BUY | WINSTREAK | 66.0 | 8 | 107 | 5 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3820670545101166 | 0.0 | 0.0 | +e00cb4c6-0784-4be7-b937-2b2b4775be1c / -— |
| Jogador 8 | 6-2 | 327 | REROLL | WINSTREAK | 66.0 | 8 | 106 | 5 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 328 | SELL | WINSTREAK | 66.0 | 8 | 104 | 5 | 54.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0838492289185524 | 0.0 | 0.0 | +— / -e00cb4c6-0784-4be7-b937-2b2b4775be1c |
| Jogador 8 | 6-2 | 329 | BUY | WINSTREAK | 66.0 | 8 | 105 | 5 | 54.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.059798002243042 | 0.0 | 0.0 | +086093f9-0a81-4d85-9916-c256df0c1c33 / -63c47a3f-6712-4cfa-9376-6140da170089,ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 |
| Jogador 8 | 6-2 | 330 | MOVE_BENCH | WINSTREAK | 66.0 | 8 | 103 | 5 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5986059308052063 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 332 | BUY | WINSTREAK | 66.0 | 8 | 116 | 5 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9051214456558228 | 0.0 | 0.0 | +530cb5ca-dea2-47db-ba63-38133c49eb12 / -4ac49c80-f0c3-47ae-a031-96928d244e13,6b7f5603-ce44-4b91-8a3e-939c4fbb26ac |
| Jogador 8 | 6-3 | 333 | BUY | WINSTREAK | 66.0 | 8 | 112 | 5 | 48.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11789866536855698 | 0.0 | 0.0 | +52c442e6-4e35-4e6f-8887-eff560f7b259 / -— |
| Jogador 8 | 6-3 | 334 | BUY | WINSTREAK | 66.0 | 8 | 108 | 5 | 48.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6106951832771301 | 0.0 | 0.0 | +ee733f3d-35a8-4ea0-86ca-92d3bdae3cc9 / -— |
| Jogador 8 | 6-3 | 335 | MOVE_BENCH | WINSTREAK | 66.0 | 8 | 105 | 5 | 48.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09692221134901047 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 336 | REROLL | WINSTREAK | 66.0 | 8 | 105 | 5 | 52.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 337 | SELL | WINSTREAK | 66.0 | 8 | 103 | 5 | 52.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14258921146392822 | 0.0 | 0.0 | +— / -ee733f3d-35a8-4ea0-86ca-92d3bdae3cc9 |
| Jogador 8 | 6-3 | 338 | BUY | WINSTREAK | 66.0 | 8 | 106 | 5 | 52.0 | Defendente/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2457825243473053 | 0.0 | 0.0 | +d4fd64a7-2945-4d09-ab2e-5bd475ff0f04 / -— |
| Jogador 8 | 6-3 | 339 | SELL | WINSTREAK | 66.0 | 8 | 103 | 5 | 52.0 | Defendente/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05037230625748634 | 0.0 | 0.0 | +— / -530cb5ca-dea2-47db-ba63-38133c49eb12 |
| Jogador 8 | 6-3 | 340 | MOVE_BENCH | WINSTREAK | 66.0 | 8 | 114 | 5 | 52.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4086824059486389 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 342 | EQUIP_FROM_INVENTORY | WINSTREAK | 66.0 | 8 | 128 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13914600014686584 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 343 | EQUIP_FROM_INVENTORY | WINSTREAK | 66.0 | 8 | 128 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.005366666708141565 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 344 | BUY | WINSTREAK | 66.0 | 8 | 128 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0188597440719604 | 0.0 | 0.0 | +aa6b7c66-6aa1-4cd5-9005-449e37829ad8 / -497fbcb9-9d15-43f0-ad71-96eeceeee99d,77c36245-d5ea-4f94-bc0c-680d4a77794a |
| Jogador 8 | 6-4 | 345 | BUY | WINSTREAK | 66.0 | 8 | 126 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32026737928390503 | 0.0 | 0.0 | +cdd76540-e76c-41e9-ac02-253f5ba2e75e / -— |
| Jogador 8 | 6-4 | 346 | BUY | WINSTREAK | 66.0 | 8 | 122 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05735388770699501 | 0.0 | 0.0 | +9c674771-d854-4df1-83ab-910478119bfa / -— |
| Jogador 8 | 6-4 | 347 | BUY | WINSTREAK | 66.0 | 8 | 117 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2746484875679016 | 0.0 | 0.0 | +4869a6d9-9cd7-4ee7-93ae-ae4b2a0c8233 / -— |
| Jogador 8 | 6-4 | 348 | REROLL | WINSTREAK | 66.0 | 8 | 114 | 5 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 349 | SELL | WINSTREAK | 66.0 | 8 | 112 | 5 | 60.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08274631202220917 | 0.0 | 0.0 | +— / -aa6b7c66-6aa1-4cd5-9005-449e37829ad8 |
| Jogador 8 | 6-4 | 350 | BUY | WINSTREAK | 66.0 | 8 | 117 | 5 | 60.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.059782862663269 | 0.0 | 0.0 | +722c4076-6e3d-4b6c-aa0d-398e801d7224 / -29c2eb81-6c39-41ff-96eb-a3b28d6e4b99,64f5c6ab-e024-4d80-b770-dee94530827e |
| Jogador 8 | 6-5 | 352 | SELL | WINSTREAK | 66.0 | 8 | 127 | 5 | 48.0 | Defendente/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2150000035762787 | 0.0 | 0.0 | +— / -722c4076-6e3d-4b6c-aa0d-398e801d7224 |
| Jogador 8 | 6-5 | 353 | BUY | WINSTREAK | 66.0 | 8 | 135 | 5 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1794060915708542 | 0.0 | 0.0 | +b3d39de6-2ee8-41d3-bd7d-fe6efb7067b1 / -— |
| Jogador 8 | 6-5 | 354 | SELL | WINSTREAK | 66.0 | 8 | 132 | 5 | 48.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -4869a6d9-9cd7-4ee7-93ae-ae4b2a0c8233 |
| Jogador 8 | 6-5 | 355 | BUY | WINSTREAK | 66.0 | 8 | 135 | 5 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4032859802246094 | 0.0 | 0.0 | +922ab25c-c204-42a4-8e12-c58153e71efe / -— |
| Jogador 8 | 6-5 | 356 | SELL | WINSTREAK | 66.0 | 8 | 134 | 5 | 48.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06300000101327896 | 0.0 | 0.0 | +— / -b3d39de6-2ee8-41d3-bd7d-fe6efb7067b1 |
| Jogador 8 | 6-5 | 357 | BUY | WINSTREAK | 66.0 | 8 | 137 | 5 | 48.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17959457635879517 | 0.0 | 0.0 | +d14fbb79-be91-410c-8ac7-065e9d02620c / -— |
| Jogador 8 | 6-5 | 358 | MOVE_BENCH | WINSTREAK | 66.0 | 8 | 134 | 5 | 48.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7518066763877869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 359 | MOVE_BENCH | WINSTREAK | 66.0 | 8 | 134 | 5 | 42.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3335449695587158 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 360 | MOVE_BENCH | WINSTREAK | 66.0 | 8 | 134 | 5 | 50.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3853603005409241 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 362 | BUY | WINSTREAK | 66.0 | 8 | 148 | 5 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4965416491031647 | 0.0 | 0.0 | +8b7968ee-f664-4b2a-b9e8-9b0ad6e81d79 / -— |
| Jogador 8 | 6-6 | 363 | BUY | WINSTREAK | 66.0 | 8 | 145 | 5 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20557501912117004 | 0.0 | 0.0 | +233643ca-941f-4ffe-8d9a-f1ff0f64d1d2 / -— |
| Jogador 8 | 6-6 | 364 | REROLL | WINSTREAK | 66.0 | 8 | 142 | 5 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 365 | SELL | WINSTREAK | 66.0 | 8 | 140 | 5 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12740905582904816 | 0.0 | 0.0 | +— / -8b7968ee-f664-4b2a-b9e8-9b0ad6e81d79 |
| Jogador 8 | 6-6 | 366 | BUY | WINSTREAK | 66.0 | 8 | 143 | 5 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9350089430809021 | 0.0 | 0.0 | +ee9f4ee2-0f17-4f55-b410-5f9c6a2984ef / -— |
| Jogador 8 | 6-6 | 367 | SELL | WINSTREAK | 66.0 | 8 | 139 | 5 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.062261536717414856 | 0.0 | 0.0 | +— / -d4fd64a7-2945-4d09-ab2e-5bd475ff0f04 |
| Jogador 8 | 6-6 | 368 | BUY | WINSTREAK | 66.0 | 8 | 142 | 5 | 56.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8808125257492065 | 0.0 | 0.0 | +52fab411-0911-4c1f-a60b-268de98a0243 / -— |
| Jogador 8 | 6-6 | 369 | REROLL | WINSTREAK | 66.0 | 8 | 138 | 5 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 370 | SELL | WINSTREAK | 66.0 | 8 | 136 | 5 | 56.0 | Defendente/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06780000030994415 | 0.0 | 0.0 | +— / -233643ca-941f-4ffe-8d9a-f1ff0f64d1d2 |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 170 | 194 | 75 | 15 | 15 | 2 | 0 | 0 | 0 | 36.0 |
- Jogador 1 — gasto por ação: BUY: 122g, BUY_XP: 72g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 15g, stage 2: 63g, stage 3: 97g, stage 4: 19g
| Jogador 2 | 192 | 168 | 83 | 4 | 0 | 0 | 14 | 0 | 133 | 26.0 |
- Jogador 2 — gasto por ação: BUY: 140g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 28g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 13g, stage 2: 34g, stage 3: 23g, stage 4: 85g, stage 5: 13g
| Jogador 3 | 163 | 172 | 86 | 16 | 4 | 0 | 8 | 0 | 45 | 32.0 |
- Jogador 3 — gasto por ação: BUY: 132g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 16g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 15g, stage 2: 46g, stage 3: 86g, stage 4: 25g
| Jogador 4 | 313 | 367 | 184 | 21 | 11 | 0 | 27 | 0 | 106 | 56.0 |
- Jogador 4 — gasto por ação: BUY: 261g, BUY_XP: 52g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 54g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 16g, stage 2: 66g, stage 3: 67g, stage 4: 67g, stage 5: 69g, stage 6: 82g
| Jogador 5 | 253 | 299 | 128 | 30 | 20 | 1 | 4 | 0 | 41 | 56.0 |
- Jogador 5 — gasto por ação: BUY: 195g, BUY_XP: 96g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 8g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 16g, stage 2: 47g, stage 3: 93g, stage 4: 68g, stage 5: 58g, stage 6: 17g
| Jogador 6 | 223 | 245 | 96 | 23 | 19 | 4 | 0 | 0 | 0 | 50.0 |
- Jogador 6 — gasto por ação: BUY: 153g, BUY_XP: 92g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 18g, stage 2: 70g, stage 3: 78g, stage 4: 61g, stage 5: 18g
| Jogador 7 | 238 | 285 | 159 | 16 | 9 | 0 | 13 | 0 | 90 | 46.0 |
- Jogador 7 — gasto por ação: BUY: 211g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 26g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 15g, stage 2: 53g, stage 3: 93g, stage 4: 89g, stage 5: 35g
| Jogador 8 | 312 | 408 | 217 | 21 | 14 | 0 | 25 | 0 | 139 | 56.0 |
- Jogador 8 — gasto por ação: BUY: 294g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 50g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 12g, stage 2: 65g, stage 3: 79g, stage 4: 83g, stage 5: 84g, stage 6: 85g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 18 | 2 |
- Jogador 1 · 2-1 · step 47: PASS com 9g, HP 100, nível 4/8 (STABILIZE).
- Jogador 1 · 2-5 · step 87: PASS com 20g, HP 84, nível 5/8 (STABILIZE).
| Jogador 2 | 0 | 23 |
- Jogador 2 · 2-2 · step 56: PASS com 9g, HP 100, nível 4/8 (STABILIZE).
- Jogador 2 · 2-3 · step 65: PASS com 16g, HP 100, nível 4/8 (STABILIZE).
- Jogador 2 · 2-4 · step 75: PASS com 25g, HP 100, nível 4/8 (STABILIZE).
- Jogador 2 · 2-6 · step 98: PASS com 38g, HP 94, nível 5/8 (STABILIZE).
- Jogador 2 · 3-1 · step 114: PASS com 55g, HP 94, nível 5/8 (STABILIZE).
- Jogador 2 · 3-2 · step 123: PASS com 65g, HP 83, nível 5/8 (STABILIZE).
- Jogador 2 · 3-3 · step 138: PASS com 74g, HP 73, nível 5/8 (STABILIZE).
- Jogador 2 · 3-5 · step 158: PASS com 95g, HP 63, nível 5/8 (STABILIZE).
- Jogador 2 · 4-2 · step 193: REROLL com 122g, HP 40, nível 6/8 (FAST8).
- Jogador 2 · 4-2 · step 198: REROLL com 118g, HP 40, nível 6/8 (FAST8).
- Jogador 2 · 4-3 · step 202: REROLL com 125g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-3 · step 209: REROLL com 121g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-4 · step 215: REROLL com 131g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-5 · step 223: REROLL com 135g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-5 · step 226: REROLL com 134g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-5 · step 229: REROLL com 131g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-6 · step 235: REROLL com 133g, HP 15, nível 6/8 (ALL_IN).
- Jogador 2 · 4-6 · step 236: REROLL com 131g, HP 15, nível 6/8 (ALL_IN).
- Jogador 2 · 4-6 · step 237: REROLL com 129g, HP 15, nível 6/8 (ALL_IN).
- Jogador 2 · 4-6 · step 238: REROLL com 127g, HP 15, nível 6/8 (ALL_IN).
- Jogador 2 · 4-6 · step 239: REROLL com 125g, HP 15, nível 6/8 (ALL_IN).
- Jogador 2 · 4-7 · step 246: PASS com 133g, HP 15, nível 6/8 (ALL_IN).
- Jogador 2 · 5-1 · step 254: REROLL com 140g, HP 15, nível 6/8 (ALL_IN).
| Jogador 3 | 6 | 11 |
- Jogador 3 · 2-1 · step 44: PASS com 6g, HP 100, nível 4/8 (STABILIZE).
- Jogador 3 · 3-3 · step 135: PASS com 27g, HP 54, nível 6/8 (FAST8).
- Jogador 3 · 3-4 · step 146: PASS com 28g, HP 43, nível 6/8 (FAST8).
- Jogador 3 · 3-5 · step 154: REROLL com 27g, HP 43, nível 6/8 (FAST8).
- Jogador 3 · 3-6 · step 164: REROLL com 32g, HP 32, nível 6/8 (STABILIZE).
- Jogador 3 · 3-6 · step 169: REROLL com 28g, HP 32, nível 6/8 (STABILIZE).
- Jogador 3 · 3-7 · step 175: REROLL com 37g, HP 20, nível 6/8 (STABILIZE).
- Jogador 3 · 3-7 · step 178: REROLL com 36g, HP 20, nível 6/8 (STABILIZE).
- Jogador 3 · 4-1 · step 184: REROLL com 43g, HP 20, nível 6/8 (STABILIZE).
- Jogador 3 · 4-1 · step 187: REROLL com 41g, HP 20, nível 6/8 (STABILIZE).
- Jogador 3 · 4-2 · step 195: REROLL com 48g, HP 10, nível 6/8 (ALL_IN).
| Jogador 4 | 13 | 29 |
- Jogador 4 · 3-2 · step 125: PASS com 8g, HP 95, nível 6/8 (FAST8).
- Jogador 4 · 4-3 · step 207: PASS com 10g, HP 72, nível 7/8 (FAST8).
- Jogador 4 · 4-4 · step 216: REROLL com 17g, HP 72, nível 7/8 (FAST8).
- Jogador 4 · 4-5 · step 227: REROLL com 28g, HP 72, nível 7/8 (FAST8).
- Jogador 4 · 4-6 · step 235: REROLL com 35g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 4-7 · step 246: REROLL com 39g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 4-7 · step 249: REROLL com 42g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 5-1 · step 255: REROLL com 49g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 5-2 · step 263: REROLL com 59g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 5-2 · step 266: REROLL com 59g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 5-3 · step 273: REROLL com 63g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 5-3 · step 278: REROLL com 62g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 5-4 · step 284: REROLL com 66g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 5-5 · step 295: REROLL com 67g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 5-7 · step 309: REROLL com 89g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 6-1 · step 315: REROLL com 93g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 6-1 · step 318: REROLL com 90g, HP 60, nível 7/8 (FAST8).
- Jogador 4 · 6-2 · step 327: REROLL com 95g, HP 41, nível 7/8 (FAST8).
- Jogador 4 · 6-3 · step 333: REROLL com 105g, HP 41, nível 7/8 (FAST8).
- Jogador 4 · 6-4 · step 345: REROLL com 104g, HP 22, nível 7/8 (STABILIZE).
- Jogador 4 · 6-4 · step 349: REROLL com 100g, HP 22, nível 7/8 (STABILIZE).
- Jogador 4 · 6-4 · step 350: REROLL com 98g, HP 22, nível 7/8 (STABILIZE).
- Jogador 4 · 6-5 · step 352: REROLL com 106g, HP 22, nível 7/8 (STABILIZE).
- Jogador 4 · 6-5 · step 353: REROLL com 104g, HP 22, nível 7/8 (STABILIZE).
- Jogador 4 · 6-5 · step 356: REROLL com 106g, HP 22, nível 7/8 (STABILIZE).
- Jogador 4 · 6-6 · step 362: REROLL com 118g, HP 3, nível 7/8 (ALL_IN).
- Jogador 4 · 6-6 · step 366: REROLL com 115g, HP 3, nível 7/8 (ALL_IN).
- Jogador 4 · 6-6 · step 369: REROLL com 110g, HP 3, nível 7/8 (ALL_IN).
- Jogador 4 · 6-6 · step 370: REROLL com 108g, HP 3, nível 7/8 (ALL_IN).
| Jogador 5 | 24 | 3 |
- Jogador 5 · 2-2 · step 57: PASS com 7g, HP 95, nível 4/8 (STABILIZE).
- Jogador 5 · 3-6 · step 165: PASS com 9g, HP 84, nível 7/8 (FAST8).
- Jogador 5 · 4-1 · step 187: PASS com 15g, HP 84, nível 7/8 (FAST8).
| Jogador 6 | 23 | 4 |
- Jogador 6 · 2-2 · step 59: PASS com 8g, HP 100, nível 4/8 (STABILIZE).
- Jogador 6 · 3-1 · step 119: PASS com 7g, HP 90, nível 6/8 (FAST8).
- Jogador 6 · 4-1 · step 187: PASS com 6g, HP 57, nível 7/8 (FAST8).
- Jogador 6 · 4-2 · step 197: PASS com 9g, HP 57, nível 7/8 (FAST8).
| Jogador 7 | 12 | 17 |
- Jogador 7 · 2-1 · step 48: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 7 · 2-4 · step 76: PASS com 23g, HP 100, nível 4/8 (STABILIZE).
- Jogador 7 · 3-5 · step 156: PASS com 30g, HP 77, nível 7/8 (FAST8).
- Jogador 7 · 3-6 · step 166: PASS com 27g, HP 77, nível 7/8 (FAST8).
- Jogador 7 · 3-7 · step 175: REROLL com 25g, HP 77, nível 7/8 (FAST8).
- Jogador 7 · 4-1 · step 188: REROLL com 31g, HP 77, nível 7/8 (FAST8).
- Jogador 7 · 4-2 · step 197: REROLL com 33g, HP 77, nível 7/8 (FAST8).
- Jogador 7 · 4-3 · step 207: REROLL com 37g, HP 64, nível 7/8 (FAST8).
- Jogador 7 · 4-4 · step 217: REROLL com 43g, HP 53, nível 7/8 (FAST8).
- Jogador 7 · 4-5 · step 225: REROLL com 53g, HP 53, nível 7/8 (FAST8).
- Jogador 7 · 4-6 · step 237: REROLL com 60g, HP 41, nível 7/8 (FAST8).
- Jogador 7 · 4-7 · step 247: REROLL com 68g, HP 29, nível 7/8 (STABILIZE).
- Jogador 7 · 5-1 · step 258: REROLL com 73g, HP 29, nível 7/8 (STABILIZE).
- Jogador 7 · 5-2 · step 264: REROLL com 80g, HP 29, nível 7/8 (STABILIZE).
- Jogador 7 · 5-2 · step 269: REROLL com 84g, HP 29, nível 7/8 (STABILIZE).
- Jogador 7 · 5-3 · step 273: REROLL com 91g, HP 13, nível 7/8 (ALL_IN).
- Jogador 7 · 5-3 · step 278: REROLL com 89g, HP 13, nível 7/8 (ALL_IN).
| Jogador 8 | 16 | 21 |
- Jogador 8 · 3-1 · step 116: PASS com 19g, HP 77, nível 6/8 (FAST8).
- Jogador 8 · 4-3 · step 203: REROLL com 9g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-3 · step 207: REROLL com 5g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-4 · step 215: REROLL com 14g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-4 · step 218: REROLL com 12g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-5 · step 222: REROLL com 19g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-5 · step 227: REROLL com 12g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-6 · step 235: REROLL com 25g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-6 · step 238: REROLL com 23g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-7 · step 244: REROLL com 27g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 4-7 · step 247: REROLL com 29g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 5-1 · step 257: REROLL com 31g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 5-2 · step 267: REROLL com 43g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 5-3 · step 273: REROLL com 59g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 5-4 · step 284: REROLL com 62g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 5-5 · step 294: REROLL com 76g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 5-5 · step 297: REROLL com 73g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 5-6 · step 303: REROLL com 88g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 5-7 · step 308: REROLL com 98g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 6-1 · step 314: REROLL com 107g, HP 66, nível 7/8 (FAST8).
- Jogador 8 · 6-1 · step 318: REROLL com 100g, HP 66, nível 7/8 (FAST8).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 2 | 2 | 0 | 0.0% |
| Jogador 3 | 2 | 1 | 1 | 50.0% |
| Jogador 4 | 2 | 2 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 2 | 2 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 4 | 4 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 170 | 48 | 45 | 77 | 0.0033 | 0.2797 | 0.0011 | 0.3957 | 0.0022 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0252 (59 ações), BUY_XP: Δ 0.0034 (18 ações), CRAFT_AND_EQUIP: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0318 (14 ações), MOVE_BOARD: Δ 0.0200 (23 ações), PASS: Δ 0.0000 (9 ações), SELL: Δ 0.0257 (42 ações)
| Jogador 2 | 192 | 55 | 51 | 86 | -0.0029 | 0.1744 | -0.0043 | 0.5120 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0302 (65 ações), CRAFT_AND_EQUIP: Δ 0.0011 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0007 (44 ações), MOVE_BOARD: Δ 0.0901 (9 ações), PASS: Δ -0.0001 (14 ações), REROLL: Δ 0.0000 (14 ações), SELL: Δ 0.0154 (37 ações)
| Jogador 3 | 163 | 49 | 45 | 69 | 0.0035 | 0.2260 | 0.0002 | 0.4746 | 0.0033 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0250 (64 ações), BUY_XP: Δ 0.0083 (6 ações), CRAFT_AND_EQUIP: Δ 0.0093 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0421 (18 ações), MOVE_BOARD: Δ 0.0274 (12 ações), PASS: Δ 0.0000 (5 ações), REROLL: Δ 0.0000 (8 ações), SELL: Δ 0.0229 (43 ações)
| Jogador 4 | 313 | 74 | 67 | 172 | 0.0009 | 0.3586 | -0.0006 | 0.4316 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0349 (111 ações), BUY_XP: Δ 0.0025 (13 ações), CRAFT_AND_EQUIP: Δ 0.0009 (7 ações), EQUIP_FROM_INVENTORY: Δ -0.0001 (12 ações), MOVE_BENCH: Δ -0.0029 (35 ações), MOVE_BOARD: Δ 0.0878 (31 ações), PASS: Δ 0.0000 (9 ações), REROLL: Δ 0.0000 (27 ações), SELL: Δ 0.0219 (68 ações)
| Jogador 5 | 253 | 63 | 56 | 134 | 0.0022 | 0.3590 | 0.0010 | 0.3545 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0277 (77 ações), BUY_XP: Δ 0.0033 (24 ações), CRAFT_AND_EQUIP: Δ -0.0631 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0535 (35 ações), MOVE_BOARD: Δ -0.0078 (35 ações), PASS: Δ 0.0000 (16 ações), REROLL: Δ 0.0000 (4 ações), SELL: Δ 0.0276 (53 ações)
| Jogador 6 | 223 | 50 | 41 | 132 | 0.0062 | 0.3660 | 0.0039 | 0.4132 | 0.0024 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0177 (65 ações), BUY_XP: Δ 0.0033 (23 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (4 ações), MOVE_BENCH: Δ 0.0452 (25 ações), MOVE_BOARD: Δ 0.0102 (35 ações), PASS: Δ 0.0000 (17 ações), SELL: Δ 0.0209 (47 ações)
| Jogador 7 | 238 | 44 | 37 | 157 | 0.0047 | 0.4218 | 0.0032 | 0.4531 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0178 (91 ações), BUY_XP: Δ 0.0077 (12 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0510 (20 ações), MOVE_BOARD: Δ 0.0574 (14 ações), PASS: Δ 0.0000 (6 ações), REROLL: Δ 0.0000 (13 ações), SELL: Δ 0.0113 (73 ações)
| Jogador 8 | 312 | 74 | 66 | 172 | 0.0017 | 0.3189 | 0.0006 | 0.4035 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0146 (119 ações), BUY_XP: Δ 0.0036 (16 ações), CRAFT_AND_EQUIP: Δ 0.0099 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0006 (7 ações), MOVE_BENCH: Δ 0.0096 (27 ações), MOVE_BOARD: Δ 0.0052 (27 ações), PASS: Δ 0.0000 (8 ações), REROLL: Δ 0.0001 (25 ações), SELL: Δ 0.0231 (76 ações)
- Jogador 1 — rounds avaliados: 21; correlação estrutural/combate: -0.028; posicional/combate: 0.038.
- Jogador 1 — combate positive: score estrutural prévio 0.329
  score posicional prévio 0.410
- Jogador 1 — combate negative: score estrutural prévio 0.290
  score posicional prévio 0.396
- Jogador 2 — rounds avaliados: 26; correlação estrutural/combate: 0.098; posicional/combate: 0.057.
- Jogador 2 — combate positive: score estrutural prévio 0.205
  score posicional prévio 0.531
- Jogador 2 — combate negative: score estrutural prévio 0.115
  score posicional prévio 0.510
- Jogador 3 — rounds avaliados: 20; correlação estrutural/combate: 0.158; posicional/combate: -0.504.
- Jogador 3 — combate positive: score estrutural prévio 0.258
  score posicional prévio 0.458
- Jogador 3 — combate negative: score estrutural prévio 0.209
  score posicional prévio 0.511
- Jogador 4 — rounds avaliados: 38; correlação estrutural/combate: -0.026; posicional/combate: 0.004.
- Jogador 4 — combate positive: score estrutural prévio 0.340
  score posicional prévio 0.433
- Jogador 4 — combate negative: score estrutural prévio 0.365
  score posicional prévio 0.436
- Jogador 5 — rounds avaliados: 34; correlação estrutural/combate: 0.156; posicional/combate: 0.374.
- Jogador 5 — combate positive: score estrutural prévio 0.416
  score posicional prévio 0.375
- Jogador 5 — combate negative: score estrutural prévio 0.365
  score posicional prévio 0.312
- Jogador 6 — rounds avaliados: 28; correlação estrutural/combate: -0.260; posicional/combate: -0.045.
- Jogador 6 — combate positive: score estrutural prévio 0.389
  score posicional prévio 0.436
- Jogador 6 — combate negative: score estrutural prévio 0.541
  score posicional prévio 0.438
- Jogador 7 — rounds avaliados: 28; correlação estrutural/combate: -0.312; posicional/combate: 0.172.
- Jogador 7 — combate positive: score estrutural prévio 0.375
  score posicional prévio 0.482
- Jogador 7 — combate negative: score estrutural prévio 0.553
  score posicional prévio 0.445
- Jogador 8 — rounds avaliados: 38; correlação estrutural/combate: 0.115; posicional/combate: -0.423.
- Jogador 8 — combate positive: score estrutural prévio 0.374
  score posicional prévio 0.371
- Jogador 8 — combate negative: score estrutural prévio 0.328
  score posicional prévio 0.580

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 190 | OK (190) | 3 | 2 | 0 | 1 | 5 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_InfinityEdge, TFT_Item_MadredsBloodrazor, TFT_Item_RunaansHurricane, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 217 | OK (217) | 4 | 3 | 0 | 0 | 7 | 2 |
- Jogador 2 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_GargoyleStoneplate, TFT_Item_LastWhisper, TFT_Item_Quicksilver, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 182 | OK (182) | 3 | 2 | 0 | 1 | 5 | 2 |
- Jogador 3 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_MadredsBloodrazor, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_UnstableConcoction; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 350 | OK (350) | 3 | 5 | 0 | 0 | 8 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_InfinityEdge, TFT_Item_PowerGauntlet, TFT_Item_Quicksilver, TFT_Item_Redemption, TFT_Item_RunaansHurricane; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 286 | OK (286) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 5 — IDs equipados observados: TFT_Item_GargoyleStoneplate, TFT_Item_JeweledGauntlet, TFT_Item_LastWhisper, TFT_Item_Leviathan, TFT_Item_MadredsBloodrazor, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 250 | OK (250) | 5 | 2 | 0 | 0 | 7 | 2 |
- Jogador 6 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_GargoyleStoneplate, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 265 | OK (265) | 7 | 0 | 0 | 0 | 7 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Crownguard, TFT_Item_GargoyleStoneplate, TFT_Item_Leviathan, TFT_Item_PowerGauntlet, TFT_Item_RedBuff, TFT_Item_RunaansHurricane; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 8 | 350 | OK (350) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 8 — IDs equipados observados: DA_18_EmblemHunter, TFT_Item_Bloodthirster, TFT_Item_DragonsClaw, TFT_Item_InfinityEdge, TFT_Item_LastWhisper, TFT_Item_Morellonomicon, TFT_Item_RabadonsDeathcap, TFT_Item_Redemption; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 1 | 1-2 | 10 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 5 | 3 → 3 | 0.005 | 0.000 |
| Jogador 1 | 1-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 7% | 2 → 5 | 5 | 3 → 3 | 0.006 | 0.000 |
| Jogador 1 | 1-4 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 0 | 7% → 7% | 5 → 9 | 4 | 3 → 4 | -0.001 | 0.000 |
| Jogador 1 | 2-1 | 8 | 2.000 | -2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 9 → 14 | 2 | 4 → 4 | 0.002 | -0.303 |
| Jogador 1 | 2-2 | 10 | 10.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 14% | 14 → 15 | 7 | 4 → 4 | 0.004 | -0.232 |
| Jogador 1 | 2-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 15 → 22 | 6 | 4 → 4 | 0.004 | -0.248 |
| Jogador 1 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 22 → 24 | 12 | 4 → 5 | -0.003 | 0.000 |
| Jogador 1 | 2-5 | 8 | 6.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 18% | 24 → 28 | 5 | 5 → 5 | 0.015 | -0.297 |
| Jogador 1 | 2-6 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 28 → 33 | 14 | 5 → 5 | -0.006 | -0.238 |
| Jogador 1 | 2-7 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 33 → 30 | 17 | 5 → 6 | 0.002 | 0.000 |
| Jogador 1 | 3-1 | 10 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 30 → 20 | 21 | 6 → 6 | 0.001 | -0.268 |
| Jogador 1 | 3-2 | 10 | 8.000 | -4.000 | 0 → 0 | 0 → 0 | 21% → 25% | 20 → 8 | 22 | 6 → 7 | -0.001 | 0.288 |
| Jogador 1 | 3-3 | 9 | 0.000 | 12.000 | 0 → 0 | 0 → 0 | 25% → 25% | 8 → 9 | 9 | 7 → 7 | 0.003 | 0.311 |
| Jogador 1 | 3-4 | 10 | 0.000 | -12.000 | 0 → 0 | 0 → 0 | 25% → 25% | 9 → 9 | 16 | 7 → 7 | 0.006 | 0.000 |
| Jogador 1 | 3-5 | 10 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 25% → 25% | 9 → 5 | 14 | 7 → 7 | 0.000 | -0.280 |
| Jogador 1 | 3-6 | 9 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 25% → 25% | 5 → 9 | 7 | 7 → 7 | -0.007 | -0.313 |
| Jogador 1 | 3-7 | 6 | 0.000 | 16.000 | 0 → 0 | 1 → 2 | 25% → 25% | 9 → 7 | 8 | 7 → 7 | -0.000 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | -0.012 | -0.271 |
| Jogador 1 | 4-2 | 7 | 0.000 | 14.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | -0.006 | -0.388 |
| Jogador 1 | 4-3 | 8 | -36.000 | -42.000 | 0 → 0 | 2 → 0 | 25% → 0% | 6 → 0 | 6 | 7 → 7 | -0.073 | -0.354 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 34, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 50 ações e piorou em 47.
- Jogador 1 — estado final: ouro 0, nível 7, vida 12.0, colocação 7.
| Jogador 2 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 2 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.024 | 0.000 |
| Jogador 2 | 1-3 | 10 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 5 | 3 → 3 | 0.000 | 0.000 |
| Jogador 2 | 1-4 | 10 | -2.000 | -2.000 | 0 → 0 | 1 → 0 | 11% → 7% | 3 → 9 | 5 | 3 → 4 | -0.017 | 0.000 |
| Jogador 2 | 2-1 | 10 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 14% | 9 → 11 | 7 | 4 → 4 | -0.008 | 0.251 |
| Jogador 2 | 2-2 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 14% → 14% | 11 → 17 | 3 | 4 → 4 | 0.000 | 0.352 |
| Jogador 2 | 2-3 | 6 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 17 → 24 | 3 | 4 → 4 | -0.006 | 0.440 |
| Jogador 2 | 2-4 | 6 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 24 → 33 | 2 | 4 → 4 | 0.005 | 0.000 |
| Jogador 2 | 2-5 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 33 → 40 | 9 | 4 → 5 | 0.007 | -0.248 |
| Jogador 2 | 2-6 | 9 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 18% | 40 → 47 | 5 | 5 → 5 | 0.016 | 0.293 |
| Jogador 2 | 2-7 | 10 | 2.000 | -6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 47 → 58 | 5 | 5 → 5 | 0.000 | 0.000 |
| Jogador 2 | 3-1 | 5 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 58 → 65 | 3 | 5 → 5 | 0.002 | -0.535 |
| Jogador 2 | 3-2 | 4 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 65 → 76 | 0 | 5 → 5 | -0.001 | -0.646 |
| Jogador 2 | 3-3 | 9 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 76 → 85 | 6 | 5 → 5 | -0.074 | -0.298 |
| Jogador 2 | 3-4 | 8 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 85 → 92 | 4 | 5 → 5 | 0.064 | 0.000 |
| Jogador 2 | 3-5 | 9 | -2.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 92 → 106 | 3 | 5 → 5 | 0.061 | -0.318 |
| Jogador 2 | 3-6 | 6 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 18% → 18% | 106 → 115 | 3 | 5 → 5 | 0.001 | -0.463 |
| Jogador 2 | 3-7 | 7 | 0.000 | 8.000 | 0 → 0 | 1 → 3 | 18% → 18% | 115 → 123 | 4 | 5 → 5 | -0.000 | 0.000 |
| Jogador 2 | 4-1 | 10 | 2.000 | 16.000 | 0 → 0 | 3 → 3 | 18% → 18% | 123 → 125 | 9 | 5 → 6 | 0.009 | 0.281 |
| Jogador 2 | 4-2 | 10 | 4.000 | 2.000 | 0 → 0 | 3 → 4 | 18% → 21% | 125 → 128 | 11 | 6 → 6 | -0.004 | -0.276 |
| Jogador 2 | 4-3 | 10 | 4.000 | 4.000 | 0 → 0 | 4 → 2 | 21% → 21% | 128 → 130 | 11 | 6 → 6 | 0.001 | 0.290 |
| Jogador 2 | 4-4 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 21% → 21% | 130 → 133 | 14 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | -2.000 | 0 → 0 | 2 → 4 | 21% → 21% | 133 → 139 | 15 | 6 → 6 | 0.006 | -0.275 |
| Jogador 2 | 4-6 | 10 | 0.000 | 8.000 | 0 → 0 | 4 → 4 | 21% → 21% | 139 → 134 | 19 | 6 → 6 | -0.006 | 0.288 |
| Jogador 2 | 4-7 | 8 | -2.000 | 0.000 | 0 → 0 | 4 → 3 | 21% → 21% | 134 → 143 | 6 | 6 → 6 | -0.142 | 0.000 |
| Jogador 2 | 5-1 | 10 | -32.000 | -56.000 | 0 → 0 | 3 → 0 | 21% → 0% | 143 → 133 | 13 | 6 → 6 | 0.004 | -0.285 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 15; mudanças de composição: 1; posicionamento melhorou em 61 ações e piorou em 51.
- Jogador 2 — estado final: ouro 133, nível 6, vida 15.0, colocação 6.
| Jogador 3 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.081 | 0.000 |
| Jogador 3 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.012 | 0.000 |
| Jogador 3 | 1-3 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 4 | 5 | 3 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-4 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 8 | 6 | 3 → 4 | 0.013 | 0.000 |
| Jogador 3 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 8 → 11 | 2 | 4 → 4 | -0.020 | -0.464 |
| Jogador 3 | 2-2 | 10 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 14% → 14% | 11 → 12 | 7 | 4 → 4 | 0.006 | -0.243 |
| Jogador 3 | 2-3 | 10 | 2.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 14% | 12 → 18 | 5 | 4 → 4 | 0.002 | -0.243 |
| Jogador 3 | 2-4 | 10 | 2.000 | 6.000 | 1 → 1 | 0 → 0 | 14% → 14% | 18 → 21 | 7 | 4 → 4 | 0.010 | 0.000 |
| Jogador 3 | 2-5 | 10 | 2.000 | -4.000 | 1 → 1 | 0 → 0 | 14% → 18% | 21 → 25 | 11 | 4 → 5 | -0.010 | 0.246 |
| Jogador 3 | 2-6 | 10 | 0.000 | -2.000 | 1 → 1 | 0 → 0 | 18% → 18% | 25 → 33 | 6 | 5 → 5 | 0.006 | -0.248 |
| Jogador 3 | 2-7 | 10 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 18% → 18% | 33 → 36 | 8 | 5 → 5 | -0.003 | 0.000 |
| Jogador 3 | 3-1 | 10 | 0.000 | -2.000 | 1 → 1 | 0 → 1 | 18% → 18% | 36 → 37 | 12 | 5 → 5 | 0.008 | -0.278 |
| Jogador 3 | 3-2 | 10 | 4.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 21% | 37 → 31 | 18 | 5 → 6 | -0.002 | -0.271 |
| Jogador 3 | 3-3 | 6 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 21% → 21% | 31 → 35 | 4 | 6 → 6 | 0.005 | -0.438 |
| Jogador 3 | 3-4 | 7 | 0.000 | 14.000 | 1 → 1 | 1 → 2 | 21% → 21% | 35 → 36 | 7 | 6 → 6 | 0.004 | 0.000 |
| Jogador 3 | 3-5 | 10 | 0.000 | 20.000 | 1 → 1 | 2 → 2 | 21% → 21% | 36 → 31 | 18 | 6 → 6 | -0.014 | -0.268 |
| Jogador 3 | 3-6 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 31 → 36 | 15 | 6 → 6 | -0.006 | -0.271 |
| Jogador 3 | 3-7 | 10 | 0.000 | -6.000 | 1 → 1 | 2 → 4 | 21% → 21% | 36 → 46 | 12 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 46 → 53 | 11 | 6 → 6 | -0.001 | -0.263 |
| Jogador 3 | 4-2 | 10 | -32.000 | -44.000 | 1 → 0 | 4 → 0 | 21% → 0% | 53 → 45 | 14 | 6 → 6 | -0.064 | -0.276 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 12, COMPOSITION_COMPATIBILITY: 34, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 14; mudanças de composição: 1; posicionamento melhorou em 51 ações e piorou em 46.
- Jogador 3 — estado final: ouro 45, nível 6, vida 10.0, colocação 8.
| Jogador 4 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 4 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.012 | 0.000 |
| Jogador 4 | 1-3 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 4 | 6 | 3 → 3 | 0.006 | 0.000 |
| Jogador 4 | 1-4 | 10 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 7 | 6 | 3 → 4 | 0.005 | 0.000 |
| Jogador 4 | 2-1 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 11 | 6 | 4 → 4 | -0.079 | 0.256 |
| Jogador 4 | 2-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 11 → 17 | 5 | 4 → 4 | 0.078 | 0.246 |
| Jogador 4 | 2-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 17 → 19 | 9 | 4 → 5 | 0.003 | -0.232 |
| Jogador 4 | 2-4 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 19 → 23 | 8 | 5 → 5 | -0.004 | 0.000 |
| Jogador 4 | 2-5 | 10 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 23 → 23 | 11 | 5 → 5 | -0.008 | 0.251 |
| Jogador 4 | 2-6 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 23 → 23 | 14 | 5 → 5 | 0.015 | 0.254 |
| Jogador 4 | 2-7 | 10 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 23 → 19 | 13 | 5 → 6 | -0.003 | 0.000 |
| Jogador 4 | 3-1 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 19 → 9 | 20 | 6 → 6 | 0.000 | 0.295 |
| Jogador 4 | 3-2 | 6 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 15 | 3 | 6 → 6 | 0.009 | 0.483 |
| Jogador 4 | 3-3 | 10 | 6.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 25% | 15 → 11 | 12 | 6 → 7 | 0.043 | 0.286 |
| Jogador 4 | 3-4 | 10 | 4.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 11 → 8 | 10 | 7 → 7 | -0.016 | 0.000 |
| Jogador 4 | 3-5 | 10 | -2.000 | 12.000 | 0 → 0 | 2 → 2 | 25% → 25% | 8 → 9 | 8 | 7 → 7 | -0.100 | 0.296 |
| Jogador 4 | 3-6 | 8 | 0.000 | 16.000 | 0 → 0 | 2 → 4 | 25% → 25% | 9 → 6 | 8 | 7 → 7 | 0.016 | -0.334 |
| Jogador 4 | 3-7 | 6 | -2.000 | 8.000 | 0 → 0 | 4 → 3 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | -0.027 | 0.000 |
| Jogador 4 | 4-1 | 10 | 2.000 | 4.000 | 0 → 0 | 3 → 2 | 25% → 25% | 5 → 6 | 5 | 7 → 7 | -0.020 | -0.266 |
| Jogador 4 | 4-2 | 7 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | 0.139 | 0.419 |
| Jogador 4 | 4-3 | 8 | 0.000 | -2.000 | 0 → 0 | 2 → 2 | 25% → 25% | 6 → 18 | 7 | 7 → 7 | 0.024 | 0.364 |
| Jogador 4 | 4-4 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 2 | 25% → 25% | 18 → 23 | 12 | 7 → 7 | 0.026 | 0.000 |
| Jogador 4 | 4-5 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 25% → 25% | 23 → 33 | 13 | 7 → 7 | 0.006 | -0.266 |
| Jogador 4 | 4-6 | 10 | 0.000 | -8.000 | 0 → 0 | 3 → 4 | 25% → 25% | 33 → 44 | 11 | 7 → 7 | 0.000 | 0.293 |
| Jogador 4 | 4-7 | 10 | -4.000 | 2.000 | 0 → 0 | 4 → 3 | 25% → 25% | 44 → 49 | 13 | 7 → 7 | -0.009 | 0.000 |
| Jogador 4 | 5-1 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 25% → 25% | 49 → 59 | 8 | 7 → 7 | 0.001 | 0.297 |
| Jogador 4 | 5-2 | 10 | 4.000 | -14.000 | 0 → 0 | 4 → 3 | 25% → 25% | 59 → 70 | 9 | 7 → 7 | -0.010 | 0.000 |
| Jogador 4 | 5-3 | 10 | 0.000 | 8.000 | 0 → 0 | 3 → 5 | 25% → 25% | 70 → 74 | 13 | 7 → 7 | 0.006 | 0.000 |
| Jogador 4 | 5-4 | 10 | -4.000 | 8.000 | 0 → 0 | 5 → 4 | 25% → 21% | 74 → 77 | 13 | 7 → 7 | -0.016 | 0.000 |
| Jogador 4 | 5-5 | 9 | 10.000 | 4.000 | 0 → 0 | 4 → 3 | 21% → 25% | 77 → 78 | 15 | 7 → 7 | -0.047 | 0.000 |
| Jogador 4 | 5-6 | 5 | 0.000 | -6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 78 → 95 | 3 | 7 → 7 | -0.000 | 0.584 |
| Jogador 4 | 5-7 | 7 | 6.000 | -6.000 | 0 → 1 | 3 → 2 | 25% → 25% | 95 → 100 | 8 | 7 → 7 | 0.087 | 0.000 |
| Jogador 4 | 6-1 | 10 | 0.000 | 18.000 | 1 → 1 | 2 → 3 | 25% → 25% | 100 → 97 | 19 | 7 → 7 | 0.000 | -0.275 |
| Jogador 4 | 6-2 | 10 | 2.000 | -10.000 | 1 → 1 | 3 → 3 | 25% → 25% | 97 → 109 | 11 | 7 → 7 | -0.002 | 0.295 |
| Jogador 4 | 6-3 | 10 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 25% → 25% | 109 → 109 | 11 | 7 → 7 | -0.006 | -0.280 |
| Jogador 4 | 6-4 | 10 | 4.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 109 → 106 | 13 | 7 → 7 | -0.020 | 0.000 |
| Jogador 4 | 6-5 | 10 | 0.000 | -8.000 | 1 → 1 | 3 → 4 | 25% → 25% | 106 → 118 | 12 | 7 → 7 | 0.014 | -0.290 |
| Jogador 4 | 6-6 | 10 | -58.000 | -62.000 | 1 → 0 | 4 → 0 | 25% → 0% | 118 → 106 | 16 | 7 → 7 | -0.107 | -0.290 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 25, COMPOSITION_COMPATIBILITY: 39, IMMEDIATE_UPGRADE: 14, PAIR_POTENTIAL: 33; mudanças de composição: 1; posicionamento melhorou em 79 ações e piorou em 69.
- Jogador 4 — estado final: ouro 106, nível 7, vida 3.0, colocação 2.
| Jogador 5 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.017 | 0.000 |
| Jogador 5 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.084 | 0.000 |
| Jogador 5 | 1-3 | 10 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 7 | 3 → 3 | -0.006 | 0.000 |
| Jogador 5 | 1-4 | 10 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 8 | 6 | 3 → 4 | 0.011 | 0.000 |
| Jogador 5 | 2-1 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 8 → 12 | 7 | 4 → 4 | -0.011 | -0.237 |
| Jogador 5 | 2-2 | 8 | 8.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 12 → 13 | 6 | 4 → 4 | 0.015 | 0.330 |
| Jogador 5 | 2-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 13 → 21 | 3 | 4 → 4 | 0.000 | 0.259 |
| Jogador 5 | 2-4 | 10 | 4.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 18% | 21 → 23 | 10 | 4 → 5 | 0.039 | 0.000 |
| Jogador 5 | 2-5 | 9 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 18% → 18% | 23 → 29 | 3 | 5 → 5 | 0.002 | 0.293 |
| Jogador 5 | 2-6 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 29 → 39 | 0 | 5 → 5 | -0.013 | 0.517 |
| Jogador 5 | 2-7 | 10 | 8.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 39 → 30 | 18 | 5 → 6 | 0.006 | 0.000 |
| Jogador 5 | 3-1 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 30 → 26 | 18 | 6 → 6 | -0.044 | 0.280 |
| Jogador 5 | 3-2 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 26 → 22 | 15 | 6 → 6 | -0.004 | -0.273 |
| Jogador 5 | 3-3 | 10 | 8.000 | -2.000 | 0 → 1 | 1 → 1 | 21% → 21% | 22 → 14 | 17 | 6 → 7 | 0.022 | 0.280 |
| Jogador 5 | 3-4 | 10 | 6.000 | -2.000 | 1 → 1 | 1 → 0 | 21% → 25% | 14 → 5 | 19 | 7 → 7 | -0.007 | 0.000 |
| Jogador 5 | 3-5 | 7 | 2.000 | 4.000 | 1 → 1 | 0 → 0 | 25% → 25% | 5 → 9 | 4 | 7 → 7 | 0.009 | 0.400 |
| Jogador 5 | 3-6 | 6 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 9 → 17 | 3 | 7 → 7 | 0.013 | 0.497 |
| Jogador 5 | 3-7 | 10 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 17 → 15 | 17 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 8 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 15 → 21 | 3 | 7 → 7 | -0.013 | -0.333 |
| Jogador 5 | 4-2 | 10 | 2.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 21 → 10 | 23 | 7 → 7 | 0.001 | 0.293 |
| Jogador 5 | 4-3 | 10 | 6.000 | -2.000 | 1 → 1 | 0 → 0 | 25% → 29% | 10 → 7 | 13 | 7 → 8 | 0.006 | 0.299 |
| Jogador 5 | 4-4 | 6 | 0.000 | 10.000 | 1 → 1 | 0 → 0 | 29% → 29% | 7 → 8 | 5 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 8 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 29% → 29% | 8 → 8 | 7 | 8 → 8 | -0.010 | 0.354 |
| Jogador 5 | 4-6 | 6 | 0.000 | 16.000 | 1 → 1 | 1 → 2 | 29% → 29% | 8 → 5 | 8 | 8 → 8 | 0.000 | -0.452 |
| Jogador 5 | 4-7 | 8 | 0.000 | 6.000 | 1 → 1 | 2 → 1 | 29% → 29% | 5 → 6 | 9 | 8 → 8 | 0.006 | 0.000 |
| Jogador 5 | 5-1 | 8 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 29% → 29% | 6 → 8 | 4 | 8 → 8 | -0.015 | -0.350 |
| Jogador 5 | 5-2 | 9 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 29% → 29% | 8 → 12 | 5 | 8 → 8 | -0.009 | 0.330 |
| Jogador 5 | 5-3 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 1 | 29% → 29% | 12 → 19 | 12 | 8 → 8 | 0.006 | 0.294 |
| Jogador 5 | 5-4 | 8 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 29% → 29% | 19 → 22 | 8 | 8 → 8 | 0.001 | 0.000 |
| Jogador 5 | 5-5 | 9 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 29% → 29% | 22 → 28 | 8 | 8 → 8 | 0.002 | -0.306 |
| Jogador 5 | 5-6 | 5 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 29% → 29% | 28 → 33 | 8 | 8 → 8 | -0.010 | -0.550 |
| Jogador 5 | 5-7 | 7 | 0.000 | 2.000 | 1 → 1 | 3 → 1 | 29% → 29% | 33 → 36 | 13 | 8 → 8 | -0.009 | 0.000 |
| Jogador 5 | 6-1 | 8 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 29% → 29% | 36 → 41 | 4 | 8 → 8 | -0.015 | 0.000 |
| Jogador 5 | 6-2 | 10 | -54.000 | -74.000 | 1 → 0 | 2 → 0 | 29% → 0% | 41 → 41 | 13 | 8 → 8 | -0.048 | -0.275 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 37, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 65 ações e piorou em 57.
- Jogador 5 — estado final: ouro 41, nível 8, vida 12.0, colocação 3.
| Jogador 6 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 6 | 1-2 | 10 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 4% | 2 → 3 | 6 | 3 → 3 | -0.006 | 0.000 |
| Jogador 6 | 1-3 | 10 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 3 → 6 | 6 | 3 → 3 | -0.000 | 0.000 |
| Jogador 6 | 1-4 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 6 → 8 | 5 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 9 | 8.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 8 → 9 | 6 | 4 → 4 | 0.012 | 0.274 |
| Jogador 6 | 2-2 | 10 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 9 → 13 | 5 | 4 → 4 | -0.004 | -0.232 |
| Jogador 6 | 2-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 14% | 13 → 11 | 14 | 4 → 5 | 0.007 | -0.232 |
| Jogador 6 | 2-4 | 10 | 6.000 | -4.000 | 0 → 0 | 1 → 1 | 14% → 18% | 11 → 8 | 13 | 5 → 5 | 0.006 | 0.000 |
| Jogador 6 | 2-5 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 6 | 13 | 5 → 6 | 0.002 | 0.254 |
| Jogador 6 | 2-6 | 10 | 6.000 | 4.000 | 0 → 0 | 1 → 2 | 18% → 21% | 6 → 8 | 8 | 6 → 6 | -0.009 | 0.265 |
| Jogador 6 | 2-7 | 10 | 2.000 | -2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 8 → 10 | 11 | 6 → 6 | 0.002 | 0.000 |
| Jogador 6 | 3-1 | 10 | 2.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 10 → 14 | 7 | 6 → 6 | 0.015 | 0.285 |
| Jogador 6 | 3-2 | 10 | -2.000 | -2.000 | 0 → 0 | 1 → 0 | 21% → 21% | 14 → 18 | 9 | 6 → 6 | -0.001 | -0.263 |
| Jogador 6 | 3-3 | 10 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 21% → 21% | 18 → 20 | 10 | 6 → 6 | -0.008 | -0.263 |
| Jogador 6 | 3-4 | 10 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 20 → 12 | 19 | 6 → 7 | 0.007 | 0.000 |
| Jogador 6 | 3-5 | 10 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 25% | 12 → 7 | 14 | 7 → 7 | -0.004 | -0.263 |
| Jogador 6 | 3-6 | 9 | 0.000 | 0.000 | 0 → 0 | 1 → 2 | 25% → 25% | 7 → 9 | 10 | 7 → 7 | 0.009 | 0.320 |
| Jogador 6 | 3-7 | 8 | 2.000 | 2.000 | 0 → 0 | 2 → 1 | 25% → 25% | 9 → 8 | 9 | 7 → 7 | 0.001 | 0.000 |
| Jogador 6 | 4-1 | 9 | 6.000 | -8.000 | 0 → 1 | 1 → 1 | 25% → 25% | 8 → 13 | 6 | 7 → 7 | -0.012 | 0.320 |
| Jogador 6 | 4-2 | 8 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 25% → 25% | 13 → 17 | 4 | 7 → 7 | 0.017 | 0.370 |
| Jogador 6 | 4-3 | 9 | 0.000 | 10.000 | 1 → 1 | 1 → 2 | 25% → 25% | 17 → 5 | 17 | 7 → 7 | 0.000 | -0.306 |
| Jogador 6 | 4-4 | 10 | 0.000 | -16.000 | 1 → 1 | 2 → 1 | 25% → 25% | 5 → 6 | 14 | 7 → 8 | 0.002 | 0.000 |
| Jogador 6 | 4-5 | 10 | 4.000 | -2.000 | 1 → 1 | 1 → 1 | 25% → 29% | 6 → 7 | 9 | 8 → 8 | 0.045 | 0.283 |
| Jogador 6 | 4-6 | 6 | 0.000 | 14.000 | 1 → 1 | 1 → 2 | 29% → 29% | 7 → 5 | 7 | 8 → 8 | 0.000 | -0.444 |
| Jogador 6 | 4-7 | 5 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 29% → 29% | 5 → 6 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 9 | -2.000 | 6.000 | 1 → 1 | 2 → 1 | 29% → 29% | 6 → 7 | 5 | 8 → 8 | -0.006 | -0.306 |
| Jogador 6 | 5-2 | 6 | 0.000 | 12.000 | 1 → 1 | 1 → 1 | 29% → 29% | 7 → 7 | 6 | 8 → 8 | 0.000 | -0.458 |
| Jogador 6 | 5-3 | 7 | -50.000 | -40.000 | 1 → 0 | 1 → 0 | 29% → 0% | 7 → 0 | 7 | 8 → 8 | -0.184 | -0.393 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 13, COMPOSITION_COMPATIBILITY: 40, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 10; mudanças de composição: 1; posicionamento melhorou em 53 ações e piorou em 42.
- Jogador 6 — estado final: ouro 0, nível 8, vida 1.0, colocação 5.
| Jogador 7 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.082 | 0.000 |
| Jogador 7 | 1-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.006 | 0.000 |
| Jogador 7 | 1-3 | 10 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 6 | 3 → 3 | 0.021 | 0.000 |
| Jogador 7 | 1-4 | 10 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 8 | 5 | 3 → 4 | 0.005 | 0.000 |
| Jogador 7 | 2-1 | 9 | 6.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 8 → 10 | 6 | 4 → 4 | 0.004 | 0.279 |
| Jogador 7 | 2-2 | 10 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 10 → 18 | 4 | 4 → 4 | 0.001 | 0.259 |
| Jogador 7 | 2-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 18 → 26 | 7 | 4 → 4 | 0.000 | 0.246 |
| Jogador 7 | 2-4 | 7 | 2.000 | 4.000 | 0 → 0 | 0 → 0 | 14% → 14% | 26 → 31 | 5 | 4 → 4 | 0.006 | 0.000 |
| Jogador 7 | 2-5 | 10 | 4.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 18% | 31 → 33 | 9 | 4 → 5 | -0.012 | -0.237 |
| Jogador 7 | 2-6 | 10 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 33 → 43 | 8 | 5 → 5 | 0.006 | -0.243 |
| Jogador 7 | 2-7 | 10 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 43 → 42 | 14 | 5 → 5 | 0.001 | 0.000 |
| Jogador 7 | 3-1 | 10 | 4.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 21% | 42 → 46 | 8 | 5 → 6 | -0.018 | 0.285 |
| Jogador 7 | 3-2 | 10 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 46 → 47 | 15 | 6 → 6 | -0.001 | 0.280 |
| Jogador 7 | 3-3 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 2 | 21% → 21% | 47 → 42 | 16 | 6 → 6 | -0.003 | -0.276 |
| Jogador 7 | 3-4 | 10 | 6.000 | 4.000 | 0 → 0 | 2 → 1 | 21% → 25% | 42 → 32 | 18 | 6 → 7 | 0.002 | 0.000 |
| Jogador 7 | 3-5 | 7 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 25% → 25% | 32 → 39 | 5 | 7 → 7 | 0.019 | 0.407 |
| Jogador 7 | 3-6 | 7 | 0.000 | 24.000 | 0 → 0 | 2 → 3 | 25% → 25% | 39 → 36 | 12 | 7 → 7 | -0.003 | 0.421 |
| Jogador 7 | 3-7 | 10 | 0.000 | 26.000 | 0 → 0 | 3 → 4 | 25% → 25% | 36 → 29 | 19 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | -8.000 | 0 → 0 | 4 → 4 | 25% → 25% | 29 → 41 | 6 | 7 → 7 | 0.034 | 0.283 |
| Jogador 7 | 4-2 | 10 | 6.000 | 8.000 | 0 → 1 | 4 → 3 | 25% → 25% | 41 → 36 | 14 | 7 → 7 | -0.003 | -0.280 |
| Jogador 7 | 4-3 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 36 → 43 | 14 | 7 → 7 | 0.000 | -0.273 |
| Jogador 7 | 4-4 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 2 | 25% → 25% | 43 → 52 | 15 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 25% → 25% | 52 → 61 | 12 | 7 → 7 | 0.000 | -0.266 |
| Jogador 7 | 4-6 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 2 | 25% → 25% | 61 → 69 | 13 | 7 → 7 | 0.000 | -0.276 |
| Jogador 7 | 4-7 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 25% → 25% | 69 → 76 | 15 | 7 → 7 | 0.015 | 0.000 |
| Jogador 7 | 5-1 | 10 | 4.000 | -8.000 | 1 → 1 | 2 → 1 | 25% → 25% | 76 → 84 | 9 | 7 → 7 | -0.010 | 0.291 |
| Jogador 7 | 5-2 | 10 | 0.000 | 0.000 | 1 → 1 | 1 → 2 | 25% → 25% | 84 → 92 | 15 | 7 → 7 | 0.006 | -0.280 |
| Jogador 7 | 5-3 | 10 | -46.000 | -56.000 | 1 → 0 | 2 → 0 | 25% → 0% | 92 → 90 | 11 | 7 → 7 | -0.119 | -0.280 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 27, COMPOSITION_COMPATIBILITY: 42, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 20; mudanças de composição: 0; posicionamento melhorou em 46 ações e piorou em 38.
- Jogador 7 — estado final: ouro 90, nível 7, vida 13.0, colocação 4.
| Jogador 8 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.017 | 0.000 |
| Jogador 8 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.057 | 0.000 |
| Jogador 8 | 1-3 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 4 | 5 | 3 → 3 | -0.006 | 0.000 |
| Jogador 8 | 1-4 | 10 | -2.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 7% | 4 → 9 | 4 | 3 → 4 | -0.003 | 0.000 |
| Jogador 8 | 2-1 | 10 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 14% | 9 → 11 | 5 | 4 → 4 | -0.024 | -0.237 |
| Jogador 8 | 2-2 | 10 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 11 → 14 | 6 | 4 → 4 | 0.076 | -0.248 |
| Jogador 8 | 2-3 | 10 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 14 → 22 | 6 | 4 → 4 | 0.008 | 0.246 |
| Jogador 8 | 2-4 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 22 → 27 | 7 | 4 → 4 | 0.006 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 27 → 35 | 6 | 4 → 5 | 0.006 | -0.232 |
| Jogador 8 | 2-6 | 10 | 6.000 | 4.000 | 0 → 0 | 0 → 0 | 14% → 18% | 35 → 21 | 24 | 5 → 5 | -0.005 | -0.249 |
| Jogador 8 | 2-7 | 10 | 6.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 21% | 21 → 23 | 11 | 5 → 6 | -0.097 | 0.000 |
| Jogador 8 | 3-1 | 7 | 4.000 | 4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 23 → 26 | 4 | 6 → 6 | 0.087 | -0.375 |
| Jogador 8 | 3-2 | 10 | 6.000 | -2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 26 → 14 | 21 | 6 → 6 | 0.001 | 0.276 |
| Jogador 8 | 3-3 | 10 | 6.000 | -2.000 | 0 → 0 | 0 → 1 | 21% → 25% | 14 → 7 | 15 | 6 → 7 | -0.003 | 0.293 |
| Jogador 8 | 3-4 | 8 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 6 | 10 | 7 → 7 | -0.008 | 0.000 |
| Jogador 8 | 3-5 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 9 | 13 | 7 → 7 | 0.011 | 0.303 |
| Jogador 8 | 3-6 | 7 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 7 | 9 | 7 → 7 | -0.000 | 0.407 |
| Jogador 8 | 3-7 | 7 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | -0.015 | 0.000 |
| Jogador 8 | 4-1 | 8 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 25% → 25% | 6 → 8 | 6 | 7 → 7 | -0.015 | 0.354 |
| Jogador 8 | 4-2 | 7 | 0.000 | 16.000 | 0 → 0 | 2 → 3 | 25% → 25% | 8 → 9 | 8 | 7 → 7 | -0.015 | 0.412 |
| Jogador 8 | 4-3 | 10 | -2.000 | -12.000 | 0 → 0 | 3 → 2 | 25% → 25% | 9 → 20 | 12 | 7 → 7 | -0.018 | 0.000 |
| Jogador 8 | 4-4 | 10 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 25% → 25% | 20 → 22 | 13 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 10 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 22 → 25 | 18 | 7 → 7 | 0.000 | 0.291 |
| Jogador 8 | 4-6 | 10 | 0.000 | -6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 25 → 35 | 11 | 7 → 7 | 0.012 | 0.283 |
| Jogador 8 | 4-7 | 10 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 35 → 37 | 15 | 7 → 7 | -0.006 | 0.000 |
| Jogador 8 | 5-1 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 37 → 45 | 15 | 7 → 7 | 0.000 | 0.301 |
| Jogador 8 | 5-2 | 10 | -2.000 | -12.000 | 0 → 0 | 4 → 4 | 25% → 25% | 45 → 63 | 9 | 7 → 7 | -0.039 | 0.292 |
| Jogador 8 | 5-3 | 10 | 0.000 | 20.000 | 0 → 0 | 4 → 3 | 25% → 25% | 63 → 63 | 18 | 7 → 7 | -0.006 | 0.297 |
| Jogador 8 | 5-4 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 3 | 25% → 25% | 63 → 73 | 11 | 7 → 7 | 0.062 | 0.000 |
| Jogador 8 | 5-5 | 9 | 0.000 | -8.000 | 0 → 0 | 3 → 4 | 25% → 25% | 73 → 89 | 13 | 7 → 7 | 0.000 | 0.325 |
| Jogador 8 | 5-6 | 5 | 0.000 | 2.000 | 0 → 0 | 4 → 5 | 25% → 25% | 89 → 99 | 7 | 7 → 7 | -0.012 | 0.000 |
| Jogador 8 | 5-7 | 7 | 2.000 | -2.000 | 0 → 0 | 5 → 4 | 25% → 25% | 99 → 109 | 11 | 7 → 7 | 0.101 | 0.000 |
| Jogador 8 | 6-1 | 10 | 6.000 | -2.000 | 0 → 1 | 4 → 3 | 25% → 25% | 109 → 114 | 13 | 7 → 8 | 0.005 | 0.296 |
| Jogador 8 | 6-2 | 10 | 6.000 | 8.000 | 1 → 1 | 3 → 3 | 25% → 29% | 114 → 116 | 12 | 8 → 8 | 0.002 | 0.000 |
| Jogador 8 | 6-3 | 10 | 4.000 | -6.000 | 1 → 2 | 3 → 2 | 29% → 29% | 116 → 128 | 16 | 8 → 8 | -0.003 | 0.301 |
| Jogador 8 | 6-4 | 10 | -12.000 | 28.000 | 2 → 2 | 2 → 1 | 29% → 21% | 128 → 127 | 19 | 8 → 8 | 0.003 | 0.000 |
| Jogador 8 | 6-5 | 10 | 8.000 | -18.000 | 2 → 2 | 1 → 1 | 21% → 29% | 127 → 148 | 7 | 8 → 8 | 0.005 | 0.311 |
| Jogador 8 | 6-6 | 10 | 0.000 | 10.000 | 2 → 2 | 1 → 3 | 29% → 29% | 148 → 140 | 18 | 8 → 8 | 0.000 | 0.311 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 35, COMPOSITION_COMPATIBILITY: 43, IMMEDIATE_UPGRADE: 14, PAIR_POTENTIAL: 27; mudanças de composição: 3; posicionamento melhorou em 79 ações e piorou em 66.
- Jogador 8 — estado final: ouro 140, nível 8, vida 66.0, colocação 1.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 59 | 42 | 11 | 14 | 16 | 9 | 0 | 0 | 0 | 3 | 3 | 0 |
| Jogador 2 | 65 | 37 | 6 | 7 | 7 | 3 | 0 | 1 | 2 | 2 | 2 | 0 |
| Jogador 3 | 64 | 43 | 6 | 7 | 7 | 4 | 0 | 1 | 7 | 2 | 7 | 0 |
| Jogador 4 | 111 | 68 | 4 | 6 | 11 | 7 | 0 | 0 | 8 | 2 | 7 | 0 |
| Jogador 5 | 77 | 53 | 9 | 11 | 13 | 3 | 0 | 0 | 2 | 3 | 7 | 0 |
| Jogador 6 | 65 | 47 | 9 | 10 | 10 | 3 | 0 | 0 | 0 | 4 | 12 | 0 |
| Jogador 7 | 91 | 73 | 11 | 14 | 16 | 5 | 0 | 0 | 22 | 2 | 6 | 0 |
| Jogador 8 | 119 | 76 | 10 | 14 | 14 | 5 | 0 | 0 | 17 | 1 | 8 | 0 |
- Jogador 1 — venda DA_18_Elise (2-6, step 93): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Cassiopeia (2-6, step 95): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_KogMaw18_AD (2-6, step 97): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Rakan (2-7, step 103): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Elise (3-2, step 123): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Vi18 (3-3, step 132): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Azir (3-4, step 142): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Vi18 (3-5, step 152): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Nidalee18_AP (3-6, step 163): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Shen (2-5, step 81): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Tristana (2-5, step 83): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Azir (2-5, step 85): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_KogMaw18_AD (2-6, step 93): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_MasterYi_AD (2-7, step 102): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Cassiopeia (3-3, step 133): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Elise (3-5, step 153): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 2 — venda DA_18_Veigar (3-5, step 154): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 2 — venda DA_Murkwolf18 (4-3, step 203): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Veigar (4-4, step 211): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Murkwolf18 (4-4, step 216): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_Gromp18_AP (4-5, step 221): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Shen (4-7, step 241): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Tristana (2-5, step 85): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 3 — venda DA_18_Yorick (2-6, step 95): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Yorick (2-7, step 104): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 3 — venda DA_18_RekSai (3-2, step 121): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Tristana (3-2, step 123): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 3 — venda DA_18_RekSai (3-5, step 155): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 3 — venda DA_18_Elise (3-6, step 162): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Alistar (3-6, step 167): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Scuttlecrab18 (4-2, step 196): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Diana (2-5, step 87): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_CrimsonRaptor18 (2-6, step 93): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Akali_AD (2-7, step 103): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Alistar (3-1, step 114): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Cassiopeia (4-3, step 203): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Alistar (4-4, step 217): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Scuttlecrab18 (4-5, step 228): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_CrimsonRaptor18 (4-6, step 236): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_CrimsonRaptor18 (4-6, step 238): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_KogMaw18_AD (4-7, step 247): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_LeBlanc (5-1, step 256): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_CrimsonRaptor18 (5-2, step 264): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Alistar (5-4, step 285): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_LeBlanc (5-5, step 296): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_Scuttlecrab18 (5-7, step 310): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Hecarim (6-1, step 316): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Fiddlesticks18 (6-2, step 328): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_Krug18 (6-5, step 354): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Scuttlecrab18 (6-5, step 357): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (3-1, step 112): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-1, step 114): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (3-2, step 126): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-3, step 131): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Yunara (3-4, step 141): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-4, step 143): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Sejuani (4-7, step 243): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_KogMaw18_AD (5-3, step 277): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_KhaZix (5-5, step 296): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Morgana (5-7, step 308): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Rammus (6-2, step 328): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (2-6, step 95): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (2-7, step 103): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 6 — venda DA_Scuttlecrab18 (2-7, step 107): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Rammus (3-2, step 121): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 6 — venda DA_18_Ahri (3-2, step 125): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Tristana (3-4, step 141): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Diana (3-6, step 163): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Diana (3-7, step 171): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Lillia (4-1, step 181): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_Kobuko (4-4, step 211): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Soraka (4-4, step 213): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Kobuko (4-4, step 218): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (2-6, step 93): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Warwick (2-7, step 102): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 7 — venda DA_CrimsonRaptor18 (3-2, step 122): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_RekSai (3-4, step 141): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (3-5, step 151): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Yunara (4-1, step 189): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Yunara (4-2, step 198): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Diana (4-3, step 201): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Aphelios (4-4, step 213): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Yunara (4-6, step 231): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Warwick (4-7, step 241): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rammus (4-7, step 248): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_CrimsonRaptor18 (5-2, step 265): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Diana (5-3, step 274): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_RekSai (5-3, step 276): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (5-3, step 279): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Krug18 (2-5, step 85): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (2-6, step 92): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_18_Akali_AD (2-7, step 104): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (2-7, step 106): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_18_Akali_AD (3-2, step 123): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_Vi18 (3-5, step 153): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Krug18 (4-3, step 201): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Diana (4-3, step 208): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_CrimsonRaptor18 (4-5, step 223): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Diana (4-5, step 228): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Murkwolf18 (4-7, step 245): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Fiddlesticks18 (5-1, step 258): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_KhaZix (5-2, step 268): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_Vi18 (5-3, step 274): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_18_Teemo (5-4, step 281): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_Scuttlecrab18 (6-1, step 315): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_Vi18 (6-3, step 337): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_18_Sett (6-3, step 339): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_Fiddlesticks18 (6-5, step 352): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Vi18 (6-6, step 365): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **94**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| MEDIUM | Jogador 1 | 1-2 | 14 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 1-3 | 21 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 1-3 | 23 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 1 | 1-3 | 25 | PURCHASE_SALE_REVIEW | Compra de DA_18_Xayah foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 1 | 1-4 | 33 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 1 | 1-4 | 35 | PURCHASE_SALE_REVIEW | Compra de DA_18_Akali_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 1 | 2-1 | 41 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Veigar) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 2-3 | 65 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 2-3 | 67 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 2-4 | 72 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 1 | 2-4 | 74 | PURCHASE_SALE_REVIEW | Compra de DA_18_Caitlyn foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 1 | 2-4 | 76 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kayle) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 2-5 | 81 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Veigar) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 2-6 | 93 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 2-6 | 95 | SOLD_CORE_UNIT | Venda de 'DA_18_Cassiopeia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 2-6 | 95 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 1 | 2-6 | 97 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 2-6 | 97 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 2-7 | 101 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Yunara) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 2-7 | 103 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 2-7 | 105 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 3-2 | 123 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 3-3 | 132 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 3-4 | 142 | SOLD_CORE_UNIT | Venda de 'DA_18_Azir' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 3-4 | 144 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 3-4 | 149 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 3-5 | 152 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 3-6 | 163 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-2 | 212 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-3 | 344 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-4 | 476 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-1 | 583 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-3 | 852 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-4 | 985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-5 | 1093 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 1224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1353 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1482 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1611 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1735 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1865 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1998 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 2120 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 2208 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 2346 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 2446 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 2559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 4-3 | 2560 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 2-4 | 1070 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 1-4 | 31 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 2 | 1-4 | 35 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yunara foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 1-4 | 37 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Veigar) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-1 | 46 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 2 | 2-5 | 81 | SOLD_CORE_UNIT | Venda de 'DA_18_Shen' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 2-5 | 83 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 2-5 | 83 | PURCHASE_SALE_REVIEW | Compra de DA_18_Tristana foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 2-5 | 85 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Azir) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 2 | 2-6 | 93 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 2-6 | 93 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 2 | 2-7 | 102 | SOLD_CORE_UNIT | Venda de 'DA_18_MasterYi_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 2-7 | 109 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Warwick) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 2 | 3-3 | 133 | SOLD_CORE_UNIT | Venda de 'DA_18_Cassiopeia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-3 | 133 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 2 | 4-4 | 211 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-5 | 221 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-6 | 1101 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 2-7 | 1239 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-1 | 1312 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-2 | 1373 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-3 | 1497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-3 | 1498 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1820 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 1921 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 2062 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 2198 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2337 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2476 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2610 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2745 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 2854 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 2855 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 2998 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 5-1 | 2999 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-2 | 742 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-3 | 825 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 1078 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-7 | 1289 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-1 | 1350 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-2 | 1474 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-4 | 1709 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-1 | 2100 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-1 | 2161 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 1-3 | 29 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 3 | 1-4 | 35 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 3 | 1-4 | 37 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 3 | 1-4 | 39 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 3 | 2-2 | 59 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yunara foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 3 | 2-5 | 83 | PURCHASE_SALE_REVIEW | Compra de DA_Scuttlecrab18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 3 | 2-5 | 85 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Tristana) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 3 | 2-6 | 91 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 3 | 2-6 | 93 | PURCHASE_SALE_REVIEW | Compra de DA_Scuttlecrab18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 3 | 2-6 | 95 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 2-6 | 97 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yunara foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 3 | 2-6 | 99 | PURCHASE_SALE_REVIEW | Compra de DA_Karma18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 3 | 2-7 | 102 | PURCHASE_SALE_REVIEW | Compra de DA_Scuttlecrab18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 3 | 3-1 | 113 | PURCHASE_SALE_REVIEW | Compra de DA_Vi18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 3 | 3-2 | 121 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 3-2 | 123 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Tristana) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 3 | 3-6 | 162 | SOLD_CORE_UNIT | Venda de 'DA_18_Elise' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 3-6 | 167 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 2-3 | 812 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-4 | 944 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 1075 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 1211 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1349 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1482 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1613 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1698 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1799 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1934 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 2070 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 2207 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 2343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2485 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 4-2 | 2486 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 2-4 | 1028 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-7 | 1448 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-7 | 1459 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-4 | 1849 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 4 | 1-2 | 12 | PURCHASE_SALE_REVIEW | Compra de DA_18_Camille foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 1-3 | 29 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 4 | 1-4 | 38 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 4 | 2-1 | 41 | PURCHASE_SALE_REVIEW | Compra de DA_18_Camille foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 4 | 2-1 | 45 | PURCHASE_SALE_REVIEW | Compra de DA_Gromp18_AP foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 2-2 | 51 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 4 | 2-3 | 65 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 4 | 2-3 | 67 | PURCHASE_SALE_REVIEW | Compra de DA_18_Camille foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 2-4 | 71 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 4 | 2-4 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_Gromp18_AP foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 2-4 | 78 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 4 | 2-5 | 81 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 4 | 2-5 | 87 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 2-5 | 87 | PURCHASE_SALE_REVIEW | Compra de DA_18_Diana foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 2-6 | 91 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Varus) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 4 | 2-6 | 93 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 2-6 | 93 | PURCHASE_SALE_REVIEW | Compra de DA_CrimsonRaptor18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 2-6 | 96 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 4 | 2-7 | 101 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 4 | 3-1 | 111 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 4 | 3-1 | 114 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 4-3 | 203 | SOLD_CORE_UNIT | Venda de 'DA_18_Cassiopeia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 4-4 | 217 | SOLD_CORE_UNIT | Venda de 'DA_18_Alistar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-5 | 228 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-6 | 236 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-6 | 238 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 4-7 | 247 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 5-1 | 256 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_LeBlanc' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 5-2 | 264 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 6-1 | 316 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 6-5 | 354 | SOLD_CORE_UNIT | Venda de 'DA_Krug18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 6-5 | 357 | SOLD_CORE_UNIT | Venda de 'DA_Scuttlecrab18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 2-1 | 596 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-4 | 1001 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-7 | 1395 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-1 | 1526 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-2 | 1616 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-3 | 1752 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1753 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 1888 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1889 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 2027 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 2028 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 2137 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 2138 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 2224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 2225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 2369 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-1 | 2370 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2471 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2581 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2582 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 2722 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2723 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2858 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-5 | 2859 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 3001 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 3002 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 3135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-7 | 3136 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-1 | 3275 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-1 | 3276 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-2 | 3420 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-2 | 3421 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-3 | 3561 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-3 | 3562 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-4 | 3704 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-4 | 3705 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-5 | 3833 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-5 | 3834 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-6 | 3912 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-6 | 3913 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-7 | 4013 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-7 | 4014 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-1 | 4152 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-1 | 4153 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-2 | 4291 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-2 | 4292 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-3 | 4426 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-3 | 4427 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-4 | 4565 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-4 | 4566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-5 | 4706 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 6-5 | 4707 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 6-6 | 4843 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 6-6 | 4844 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-4 | 1110 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-5 | 1231 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-5 | 1242 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-3 | 2657 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-4 | 2808 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-5 | 2923 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-6 | 3075 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-6 | 3111 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-7 | 3200 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-1 | 3317 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-1 | 3356 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-2 | 3460 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-2 | 3525 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-3 | 3614 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-4 | 3771 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-6 | 3977 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-7 | 4066 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 5-7 | 4103 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 6-1 | 4231 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 6-2 | 4318 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 1-3 | 26 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 1-4 | 31 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 1-4 | 33 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sejuani) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 1-4 | 35 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kayle) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 1-4 | 37 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 1-4 | 39 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 2-1 | 42 | PURCHASE_SALE_REVIEW | Compra de DA_18_Cassiopeia foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 2-1 | 44 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 2-1 | 46 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 5 | 2-3 | 63 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 5 | 2-3 | 65 | PURCHASE_SALE_REVIEW | Compra de DA_18_Camille foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 2-4 | 76 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-1 | 112 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 3-1 | 114 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-1 | 114 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Tristana) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-2 | 124 | PURCHASE_SALE_REVIEW | Compra de DA_18_Shen foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 3-2 | 126 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-3 | 131 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Tristana) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-4 | 141 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-4 | 143 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Tristana) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 173 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 176 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Tristana) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 4-1 | 181 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Vi18) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 4-2 | 193 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rammus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 5 | 4-7 | 243 | SOLD_CORE_UNIT | Venda de 'DA_18_Sejuani' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-3 | 277 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-5 | 296 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-2 | 328 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 1-3 | 295 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 1-4 | 427 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-1 | 559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-2 | 666 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-3 | 802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-4 | 933 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-5 | 1056 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-6 | 1131 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-7 | 1264 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-1 | 1398 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-2 | 1532 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-5 | 1896 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1897 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-6 | 1981 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1982 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-7 | 2115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 2116 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-1 | 2227 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-2 | 2360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-3 | 2501 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 2702 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2792 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2902 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-7 | 2903 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 3016 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 3017 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 3147 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 3148 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 3286 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-3 | 3287 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3401 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-4 | 3402 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3531 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 3708 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 3825 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-2 | 3974 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-2 | 3975 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 2-6 | 1196 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-6 | 1207 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-6 | 1218 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-2 | 2411 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-4 | 2641 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-2 | 3226 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-4 | 3469 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 1-2 | 12 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yorick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 1-2 | 18 | PURCHASE_SALE_REVIEW | Compra de DA_18_Xayah foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 1-3 | 21 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Varus) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 1-3 | 23 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 1-3 | 25 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 6 | 1-3 | 27 | PURCHASE_SALE_REVIEW | Compra de DA_18_Xayah foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 1-4 | 34 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 1-4 | 36 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 1-4 | 39 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 6 | 2-2 | 53 | PURCHASE_SALE_REVIEW | Compra de DA_18_Tristana foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-3 | 66 | PURCHASE_SALE_REVIEW | Compra de DA_Gromp18_AP foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-4 | 71 | PURCHASE_SALE_REVIEW | Compra de DA_18_Teemo foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-4 | 75 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-4 | 79 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 2-5 | 82 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 6 | 2-5 | 84 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yorick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 6 | 2-6 | 95 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 2-7 | 103 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 2-7 | 107 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 3-1 | 111 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 3-4 | 141 | PURCHASE_SALE_REVIEW | Compra de DA_18_Tristana foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 3-5 | 153 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 3-6 | 163 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-4 | 211 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-4 | 213 | SOLD_CORE_UNIT | Venda de 'DA_18_Soraka' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-4 | 218 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 4-5 | 221 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 4-5 | 223 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 6 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 212 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 2-2 | 732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-3 | 867 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-4 | 1002 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-5 | 1134 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-6 | 1271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-7 | 1405 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-1 | 1540 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1541 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-2 | 1680 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-3 | 1823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1953 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 2083 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 2209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 2319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 2446 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2681 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2815 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2947 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 3035 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 3112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 3239 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 3328 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 3430 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-3 | 3431 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 2-2 | 844 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-3 | 955 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-3 | 966 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 1076 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 1099 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-3 | 2767 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-4 | 2877 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 1-2 | 12 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 1-4 | 31 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 7 | 1-4 | 33 | PURCHASE_SALE_REVIEW | Compra de DA_18_Elise foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 7 | 1-4 | 35 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 7 | 1-4 | 37 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 7 | 1-4 | 39 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-1 | 44 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-3 | 67 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-3 | 69 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Varus) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 7 | 2-5 | 83 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 7 | 2-5 | 88 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Karma18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-6 | 91 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 7 | 2-6 | 93 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 2-6 | 93 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-6 | 95 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-6 | 97 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Karma18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 2-6 | 99 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 3-1 | 115 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Karma18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 7 | 3-1 | 117 | PURCHASE_SALE_REVIEW | Compra de DA_18_Ornn foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 7 | 3-2 | 122 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-2 | 122 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_CrimsonRaptor18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 3-2 | 126 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Vi18) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 7 | 3-3 | 131 | PURCHASE_SALE_REVIEW | Compra de DA_18_Ornn foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 7 | 3-4 | 141 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-5 | 151 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-5 | 151 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 4-1 | 189 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-2 | 198 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-3 | 201 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-4 | 213 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Aphelios' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-6 | 231 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-7 | 241 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-7 | 248 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-2 | 265 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 5-3 | 274 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 5-3 | 276 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 5-3 | 279 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 2-7 | 1371 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1508 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1641 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1778 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1908 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 2009 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 2108 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 2243 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2382 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2528 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2666 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2803 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2936 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 3073 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 3215 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 3353 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 3490 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 3629 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-3 | 3630 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 2-3 | 950 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-6 | 2170 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-7 | 2345 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-1 | 2478 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-2 | 2616 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-3 | 2755 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-4 | 2864 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-5 | 3025 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-3 | 22 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 1-3 | 24 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Yorick) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 1-3 | 26 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 1-3 | 28 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Karma18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 1-4 | 31 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 1-4 | 37 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-1 | 41 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-1 | 47 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Karma18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 2-2 | 51 | PURCHASE_SALE_REVIEW | Compra de DA_18_Leona foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-3 | 61 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-3 | 63 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-3 | 65 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-3 | 67 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Veigar) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-4 | 71 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 2-4 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_18_Shen foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-4 | 78 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-5 | 81 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 8 | 2-5 | 85 | SOLD_CORE_UNIT | Venda de 'DA_Krug18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 2-5 | 87 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-5 | 89 | PURCHASE_SALE_REVIEW | Compra de DA_18_Kobuko foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-6 | 92 | PURCHASE_SALE_REVIEW | Compra de DA_18_Tristana foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-7 | 104 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 2-7 | 106 | PURCHASE_SALE_REVIEW | Compra de DA_18_Tristana foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 3-4 | 142 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_CrimsonRaptor18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-5 | 153 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-3 | 201 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Krug18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-5 | 228 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-7 | 245 | SOLD_CORE_UNIT | Venda de 'DA_Murkwolf18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 5-1 | 258 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 6-5 | 352 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 6-6 | 365 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-6 | 94 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 8 | 2-7 | 104 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| LOW | Jogador 8 | 1-1 | 80 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 3-3 | 1757 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1863 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1994 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 2089 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 2187 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2396 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2536 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2672 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2809 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 3084 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 3220 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 3354 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-2 | 3355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-3 | 3497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-3 | 3498 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-4 | 3643 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-5 | 3774 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-6 | 3848 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-7 | 3946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-1 | 4084 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-2 | 4221 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-3 | 4363 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-4 | 4501 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-5 | 4640 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-6 | 4780 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| MEDIUM | Jogador 8 | 2-6 | 1294 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-2 | 2435 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-2 | 2485 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-3 | 2599 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-3 | 2636 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-4 | 2698 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-4 | 2759 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-5 | 2873 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-5 | 2910 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-6 | 2999 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-6 | 3036 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-7 | 3172 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-1 | 3306 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-2 | 3395 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-3 | 3551 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-4 | 3699 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-4 | 3738 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-5 | 3824 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-6 | 3898 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-7 | 3985 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-7 | 4035 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
