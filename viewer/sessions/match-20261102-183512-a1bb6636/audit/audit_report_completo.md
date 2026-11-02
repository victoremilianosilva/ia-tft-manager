# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4861**
- Achados: **149**
- CRITICAL: 0 | HIGH: 9 | MEDIUM: 99 | LOW: 41

## Metadados da sessão

- Match ID: a1bb6636-3f28-491f-933f-0d47c62fcc7f
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 31f2eae09c7047c90ab4814e194d7cbc0b0ff4caf7abfd663e3d7a39a5e90f10
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4089**
- Entradas posteriores à eliminação ignoradas: **772**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 0 | 7 | 14 | 16 | 47 | 0 | 1 | não/inconclusivo | 1 |
| Jogador 6 | 1 | 7 | 15 | 32 | 46 | 3 | 1 | não/inconclusivo | 1 |
| Jogador 7 | 12 | 7 | 10 | 26 | 44 | 3 | 1 | sim | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 193 | 43 | 16 | 16 | 20 | 27 | 68 | 0.0133 | 22 | 3 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::ITEM: 1, ALL_IN::PASS: 3, ALL_IN::REROLL: 7, ALL_IN::SELL: 1, FAST8::BUY: 19, FAST8::BUY_XP: 13, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 5, FAST8::MOVE_BOARD: 2, FAST8::PASS: 6, FAST8::REROLL: 5, FAST8::SELL: 4, SLOWROLL::BUY: 7, SLOWROLL::BUY_XP: 2, SLOWROLL::MOVE_BENCH: 41, SLOWROLL::PASS: 9, SLOWROLL::SELL: 3, STABILIZE::BUY: 15, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 1, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 6, STABILIZE::PASS: 9, STABILIZE::REROLL: 8, STABILIZE::SELL: 8
- Jogador 1 — recompensas por ação: BUY: média 0.3756 (n=43), BUY_XP: média -0.0006 (n=16), ITEM: média 0.1167 (n=3), MOVE_BENCH: média -0.1113 (n=60), MOVE_BOARD: média -0.1013 (n=8), PASS: média -0.0378 (n=27), REROLL: média -0.1115 (n=20), SELL: média -0.1994 (n=16)
| Jogador 2 | 243 | 70 | 41 | 25 | 7 | 38 | 58 | 0.0492 | 20 | 10 |
- Jogador 2 — ações por estratégia: ECON::BUY: 12, ECON::BUY_XP: 3, ECON::ITEM: 2, ECON::MOVE_BENCH: 6, ECON::PASS: 6, ECON::REROLL: 1, ECON::SELL: 2, FAST8::BUY: 8, FAST8::BUY_XP: 13, FAST8::MOVE_BENCH: 17, FAST8::PASS: 10, FAST8::SELL: 5, SLOWROLL::BUY: 5, SLOWROLL::BUY_XP: 8, SLOWROLL::MOVE_BENCH: 16, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::PASS: 6, SLOWROLL::SELL: 3, STABILIZE::BUY: 5, STABILIZE::BUY_XP: 1, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 5, STABILIZE::SELL: 1, WINSTREAK::BUY: 40, WINSTREAK::ITEM: 2, WINSTREAK::MOVE_BENCH: 8, WINSTREAK::PASS: 11, WINSTREAK::REROLL: 6, WINSTREAK::SELL: 30
- Jogador 2 — recompensas por ação: BUY: média 0.3199 (n=70), BUY_XP: média -0.0372 (n=25), ITEM: média 0.0300 (n=4), MOVE_BENCH: média -0.0429 (n=56), MOVE_BOARD: média -0.0750 (n=2), PASS: média -0.0234 (n=38), REROLL: média -0.1314 (n=7), SELL: média -0.1285 (n=41)
| Jogador 3 | 162 | 21 | 2 | 37 | 0 | 28 | 72 | -0.0374 | 15 | 5 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::PASS: 1, ECON::BUY_XP: 1, ECON::MOVE_BENCH: 5, ECON::PASS: 1, FAST8::BUY: 2, FAST8::BUY_XP: 15, FAST8::MOVE_BENCH: 4, FAST8::PASS: 2, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 6, SLOWROLL::MOVE_BENCH: 33, SLOWROLL::PASS: 10, STABILIZE::BUY: 15, STABILIZE::BUY_XP: 15, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 28, STABILIZE::MOVE_BOARD: 2, STABILIZE::PASS: 14, STABILIZE::SELL: 2
- Jogador 3 — recompensas por ação: BUY: média 0.2490 (n=21), BUY_XP: média 0.0108 (n=37), ITEM: média 0.0600 (n=2), MOVE_BENCH: média -0.1374 (n=70), MOVE_BOARD: média -0.1850 (n=2), PASS: média -0.0629 (n=28), SELL: média -0.0250 (n=2)
| Jogador 4 | 192 | 47 | 16 | 14 | 13 | 26 | 74 | 0.0331 | 20 | 4 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 1, ALL_IN::PASS: 2, ALL_IN::REROLL: 5, ALL_IN::SELL: 2, FAST8::BUY: 11, FAST8::BUY_XP: 9, FAST8::MOVE_BENCH: 12, FAST8::MOVE_BOARD: 3, FAST8::PASS: 4, LOSS_STREAK::MOVE_BENCH: 3, LOSS_STREAK::PASS: 1, SLOWROLL::BUY: 5, SLOWROLL::BUY_XP: 5, SLOWROLL::MOVE_BENCH: 13, SLOWROLL::PASS: 4, STABILIZE::BUY: 26, STABILIZE::ITEM: 1, STABILIZE::MOVE_BENCH: 37, STABILIZE::MOVE_BOARD: 5, STABILIZE::PASS: 15, STABILIZE::REROLL: 8, STABILIZE::SELL: 14
- Jogador 4 — recompensas por ação: BUY: média 0.3587 (n=47), BUY_XP: média -0.0386 (n=14), ITEM: média 0.0550 (n=2), MOVE_BENCH: média -0.1165 (n=66), MOVE_BOARD: média -0.0825 (n=8), PASS: média -0.0158 (n=26), REROLL: média -0.0961 (n=13), SELL: média -0.0044 (n=16)
| Jogador 5 | 186 | 48 | 24 | 20 | 12 | 30 | 50 | 0.0172 | 19 | 4 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::ITEM: 1, ALL_IN::PASS: 2, ALL_IN::REROLL: 2, ALL_IN::SELL: 8, FAST8::BUY: 20, FAST8::BUY_XP: 8, FAST8::MOVE_BENCH: 5, FAST8::MOVE_BOARD: 2, FAST8::PASS: 10, FAST8::REROLL: 6, FAST8::SELL: 6, STABILIZE::BUY: 19, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 1, STABILIZE::MOVE_BENCH: 39, STABILIZE::MOVE_BOARD: 4, STABILIZE::PASS: 18, STABILIZE::REROLL: 4, STABILIZE::SELL: 10
- Jogador 5 — recompensas por ação: BUY: média 0.2658 (n=48), BUY_XP: média -0.0365 (n=20), ITEM: média 0.0400 (n=2), MOVE_BENCH: média -0.0973 (n=44), MOVE_BOARD: média -0.0467 (n=6), PASS: média -0.0193 (n=30), REROLL: média -0.1200 (n=12), SELL: média -0.0971 (n=24)
| Jogador 6 | 190 | 46 | 21 | 15 | 27 | 27 | 52 | 0.0256 | 11 | 4 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::PASS: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 1, FAST8::BUY: 20, FAST8::BUY_XP: 11, FAST8::MOVE_BENCH: 12, FAST8::PASS: 7, FAST8::REROLL: 7, FAST8::SELL: 7, SLOWROLL::BUY: 5, SLOWROLL::BUY_XP: 2, SLOWROLL::MOVE_BENCH: 15, SLOWROLL::PASS: 4, SLOWROLL::SELL: 1, STABILIZE::BUY: 20, STABILIZE::BUY_XP: 2, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 23, STABILIZE::MOVE_BOARD: 2, STABILIZE::PASS: 15, STABILIZE::REROLL: 19, STABILIZE::SELL: 12
- Jogador 6 — recompensas por ação: BUY: média 0.3585 (n=46), BUY_XP: média -0.0207 (n=15), ITEM: média 0.0900 (n=2), MOVE_BENCH: média -0.0984 (n=50), MOVE_BOARD: média -0.0200 (n=2), PASS: média -0.0344 (n=27), REROLL: média -0.1141 (n=27), SELL: média -0.1200 (n=21)
| Jogador 7 | 155 | 44 | 20 | 10 | 21 | 23 | 37 | 0.0081 | 6 | 6 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::PASS: 2, ALL_IN::REROLL: 6, ALL_IN::SELL: 7, FAST8::BUY: 5, FAST8::BUY_XP: 7, FAST8::MOVE_BENCH: 1, FAST8::PASS: 1, FAST8::REROLL: 1, FAST8::SELL: 1, SLOWROLL::BUY: 7, SLOWROLL::BUY_XP: 2, SLOWROLL::MOVE_BENCH: 18, SLOWROLL::PASS: 9, SLOWROLL::REROLL: 4, STABILIZE::BUY: 25, STABILIZE::BUY_XP: 1, STABILIZE::MOVE_BENCH: 16, STABILIZE::MOVE_BOARD: 2, STABILIZE::PASS: 11, STABILIZE::REROLL: 10, STABILIZE::SELL: 12
- Jogador 7 — recompensas por ação: BUY: média 0.3016 (n=44), BUY_XP: média 0.0290 (n=10), MOVE_BENCH: média -0.2069 (n=35), MOVE_BOARD: média -0.0900 (n=2), PASS: média -0.0470 (n=23), REROLL: média -0.0943 (n=21), SELL: média -0.0910 (n=20)
| Jogador 8 | 266 | 79 | 48 | 23 | 15 | 38 | 59 | 0.0337 | 25 | 5 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 14, ALL_IN::MOVE_BENCH: 3, ALL_IN::PASS: 3, ALL_IN::REROLL: 4, ALL_IN::SELL: 9, ECON::BUY: 9, ECON::ITEM: 2, ECON::PASS: 2, ECON::REROLL: 3, ECON::SELL: 6, FAST8::BUY: 4, FAST8::BUY_XP: 19, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 9, FAST8::PASS: 6, FAST8::SELL: 2, STABILIZE::BUY: 22, STABILIZE::BUY_XP: 3, STABILIZE::MOVE_BENCH: 38, STABILIZE::MOVE_BOARD: 5, STABILIZE::PASS: 15, STABILIZE::REROLL: 5, STABILIZE::SELL: 15, WINSTREAK::BUY: 30, WINSTREAK::BUY_XP: 1, WINSTREAK::ITEM: 1, WINSTREAK::MOVE_BENCH: 4, WINSTREAK::PASS: 12, WINSTREAK::REROLL: 3, WINSTREAK::SELL: 16
- Jogador 8 — recompensas por ação: BUY: média 0.3283 (n=79), BUY_XP: média -0.0274 (n=23), ITEM: média 0.0500 (n=4), MOVE_BENCH: média -0.1028 (n=54), MOVE_BOARD: média -0.0840 (n=5), PASS: média -0.0916 (n=38), REROLL: média -0.0947 (n=15), SELL: média -0.1181 (n=48)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 18:35:17 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.5200 |  |
| Jogador 1 | ? | 18:35:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 18:35:23 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 1-1 | 18:35:23 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3800 |  |
| Jogador 1 | 1-1 | 18:35:24 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2700 |  |
| Jogador 1 | 1-1 | 18:35:24 | MOVE Board -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.1000 |  |
| Jogador 1 | 1-1 | 18:35:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-2 | 18:35:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.2200 |  |
| Jogador 1 | 1-2 | 18:35:30 | MOVE Bench -> Board: Grompe (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | -0.7600 |  |
| Jogador 1 | 1-2 | 18:35:30 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.6300 |  |
| Jogador 1 | 1-2 | 18:35:30 | MOVE Board -> Board: Ornn (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | -0.1000 |  |
| Jogador 1 | 1-2 | 18:35:31 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | -0.2100 |  |
| Jogador 1 | 1-2 | 18:35:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 1 | 1-3 | 18:35:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Gromp18_AP | 1.0400 |  |
| Jogador 1 | 1-3 | 18:35:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 1 | 1-3 | 18:35:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 18:35:42 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Gromp18_AP | 0.2700 |  |
| Jogador 1 | 1-4 | 18:35:43 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Gromp18_AP | 0.0600 |  |
| Jogador 1 | 1-4 | 18:35:43 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Gromp18_AP | -0.2800 |  |
| Jogador 1 | 1-4 | 18:35:43 | MOVE Bench -> Board: Akali (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 1 | 1-4 | 18:35:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 1-4 | 18:35:44 | MOVE Board -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | -0.1000 |  |
| Jogador 1 | 1-4 | 18:35:44 | MOVE Board -> Board: Ornn (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.1000 |  |
| Jogador 1 | 1-4 | 18:35:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-1 | 18:35:49 | MOVE Bench -> Board: Grompe (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.4400 |  |
| Jogador 1 | 2-1 | 18:35:49 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Sejuani | -0.2800 |  |
| Jogador 1 | 2-1 | 18:35:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-2 | 18:35:56 | MOVE Bench -> Board: Akali (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Sejuani | 0.2300 |  |
| Jogador 1 | 2-2 | 18:35:56 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Sejuani | -0.4300 |  |
| Jogador 1 | 2-2 | 18:35:56 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Sejuani | 1.0100 |  |
| Jogador 1 | 2-2 | 18:35:56 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Sejuani | -0.3600 |  |
| Jogador 1 | 2-2 | 18:35:56 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Sejuani | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-2 | 18:35:57 | MOVE Bench -> Board: Akali (i:2.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Sejuani | 0.0800 |  |
| Jogador 1 | 2-2 | 18:35:57 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Sejuani | -0.4000 |  |
| Jogador 1 | 2-2 | 18:35:57 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Sejuani | 0.5300 |  |
| Jogador 1 | 2-2 | 18:35:57 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_18_Sejuani | 0.3000 |  |
| Jogador 1 | 2-2 | 18:35:58 | MOVE Bench -> Board: Shen (i:4.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_18_Sejuani | -0.3100 |  |
| Jogador 1 | 2-2 | 18:35:58 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-3 | 18:36:02 | VENDEU: Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 0 | — | DA_18_Sejuani | -0.8700 |  |
| Jogador 1 | 2-3 | 18:36:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 1 | 2-3 | 18:36:03 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_KogMaw18_AD | -0.4200 |  |
| Jogador 1 | 2-3 | 18:36:03 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 1 | 2-3 | 18:36:04 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 18:36:09 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Kog'Maw (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 16 | 1 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 2-4 | 18:36:09 | VENDEU: Kog'Maw (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Inferno | DA_18_Sejuani | -0.4900 |  |
| Jogador 1 | 2-4 | 18:36:10 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Inferno | DA_18_Sejuani | 0.9900 |  |
| Jogador 1 | 2-4 | 18:36:10 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Inferno | DA_18_Shen | 0.1000 |  |
| Jogador 1 | 2-4 | 18:36:11 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Inferno | DA_18_Shen | -0.6400 |  |
| Jogador 1 | 2-4 | 18:36:11 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Inferno | DA_18_Shen | -0.4000 |  |
| Jogador 1 | 2-4 | 18:36:11 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 2-5 | 18:36:16 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Inferno | DA_18_Shen | 0.1000 |  |
| Jogador 1 | 2-5 | 18:36:17 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Inferno | DA_18_Sejuani | -0.6400 |  |
| Jogador 1 | 2-5 | 18:36:17 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Inferno | DA_18_Sejuani | 0.0900 |  |
| Jogador 1 | 2-5 | 18:36:17 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Inferno | DA_18_Sejuani | -0.4000 |  |
| Jogador 1 | 2-5 | 18:36:17 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Inferno | DA_18_Sejuani | -0.6300 |  |
| Jogador 1 | 2-5 | 18:36:18 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 23 | 1 | Inferno | DA_18_Sejuani | -0.0200 |  |
| Jogador 1 | 2-6 | 18:36:23 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 2 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 2-6 | 18:36:23 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 2 | Inferno | DA_18_Shen | -0.4000 |  |
| Jogador 1 | 2-6 | 18:36:24 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 2 | Inferno | DA_18_Sejuani | -0.6300 |  |
| Jogador 1 | 2-6 | 18:36:24 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 31 | 2 | Inferno | DA_18_Sejuani | -0.0400 |  |
| Jogador 1 | 2-7 | 18:36:31 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Inferno | DA_18_Sejuani | -0.4000 |  |
| Jogador 1 | 2-7 | 18:36:31 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 2-7 | 18:36:31 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Inferno | DA_18_Shen | -0.4000 |  |
| Jogador 1 | 2-7 | 18:36:32 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Inferno | DA_18_Sejuani | -0.6300 |  |
| Jogador 1 | 2-7 | 18:36:32 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Inferno | DA_18_Sejuani | -0.1100 |  |
| Jogador 1 | 3-1 | 18:36:38 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 50 | 4 | Inferno | DA_18_Sejuani | 0.0900 |  |
| Jogador 1 | 3-1 | 18:36:38 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 50 | 4 | Inferno | DA_18_Sejuani | -0.4000 |  |
| Jogador 1 | 3-1 | 18:36:39 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Ornn (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 50 | 4 | Inferno | DA_18_Sejuani | 0.0900 |  |
| Jogador 1 | 3-1 | 18:36:39 | VENDEU: Ornn (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 51 | 4 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 3-1 | 18:36:40 | COMPROU: Ezreal (Custo 4 \| i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 47 | 4 | Inferno | DA_18_Ezreal | -0.3700 |  |
| Jogador 1 | 3-1 | 18:36:40 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 47 | 4 | Inferno | DA_18_Ezreal | -0.5300 |  |
| Jogador 1 | 3-1 | 18:36:41 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 47 | 4 | Inferno | DA_18_Ezreal | -0.6000 |  |
| Jogador 1 | 3-1 | 18:36:41 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 47 | 4 | Inferno | DA_18_Ezreal | -0.1100 |  |
| Jogador 1 | 3-2 | 18:36:45 | MOVE Bench -> Board: Shen (i:4.0) <-> Ezreal (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 4 | Inferno | DA_18_Ezreal | 0.2300 |  |
| Jogador 1 | 3-2 | 18:36:45 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 4 | Inferno | DA_18_Ezreal | -0.5300 |  |
| Jogador 1 | 3-2 | 18:36:47 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 4 | Inferno | DA_18_Ezreal | -0.6000 |  |
| Jogador 1 | 3-2 | 18:36:47 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 4 | Inferno | DA_18_Ezreal | -0.1200 |  |
| Jogador 1 | 3-3 | 18:36:52 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 67 | 5 | Inferno | DA_18_Ezreal | -0.4000 |  |
| Jogador 1 | 3-3 | 18:36:53 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 67 | 5 | Inferno | DA_18_Ezreal | 0.0900 |  |
| Jogador 1 | 3-3 | 18:36:53 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Ezreal (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 67 | 5 | Inferno | DA_18_Ezreal | 0.2300 |  |
| Jogador 1 | 3-3 | 18:36:53 | COMPROU: Varus (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 66 | 5 | Inferno | DA_18_Ezreal | 0.3300 |  |
| Jogador 1 | 3-3 | 18:36:53 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Ezreal | 0.2200 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 3-3 | 18:36:54 | MOVE Bench -> Board: Varus (i:2.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Ezreal | -0.4800 |  |
| Jogador 1 | 3-3 | 18:36:54 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Ezreal | 0.0900 |  |
| Jogador 1 | 3-3 | 18:36:54 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Varus (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Ezreal | -0.2500 |  |
| Jogador 1 | 3-3 | 18:36:55 | MOVE Bench -> Board: Varus (i:2.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Ezreal | -0.4800 |  |
| Jogador 1 | 3-3 | 18:36:55 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Ezreal | -0.1300 |  |
| Jogador 1 | 3-3 | 18:36:57 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Ezreal | 0.3300 |  |
| Jogador 1 | 3-4 | 18:37:00 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 70 | 5 | Inferno | DA_18_Shen | 0.9400 |  |
| Jogador 1 | 3-4 | 18:37:00 | MOVE Bench -> Board: Shen (i:8.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 70 | 5 | Inferno | DA_18_Shen | 0.2400 |  |
| Jogador 1 | 3-4 | 18:37:01 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Inferno | DA_18_Shen | 0.1300 |  |
| Jogador 1 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 5 | Inferno | DA_18_Shen | -0.0800 |  |
| Jogador 1 | 3-4 | 18:37:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-4 | 18:37:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 5 | Inferno | DA_18_Shen | -0.1300 |  |
| Jogador 1 | 3-5 | 18:37:08 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Inferno | DA_18_Shen | 0.2900 |  |
| Jogador 1 | 3-5 | 18:37:08 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Inferno | DA_18_Shen | 0.8000 |  |
| Jogador 1 | 3-5 | 18:37:08 | COMPROU: Sejuani (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 45 | 4 | Inferno | DA_18_Shen | 0.8300 |  |
| Jogador 1 | 3-5 | 18:37:09 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 45 | 4 | Inferno | DA_18_Shen | -0.5700 |  |
| Jogador 1 | 3-5 | 18:37:09 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 45 | 4 | Inferno | DA_18_Shen | 0.3900 |  |
| Jogador 1 | 3-5 | 18:37:09 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 4 | Inferno | DA_18_Shen | -0.3000 |  |
| Jogador 1 | 3-5 | 18:37:10 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 4 | Inferno | DA_18_Shen | 0.4500 |  |
| Jogador 1 | 3-5 | 18:37:10 | MOVE Board -> Board: Sejuani (i:8.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 4 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 3-5 | 18:37:10 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 4 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 3-5 | 18:37:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 4 | Inferno | DA_18_Shen | 0.0800 |  |
| Jogador 1 | 3-5 | 18:37:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 4 | Inferno | DA_18_Shen | -0.1300 |  |
| Jogador 1 | 3-6 | 18:37:16 | COMPROU: Lux (Feérica) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Inferno | DA_18_Shen | -0.1500 |  |
| Jogador 1 | 3-6 | 18:37:17 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 4 | Inferno | DA_18_Shen | 0.2500 |  |
| Jogador 1 | 3-6 | 18:37:17 | MOVE Bench -> Board: Lux (Feérica) (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 4 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 3-6 | 18:37:17 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Inferno | DA_18_Shen | 0.2500 |  |
| Jogador 1 | 3-6 | 18:37:17 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Inferno | DA_18_Shen | 0.4900 |  |
| Jogador 1 | 3-6 | 18:37:18 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 4 | Inferno | DA_18_Shen | -0.0800 |  |
| Jogador 1 | 3-6 | 18:37:18 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 4 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-6 | 18:37:18 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 4 | Inferno | DA_18_Shen | -0.0800 |  |
| Jogador 1 | 3-6 | 18:37:18 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 4 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-6 | 18:37:20 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 4 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-6 | 18:37:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 4 | Inferno | DA_18_Shen | -0.0600 |  |
| Jogador 1 | 3-7 | 18:37:25 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Inferno | DA_18_Shen | -0.0600 |  |
| Jogador 1 | 3-7 | 18:37:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 2 | Inferno | DA_18_Shen | -0.0600 |  |
| Jogador 1 | 3-7 | 18:37:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 2 | Inferno | DA_18_Shen | 0.6800 |  |
| Jogador 1 | 3-7 | 18:37:26 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 2 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-7 | 18:37:26 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 2 | Inferno | DA_18_Shen | -0.0800 |  |
| Jogador 1 | 3-7 | 18:37:26 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NeedlesslyLargeRod -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 2 | Inferno | DA_18_Shen | 0.2200 |  |
| Jogador 1 | 3-7 | 18:37:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 2 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-1 | 18:37:34 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Inferno | DA_18_Shen | 0.6800 |  |
| Jogador 1 | 4-1 | 18:37:34 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Inferno | DA_18_Shen | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 1 | 4-1 | 18:37:34 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Inferno | DA_18_Shen | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 1 | 4-1 | 18:37:34 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Inferno | DA_18_Shen | 0.0500 |  |
| Jogador 1 | 4-1 | 18:37:35 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Inferno | DA_18_Tristana | 0.7600 |  |
| Jogador 1 | 4-1 | 18:37:35 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Inferno | DA_18_Tristana | 0.7300 |  |
| Jogador 1 | 4-1 | 18:37:35 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Inferno | DA_18_Tristana | 0.4200 |  |
| Jogador 1 | 4-1 | 18:37:36 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 1 | Inferno | DA_18_Tristana | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 1 | 4-1 | 18:37:36 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Inferno | DA_18_Tristana | 0.1300 |  |
| Jogador 1 | 4-1 | 18:37:38 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 1 | Inferno | DA_18_Tristana | -0.0200 |  |
| Jogador 1 | 4-1 | 18:37:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 1 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 1 | 4-2 | 18:37:43 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Inferno | DA_18_Tristana | -0.2400 | FAST8_REROLL_REVIEW |
| Jogador 1 | 4-2 | 18:37:43 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Inferno | DA_18_Tristana | -0.2700 |  |
| Jogador 1 | 4-2 | 18:37:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Inferno | DA_18_Tristana | 0.6500 |  |
| Jogador 1 | 4-2 | 18:37:44 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_18_Tristana | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 1 | 4-2 | 18:37:44 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Inferno | DA_18_Tristana | 0.1200 |  |
| Jogador 1 | 4-2 | 18:37:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 1 | 4-2 | 18:37:45 | COMPROU: Sett (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 4-2 | 18:37:45 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 1 | 4-2 | 18:37:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-3 | 18:37:53 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 4-3 | 18:37:53 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 4-3 | 18:37:53 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-3 | 18:37:53 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 4-3 | 18:37:53 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 4-3 | 18:37:54 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 4-3 | 18:37:54 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 1 | 4-3 | 18:37:54 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 4-3 | 18:37:54 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-3 | 18:37:56 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-4 | 18:38:02 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 18:38:03 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 18:38:03 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 18:38:03 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.4200 |  |
| Jogador 1 | 4-4 | 18:38:03 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 1 | 4-4 | 18:38:04 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 18:38:04 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Inferno | DA_KogMaw18_AD | -0.8600 |  |
| Jogador 1 | 4-4 | 18:38:04 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Fiddlesticks (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Inferno | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 4-4 | 18:38:05 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 4-4 | 18:38:07 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 18:38:07 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-5 | 18:38:11 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Inferno | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 4-5 | 18:38:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 4-5 | 18:38:11 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Inferno | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 1 | 4-5 | 18:38:12 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 1 | 4-5 | 18:38:12 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 4-5 | 18:38:12 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 1 | 4-5 | 18:38:12 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 4-5 | 18:38:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-5 | 18:38:13 | MOVE Bench -> Board: Sett (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 1 | 4-5 | 18:38:13 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-6 | 18:38:19 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 1 | 4-6 | 18:38:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-6 | 18:38:22 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 4-7 | 18:38:28 | BIGORNA: escolheu componente TFT_Item_RecurveBow | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-7 | 18:38:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-7 | 18:38:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-7 | 18:38:29 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 4-7 | 18:38:29 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.7900 |  |
| Jogador 1 | 4-7 | 18:38:30 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-7 | 18:38:30 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 5-1 | 18:38:37 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 5-1 | 18:38:37 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 5-1 | 18:38:37 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 5-1 | 18:38:38 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 2 | ? | 18:35:17 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0200 |  |
| Jogador 2 | ? | 18:35:17 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.3100 |  |
| Jogador 2 | ? | 18:35:18 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.6000 |  |
| Jogador 2 | ? | 18:35:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-1 | 18:35:23 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 2 | 1-1 | 18:35:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.3600 |  |
| Jogador 2 | 1-1 | 18:35:24 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.2100 |  |
| Jogador 2 | 1-1 | 18:35:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2600 |  |
| Jogador 2 | 1-1 | 18:35:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5700 |  |
| Jogador 2 | 1-1 | 18:35:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-2 | 18:35:29 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 2 | 1-2 | 18:35:30 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.3600 |  |
| Jogador 2 | 1-2 | 18:35:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-3 | 18:35:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-4 | 18:35:42 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Sejuani | -0.3200 |  |
| Jogador 2 | 1-4 | 18:35:43 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Yorick | 0.5800 |  |
| Jogador 2 | 1-4 | 18:35:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 2 | 1-4 | 18:35:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.0400 |  |
| Jogador 2 | 1-4 | 18:35:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-4 | 18:35:44 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.2800 |  |
| Jogador 2 | 1-4 | 18:35:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 2-1 | 18:35:49 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Yorick | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-1 | 18:35:49 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 2 | 2-1 | 18:35:50 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 2 | 2-1 | 18:35:50 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_18_Rakan | -0.3200 |  |
| Jogador 2 | 2-1 | 18:35:51 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_18_Sejuani | -0.3900 |  |
| Jogador 2 | 2-1 | 18:35:51 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 2-2 | 18:35:56 | MOVE Bench -> Board: Rakan (i:2.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | — | DA_18_Sejuani | -0.0600 |  |
| Jogador 2 | 2-2 | 18:35:56 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | — | DA_18_Shen | -0.3200 |  |
| Jogador 2 | 2-2 | 18:35:56 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 9 | 0 | — | DA_18_Shen | 0.0000 |  |
| Jogador 2 | 2-3 | 18:36:02 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 0 | — | DA_18_Shen | -0.3500 |  |
| Jogador 2 | 2-3 | 18:36:03 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 0 | — | DA_18_Shen | -0.6200 |  |
| Jogador 2 | 2-3 | 18:36:03 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 0 | — | DA_18_Shen | 0.0000 |  |
| Jogador 2 | 2-4 | 18:36:09 | MOVE Bench -> Board: Yorick (i:2.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Colosso | DA_18_Yorick | -0.3700 |  |
| Jogador 2 | 2-4 | 18:36:09 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Colosso | DA_18_Yorick | -0.3200 |  |
| Jogador 2 | 2-4 | 18:36:10 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 20 | 1 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 2 | 2-5 | 18:36:16 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 2 | Colosso | DA_18_Sejuani | -0.3900 |  |
| Jogador 2 | 2-5 | 18:36:17 | COMPROU: Sejuani (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 2 | Colosso | DA_18_Sejuani | 0.9700 |  |
| Jogador 2 | 2-5 | 18:36:17 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 2 | Colosso | DA_18_Sejuani | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-5 | 18:36:17 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 2 | Colosso | DA_18_Sejuani | -0.1400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-5 | 18:36:17 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Colosso | DA_18_Sejuani | 0.0100 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-5 | 18:36:18 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Colosso | DA_18_Sejuani | -0.4000 |  |
| Jogador 2 | 2-5 | 18:36:18 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Colosso | DA_18_Sejuani | 0.0200 |  |
| Jogador 2 | 2-5 | 18:36:18 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Colosso | DA_18_Sejuani | -0.3200 |  |
| Jogador 2 | 2-5 | 18:36:18 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 2 | Colosso | DA_18_Sejuani | 0.5600 |  |
| Jogador 2 | 2-5 | 18:36:19 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 2 | Colosso | DA_18_Sejuani | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-5 | 18:36:19 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 2 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 2-6 | 18:36:23 | COMPROU: Lillia (Custo 4 \| i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 1 | Colosso | DA_18_Lillia | 0.1400 |  |
| Jogador 2 | 2-6 | 18:36:23 | MOVE Bench -> Board: Lillia (i:8.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 14 | 1 | Colosso | DA_18_Lillia | -0.4000 |  |
| Jogador 2 | 2-6 | 18:36:24 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 1 | Colosso | DA_18_Lillia | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-6 | 18:36:24 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 1 | Colosso | DA_18_Lillia | -0.1400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-6 | 18:36:24 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 1 | Colosso | DA_18_Lillia | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-6 | 18:36:25 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 1 | Colosso | DA_18_Lillia | 0.0600 |  |
| Jogador 2 | 2-6 | 18:36:25 | MOVE Bench -> Board: Shen (i:4.0) <-> Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 1 | Colosso | DA_18_Lillia | -0.3200 |  |
| Jogador 2 | 2-6 | 18:36:25 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 1 | Colosso | DA_18_Lillia | -0.8500 |  |
| Jogador 2 | 2-6 | 18:36:26 | VENDEU: Yorick (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 1 | Colosso | DA_18_Lillia | -0.4800 |  |
| Jogador 2 | 2-6 | 18:36:26 | COMPROU: Kayle (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 1 | Colosso | DA_18_Lillia | 0.2900 |  |
| Jogador 2 | 2-6 | 18:36:26 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 1 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 2-7 | 18:36:31 | VENDEU: Kayle (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | Colosso | DA_18_Lillia | -0.3400 |  |
| Jogador 2 | 2-7 | 18:36:31 | COMPROU: Master Yi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | Colosso | DA_18_Lillia | -0.3300 |  |
| Jogador 2 | 2-7 | 18:36:31 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Lillia | -0.3500 |  |
| Jogador 2 | 2-7 | 18:36:32 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Lillia | 0.1000 |  |
| Jogador 2 | 2-7 | 18:36:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 2-7 | 18:36:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-1 | 18:36:38 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Lillia | -0.8900 |  |
| Jogador 2 | 3-1 | 18:36:38 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Lillia | 0.2200 |  |
| Jogador 2 | 3-1 | 18:36:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 3-1 | 18:36:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-1 | 18:36:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-2 | 18:36:45 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Lillia | 0.2100 |  |
| Jogador 2 | 3-2 | 18:36:45 | MOVE Bench -> Board: Amumu (i:8.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Amumu18 | -0.3100 |  |
| Jogador 2 | 3-2 | 18:36:47 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Amumu18 | 0.5500 |  |
| Jogador 2 | 3-2 | 18:36:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-2 | 18:36:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-3 | 18:36:52 | VENDEU: Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_Amumu18 | -0.4000 |  |
| Jogador 2 | 3-3 | 18:36:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-3 | 18:36:53 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Lillia | -0.3200 |  |
| Jogador 2 | 3-3 | 18:36:53 | MOVE Bench -> Board: Amumu (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Amumu18 | 0.1000 |  |
| Jogador 2 | 3-3 | 18:36:53 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Amumu18 | -0.8200 |  |
| Jogador 2 | 3-3 | 18:36:54 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Lillia | -0.3200 |  |
| Jogador 2 | 3-3 | 18:36:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-4 | 18:37:00 | MOVE Bench -> Board: Amumu (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_Amumu18 | 0.1000 |  |
| Jogador 2 | 3-4 | 18:37:00 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_Amumu18 | -0.3500 |  |
| Jogador 2 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-4 | 18:37:01 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Amumu18 | 0.0500 |  |
| Jogador 2 | 3-4 | 18:37:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-5 | 18:37:08 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Amumu18 | -0.0400 |  |
| Jogador 2 | 3-5 | 18:37:08 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Sejuani | 0.7700 |  |
| Jogador 2 | 3-5 | 18:37:08 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Sejuani | 0.4100 |  |
| Jogador 2 | 3-5 | 18:37:09 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | -0.0200 |  |
| Jogador 2 | 3-5 | 18:37:09 | MOVE Bench -> Board: Zyra (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | -0.6400 |  |
| Jogador 2 | 3-5 | 18:37:09 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | -0.3600 |  |
| Jogador 2 | 3-5 | 18:37:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 3-5 | 18:37:13 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | 0.5900 |  |
| Jogador 2 | 3-6 | 18:37:16 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Sejuani | 0.5500 |  |
| Jogador 2 | 3-6 | 18:37:17 | MOVE Bench -> Board: Lillia (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Sejuani | -0.0600 |  |
| Jogador 2 | 3-6 | 18:37:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Sejuani | -0.0100 |  |
| Jogador 2 | 3-6 | 18:37:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 3-7 | 18:37:25 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Sejuani | 0.3100 |  |
| Jogador 2 | 3-7 | 18:37:25 | VENDEU: Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Sejuani | 0.0700 |  |
| Jogador 2 | 3-7 | 18:37:25 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Sejuani | -0.3500 |  |
| Jogador 2 | 3-7 | 18:37:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Sejuani | -0.0100 |  |
| Jogador 2 | 3-7 | 18:37:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-1 | 18:37:34 | VENDEU: Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Sejuani | 0.1000 |  |
| Jogador 2 | 4-1 | 18:37:34 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_18_Sejuani | 0.7800 |  |
| Jogador 2 | 4-1 | 18:37:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Sejuani | -0.0900 |  |
| Jogador 2 | 4-1 | 18:37:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Sejuani | -0.0100 |  |
| Jogador 2 | 4-1 | 18:37:35 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Sejuani | -0.0100 |  |
| Jogador 2 | 4-1 | 18:37:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-2 | 18:37:43 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Sejuani | -0.0100 |  |
| Jogador 2 | 4-2 | 18:37:43 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-3 | 18:37:53 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_Sejuani | 0.4100 |  |
| Jogador 2 | 4-3 | 18:37:53 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Sejuani | -0.1100 |  |
| Jogador 2 | 4-3 | 18:37:53 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-3 | 18:37:58 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Sejuani | 0.5500 |  |
| Jogador 2 | 4-4 | 18:38:02 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Colosso | DA_18_Sejuani | -0.0200 |  |
| Jogador 2 | 4-4 | 18:38:03 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Sejuani | 0.2100 |  |
| Jogador 2 | 4-4 | 18:38:03 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-5 | 18:38:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_Sejuani | 0.7700 |  |
| Jogador 2 | 4-5 | 18:38:11 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_Sejuani | -0.5600 |  |
| Jogador 2 | 4-5 | 18:38:11 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_Sejuani | 0.2900 |  |
| Jogador 2 | 4-5 | 18:38:12 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Colosso | DA_18_Sejuani | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 4-5 | 18:38:12 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-5 | 18:38:16 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Colosso | DA_18_Sejuani | 0.6600 |  |
| Jogador 2 | 4-6 | 18:38:19 | COMPROU: Shen (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Colosso | DA_18_Sejuani | 0.1600 |  |
| Jogador 2 | 4-6 | 18:38:22 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Colosso | DA_18_Sejuani | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 4-6 | 18:38:22 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 3 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-7 | 18:38:28 | BIGORNA: escolheu componente TFT_Item_TearOfTheGoddess | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-7 | 18:38:29 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Lillia (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Colosso | DA_18_Sejuani | 0.0200 |  |
| Jogador 2 | 4-7 | 18:38:29 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_Lux_Sunbeam | 0.0400 |  |
| Jogador 2 | 4-7 | 18:38:29 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_18_Lux_Sunbeam | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 4-7 | 18:38:29 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-1 | 18:38:37 | COMPROU: Amumu (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Colosso | DA_18_Lux_Sunbeam | 0.7800 |  |
| Jogador 2 | 5-1 | 18:38:37 | COMPROU: Hecarim (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_18_Lux_Sunbeam | -0.2300 |  |
| Jogador 2 | 5-1 | 18:38:37 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-2 | 18:38:46 | COMPROU: Sejuani (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_18_Sejuani | 0.2700 |  |
| Jogador 2 | 5-2 | 18:38:46 | COMPROU: Ahri (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_18_Sejuani | 0.5000 |  |
| Jogador 2 | 5-2 | 18:38:49 | VENDEU: Cassiopeia (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Colosso | DA_18_Sejuani | 0.0700 |  |
| Jogador 2 | 5-2 | 18:38:49 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_18_Sejuani | 0.0900 |  |
| Jogador 2 | 5-2 | 18:38:49 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 5-3 | 18:38:56 | VENDEU: Shen (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Colosso | DA_18_Sejuani | 0.1000 |  |
| Jogador 2 | 5-3 | 18:38:56 | COMPROU: Alune (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_18_Alune | 0.1200 |  |
| Jogador 2 | 5-3 | 18:38:56 | VENDEU: Rakan (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Colosso | DA_18_Alune | -0.4600 |  |
| Jogador 2 | 5-3 | 18:38:56 | COMPROU: Master Yi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_18_Alune | 0.7600 |  |
| Jogador 2 | 5-3 | 18:38:56 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Amumu (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_18_Alune | -0.4500 |  |
| Jogador 2 | 5-3 | 18:38:57 | MOVE Bench -> Board: Amumu (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_18_Alune | 0.4400 |  |
| Jogador 2 | 5-3 | 18:38:57 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Colosso | DA_18_Alune | 0.1500 |  |
| Jogador 2 | 5-3 | 18:38:57 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Colosso | DA_18_Alune | 0.4500 |  |
| Jogador 2 | 5-3 | 18:38:57 | COMPROU: Yorick (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_18_Alune | 0.2700 |  |
| Jogador 2 | 5-3 | 18:39:00 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_18_Alune | 0.0000 |  |
| Jogador 2 | 5-4 | 18:39:05 | VENDEU: Ahri (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 0 | Colosso | DA_18_Alune | -0.2500 |  |
| Jogador 2 | 5-4 | 18:39:05 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Colosso | DA_18_Alune | 0.7600 |  |
| Jogador 2 | 5-4 | 18:39:05 | VENDEU: Master Yi (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 0 | Colosso | DA_18_Alune | -0.3400 |  |
| Jogador 2 | 5-4 | 18:39:05 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 15 | 0 | Colosso | DA_CrimsonRaptor18 | 0.8100 |  |
| Jogador 2 | 5-4 | 18:39:05 | COMPROU: Zyra (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Colosso | DA_CrimsonRaptor18 | -0.0600 |  |
| Jogador 2 | 5-4 | 18:39:06 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Colosso | DA_CrimsonRaptor18 | -0.0700 |  |
| Jogador 2 | 5-4 | 18:39:06 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 2 | 5-5 | 18:39:13 | VENDEU: Kog'Maw (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 0 | Colosso | DA_CrimsonRaptor18 | 0.0400 |  |
| Jogador 2 | 5-5 | 18:39:14 | COMPROU: Ahri (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Colosso | DA_CrimsonRaptor18 | 0.5300 |  |
| Jogador 2 | 5-5 | 18:39:17 | VENDEU: Zyra (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 0 | Colosso | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 2 | 5-5 | 18:39:17 | COMPROU: Malphite (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Colosso | DA_CrimsonRaptor18 | -0.0600 |  |
| Jogador 2 | 5-5 | 18:39:17 | VENDEU: Malphite (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 0 | Colosso | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 2 | 5-5 | 18:39:17 | COMPROU: Rengar (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 15 | 0 | Colosso | DA_CrimsonRaptor18 | -0.1500 |  |
| Jogador 2 | 5-5 | 18:39:17 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 15 | 0 | Colosso | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 2 | 5-6 | 18:39:25 | VENDEU: Rengar (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 28 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 2 | 5-6 | 18:39:25 | COMPROU: Lux (Lunar) (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 23 | 1 | Colosso | DA_CrimsonRaptor18 | 0.1800 |  |
| Jogador 2 | 5-6 | 18:39:26 | VENDEU: Ahri (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 1 | Colosso | DA_CrimsonRaptor18 | -0.3200 |  |
| Jogador 2 | 5-6 | 18:39:26 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 23 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 2 | 5-6 | 18:39:26 | VENDEU: Rubrivira (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 2 | 5-6 | 18:39:26 | COMPROU: Rammus (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 24 | 1 | Colosso | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 2 | 5-6 | 18:39:26 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Colosso | DA_CrimsonRaptor18 | -0.1600 |  |
| Jogador 2 | 5-6 | 18:39:26 | VENDEU: Rammus (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 2 | 5-6 | 18:39:27 | COMPROU: Hecarim (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 1 | Colosso | DA_CrimsonRaptor18 | 0.3800 |  |
| Jogador 2 | 5-6 | 18:39:30 | VENDEU: Hecarim (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Colosso | DA_CrimsonRaptor18 | -0.3000 |  |
| Jogador 2 | 5-6 | 18:39:30 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Colosso | DA_CrimsonRaptor18 | -0.1200 |  |
| Jogador 2 | 5-7 | 18:39:34 | BIGORNA: escolheu item completo TFT_Item_IonicSpark | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 2 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 2 | 5-7 | 18:39:34 | COMPROU: Sett (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 31 | 2 | Colosso | DA_CrimsonRaptor18 | -0.1600 |  |
| Jogador 2 | 5-7 | 18:39:34 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Lillia (i:8.0) (tabuleiro slot 10) | WINSTREAK | WINSTREAK: preservar vantagem atual | 31 | 2 | Colosso | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 2 | 5-7 | 18:39:34 | VENDEU: Sett (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 2 | Colosso | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 2 | 5-7 | 18:39:37 | COMPROU: Shen (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 33 | 2 | Colosso | DA_CrimsonRaptor18 | 0.2200 |  |
| Jogador 2 | 5-7 | 18:39:37 | VENDEU: Shen (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 2 | Colosso | DA_CrimsonRaptor18 | 0.0200 |  |
| Jogador 2 | 5-7 | 18:39:38 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 33 | 2 | Colosso | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 2 | 5-7 | 18:39:38 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 31 | 2 | Colosso | DA_CrimsonRaptor18 | -0.1600 |  |
| Jogador 2 | 5-7 | 18:39:38 | VENDEU: LeBlanc (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 33 | 2 | Colosso | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 2 | 5-7 | 18:39:38 | COMPROU: Ahri (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 2 | Colosso | DA_CrimsonRaptor18 | 0.4500 |  |
| Jogador 2 | 5-7 | 18:39:38 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 2 | Colosso | DA_CrimsonRaptor18 | -0.0400 |  |
| Jogador 2 | 6-1 | 18:39:45 | VENDEU: Ahri (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Colosso | DA_CrimsonRaptor18 | -0.3200 |  |
| Jogador 2 | 6-1 | 18:39:45 | COMPROU: Lux (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 40 | 3 | Colosso | DA_CrimsonRaptor18 | -0.1300 |  |
| Jogador 2 | 6-1 | 18:39:45 | VENDEU: Lux (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Colosso | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 2 | 6-1 | 18:39:45 | COMPROU: Aphelios (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Colosso | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 2 | 6-1 | 18:39:46 | VENDEU: Aphelios (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Colosso | DA_CrimsonRaptor18 | 0.0400 |  |
| Jogador 2 | 6-1 | 18:39:46 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Colosso | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 2 | 6-1 | 18:39:46 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 39 | 3 | Colosso | DA_CrimsonRaptor18 | -0.2400 |  |
| Jogador 2 | 6-1 | 18:39:46 | VENDEU: Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 3 | Colosso | DA_CrimsonRaptor18 | 0.1300 |  |
| Jogador 2 | 6-1 | 18:39:46 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 40 | 3 | Colosso | DA_CrimsonRaptor18 | 0.8400 |  |
| Jogador 2 | 6-1 | 18:39:50 | VENDEU: Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 3 | Colosso | DA_CrimsonRaptor18 | -0.3900 |  |
| Jogador 2 | 6-1 | 18:39:50 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 3 | Colosso | DA_CrimsonRaptor18 | -0.2200 |  |
| Jogador 2 | 6-2 | 18:39:54 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 52 | 4 | Colosso | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 2 | 6-2 | 18:39:54 | VENDEU: Rubrivira (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 56 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0400 |  |
| Jogador 2 | 6-2 | 18:39:54 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 52 | 4 | Colosso | DA_CrimsonRaptor18 | 0.1100 |  |
| Jogador 2 | 6-2 | 18:39:58 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 50 | 4 | Colosso | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 2 | 6-2 | 18:39:58 | VENDEU: Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 54 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0400 |  |
| Jogador 2 | 6-2 | 18:39:58 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 50 | 4 | Colosso | DA_CrimsonRaptor18 | 0.1100 |  |
| Jogador 2 | 6-2 | 18:39:58 | VENDEU: Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 54 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0400 |  |
| Jogador 2 | 6-2 | 18:39:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 53 | 4 | Colosso | DA_CrimsonRaptor18 | 0.3500 |  |
| Jogador 2 | 6-2 | 18:39:59 | VENDEU: Lux (Solar) (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 58 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0400 |  |
| Jogador 2 | 6-2 | 18:39:59 | COMPROU: Xayah (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 57 | 4 | Colosso | DA_CrimsonRaptor18 | 0.8700 |  |
| Jogador 2 | 6-2 | 18:39:59 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 57 | 4 | Colosso | DA_CrimsonRaptor18 | -0.1000 |  |
| Jogador 2 | 6-3 | 18:40:06 | VENDEU: Lux (Lunar) (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 76 | 5 | Colosso | DA_CrimsonRaptor18 | 0.0200 |  |
| Jogador 2 | 6-3 | 18:40:06 | COMPROU: Lillia (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 72 | 5 | Colosso | DA_18_Lillia | 1.0200 |  |
| Jogador 2 | 6-3 | 18:40:06 | VENDEU: Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 73 | 5 | Colosso | DA_18_Lillia | -0.4100 |  |
| Jogador 2 | 6-3 | 18:40:06 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 70 | 5 | Colosso | DA_18_Lillia | 0.7400 |  |
| Jogador 2 | 6-3 | 18:40:06 | MOVE Bench -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 70 | 5 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 6-3 | 18:40:07 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Amumu (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 70 | 5 | Colosso | DA_18_Lillia | -0.4500 |  |
| Jogador 2 | 6-3 | 18:40:07 | MOVE Bench -> Board: Amumu (i:8.0) <-> Diana (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 70 | 5 | Colosso | DA_18_Lillia | 0.2000 |  |
| Jogador 2 | 6-3 | 18:40:07 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 70 | 5 | Colosso | DA_18_Lillia | -0.0800 |  |
| Jogador 2 | 6-3 | 18:40:07 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 66 | 5 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 6-3 | 18:40:11 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 64 | 5 | Colosso | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 6-3 | 18:40:11 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 64 | 5 | Colosso | DA_18_Lillia | -0.1100 |  |
| Jogador 2 | 6-4 | 18:40:15 | VENDEU: Rubrivira (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 81 | 5 | Colosso | DA_18_Lillia | 0.0600 |  |
| Jogador 2 | 6-4 | 18:40:15 | COMPROU: Sejuani (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 79 | 5 | Colosso | DA_18_Lillia | 0.9500 |  |
| Jogador 2 | 6-4 | 18:40:19 | VENDEU: Mamãe Bicuda (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 87 | 5 | Colosso | DA_18_Lillia | -0.4300 |  |
| Jogador 2 | 6-4 | 18:40:19 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 84 | 5 | Colosso | DA_18_Lillia | 0.7600 |  |
| Jogador 2 | 6-4 | 18:40:19 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 82 | 5 | Colosso | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 6-4 | 18:40:20 | VENDEU: Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 85 | 5 | Colosso | DA_18_Lillia | -0.3900 |  |
| Jogador 2 | 6-4 | 18:40:20 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 82 | 5 | Colosso | DA_18_Lillia | 1.0500 |  |
| Jogador 2 | 6-4 | 18:40:20 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Amumu (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Colosso | DA_18_Lillia | -0.6300 |  |
| Jogador 2 | 6-4 | 18:40:20 | MOVE Bench -> Board: Alune (i:10.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 82 | 5 | Colosso | DA_18_Lillia | 0.2100 |  |
| Jogador 2 | 6-4 | 18:40:21 | COMPROU: Shen (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 80 | 5 | Colosso | DA_18_Lillia | 0.0400 |  |
| Jogador 2 | 6-4 | 18:40:21 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 80 | 5 | Colosso | DA_18_Lillia | -0.1200 |  |
| Jogador 2 | 6-5 | 18:40:28 | VENDEU: Shen (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 92 | 5 | Colosso | DA_18_Lillia | 0.0400 |  |
| Jogador 2 | 6-5 | 18:40:28 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 90 | 5 | Colosso | DA_18_Lillia | 1.0500 |  |
| Jogador 2 | 6-5 | 18:40:28 | MOVE Bench -> Board: Amumu (i:8.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 90 | 5 | Colosso | DA_18_Lillia | 0.5800 |  |
| Jogador 2 | 6-5 | 18:40:28 | COMPROU: Sett (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 86 | 5 | Colosso | DA_18_Lillia | -0.0400 |  |
| Jogador 2 | 6-5 | 18:40:29 | COMPROU: Elise (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Colosso | DA_18_Lillia | 0.0500 |  |
| Jogador 2 | 6-5 | 18:40:29 | MOVE Bench -> Board: Sett (i:8.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Colosso | DA_18_Lillia | 0.1300 |  |
| Jogador 2 | 6-5 | 18:40:29 | COMPROU: Yunara (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 82 | 5 | Colosso | DA_18_Lillia | 0.0500 |  |
| Jogador 2 | 6-5 | 18:40:29 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 80 | 5 | Colosso | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 6-5 | 18:40:30 | VENDEU: Yunara (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 82 | 5 | Colosso | DA_18_Lillia | 0.0400 |  |
| Jogador 2 | 6-5 | 18:40:33 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 80 | 5 | Colosso | DA_18_Lillia | 0.9100 |  |
| Jogador 2 | 6-5 | 18:40:33 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 80 | 5 | Colosso | DA_18_Lillia | -0.1300 |  |
| Jogador 3 | ? | 18:35:17 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 3 | ? | 18:35:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 18:35:23 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 18:35:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.3400 |  |
| Jogador 3 | 1-1 | 18:35:24 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.2100 |  |
| Jogador 3 | 1-1 | 18:35:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 3 | 1-1 | 18:35:25 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5500 |  |
| Jogador 3 | 1-1 | 18:35:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 1-2 | 18:35:29 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 18:35:30 | MOVE Bench -> Board: Akali (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 1-2 | 18:35:30 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.5500 |  |
| Jogador 3 | 1-2 | 18:35:30 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.3200 |  |
| Jogador 3 | 1-2 | 18:35:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 18:35:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 1-3 | 18:35:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0400 |  |
| Jogador 3 | 1-3 | 18:35:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4700 |  |
| Jogador 3 | 1-3 | 18:35:37 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 1-3 | 18:35:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 18:35:42 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3200 |  |
| Jogador 3 | 1-4 | 18:35:43 | MOVE Bench -> Board: Shen (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Shen | 0.1900 |  |
| Jogador 3 | 1-4 | 18:35:43 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Shen | -0.0100 |  |
| Jogador 3 | 1-4 | 18:35:43 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Shen | 0.1800 |  |
| Jogador 3 | 1-4 | 18:35:44 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Shen | -0.0200 |  |
| Jogador 3 | 1-4 | 18:35:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Shen | 0.0000 |  |
| Jogador 3 | 2-1 | 18:35:49 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Shen | -0.0400 |  |
| Jogador 3 | 2-1 | 18:35:49 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 1.0100 |  |
| Jogador 3 | 2-1 | 18:35:50 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | -0.6300 |  |
| Jogador 3 | 2-1 | 18:35:50 | MOVE Bench -> Board: Shen (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | -0.2700 |  |
| Jogador 3 | 2-1 | 18:35:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-2 | 18:35:56 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 2-2 | 18:35:56 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 2-2 | 18:35:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Scuttlecrab18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-3 | 18:36:02 | MOVE Bench -> Board: Shen (i:4.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | — | DA_Scuttlecrab18 | -0.2900 |  |
| Jogador 3 | 2-3 | 18:36:03 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 18 | 1 | — | DA_Scuttlecrab18 | 0.4900 |  |
| Jogador 3 | 2-3 | 18:36:03 | COMPROU: Rengar (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 15 | 1 | — | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 2-3 | 18:36:03 | MOVE Bench -> Board: Rengar (i:6.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 15 | 1 | — | DA_Scuttlecrab18 | -0.5800 |  |
| Jogador 3 | 2-3 | 18:36:04 | MOVE Bench -> Board: Shen (i:4.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 15 | 1 | — | DA_Scuttlecrab18 | -0.3200 |  |
| Jogador 3 | 2-3 | 18:36:04 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 15 | 1 | — | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-4 | 18:36:09 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 1 | Inferno | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 2-4 | 18:36:09 | MOVE Bench -> Board: Rengar (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 1 | Inferno | DA_18_Rengar | -0.2600 |  |
| Jogador 3 | 2-4 | 18:36:10 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 1 | Inferno | DA_18_Rengar | -0.4000 |  |
| Jogador 3 | 2-4 | 18:36:10 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 1 | Inferno | DA_18_Rengar | -0.0200 |  |
| Jogador 3 | 2-5 | 18:36:16 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Inferno | DA_Scuttlecrab18 | -0.3400 |  |
| Jogador 3 | 2-5 | 18:36:17 | MOVE Bench -> Board: Rengar (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Inferno | DA_Scuttlecrab18 | -0.2600 |  |
| Jogador 3 | 2-5 | 18:36:17 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Inferno | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 2-6 | 18:36:23 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 3 | Inferno | DA_Scuttlecrab18 | -0.7400 |  |
| Jogador 3 | 2-6 | 18:36:23 | MOVE Bench -> Board: Shen (i:4.0) <-> Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 3 | Inferno | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 2-6 | 18:36:24 | MOVE Bench -> Board: Rengar (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 3 | Inferno | DA_18_Rengar | -0.2600 |  |
| Jogador 3 | 2-6 | 18:36:24 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 3 | Inferno | DA_18_Rengar | -0.8200 |  |
| Jogador 3 | 2-6 | 18:36:24 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 3 | Inferno | DA_18_Rengar | -0.0400 |  |
| Jogador 3 | 2-7 | 18:36:31 | MOVE Bench -> Board: Shen (i:4.0) <-> Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 46 | 3 | Inferno | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 2-7 | 18:36:31 | MOVE Bench -> Board: Rengar (i:6.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 46 | 3 | Inferno | DA_18_Rengar | -0.2100 |  |
| Jogador 3 | 2-7 | 18:36:31 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 46 | 3 | Inferno | DA_18_Rengar | -0.4000 |  |
| Jogador 3 | 2-7 | 18:36:32 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 46 | 3 | Inferno | DA_18_Rengar | -0.1100 |  |
| Jogador 3 | 3-1 | 18:36:38 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rengar (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 4 | Inferno | DA_Scuttlecrab18 | -0.7400 |  |
| Jogador 3 | 3-1 | 18:36:38 | MOVE Bench -> Board: Rengar (i:6.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 4 | Inferno | DA_18_Rengar | -0.6300 |  |
| Jogador 3 | 3-1 | 18:36:39 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 4 | Inferno | DA_18_Rengar | -0.1200 |  |
| Jogador 3 | 3-2 | 18:36:45 | MOVE Bench -> Board: Shen (i:4.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 68 | 5 | Inferno | DA_18_Rengar | 0.1600 |  |
| Jogador 3 | 3-2 | 18:36:45 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 68 | 5 | Inferno | DA_18_Rengar | -0.3700 |  |
| Jogador 3 | 3-2 | 18:36:47 | MOVE Bench -> Board: Akali (i:2.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 68 | 5 | Inferno | DA_18_Rengar | -0.0700 |  |
| Jogador 3 | 3-2 | 18:36:47 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 68 | 5 | Inferno | DA_18_Rengar | -0.1300 |  |
| Jogador 3 | 3-3 | 18:36:52 | MOVE Bench -> Board: Shen (i:4.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 78 | 5 | Inferno | DA_18_Rengar | 0.1700 |  |
| Jogador 3 | 3-3 | 18:36:53 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 78 | 5 | Inferno | DA_18_Rengar | -0.3500 |  |
| Jogador 3 | 3-3 | 18:36:53 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 74 | 5 | Inferno | DA_18_Rengar | 0.0000 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-3 | 18:36:53 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 70 | 5 | Inferno | DA_18_Rengar | 0.3400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-3 | 18:36:53 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 70 | 5 | Inferno | DA_18_Rengar | 0.5100 |  |
| Jogador 3 | 3-3 | 18:36:54 | COMPROU: Alistar (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 68 | 5 | Inferno | DA_18_Rengar | -0.2800 |  |
| Jogador 3 | 3-3 | 18:36:54 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 64 | 5 | Inferno | DA_18_Rengar | 0.0000 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-3 | 18:36:54 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 60 | 5 | Inferno | DA_18_Rengar | 0.0000 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-3 | 18:36:55 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 5 | Inferno | DA_18_Rengar | 0.0000 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-3 | 18:36:55 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 5 | Inferno | DA_18_Rengar | 0.0000 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-3 | 18:36:56 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 5 | Inferno | DA_18_Rengar | -0.1200 |  |
| Jogador 3 | 3-4 | 18:37:00 | MOVE Bench -> Board: Alistar (i:4.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Rengar | -0.3500 |  |
| Jogador 3 | 3-4 | 18:37:00 | MOVE Bench -> Board: Akali (i:2.0) <-> Aronguejo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_18_Rengar | 0.0600 |  |
| Jogador 3 | 3-4 | 18:37:01 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Alistar (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-4 | 18:37:01 | MOVE Bench -> Board: Alistar (i:4.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_Scuttlecrab18 | -0.3100 |  |
| Jogador 3 | 3-4 | 18:37:01 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Inferno | DA_Scuttlecrab18 | -0.1300 |  |
| Jogador 3 | 3-5 | 18:37:08 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 71 | 5 | Inferno | DA_Scuttlecrab18 | 0.9300 |  |
| Jogador 3 | 3-5 | 18:37:08 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 71 | 5 | Inferno | DA_Scuttlecrab18 | 0.1600 |  |
| Jogador 3 | 3-5 | 18:37:08 | MOVE Bench -> Board: Akali (i:2.0) <-> Aronguejo (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 71 | 5 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-5 | 18:37:09 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Alistar (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 71 | 5 | Inferno | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 3-5 | 18:37:09 | MOVE Bench -> Board: Alistar (i:4.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 71 | 5 | Inferno | DA_Scuttlecrab18 | -0.3400 |  |
| Jogador 3 | 3-5 | 18:37:09 | MOVE Bench -> Board: Akali (i:2.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 71 | 5 | Inferno | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 3-5 | 18:37:10 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 71 | 5 | Inferno | DA_Scuttlecrab18 | -0.1300 |  |
| Jogador 3 | 3-5 | 18:37:13 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Inferno | DA_Scuttlecrab18 | 0.5000 |  |
| Jogador 3 | 3-6 | 18:37:16 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 80 | 5 | Inferno | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 3-6 | 18:37:17 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 80 | 5 | Inferno | DA_Scuttlecrab18 | 0.1200 |  |
| Jogador 3 | 3-6 | 18:37:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 3-6 | 18:37:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 3-6 | 18:37:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Inferno | DA_Scuttlecrab18 | 0.3100 |  |
| Jogador 3 | 3-6 | 18:37:18 | MOVE Bench -> Board: Alistar (i:4.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Inferno | DA_Scuttlecrab18 | -0.3200 |  |
| Jogador 3 | 3-6 | 18:37:18 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 3-6 | 18:37:18 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 3-6 | 18:37:18 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 3-6 | 18:37:20 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 5 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 3-6 | 18:37:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 5 | Inferno | DA_Scuttlecrab18 | -0.1500 |  |
| Jogador 3 | 3-7 | 18:37:25 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Inferno | DA_Scuttlecrab18 | 0.6100 |  |
| Jogador 3 | 3-7 | 18:37:25 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Inferno | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 3-7 | 18:37:25 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 3-7 | 18:37:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 5 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 3-7 | 18:37:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 5 | Inferno | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 3 | 3-7 | 18:37:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 5 | Inferno | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 3-7 | 18:37:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 5 | Inferno | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 3-7 | 18:37:27 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 5 | Inferno | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 3-7 | 18:37:27 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 5 | Inferno | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 3-7 | 18:37:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 5 | Inferno | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 3-7 | 18:37:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 5 | Inferno | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 4-1 | 18:37:34 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Inferno | DA_Scuttlecrab18 | 0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 4-1 | 18:37:34 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Inferno | DA_Scuttlecrab18 | -0.7900 |  |
| Jogador 3 | 4-1 | 18:37:34 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Inferno | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 3 | 4-1 | 18:37:34 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Inferno | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 4-1 | 18:37:35 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Inferno | DA_Scuttlecrab18 | -0.7900 |  |
| Jogador 3 | 4-1 | 18:37:35 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Inferno | DA_Scuttlecrab18 | -0.1500 |  |
| Jogador 3 | 4-1 | 18:37:39 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Inferno | DA_Scuttlecrab18 | 0.2900 |  |
| Jogador 3 | 4-2 | 18:37:43 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-2 | 18:37:43 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 3 | 4-2 | 18:37:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 4-2 | 18:37:44 | MOVE Bench -> Board: Alistar (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | -0.7000 |  |
| Jogador 3 | 4-2 | 18:37:44 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 3 | 4-2 | 18:37:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 4-2 | 18:37:45 | MOVE Bench -> Board: Alistar (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | -0.7000 |  |
| Jogador 3 | 4-2 | 18:37:45 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 3 | 4-2 | 18:37:45 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 4-2 | 18:37:47 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | -0.7900 |  |
| Jogador 3 | 4-2 | 18:37:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Scuttlecrab18 | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-3 | 18:37:53 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Inferno | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 4-3 | 18:37:53 | MOVE Bench -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Inferno | DA_Scuttlecrab18 | -0.2100 |  |
| Jogador 3 | 4-3 | 18:37:53 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Inferno | DA_Scuttlecrab18 | -0.7900 |  |
| Jogador 3 | 4-3 | 18:37:53 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Inferno | DA_Scuttlecrab18 | -0.1900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-3 | 18:37:58 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Inferno | DA_Scuttlecrab18 | 0.4200 |  |
| Jogador 3 | 4-4 | 18:38:02 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 4 | Inferno | DA_Scuttlecrab18 | 0.1600 |  |
| Jogador 3 | 4-4 | 18:38:03 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 4 | Inferno | DA_Scuttlecrab18 | -0.1500 |  |
| Jogador 3 | 4-4 | 18:38:03 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 43 | 4 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-4 | 18:38:03 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 39 | 4 | Inferno | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-4 | 18:38:03 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 35 | 4 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-4 | 18:38:04 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 31 | 4 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-4 | 18:38:04 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 27 | 4 | Inferno | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-4 | 18:38:04 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 23 | 4 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-4 | 18:38:05 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 19 | 4 | Inferno | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-4 | 18:38:07 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 15 | 4 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-4 | 18:38:07 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 15 | 4 | Inferno | DA_Scuttlecrab18 | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-5 | 18:38:11 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Inferno | DA_Scuttlecrab18 | -0.0500 |  |
| Jogador 3 | 4-5 | 18:38:11 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-5 | 18:38:11 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-5 | 18:38:12 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 6 | 1 | Inferno | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-5 | 18:38:12 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 1 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-5 | 18:38:12 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 1 | Inferno | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-6 | 18:38:19 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Inferno | DA_Scuttlecrab18 | 0.3000 |  |
| Jogador 3 | 4-6 | 18:38:22 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Inferno | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-6 | 18:38:22 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Inferno | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-7 | 18:38:28 | BIGORNA: escolheu componente TFT_Item_SparringGloves | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Inferno | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-7 | 18:38:29 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Inferno | DA_Scuttlecrab18 | 0.1200 |  |
| Jogador 3 | 4-7 | 18:38:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Inferno | DA_Scuttlecrab18 | 0.3900 |  |
| Jogador 3 | 4-7 | 18:38:29 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Inferno | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 4-7 | 18:38:29 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_Scuttlecrab18 | 0.2900 |  |
| Jogador 3 | 4-7 | 18:38:30 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_Scuttlecrab18 | 0.8100 |  |
| Jogador 3 | 4-7 | 18:38:30 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-1 | 18:38:37 | COMPROU: Lux (Lunar) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Inferno | DA_18_Lux_Moonbeam | -0.1000 |  |
| Jogador 3 | 5-1 | 18:38:37 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_18_Lux_Moonbeam | 0.0500 |  |
| Jogador 3 | 5-1 | 18:38:37 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_18_Lux_Moonbeam | 0.0000 |  |
| Jogador 3 | 5-2 | 18:38:46 | COMPROU: Lux (Lunar) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Inferno | DA_18_Lux_Moonbeam | 0.7300 |  |
| Jogador 3 | 5-2 | 18:38:46 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Inferno | DA_18_Lux_Moonbeam | -0.0500 |  |
| Jogador 4 | ? | 18:35:17 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6000 |  |
| Jogador 4 | ? | 18:35:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 18:35:23 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 18:35:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.3400 |  |
| Jogador 4 | 1-1 | 18:35:24 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.2100 |  |
| Jogador 4 | 1-1 | 18:35:24 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.1000 |  |
| Jogador 4 | 1-1 | 18:35:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 18:35:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.0600 |  |
| Jogador 4 | 1-2 | 18:35:30 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | -1.0500 |  |
| Jogador 4 | 1-2 | 18:35:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.7800 |  |
| Jogador 4 | 1-2 | 18:35:30 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | -0.2600 |  |
| Jogador 4 | 1-2 | 18:35:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | -0.1000 |  |
| Jogador 4 | 1-2 | 18:35:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 1-3 | 18:35:36 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Gromp18_AP | 0.0800 |  |
| Jogador 4 | 1-3 | 18:35:36 | MOVE Bench -> Board: Teemo (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Teemo | -0.5600 |  |
| Jogador 4 | 1-3 | 18:35:36 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Teemo | -1.0100 |  |
| Jogador 4 | 1-3 | 18:35:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Teemo | 0.0000 |  |
| Jogador 4 | 1-4 | 18:35:42 | MOVE Bench -> Board: Rakan (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Gromp18_AP | 0.3000 |  |
| Jogador 4 | 1-4 | 18:35:43 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Teemo | 0.3000 |  |
| Jogador 4 | 1-4 | 18:35:43 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 1.0200 |  |
| Jogador 4 | 1-4 | 18:35:43 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | -1.0200 |  |
| Jogador 4 | 1-4 | 18:35:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 0.3000 |  |
| Jogador 4 | 1-4 | 18:35:44 | MOVE Bench -> Board: Teemo (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | -0.1900 |  |
| Jogador 4 | 1-4 | 18:35:44 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | -1.0300 |  |
| Jogador 4 | 1-4 | 18:35:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-1 | 18:35:49 | MOVE Bench -> Board: Rakan (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Gromp18_AP | 0.3000 |  |
| Jogador 4 | 2-1 | 18:35:49 | MOVE Bench -> Board: Teemo (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Gromp18_AP | -0.3500 |  |
| Jogador 4 | 2-1 | 18:35:50 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Gromp18_AP | -1.0200 |  |
| Jogador 4 | 2-1 | 18:35:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-2 | 18:35:56 | MOVE Bench -> Board: Rakan (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_Gromp18_AP | -0.1100 |  |
| Jogador 4 | 2-2 | 18:35:56 | MOVE Bench -> Board: Grompe (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_Gromp18_AP | -0.4000 |  |
| Jogador 4 | 2-2 | 18:35:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_Gromp18_AP | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-3 | 18:36:02 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rakan (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 22 | 1 | — | DA_Gromp18_AP | -1.0200 |  |
| Jogador 4 | 2-3 | 18:36:03 | MOVE Bench -> Board: Rakan (i:2.0) <-> Grompe (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 22 | 1 | — | DA_Gromp18_AP | -0.1100 |  |
| Jogador 4 | 2-3 | 18:36:03 | PASSOU TURNO | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 22 | 1 | — | DA_Gromp18_AP | -0.0200 |  |
| Jogador 4 | 2-4 | 18:36:09 | MOVE Bench -> Board: Grompe (i:4.0) <-> Teemo (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 30 | 2 | Colosso | DA_Gromp18_AP | 0.0300 |  |
| Jogador 4 | 2-4 | 18:36:09 | MOVE Bench -> Board: Teemo (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Gromp18_AP | -1.0500 |  |
| Jogador 4 | 2-4 | 18:36:10 | MOVE Bench -> Board: Rakan (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Gromp18_AP | -0.0400 |  |
| Jogador 4 | 2-4 | 18:36:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_Gromp18_AP | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-5 | 18:36:16 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Colosso | DA_Gromp18_AP | 0.3500 |  |
| Jogador 4 | 2-5 | 18:36:17 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 36 | 3 | Colosso | DA_CrimsonRaptor18 | 0.3200 |  |
| Jogador 4 | 2-5 | 18:36:17 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Grompe (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 36 | 3 | Colosso | DA_CrimsonRaptor18 | -0.0800 |  |
| Jogador 4 | 2-5 | 18:36:17 | MOVE Bench -> Board: Grompe (i:4.0) <-> Teemo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 36 | 3 | Colosso | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 4 | 2-5 | 18:36:17 | MOVE Bench -> Board: Teemo (i:4.0) <-> Mamãe Bicuda (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 36 | 3 | Colosso | DA_CrimsonRaptor18 | -0.8200 |  |
| Jogador 4 | 2-5 | 18:36:18 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Grompe (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 36 | 3 | Colosso | DA_CrimsonRaptor18 | -0.0800 |  |
| Jogador 4 | 2-5 | 18:36:18 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 36 | 3 | Colosso | DA_CrimsonRaptor18 | -0.0400 |  |
| Jogador 4 | 2-6 | 18:36:23 | MOVE Bench -> Board: Grompe (i:4.0) <-> Teemo (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 46 | 3 | Colosso | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 4 | 2-6 | 18:36:23 | COMPROU: Master Yi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Fera do Rift | DA_CrimsonRaptor18 | 0.1700 |  |
| Jogador 4 | 2-6 | 18:36:24 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Grompe (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Fera do Rift | DA_CrimsonRaptor18 | -0.1500 |  |
| Jogador 4 | 2-6 | 18:36:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 42 | 3 | Fera do Rift | DA_CrimsonRaptor18 | 0.9700 |  |
| Jogador 4 | 2-6 | 18:36:24 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 38 | 3 | Fera do Rift | DA_CrimsonRaptor18 | -0.1400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-6 | 18:36:25 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 34 | 3 | Fera do Rift | DA_CrimsonRaptor18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-6 | 18:36:25 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 3 | Fera do Rift | DA_CrimsonRaptor18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-6 | 18:36:25 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 3 | Fera do Rift | DA_CrimsonRaptor18 | -0.1400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-6 | 18:36:26 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 3 | Fera do Rift | DA_CrimsonRaptor18 | 0.0500 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-6 | 18:36:26 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 3 | Fera do Rift | DA_CrimsonRaptor18 | 0.6100 |  |
| Jogador 4 | 2-6 | 18:36:26 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 3 | Fera do Rift | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 4 | 2-7 | 18:36:31 | COMPROU: Grompe (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Fera do Rift | DA_Gromp18_AP | 0.7400 |  |
| Jogador 4 | 2-7 | 18:36:31 | MOVE Bench -> Board: Grompe (i:8.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Fera do Rift | DA_Gromp18_AP | -0.0800 |  |
| Jogador 4 | 2-7 | 18:36:31 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Mamãe Bicuda (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Fera do Rift | DA_Gromp18_AP | -0.2700 |  |
| Jogador 4 | 2-7 | 18:36:32 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Fera do Rift | DA_Gromp18_AP | -0.0600 |  |
| Jogador 4 | 2-7 | 18:36:36 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 29 | 2 | Colosso | DA_Gromp18_AP | 0.0900 |  |
| Jogador 4 | 3-1 | 18:36:38 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Colosso | DA_Gromp18_AP | 0.2500 |  |
| Jogador 4 | 3-1 | 18:36:38 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Grompe (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Colosso | DA_Gromp18_AP | -0.3900 |  |
| Jogador 4 | 3-1 | 18:36:39 | MOVE Bench -> Board: Grompe (i:8.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Colosso | DA_Gromp18_AP | -0.1000 |  |
| Jogador 4 | 3-1 | 18:36:39 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 37 | 2 | Colosso | DA_Gromp18_AP | -0.1100 |  |
| Jogador 4 | 3-1 | 18:36:43 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Colosso | DA_Gromp18_AP | 0.7000 |  |
| Jogador 4 | 3-2 | 18:36:45 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_Gromp18_AP | 0.2600 |  |
| Jogador 4 | 3-2 | 18:36:45 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_Gromp18_AP | -0.2700 |  |
| Jogador 4 | 3-2 | 18:36:47 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Colosso | DA_Gromp18_AP | -0.1400 |  |
| Jogador 4 | 3-2 | 18:36:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Colosso | DA_Gromp18_AP | -0.0800 |  |
| Jogador 4 | 3-2 | 18:36:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 3 | Colosso | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-2 | 18:36:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 3 | Colosso | DA_Gromp18_AP | -0.0800 |  |
| Jogador 4 | 3-2 | 18:36:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 3 | Colosso | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-2 | 18:36:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 3 | Colosso | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-2 | 18:36:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 3 | Colosso | DA_Gromp18_AP | -0.0900 |  |
| Jogador 4 | 3-2 | 18:36:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 3 | Colosso | DA_Gromp18_AP | 0.0800 |  |
| Jogador 4 | 3-2 | 18:36:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 3 | Colosso | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-3 | 18:36:52 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Colosso | DA_Gromp18_AP | 0.7300 |  |
| Jogador 4 | 3-3 | 18:36:53 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Colosso | DA_Gromp18_AP | 0.7300 |  |
| Jogador 4 | 3-3 | 18:36:53 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Colosso | DA_Gromp18_AP | 0.6000 |  |
| Jogador 4 | 3-3 | 18:36:53 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Colosso | DA_Gromp18_AP | -0.1400 |  |
| Jogador 4 | 3-3 | 18:36:53 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Colosso | DA_Gromp18_AP | 0.1300 |  |
| Jogador 4 | 3-3 | 18:36:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 1 | Colosso | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-3 | 18:36:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-3 | 18:36:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-4 | 18:37:00 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.7600 |  |
| Jogador 4 | 3-4 | 18:37:00 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | 0.7600 |  |
| Jogador 4 | 3-4 | 18:37:01 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | 0.5500 |  |
| Jogador 4 | 3-4 | 18:37:01 | MOVE Board -> Board: Akali (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | -0.1000 |  |
| Jogador 4 | 3-4 | 18:37:01 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Vi18 | 0.0600 |  |
| Jogador 4 | 3-4 | 18:37:01 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.2200 |  |
| Jogador 4 | 3-4 | 18:37:02 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.5300 |  |
| Jogador 4 | 3-4 | 18:37:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 18:37:08 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_MasterYi_AD | 0.7300 |  |
| Jogador 4 | 3-5 | 18:37:08 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.7700 |  |
| Jogador 4 | 3-5 | 18:37:08 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.6900 |  |
| Jogador 4 | 3-5 | 18:37:09 | MOVE Bench -> Board: Elise (i:4.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_MasterYi_AD | -0.8300 |  |
| Jogador 4 | 3-5 | 18:37:09 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0500 |  |
| Jogador 4 | 3-5 | 18:37:09 | MOVE Bench -> Board: Yorick (i:2.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 3-5 | 18:37:10 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 18:37:10 | MOVE Bench -> Board: Elise (i:4.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.4500 |  |
| Jogador 4 | 3-5 | 18:37:10 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.1700 |  |
| Jogador 4 | 3-5 | 18:37:12 | MOVE Bench -> Board: Yorick (i:2.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 4 | 3-5 | 18:37:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 18:37:16 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.2800 |  |
| Jogador 4 | 3-6 | 18:37:17 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.8400 |  |
| Jogador 4 | 3-6 | 18:37:17 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.6100 |  |
| Jogador 4 | 3-6 | 18:37:17 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.2200 |  |
| Jogador 4 | 3-6 | 18:37:17 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.5700 |  |
| Jogador 4 | 3-6 | 18:37:18 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.6900 |  |
| Jogador 4 | 3-6 | 18:37:18 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 18:37:25 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.2700 |  |
| Jogador 4 | 3-7 | 18:37:25 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.1800 |  |
| Jogador 4 | 3-7 | 18:37:25 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 4 | 3-7 | 18:37:26 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.3700 |  |
| Jogador 4 | 3-7 | 18:37:26 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 3-7 | 18:37:26 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0200 |  |
| Jogador 4 | 3-7 | 18:37:26 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.4100 |  |
| Jogador 4 | 3-7 | 18:37:27 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 3-7 | 18:37:27 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.2500 |  |
| Jogador 4 | 3-7 | 18:37:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-1 | 18:37:34 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.1700 |  |
| Jogador 4 | 4-1 | 18:37:34 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-1 | 18:37:34 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 4 | 4-1 | 18:37:34 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.1500 |  |
| Jogador 4 | 4-1 | 18:37:35 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 4 | 4-1 | 18:37:35 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_MasterYi_AD | -0.5200 |  |
| Jogador 4 | 4-1 | 18:37:35 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.6200 |  |
| Jogador 4 | 4-1 | 18:37:36 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-1 | 18:37:36 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 4 | 4-1 | 18:37:38 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.2800 |  |
| Jogador 4 | 4-1 | 18:37:38 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 18:37:43 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 4 | 4-2 | 18:37:43 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_18_MasterYi_AD | 0.0200 |  |
| Jogador 4 | 4-2 | 18:37:44 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_MasterYi_AD | -0.1600 |  |
| Jogador 4 | 4-2 | 18:37:44 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-2 | 18:37:44 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 4 | 4-2 | 18:37:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.2800 |  |
| Jogador 4 | 4-2 | 18:37:45 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-2 | 18:37:45 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_MasterYi_AD | 0.0500 |  |
| Jogador 4 | 4-2 | 18:37:45 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | 0.8000 |  |
| Jogador 4 | 4-2 | 18:37:47 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_Vi18 | -0.0300 |  |
| Jogador 4 | 4-2 | 18:37:47 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 4 | 4-3 | 18:37:53 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_Vi18 | 0.7200 |  |
| Jogador 4 | 4-3 | 18:37:53 | REROLL | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 4 | 4-3 | 18:37:53 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_Vi18 | 0.0600 |  |
| Jogador 4 | 4-3 | 18:37:53 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.8000 |  |
| Jogador 4 | 4-3 | 18:37:53 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_MasterYi_AD | -0.3400 |  |
| Jogador 4 | 4-3 | 18:37:54 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.8300 |  |
| Jogador 4 | 4-3 | 18:37:54 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 4 | 4-3 | 18:37:54 | MOVE Bench -> Board: Grompe (i:8.0) <-> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_MasterYi_AD | -0.4700 |  |
| Jogador 4 | 4-3 | 18:37:54 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 4 | 4-3 | 18:37:56 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_MasterYi_AD | -0.2700 |  |
| Jogador 4 | 4-3 | 18:37:57 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 18:38:02 | MOVE Bench -> Board: Grompe (i:8.0) <-> Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_MasterYi_AD | -0.4500 |  |
| Jogador 4 | 4-4 | 18:38:03 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 4 | 4-4 | 18:38:03 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_MasterYi_AD | 0.5700 |  |
| Jogador 4 | 4-4 | 18:38:03 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 4 | 4-4 | 18:38:03 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-4 | 18:38:04 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0400 |  |
| Jogador 4 | 4-4 | 18:38:04 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Adaptador | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 4 | 4-4 | 18:38:04 | MOVE Board -> Board: Master Yi (i:12.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Adaptador | DA_CrimsonRaptor18 | -0.1200 |  |
| Jogador 4 | 4-4 | 18:38:05 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Adaptador | DA_CrimsonRaptor18 | -0.1200 |  |
| Jogador 4 | 4-4 | 18:38:07 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Adaptador | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 4-5 | 18:38:11 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Adaptador | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 4 | 4-5 | 18:38:11 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Adaptador | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 4 | 4-5 | 18:38:11 | REROLL | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Adaptador | DA_CrimsonRaptor18 | -0.1700 |  |
| Jogador 4 | 4-5 | 18:38:12 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Adaptador | DA_CrimsonRaptor18 | 0.1500 |  |
| Jogador 4 | 4-5 | 18:38:12 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Adaptador | DA_CrimsonRaptor18 | 0.7500 |  |
| Jogador 4 | 4-5 | 18:38:12 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Adaptador | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 4 | 4-5 | 18:38:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Adaptador | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 4 | 4-5 | 18:38:12 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Adaptador | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 4 | 4-5 | 18:38:13 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Adaptador | DA_18_MasterYi_AD | 0.2800 |  |
| Jogador 4 | 4-5 | 18:38:13 | MOVE Bench -> Board: Akali (i:2.0) <-> Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Adaptador | DA_18_MasterYi_AD | -0.1800 |  |
| Jogador 4 | 4-5 | 18:38:15 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-6 | 18:38:19 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Adaptador | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 4 | 4-6 | 18:38:22 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 9 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-6 | 18:38:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-6 | 18:38:22 | MOVE Bench -> Board: Grompe (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Adaptador | DA_18_MasterYi_AD | 0.6200 |  |
| Jogador 4 | 4-6 | 18:38:22 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Adaptador | DA_18_MasterYi_AD | 0.7500 |  |
| Jogador 4 | 4-6 | 18:38:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-6 | 18:38:23 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0500 |  |
| Jogador 4 | 4-6 | 18:38:23 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Adaptador | DA_18_MasterYi_AD | 0.8200 |  |
| Jogador 4 | 4-6 | 18:38:23 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 4 | 4-6 | 18:38:23 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_MasterYi_AD | -0.2600 |  |
| Jogador 4 | 4-6 | 18:38:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 4-7 | 18:38:28 | BIGORNA: escolheu componente TFT_Item_BFSword | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Adaptador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-7 | 18:38:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-7 | 18:38:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-7 | 18:38:29 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 4 | 4-7 | 18:38:29 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Adaptador | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 5 | ? | 18:35:17 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5700 |  |
| Jogador 5 | ? | 18:35:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 18:35:23 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0500 |  |
| Jogador 5 | 1-1 | 18:35:23 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.3700 |  |
| Jogador 5 | 1-1 | 18:35:24 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | -0.2400 |  |
| Jogador 5 | 1-1 | 18:35:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 1-2 | 18:35:29 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.2200 |  |
| Jogador 5 | 1-2 | 18:35:30 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.3200 |  |
| Jogador 5 | 1-2 | 18:35:30 | MOVE Board -> Board: Yunara (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.1400 |  |
| Jogador 5 | 1-2 | 18:35:30 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0600 |  |
| Jogador 5 | 1-2 | 18:35:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 1-3 | 18:35:36 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | 0.2400 |  |
| Jogador 5 | 1-3 | 18:35:36 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | -0.3000 |  |
| Jogador 5 | 1-3 | 18:35:36 | MOVE Bench -> Board: Elise (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | -0.2600 |  |
| Jogador 5 | 1-3 | 18:35:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 1-4 | 18:35:42 | MOVE Bench -> Board: Yunara (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yunara | -0.4500 |  |
| Jogador 5 | 1-4 | 18:35:43 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Sejuani | 0.6600 |  |
| Jogador 5 | 1-4 | 18:35:43 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 1-4 | 18:35:43 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | -0.5900 |  |
| Jogador 5 | 1-4 | 18:35:44 | MOVE Bench -> Board: Yunara (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | -0.5200 |  |
| Jogador 5 | 1-4 | 18:35:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 18:35:49 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-1 | 18:35:49 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Yunara | -0.3300 |  |
| Jogador 5 | 2-1 | 18:35:50 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | 0.2600 |  |
| Jogador 5 | 2-1 | 18:35:50 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | -0.2200 |  |
| Jogador 5 | 2-1 | 18:35:51 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | -0.2500 |  |
| Jogador 5 | 2-1 | 18:35:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-2 | 18:35:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 5 | 2-2 | 18:35:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_MasterYi_AD | 0.0500 |  |
| Jogador 5 | 2-2 | 18:35:56 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_MasterYi_AD | 0.3200 |  |
| Jogador 5 | 2-2 | 18:35:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_MasterYi_AD | 0.3800 |  |
| Jogador 5 | 2-2 | 18:35:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 5 | 2-2 | 18:35:57 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_MasterYi_AD | -0.1300 |  |
| Jogador 5 | 2-2 | 18:35:57 | MOVE Board -> Board: Rakan (i:2.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_MasterYi_AD | -0.1300 |  |
| Jogador 5 | 2-2 | 18:35:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-3 | 18:36:02 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 5 | 2-3 | 18:36:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 5 | 2-3 | 18:36:03 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 2-3 | 18:36:03 | MOVE Bench -> Board: Elise (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | -0.7500 |  |
| Jogador 5 | 2-3 | 18:36:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 2-4 | 18:36:09 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 5 | 2-4 | 18:36:09 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 5 | 2-4 | 18:36:10 | MOVE Bench -> Board: Elise (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 5 | 2-4 | 18:36:10 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 5 | 2-4 | 18:36:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 2-5 | 18:36:16 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_KogMaw18_AD | -0.3400 |  |
| Jogador 5 | 2-5 | 18:36:17 | MOVE Bench -> Board: Elise (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 5 | 2-5 | 18:36:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_KogMaw18_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 2-6 | 18:36:23 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 5 | 2-6 | 18:36:23 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 5 | 2-6 | 18:36:24 | MOVE Bench -> Board: Elise (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_KogMaw18_AD | -0.3500 |  |
| Jogador 5 | 2-6 | 18:36:24 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_KogMaw18_AD | -0.7700 |  |
| Jogador 5 | 2-6 | 18:36:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_KogMaw18_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 2-7 | 18:36:31 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 2-7 | 18:36:31 | MOVE Bench -> Board: Elise (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_KogMaw18_AD | -0.3500 |  |
| Jogador 5 | 2-7 | 18:36:31 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 5 | 2-7 | 18:36:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_KogMaw18_AD | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-1 | 18:36:38 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-1 | 18:36:38 | MOVE Bench -> Board: Elise (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Colosso | DA_KogMaw18_AD | -0.7500 |  |
| Jogador 5 | 3-1 | 18:36:39 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Colosso | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 5 | 3-1 | 18:36:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Colosso | DA_KogMaw18_AD | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-2 | 18:36:45 | MOVE Bench -> Board: Rakan (i:2.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 5 | 3-2 | 18:36:45 | MOVE Bench -> Board: Elise (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 5 | 3-2 | 18:36:47 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 5 | 3-2 | 18:36:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_KogMaw18_AD | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-2 | 18:36:50 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_KogMaw18_AD | 0.5600 |  |
| Jogador 5 | 3-3 | 18:36:52 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-3 | 18:36:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-3 | 18:36:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 4 | Colosso | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 5 | 3-3 | 18:36:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 4 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-3 | 18:36:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 4 | Colosso | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 5 | 3-3 | 18:36:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 4 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-3 | 18:36:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 4 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-3 | 18:36:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 4 | Colosso | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 5 | 3-3 | 18:36:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 4 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-3 | 18:36:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 4 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 3-3 | 18:36:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 4 | Colosso | DA_KogMaw18_AD | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-4 | 18:37:00 | COMPROU: Morgana (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 3-4 | 18:37:00 | MOVE Bench -> Board: Morgana (i:8.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Colosso | DA_18_Morgana | -0.3000 |  |
| Jogador 5 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Colosso | DA_18_Morgana | -0.1100 |  |
| Jogador 5 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Colosso | DA_18_Morgana | -0.0300 |  |
| Jogador 5 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Colosso | DA_18_Morgana | -0.1100 |  |
| Jogador 5 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 1 | Colosso | DA_18_Morgana | -0.0300 |  |
| Jogador 5 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Morgana | -0.0300 |  |
| Jogador 5 | 3-4 | 18:37:02 | MOVE Board -> Board: Morgana (i:8.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Morgana | 0.0200 |  |
| Jogador 5 | 3-4 | 18:37:02 | MOVE Board -> Board: Yorick (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Morgana | -0.1300 |  |
| Jogador 5 | 3-4 | 18:37:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 3-5 | 18:37:08 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Morgana | -0.0400 |  |
| Jogador 5 | 3-5 | 18:37:08 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Morgana | 0.7400 |  |
| Jogador 5 | 3-5 | 18:37:08 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Morgana | -0.0300 |  |
| Jogador 5 | 3-5 | 18:37:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 3-5 | 18:37:13 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Morgana | 0.6200 |  |
| Jogador 5 | 3-6 | 18:37:16 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Morgana | 0.2100 |  |
| Jogador 5 | 3-6 | 18:37:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Morgana | -0.0100 |  |
| Jogador 5 | 3-6 | 18:37:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 3-7 | 18:37:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Morgana | 0.2200 |  |
| Jogador 5 | 3-7 | 18:37:25 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Morgana | -0.0100 |  |
| Jogador 5 | 3-7 | 18:37:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 4-1 | 18:37:34 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Morgana | -0.1100 |  |
| Jogador 5 | 4-1 | 18:37:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 4-2 | 18:37:43 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Morgana | 0.7300 |  |
| Jogador 5 | 4-2 | 18:37:43 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Morgana | 0.7400 |  |
| Jogador 5 | 4-2 | 18:37:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Morgana | -0.2300 |  |
| Jogador 5 | 4-2 | 18:37:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Morgana | 0.0000 |  |
| Jogador 5 | 4-3 | 18:37:53 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Morgana | 0.0700 |  |
| Jogador 5 | 4-3 | 18:37:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Morgana | -0.2600 |  |
| Jogador 5 | 4-3 | 18:37:53 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Morgana | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 5 | 4-3 | 18:37:53 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Morgana | 0.0800 |  |
| Jogador 5 | 4-3 | 18:37:53 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Sejuani | 0.7700 |  |
| Jogador 5 | 4-3 | 18:37:54 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | -0.2500 |  |
| Jogador 5 | 4-3 | 18:37:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 4-3 | 18:37:58 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | 0.5500 |  |
| Jogador 5 | 4-4 | 18:38:02 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | 0.1300 |  |
| Jogador 5 | 4-4 | 18:38:03 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Sentinel18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 5 | 4-4 | 18:38:03 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | 0.0800 |  |
| Jogador 5 | 4-4 | 18:38:03 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Sejuani | 0.2200 |  |
| Jogador 5 | 4-4 | 18:38:03 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Sejuani | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 5 | 4-4 | 18:38:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 4-5 | 18:38:11 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_18_Sejuani | 0.1300 |  |
| Jogador 5 | 4-5 | 18:38:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Sejuani | 0.7400 |  |
| Jogador 5 | 4-5 | 18:38:11 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Sejuani | -0.2400 | FAST8_REROLL_REVIEW |
| Jogador 5 | 4-5 | 18:38:12 | VENDEU: Sejuani (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_Sentinel18 | -0.4000 |  |
| Jogador 5 | 4-5 | 18:38:12 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 5 | 4-5 | 18:38:12 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 5 | 4-5 | 18:38:12 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 5 | 4-5 | 18:38:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-6 | 18:38:19 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 5 | 4-6 | 18:38:22 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 5 | 4-6 | 18:38:22 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-6 | 18:38:22 | MOVE Bench -> Board: Vi (i:12.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 4-6 | 18:38:22 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.6100 |  |
| Jogador 5 | 4-6 | 18:38:22 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.5200 |  |
| Jogador 5 | 4-6 | 18:38:23 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 5 | 4-6 | 18:38:23 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0900 | FAST8_REROLL_REVIEW |
| Jogador 5 | 4-6 | 18:38:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-7 | 18:38:28 | BIGORNA: escolheu componente TFT_Item_RecurveBow | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-7 | 18:38:29 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_KogMaw18_AD | -0.3300 |  |
| Jogador 5 | 4-7 | 18:38:29 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 5 | 4-7 | 18:38:29 | MOVE Bench -> Board: Diana (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 5 | 4-7 | 18:38:29 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 4-7 | 18:38:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-7 | 18:38:33 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.6200 |  |
| Jogador 5 | 5-1 | 18:38:37 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 5-1 | 18:38:37 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 5-1 | 18:38:37 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 5 | 5-1 | 18:38:38 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 5 | 5-1 | 18:38:38 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Colosso | DA_Vi18 | -0.3900 |  |
| Jogador 5 | 5-1 | 18:38:38 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_Vi18 | -0.0500 |  |
| Jogador 5 | 5-1 | 18:38:38 | REROLL | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 5-1 | 18:38:39 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_Vi18 | 0.1300 |  |
| Jogador 5 | 5-1 | 18:38:39 | COMPROU: Maokai (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_Vi18 | 0.2000 |  |
| Jogador 5 | 5-1 | 18:38:39 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_Vi18 | -0.8400 |  |
| Jogador 5 | 5-1 | 18:38:42 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 5 | 5-2 | 18:38:46 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_Vi18 | 0.7100 |  |
| Jogador 5 | 5-2 | 18:38:46 | REROLL | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 5-2 | 18:38:49 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_Vi18 | -0.3100 |  |
| Jogador 5 | 5-2 | 18:38:49 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_Vi18 | 0.7600 |  |
| Jogador 5 | 5-2 | 18:38:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_Vi18 | 0.6500 |  |
| Jogador 5 | 5-2 | 18:38:49 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_Vi18 | -0.2300 |  |
| Jogador 5 | 5-2 | 18:38:49 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 5-2 | 18:38:50 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_Vi18 | 0.0700 |  |
| Jogador 5 | 5-2 | 18:38:50 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_Vi18 | -0.2300 |  |
| Jogador 5 | 5-2 | 18:38:50 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_Vi18 | 0.0700 |  |
| Jogador 5 | 5-2 | 18:38:50 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 5 | 5-3 | 18:38:56 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_Vi18 | 0.7500 |  |
| Jogador 5 | 5-3 | 18:38:56 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_Vi18 | 0.1300 |  |
| Jogador 5 | 5-3 | 18:38:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Master Yi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_Vi18 | 0.0800 |  |
| Jogador 5 | 5-3 | 18:38:56 | VENDEU: Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_Vi18 | 0.0300 |  |
| Jogador 5 | 5-3 | 18:38:56 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Vi18 | 0.1700 |  |
| Jogador 5 | 5-3 | 18:38:57 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 5-3 | 18:38:57 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Vi18 | 0.0200 |  |
| Jogador 5 | 5-3 | 18:38:57 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 5 | 5-3 | 18:38:57 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Vi18 | 0.0400 |  |
| Jogador 5 | 5-3 | 18:39:00 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_Vi18 | 0.0800 |  |
| Jogador 5 | 5-3 | 18:39:00 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_Vi18 | -0.0500 |  |
| Jogador 5 | 5-4 | 18:39:05 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Colosso | DA_Vi18 | 0.0400 |  |
| Jogador 5 | 5-4 | 18:39:05 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_Vi18 | 0.2700 |  |
| Jogador 5 | 5-4 | 18:39:05 | VENDEU: Aronguejo (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_Vi18 | -0.4000 |  |
| Jogador 5 | 5-4 | 18:39:05 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Colosso | DA_Vi18 | -0.1500 |  |
| Jogador 5 | 5-4 | 18:39:05 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_Vi18 | 0.1200 |  |
| Jogador 5 | 5-4 | 18:39:06 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Colosso | DA_Vi18 | -0.1500 |  |
| Jogador 5 | 5-4 | 18:39:06 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 5-4 | 18:39:06 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Colosso | DA_Vi18 | 0.0400 |  |
| Jogador 5 | 5-4 | 18:39:06 | COMPROU: Lux (Feérica) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_Vi18 | 0.2600 |  |
| Jogador 5 | 5-4 | 18:39:06 | VENDEU: Master Yi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 11 | 0 | Colosso | DA_Vi18 | -0.2800 |  |
| Jogador 5 | 5-4 | 18:39:09 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 11 | 0 | Colosso | DA_Vi18 | -0.0500 |  |
| Jogador 6 | ? | 18:35:17 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | 0.0000 |  |
| Jogador 6 | ? | 18:35:17 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 6 | ? | 18:35:18 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6100 |  |
| Jogador 6 | ? | 18:35:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 6 | 1-1 | 18:35:23 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0300 |  |
| Jogador 6 | 1-1 | 18:35:23 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0200 |  |
| Jogador 6 | 1-1 | 18:35:24 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | -0.2200 |  |
| Jogador 6 | 1-1 | 18:35:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0000 |  |
| Jogador 6 | 1-2 | 18:35:29 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0800 |  |
| Jogador 6 | 1-2 | 18:35:30 | MOVE Bench -> Board: Caitlyn (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Caitlyn | 0.2800 |  |
| Jogador 6 | 1-2 | 18:35:30 | MOVE Board -> Board: Caitlyn (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.1800 |  |
| Jogador 6 | 1-2 | 18:35:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0000 |  |
| Jogador 6 | 1-3 | 18:35:36 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yunara | 0.2600 |  |
| Jogador 6 | 1-3 | 18:35:36 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | -0.1200 |  |
| Jogador 6 | 1-3 | 18:35:36 | MOVE Bench -> Board: Yunara (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | -0.7200 |  |
| Jogador 6 | 1-3 | 18:35:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Murkwolf18 | 0.0000 |  |
| Jogador 6 | 1-4 | 18:35:42 | MOVE Bench -> Board: Akali (i:2.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yunara | -0.2400 |  |
| Jogador 6 | 1-4 | 18:35:43 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Murkwolf18 | 0.4800 |  |
| Jogador 6 | 1-4 | 18:35:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | 0.1400 |  |
| Jogador 6 | 1-4 | 18:35:43 | MOVE Bench -> Board: Rammus (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 1-4 | 18:35:44 | MOVE Bench -> Board: Akali (i:2.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | -0.2500 |  |
| Jogador 6 | 1-4 | 18:35:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-1 | 18:35:49 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | -0.6200 |  |
| Jogador 6 | 2-1 | 18:35:49 | MOVE Bench -> Board: Rammus (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | -0.1000 |  |
| Jogador 6 | 2-1 | 18:35:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 2-2 | 18:35:56 | MOVE Bench -> Board: Akali (i:2.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Rammus | -0.2500 |  |
| Jogador 6 | 2-2 | 18:35:56 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Rammus | -0.1900 |  |
| Jogador 6 | 2-2 | 18:35:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | — | DA_18_Rammus | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-3 | 18:36:02 | MOVE Bench -> Board: Yunara (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | — | DA_18_Rammus | -0.8300 |  |
| Jogador 6 | 2-3 | 18:36:03 | MOVE Bench -> Board: Rammus (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | — | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 2-3 | 18:36:03 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | — | DA_18_Rammus | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-4 | 18:36:09 | MOVE Bench -> Board: Akali (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Devastador | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 2-4 | 18:36:09 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Rammus | 0.0200 |  |
| Jogador 6 | 2-4 | 18:36:10 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Devastador | DA_18_Rammus | 0.3900 |  |
| Jogador 6 | 2-4 | 18:36:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Devastador | DA_18_Rammus | 0.0200 |  |
| Jogador 6 | 2-4 | 18:36:11 | MOVE Bench -> Board: Camille (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Devastador | DA_18_Rammus | -0.7400 |  |
| Jogador 6 | 2-4 | 18:36:11 | MOVE Bench -> Board: Akali (i:2.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Devastador | DA_18_Rammus | 0.0700 |  |
| Jogador 6 | 2-4 | 18:36:11 | MOVE Bench -> Board: Rammus (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Devastador | DA_18_Rammus | -0.3300 |  |
| Jogador 6 | 2-4 | 18:36:11 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Devastador | DA_18_Rammus | 0.5900 |  |
| Jogador 6 | 2-4 | 18:36:12 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Devastador | DA_18_Rammus | 0.3700 |  |
| Jogador 6 | 2-4 | 18:36:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Rammus | -0.0400 |  |
| Jogador 6 | 2-4 | 18:36:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Rammus | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-5 | 18:36:16 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Rammus | -0.4200 |  |
| Jogador 6 | 2-5 | 18:36:17 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Devastador | DA_18_Rammus | 0.9400 |  |
| Jogador 6 | 2-5 | 18:36:17 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Devastador | DA_18_Rammus | -0.4000 |  |
| Jogador 6 | 2-5 | 18:36:17 | MOVE Bench -> Board: Rammus (i:6.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Devastador | DA_18_Rammus | -0.4300 |  |
| Jogador 6 | 2-5 | 18:36:17 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 2 | Devastador | DA_18_Rammus | -0.0400 |  |
| Jogador 6 | 2-6 | 18:36:23 | VENDEU: Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 42 | 3 | Devastador | DA_18_Rammus | -0.4800 |  |
| Jogador 6 | 2-6 | 18:36:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 6 | 2-6 | 18:36:24 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 2-6 | 18:36:24 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 6 | 2-6 | 18:36:24 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 2-7 | 18:36:31 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kog'Maw (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 49 | 3 | Devastador | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 6 | 2-7 | 18:36:31 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 47 | 3 | Devastador | DA_KogMaw18_AD | 0.7900 |  |
| Jogador 6 | 2-7 | 18:36:31 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 47 | 3 | Devastador | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 6 | 2-7 | 18:36:32 | MOVE Bench -> Board: Rammus (i:6.0) <-> Camille (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 47 | 3 | Devastador | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 6 | 2-7 | 18:36:32 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 43 | 3 | Devastador | DA_KogMaw18_AD | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-7 | 18:36:32 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | -0.0200 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-7 | 18:36:32 | MOVE Bench -> Board: Camille (i:2.0) <-> Lobo Trevoguari (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 6 | 2-7 | 18:36:32 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 2-7 | 18:36:33 | MOVE Bench -> Board: Rammus (i:6.0) <-> Camille (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | -0.4700 |  |
| Jogador 6 | 2-7 | 18:36:34 | MOVE Bench -> Board: Camille (i:2.0) <-> Lobo Trevoguari (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 6 | 2-7 | 18:36:34 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 39 | 3 | Devastador | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 6 | 3-1 | 18:36:38 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Rammus (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 47 | 3 | Devastador | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 6 | 3-1 | 18:36:38 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Devastador | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 6 | 3-1 | 18:36:39 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Devastador | DA_KogMaw18_AD | -0.4800 |  |
| Jogador 6 | 3-1 | 18:36:39 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Devastador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 3-1 | 18:36:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Devastador | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 6 | 3-2 | 18:36:45 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 54 | 4 | Devastador | DA_18_Rammus | 0.9200 |  |
| Jogador 6 | 3-2 | 18:36:45 | MOVE Bench -> Board: Rammus (i:12.0) <-> Kog'Maw (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 54 | 4 | Devastador | DA_18_Rammus | -0.3000 |  |
| Jogador 6 | 3-2 | 18:36:47 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Rammus | -0.4800 |  |
| Jogador 6 | 3-2 | 18:36:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Rammus | -0.1600 |  |
| Jogador 6 | 3-2 | 18:36:50 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Rammus | 0.3000 |  |
| Jogador 6 | 3-3 | 18:36:52 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Devastador | DA_18_Rammus | 0.9300 |  |
| Jogador 6 | 3-3 | 18:36:53 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Rammus (i:12.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Devastador | DA_18_Rammus | 0.0800 |  |
| Jogador 6 | 3-3 | 18:36:53 | MOVE Bench -> Board: Rammus (i:12.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Devastador | DA_18_Rammus | -0.3000 |  |
| Jogador 6 | 3-3 | 18:36:53 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Lobo Trevoguari (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Devastador | DA_18_Rammus | -0.4900 |  |
| Jogador 6 | 3-3 | 18:36:53 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 62 | 5 | Devastador | DA_18_Rammus | -0.1300 |  |
| Jogador 6 | 3-3 | 18:36:57 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Devastador | DA_18_Rammus | 0.4800 |  |
| Jogador 6 | 3-4 | 18:37:00 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Devastador | DA_18_Rammus | 0.3000 |  |
| Jogador 6 | 3-4 | 18:37:00 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Devastador | DA_18_Rammus | -0.2700 |  |
| Jogador 6 | 3-4 | 18:37:01 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Devastador | DA_18_Rammus | 0.7300 |  |
| Jogador 6 | 3-4 | 18:37:01 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Devastador | DA_18_Rammus | 0.8700 |  |
| Jogador 6 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Devastador | DA_18_Rammus | 0.0100 |  |
| Jogador 6 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Devastador | DA_18_Rammus | 0.0100 |  |
| Jogador 6 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 5 | Devastador | DA_18_Rammus | 0.0100 |  |
| Jogador 6 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 5 | Devastador | DA_18_Rammus | 0.0100 |  |
| Jogador 6 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 5 | Devastador | DA_18_Rammus | -0.0800 |  |
| Jogador 6 | 3-4 | 18:37:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 5 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 3-4 | 18:37:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 5 | Devastador | DA_18_Rammus | -0.1300 |  |
| Jogador 6 | 3-5 | 18:37:08 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Devastador | DA_18_Rammus | 0.9200 |  |
| Jogador 6 | 3-5 | 18:37:08 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Devastador | DA_18_Rammus | 0.2400 |  |
| Jogador 6 | 3-5 | 18:37:08 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Devastador | DA_18_Rammus | 0.2400 |  |
| Jogador 6 | 3-5 | 18:37:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Devastador | DA_18_Rammus | 0.0800 |  |
| Jogador 6 | 3-5 | 18:37:09 | MOVE Bench -> Board: Caitlyn (i:8.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Devastador | DA_18_Rammus | -0.0100 |  |
| Jogador 6 | 3-5 | 18:37:09 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Devastador | DA_18_Rammus | 0.2900 |  |
| Jogador 6 | 3-5 | 18:37:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 4 | Devastador | DA_18_Rammus | -0.1100 |  |
| Jogador 6 | 3-5 | 18:37:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 4 | Devastador | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 3-5 | 18:37:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 4 | Devastador | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 3-5 | 18:37:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 4 | Devastador | DA_18_Rammus | -0.1100 |  |
| Jogador 6 | 3-5 | 18:37:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 4 | Devastador | DA_18_Rammus | -0.0800 |  |
| Jogador 6 | 3-6 | 18:37:16 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Devastador | DA_18_Rammus | 0.7800 |  |
| Jogador 6 | 3-6 | 18:37:17 | COMPROU: Gnar (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Devastador | DA_18_Rammus | -0.1000 |  |
| Jogador 6 | 3-6 | 18:37:17 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Devastador | DA_18_Rammus | -0.0500 |  |
| Jogador 6 | 3-6 | 18:37:17 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Devastador | DA_18_Rammus | 0.1100 |  |
| Jogador 6 | 3-6 | 18:37:17 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 2 | Devastador | DA_18_Rammus | -0.1800 |  |
| Jogador 6 | 3-6 | 18:37:18 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 2 | Devastador | DA_18_Rammus | -0.2400 | FAST8_REROLL_REVIEW |
| Jogador 6 | 3-6 | 18:37:18 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Devastador | DA_18_Rammus | 0.7300 |  |
| Jogador 6 | 3-6 | 18:37:18 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 2 | Devastador | DA_18_Rammus | -0.2800 |  |
| Jogador 6 | 3-6 | 18:37:18 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 2 | Devastador | DA_18_Rammus | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 6 | 3-6 | 18:37:20 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 2 | Devastador | DA_18_Rammus | 0.0700 |  |
| Jogador 6 | 3-6 | 18:37:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 2 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 3-7 | 18:37:25 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Devastador | DA_18_Rammus | -0.1900 |  |
| Jogador 6 | 3-7 | 18:37:25 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Devastador | DA_18_Rammus | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 6 | 3-7 | 18:37:25 | VENDEU: Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Devastador | DA_18_Rammus | 0.0200 |  |
| Jogador 6 | 3-7 | 18:37:26 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Devastador | DA_18_Rammus | 0.7400 |  |
| Jogador 6 | 3-7 | 18:37:26 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 1 | Devastador | DA_18_Rammus | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 6 | 3-7 | 18:37:26 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Devastador | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 3-7 | 18:37:26 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 1 | Devastador | DA_18_Rammus | 0.0300 |  |
| Jogador 6 | 3-7 | 18:37:27 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Devastador | DA_18_Rammus | 0.0800 |  |
| Jogador 6 | 3-7 | 18:37:27 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Devastador | DA_18_Rammus | 0.1100 |  |
| Jogador 6 | 3-7 | 18:37:29 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Devastador | DA_18_Rammus | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 6 | 3-7 | 18:37:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-1 | 18:37:34 | VENDEU: Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_18_Rammus | 0.0200 |  |
| Jogador 6 | 4-1 | 18:37:34 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Devastador | DA_18_Rammus | 0.7600 |  |
| Jogador 6 | 4-1 | 18:37:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Devastador | DA_18_Rammus | 0.7200 |  |
| Jogador 6 | 4-1 | 18:37:34 | MOVE Bench -> Board: Amumu (i:8.0) <-> Caitlyn (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Devastador | DA_18_Rammus | -0.2200 |  |
| Jogador 6 | 4-1 | 18:37:35 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 1 | Devastador | DA_18_Rammus | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 6 | 4-1 | 18:37:35 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Devastador | DA_18_Rammus | 0.0600 |  |
| Jogador 6 | 4-1 | 18:37:35 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 1 | Devastador | DA_18_Rammus | 0.2100 |  |
| Jogador 6 | 4-1 | 18:37:36 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Devastador | DA_18_Rammus | -0.2400 | FAST8_REROLL_REVIEW |
| Jogador 6 | 4-1 | 18:37:36 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Devastador | DA_18_Rammus | 0.0500 |  |
| Jogador 6 | 4-1 | 18:37:38 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Devastador | DA_18_Rammus | 0.7700 |  |
| Jogador 6 | 4-1 | 18:37:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 1 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-2 | 18:37:43 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Devastador | DA_18_Rammus | 0.2100 |  |
| Jogador 6 | 4-2 | 18:37:43 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Devastador | DA_18_Rammus | 0.0100 |  |
| Jogador 6 | 4-2 | 18:37:44 | MOVE Bench -> Board: Caitlyn (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Devastador | DA_18_Rammus | 0.2200 |  |
| Jogador 6 | 4-2 | 18:37:44 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 1 | Devastador | DA_18_Rammus | 0.3600 |  |
| Jogador 6 | 4-2 | 18:37:44 | REROLL | STABILIZE | STABILIZE: pressão de vida | 7 | 1 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-2 | 18:37:44 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Devastador | DA_18_Rammus | -0.2400 |  |
| Jogador 6 | 4-2 | 18:37:45 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 1 | Devastador | DA_18_Rammus | 0.2000 |  |
| Jogador 6 | 4-2 | 18:37:45 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 1 | Devastador | DA_18_Rammus | -0.2000 |  |
| Jogador 6 | 4-2 | 18:37:45 | MOVE Bench -> Board: Amumu (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 7 | 1 | Devastador | DA_18_Rammus | 0.6500 |  |
| Jogador 6 | 4-2 | 18:37:47 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Devastador | DA_18_Rammus | 0.6400 |  |
| Jogador 6 | 4-2 | 18:37:47 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-3 | 18:37:53 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Devastador | DA_18_Rammus | 0.0900 |  |
| Jogador 6 | 4-3 | 18:37:53 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Devastador | DA_18_Rammus | -0.0500 |  |
| Jogador 6 | 4-3 | 18:37:53 | REROLL | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-3 | 18:37:53 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Devastador | DA_18_Rammus | 0.1200 |  |
| Jogador 6 | 4-3 | 18:37:53 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Devastador | DA_18_Rammus | 0.2000 |  |
| Jogador 6 | 4-3 | 18:37:54 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-3 | 18:37:54 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-3 | 18:37:54 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Devastador | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 4-3 | 18:37:54 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Devastador | DA_18_Rammus | 0.2800 |  |
| Jogador 6 | 4-3 | 18:37:56 | REROLL | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-3 | 18:37:57 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-4 | 18:38:02 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-4 | 18:38:03 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-4 | 18:38:03 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-4 | 18:38:03 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Devastador | DA_18_Rammus | -0.0300 |  |
| Jogador 6 | 4-4 | 18:38:03 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Devastador | DA_18_Rammus | 0.1200 |  |
| Jogador 6 | 4-4 | 18:38:04 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-5 | 18:38:11 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Devastador | DA_18_Rammus | 0.0400 |  |
| Jogador 6 | 4-5 | 18:38:11 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Devastador | DA_18_Rammus | 0.2900 |  |
| Jogador 6 | 4-5 | 18:38:11 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-5 | 18:38:12 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Devastador | DA_18_Rammus | -0.3400 |  |
| Jogador 6 | 4-5 | 18:38:12 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Devastador | DA_18_Rammus | 0.2900 |  |
| Jogador 6 | 4-5 | 18:38:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-5 | 18:38:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-5 | 18:38:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-5 | 18:38:13 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-6 | 18:38:19 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Devastador | DA_18_Rammus | 0.0300 |  |
| Jogador 6 | 4-6 | 18:38:22 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Devastador | DA_18_Rammus | 0.8100 |  |
| Jogador 6 | 4-6 | 18:38:22 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-6 | 18:38:22 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-6 | 18:38:22 | REROLL | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-6 | 18:38:22 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-7 | 18:38:28 | BIGORNA: escolheu componente TFT_Item_NegatronCloak | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 4-7 | 18:38:29 | VENDEU: Caitlyn (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Devastador | DA_18_Rammus | -0.7500 |  |
| Jogador 6 | 4-7 | 18:38:29 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Devastador | DA_18_Rammus | 0.7200 |  |
| Jogador 6 | 4-7 | 18:38:29 | REROLL | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-7 | 18:38:29 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-7 | 18:38:30 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-7 | 18:38:30 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 4-7 | 18:38:30 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Devastador | DA_18_Rammus | 0.1800 |  |
| Jogador 6 | 4-7 | 18:38:30 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Devastador | DA_18_Rammus | 0.0000 |  |
| Jogador 6 | 5-1 | 18:38:37 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Devastador | DA_18_Rammus | -0.8000 |  |
| Jogador 6 | 5-1 | 18:38:37 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Devastador | DA_18_Rammus | 0.2700 |  |
| Jogador 6 | 5-1 | 18:38:37 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Devastador | DA_18_Rammus | -0.0900 |  |
| Jogador 6 | 5-1 | 18:38:38 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Devastador | DA_18_Rammus | -0.0500 |  |
| Jogador 7 | ? | 18:35:17 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0300 |  |
| Jogador 7 | ? | 18:35:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 7 | ? | 18:35:18 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 7 | ? | 18:35:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-1 | 18:35:23 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0800 |  |
| Jogador 7 | 1-1 | 18:35:23 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 7 | 1-1 | 18:35:24 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 7 | 1-1 | 18:35:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 1.0300 |  |
| Jogador 7 | 1-1 | 18:35:25 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5400 |  |
| Jogador 7 | 1-1 | 18:35:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-2 | 18:35:29 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.2100 |  |
| Jogador 7 | 1-2 | 18:35:30 | MOVE Bench -> Board: Elise (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | -0.2100 |  |
| Jogador 7 | 1-2 | 18:35:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 7 | 1-3 | 18:35:36 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Elise | -0.4000 |  |
| Jogador 7 | 1-3 | 18:35:36 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | -0.8400 |  |
| Jogador 7 | 1-3 | 18:35:36 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | 1.0200 |  |
| Jogador 7 | 1-3 | 18:35:37 | MOVE Bench -> Board: Elise (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | -0.4000 |  |
| Jogador 7 | 1-3 | 18:35:37 | MOVE Bench -> Board: Elise (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | -0.2900 |  |
| Jogador 7 | 1-3 | 18:35:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 7 | 1-4 | 18:35:42 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Elise | 0.3700 |  |
| Jogador 7 | 1-4 | 18:35:43 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | 0.2000 |  |
| Jogador 7 | 1-4 | 18:35:43 | MOVE Bench -> Board: Alistar (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Elise | -0.0200 |  |
| Jogador 7 | 1-4 | 18:35:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | -0.0400 |  |
| Jogador 7 | 1-4 | 18:35:44 | MOVE Board -> Board: Alistar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0300 |  |
| Jogador 7 | 1-4 | 18:35:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 7 | 2-1 | 18:35:49 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Elise | -0.0600 |  |
| Jogador 7 | 2-1 | 18:35:49 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Hecarim | 0.3500 |  |
| Jogador 7 | 2-1 | 18:35:50 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Hecarim | -0.3200 |  |
| Jogador 7 | 2-1 | 18:35:50 | MOVE Bench -> Board: Elise (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Hecarim | -0.4000 |  |
| Jogador 7 | 2-1 | 18:35:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-2 | 18:35:56 | MOVE Bench -> Board: Elise (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Hecarim | -0.5500 |  |
| Jogador 7 | 2-2 | 18:35:56 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Hecarim | -0.3200 |  |
| Jogador 7 | 2-2 | 18:35:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Hecarim | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-3 | 18:36:02 | MOVE Bench -> Board: Elise (i:4.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | — | DA_18_Hecarim | -0.4000 |  |
| Jogador 7 | 2-3 | 18:36:03 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 17 | 1 | — | DA_18_Hecarim | 0.4400 |  |
| Jogador 7 | 2-3 | 18:36:03 | COMPROU: Azuporã (Custo 4 \| i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 1 | — | DA_Sentinel18 | 0.2700 |  |
| Jogador 7 | 2-3 | 18:36:03 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 1 | — | DA_Sentinel18 | -0.2900 |  |
| Jogador 7 | 2-3 | 18:36:04 | MOVE Bench -> Board: Elise (i:4.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 1 | — | DA_Sentinel18 | -0.4000 |  |
| Jogador 7 | 2-3 | 18:36:04 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 13 | 1 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 18:36:09 | MOVE Bench -> Board: Elise (i:4.0) <-> Azuporã (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Vanguarda | DA_Sentinel18 | -0.6500 |  |
| Jogador 7 | 2-4 | 18:36:09 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Vanguarda | DA_Sentinel18 | -0.2000 |  |
| Jogador 7 | 2-4 | 18:36:10 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 19 | 1 | Vanguarda | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-5 | 18:36:16 | MOVE Bench -> Board: Elise (i:4.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 27 | 2 | Vanguarda | DA_Sentinel18 | -0.4000 |  |
| Jogador 7 | 2-5 | 18:36:17 | MOVE Bench -> Board: Elise (i:4.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 27 | 2 | Vanguarda | DA_Sentinel18 | -0.8000 |  |
| Jogador 7 | 2-5 | 18:36:17 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 27 | 2 | Vanguarda | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-6 | 18:36:23 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Azuporã (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 34 | 2 | Vanguarda | DA_Sentinel18 | -0.5700 |  |
| Jogador 7 | 2-6 | 18:36:23 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 34 | 2 | Vanguarda | DA_Sentinel18 | -0.1900 |  |
| Jogador 7 | 2-6 | 18:36:24 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 34 | 2 | Vanguarda | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-7 | 18:36:31 | MOVE Bench -> Board: Elise (i:4.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 42 | 3 | Vanguarda | DA_Sentinel18 | -0.8000 |  |
| Jogador 7 | 2-7 | 18:36:31 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Azuporã (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 42 | 3 | Vanguarda | DA_Sentinel18 | -0.5700 |  |
| Jogador 7 | 2-7 | 18:36:31 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 42 | 3 | Vanguarda | DA_Sentinel18 | -0.1100 |  |
| Jogador 7 | 3-1 | 18:36:38 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 4 | Vanguarda | DA_Sentinel18 | -0.1900 |  |
| Jogador 7 | 3-1 | 18:36:38 | MOVE Bench -> Board: Elise (i:4.0) <-> Elise (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 4 | Vanguarda | DA_Sentinel18 | -0.4000 |  |
| Jogador 7 | 3-1 | 18:36:39 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 52 | 4 | Vanguarda | DA_Sentinel18 | -0.1200 |  |
| Jogador 7 | 3-2 | 18:36:45 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 60 | 5 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-2 | 18:36:45 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Azuporã (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 60 | 5 | Vanguarda | DA_Sentinel18 | -0.3500 |  |
| Jogador 7 | 3-2 | 18:36:47 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 60 | 5 | Vanguarda | DA_Sentinel18 | -0.4300 |  |
| Jogador 7 | 3-2 | 18:36:47 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 60 | 5 | Vanguarda | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 3-3 | 18:36:52 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 68 | 5 | Vanguarda | DA_Sentinel18 | 0.3300 |  |
| Jogador 7 | 3-3 | 18:36:53 | COMPROU: Diana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 65 | 5 | Vanguarda | DA_Sentinel18 | 0.3300 |  |
| Jogador 7 | 3-3 | 18:36:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 64 | 5 | Vanguarda | DA_Sentinel18 | 0.8700 |  |
| Jogador 7 | 3-3 | 18:36:53 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 60 | 5 | Vanguarda | DA_Sentinel18 | 0.0000 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 3-3 | 18:36:53 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 5 | Vanguarda | DA_Sentinel18 | 0.4600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 3-3 | 18:36:54 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Fiddlesticks (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 5 | Vanguarda | DA_Sentinel18 | -0.6500 |  |
| Jogador 7 | 3-3 | 18:36:54 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Azuporã (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 5 | Vanguarda | DA_Sentinel18 | -0.3500 |  |
| Jogador 7 | 3-3 | 18:36:54 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 56 | 5 | Vanguarda | DA_Sentinel18 | -0.1200 |  |
| Jogador 7 | 3-3 | 18:36:57 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Vanguarda | DA_Sentinel18 | 0.4600 |  |
| Jogador 7 | 3-4 | 18:37:00 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Vanguarda | DA_Sentinel18 | 0.8400 |  |
| Jogador 7 | 3-4 | 18:37:00 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Vanguarda | DA_Sentinel18 | 0.6900 |  |
| Jogador 7 | 3-4 | 18:37:01 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Vanguarda | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Vanguarda | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 5 | Vanguarda | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 3-4 | 18:37:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 5 | Vanguarda | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 5 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 5 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-4 | 18:37:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 5 | Vanguarda | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 3-4 | 18:37:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 5 | Vanguarda | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-4 | 18:37:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 5 | Vanguarda | DA_Sentinel18 | -0.1200 |  |
| Jogador 7 | 3-5 | 18:37:08 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Vanguarda | DA_Sentinel18 | 0.6900 |  |
| Jogador 7 | 3-5 | 18:37:08 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 3 | Vanguarda | DA_Sentinel18 | -0.2500 |  |
| Jogador 7 | 3-5 | 18:37:08 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 3 | Vanguarda | DA_Sentinel18 | -0.1600 | FAST8_REROLL_REVIEW |
| Jogador 7 | 3-5 | 18:37:09 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 3 | Vanguarda | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 3-5 | 18:37:09 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 32 | 3 | Vanguarda | DA_Fiddlesticks18 | 0.7900 |  |
| Jogador 7 | 3-5 | 18:37:09 | COMPROU: Grompe (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 30 | 3 | Vanguarda | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 7 | 3-5 | 18:37:10 | REROLL | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 28 | 3 | Vanguarda | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 7 | 3-5 | 18:37:10 | REROLL | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 26 | 3 | Vanguarda | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 7 | 3-5 | 18:37:10 | REROLL | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 24 | 3 | Vanguarda | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 3-5 | 18:37:12 | REROLL | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 3 | Vanguarda | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 3-5 | 18:37:12 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 22 | 3 | Vanguarda | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-6 | 18:37:16 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.5300 |  |
| Jogador 7 | 3-6 | 18:37:17 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 3-6 | 18:37:17 | REROLL | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-6 | 18:37:17 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.3500 |  |
| Jogador 7 | 3-6 | 18:37:17 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.8100 |  |
| Jogador 7 | 3-6 | 18:37:18 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 3-6 | 18:37:18 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 7 | 3-6 | 18:37:18 | REROLL | STABILIZE | STABILIZE: pressão de vida | 24 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-6 | 18:37:18 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 7 | 3-6 | 18:37:20 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.8600 |  |
| Jogador 7 | 3-6 | 18:37:20 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 25 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.0700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-7 | 18:37:25 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 7 | 3-7 | 18:37:25 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.3600 |  |
| Jogador 7 | 3-7 | 18:37:25 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.3800 |  |
| Jogador 7 | 3-7 | 18:37:26 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.6200 |  |
| Jogador 7 | 3-7 | 18:37:26 | REROLL | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-7 | 18:37:26 | REROLL | STABILIZE | STABILIZE: pressão de vida | 24 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-7 | 18:37:26 | REROLL | STABILIZE | STABILIZE: pressão de vida | 22 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-7 | 18:37:27 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.8200 |  |
| Jogador 7 | 3-7 | 18:37:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 2 | Vanguarda | DA_Fiddlesticks18 | 0.8600 |  |
| Jogador 7 | 3-7 | 18:37:29 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.1400 |  |
| Jogador 7 | 3-7 | 18:37:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 16 | 2 | Vanguarda | DA_Fiddlesticks18 | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-1 | 18:37:34 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 4-1 | 18:37:34 | REROLL | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-1 | 18:37:34 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 4-1 | 18:37:34 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 4-1 | 18:37:35 | REROLL | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 7 | 4-1 | 18:37:35 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 7 | 4-1 | 18:37:35 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.3400 |  |
| Jogador 7 | 4-1 | 18:37:36 | REROLL | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-1 | 18:37:36 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 4-1 | 18:37:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.8100 |  |
| Jogador 7 | 4-1 | 18:37:38 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-2 | 18:37:43 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 7 | 4-2 | 18:37:43 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 7 | 4-2 | 18:37:44 | REROLL | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-2 | 18:37:44 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 4-2 | 18:37:44 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.8300 |  |
| Jogador 7 | 4-2 | 18:37:44 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.4300 |  |
| Jogador 7 | 4-2 | 18:37:45 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 7 | 4-2 | 18:37:45 | REROLL | STABILIZE | STABILIZE: pressão de vida | 8 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 7 | 4-2 | 18:37:45 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 7 | 4-2 | 18:37:47 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.3300 |  |
| Jogador 7 | 4-2 | 18:37:47 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 8 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 4-3 | 18:37:53 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 16 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 4-3 | 18:37:53 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 7 | 4-3 | 18:37:53 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 11 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-3 | 18:37:53 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 4-3 | 18:37:53 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 7 | 4-3 | 18:37:54 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 7 | 4-3 | 18:37:54 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 11 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 7 | 4-3 | 18:37:54 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 7 | 4-3 | 18:37:54 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-3 | 18:37:56 | VENDEU: Grompe (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 11 | 0 | Vanguarda | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 7 | 4-3 | 18:37:57 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 11 | 0 | Vanguarda | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 7 | 4-4 | 18:38:02 | COMPROU: Morgana (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 4-4 | 18:38:03 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 16 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 4-4 | 18:38:03 | COMPROU: Morgana (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.7800 |  |
| Jogador 7 | 4-4 | 18:38:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 10 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-4 | 18:38:03 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 7 | 4-4 | 18:38:04 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 11 | 1 | Vanguarda | DA_Fiddlesticks18 | 0.2700 |  |
| Jogador 7 | 4-4 | 18:38:04 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 9 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 7 | 4-4 | 18:38:04 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 7 | 4-4 | 18:38:05 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.2500 |  |
| Jogador 7 | 4-4 | 18:38:07 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 12 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-4 | 18:38:07 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 12 | 1 | Vanguarda | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 8 | ? | 18:35:17 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6000 |  |
| Jogador 8 | ? | 18:35:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 18:35:23 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0100 |  |
| Jogador 8 | 1-1 | 18:35:23 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3100 |  |
| Jogador 8 | 1-1 | 18:35:24 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 1.0200 |  |
| Jogador 8 | 1-1 | 18:35:24 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.8100 |  |
| Jogador 8 | 1-1 | 18:35:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5300 |  |
| Jogador 8 | 1-1 | 18:35:25 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.1300 |  |
| Jogador 8 | 1-1 | 18:35:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-2 | 18:35:29 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 8 | 1-2 | 18:35:30 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.7300 |  |
| Jogador 8 | 1-2 | 18:35:30 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 8 | 1-2 | 18:35:30 | MOVE Bench -> Board: Yorick (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.3000 |  |
| Jogador 8 | 1-2 | 18:35:31 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.6500 |  |
| Jogador 8 | 1-2 | 18:35:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 8 | 1-3 | 18:35:36 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.2700 |  |
| Jogador 8 | 1-3 | 18:35:36 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | -0.4300 |  |
| Jogador 8 | 1-3 | 18:35:36 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 1.1200 |  |
| Jogador 8 | 1-3 | 18:35:37 | MOVE Bench -> Board: Leona (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.2100 |  |
| Jogador 8 | 1-3 | 18:35:37 | MOVE Board -> Board: Leona (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | -0.1500 |  |
| Jogador 8 | 1-3 | 18:35:37 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | -0.1000 |  |
| Jogador 8 | 1-3 | 18:35:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 1-4 | 18:35:42 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | 0.3900 |  |
| Jogador 8 | 1-4 | 18:35:43 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 1-4 | 18:35:43 | MOVE Board -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | -0.1000 |  |
| Jogador 8 | 1-4 | 18:35:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-1 | 18:35:49 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Leona | -0.0300 |  |
| Jogador 8 | 2-1 | 18:35:49 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Leona | 0.5200 |  |
| Jogador 8 | 2-1 | 18:35:50 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | 0.1300 |  |
| Jogador 8 | 2-1 | 18:35:50 | MOVE Bench -> Board: Warwick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | -0.4100 |  |
| Jogador 8 | 2-1 | 18:35:51 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | 0.0600 |  |
| Jogador 8 | 2-1 | 18:35:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-1 | 18:35:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-2 | 18:35:56 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Leona | 0.0400 |  |
| Jogador 8 | 2-2 | 18:35:56 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | 0.0100 |  |
| Jogador 8 | 2-2 | 18:35:56 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | -0.5300 |  |
| Jogador 8 | 2-2 | 18:35:56 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Cassiopeia | -0.4200 |  |
| Jogador 8 | 2-2 | 18:35:56 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Cassiopeia | 0.2700 |  |
| Jogador 8 | 2-2 | 18:35:57 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Cassiopeia | -0.3200 |  |
| Jogador 8 | 2-2 | 18:35:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 8 | 2-2 | 18:35:57 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.2000 |  |
| Jogador 8 | 2-2 | 18:35:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 8 | 2-2 | 18:35:58 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.5800 |  |
| Jogador 8 | 2-2 | 18:35:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 8 | 2-3 | 18:36:02 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.2400 |  |
| Jogador 8 | 2-3 | 18:36:03 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Krug18 | -0.1100 |  |
| Jogador 8 | 2-3 | 18:36:03 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.8500 |  |
| Jogador 8 | 2-3 | 18:36:03 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 8 | 2-4 | 18:36:09 | MOVE Bench -> Board: Krugue (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fera do Rift | DA_Krug18 | -0.4100 |  |
| Jogador 8 | 2-4 | 18:36:09 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fera do Rift | DA_Krug18 | 0.1900 |  |
| Jogador 8 | 2-4 | 18:36:10 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Fera do Rift | DA_Krug18 | -0.3700 |  |
| Jogador 8 | 2-4 | 18:36:10 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fera do Rift | DA_Krug18 | 0.2300 |  |
| Jogador 8 | 2-4 | 18:36:11 | MOVE Bench -> Board: Rammus (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fera do Rift | DA_18_Rammus | -0.4000 |  |
| Jogador 8 | 2-4 | 18:36:11 | MOVE Bench -> Board: Krugue (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fera do Rift | DA_18_Rammus | 0.0600 |  |
| Jogador 8 | 2-4 | 18:36:11 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fera do Rift | DA_Krug18 | -0.2900 |  |
| Jogador 8 | 2-4 | 18:36:11 | MOVE Bench -> Board: Rammus (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fera do Rift | DA_18_Rammus | -0.4100 |  |
| Jogador 8 | 2-4 | 18:36:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fera do Rift | DA_18_Rammus | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 2-5 | 18:36:16 | MOVE Bench -> Board: Krugue (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Fera do Rift | DA_Krug18 | 0.0500 |  |
| Jogador 8 | 2-5 | 18:36:17 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Fera do Rift | DA_Krug18 | 0.0600 |  |
| Jogador 8 | 2-5 | 18:36:17 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Fera do Rift | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-5 | 18:36:17 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Fera do Rift | DA_18_Tristana | 0.3000 |  |
| Jogador 8 | 2-5 | 18:36:17 | MOVE Bench -> Board: Tristana (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Caçador | DA_18_Tristana | -0.5100 |  |
| Jogador 8 | 2-5 | 18:36:18 | MOVE Bench -> Board: Krugue (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Caçador | DA_18_Tristana | -0.6400 |  |
| Jogador 8 | 2-5 | 18:36:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Caçador | DA_18_Tristana | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 2-6 | 18:36:23 | MOVE Bench -> Board: Rammus (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Caçador | DA_18_Tristana | -0.2700 |  |
| Jogador 8 | 2-6 | 18:36:23 | MOVE Bench -> Board: Tristana (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Caçador | DA_18_Tristana | 0.0400 |  |
| Jogador 8 | 2-6 | 18:36:24 | MOVE Bench -> Board: Krugue (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Caçador | DA_18_Tristana | -0.7000 |  |
| Jogador 8 | 2-6 | 18:36:24 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Caçador | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 2-6 | 18:36:24 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Caçador | DA_18_Tristana | -0.2700 |  |
| Jogador 8 | 2-6 | 18:36:25 | MOVE Bench -> Board: Krugue (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Caçador | DA_18_Tristana | -0.3400 |  |
| Jogador 8 | 2-6 | 18:36:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Caçador | DA_18_Tristana | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 2-7 | 18:36:31 | MOVE Bench -> Board: Tristana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Caçador | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 2-7 | 18:36:31 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Caçador | DA_18_Tristana | -0.2800 |  |
| Jogador 8 | 2-7 | 18:36:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Caçador | DA_18_Tristana | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-1 | 18:36:38 | MOVE Bench -> Board: Krugue (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Caçador | DA_18_Tristana | -0.2700 |  |
| Jogador 8 | 3-1 | 18:36:38 | MOVE Bench -> Board: Tristana (i:6.0) <-> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Caçador | DA_18_Tristana | 0.1300 |  |
| Jogador 8 | 3-1 | 18:36:39 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Caçador | DA_18_Tristana | -0.4800 |  |
| Jogador 8 | 3-1 | 18:36:39 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Caçador | DA_Brambleback18 | -0.0300 |  |
| Jogador 8 | 3-1 | 18:36:40 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Caçador | DA_Brambleback18 | -0.4700 |  |
| Jogador 8 | 3-1 | 18:36:40 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Caçador | DA_Brambleback18 | -0.3100 |  |
| Jogador 8 | 3-1 | 18:36:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Caçador | DA_Brambleback18 | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-2 | 18:36:45 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Caçador | DA_Brambleback18 | 0.4700 |  |
| Jogador 8 | 3-2 | 18:36:45 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Caçador | DA_Brambleback18 | 0.7200 |  |
| Jogador 8 | 3-2 | 18:36:47 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rubrivira (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Caçador | DA_Brambleback18 | -0.3700 |  |
| Jogador 8 | 3-2 | 18:36:47 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Caçador | DA_Brambleback18 | -0.2400 |  |
| Jogador 8 | 3-2 | 18:36:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Caçador | DA_Brambleback18 | -0.1300 |  |
| Jogador 8 | 3-3 | 18:36:52 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Caçador | DA_Brambleback18 | -0.3500 |  |
| Jogador 8 | 3-3 | 18:36:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 4 | Caçador | DA_Brambleback18 | -0.0700 |  |
| Jogador 8 | 3-3 | 18:36:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 4 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-3 | 18:36:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-3 | 18:36:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 4 | Caçador | DA_Brambleback18 | -0.0800 |  |
| Jogador 8 | 3-3 | 18:36:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 4 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-3 | 18:36:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 4 | Caçador | DA_Brambleback18 | -0.0800 |  |
| Jogador 8 | 3-3 | 18:36:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 4 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-3 | 18:36:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 4 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-3 | 18:36:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 4 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-3 | 18:36:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 4 | Caçador | DA_Brambleback18 | -0.0600 |  |
| Jogador 8 | 3-4 | 18:37:00 | MOVE Bench -> Board: Krugue (i:6.0) <-> Rubrivira (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Caçador | DA_Brambleback18 | -0.6600 |  |
| Jogador 8 | 3-4 | 18:37:00 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Caçador | DA_Brambleback18 | -0.2600 |  |
| Jogador 8 | 3-4 | 18:37:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Caçador | DA_Brambleback18 | -0.0600 |  |
| Jogador 8 | 3-4 | 18:37:05 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Caçador | DA_Brambleback18 | -0.1000 |  |
| Jogador 8 | 3-5 | 18:37:08 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Caçador | DA_Brambleback18 | -0.0500 |  |
| Jogador 8 | 3-5 | 18:37:08 | MOVE Bench -> Board: Malphite (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Caçador | DA_Brambleback18 | -0.2000 |  |
| Jogador 8 | 3-5 | 18:37:08 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Caçador | DA_Brambleback18 | 0.0300 |  |
| Jogador 8 | 3-5 | 18:37:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-5 | 18:37:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 2 | Caçador | DA_Brambleback18 | -0.0900 |  |
| Jogador 8 | 3-5 | 18:37:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 2 | Caçador | DA_Brambleback18 | -0.0100 |  |
| Jogador 8 | 3-5 | 18:37:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 2 | Caçador | DA_Brambleback18 | -0.0100 |  |
| Jogador 8 | 3-5 | 18:37:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 2 | Caçador | DA_Brambleback18 | -0.0900 |  |
| Jogador 8 | 3-5 | 18:37:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 2 | Caçador | DA_Brambleback18 | -0.0100 |  |
| Jogador 8 | 3-5 | 18:37:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 2 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-6 | 18:37:16 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Caçador | DA_Brambleback18 | -0.0900 |  |
| Jogador 8 | 3-6 | 18:37:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Caçador | DA_Brambleback18 | -0.0100 |  |
| Jogador 8 | 3-6 | 18:37:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-7 | 18:37:25 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Caçador | DA_Brambleback18 | 0.1100 |  |
| Jogador 8 | 3-7 | 18:37:25 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Caçador | DA_Brambleback18 | 0.0800 |  |
| Jogador 8 | 3-7 | 18:37:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Caçador | DA_Brambleback18 | 0.6500 |  |
| Jogador 8 | 3-7 | 18:37:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Caçador | DA_Brambleback18 | -0.0100 |  |
| Jogador 8 | 3-7 | 18:37:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Caçador | DA_Brambleback18 | -0.0100 |  |
| Jogador 8 | 3-7 | 18:37:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 4-1 | 18:37:34 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Caçador | DA_Brambleback18 | -0.8400 |  |
| Jogador 8 | 4-1 | 18:37:34 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Caçador | DA_Brambleback18 | 0.1300 |  |
| Jogador 8 | 4-1 | 18:37:34 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Caçador | DA_Brambleback18 | 0.0900 |  |
| Jogador 8 | 4-1 | 18:37:34 | MOVE Bench -> Board: Sivir (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Caçador | DA_Brambleback18 | 0.6400 |  |
| Jogador 8 | 4-1 | 18:37:35 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Caçador | DA_Brambleback18 | 0.2600 |  |
| Jogador 8 | 4-1 | 18:37:35 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 4-2 | 18:37:43 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Caçador | DA_Brambleback18 | -0.0600 |  |
| Jogador 8 | 4-2 | 18:37:43 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 4-3 | 18:37:53 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 0 | Caçador | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 4-4 | 18:38:02 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 1 | Caçador | DA_18_Soraka | 0.5200 |  |
| Jogador 8 | 4-4 | 18:38:03 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 1 | Caçador | DA_18_Soraka | -0.0800 |  |
| Jogador 8 | 4-5 | 18:38:11 | COMPROU: Amumu (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 24 | 1 | Caçador | DA_18_Soraka | -0.1600 |  |
| Jogador 8 | 4-5 | 18:38:11 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 24 | 1 | Caçador | DA_18_Soraka | -0.0900 |  |
| Jogador 8 | 4-6 | 18:38:19 | COMPROU: Ezreal (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 31 | 2 | Caçador | DA_18_Soraka | -0.2200 |  |
| Jogador 8 | 4-6 | 18:38:22 | COMPROU: Nidalee (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 2 | Caçador | DA_18_Soraka | 0.0200 |  |
| Jogador 8 | 4-6 | 18:38:22 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 2 | Caçador | DA_18_Soraka | -0.0900 |  |
| Jogador 8 | 4-7 | 18:38:28 | BIGORNA: escolheu componente TFT_Item_NegatronCloak | WINSTREAK | WINSTREAK: preservar vantagem atual | 37 | 2 | Caçador | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 4-7 | 18:38:29 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 2 | Caçador | DA_18_Lux_Elderwood | -0.1100 |  |
| Jogador 8 | 4-7 | 18:38:29 | COMPROU: Zyra (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 28 | 2 | Caçador | DA_18_Lux_Elderwood | -0.1200 |  |
| Jogador 8 | 4-7 | 18:38:29 | COMPROU: Morgana (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 24 | 2 | Caçador | DA_18_Lux_Elderwood | -0.2100 |  |
| Jogador 8 | 4-7 | 18:38:29 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 24 | 2 | Caçador | DA_18_Lux_Elderwood | -0.0300 |  |
| Jogador 8 | 5-1 | 18:38:37 | VENDEU: Nidalee (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 39 | 2 | Caçador | DA_18_Lux_Elderwood | 0.0500 |  |
| Jogador 8 | 5-1 | 18:38:37 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 36 | 2 | Caçador | DA_18_KhaZix | 0.8600 |  |
| Jogador 8 | 5-1 | 18:38:37 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Rubrivira (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 36 | 2 | Caçador | DA_18_Lux_Elderwood | -0.1000 |  |
| Jogador 8 | 5-1 | 18:38:38 | VENDEU: Zyra (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 40 | 2 | Caçador | DA_18_Lux_Elderwood | 0.1300 |  |
| Jogador 8 | 5-1 | 18:38:38 | COMPROU: Ezreal (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 36 | 2 | Caçador | DA_18_Lux_Elderwood | 0.5400 |  |
| Jogador 8 | 5-1 | 18:38:38 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 36 | 2 | Caçador | DA_18_Lux_Elderwood | 0.2400 |  |
| Jogador 8 | 5-1 | 18:38:38 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 33 | 2 | Caçador | DA_18_Lux_Elderwood | 0.3000 |  |
| Jogador 8 | 5-1 | 18:38:39 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 33 | 2 | Caçador | DA_18_Lux_Elderwood | -0.0400 |  |
| Jogador 8 | 5-1 | 18:38:42 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 33 | 2 | Caçador | DA_18_Lux_Elderwood | 0.5900 |  |
| Jogador 8 | 5-2 | 18:38:46 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 42 | 3 | Caçador | DA_18_Lux_Elderwood | 0.8300 |  |
| Jogador 8 | 5-2 | 18:38:46 | VENDEU: Morgana (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 46 | 3 | Caçador | DA_18_Lux_Elderwood | 0.0800 |  |
| Jogador 8 | 5-2 | 18:38:49 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 3 | Caçador | DA_18_Diana | 0.9500 |  |
| Jogador 8 | 5-2 | 18:38:49 | COMPROU: Hecarim (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 40 | 3 | Caçador | DA_18_Diana | 0.0600 |  |
| Jogador 8 | 5-2 | 18:38:49 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 38 | 3 | Caçador | DA_18_Diana | -0.0100 |  |
| Jogador 8 | 5-2 | 18:38:49 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 38 | 3 | Caçador | DA_18_Diana | -0.0500 |  |
| Jogador 8 | 5-3 | 18:38:56 | VENDEU: LeBlanc (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 52 | 3 | Caçador | DA_18_Diana | 0.0500 |  |
| Jogador 8 | 5-3 | 18:38:56 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 49 | 3 | Caçador | DA_18_Diana | 0.3100 |  |
| Jogador 8 | 5-3 | 18:38:56 | VENDEU: Hecarim (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 52 | 3 | Caçador | DA_18_Diana | 0.1300 |  |
| Jogador 8 | 5-3 | 18:38:56 | COMPROU: Amumu (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 48 | 3 | Caçador | DA_18_Diana | 0.3300 |  |
| Jogador 8 | 5-3 | 18:38:56 | VENDEU: Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 52 | 3 | Caçador | DA_18_Diana | -0.2600 |  |
| Jogador 8 | 5-3 | 18:38:57 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 49 | 3 | Caçador | DA_18_Diana | 0.1000 |  |
| Jogador 8 | 5-3 | 18:38:57 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 47 | 3 | Caçador | DA_18_Diana | -0.1600 |  |
| Jogador 8 | 5-3 | 18:38:57 | VENDEU: Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 51 | 3 | Caçador | DA_18_Diana | 0.1500 |  |
| Jogador 8 | 5-3 | 18:38:57 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 49 | 3 | Caçador | DA_18_Diana | 0.7900 |  |
| Jogador 8 | 5-3 | 18:39:00 | VENDEU: Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 52 | 3 | Caçador | DA_18_Diana | 0.1000 |  |
| Jogador 8 | 5-3 | 18:39:00 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 52 | 3 | Caçador | DA_18_Diana | -0.2400 |  |
| Jogador 8 | 5-4 | 18:39:05 | COMPROU: Ahri (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 61 | 5 | Caçador | DA_18_Diana | -0.2000 |  |
| Jogador 8 | 5-4 | 18:39:05 | VENDEU: Ahri (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 65 | 5 | Caçador | DA_18_Diana | 0.0700 |  |
| Jogador 8 | 5-4 | 18:39:05 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 62 | 5 | Caçador | DA_18_Diana | 0.0200 |  |
| Jogador 8 | 5-4 | 18:39:05 | VENDEU: Kog'Maw (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 65 | 5 | Caçador | DA_18_Diana | 0.0300 |  |
| Jogador 8 | 5-4 | 18:39:05 | COMPROU: Teemo (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 63 | 5 | Caçador | DA_18_Diana | 0.0900 |  |
| Jogador 8 | 5-4 | 18:39:06 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 61 | 5 | Caçador | DA_18_Diana | -0.0900 |  |
| Jogador 8 | 5-4 | 18:39:06 | VENDEU: Teemo (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 63 | 5 | Caçador | DA_18_Diana | 0.0400 |  |
| Jogador 8 | 5-4 | 18:39:06 | COMPROU: Rammus (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 60 | 5 | Caçador | DA_18_Diana | 0.5800 |  |
| Jogador 8 | 5-4 | 18:39:06 | VENDEU: Rammus (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 63 | 5 | Caçador | DA_18_Diana | -0.3400 |  |
| Jogador 8 | 5-4 | 18:39:06 | COMPROU: Rammus (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 60 | 5 | Caçador | DA_18_Diana | 0.5800 |  |
| Jogador 8 | 5-4 | 18:39:09 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 60 | 5 | Caçador | DA_18_Diana | -0.0900 |  |
| Jogador 8 | 5-5 | 18:39:13 | VENDEU: Rammus (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 77 | 5 | Caçador | DA_18_Diana | -0.3400 |  |
| Jogador 8 | 5-5 | 18:39:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 74 | 5 | Caçador | DA_18_Diana | 0.9500 |  |
| Jogador 8 | 5-5 | 18:39:17 | VENDEU: Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 78 | 5 | Caçador | DA_18_Diana | -0.3300 |  |
| Jogador 8 | 5-5 | 18:39:17 | COMPROU: Sivir (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 74 | 5 | Caçador | DA_18_Diana | 0.8900 |  |
| Jogador 8 | 5-5 | 18:39:17 | VENDEU: Soraka (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 78 | 5 | Caçador | DA_18_Diana | 0.0400 |  |
| Jogador 8 | 5-5 | 18:39:17 | COMPROU: Aphelios (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 74 | 5 | Caçador | DA_18_Diana | -0.1500 |  |
| Jogador 8 | 5-5 | 18:39:17 | REROLL | WINSTREAK | WINSTREAK: preservar vantagem atual | 72 | 5 | Caçador | DA_18_Diana | -0.0900 |  |
| Jogador 8 | 5-5 | 18:39:18 | VENDEU: Aphelios (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 76 | 5 | Caçador | DA_18_Diana | 0.0600 |  |
| Jogador 8 | 5-5 | 18:39:18 | COMPROU: Tristana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 73 | 5 | Caçador | DA_18_Diana | 1.0000 |  |
| Jogador 8 | 5-5 | 18:39:18 | COMPROU: Grompe (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 71 | 5 | Caçador | DA_18_Diana | 0.1800 |  |
| Jogador 8 | 5-5 | 18:39:19 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 71 | 5 | Caçador | DA_18_Diana | -0.1000 |  |
| Jogador 8 | 5-6 | 18:39:25 | VENDEU: Grompe (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 83 | 5 | Caçador | DA_18_Diana | 0.0400 |  |
| Jogador 8 | 5-6 | 18:39:25 | COMPROU: Amumu (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 79 | 5 | Caçador | DA_Amumu18 | 0.8400 |  |
| Jogador 8 | 5-6 | 18:39:26 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 78 | 5 | Caçador | DA_Amumu18 | 0.3900 |  |
| Jogador 8 | 5-6 | 18:39:26 | COMPROU: Morgana (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 74 | 5 | Caçador | DA_Amumu18 | -0.1700 |  |
| Jogador 8 | 5-6 | 18:39:26 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 72 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 5-6 | 18:39:26 | VENDEU: Kha'Zix (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 80 | 5 | Caçador | DA_Amumu18 | 0.0100 |  |
| Jogador 8 | 5-6 | 18:39:26 | COMPROU: Rammus (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 77 | 5 | Caçador | DA_Amumu18 | 0.4200 |  |
| Jogador 8 | 5-6 | 18:39:26 | VENDEU: Morgana (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 81 | 5 | Caçador | DA_Amumu18 | 0.0700 |  |
| Jogador 8 | 5-6 | 18:39:27 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 77 | 5 | Caçador | DA_Amumu18 | 0.0100 |  |
| Jogador 8 | 5-6 | 18:39:30 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 75 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 5-6 | 18:39:30 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 75 | 5 | Caçador | DA_Amumu18 | -0.1100 |  |
| Jogador 8 | 5-7 | 18:39:34 | BIGORNA: escolheu item completo TFT_Item_LastWhisper | ECON | ECON: manter reserva de 50 e gastar excedente útil | 85 | 5 | Caçador | DA_Amumu18 | 0.0000 |  |
| Jogador 8 | 5-7 | 18:39:34 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Malphite (i:8.0) (tabuleiro slot 10) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 85 | 5 | Caçador | DA_Amumu18 | 0.0900 |  |
| Jogador 8 | 5-7 | 18:39:34 | VENDEU: Ezreal (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 89 | 5 | Caçador | DA_Amumu18 | 0.0600 |  |
| Jogador 8 | 5-7 | 18:39:34 | COMPROU: Krugue (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 86 | 5 | Caçador | DA_Amumu18 | 0.1600 |  |
| Jogador 8 | 5-7 | 18:39:37 | REROLL | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 5-7 | 18:39:37 | VENDEU: Krugue (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 87 | 5 | Caçador | DA_Amumu18 | 0.0300 |  |
| Jogador 8 | 5-7 | 18:39:38 | COMPROU: Amumu (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 83 | 5 | Caçador | DA_Amumu18 | 0.2400 |  |
| Jogador 8 | 5-7 | 18:39:38 | VENDEU: Rammus (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 86 | 5 | Caçador | DA_Amumu18 | -0.3100 |  |
| Jogador 8 | 5-7 | 18:39:38 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Caçador | DA_Amumu18 | 1.0500 |  |
| Jogador 8 | 5-7 | 18:39:38 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 80 | 5 | Caçador | DA_Amumu18 | 0.0100 |  |
| Jogador 8 | 5-7 | 18:39:38 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 80 | 5 | Caçador | DA_Amumu18 | -0.1200 |  |
| Jogador 8 | 6-1 | 18:39:45 | VENDEU: Lobo Trevoguari (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Caçador | DA_Amumu18 | -0.4200 |  |
| Jogador 8 | 6-1 | 18:39:45 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Caçador | DA_Amumu18 | 0.2100 |  |
| Jogador 8 | 6-1 | 18:39:45 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Caçador | DA_Amumu18 | 0.0200 |  |
| Jogador 8 | 6-1 | 18:39:45 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Caçador | DA_Amumu18 | 0.2100 |  |
| Jogador 8 | 6-1 | 18:39:46 | REROLL | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 6-1 | 18:39:46 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Caçador | DA_Amumu18 | 0.0200 |  |
| Jogador 8 | 6-1 | 18:39:46 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Caçador | DA_Amumu18 | 0.9200 |  |
| Jogador 8 | 6-1 | 18:39:46 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Caçador | DA_Amumu18 | 0.0600 |  |
| Jogador 8 | 6-1 | 18:39:46 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Caçador | DA_Amumu18 | -0.1300 |  |
| Jogador 8 | 6-1 | 18:39:50 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Caçador | DA_Amumu18 | 0.3900 |  |
| Jogador 8 | 6-1 | 18:39:50 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Caçador | DA_Amumu18 | -0.3100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 6-2 | 18:39:54 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Caçador | DA_Amumu18 | 0.0100 |  |
| Jogador 8 | 6-2 | 18:39:54 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Caçador | DA_Amumu18 | 0.0600 |  |
| Jogador 8 | 6-2 | 18:39:54 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Caçador | DA_Amumu18 | 0.4200 |  |
| Jogador 8 | 6-2 | 18:39:58 | REROLL | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 6-2 | 18:39:58 | REROLL | STABILIZE | STABILIZE: pressão de vida | 95 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 6-2 | 18:39:58 | REROLL | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 6-2 | 18:39:58 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Caçador | DA_Amumu18 | 0.0400 |  |
| Jogador 8 | 6-2 | 18:39:58 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Caçador | DA_18_Diana | 1.0100 |  |
| Jogador 8 | 6-2 | 18:39:59 | REROLL | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Caçador | DA_18_Diana | -0.0900 |  |
| Jogador 8 | 6-2 | 18:39:59 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Caçador | DA_Amumu18 | -0.4900 |  |
| Jogador 8 | 6-2 | 18:39:59 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Caçador | DA_Amumu18 | -0.3600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 6-3 | 18:40:06 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Caçador | DA_Amumu18 | 1.0700 |  |
| Jogador 8 | 6-3 | 18:40:06 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Caçador | DA_Amumu18 | 0.7800 |  |
| Jogador 8 | 6-3 | 18:40:06 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Caçador | DA_Amumu18 | -0.4600 |  |
| Jogador 8 | 6-3 | 18:40:06 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Caçador | DA_Amumu18 | 0.9600 |  |
| Jogador 8 | 6-3 | 18:40:06 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 6-3 | 18:40:07 | VENDEU: Tristana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Caçador | DA_Amumu18 | -0.5000 |  |
| Jogador 8 | 6-3 | 18:40:07 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Caçador | DA_Amumu18 | -0.0400 |  |
| Jogador 8 | 6-3 | 18:40:07 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Caçador | DA_Amumu18 | 0.0400 |  |
| Jogador 8 | 6-3 | 18:40:07 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Caçador | DA_Amumu18 | 0.1800 |  |
| Jogador 8 | 6-3 | 18:40:11 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Caçador | DA_Amumu18 | -0.0900 |  |
| Jogador 8 | 6-3 | 18:40:11 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Caçador | DA_Amumu18 | -0.2900 |  |
| Jogador 8 | 6-4 | 18:40:15 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Caçador | DA_Amumu18 | 0.0200 |  |
| Jogador 8 | 6-4 | 18:40:15 | COMPROU: Lux (Inferno) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Caçador | DA_Amumu18 | -0.0500 |  |
| Jogador 8 | 6-4 | 18:40:19 | VENDEU: Amumu (i:16.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Caçador | DA_18_Lux_Elderwood | -0.3700 |  |
| Jogador 8 | 6-4 | 18:40:19 | COMPROU: Lux (Congregação das Bruxas) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Caçador | DA_18_Lux_Elderwood | -0.0400 |  |
| Jogador 8 | 6-4 | 18:40:19 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Caçador | DA_18_Lux_Elderwood | 0.0600 |  |
| Jogador 8 | 6-4 | 18:40:20 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Caçador | DA_18_Lux_Elderwood | 0.1200 |  |
| Jogador 8 | 6-4 | 18:40:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Caçador | DA_18_Lux_Elderwood | -0.0900 |  |
| Jogador 8 | 6-4 | 18:40:20 | VENDEU: Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Caçador | DA_18_Lux_Elderwood | 0.0400 |  |
| Jogador 8 | 6-4 | 18:40:20 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Caçador | DA_18_Lux_Elderwood | 0.3100 |  |
| Jogador 8 | 6-4 | 18:40:21 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Caçador | DA_18_Lux_Elderwood | -0.2300 |  |
| Jogador 8 | 6-4 | 18:40:21 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Caçador | DA_18_Lux_Elderwood | -0.4700 |  |
| Jogador 8 | 6-5 | 18:40:28 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Caçador | DA_18_Lux_Elderwood | 0.3900 |  |
| Jogador 8 | 6-5 | 18:40:28 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Caçador | DA_18_Lux_Elderwood | 0.0800 |  |
| Jogador 8 | 6-5 | 18:40:28 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Caçador | DA_18_Lux_Elderwood | -0.0700 |  |
| Jogador 8 | 6-5 | 18:40:28 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Caçador | DA_18_Lux_Elderwood | -0.0900 |  |
| Jogador 8 | 6-5 | 18:40:29 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Caçador | DA_18_Lux_Elderwood | 0.0400 |  |
| Jogador 8 | 6-5 | 18:40:29 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Caçador | DA_18_Sivir | 1.0700 |  |
| Jogador 8 | 6-5 | 18:40:29 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Caçador | DA_18_Sivir | 1.0700 |  |
| Jogador 8 | 6-5 | 18:40:29 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Caçador | DA_18_Sivir | 0.3600 |  |
| Jogador 8 | 6-5 | 18:40:30 | MOVE Bench -> Board: Caitlyn (i:4.0) <-> Lux (Sabugueiro) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Caçador | DA_18_Sivir | 0.2000 |  |
| Jogador 8 | 6-5 | 18:40:33 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Caçador | DA_18_Sivir | 0.0900 |  |
| Jogador 8 | 6-5 | 18:40:33 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Caçador | DA_18_Sivir | -0.4700 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 27 | 47 | 235 | 27 | 10 | 193 | 22 | 3 |
| Jogador 2 | 38 | 45 | 225 | 38 | 28 | 243 | 20 | 10 |
| Jogador 3 | 28 | 28 | 140 | 28 | 18 | 162 | 15 | 5 |
| Jogador 4 | 26 | 39 | 195 | 26 | 9 | 192 | 20 | 4 |
| Jogador 5 | 30 | 42 | 210 | 30 | 21 | 186 | 19 | 4 |
| Jogador 6 | 27 | 54 | 270 | 27 | 17 | 190 | 11 | 4 |
| Jogador 7 | 23 | 44 | 220 | 23 | 13 | 155 | 6 | 6 |
| Jogador 8 | 38 | 53 | 265 | 38 | 21 | 266 | 25 | 5 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 193 | 193 | 193 | 0 | 190 | 0 | 193 | 193 | 193 | 43/28 |
| Jogador 2 | 243 | 243 | 243 | 0 | 239 | 0 | 243 | 243 | 243 | 70/55 |
| Jogador 3 | 162 | 162 | 162 | 0 | 160 | 0 | 162 | 162 | 162 | 21/4 |
| Jogador 4 | 192 | 192 | 192 | 0 | 190 | 0 | 192 | 192 | 192 | 47/32 |
| Jogador 5 | 186 | 186 | 186 | 0 | 184 | 0 | 186 | 186 | 186 | 48/34 |
| Jogador 6 | 190 | 190 | 190 | 0 | 188 | 0 | 190 | 190 | 190 | 46/31 |
| Jogador 7 | 155 | 155 | 155 | 0 | 155 | 0 | 155 | 155 | 155 | 44/30 |
| Jogador 8 | 266 | 266 | 266 | 0 | 262 | 0 | 266 | 266 | 266 | 79/66 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5151995420455933 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37528008222579956 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.26821237802505493 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 62 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21567106246948242 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7556446194648743 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6337111592292786 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | -0.21332567930221558 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 67 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 92 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0420702695846558 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2325429618358612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 94 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 122 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27275240421295166 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 123 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0553484670817852 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 124 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2781783640384674 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 125 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23285172879695892 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 126 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 127 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 128 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 129 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 148 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4424682855606079 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 149 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2834046185016632 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 150 | PASS | STABILIZE | 100.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 172 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 12 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23269730806350708 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 173 | SELL | STABILIZE | 95.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4258813261985779 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 2-3 | 174 | BUY | STABILIZE | 95.0 | 4 | 14 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.008753776550293 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -— |
| Jogador 1 | 2-3 | 175 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3612024784088135 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 176 | BUY_XP | STABILIZE | 95.0 | 4 | 12 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058435000479221344 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 177 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500970363616943 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 178 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 179 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5305014848709106 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 180 | BUY | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29746758937835693 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 181 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31088852882385254 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 182 | PASS | SLOWROLL | 95.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 201 | SELL | SLOWROLL | 95.0 | 5 | 12 | 1 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8724825978279114 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 2-4 | 202 | BUY | SLOWROLL | 95.0 | 5 | 13 | 1 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2990299165248871 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 203 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 10 | 1 | 16.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4188394546508789 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 204 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 10 | 1 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22334913909435272 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 205 | PASS | SLOWROLL | 95.0 | 5 | 10 | 1 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 227 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 16 | 1 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27999061346054077 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 228 | SELL | SLOWROLL | 95.0 | 5 | 16 | 1 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4923838973045349 | 0.0 | 0.0 | +— / -d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 2-5 | 229 | BUY | SLOWROLL | 95.0 | 5 | 19 | 1 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9884387254714966 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 230 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 17 | 1 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09937315434217453 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 231 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 17 | 1 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6386682987213135 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 232 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 17 | 1 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 233 | PASS | SLOWROLL | 95.0 | 5 | 17 | 1 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020357143133878708 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 252 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 23 | 2 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09937488287687302 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 253 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 23 | 2 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6386258602142334 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 254 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 23 | 2 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09430007636547089 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 255 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 23 | 2 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 256 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 23 | 2 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6264946460723877 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 257 | PASS | SLOWROLL | 90.0 | 5 | 23 | 2 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02142857201397419 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 276 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 31 | 3 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09384401887655258 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 277 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 31 | 3 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 278 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 31 | 3 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6269256472587585 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 279 | PASS | SLOWROLL | 90.0 | 5 | 31 | 3 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037857141345739365 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 302 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 39 | 3 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 303 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 39 | 3 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09348367899656296 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 304 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 39 | 3 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 305 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 39 | 3 | 16.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6258804202079773 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 306 | PASS | SLOWROLL | 90.0 | 5 | 39 | 3 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10999999940395355 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 327 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 50 | 5 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09399271011352539 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 328 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 50 | 5 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 329 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 50 | 5 | 16.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08786242455244064 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 330 | SELL | SLOWROLL | 90.0 | 5 | 50 | 5 | 18.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0046819294802844524 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 3-2 | 331 | BUY | SLOWROLL | 90.0 | 5 | 51 | 5 | 18.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3729189336299896 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 332 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 47 | 4 | 18.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.533181369304657 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 333 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 47 | 4 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6030027270317078 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 334 | PASS | SLOWROLL | 90.0 | 5 | 47 | 4 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11400000005960464 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 349 | MOVE_BENCH | SLOWROLL | 80.0 | 5 | 56 | 5 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2333914041519165 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 350 | MOVE_BENCH | SLOWROLL | 80.0 | 5 | 56 | 5 | 18.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5328404307365417 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 351 | MOVE_BENCH | SLOWROLL | 80.0 | 5 | 56 | 5 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6028380990028381 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 352 | PASS | SLOWROLL | 80.0 | 5 | 56 | 5 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12487752735614777 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 371 | MOVE_BENCH | SLOWROLL | 80.0 | 5 | 67 | 5 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 372 | MOVE_BENCH | SLOWROLL | 80.0 | 5 | 67 | 5 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09499543160200119 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 373 | MOVE_BENCH | SLOWROLL | 80.0 | 5 | 67 | 5 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2310526967048645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 374 | BUY | SLOWROLL | 80.0 | 5 | 67 | 5 | 18.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32700273394584656 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 1 | 3-4 | 375 | BUY_XP | SLOWROLL | 80.0 | 5 | 66 | 5 | 18.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.221670001745224 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 376 | MOVE_BENCH | SLOWROLL | 80.0 | 6 | 62 | 5 | 18.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4838011562824249 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 377 | MOVE_BENCH | SLOWROLL | 80.0 | 6 | 62 | 5 | 16.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08735521137714386 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 378 | MOVE_BENCH | SLOWROLL | 80.0 | 6 | 62 | 5 | 16.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25011885166168213 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 379 | MOVE_BENCH | SLOWROLL | 80.0 | 6 | 62 | 5 | 18.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48311498761177063 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 380 | PASS | SLOWROLL | 80.0 | 6 | 62 | 5 | 16.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12759634852409363 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 389 | MOVE_BENCH | SLOWROLL | 80.0 | 6 | 62 | 5 | 16.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3305797874927521 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 392 | BUY | SLOWROLL | 80.0 | 6 | 72 | 5 | 24.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9419623613357544 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 393 | MOVE_BENCH | SLOWROLL | 80.0 | 6 | 70 | 5 | 20.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24067272245883942 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 394 | MOVE_BENCH | SLOWROLL | 80.0 | 6 | 70 | 5 | 24.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12868058681488037 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 395 | BUY_XP | FAST8 | 80.0 | 6 | 70 | 5 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 396 | BUY_XP | FAST8 | 80.0 | 6 | 66 | 5 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 397 | BUY_XP | FAST8 | 80.0 | 6 | 62 | 5 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 398 | BUY_XP | FAST8 | 80.0 | 6 | 58 | 5 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 399 | BUY_XP | FAST8 | 80.0 | 6 | 54 | 5 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 400 | BUY_XP | FAST8 | 80.0 | 6 | 50 | 5 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 401 | BUY_XP | FAST8 | 80.0 | 6 | 46 | 4 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02355000004172325 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 402 | PASS | FAST8 | 80.0 | 6 | 42 | 4 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1289999932050705 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 412 | BUY | FAST8 | 70.0 | 6 | 51 | 5 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2889918386936188 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 413 | BUY | FAST8 | 70.0 | 6 | 49 | 4 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8049927949905396 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 414 | BUY | FAST8 | 70.0 | 6 | 47 | 4 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8337679505348206 | 0.0 | 0.0 | +da5abe09-7f54-4361-8d82-84427a9da9e1 / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f,ff10e482-7085-4e73-8a0c-fdd3f4938128 |
| Jogador 1 | 3-6 | 415 | MOVE_BENCH | SLOWROLL | 70.0 | 6 | 45 | 4 | 18.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5681386590003967 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 416 | MOVE_BENCH | SLOWROLL | 70.0 | 6 | 45 | 4 | 14.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3923915922641754 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 417 | MOVE_BENCH | SLOWROLL | 70.0 | 6 | 45 | 4 | 22.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29685792326927185 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 418 | MOVE_BENCH | FAST8 | 70.0 | 6 | 45 | 4 | 26.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4473908245563507 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 419 | MOVE_BOARD | FAST8 | 70.0 | 6 | 45 | 4 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010986327193677425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 420 | MOVE_BOARD | FAST8 | 70.0 | 6 | 45 | 4 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059659093618392944 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 421 | BUY_XP | FAST8 | 70.0 | 6 | 45 | 4 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08250000327825546 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 422 | PASS | FAST8 | 70.0 | 7 | 41 | 4 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12849999964237213 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 432 | BUY | FAST8 | 59.0 | 7 | 51 | 5 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1528448462486267 | 0.0 | 0.0 | +89cec488-9a0e-4838-b486-2504a0742476 / -— |
| Jogador 1 | 3-7 | 433 | BUY | FAST8 | 59.0 | 7 | 46 | 4 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25222229957580566 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 1 | 3-7 | 434 | MOVE_BENCH | FAST8 | 59.0 | 7 | 43 | 4 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06221483647823334 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 435 | BUY | FAST8 | 59.0 | 7 | 43 | 4 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24548767507076263 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 1 | 3-7 | 436 | MOVE_BENCH | FAST8 | 59.0 | 7 | 40 | 4 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4870935082435608 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 437 | BUY_XP | FAST8 | 59.0 | 7 | 40 | 4 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08327499777078629 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 438 | BUY_XP | FAST8 | 59.0 | 7 | 36 | 3 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003275000024586916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 439 | BUY_XP | FAST8 | 59.0 | 7 | 32 | 3 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08327499777078629 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 440 | BUY_XP | FAST8 | 59.0 | 7 | 28 | 2 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003275000024586916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 441 | BUY_XP | FAST8 | 59.0 | 7 | 24 | 2 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003275000024586916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 442 | PASS | FAST8 | 59.0 | 7 | 20 | 2 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05849999934434891 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 452 | BUY | FAST8 | 59.0 | 7 | 28 | 2 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05756345018744469 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -— |
| Jogador 1 | 4-1 | 453 | BUY | FAST8 | 59.0 | 7 | 25 | 2 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05877860262989998 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -— |
| Jogador 1 | 4-1 | 454 | BUY | FAST8 | 59.0 | 7 | 22 | 2 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6780356764793396 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -— |
| Jogador 1 | 4-1 | 455 | BUY | FAST8 | 59.0 | 7 | 19 | 1 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.003805263200774789 | 0.0 | 0.0 | +3fdd5708-2e07-4636-a598-d872f57e1c16 / -— |
| Jogador 1 | 4-1 | 456 | BUY | FAST8 | 59.0 | 7 | 16 | 1 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07728111743927002 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 1 | 4-1 | 457 | CRAFT_AND_EQUIP | FAST8 | 59.0 | 7 | 13 | 1 | 46.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2213936448097229 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 458 | PASS | FAST8 | 59.0 | 7 | 13 | 1 | 46.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 472 | BUY | FAST8 | 59.0 | 7 | 20 | 2 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6817496418952942 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 1 | 4-2 | 473 | REROLL | FAST8 | 59.0 | 7 | 19 | 1 | 46.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 474 | REROLL | FAST8 | 59.0 | 7 | 17 | 1 | 46.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 475 | SELL | FAST8 | 59.0 | 7 | 15 | 1 | 46.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052569229155778885 | 0.0 | 0.0 | +— / -c617e958-b482-40ce-ab24-acff4dc48bc0 |
| Jogador 1 | 4-2 | 476 | BUY | FAST8 | 59.0 | 7 | 18 | 1 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7562451362609863 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5,9cb61b5c-2c8a-43a2-a854-517f4377f6db |
| Jogador 1 | 4-2 | 477 | BUY | FAST8 | 59.0 | 7 | 15 | 1 | 46.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7329080700874329 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 1 | 4-2 | 478 | BUY | FAST8 | 59.0 | 7 | 12 | 1 | 46.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41854628920555115 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 1 | 4-2 | 479 | REROLL | FAST8 | 59.0 | 7 | 9 | 0 | 46.0 | Inferno/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 480 | SELL | FAST8 | 59.0 | 7 | 7 | 0 | 46.0 | Inferno/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12891075015068054 | 0.0 | 0.0 | +— / -b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 1 | 4-2 | 481 | BUY | FAST8 | 59.0 | 7 | 10 | 1 | 46.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01876818761229515 | 0.0 | 0.0 | +9cc98c55-1b3a-4b31-ae06-f66098e86e8f / -— |
| Jogador 1 | 4-2 | 482 | PASS | FAST8 | 59.0 | 7 | 6 | 0 | 46.0 | Inferno/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 492 | REROLL | FAST8 | 47.0 | 7 | 11 | 1 | 46.0 | Inferno/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 493 | SELL | FAST8 | 47.0 | 7 | 9 | 0 | 46.0 | Inferno/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26878461241722107 | 0.0 | 0.0 | +— / -5f9e16e2-0766-403f-a85a-f6a735c04261 |
| Jogador 1 | 4-3 | 494 | BUY | FAST8 | 47.0 | 7 | 12 | 1 | 46.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6508724093437195 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -— |
| Jogador 1 | 4-3 | 495 | REROLL | FAST8 | 47.0 | 7 | 9 | 0 | 46.0 | Inferno/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 496 | SELL | FAST8 | 47.0 | 7 | 7 | 0 | 46.0 | Inferno/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11853846162557602 | 0.0 | 0.0 | +— / -3fdd5708-2e07-4636-a598-d872f57e1c16 |
| Jogador 1 | 4-3 | 497 | BUY | FAST8 | 47.0 | 7 | 10 | 1 | 46.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6827069520950317 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -891aea62-e06a-46d4-8250-a3d4a56e847d,d1bc6c5b-74a5-46db-b00f-e91265546f5d |
| Jogador 1 | 4-3 | 498 | BUY | FAST8 | 47.0 | 7 | 7 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27446597814559937 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -— |
| Jogador 1 | 4-3 | 499 | BUY | FAST8 | 47.0 | 7 | 3 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24409808218479156 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 1 | 4-3 | 500 | PASS | FAST8 | 47.0 | 7 | 0 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 512 | SELL | STABILIZE | 36.0 | 7 | 6 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07103076577186584 | 0.0 | 0.0 | +— / -1388df2e-8cb4-4e29-8b30-776c29406917 |
| Jogador 1 | 4-4 | 513 | BUY | STABILIZE | 36.0 | 7 | 9 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03764054551720619 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 1 | 4-4 | 514 | REROLL | STABILIZE | 36.0 | 7 | 5 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 515 | SELL | STABILIZE | 36.0 | 7 | 3 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08226153999567032 | 0.0 | 0.0 | +— / -6722b147-c2a7-4fd0-a943-5036adb3e3a1 |
| Jogador 1 | 4-4 | 516 | BUY | STABILIZE | 36.0 | 7 | 7 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28392651677131653 | 0.0 | 0.0 | +99857cfa-b422-4167-bb01-d9fd94a55d88 / -— |
| Jogador 1 | 4-4 | 517 | SELL | STABILIZE | 36.0 | 7 | 4 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06379999965429306 | 0.0 | 0.0 | +— / -5754c4b4-0a7d-49e5-93e4-b144c3090a41 |
| Jogador 1 | 4-4 | 518 | BUY | STABILIZE | 36.0 | 7 | 8 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359864354133606 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-4 | 519 | BUY | STABILIZE | 36.0 | 7 | 6 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2803831994533539 | 0.0 | 0.0 | +4432f76a-94cc-4a96-b72b-1cf35b310dca / -— |
| Jogador 1 | 4-4 | 520 | REROLL | STABILIZE | 36.0 | 7 | 2 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 521 | PASS | STABILIZE | 36.0 | 7 | 0 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 532 | REROLL | STABILIZE | 36.0 | 7 | 6 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 533 | REROLL | STABILIZE | 36.0 | 7 | 4 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 534 | REROLL | STABILIZE | 36.0 | 7 | 2 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 535 | SELL | STABILIZE | 36.0 | 7 | 0 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4221692383289337 | 0.0 | 0.0 | +— / -734c25e1-eddf-4452-a04a-1b39db3b94d0 |
| Jogador 1 | 4-5 | 536 | BUY | STABILIZE | 36.0 | 7 | 8 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.285987913608551 | 0.0 | 0.0 | +8068dc77-9528-4a1d-b4dc-5ac216e8684f / -— |
| Jogador 1 | 4-5 | 537 | REROLL | STABILIZE | 36.0 | 7 | 6 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 538 | SELL | STABILIZE | 36.0 | 7 | 4 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8550000190734863 | 0.0 | 0.0 | +— / -3658b5d8-450f-451a-8487-5b3bdd7c385b |
| Jogador 1 | 4-5 | 539 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 7 | 9 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13401198387145996 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 540 | BUY | STABILIZE | 36.0 | 7 | 9 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.79662024974823 | 0.0 | 0.0 | +f9820f05-e1b0-4953-a98d-3ae191b1249a / -— |
| Jogador 1 | 4-5 | 541 | REROLL | STABILIZE | 36.0 | 7 | 5 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 542 | PASS | STABILIZE | 36.0 | 7 | 3 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 551 | SELL | STABILIZE | 23.0 | 7 | 9 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025646153837442398 | 0.0 | 0.0 | +— / -4432f76a-94cc-4a96-b72b-1cf35b310dca |
| Jogador 1 | 4-6 | 552 | BUY | STABILIZE | 23.0 | 7 | 13 | 1 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8039174675941467 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -— |
| Jogador 1 | 4-6 | 553 | SELL | STABILIZE | 23.0 | 7 | 10 | 1 | 42.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4095846116542816 | 0.0 | 0.0 | +— / -7a60e1b2-fc20-4070-b163-2f9fb6f93264 |
| Jogador 1 | 4-6 | 554 | BUY | STABILIZE | 23.0 | 7 | 11 | 1 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7529329657554626 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -45da6d00-829e-4e2e-a1a5-318498fd007b,665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 1 | 4-6 | 555 | BUY | STABILIZE | 23.0 | 7 | 8 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17288489639759064 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -— |
| Jogador 1 | 4-6 | 556 | MOVE_BENCH | STABILIZE | 23.0 | 7 | 6 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29663702845573425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 557 | BUY | STABILIZE | 23.0 | 7 | 6 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2800690531730652 | 0.0 | 0.0 | +d79de824-d9b2-4dfb-a7be-a359b416aea1 / -— |
| Jogador 1 | 4-6 | 558 | REROLL | STABILIZE | 23.0 | 7 | 2 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 559 | MOVE_BENCH | STABILIZE | 23.0 | 7 | 0 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.602985143661499 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 560 | PASS | STABILIZE | 23.0 | 7 | 0 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 570 | BUY | ALL_IN | 11.0 | 7 | 6 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27392953634262085 | 0.0 | 0.0 | +a960f5cb-d806-4d73-9146-244e1ecde6f2 / -— |
| Jogador 1 | 4-7 | 571 | REROLL | ALL_IN | 11.0 | 7 | 3 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 572 | PASS | ALL_IN | 11.0 | 7 | 1 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 582 | ANVIL_CHOICE | ALL_IN | 11.0 | 7 | 7 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 583 | REROLL | ALL_IN | 11.0 | 7 | 7 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 584 | REROLL | ALL_IN | 11.0 | 7 | 5 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 585 | SELL | ALL_IN | 11.0 | 7 | 3 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0228769239038229 | 0.0 | 0.0 | +— / -dc423197-9320-4651-b71d-a62086416f9d |
| Jogador 1 | 5-1 | 586 | BUY | ALL_IN | 11.0 | 7 | 5 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7939307689666748 | 0.0 | 0.0 | +45a43922-1521-4147-be21-d34b3e573cf5 / -— |
| Jogador 1 | 5-1 | 587 | REROLL | ALL_IN | 11.0 | 7 | 2 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 588 | PASS | ALL_IN | 11.0 | 7 | 0 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 601 | REROLL | ALL_IN | 11.0 | 7 | 6 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 602 | REROLL | ALL_IN | 11.0 | 7 | 4 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 603 | REROLL | ALL_IN | 11.0 | 7 | 2 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 604 | PASS | ALL_IN | 11.0 | 7 | 0 | 0 | 56.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3124316334724426 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5974857807159424 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35926106572151184 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.25888845324516296 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5669147372245789 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 62 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.24529090523719788 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3570922017097473 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 64 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 92 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 122 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3216458857059479 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 123 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5798891186714172 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 124 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0389384031295776 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 125 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 126 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004513553809374571 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 127 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28234025835990906 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 128 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 148 | BUY_XP | STABILIZE | 100.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 149 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4255598783493042 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 150 | BUY | SLOWROLL | 100.0 | 5 | 4 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02002333104610443 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 151 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32181259989738464 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 152 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3904915153980255 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 153 | PASS | SLOWROLL | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 172 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059892382472753525 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 173 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 9 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3218534290790558 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 174 | PASS | SLOWROLL | 100.0 | 5 | 9 | 0 | 12.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 201 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 14 | 1 | 12.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3495677411556244 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 202 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 14 | 1 | 14.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6208499670028687 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 203 | PASS | SLOWROLL | 94.0 | 5 | 14 | 1 | 14.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 227 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 20 | 2 | 14.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3661489486694336 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 228 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 20 | 2 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3238196074962616 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 229 | PASS | SLOWROLL | 94.0 | 5 | 20 | 2 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020892856642603874 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 252 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 28 | 2 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.390815794467926 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 253 | BUY | SLOWROLL | 94.0 | 5 | 28 | 2 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9743374586105347 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 254 | BUY_XP | SLOWROLL | 94.0 | 5 | 26 | 2 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 255 | BUY_XP | SLOWROLL | 94.0 | 5 | 22 | 2 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 256 | BUY_XP | SLOWROLL | 94.0 | 5 | 18 | 1 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011409999802708626 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 257 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 14 | 1 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 258 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 14 | 1 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022827258333563805 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 259 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 14 | 1 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3238380551338196 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 260 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 14 | 1 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.555854856967926 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 261 | BUY_XP | SLOWROLL | 94.0 | 6 | 14 | 1 | 18.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 262 | PASS | SLOWROLL | 94.0 | 6 | 10 | 1 | 18.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 276 | BUY | SLOWROLL | 94.0 | 6 | 18 | 1 | 18.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14123544096946716 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 277 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 14 | 1 | 18.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40457528829574585 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 278 | BUY_XP | SLOWROLL | 94.0 | 6 | 14 | 1 | 22.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 279 | BUY_XP | SLOWROLL | 94.0 | 6 | 10 | 1 | 22.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 280 | BUY_XP | SLOWROLL | 94.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 281 | MOVE_BOARD | SLOWROLL | 94.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05607267841696739 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 282 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3248603940010071 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 283 | SELL | SLOWROLL | 94.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8520264625549316 | 0.0 | 0.0 | +— / -94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 2-7 | 284 | SELL | SLOWROLL | 94.0 | 6 | 3 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47725924849510193 | 0.0 | 0.0 | +— / -292ef825-d326-4dd8-9c42-c47cfc62116f |
| Jogador 2 | 2-7 | 285 | BUY | SLOWROLL | 94.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29369768500328064 | 0.0 | 0.0 | +068d0768-4134-4a5f-a132-0642c23d91e1 / -— |
| Jogador 2 | 2-7 | 286 | PASS | SLOWROLL | 94.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 302 | SELL | SLOWROLL | 94.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3388069272041321 | 0.0 | 0.0 | +— / -068d0768-4134-4a5f-a132-0642c23d91e1 |
| Jogador 2 | 3-1 | 303 | BUY | SLOWROLL | 94.0 | 6 | 10 | 1 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3326255679130554 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 304 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 7 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35376250743865967 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 305 | MOVE_BENCH | FAST8 | 94.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09837432205677032 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 306 | BUY_XP | FAST8 | 94.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 307 | PASS | FAST8 | 94.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 327 | SELL | FAST8 | 94.0 | 6 | 10 | 1 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8921291828155518 | 0.0 | 0.0 | +— / -5a1572b3-8b27-4d87-b885-f342b91c0854 |
| Jogador 2 | 3-2 | 328 | BUY | FAST8 | 94.0 | 6 | 11 | 1 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21753652393817902 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 329 | BUY_XP | FAST8 | 94.0 | 6 | 10 | 1 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 330 | BUY_XP | FAST8 | 94.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 331 | PASS | FAST8 | 94.0 | 6 | 2 | 0 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 349 | BUY | FAST8 | 94.0 | 7 | 9 | 0 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21033620834350586 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 350 | MOVE_BENCH | FAST8 | 94.0 | 7 | 5 | 0 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3050816059112549 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 351 | MOVE_BENCH | FAST8 | 94.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5549943447113037 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 352 | BUY_XP | FAST8 | 94.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 353 | PASS | FAST8 | 94.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 371 | SELL | FAST8 | 94.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39865249395370483 | 0.0 | 0.0 | +— / -584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 3-4 | 372 | BUY | FAST8 | 94.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.007332168985158205 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 373 | MOVE_BENCH | FAST8 | 94.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3206930160522461 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 374 | MOVE_BENCH | FAST8 | 94.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09993069618940353 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 375 | MOVE_BENCH | FAST8 | 94.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8224202394485474 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 376 | MOVE_BENCH | FAST8 | 94.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32049626111984253 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 377 | PASS | FAST8 | 94.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 392 | MOVE_BENCH | FAST8 | 94.0 | 7 | 14 | 1 | 34.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09992986172437668 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 393 | MOVE_BENCH | FAST8 | 94.0 | 7 | 14 | 1 | 36.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3537610173225403 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 394 | BUY_XP | FAST8 | 94.0 | 7 | 14 | 1 | 38.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 395 | BUY_XP | FAST8 | 94.0 | 7 | 10 | 1 | 38.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 396 | BUY_XP | FAST8 | 94.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 397 | MOVE_BENCH | FAST8 | 94.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052235763520002365 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 398 | PASS | FAST8 | 94.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 412 | SELL | FAST8 | 83.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035331182181835175 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 3-6 | 413 | BUY | FAST8 | 83.0 | 7 | 9 | 0 | 38.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7656534910202026 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -6f3f86ec-6928-4032-a1ef-533a68865516,de00430a-8a57-423c-887c-317d53c2cdd3 |
| Jogador 2 | 3-6 | 414 | MOVE_BENCH | FAST8 | 83.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40879371762275696 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 415 | BUY | FAST8 | 83.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.022124985232949257 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 416 | MOVE_BENCH | FAST8 | 83.0 | 7 | 3 | 0 | 38.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6359860897064209 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 417 | MOVE_BENCH | FAST8 | 83.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3559938073158264 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 418 | PASS | FAST8 | 83.0 | 7 | 3 | 0 | 38.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 426 | MOVE_BENCH | FAST8 | 83.0 | 7 | 3 | 0 | 38.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5937955379486084 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 432 | BUY | FAST8 | 83.0 | 7 | 9 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5461181402206421 | 0.0 | 0.0 | +1cba4955-961e-4efd-a291-e0a70bf72841 / -— |
| Jogador 2 | 3-7 | 433 | MOVE_BENCH | FAST8 | 83.0 | 7 | 5 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.056903623044490814 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 434 | BUY_XP | FAST8 | 83.0 | 7 | 5 | 0 | 48.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 435 | PASS | FAST8 | 83.0 | 7 | 1 | 0 | 48.0 | Colosso/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 452 | MOVE_BENCH | FAST8 | 83.0 | 7 | 6 | 0 | 48.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30538028478622437 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 453 | SELL | FAST8 | 83.0 | 7 | 6 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07154136896133423 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 4-1 | 454 | BUY | FAST8 | 83.0 | 7 | 10 | 1 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3507177531719208 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 2 | 4-1 | 455 | BUY_XP | FAST8 | 83.0 | 7 | 6 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 456 | PASS | FAST8 | 83.0 | 7 | 2 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 472 | SELL | FAST8 | 83.0 | 7 | 9 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1013842225074768 | 0.0 | 0.0 | +— / -974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 |
| Jogador 2 | 4-2 | 473 | BUY | FAST8 | 83.0 | 7 | 13 | 1 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7769652605056763 | 0.0 | 0.0 | +6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 / -— |
| Jogador 2 | 4-2 | 474 | BUY_XP | FAST8 | 83.0 | 7 | 12 | 1 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 475 | BUY_XP | FAST8 | 83.0 | 7 | 8 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 476 | BUY_XP | FAST8 | 83.0 | 7 | 4 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 477 | PASS | FAST8 | 83.0 | 7 | 0 | 0 | 46.0 | Colosso/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 492 | BUY_XP | FAST8 | 71.0 | 7 | 5 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 493 | PASS | FAST8 | 71.0 | 7 | 1 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 512 | BUY | ECON | 59.0 | 8 | 7 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4112609624862671 | 0.0 | 0.0 | +952ea2b4-387d-455d-b1ad-fb0de8c46e47 / -— |
| Jogador 2 | 4-4 | 513 | BUY | ECON | 59.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1126258373260498 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -— |
| Jogador 2 | 4-4 | 514 | PASS | ECON | 59.0 | 8 | 1 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 528 | MOVE_BENCH | ECON | 59.0 | 8 | 1 | 0 | 46.0 | Colosso/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5487014055252075 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 532 | BUY | ECON | 59.0 | 8 | 7 | 0 | 48.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018905390053987503 | 0.0 | 0.0 | +d2afd490-f89f-47c9-8279-a88acde5b1b6 / -— |
| Jogador 2 | 4-5 | 533 | BUY | ECON | 59.0 | 8 | 3 | 0 | 48.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21393537521362305 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 2 | 4-5 | 534 | PASS | ECON | 59.0 | 8 | 1 | 0 | 48.0 | Colosso/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 551 | BUY | ECON | 59.0 | 8 | 7 | 0 | 48.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.767600953578949 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -6556f264-6237-4af2-ab1b-52bf9a6246c1,6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 |
| Jogador 2 | 4-6 | 552 | MOVE_BENCH | ECON | 59.0 | 8 | 6 | 0 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5569496750831604 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 553 | MOVE_BENCH | ECON | 59.0 | 8 | 6 | 0 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28947073221206665 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 554 | BUY_XP | ECON | 59.0 | 8 | 6 | 0 | 50.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 555 | PASS | ECON | 59.0 | 8 | 2 | 0 | 50.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 564 | MOVE_BENCH | ECON | 59.0 | 8 | 2 | 0 | 50.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6560735702514648 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 570 | BUY | ECON | 59.0 | 8 | 9 | 0 | 58.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16076935827732086 | 0.0 | 0.0 | +533790d1-aca6-417d-b163-b0bda70d1500 / -— |
| Jogador 2 | 4-7 | 571 | BUY_XP | ECON | 59.0 | 8 | 7 | 0 | 58.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 572 | PASS | ECON | 59.0 | 8 | 3 | 0 | 58.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 582 | ANVIL_CHOICE | ECON | 59.0 | 8 | 9 | 0 | 58.0 | Colosso/DA_18_Sejuani | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 583 | CRAFT_AND_EQUIP | ECON | 59.0 | 8 | 9 | 0 | 58.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.019354231655597687 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 584 | BUY | ECON | 59.0 | 8 | 9 | 0 | 58.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03989480063319206 | 0.0 | 0.0 | +9fd5cb87-62ee-43bc-85db-7f166ac20532 / -— |
| Jogador 2 | 5-1 | 585 | BUY_XP | ECON | 59.0 | 8 | 4 | 0 | 58.0 | Colosso/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 586 | PASS | ECON | 59.0 | 8 | 0 | 0 | 58.0 | Colosso/DA_18_Lux_Sunbeam | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 601 | BUY | WINSTREAK | 59.0 | 8 | 7 | 0 | 58.0 | Colosso/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7789820432662964 | 0.0 | 0.0 | +d586f67f-487b-408e-b96d-21f5b8b6670e / -— |
| Jogador 2 | 5-2 | 602 | BUY | WINSTREAK | 59.0 | 8 | 3 | 0 | 58.0 | Colosso/DA_18_Lux_Sunbeam | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23200729489326477 | 0.0 | 0.0 | +3b98edb7-348f-47b4-85fd-66ee3f1a7af5 / -— |
| Jogador 2 | 5-2 | 603 | PASS | WINSTREAK | 59.0 | 8 | 0 | 0 | 58.0 | Colosso/DA_18_Lux_Sunbeam | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 619 | BUY | WINSTREAK | 59.0 | 8 | 7 | 0 | 58.0 | Colosso/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26596349477767944 | 0.0 | 0.0 | +7c5ba0a8-2f8d-40e5-b4b2-2c77bbc03b83 / -— |
| Jogador 2 | 5-3 | 620 | BUY | WINSTREAK | 59.0 | 8 | 5 | 0 | 58.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5032719373703003 | 0.0 | 0.0 | +d1464eaa-d2dc-4eef-8bf0-14c704a500e9 / -— |
| Jogador 2 | 5-3 | 621 | SELL | WINSTREAK | 59.0 | 8 | 1 | 0 | 58.0 | Colosso/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06955384463071823 | 0.0 | 0.0 | +— / -02e125a0-3563-47ec-a82a-cba5178731dd |
| Jogador 2 | 5-3 | 622 | BUY | WINSTREAK | 59.0 | 8 | 4 | 0 | 58.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09491036832332611 | 0.0 | 0.0 | +086093f9-0a81-4d85-9916-c256df0c1c33 / -— |
| Jogador 2 | 5-3 | 623 | PASS | WINSTREAK | 59.0 | 8 | 1 | 0 | 58.0 | Colosso/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 632 | SELL | WINSTREAK | 59.0 | 8 | 9 | 0 | 58.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09939245879650116 | 0.0 | 0.0 | +— / -533790d1-aca6-417d-b163-b0bda70d1500 |
| Jogador 2 | 5-4 | 633 | BUY | WINSTREAK | 59.0 | 8 | 11 | 1 | 58.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12349261343479156 | 0.0 | 0.0 | +22f1ab5f-b752-49e7-b6f0-ed9b5e641d64 / -— |
| Jogador 2 | 5-4 | 634 | SELL | WINSTREAK | 59.0 | 8 | 6 | 0 | 58.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46210017800331116 | 0.0 | 0.0 | +— / -a810e10d-e7ef-4ece-8fb2-8b6471b557ec |
| Jogador 2 | 5-4 | 635 | BUY | WINSTREAK | 59.0 | 8 | 9 | 0 | 58.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.756801187992096 | 0.0 | 0.0 | +cdd76540-e76c-41e9-ac02-253f5ba2e75e / -952ea2b4-387d-455d-b1ad-fb0de8c46e47,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 5-4 | 636 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4505840837955475 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 637 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 6 | 0 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43960705399513245 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 638 | BUY | WINSTREAK | 59.0 | 8 | 6 | 0 | 52.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1479184627532959 | 0.0 | 0.0 | +4869a6d9-9cd7-4ee7-93ae-ae4b2a0c8233 / -— |
| Jogador 2 | 5-4 | 639 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 3 | 0 | 52.0 | Colosso/DA_18_Alune | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4534248411655426 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 640 | BUY | WINSTREAK | 59.0 | 8 | 3 | 0 | 58.0 | Colosso/DA_18_Alune | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2673487663269043 | 0.0 | 0.0 | +aa6b7c66-6aa1-4cd5-9005-449e37829ad8 / -— |
| Jogador 2 | 5-4 | 641 | PASS | WINSTREAK | 59.0 | 8 | 2 | 0 | 58.0 | Colosso/DA_18_Alune | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 651 | SELL | WINSTREAK | 59.0 | 8 | 9 | 0 | 58.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.252888560295105 | 0.0 | 0.0 | +— / -d1464eaa-d2dc-4eef-8bf0-14c704a500e9 |
| Jogador 2 | 5-5 | 652 | BUY | WINSTREAK | 59.0 | 8 | 13 | 1 | 58.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7632367610931396 | 0.0 | 0.0 | +9db714e5-6351-482b-a263-282320af3345 / -— |
| Jogador 2 | 5-5 | 653 | SELL | WINSTREAK | 59.0 | 8 | 10 | 1 | 58.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34389230608940125 | 0.0 | 0.0 | +— / -cdd76540-e76c-41e9-ac02-253f5ba2e75e |
| Jogador 2 | 5-5 | 654 | BUY | WINSTREAK | 59.0 | 8 | 18 | 1 | 58.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8063050508499146 | 0.0 | 0.0 | +a61d9734-02d1-4fee-b9bd-7400fbf50817 / -086093f9-0a81-4d85-9916-c256df0c1c33,9db714e5-6351-482b-a263-282320af3345 |
| Jogador 2 | 5-5 | 655 | BUY | WINSTREAK | 59.0 | 8 | 15 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055515091866254807 | 0.0 | 0.0 | +53722e0c-9ca3-44b8-b593-c803870bce62 / -— |
| Jogador 2 | 5-5 | 656 | BUY | WINSTREAK | 59.0 | 8 | 11 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0718993991613388 | 0.0 | 0.0 | +02cb9b8e-6bb3-4b3d-8369-5fb39975c0ed / -— |
| Jogador 2 | 5-5 | 657 | PASS | WINSTREAK | 59.0 | 8 | 8 | 0 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 669 | SELL | WINSTREAK | 59.0 | 8 | 15 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038538459688425064 | 0.0 | 0.0 | +— / -02cb9b8e-6bb3-4b3d-8369-5fb39975c0ed |
| Jogador 2 | 5-6 | 670 | BUY | WINSTREAK | 59.0 | 8 | 18 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5290878415107727 | 0.0 | 0.0 | +fd689140-8b80-48df-92c1-aeadf35505e8 / -— |
| Jogador 2 | 5-6 | 671 | SELL | WINSTREAK | 59.0 | 8 | 14 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -53722e0c-9ca3-44b8-b593-c803870bce62 |
| Jogador 2 | 5-6 | 672 | BUY | WINSTREAK | 59.0 | 8 | 18 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05872664228081703 | 0.0 | 0.0 | +646dafa4-69ff-4189-8342-afea213a6790 / -— |
| Jogador 2 | 5-6 | 673 | SELL | WINSTREAK | 59.0 | 8 | 14 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -646dafa4-69ff-4189-8342-afea213a6790 |
| Jogador 2 | 5-6 | 674 | BUY | WINSTREAK | 59.0 | 8 | 18 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1499742716550827 | 0.0 | 0.0 | +81d97dc0-cc50-4303-acfe-e8273ef39d35 / -— |
| Jogador 2 | 5-6 | 675 | PASS | WINSTREAK | 59.0 | 8 | 15 | 1 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027499999850988388 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 682 | SELL | WINSTREAK | 59.0 | 8 | 25 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.066600002348423 | 0.0 | 0.0 | +— / -81d97dc0-cc50-4303-acfe-e8273ef39d35 |
| Jogador 2 | 5-7 | 683 | BUY | WINSTREAK | 59.0 | 8 | 28 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18325555324554443 | 0.0 | 0.0 | +3d7b58af-0df4-452d-b82e-049660a817ec / -— |
| Jogador 2 | 5-7 | 684 | SELL | WINSTREAK | 59.0 | 8 | 23 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3187280297279358 | 0.0 | 0.0 | +— / -fd689140-8b80-48df-92c1-aeadf35505e8 |
| Jogador 2 | 5-7 | 685 | BUY | WINSTREAK | 59.0 | 8 | 27 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09438265860080719 | 0.0 | 0.0 | +ee9f4ee2-0f17-4f55-b410-5f9c6a2984ef / -— |
| Jogador 2 | 5-7 | 686 | SELL | WINSTREAK | 59.0 | 8 | 23 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -ee9f4ee2-0f17-4f55-b410-5f9c6a2984ef |
| Jogador 2 | 5-7 | 687 | BUY | WINSTREAK | 59.0 | 8 | 27 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10458095371723175 | 0.0 | 0.0 | +52fab411-0911-4c1f-a60b-268de98a0243 / -— |
| Jogador 2 | 5-7 | 688 | REROLL | WINSTREAK | 59.0 | 8 | 24 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 689 | SELL | WINSTREAK | 59.0 | 8 | 22 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.049115996807813644 | 0.0 | 0.0 | +— / -52fab411-0911-4c1f-a60b-268de98a0243 |
| Jogador 2 | 5-7 | 690 | BUY | WINSTREAK | 59.0 | 8 | 25 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3809596598148346 | 0.0 | 0.0 | +4232b4b4-99b2-4af0-b352-13f5b0726727 / -— |
| Jogador 2 | 5-7 | 691 | SELL | WINSTREAK | 59.0 | 8 | 22 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30373847484588623 | 0.0 | 0.0 | +— / -4232b4b4-99b2-4af0-b352-13f5b0726727 |
| Jogador 2 | 5-7 | 692 | PASS | WINSTREAK | 59.0 | 8 | 25 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1233571395277977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 697 | ANVIL_CHOICE | WINSTREAK | 59.0 | 8 | 35 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 698 | BUY | WINSTREAK | 59.0 | 8 | 35 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.16325536370277405 | 0.0 | 0.0 | +83fa2298-3d6d-4785-bd01-7b40f6a69f1e / -— |
| Jogador 2 | 6-1 | 699 | EQUIP_FROM_INVENTORY | WINSTREAK | 59.0 | 8 | 31 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10451441258192062 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 700 | SELL | WINSTREAK | 59.0 | 8 | 31 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07118461281061172 | 0.0 | 0.0 | +— / -83fa2298-3d6d-4785-bd01-7b40f6a69f1e |
| Jogador 2 | 6-1 | 701 | BUY | WINSTREAK | 59.0 | 8 | 35 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21618138253688812 | 0.0 | 0.0 | +0cb30b20-2d68-4168-94b6-5198b58776bb / -— |
| Jogador 2 | 6-1 | 702 | SELL | WINSTREAK | 59.0 | 8 | 33 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019460417330265045 | 0.0 | 0.0 | +— / -0cb30b20-2d68-4168-94b6-5198b58776bb |
| Jogador 2 | 6-1 | 703 | BUY | WINSTREAK | 59.0 | 8 | 35 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05258467420935631 | 0.0 | 0.0 | +30adc860-f40e-4899-b3fe-a5fefb4a472a / -— |
| Jogador 2 | 6-1 | 704 | REROLL | WINSTREAK | 59.0 | 8 | 33 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 705 | SELL | WINSTREAK | 59.0 | 8 | 31 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055877748876810074 | 0.0 | 0.0 | +— / -30adc860-f40e-4899-b3fe-a5fefb4a472a |
| Jogador 2 | 6-1 | 706 | BUY | WINSTREAK | 59.0 | 8 | 33 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45189714431762695 | 0.0 | 0.0 | +d4149507-5936-4286-bc92-03a8f6fd9c13 / -— |
| Jogador 2 | 6-1 | 707 | PASS | WINSTREAK | 59.0 | 8 | 29 | 2 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041999999433755875 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 712 | SELL | WINSTREAK | 59.0 | 8 | 41 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3187251091003418 | 0.0 | 0.0 | +— / -d4149507-5936-4286-bc92-03a8f6fd9c13 |
| Jogador 2 | 6-2 | 713 | BUY | WINSTREAK | 59.0 | 8 | 45 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12914344668388367 | 0.0 | 0.0 | +4b2b838a-f08a-4c2f-8d4f-5ca9265efe94 / -— |
| Jogador 2 | 6-2 | 714 | SELL | WINSTREAK | 59.0 | 8 | 40 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06690768897533417 | 0.0 | 0.0 | +— / -4b2b838a-f08a-4c2f-8d4f-5ca9265efe94 |
| Jogador 2 | 6-2 | 715 | BUY | WINSTREAK | 59.0 | 8 | 45 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09448463469743729 | 0.0 | 0.0 | +b5df9bf6-5601-488f-bdb3-2109875f255d / -— |
| Jogador 2 | 6-2 | 716 | SELL | WINSTREAK | 59.0 | 8 | 41 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040169231593608856 | 0.0 | 0.0 | +— / -b5df9bf6-5601-488f-bdb3-2109875f255d |
| Jogador 2 | 6-2 | 717 | BUY | WINSTREAK | 59.0 | 8 | 45 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10305081307888031 | 0.0 | 0.0 | +184fd23e-e7de-4450-b114-831f6a9e8251 / -— |
| Jogador 2 | 6-2 | 718 | REROLL | WINSTREAK | 59.0 | 8 | 41 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 719 | SELL | WINSTREAK | 59.0 | 8 | 39 | 3 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13103513419628143 | 0.0 | 0.0 | +— / -184fd23e-e7de-4450-b114-831f6a9e8251 |
| Jogador 2 | 6-2 | 720 | BUY | WINSTREAK | 59.0 | 8 | 43 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8398618698120117 | 0.0 | 0.0 | +09c6b187-ccc0-4525-9a38-7bde65ca178a / -— |
| Jogador 2 | 6-2 | 721 | SELL | WINSTREAK | 59.0 | 8 | 40 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3870784640312195 | 0.0 | 0.0 | +— / -09c6b187-ccc0-4525-9a38-7bde65ca178a |
| Jogador 2 | 6-2 | 722 | PASS | WINSTREAK | 59.0 | 8 | 43 | 4 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22200000286102295 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 728 | BUY | WINSTREAK | 59.0 | 8 | 56 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10250389575958252 | 0.0 | 0.0 | +aabb68a2-aa23-402a-a8ca-36ef9f9f6f3e / -— |
| Jogador 2 | 6-3 | 729 | SELL | WINSTREAK | 59.0 | 8 | 52 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -aabb68a2-aa23-402a-a8ca-36ef9f9f6f3e |
| Jogador 2 | 6-3 | 730 | BUY | WINSTREAK | 59.0 | 8 | 56 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1110578402876854 | 0.0 | 0.0 | +31f86c34-a81d-4ba0-9136-c9106b0fbec5 / -— |
| Jogador 2 | 6-3 | 731 | REROLL | WINSTREAK | 59.0 | 8 | 52 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 732 | SELL | WINSTREAK | 59.0 | 8 | 50 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04303498566150665 | 0.0 | 0.0 | +— / -31f86c34-a81d-4ba0-9136-c9106b0fbec5 |
| Jogador 2 | 6-3 | 733 | BUY | WINSTREAK | 59.0 | 8 | 54 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11086047440767288 | 0.0 | 0.0 | +0088ca46-2bd7-4e4e-a102-8cfdc86bc494 / -— |
| Jogador 2 | 6-3 | 734 | SELL | WINSTREAK | 59.0 | 8 | 50 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04304778575897217 | 0.0 | 0.0 | +— / -0088ca46-2bd7-4e4e-a102-8cfdc86bc494 |
| Jogador 2 | 6-3 | 735 | BUY | WINSTREAK | 59.0 | 8 | 54 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34927377104759216 | 0.0 | 0.0 | +504ad65c-e5fe-48dc-bc1c-88b1d6ce1641 / -— |
| Jogador 2 | 6-3 | 736 | SELL | WINSTREAK | 59.0 | 8 | 53 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042876921594142914 | 0.0 | 0.0 | +— / -9fd5cb87-62ee-43bc-85db-7f166ac20532 |
| Jogador 2 | 6-3 | 737 | BUY | WINSTREAK | 59.0 | 8 | 58 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.867029070854187 | 0.0 | 0.0 | +28bfd469-8412-4227-af3a-4ac1cf3574ac / -— |
| Jogador 2 | 6-3 | 738 | PASS | WINSTREAK | 59.0 | 8 | 57 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10082892328500748 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 742 | SELL | WINSTREAK | 59.0 | 8 | 71 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024415384978055954 | 0.0 | 0.0 | +— / -3d7b58af-0df4-452d-b82e-049660a817ec |
| Jogador 2 | 6-4 | 743 | BUY | WINSTREAK | 59.0 | 8 | 76 | 5 | 58.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0171304941177368 | 0.0 | 0.0 | +3db81741-d40d-438e-911a-9566edc245a8 / -1cba4955-961e-4efd-a291-e0a70bf72841,729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 6-4 | 744 | SELL | WINSTREAK | 59.0 | 8 | 72 | 5 | 42.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.407153844833374 | 0.0 | 0.0 | +— / -aa6b7c66-6aa1-4cd5-9005-449e37829ad8 |
| Jogador 2 | 6-4 | 745 | BUY | WINSTREAK | 59.0 | 8 | 73 | 5 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7370157837867737 | 0.0 | 0.0 | +f5078e39-0584-491b-b681-0f58b2897b3b / -— |
| Jogador 2 | 6-4 | 746 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 70 | 5 | 42.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002496992819942534 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 747 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 70 | 5 | 42.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4505508542060852 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 748 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 70 | 5 | 40.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2003173828125 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 749 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 70 | 5 | 42.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08006926625967026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 750 | BUY | WINSTREAK | 59.0 | 8 | 70 | 5 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008970380760729313 | 0.0 | 0.0 | +993e2955-9769-4af0-b3c4-6bc092f8e221 / -— |
| Jogador 2 | 6-4 | 751 | REROLL | WINSTREAK | 59.0 | 8 | 66 | 5 | 48.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 752 | PASS | WINSTREAK | 59.0 | 8 | 64 | 5 | 48.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10635102540254593 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 759 | SELL | WINSTREAK | 59.0 | 8 | 77 | 5 | 48.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -993e2955-9769-4af0-b3c4-6bc092f8e221 |
| Jogador 2 | 6-5 | 760 | BUY | WINSTREAK | 59.0 | 8 | 81 | 5 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9491596221923828 | 0.0 | 0.0 | +d1c35cea-32ee-419f-bc79-d14cbab4f8b9 / -— |
| Jogador 2 | 6-5 | 761 | SELL | WINSTREAK | 59.0 | 8 | 79 | 5 | 48.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4307846128940582 | 0.0 | 0.0 | +— / -a61d9734-02d1-4fee-b9bd-7400fbf50817 |
| Jogador 2 | 6-5 | 762 | BUY | WINSTREAK | 59.0 | 8 | 87 | 5 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7592045664787292 | 0.0 | 0.0 | +3c7e765c-5e57-40ea-a310-c15b18d99e04 / -— |
| Jogador 2 | 6-5 | 763 | REROLL | WINSTREAK | 59.0 | 8 | 84 | 5 | 48.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 764 | SELL | WINSTREAK | 59.0 | 8 | 82 | 5 | 48.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39122310280799866 | 0.0 | 0.0 | +— / -3c7e765c-5e57-40ea-a310-c15b18d99e04 |
| Jogador 2 | 6-5 | 765 | BUY | WINSTREAK | 59.0 | 8 | 85 | 5 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0469259023666382 | 0.0 | 0.0 | +1ffb7115-2f25-4625-80c4-37c853de7ea2 / -4869a6d9-9cd7-4ee7-93ae-ae4b2a0c8233,f5078e39-0584-491b-b681-0f58b2897b3b |
| Jogador 2 | 6-5 | 766 | MOVE_BENCH | WINSTREAK | 59.0 | 8 | 82 | 5 | 36.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.630152702331543 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 767 | MOVE_BENCH | STABILIZE | 59.0 | 8 | 82 | 5 | 32.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21340031921863556 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 768 | BUY | WINSTREAK | 59.0 | 8 | 82 | 5 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03885938972234726 | 0.0 | 0.0 | +863cac79-64c8-46ae-8653-733bca3b8bb7 / -— |
| Jogador 2 | 6-5 | 769 | PASS | WINSTREAK | 59.0 | 8 | 80 | 5 | 42.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11993733793497086 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 772 | SELL | ECON | 42.0 | 8 | 90 | 5 | 42.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035861536860466 | 0.0 | 0.0 | +— / -863cac79-64c8-46ae-8653-733bca3b8bb7 |
| Jogador 2 | 6-6 | 773 | BUY | ECON | 42.0 | 8 | 92 | 5 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0499322414398193 | 0.0 | 0.0 | +59a36bb7-7bda-4fe5-8e51-77f6aa7ca147 / -7c5ba0a8-2f8d-40e5-b4b2-2c77bbc03b83,d1c35cea-32ee-419f-bc79-d14cbab4f8b9 |
| Jogador 2 | 6-6 | 774 | MOVE_BENCH | ECON | 42.0 | 8 | 90 | 5 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5806843042373657 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 775 | BUY | ECON | 42.0 | 8 | 90 | 5 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04429411515593529 | 0.0 | 0.0 | +3a3f1653-12f4-4733-9412-2e519a26b7af / -— |
| Jogador 2 | 6-6 | 776 | BUY | ECON | 42.0 | 8 | 86 | 5 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045662771910429 | 0.0 | 0.0 | +4afb6994-b5d7-40b5-8027-8825b1f74956 / -— |
| Jogador 2 | 6-6 | 777 | MOVE_BENCH | ECON | 42.0 | 8 | 84 | 5 | 46.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13364866375923157 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 778 | BUY | ECON | 42.0 | 8 | 84 | 5 | 54.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04790345951914787 | 0.0 | 0.0 | +bbbcbf7e-ab89-4457-acf1-529729f83aaa / -— |
| Jogador 2 | 6-6 | 779 | REROLL | ECON | 42.0 | 8 | 82 | 5 | 54.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 780 | SELL | ECON | 42.0 | 8 | 80 | 5 | 54.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035861536860466 | 0.0 | 0.0 | +— / -bbbcbf7e-ab89-4457-acf1-529729f83aaa |
| Jogador 2 | 6-6 | 781 | BUY | ECON | 42.0 | 8 | 82 | 5 | 54.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9081773161888123 | 0.0 | 0.0 | +01cb9abd-4b2d-4758-9ca8-28562ab57551 / -— |
| Jogador 2 | 6-6 | 782 | PASS | ECON | 42.0 | 8 | 80 | 5 | 54.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12633733451366425 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3363300859928131 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.11721326410770416 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5543375015258789 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 62 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0396400690078735 | 0.0 | 0.0 | +477d3aa4-2130-4a0e-8254-2688ac860569 / -— |
| Jogador 3 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0226153377443552 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5497032403945923 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32369595766067505 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 66 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 92 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02259032614529133 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 93 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 94 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4692728519439697 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 95 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.15635113418102264 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 96 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 122 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32198193669319153 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 123 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18542039394378662 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 124 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012907692231237888 | 0.0 | 0.0 | +— / -bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 2-1 | 125 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Shen | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17874489724636078 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 126 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01939353160560131 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 127 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 148 | SELL | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041357703506946564 | 0.0 | 0.0 | +— / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef |
| Jogador 3 | 2-2 | 149 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0149164199829102 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 150 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330201625823975 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 151 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26889440417289734 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 152 | PASS | STABILIZE | 95.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 172 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 11 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 173 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 11 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027924543246626854 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 174 | PASS | STABILIZE | 90.0 | 4 | 11 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 201 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 18 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2868805229663849 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 202 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 18 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48821547627449036 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 203 | BUY | SLOWROLL | 83.0 | 5 | 18 | 1 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10340388864278793 | 0.0 | 0.0 | +4c8a9a18-68d8-4672-a96d-bb09816257dc / -— |
| Jogador 3 | 2-4 | 204 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 15 | 1 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.579906702041626 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 205 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 15 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31762242317199707 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 206 | PASS | SLOWROLL | 83.0 | 5 | 15 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019999999552965164 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 227 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 22 | 2 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01654316857457161 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 228 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 22 | 2 | 16.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2633313536643982 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 229 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 22 | 2 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 230 | PASS | SLOWROLL | 83.0 | 5 | 22 | 2 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021250000223517418 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 252 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 30 | 3 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3442819118499756 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 253 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 30 | 3 | 16.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2591661512851715 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 254 | PASS | SLOWROLL | 83.0 | 5 | 30 | 3 | 18.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03767857328057289 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 276 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 38 | 3 | 18.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7362809181213379 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 277 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 38 | 3 | 18.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07968781143426895 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 278 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 38 | 3 | 16.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2593626081943512 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 279 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 38 | 3 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8190218210220337 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 280 | PASS | SLOWROLL | 75.0 | 5 | 38 | 3 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03910714387893677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 302 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 46 | 4 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07819204032421112 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 303 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 46 | 4 | 16.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21312181651592255 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 304 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 46 | 4 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 305 | PASS | SLOWROLL | 75.0 | 5 | 46 | 4 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11349999904632568 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 327 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 56 | 5 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7446519136428833 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 328 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 56 | 5 | 16.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6323419213294983 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 329 | PASS | SLOWROLL | 75.0 | 5 | 56 | 5 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12487752735614777 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 349 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 68 | 5 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15866540372371674 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 350 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 68 | 5 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.365192174911499 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 351 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 68 | 5 | 20.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07106978446245193 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 352 | PASS | SLOWROLL | 75.0 | 5 | 68 | 5 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13046084344387054 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 371 | MOVE_BENCH | SLOWROLL | 64.0 | 5 | 78 | 5 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1714007407426834 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 372 | MOVE_BENCH | SLOWROLL | 64.0 | 5 | 78 | 5 | 18.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35121503472328186 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 373 | BUY_XP | SLOWROLL | 64.0 | 5 | 78 | 5 | 20.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 374 | BUY_XP | SLOWROLL | 64.0 | 5 | 74 | 5 | 20.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33588001132011414 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 375 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 70 | 5 | 20.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5062835216522217 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 376 | BUY | SLOWROLL | 64.0 | 6 | 70 | 5 | 22.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.27560529112815857 | 0.0 | 0.0 | +fe8191d8-bc21-499a-aff7-31c3ca9b2e64 / -— |
| Jogador 3 | 3-4 | 377 | BUY_XP | SLOWROLL | 64.0 | 6 | 68 | 5 | 22.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 378 | BUY_XP | SLOWROLL | 64.0 | 6 | 64 | 5 | 22.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 379 | BUY_XP | SLOWROLL | 64.0 | 6 | 60 | 5 | 22.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 380 | BUY_XP | SLOWROLL | 64.0 | 6 | 56 | 5 | 22.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 381 | PASS | SLOWROLL | 64.0 | 6 | 52 | 5 | 22.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12321005761623383 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 392 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 62 | 5 | 22.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3522879481315613 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 393 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 62 | 5 | 24.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05877555534243584 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 394 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 62 | 5 | 22.0 | Inferno/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005480842664837837 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 395 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 62 | 5 | 22.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31284940242767334 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 396 | PASS | SLOWROLL | 64.0 | 6 | 62 | 5 | 24.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12759634852409363 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 412 | BUY | SLOWROLL | 64.0 | 6 | 73 | 5 | 24.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9344492554664612 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 3-6 | 413 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 71 | 5 | 16.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15990467369556427 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 414 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 71 | 5 | 24.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006964176427572966 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 415 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 71 | 5 | 18.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1433982104063034 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 416 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 71 | 5 | 22.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3447954058647156 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 417 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 71 | 5 | 24.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016908274963498116 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 418 | PASS | SLOWROLL | 64.0 | 6 | 71 | 5 | 22.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13193193078041077 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 426 | MOVE_BENCH | SLOWROLL | 64.0 | 6 | 71 | 5 | 22.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5042409896850586 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 432 | BUY | FAST8 | 64.0 | 6 | 83 | 5 | 26.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10561265796422958 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 3 | 3-7 | 433 | MOVE_BENCH | FAST8 | 64.0 | 6 | 80 | 5 | 26.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12443830072879791 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 434 | BUY_XP | FAST8 | 64.0 | 6 | 80 | 5 | 28.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 435 | BUY_XP | FAST8 | 64.0 | 6 | 76 | 5 | 28.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 436 | BUY_XP | FAST8 | 64.0 | 6 | 72 | 5 | 28.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3149000108242035 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 437 | MOVE_BENCH | FAST8 | 64.0 | 7 | 68 | 5 | 28.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32284536957740784 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 438 | BUY_XP | FAST8 | 64.0 | 7 | 68 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006300000008195639 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 439 | BUY_XP | FAST8 | 64.0 | 7 | 64 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006300000008195639 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 440 | BUY_XP | FAST8 | 64.0 | 7 | 60 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006300000008195639 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 441 | BUY_XP | FAST8 | 64.0 | 7 | 56 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006300000008195639 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 442 | PASS | FAST8 | 64.0 | 7 | 52 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.154710054397583 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 452 | BUY | FAST8 | 64.0 | 7 | 63 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6094947457313538 | 0.0 | 0.0 | +f394f34c-c68b-4213-9eb0-88f302976405 / -— |
| Jogador 3 | 4-1 | 453 | MOVE_BENCH | FAST8 | 64.0 | 7 | 60 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 454 | BUY_XP | FAST8 | 64.0 | 7 | 60 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008100000210106373 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 455 | BUY_XP | FAST8 | 64.0 | 7 | 56 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008100000210106373 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 456 | BUY_XP | FAST8 | 64.0 | 7 | 52 | 5 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07792499661445618 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 457 | BUY_XP | FAST8 | 64.0 | 7 | 48 | 4 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026924999430775642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 458 | BUY_XP | FAST8 | 64.0 | 7 | 44 | 4 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026924999430775642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 459 | BUY_XP | FAST8 | 64.0 | 7 | 40 | 4 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10692500323057175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 460 | BUY_XP | FAST8 | 64.0 | 7 | 36 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026924999430775642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 461 | BUY_XP | FAST8 | 64.0 | 7 | 32 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10692500323057175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 462 | PASS | FAST8 | 64.0 | 7 | 28 | 2 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11428571492433548 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 472 | BUY_XP | FAST8 | 51.0 | 7 | 35 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07968749850988388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 473 | MOVE_BENCH | ECON | 51.0 | 8 | 31 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7909470796585083 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 474 | MOVE_BENCH | ECON | 51.0 | 8 | 31 | 3 | 28.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17088089883327484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 475 | MOVE_BENCH | ECON | 51.0 | 8 | 31 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 476 | MOVE_BENCH | ECON | 51.0 | 8 | 31 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7929771542549133 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 477 | PASS | ECON | 51.0 | 8 | 31 | 3 | 28.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15142856538295746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 487 | MOVE_BENCH | ECON | 51.0 | 8 | 31 | 3 | 28.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2908115088939667 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 492 | BUY | STABILIZE | 39.0 | 8 | 40 | 4 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09141144901514053 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -— |
| Jogador 3 | 4-3 | 493 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17201662063598633 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 494 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 32.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010392243042588234 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 495 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 34.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6963061690330505 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 496 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16964000463485718 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 497 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 32.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006531175225973129 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 498 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 34.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6963083744049072 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 499 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17210793495178223 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 500 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 32.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 501 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 36 | 3 | 32.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.793721079826355 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 502 | PASS | STABILIZE | 39.0 | 8 | 36 | 3 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16424444317817688 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 512 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 45 | 4 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07248376309871674 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 513 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 45 | 4 | 32.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20993134379386902 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 514 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 45 | 4 | 32.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7937209606170654 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 515 | PASS | STABILIZE | 27.0 | 8 | 45 | 4 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19342857599258423 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 528 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 45 | 4 | 30.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4201769232749939 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 532 | BUY | STABILIZE | 27.0 | 8 | 55 | 5 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1603490710258484 | 0.0 | 0.0 | +98991369-e5f0-4725-928c-f2fa5362bf73 / -— |
| Jogador 3 | 4-5 | 533 | BUY | STABILIZE | 27.0 | 8 | 51 | 5 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15003274381160736 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 3 | 4-5 | 534 | BUY_XP | STABILIZE | 27.0 | 8 | 47 | 4 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 535 | BUY_XP | STABILIZE | 27.0 | 8 | 43 | 4 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 536 | BUY_XP | STABILIZE | 27.0 | 8 | 39 | 3 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 537 | BUY_XP | STABILIZE | 27.0 | 8 | 35 | 3 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 538 | BUY_XP | STABILIZE | 27.0 | 8 | 31 | 3 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 539 | BUY_XP | STABILIZE | 27.0 | 8 | 27 | 2 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 540 | BUY_XP | STABILIZE | 27.0 | 8 | 23 | 2 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 541 | BUY_XP | STABILIZE | 27.0 | 8 | 19 | 1 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 542 | PASS | STABILIZE | 27.0 | 8 | 15 | 1 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08533333241939545 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 551 | BUY | STABILIZE | 27.0 | 8 | 22 | 2 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048652179539203644 | 0.0 | 0.0 | +4b4293ce-1cca-473e-8c07-b441686985ac / -— |
| Jogador 3 | 4-6 | 552 | BUY_XP | STABILIZE | 27.0 | 8 | 18 | 1 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 553 | BUY_XP | STABILIZE | 27.0 | 8 | 14 | 1 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 554 | BUY_XP | STABILIZE | 27.0 | 8 | 10 | 1 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 555 | BUY_XP | STABILIZE | 27.0 | 8 | 6 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 556 | PASS | STABILIZE | 27.0 | 8 | 2 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 570 | BUY | STABILIZE | 27.0 | 8 | 9 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3022819757461548 | 0.0 | 0.0 | +280265b0-7892-4e7e-b654-e2cc7b0ea97b / -— |
| Jogador 3 | 4-7 | 571 | BUY_XP | STABILIZE | 27.0 | 8 | 6 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 572 | PASS | STABILIZE | 27.0 | 8 | 2 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 582 | ANVIL_CHOICE | STABILIZE | 27.0 | 8 | 8 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 583 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 8 | 8 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11610331386327744 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 584 | BUY_XP | STABILIZE | 27.0 | 8 | 8 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3909881114959717 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 585 | BUY | STABILIZE | 27.0 | 9 | 4 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07283227890729904 | 0.0 | 0.0 | +bf2246f7-4b73-4b2b-92ad-56849f783dfb / -— |
| Jogador 3 | 5-1 | 586 | BUY | STABILIZE | 27.0 | 9 | 1 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2868490219116211 | 0.0 | 0.0 | +50d7d851-387f-449e-8456-45a445f89cb7 / -— |
| Jogador 3 | 5-1 | 587 | MOVE_BENCH | STABILIZE | 27.0 | 9 | 0 | 0 | 38.0 | Inferno/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8050161600112915 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 588 | PASS | STABILIZE | 27.0 | 9 | 0 | 0 | 40.0 | Inferno/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 601 | BUY | STABILIZE | 27.0 | 9 | 7 | 0 | 40.0 | Inferno/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09921871870756149 | 0.0 | 0.0 | +aac54d95-6848-43d9-b837-d2189beede69 / -— |
| Jogador 3 | 5-2 | 602 | BUY | STABILIZE | 27.0 | 9 | 2 | 0 | 40.0 | Inferno/DA_18_Lux_Moonbeam | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05294908583164215 | 0.0 | 0.0 | +e24c48af-b2d8-4dbd-a22c-e6bd4e0d6fdf / -— |
| Jogador 3 | 5-2 | 603 | PASS | STABILIZE | 27.0 | 9 | 0 | 0 | 40.0 | Inferno/DA_18_Lux_Moonbeam | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 619 | BUY | ALL_IN | 10.0 | 9 | 5 | 0 | 40.0 | Inferno/DA_18_Lux_Moonbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7343800067901611 | 0.0 | 0.0 | +2b9c96b0-47c3-4330-894e-c42471aef448 / -— |
| Jogador 3 | 5-3 | 620 | PASS | ALL_IN | 10.0 | 9 | 0 | 0 | 40.0 | Inferno/DA_18_Lux_Moonbeam | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.340021014213562 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 62 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.05943821370601654 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0543689727783203 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7826818823814392 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | -0.2599632143974304 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 67 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 92 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08497094362974167 | 0.0 | 0.0 | +df71e10d-846b-4b12-8eb4-53633834303f / -— |
| Jogador 4 | 1-4 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5593688488006592 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 94 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0140483379364014 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 95 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 122 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2979736924171448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 123 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3049631416797638 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 124 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.018864393234253 | 0.0 | 0.0 | +c05579e6-aa73-434f-8a91-c58d68a81ced / -— |
| Jogador 4 | 2-1 | 125 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0172455310821533 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 126 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2985725998878479 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 127 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18916302919387817 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 128 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0301775932312012 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 129 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 148 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 9 | 0 | 14.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29793959856033325 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 149 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 9 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35208970308303833 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 150 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 9 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.016433835029602 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 151 | PASS | STABILIZE | 94.0 | 4 | 9 | 0 | 14.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 172 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 15 | 1 | 14.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11092427372932434 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 173 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 15 | 1 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 174 | PASS | STABILIZE | 88.0 | 4 | 15 | 1 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019999999552965164 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 201 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 22 | 2 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0190314054489136 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 202 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 22 | 2 | 14.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11066640168428421 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 203 | PASS | LOSS_STREAK | 82.0 | 4 | 22 | 2 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021250000223517418 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 227 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 30 | 3 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033108193427324295 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 228 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 30 | 3 | 12.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0538743734359741 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 229 | MOVE_BENCH | STABILIZE | 82.0 | 4 | 30 | 3 | 14.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035670205950737 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 230 | PASS | STABILIZE | 82.0 | 4 | 30 | 3 | 12.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03767857328057289 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 252 | MOVE_BENCH | SLOWROLL | 76.0 | 5 | 39 | 3 | 12.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3451420068740845 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 253 | BUY | SLOWROLL | 76.0 | 5 | 39 | 3 | 16.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31918299198150635 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 254 | MOVE_BENCH | SLOWROLL | 76.0 | 5 | 36 | 3 | 16.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08150557428598404 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 255 | MOVE_BENCH | SLOWROLL | 76.0 | 5 | 36 | 3 | 18.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05309133604168892 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 256 | MOVE_BENCH | SLOWROLL | 76.0 | 5 | 36 | 3 | 18.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8224606513977051 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 257 | MOVE_BENCH | SLOWROLL | 76.0 | 5 | 36 | 3 | 16.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0790010392665863 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 258 | PASS | SLOWROLL | 76.0 | 5 | 36 | 3 | 18.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038750000298023224 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 276 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 46 | 4 | 18.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052518080919981 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 277 | BUY | SLOWROLL | 70.0 | 5 | 46 | 4 | 18.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1698855608701706 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 278 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 43 | 4 | 18.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14505039155483246 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 279 | BUY | SLOWROLL | 70.0 | 5 | 43 | 4 | 20.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9668315649032593 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 280 | BUY_XP | SLOWROLL | 70.0 | 5 | 42 | 4 | 20.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 281 | BUY_XP | SLOWROLL | 70.0 | 5 | 38 | 3 | 20.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 282 | BUY_XP | SLOWROLL | 70.0 | 5 | 34 | 3 | 20.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 283 | BUY_XP | SLOWROLL | 70.0 | 5 | 30 | 3 | 20.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 284 | BUY_XP | SLOWROLL | 70.0 | 5 | 26 | 2 | 20.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.051910001784563065 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 285 | MOVE_BENCH | SLOWROLL | 70.0 | 6 | 22 | 2 | 20.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6130624413490295 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 286 | PASS | SLOWROLL | 70.0 | 6 | 22 | 2 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021250000223517418 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 302 | BUY | SLOWROLL | 70.0 | 6 | 31 | 3 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7399621605873108 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -a19fc47b-fc81-49b2-bc25-d25d58b8deef,c05579e6-aa73-434f-8a91-c58d68a81ced |
| Jogador 4 | 3-1 | 303 | MOVE_BENCH | SLOWROLL | 70.0 | 6 | 29 | 2 | 16.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07803979516029358 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 304 | MOVE_BENCH | SLOWROLL | 70.0 | 6 | 29 | 2 | 18.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2672565281391144 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 305 | PASS | SLOWROLL | 70.0 | 6 | 29 | 2 | 18.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 321 | MOVE_BENCH | SLOWROLL | 70.0 | 6 | 29 | 2 | 18.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08936835080385208 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 327 | BUY | SLOWROLL | 61.0 | 6 | 39 | 3 | 22.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25133320689201355 | 0.0 | 0.0 | +3f253868-2de5-4189-95a0-705f62682958 / -— |
| Jogador 4 | 3-2 | 328 | MOVE_BENCH | SLOWROLL | 61.0 | 6 | 37 | 3 | 22.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3907395601272583 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 329 | MOVE_BENCH | SLOWROLL | 61.0 | 6 | 37 | 3 | 20.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0976162850856781 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 330 | PASS | SLOWROLL | 61.0 | 6 | 37 | 3 | 22.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10899999737739563 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 342 | MOVE_BENCH | SLOWROLL | 61.0 | 6 | 37 | 3 | 22.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6969717144966125 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 349 | BUY | FAST8 | 61.0 | 6 | 46 | 4 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2601006031036377 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 350 | MOVE_BENCH | FAST8 | 61.0 | 6 | 43 | 4 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2692748010158539 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 351 | BUY | FAST8 | 61.0 | 6 | 43 | 4 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1443752646446228 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 352 | BUY_XP | FAST8 | 61.0 | 6 | 40 | 4 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 353 | BUY_XP | FAST8 | 61.0 | 6 | 36 | 3 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 354 | BUY_XP | FAST8 | 61.0 | 6 | 32 | 3 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 355 | BUY_XP | FAST8 | 61.0 | 6 | 28 | 2 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 356 | BUY_XP | FAST8 | 61.0 | 6 | 24 | 2 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 357 | BUY_XP | FAST8 | 61.0 | 6 | 20 | 2 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 358 | BUY_XP | FAST8 | 61.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 359 | PASS | FAST8 | 61.0 | 7 | 12 | 1 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 371 | BUY | FAST8 | 50.0 | 7 | 18 | 1 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7329691052436829 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 372 | BUY | FAST8 | 50.0 | 7 | 15 | 1 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7326095700263977 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 373 | MOVE_BENCH | FAST8 | 50.0 | 7 | 12 | 1 | 26.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6048882007598877 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 374 | BUY | FAST8 | 50.0 | 7 | 12 | 1 | 32.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13715140521526337 | 0.0 | 0.0 | +4cf7dfe2-9d2c-4d45-803e-503eda810357 / -— |
| Jogador 4 | 3-4 | 375 | BUY | FAST8 | 50.0 | 7 | 10 | 1 | 32.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12747155129909515 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 376 | BUY_XP | FAST8 | 50.0 | 7 | 9 | 0 | 32.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 377 | BUY_XP | FAST8 | 50.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 378 | PASS | FAST8 | 50.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 392 | BUY | FAST8 | 50.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7637861967086792 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-5 | 393 | BUY | FAST8 | 50.0 | 7 | 3 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7634949684143066 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -58c38a13-23c5-4ac1-8601-f0636aeb33ab,7fd03119-ac82-49e1-b3bb-3a0caa31011f |
| Jogador 4 | 3-5 | 394 | MOVE_BENCH | FAST8 | 50.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5506101846694946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 395 | MOVE_BOARD | FAST8 | 50.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 396 | MOVE_BOARD | FAST8 | 50.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.062188852578401566 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 397 | MOVE_BENCH | FAST8 | 50.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2226572036743164 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 398 | MOVE_BENCH | FAST8 | 50.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5314900875091553 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 399 | PASS | FAST8 | 50.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 412 | BUY | FAST8 | 50.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7345496416091919 | 0.0 | 0.0 | +fe3fea0b-bb55-4236-830e-828a00a9e529 / -— |
| Jogador 4 | 3-6 | 413 | BUY | FAST8 | 50.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7679131031036377 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -4a0403a3-c999-4d4c-83f0-7270e8576aed,9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 3-6 | 414 | MOVE_BENCH | FAST8 | 50.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6933809518814087 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 415 | MOVE_BENCH | FAST8 | 50.0 | 7 | 3 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8269587159156799 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 416 | BUY | FAST8 | 50.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05016485974192619 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 417 | MOVE_BENCH | FAST8 | 50.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0963730439543724 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 418 | MOVE_BENCH | FAST8 | 50.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000325138884363696 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 419 | MOVE_BENCH | FAST8 | 50.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4495604634284973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 420 | MOVE_BOARD | FAST8 | 50.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17271725833415985 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 421 | MOVE_BENCH | FAST8 | 50.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1495216339826584 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 422 | PASS | FAST8 | 50.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 432 | BUY | STABILIZE | 38.0 | 7 | 5 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.283864825963974 | 0.0 | 0.0 | +502a6e8c-8f81-456f-a1ef-c6bb8dd6fc7e / -— |
| Jogador 4 | 3-7 | 433 | BUY | STABILIZE | 38.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8353912830352783 | 0.0 | 0.0 | +e7c8751e-5d30-4953-9508-35488b6c45db / -3f253868-2de5-4189-95a0-705f62682958,fe3fea0b-bb55-4236-830e-828a00a9e529 |
| Jogador 4 | 3-7 | 434 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6070994138717651 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 435 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22344474494457245 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 436 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5681386590003967 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 437 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6854381561279297 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 438 | PASS | STABILIZE | 38.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 452 | BUY | STABILIZE | 38.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2718932628631592 | 0.0 | 0.0 | +02c8aff1-803e-42bc-b7c2-f7cd6d986b4f / -— |
| Jogador 4 | 4-1 | 453 | BUY | STABILIZE | 38.0 | 7 | 2 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.18261362612247467 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 4 | 4-1 | 454 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10688906162977219 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 455 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3719569444656372 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 456 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09864798933267593 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 457 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019963327795267105 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 458 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40779829025268555 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 459 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09864798933267593 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 460 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2477322667837143 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 461 | PASS | STABILIZE | 38.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 472 | BUY | STABILIZE | 38.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1695343405008316 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -— |
| Jogador 4 | 4-2 | 473 | REROLL | STABILIZE | 38.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 474 | SELL | STABILIZE | 38.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07900000363588333 | 0.0 | 0.0 | +— / -4cf7dfe2-9d2c-4d45-803e-503eda810357 |
| Jogador 4 | 4-2 | 475 | BUY | STABILIZE | 38.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15480762720108032 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 4 | 4-2 | 476 | SELL | STABILIZE | 38.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05537804961204529 | 0.0 | 0.0 | +— / -ddae48a6-5360-4660-9fa1-143ac35635ee |
| Jogador 4 | 4-2 | 477 | SELL | STABILIZE | 38.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5197625160217285 | 0.0 | 0.0 | +— / -320038b5-88c4-48fe-a7fa-a30823d674c0 |
| Jogador 4 | 4-2 | 478 | BUY | STABILIZE | 38.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6180263757705688 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 4 | 4-2 | 479 | REROLL | STABILIZE | 38.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 480 | SELL | STABILIZE | 38.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006599999964237213 | 0.0 | 0.0 | +— / -409b32b9-5280-4d79-b5b2-871ed597ba56 |
| Jogador 4 | 4-2 | 481 | BUY | STABILIZE | 38.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2839314639568329 | 0.0 | 0.0 | +31ea6d79-501d-4f2a-821d-7058334be82f / -— |
| Jogador 4 | 4-2 | 482 | PASS | STABILIZE | 38.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 492 | BUY | STABILIZE | 38.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12203262001276016 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 4 | 4-3 | 493 | SELL | STABILIZE | 38.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020392920821905136 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 4 | 4-3 | 494 | BUY | STABILIZE | 38.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15651555359363556 | 0.0 | 0.0 | +241a8a03-6e6f-4a9a-8550-e9154f3e1e76 / -— |
| Jogador 4 | 4-3 | 495 | REROLL | STABILIZE | 38.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 496 | SELL | STABILIZE | 38.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05700000002980232 | 0.0 | 0.0 | +— / -241a8a03-6e6f-4a9a-8550-e9154f3e1e76 |
| Jogador 4 | 4-3 | 497 | BUY | STABILIZE | 38.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2781417965888977 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 4 | 4-3 | 498 | REROLL | STABILIZE | 38.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 499 | SELL | STABILIZE | 38.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 4 | 4-3 | 500 | BUY | STABILIZE | 38.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8039268851280212 | 0.0 | 0.0 | +0fd34229-b814-4580-8651-59e712d5657f / -— |
| Jogador 4 | 4-3 | 501 | SELL | STABILIZE | 38.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030491948127746582 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 4 | 4-3 | 502 | PASS | STABILIZE | 38.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 512 | BUY | STABILIZE | 38.0 | 7 | 11 | 1 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7232265472412109 | 0.0 | 0.0 | +55cd39c0-65d5-410e-917e-501f584115fa / -— |
| Jogador 4 | 4-4 | 513 | REROLL | STABILIZE | 38.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 514 | SELL | STABILIZE | 38.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05700000002980232 | 0.0 | 0.0 | +— / -02c8aff1-803e-42bc-b7c2-f7cd6d986b4f |
| Jogador 4 | 4-4 | 515 | BUY | STABILIZE | 38.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8039059638977051 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -— |
| Jogador 4 | 4-4 | 516 | SELL | STABILIZE | 38.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3362307548522949 | 0.0 | 0.0 | +— / -d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 4 | 4-4 | 517 | BUY | STABILIZE | 38.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8336760401725769 | 0.0 | 0.0 | +da6c9f59-1fc3-467d-8845-bf7b38b4232c / -55cd39c0-65d5-410e-917e-501f584115fa,b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 4-4 | 518 | BUY | STABILIZE | 38.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05753369256854057 | 0.0 | 0.0 | +79b461e3-2c4f-40a2-b967-e0b6d5248bf6 / -— |
| Jogador 4 | 4-4 | 519 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46937018632888794 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 520 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 3 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11298274993896484 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 521 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2684757709503174 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 522 | PASS | STABILIZE | 38.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 532 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45072120428085327 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 533 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 9 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07763473689556122 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 534 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 9 | 0 | 34.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5708934664726257 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 535 | BUY | STABILIZE | 38.0 | 7 | 9 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11949846893548965 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 4 | 4-5 | 536 | REROLL | STABILIZE | 38.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 537 | SELL | STABILIZE | 38.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03842446953058243 | 0.0 | 0.0 | +— / -3faf4ab2-44b3-4779-985b-658c64791c28 |
| Jogador 4 | 4-5 | 538 | BUY | STABILIZE | 38.0 | 7 | 7 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28392186760902405 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -— |
| Jogador 4 | 4-5 | 539 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 4 | 0 | 38.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11938588321208954 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 540 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 4 | 0 | 38.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12090273201465607 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 541 | PASS | STABILIZE | 38.0 | 7 | 4 | 0 | 42.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 551 | SELL | STABILIZE | 27.0 | 7 | 9 | 0 | 42.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0605180598795414 | 0.0 | 0.0 | +— / -e7c8751e-5d30-4953-9508-35488b6c45db |
| Jogador 4 | 4-6 | 552 | BUY | STABILIZE | 27.0 | 7 | 14 | 1 | 42.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023122543469071388 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -— |
| Jogador 4 | 4-6 | 553 | REROLL | STABILIZE | 27.0 | 7 | 10 | 1 | 42.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 554 | SELL | STABILIZE | 27.0 | 7 | 8 | 0 | 42.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1510307639837265 | 0.0 | 0.0 | +— / -79b461e3-2c4f-40a2-b967-e0b6d5248bf6 |
| Jogador 4 | 4-6 | 555 | BUY | STABILIZE | 27.0 | 7 | 11 | 1 | 42.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7539849281311035 | 0.0 | 0.0 | +f1ece814-0986-421f-b5df-0b457ebaa484 / -45ae38c5-7e69-41bb-9a93-f14db3af3587,502a6e8c-8f81-456f-a1ef-c6bb8dd6fc7e |
| Jogador 4 | 4-6 | 556 | BUY | STABILIZE | 27.0 | 7 | 8 | 0 | 36.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024529431015253067 | 0.0 | 0.0 | +5184a53b-fca3-448c-b5ab-7daa37b0c259 / -— |
| Jogador 4 | 4-6 | 557 | REROLL | STABILIZE | 27.0 | 7 | 5 | 0 | 36.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 558 | SELL | STABILIZE | 27.0 | 7 | 3 | 0 | 36.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05700000002980232 | 0.0 | 0.0 | +— / -5184a53b-fca3-448c-b5ab-7daa37b0c259 |
| Jogador 4 | 4-6 | 559 | BUY | STABILIZE | 27.0 | 7 | 6 | 0 | 36.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2839946448802948 | 0.0 | 0.0 | +d8ca1093-815c-4f3e-af3e-fd6c4ab6ecd8 / -— |
| Jogador 4 | 4-6 | 560 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 3 | 0 | 36.0 | Adaptador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17731478810310364 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 561 | PASS | STABILIZE | 27.0 | 7 | 3 | 0 | 30.0 | Adaptador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 570 | SELL | ALL_IN | 13.0 | 7 | 9 | 0 | 30.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11853846162557602 | 0.0 | 0.0 | +— / -8e1a5a7a-d27d-47c9-a197-b383c1c3da3b |
| Jogador 4 | 4-7 | 571 | BUY | ALL_IN | 13.0 | 7 | 12 | 1 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010813375934958458 | 0.0 | 0.0 | +0d4bcb6c-af4b-4726-a600-d24420cb04bd / -— |
| Jogador 4 | 4-7 | 572 | REROLL | ALL_IN | 13.0 | 7 | 9 | 0 | 30.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 573 | MOVE_BENCH | ALL_IN | 13.0 | 7 | 7 | 0 | 30.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6164981722831726 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 574 | BUY | ALL_IN | 13.0 | 7 | 7 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7510104775428772 | 0.0 | 0.0 | +e15f057a-185e-4f99-8417-2c2b059912af / -— |
| Jogador 4 | 4-7 | 575 | REROLL | ALL_IN | 13.0 | 7 | 5 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 576 | SELL | ALL_IN | 13.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05466010421514511 | 0.0 | 0.0 | +— / -0d4bcb6c-af4b-4726-a600-d24420cb04bd |
| Jogador 4 | 4-7 | 577 | BUY | ALL_IN | 13.0 | 7 | 6 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8229029774665833 | 0.0 | 0.0 | +af23c553-04de-4813-87d0-bb7e4becafe4 / -0fd34229-b814-4580-8651-59e712d5657f,31ea6d79-501d-4f2a-821d-7058334be82f |
| Jogador 4 | 4-7 | 578 | BUY | ALL_IN | 13.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06539657711982727 | 0.0 | 0.0 | +472b4728-efd0-4853-a186-37811f40157a / -— |
| Jogador 4 | 4-7 | 579 | BUY | ALL_IN | 13.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2641662657260895 | 0.0 | 0.0 | +8ec344bd-ba9a-47e6-ba65-a4c832038b18 / -— |
| Jogador 4 | 4-7 | 580 | PASS | ALL_IN | 13.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 582 | ANVIL_CHOICE | ALL_IN | 13.0 | 7 | 6 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 583 | REROLL | ALL_IN | 13.0 | 7 | 6 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 584 | REROLL | ALL_IN | 13.0 | 7 | 4 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 585 | REROLL | ALL_IN | 13.0 | 7 | 2 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 586 | PASS | ALL_IN | 13.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5692920684814453 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.05371737480163574 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3658296465873718 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | -0.237098827958107 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 62 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22225287556648254 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3213253319263458 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.14091911911964417 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0628504678606987 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 66 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 92 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23595066368579865 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2991045117378235 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 94 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2611561715602875 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 95 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 122 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4489038586616516 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 123 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6585001945495605 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 124 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20563717186450958 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 125 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5912525057792664 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 126 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5150347352027893 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 127 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 148 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2597275674343109 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 149 | SELL | STABILIZE | 95.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32825183868408203 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 2-2 | 150 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 14.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26425379514694214 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 151 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21624259650707245 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 152 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2490224838256836 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 153 | PASS | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 172 | BUY_XP | STABILIZE | 90.0 | 4 | 13 | 1 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 173 | BUY_XP | STABILIZE | 90.0 | 4 | 9 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 174 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31555619835853577 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 175 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3781936764717102 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 176 | BUY_XP | STABILIZE | 90.0 | 5 | 4 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 177 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 0 | 0 | 20.0 | —/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1308051347732544 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 178 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 18.0 | —/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12813113629817963 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 179 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 18.0 | —/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 201 | SELL | STABILIZE | 90.0 | 5 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05194772407412529 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 202 | BUY | STABILIZE | 90.0 | 5 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3598727881908417 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 203 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 5 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0262315534055233 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 204 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 5 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7468810677528381 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 205 | PASS | STABILIZE | 90.0 | 5 | 5 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 227 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 10 | 1 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23837114870548248 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 228 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 10 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04394765943288803 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 229 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 10 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.307798832654953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 230 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4623282551765442 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 231 | PASS | STABILIZE | 90.0 | 5 | 10 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 252 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34133848547935486 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 253 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30728358030319214 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 254 | PASS | STABILIZE | 84.0 | 5 | 16 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020178571343421936 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 276 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 23 | 2 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.401350736618042 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 277 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 23 | 2 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13787490129470825 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 278 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 23 | 2 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3528718650341034 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 279 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 23 | 2 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7695196270942688 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 280 | PASS | STABILIZE | 84.0 | 5 | 23 | 2 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02142857201397419 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 302 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 30 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09690488129854202 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 303 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 30 | 3 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35290050506591797 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 304 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 30 | 3 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29332655668258667 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 305 | PASS | STABILIZE | 84.0 | 5 | 30 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12300000339746475 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 327 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 38 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009616700932383537 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 328 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 38 | 3 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7457655072212219 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 329 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 38 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3562847971916199 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 330 | PASS | STABILIZE | 75.0 | 5 | 38 | 3 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12700000405311584 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 349 | MOVE_BENCH | STABILIZE | 66.0 | 6 | 47 | 4 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1169070228934288 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 350 | MOVE_BENCH | STABILIZE | 66.0 | 6 | 47 | 4 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30651354789733887 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 351 | MOVE_BENCH | STABILIZE | 66.0 | 6 | 47 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46191203594207764 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 352 | PASS | STABILIZE | 66.0 | 6 | 47 | 4 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1315000057220459 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 364 | MOVE_BENCH | STABILIZE | 66.0 | 6 | 47 | 4 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5629612803459167 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 371 | BUY | STABILIZE | 66.0 | 6 | 57 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.008297538384795189 | 0.0 | 0.0 | +3a11170d-1b8e-4316-ad59-9a7e60071f12 / -— |
| Jogador 5 | 3-4 | 372 | BUY_XP | STABILIZE | 66.0 | 6 | 55 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004724999889731407 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 373 | BUY_XP | STABILIZE | 66.0 | 6 | 51 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08245625346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 374 | BUY_XP | STABILIZE | 66.0 | 6 | 47 | 4 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004456249997019768 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 375 | BUY_XP | STABILIZE | 66.0 | 6 | 43 | 4 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08445625007152557 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 376 | BUY_XP | STABILIZE | 66.0 | 6 | 39 | 3 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004456249997019768 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 377 | BUY_XP | STABILIZE | 66.0 | 6 | 35 | 3 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004456249997019768 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 378 | BUY_XP | STABILIZE | 66.0 | 6 | 31 | 3 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08445625007152557 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 379 | BUY_XP | STABILIZE | 66.0 | 6 | 27 | 2 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004456249997019768 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 380 | BUY_XP | STABILIZE | 66.0 | 6 | 23 | 2 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017319999635219574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 381 | PASS | STABILIZE | 66.0 | 7 | 19 | 1 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 392 | BUY | STABILIZE | 66.0 | 7 | 25 | 2 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003071403130888939 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 393 | MOVE_BENCH | STABILIZE | 66.0 | 7 | 21 | 2 | 24.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29557517170906067 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 394 | BUY_XP | FAST8 | 66.0 | 7 | 21 | 2 | 26.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 395 | BUY_XP | FAST8 | 66.0 | 7 | 17 | 1 | 26.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 396 | BUY_XP | FAST8 | 66.0 | 7 | 13 | 1 | 26.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 397 | BUY_XP | FAST8 | 66.0 | 7 | 9 | 0 | 26.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 398 | BUY_XP | FAST8 | 66.0 | 7 | 5 | 0 | 26.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 399 | MOVE_BOARD | FAST8 | 66.0 | 7 | 1 | 0 | 26.0 | Colosso/DA_18_Morgana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015130875632166862 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 400 | MOVE_BOARD | FAST8 | 66.0 | 7 | 1 | 0 | 26.0 | Colosso/DA_18_Morgana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12990932166576385 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 401 | PASS | FAST8 | 66.0 | 7 | 1 | 0 | 26.0 | Colosso/DA_18_Morgana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 412 | BUY | FAST8 | 66.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04279938340187073 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 413 | BUY | FAST8 | 66.0 | 7 | 5 | 0 | 26.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7379630208015442 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 414 | BUY_XP | FAST8 | 66.0 | 7 | 4 | 0 | 26.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 415 | PASS | FAST8 | 66.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_18_Morgana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 426 | MOVE_BENCH | FAST8 | 66.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_18_Morgana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6203569173812866 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 432 | BUY | FAST8 | 66.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2094329595565796 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 5 | 3-7 | 433 | BUY_XP | FAST8 | 66.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 434 | PASS | FAST8 | 66.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Morgana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 452 | BUY | FAST8 | 66.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21515707671642303 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 5 | 4-1 | 453 | BUY_XP | FAST8 | 66.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 454 | PASS | FAST8 | 66.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Morgana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 472 | BUY | FAST8 | 53.0 | 7 | 5 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10917990654706955 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 5 | 4-2 | 473 | PASS | FAST8 | 53.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 492 | BUY | FAST8 | 53.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7339045405387878 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 5 | 4-3 | 493 | BUY | FAST8 | 53.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7351590991020203 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 5 | 4-3 | 494 | BUY | FAST8 | 53.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2307814508676529 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 5 | 4-3 | 495 | PASS | FAST8 | 53.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Morgana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 512 | SELL | FAST8 | 53.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07072307914495468 | 0.0 | 0.0 | +— / -20821a31-3317-4f82-bbb2-b70cdebdd893 |
| Jogador 5 | 4-4 | 513 | BUY | FAST8 | 53.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2551935613155365 | 0.0 | 0.0 | +eeb774dc-b3d1-4a90-8a93-b71a9b754169 / -— |
| Jogador 5 | 4-4 | 514 | REROLL | FAST8 | 53.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 515 | SELL | FAST8 | 53.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Morgana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08030389994382858 | 0.0 | 0.0 | +— / -eeb774dc-b3d1-4a90-8a93-b71a9b754169 |
| Jogador 5 | 4-4 | 516 | BUY | FAST8 | 53.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_18_Morgana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7656585574150085 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb,6fb9f857-4ee1-4b52-8825-57f514dc2d0f |
| Jogador 5 | 4-4 | 517 | BUY | FAST8 | 53.0 | 7 | 5 | 0 | 26.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25431355834007263 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 5 | 4-4 | 518 | PASS | FAST8 | 53.0 | 7 | 3 | 0 | 26.0 | Colosso/DA_18_Sejuani | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 528 | MOVE_BENCH | FAST8 | 53.0 | 7 | 3 | 0 | 26.0 | Colosso/DA_18_Sejuani | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5483325719833374 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 532 | BUY | FAST8 | 53.0 | 7 | 9 | 0 | 32.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1289616823196411 | 0.0 | 0.0 | +91eb044c-6989-4b6a-a9fa-a59f75b56743 / -— |
| Jogador 5 | 4-5 | 533 | REROLL | FAST8 | 53.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 534 | SELL | FAST8 | 53.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07900000363588333 | 0.0 | 0.0 | +— / -b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 |
| Jogador 5 | 4-5 | 535 | BUY | FAST8 | 53.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21596506237983704 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -— |
| Jogador 5 | 4-5 | 536 | REROLL | FAST8 | 53.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_18_Sejuani | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 537 | PASS | FAST8 | 53.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 551 | SELL | FAST8 | 53.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13272307813167572 | 0.0 | 0.0 | +— / -29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 5 | 4-6 | 552 | BUY | FAST8 | 53.0 | 7 | 12 | 1 | 32.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7379231452941895 | 0.0 | 0.0 | +d47034a1-8b51-4b82-b1b4-5f2aee8f959a / -— |
| Jogador 5 | 4-6 | 553 | REROLL | FAST8 | 53.0 | 7 | 11 | 1 | 32.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 554 | SELL | FAST8 | 53.0 | 7 | 9 | 0 | 32.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39727693796157837 | 0.0 | 0.0 | +— / -a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 5 | 4-6 | 555 | BUY | FAST8 | 53.0 | 7 | 14 | 1 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7639639973640442 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -0f1b15a2-9978-4691-a15e-483ccd03db7f,3bfc4626-3226-44b6-a401-ff9c18761448 |
| Jogador 5 | 4-6 | 556 | BUY | FAST8 | 53.0 | 7 | 11 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6537403464317322 | 0.0 | 0.0 | +bfff6629-3ccc-4136-82a4-319a2fc5350e / -— |
| Jogador 5 | 4-6 | 557 | BUY | FAST8 | 53.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04648204892873764 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 5 | 4-6 | 558 | PASS | FAST8 | 53.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 570 | SELL | FAST8 | 39.0 | 7 | 10 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042567040771245956 | 0.0 | 0.0 | +— / -ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 |
| Jogador 5 | 4-7 | 571 | BUY | FAST8 | 39.0 | 7 | 13 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7638958096504211 | 0.0 | 0.0 | +f1c48e72-ce66-4b0d-ab88-5d965e06066b / -59304448-26ee-4e38-a52e-014e22ece127,bfff6629-3ccc-4136-82a4-319a2fc5350e |
| Jogador 5 | 4-7 | 572 | BUY | FAST8 | 39.0 | 7 | 10 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0020404295064508915 | 0.0 | 0.0 | +7904ab26-de3f-4144-b70f-ed620b41c907 / -— |
| Jogador 5 | 4-7 | 573 | MOVE_BENCH | FAST8 | 39.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10482501238584518 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 574 | MOVE_BENCH | FAST8 | 39.0 | 7 | 7 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6051638126373291 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 575 | BUY | FAST8 | 39.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5233853459358215 | 0.0 | 0.0 | +60290b49-92fb-48d4-a657-26afd1f3f662 / -— |
| Jogador 5 | 4-7 | 576 | REROLL | FAST8 | 39.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 577 | REROLL | FAST8 | 39.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 578 | PASS | FAST8 | 39.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 582 | ANVIL_CHOICE | STABILIZE | 39.0 | 8 | 5 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 583 | SELL | STABILIZE | 39.0 | 8 | 5 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3346411883831024 | 0.0 | 0.0 | +— / -7904ab26-de3f-4144-b70f-ed620b41c907 |
| Jogador 5 | 5-1 | 584 | BUY | STABILIZE | 39.0 | 8 | 8 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8055703043937683 | 0.0 | 0.0 | +2adb37ce-c46e-4c3a-a715-443bdb688103 / -— |
| Jogador 5 | 5-1 | 585 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 6 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2100275754928589 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 586 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 6 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.01890616863965988 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 587 | PASS | STABILIZE | 39.0 | 8 | 6 | 0 | 40.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 595 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 6 | 0 | 40.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6202546954154968 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 601 | BUY | STABILIZE | 22.0 | 8 | 12 | 1 | 48.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.032687991857528687 | 0.0 | 0.0 | +ac2e2c72-371d-478d-a3f2-32d51e71f567 / -— |
| Jogador 5 | 5-2 | 602 | REROLL | STABILIZE | 22.0 | 8 | 7 | 0 | 48.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 603 | SELL | STABILIZE | 22.0 | 8 | 5 | 0 | 48.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03811521828174591 | 0.0 | 0.0 | +— / -df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 5-2 | 604 | BUY | STABILIZE | 22.0 | 8 | 7 | 0 | 48.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8013227581977844 | 0.0 | 0.0 | +9b711f23-11ec-4049-b5e4-b0623b01204e / -— |
| Jogador 5 | 5-2 | 605 | SELL | STABILIZE | 22.0 | 8 | 4 | 0 | 48.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3933858275413513 | 0.0 | 0.0 | +— / -497fbcb9-9d15-43f0-ad71-96eeceeee99d |
| Jogador 5 | 5-2 | 606 | BUY | STABILIZE | 22.0 | 8 | 12 | 1 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04828779026865959 | 0.0 | 0.0 | +f074442b-5ccc-4174-ac90-ef9eb358f8c1 / -— |
| Jogador 5 | 5-2 | 607 | REROLL | STABILIZE | 22.0 | 8 | 8 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 608 | SELL | STABILIZE | 22.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13272307813167572 | 0.0 | 0.0 | +— / -f074442b-5ccc-4174-ac90-ef9eb358f8c1 |
| Jogador 5 | 5-2 | 609 | BUY | STABILIZE | 22.0 | 8 | 10 | 1 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19973798096179962 | 0.0 | 0.0 | +72ffdfa0-5a48-4c08-a7b4-5dbd9d59df51 / -— |
| Jogador 5 | 5-2 | 610 | SELL | STABILIZE | 22.0 | 8 | 5 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.8365190625190735 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 5-2 | 611 | PASS | STABILIZE | 22.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 619 | BUY | STABILIZE | 22.0 | 8 | 12 | 1 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7056925296783447 | 0.0 | 0.0 | +530cb5ca-dea2-47db-ba63-38133c49eb12 / -— |
| Jogador 5 | 5-3 | 620 | REROLL | STABILIZE | 22.0 | 8 | 9 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 621 | SELL | STABILIZE | 22.0 | 8 | 7 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.30766451358795166 | 0.0 | 0.0 | +— / -530cb5ca-dea2-47db-ba63-38133c49eb12 |
| Jogador 5 | 5-3 | 622 | BUY | STABILIZE | 22.0 | 8 | 10 | 1 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7559261918067932 | 0.0 | 0.0 | +cd715559-798e-4752-8df7-ee70ca67d8a1 / -2adb37ce-c46e-4c3a-a715-443bdb688103,ef54ddfd-f436-4813-9585-cb652488ffa3 |
| Jogador 5 | 5-3 | 623 | BUY | STABILIZE | 22.0 | 8 | 8 | 0 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.653191089630127 | 0.0 | 0.0 | +68e8df20-cef6-4099-9daa-8fd4180c1a0d / -— |
| Jogador 5 | 5-3 | 624 | BUY | STABILIZE | 22.0 | 8 | 5 | 0 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2326774001121521 | 0.0 | 0.0 | +c131e810-debd-4555-b9eb-9b542cdd3f78 / -— |
| Jogador 5 | 5-3 | 625 | REROLL | STABILIZE | 22.0 | 8 | 2 | 0 | 48.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 626 | SELL | STABILIZE | 22.0 | 8 | 0 | 0 | 48.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07103076577186584 | 0.0 | 0.0 | +— / -c131e810-debd-4555-b9eb-9b542cdd3f78 |
| Jogador 5 | 5-3 | 627 | BUY | STABILIZE | 22.0 | 8 | 3 | 0 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.23287075757980347 | 0.0 | 0.0 | +38b4cb27-ddc9-4488-9d22-eca4612a4bd8 / -— |
| Jogador 5 | 5-3 | 628 | SELL | STABILIZE | 22.0 | 8 | 0 | 0 | 48.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07103076577186584 | 0.0 | 0.0 | +— / -38b4cb27-ddc9-4488-9d22-eca4612a4bd8 |
| Jogador 5 | 5-3 | 629 | PASS | STABILIZE | 22.0 | 8 | 3 | 0 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 632 | BUY | ALL_IN | 8.0 | 8 | 8 | 0 | 48.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.753044843673706 | 0.0 | 0.0 | +bb2609fb-c8cb-4e7a-b308-8cd512ff870d / -68cd8ae3-399f-461f-89a8-189d7b0a6b59,68e8df20-cef6-4099-9daa-8fd4180c1a0d |
| Jogador 5 | 5-4 | 633 | BUY | ALL_IN | 8.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1311185359954834 | 0.0 | 0.0 | +0474e055-4633-408f-837c-b93b86fa46be / -— |
| Jogador 5 | 5-4 | 634 | CRAFT_AND_EQUIP | ALL_IN | 8.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08450881391763687 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 635 | SELL | ALL_IN | 8.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033188462257385254 | 0.0 | 0.0 | +— / -0474e055-4633-408f-837c-b93b86fa46be |
| Jogador 5 | 5-4 | 636 | BUY | ALL_IN | 8.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1711573302745819 | 0.0 | 0.0 | +fe0cdc83-3953-4aad-86c0-cf907a803a8f / -— |
| Jogador 5 | 5-4 | 637 | REROLL | ALL_IN | 8.0 | 8 | 3 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 638 | SELL | ALL_IN | 8.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019114792346954346 | 0.0 | 0.0 | +— / -fe0cdc83-3953-4aad-86c0-cf907a803a8f |
| Jogador 5 | 5-4 | 639 | BUY | ALL_IN | 8.0 | 8 | 3 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0689144879579544 | 0.0 | 0.0 | +41a8da11-61e8-4789-938a-80895b9216f2 / -— |
| Jogador 5 | 5-4 | 640 | SELL | ALL_IN | 8.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038538459688425064 | 0.0 | 0.0 | +— / -41a8da11-61e8-4789-938a-80895b9216f2 |
| Jogador 5 | 5-4 | 641 | BUY | ALL_IN | 8.0 | 8 | 3 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08407363295555115 | 0.0 | 0.0 | +4dd42303-55f8-4677-9669-f8f7ecf895ae / -— |
| Jogador 5 | 5-4 | 642 | PASS | ALL_IN | 8.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 651 | SELL | ALL_IN | 8.0 | 8 | 6 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03785644844174385 | 0.0 | 0.0 | +— / -4dd42303-55f8-4677-9669-f8f7ecf895ae |
| Jogador 5 | 5-5 | 652 | BUY | ALL_IN | 8.0 | 8 | 8 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2739908695220947 | 0.0 | 0.0 | +d14fbb79-be91-410c-8ac7-065e9d02620c / -— |
| Jogador 5 | 5-5 | 653 | SELL | ALL_IN | 8.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4037081003189087 | 0.0 | 0.0 | +— / -cd715559-798e-4752-8df7-ee70ca67d8a1 |
| Jogador 5 | 5-5 | 654 | BUY | ALL_IN | 8.0 | 8 | 10 | 1 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.148755744099617 | 0.0 | 0.0 | +876b71be-47f0-45df-800e-d40cb8905423 / -— |
| Jogador 5 | 5-5 | 655 | SELL | ALL_IN | 8.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11853846162557602 | 0.0 | 0.0 | +— / -876b71be-47f0-45df-800e-d40cb8905423 |
| Jogador 5 | 5-5 | 656 | BUY | ALL_IN | 8.0 | 8 | 10 | 1 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1487559825181961 | 0.0 | 0.0 | +ec337b44-d045-465d-9aa7-155637f289b8 / -— |
| Jogador 5 | 5-5 | 657 | REROLL | ALL_IN | 8.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 658 | SELL | ALL_IN | 8.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038538459688425064 | 0.0 | 0.0 | +— / -ec337b44-d045-465d-9aa7-155637f289b8 |
| Jogador 5 | 5-5 | 659 | BUY | ALL_IN | 8.0 | 8 | 8 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2609172463417053 | 0.0 | 0.0 | +f1d000f5-290e-44e3-b682-124fe695acf2 / -— |
| Jogador 5 | 5-5 | 660 | SELL | ALL_IN | 8.0 | 8 | 3 | 0 | 42.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2833857238292694 | 0.0 | 0.0 | +— / -bb2609fb-c8cb-4e7a-b308-8cd512ff870d |
| Jogador 5 | 5-5 | 661 | PASS | ALL_IN | 8.0 | 8 | 11 | 1 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +5fb26eae-800c-4f7a-8caa-e94d36794159 / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.6121415495872498 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032908253371715546 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017233550548553467 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.2239539474248886 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 62 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08310991525650024 | 0.0 | 0.0 | +f29b0444-8dd6-44a6-9a04-824febf737a0 / -— |
| Jogador 6 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27540284395217896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Caitlyn | MOVE_BOARD, PASS | True | True | 0.17796212434768677 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 65 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 92 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2617354989051819 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1188710629940033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 94 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.722357451915741 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 95 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 122 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24487747251987457 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 123 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47726085782051086 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 124 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13613437116146088 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 125 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09381663799285889 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 126 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24676907062530518 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 127 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 148 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6200312972068787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 149 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09881820529699326 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 150 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 172 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 15 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2490779459476471 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 173 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1898936927318573 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 174 | PASS | STABILIZE | 100.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019999999552965164 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 201 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 23 | 2 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8274853825569153 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 202 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 23 | 2 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09292692691087723 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 203 | PASS | STABILIZE | 100.0 | 4 | 23 | 2 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02142857201397419 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 227 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 31 | 3 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030160395428538322 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 228 | SELL | STABILIZE | 100.0 | 4 | 31 | 3 | 16.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015270507894456387 | 0.0 | 0.0 | +— / -4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 |
| Jogador 6 | 2-5 | 229 | BUY | STABILIZE | 100.0 | 4 | 33 | 3 | 16.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3924732208251953 | 0.0 | 0.0 | +0c6afd45-be8c-4f89-8fdc-938247537ab9 / -— |
| Jogador 6 | 2-5 | 230 | BUY_XP | STABILIZE | 100.0 | 4 | 32 | 3 | 16.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018515000119805336 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 231 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 28 | 2 | 16.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7355195879936218 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 232 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 28 | 2 | 16.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06985551863908768 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 233 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 28 | 2 | 12.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3295919895172119 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 234 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 28 | 2 | 16.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.593282163143158 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 235 | BUY | STABILIZE | 100.0 | 5 | 28 | 2 | 18.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.36510562896728516 | 0.0 | 0.0 | +f957e607-dd51-492b-9186-252da4e0c12f / -— |
| Jogador 6 | 2-5 | 236 | BUY_XP | STABILIZE | 100.0 | 5 | 27 | 2 | 18.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 237 | PASS | STABILIZE | 100.0 | 5 | 23 | 2 | 18.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02142857201397419 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 252 | SELL | STABILIZE | 100.0 | 5 | 32 | 3 | 18.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41924068331718445 | 0.0 | 0.0 | +— / -f957e607-dd51-492b-9186-252da4e0c12f |
| Jogador 6 | 2-6 | 253 | BUY | STABILIZE | 100.0 | 5 | 33 | 3 | 18.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9374206066131592 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 254 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 30 | 3 | 18.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 255 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 30 | 3 | 18.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42697879672050476 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 256 | PASS | SLOWROLL | 100.0 | 5 | 30 | 3 | 22.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03767857328057289 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 276 | SELL | SLOWROLL | 100.0 | 5 | 41 | 4 | 22.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4772557318210602 | 0.0 | 0.0 | +— / -5fb26eae-800c-4f7a-8caa-e94d36794159 |
| Jogador 6 | 2-7 | 277 | BUY | SLOWROLL | 100.0 | 5 | 42 | 4 | 22.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22261102497577667 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 278 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 39 | 3 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017693234607577324 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 279 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 39 | 3 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 280 | PASS | SLOWROLL | 100.0 | 5 | 39 | 3 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03928571566939354 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 302 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 49 | 4 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2889300286769867 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 303 | BUY | SLOWROLL | 100.0 | 5 | 49 | 4 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7909464240074158 | 0.0 | 0.0 | +ab127012-83d7-46f0-a16c-b20582d1179b / -— |
| Jogador 6 | 3-1 | 304 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 47 | 4 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08740752190351486 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 305 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 47 | 4 | 20.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3760998547077179 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 306 | BUY_XP | SLOWROLL | 100.0 | 5 | 47 | 4 | 24.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 307 | BUY_XP | SLOWROLL | 100.0 | 5 | 43 | 4 | 24.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024010000750422478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 308 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 39 | 3 | 24.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31996166706085205 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 309 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 39 | 3 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04947143420577049 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 310 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 39 | 3 | 20.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46607735753059387 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 311 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 39 | 3 | 24.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3167060613632202 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 312 | PASS | SLOWROLL | 100.0 | 6 | 39 | 3 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10999999940395355 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 327 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 47 | 4 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08759652823209763 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 328 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 47 | 4 | 20.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45221200585365295 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 329 | MOVE_BENCH | FAST8 | 89.0 | 6 | 47 | 4 | 26.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4824606776237488 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 330 | MOVE_BENCH | FAST8 | 89.0 | 6 | 47 | 4 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01700025051832199 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 331 | PASS | FAST8 | 89.0 | 6 | 47 | 4 | 30.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1315000057220459 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 349 | BUY | FAST8 | 89.0 | 6 | 57 | 5 | 30.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9184994697570801 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -2938180d-94e5-4bb7-832e-baa51f820ba2,75005e9c-56d1-48d6-815e-573e489e3dd7 |
| Jogador 6 | 3-3 | 350 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 54 | 5 | 18.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30106425285339355 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 351 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 54 | 5 | 24.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4803693890571594 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 352 | PASS | FAST8 | 89.0 | 6 | 54 | 5 | 26.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15552203357219696 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 364 | MOVE_BENCH | FAST8 | 89.0 | 6 | 54 | 5 | 26.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2984481155872345 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 371 | BUY | FAST8 | 79.0 | 6 | 64 | 5 | 28.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9339197874069214 | 0.0 | 0.0 | +4698e3b3-0833-4895-a1f1-26b372b2f965 / -ab127012-83d7-46f0-a16c-b20582d1179b,c19cf6a8-c66e-4670-b0fc-fb83453f22e7 |
| Jogador 6 | 3-4 | 372 | MOVE_BENCH | SLOWROLL | 79.0 | 6 | 62 | 5 | 24.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07932139933109283 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 373 | MOVE_BENCH | SLOWROLL | 79.0 | 6 | 62 | 5 | 20.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30267971754074097 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 374 | MOVE_BENCH | FAST8 | 79.0 | 6 | 62 | 5 | 26.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48631444573402405 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 375 | PASS | SLOWROLL | 79.0 | 6 | 62 | 5 | 24.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12759634852409363 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 389 | MOVE_BENCH | SLOWROLL | 79.0 | 6 | 62 | 5 | 24.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4761488437652588 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 392 | BUY | FAST8 | 79.0 | 6 | 72 | 5 | 32.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2998026907444 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 6 | 3-5 | 393 | MOVE_BENCH | FAST8 | 79.0 | 6 | 69 | 5 | 32.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26574021577835083 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 394 | MOVE_BENCH | FAST8 | 79.0 | 6 | 69 | 5 | 32.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7266246676445007 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 395 | BUY | FAST8 | 79.0 | 6 | 69 | 5 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8710602521896362 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-5 | 396 | BUY_XP | FAST8 | 79.0 | 6 | 67 | 5 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 397 | BUY_XP | FAST8 | 79.0 | 6 | 63 | 5 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 398 | BUY_XP | FAST8 | 79.0 | 6 | 59 | 5 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 399 | BUY_XP | FAST8 | 79.0 | 6 | 55 | 5 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 400 | BUY_XP | FAST8 | 79.0 | 6 | 51 | 5 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07654999941587448 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 401 | BUY_XP | FAST8 | 79.0 | 6 | 47 | 4 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 402 | PASS | FAST8 | 79.0 | 6 | 43 | 4 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12950000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 412 | BUY | FAST8 | 69.0 | 6 | 53 | 5 | 38.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9201148748397827 | 0.0 | 0.0 | +ab050f92-777b-429f-9ed8-9b6c63794641 / -5b95b64a-b46a-4827-8613-307c8dadc072,f29b0444-8dd6-44a6-9a04-824febf737a0 |
| Jogador 6 | 3-6 | 413 | BUY | FAST8 | 69.0 | 6 | 51 | 5 | 34.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24431444704532623 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -— |
| Jogador 6 | 3-6 | 414 | BUY | FAST8 | 69.0 | 6 | 49 | 4 | 34.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.244300976395607 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 415 | BUY_XP | FAST8 | 69.0 | 6 | 46 | 4 | 34.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08250000327825546 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 416 | MOVE_BENCH | FAST8 | 69.0 | 7 | 42 | 4 | 34.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014277387410402298 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 417 | MOVE_BENCH | FAST8 | 69.0 | 7 | 42 | 4 | 36.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29201236367225647 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 418 | BUY_XP | FAST8 | 69.0 | 7 | 42 | 4 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10827499628067017 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 419 | BUY_XP | FAST8 | 69.0 | 7 | 38 | 3 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 420 | BUY_XP | FAST8 | 69.0 | 7 | 34 | 3 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 421 | BUY_XP | FAST8 | 69.0 | 7 | 30 | 3 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10827499628067017 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 422 | PASS | FAST8 | 69.0 | 7 | 26 | 2 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07900000363588333 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 432 | BUY | FAST8 | 60.0 | 7 | 34 | 3 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7842339277267456 | 0.0 | 0.0 | +48be5cb2-e7b3-41f8-b212-79e21249fa6a / -— |
| Jogador 6 | 3-7 | 433 | BUY | FAST8 | 60.0 | 7 | 32 | 3 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10045737028121948 | 0.0 | 0.0 | +f8d6cf7b-e18c-4a52-87c6-8858f03eef72 / -— |
| Jogador 6 | 3-7 | 434 | BUY | FAST8 | 60.0 | 7 | 27 | 2 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048721738159656525 | 0.0 | 0.0 | +d885db3e-3cc6-466d-8a25-37f632c5db40 / -— |
| Jogador 6 | 3-7 | 435 | BUY | FAST8 | 60.0 | 7 | 23 | 2 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11141090840101242 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 6 | 3-7 | 436 | BUY | FAST8 | 60.0 | 7 | 21 | 2 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17766647040843964 | 0.0 | 0.0 | +15d93457-0760-419e-87db-74223c1cb7f4 / -— |
| Jogador 6 | 3-7 | 437 | REROLL | FAST8 | 60.0 | 7 | 20 | 2 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 438 | BUY | FAST8 | 60.0 | 7 | 18 | 1 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7251598834991455 | 0.0 | 0.0 | +ddf39480-6ce0-46d0-ac45-57114245ffba / -— |
| Jogador 6 | 3-7 | 439 | BUY | FAST8 | 60.0 | 7 | 15 | 1 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27897199988365173 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -— |
| Jogador 6 | 3-7 | 440 | REROLL | FAST8 | 60.0 | 7 | 12 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 441 | SELL | FAST8 | 60.0 | 7 | 10 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06513368338346481 | 0.0 | 0.0 | +— / -15d93457-0760-419e-87db-74223c1cb7f4 |
| Jogador 6 | 3-7 | 442 | PASS | FAST8 | 60.0 | 7 | 11 | 1 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 452 | BUY | FAST8 | 60.0 | 7 | 18 | 1 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19039514660835266 | 0.0 | 0.0 | +00f38555-1887-4fe2-9930-934055269095 / -— |
| Jogador 6 | 4-1 | 453 | REROLL | FAST8 | 60.0 | 7 | 14 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 454 | SELL | FAST8 | 60.0 | 7 | 12 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018704364076256752 | 0.0 | 0.0 | +— / -f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 6 | 4-1 | 455 | BUY | FAST8 | 60.0 | 7 | 14 | 1 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7373531460762024 | 0.0 | 0.0 | +84886290-556f-45e9-805b-9ca86a80ba27 / -— |
| Jogador 6 | 4-1 | 456 | REROLL | FAST8 | 60.0 | 7 | 13 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 457 | SELL | FAST8 | 60.0 | 7 | 11 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03161538392305374 | 0.0 | 0.0 | +— / -cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 4-1 | 458 | BUY | FAST8 | 60.0 | 7 | 14 | 1 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027241094037890434 | 0.0 | 0.0 | +506f421d-7a3c-46d7-9cac-6c107bc35e31 / -— |
| Jogador 6 | 4-1 | 459 | SELL | FAST8 | 60.0 | 7 | 11 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08100000023841858 | 0.0 | 0.0 | +— / -cc56fedc-f555-4075-af15-6b5fb93a156f |
| Jogador 6 | 4-1 | 460 | BUY | FAST8 | 60.0 | 7 | 14 | 1 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11384045332670212 | 0.0 | 0.0 | +395ae945-c8a2-4d80-98a4-5eb6887b8f78 / -— |
| Jogador 6 | 4-1 | 461 | REROLL | FAST8 | 60.0 | 7 | 12 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 462 | PASS | FAST8 | 60.0 | 7 | 10 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 472 | SELL | FAST8 | 46.0 | 7 | 17 | 1 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01963573507964611 | 0.0 | 0.0 | +— / -395ae945-c8a2-4d80-98a4-5eb6887b8f78 |
| Jogador 6 | 4-2 | 473 | BUY | FAST8 | 46.0 | 7 | 19 | 1 | 42.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7560736536979675 | 0.0 | 0.0 | +ed23d828-f4bc-4d6c-8cc1-c074047dac8a / -06db3a99-d008-406a-ac86-30884335d7c2,ddf39480-6ce0-46d0-ac45-57114245ffba |
| Jogador 6 | 4-2 | 474 | BUY | FAST8 | 46.0 | 7 | 16 | 1 | 36.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7199578285217285 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 6 | 4-2 | 475 | MOVE_BENCH | FAST8 | 46.0 | 7 | 13 | 1 | 36.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2201295793056488 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 476 | REROLL | FAST8 | 46.0 | 7 | 13 | 1 | 36.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 477 | SELL | FAST8 | 46.0 | 7 | 11 | 1 | 36.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055725786834955215 | 0.0 | 0.0 | +— / -506f421d-7a3c-46d7-9cac-6c107bc35e31 |
| Jogador 6 | 4-2 | 478 | BUY | FAST8 | 46.0 | 7 | 14 | 1 | 36.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2084488421678543 | 0.0 | 0.0 | +fcc4f620-7b85-40ed-a42c-2eadd37a82fd / -— |
| Jogador 6 | 4-2 | 479 | REROLL | FAST8 | 46.0 | 7 | 11 | 1 | 36.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 480 | SELL | FAST8 | 46.0 | 7 | 9 | 0 | 36.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048384614288806915 | 0.0 | 0.0 | +— / -fcc4f620-7b85-40ed-a42c-2eadd37a82fd |
| Jogador 6 | 4-2 | 481 | BUY | FAST8 | 46.0 | 7 | 12 | 1 | 36.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.765104353427887 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -48be5cb2-e7b3-41f8-b212-79e21249fa6a,ab472080-6e4b-4b75-b37d-cf10da9a5a0d |
| Jogador 6 | 4-2 | 482 | PASS | FAST8 | 46.0 | 7 | 10 | 1 | 36.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 492 | BUY | STABILIZE | 34.0 | 7 | 18 | 1 | 36.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2111448347568512 | 0.0 | 0.0 | +673bda2e-1343-4894-8005-c3ee2c90f1b7 / -— |
| Jogador 6 | 4-3 | 493 | BUY | STABILIZE | 34.0 | 7 | 15 | 1 | 36.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013700625859200954 | 0.0 | 0.0 | +5c931416-3aeb-40d4-9e6f-612b0d387226 / -— |
| Jogador 6 | 4-3 | 494 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 12 | 1 | 36.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2195039689540863 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 495 | BUY | STABILIZE | 34.0 | 7 | 12 | 1 | 44.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3647282123565674 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 6 | 4-3 | 496 | REROLL | STABILIZE | 34.0 | 7 | 9 | 0 | 44.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 497 | SELL | STABILIZE | 34.0 | 7 | 7 | 0 | 44.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2377692312002182 | 0.0 | 0.0 | +— / -5c931416-3aeb-40d4-9e6f-612b0d387226 |
| Jogador 6 | 4-3 | 498 | BUY | STABILIZE | 34.0 | 7 | 10 | 1 | 44.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19983692467212677 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 6 | 4-3 | 499 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 7 | 0 | 44.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.204582080245018 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 500 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 7 | 0 | 42.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6456233263015747 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 501 | BUY | STABILIZE | 34.0 | 7 | 7 | 0 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6408401131629944 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 6 | 4-3 | 502 | PASS | STABILIZE | 34.0 | 7 | 3 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 512 | SELL | STABILIZE | 34.0 | 7 | 9 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08642333000898361 | 0.0 | 0.0 | +— / -673bda2e-1343-4894-8005-c3ee2c90f1b7 |
| Jogador 6 | 4-4 | 513 | BUY | STABILIZE | 34.0 | 7 | 12 | 1 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053214382380247116 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 6 | 4-4 | 514 | REROLL | STABILIZE | 34.0 | 7 | 9 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 515 | SELL | STABILIZE | 34.0 | 7 | 7 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12001538276672363 | 0.0 | 0.0 | +— / -d78561b4-3dcc-42fb-9983-2ed5d62f8606 |
| Jogador 6 | 4-4 | 516 | BUY | STABILIZE | 34.0 | 7 | 10 | 1 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19712866842746735 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 6 | 4-4 | 517 | REROLL | STABILIZE | 34.0 | 7 | 7 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 518 | REROLL | STABILIZE | 34.0 | 7 | 5 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 519 | SELL | STABILIZE | 34.0 | 7 | 3 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03161538392305374 | 0.0 | 0.0 | +— / -b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 6 | 4-4 | 520 | BUY | STABILIZE | 34.0 | 7 | 6 | 0 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27712923288345337 | 0.0 | 0.0 | +a1357716-abf4-4d4f-abb8-34f2681f16dd / -— |
| Jogador 6 | 4-4 | 521 | REROLL | STABILIZE | 34.0 | 7 | 3 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 522 | PASS | STABILIZE | 34.0 | 7 | 1 | 0 | 50.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 532 | REROLL | STABILIZE | 34.0 | 7 | 6 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 533 | REROLL | STABILIZE | 34.0 | 7 | 4 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 534 | REROLL | STABILIZE | 34.0 | 7 | 2 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 535 | SELL | STABILIZE | 34.0 | 7 | 0 | 0 | 50.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03161538392305374 | 0.0 | 0.0 | +— / -a1357716-abf4-4d4f-abb8-34f2681f16dd |
| Jogador 6 | 4-5 | 536 | BUY | STABILIZE | 34.0 | 7 | 3 | 0 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11575067788362503 | 0.0 | 0.0 | +b58c0c0e-9c6f-4977-91d1-177b7113c439 / -— |
| Jogador 6 | 4-5 | 537 | PASS | STABILIZE | 34.0 | 7 | 0 | 0 | 50.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 551 | SELL | STABILIZE | 22.0 | 7 | 5 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03725021332502365 | 0.0 | 0.0 | +— / -b58c0c0e-9c6f-4977-91d1-177b7113c439 |
| Jogador 6 | 4-6 | 552 | BUY | STABILIZE | 22.0 | 7 | 8 | 0 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2857975363731384 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 6 | 4-6 | 553 | REROLL | STABILIZE | 22.0 | 7 | 6 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 554 | SELL | STABILIZE | 22.0 | 7 | 4 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3405076861381531 | 0.0 | 0.0 | +— / -d885db3e-3cc6-466d-8a25-37f632c5db40 |
| Jogador 6 | 4-6 | 555 | BUY | STABILIZE | 22.0 | 7 | 8 | 0 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2858634293079376 | 0.0 | 0.0 | +13169f05-0cd0-4012-89a6-7b47246b475e / -— |
| Jogador 6 | 4-6 | 556 | REROLL | STABILIZE | 22.0 | 7 | 6 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 557 | REROLL | STABILIZE | 22.0 | 7 | 4 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 558 | REROLL | STABILIZE | 22.0 | 7 | 2 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 559 | PASS | STABILIZE | 22.0 | 7 | 0 | 0 | 50.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 570 | SELL | STABILIZE | 22.0 | 7 | 5 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034261539578437805 | 0.0 | 0.0 | +— / -24b29fe6-466c-42d5-9f92-5d6114f0f98f |
| Jogador 6 | 4-7 | 571 | BUY | STABILIZE | 22.0 | 7 | 9 | 0 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8058419227600098 | 0.0 | 0.0 | +19e8f3ef-c3a6-459e-bf05-a53f742ba05d / -— |
| Jogador 6 | 4-7 | 572 | REROLL | STABILIZE | 22.0 | 7 | 7 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 573 | REROLL | STABILIZE | 22.0 | 7 | 5 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 574 | REROLL | STABILIZE | 22.0 | 7 | 3 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 575 | PASS | STABILIZE | 22.0 | 7 | 1 | 0 | 50.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 582 | ANVIL_CHOICE | STABILIZE | 22.0 | 7 | 6 | 0 | 50.0 | Devastador/DA_18_Rammus | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 583 | SELL | STABILIZE | 22.0 | 7 | 6 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7519506812095642 | 0.0 | 0.0 | +— / -8aa832ec-4c09-43bd-ae21-baf7268e468d |
| Jogador 6 | 5-1 | 584 | BUY | STABILIZE | 22.0 | 7 | 11 | 1 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7155418395996094 | 0.0 | 0.0 | +3acea3a8-5fa8-441c-85bc-59b2c30e9730 / -— |
| Jogador 6 | 5-1 | 585 | REROLL | STABILIZE | 22.0 | 7 | 8 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 586 | REROLL | STABILIZE | 22.0 | 7 | 6 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 587 | REROLL | STABILIZE | 22.0 | 7 | 4 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 588 | REROLL | STABILIZE | 22.0 | 7 | 2 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 589 | CRAFT_AND_EQUIP | STABILIZE | 22.0 | 7 | 0 | 0 | 50.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18103380501270294 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 590 | PASS | STABILIZE | 22.0 | 7 | 0 | 0 | 50.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 601 | SELL | ALL_IN | 7.0 | 7 | 6 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7972040176391602 | 0.0 | 0.0 | +— / -84886290-556f-45e9-805b-9ca86a80ba27 |
| Jogador 6 | 5-2 | 602 | BUY | ALL_IN | 7.0 | 7 | 7 | 0 | 50.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26719778776168823 | 0.0 | 0.0 | +703b70a3-3aca-4ecd-86da-0a1b34e4bb3a / -— |
| Jogador 6 | 5-2 | 603 | REROLL | ALL_IN | 7.0 | 7 | 3 | 0 | 50.0 | Devastador/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 604 | PASS | ALL_IN | 7.0 | 7 | 1 | 0 | 50.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6121415495872498 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0808350220322609 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33619609475135803 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 1.0300270318984985 | 0.0 | 0.0 | +a529e9b4-89c2-47e0-b821-7269b112f8ef / -— |
| Jogador 7 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5446590781211853 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 62 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2145349532365799 | 0.0 | 0.0 | +42edb83f-b613-45e2-95e2-d603ddf9d104 / -— |
| Jogador 7 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21236151456832886 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 64 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 92 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 93 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8436985015869141 | 0.0 | 0.0 | +— / -a529e9b4-89c2-47e0-b821-7269b112f8ef |
| Jogador 7 | 1-4 | 94 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.022884488105774 | 0.0 | 0.0 | +a179e7d4-31e2-4a74-9905-0daede16517e / -— |
| Jogador 7 | 1-4 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 96 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2934668958187103 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 97 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 122 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3745430111885071 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 123 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19803185760974884 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 124 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018009506165981293 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 125 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 126 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 14.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03263518214225769 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 127 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 14.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 148 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05711591988801956 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 2-2 | 149 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.34725552797317505 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 150 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32289522886276245 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 151 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 152 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 172 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 11 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5466405153274536 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 173 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32289522886276245 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 174 | PASS | STABILIZE | 100.0 | 4 | 11 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 201 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 17 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 202 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 17 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4415782392024994 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 203 | BUY | SLOWROLL | 94.0 | 5 | 17 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26730018854141235 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 204 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 13 | 1 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.288051575422287 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 205 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 13 | 1 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 206 | PASS | SLOWROLL | 94.0 | 5 | 13 | 1 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 227 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 19 | 1 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.645287275314331 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 228 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 19 | 1 | 20.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20317862927913666 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 229 | PASS | SLOWROLL | 94.0 | 5 | 19 | 1 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020714284852147102 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 252 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 27 | 2 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 253 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 27 | 2 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8041101694107056 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 254 | PASS | SLOWROLL | 94.0 | 5 | 27 | 2 | 22.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022142857313156128 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 276 | MOVE_BENCH | SLOWROLL | 88.0 | 5 | 34 | 3 | 22.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5695439577102661 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 277 | MOVE_BENCH | SLOWROLL | 88.0 | 5 | 34 | 3 | 20.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19355766475200653 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 278 | PASS | SLOWROLL | 88.0 | 5 | 34 | 3 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03839285671710968 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 302 | MOVE_BENCH | SLOWROLL | 88.0 | 5 | 42 | 4 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8045380711555481 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 303 | MOVE_BENCH | SLOWROLL | 88.0 | 5 | 42 | 4 | 22.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5701250433921814 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 304 | PASS | SLOWROLL | 88.0 | 5 | 42 | 4 | 20.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11150000244379044 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 327 | MOVE_BENCH | SLOWROLL | 78.0 | 5 | 52 | 5 | 20.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19355408847332 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 328 | MOVE_BENCH | SLOWROLL | 78.0 | 5 | 52 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 329 | PASS | SLOWROLL | 78.0 | 5 | 52 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12321005761623383 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 349 | BUY | SLOWROLL | 67.0 | 5 | 63 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003341095522046089 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 350 | MOVE_BENCH | SLOWROLL | 67.0 | 5 | 60 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3522569239139557 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 351 | MOVE_BENCH | SLOWROLL | 67.0 | 5 | 60 | 5 | 22.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4273202121257782 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 352 | PASS | SLOWROLL | 67.0 | 5 | 60 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1266702264547348 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 371 | BUY | SLOWROLL | 55.0 | 5 | 71 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3310653269290924 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 372 | BUY | SLOWROLL | 55.0 | 5 | 68 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33046409487724304 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 373 | BUY | SLOWROLL | 55.0 | 5 | 65 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8680353760719299 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 7 | 3-4 | 374 | BUY_XP | SLOWROLL | 55.0 | 5 | 64 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 375 | BUY_XP | SLOWROLL | 55.0 | 5 | 60 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4622400104999542 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 376 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 56 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6453271508216858 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 377 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 56 | 5 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35230281949043274 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 378 | PASS | SLOWROLL | 55.0 | 6 | 56 | 5 | 22.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12487752735614777 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 389 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 56 | 5 | 22.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46064409613609314 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 392 | BUY | FAST8 | 55.0 | 6 | 67 | 5 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8395184874534607 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 393 | BUY | FAST8 | 55.0 | 6 | 64 | 5 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6901054978370667 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 7 | 3-5 | 394 | BUY | FAST8 | 55.0 | 6 | 62 | 5 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10232314467430115 | 0.0 | 0.0 | +2074e6ec-81e7-41c9-be7e-a0d9310fbafa / -— |
| Jogador 7 | 3-5 | 395 | BUY_XP | FAST8 | 55.0 | 6 | 60 | 5 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 396 | BUY_XP | FAST8 | 55.0 | 6 | 56 | 5 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 397 | BUY_XP | FAST8 | 55.0 | 6 | 52 | 5 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07455000281333923 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 398 | BUY_XP | FAST8 | 55.0 | 6 | 48 | 4 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 399 | BUY_XP | FAST8 | 55.0 | 6 | 44 | 4 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 400 | BUY_XP | FAST8 | 55.0 | 6 | 40 | 4 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 401 | BUY_XP | FAST8 | 55.0 | 6 | 36 | 3 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 402 | PASS | FAST8 | 55.0 | 6 | 32 | 3 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12399999797344208 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 412 | BUY | FAST8 | 44.0 | 6 | 42 | 4 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6889103055000305 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 413 | BUY | FAST8 | 44.0 | 6 | 39 | 3 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2497749775648117 | 0.0 | 0.0 | +a1aa0280-2379-4d0b-a475-143c1a2f6c25 / -— |
| Jogador 7 | 3-6 | 414 | REROLL | FAST8 | 44.0 | 6 | 35 | 3 | 26.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 415 | SELL | FAST8 | 44.0 | 6 | 33 | 3 | 26.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0077953157015144825 | 0.0 | 0.0 | +— / -2074e6ec-81e7-41c9-be7e-a0d9310fbafa |
| Jogador 7 | 3-6 | 416 | BUY | FAST8 | 44.0 | 6 | 35 | 3 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7914965748786926 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -d69fa0dc-74b6-4ee7-90f7-aaca5405c59c,f116ca4e-dbe8-457e-83a5-958525aa384a |
| Jogador 7 | 3-6 | 417 | BUY | SLOWROLL | 44.0 | 6 | 32 | 3 | 20.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13901746273040771 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 7 | 3-6 | 418 | REROLL | SLOWROLL | 44.0 | 6 | 30 | 3 | 20.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028954600915312767 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 419 | REROLL | SLOWROLL | 44.0 | 6 | 28 | 2 | 20.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1259852647781372 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 420 | REROLL | SLOWROLL | 44.0 | 6 | 26 | 2 | 20.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045682642608881 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 421 | REROLL | SLOWROLL | 44.0 | 6 | 24 | 2 | 20.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05307747796177864 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 422 | PASS | SLOWROLL | 44.0 | 6 | 22 | 2 | 20.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 432 | MOVE_BENCH | STABILIZE | 32.0 | 7 | 32 | 3 | 20.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5270161628723145 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 433 | BUY | STABILIZE | 32.0 | 7 | 32 | 3 | 32.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008061903528869152 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 7 | 3-7 | 434 | REROLL | STABILIZE | 32.0 | 7 | 28 | 2 | 32.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 435 | SELL | STABILIZE | 32.0 | 7 | 26 | 2 | 32.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35448169708251953 | 0.0 | 0.0 | +— / -7c8b3027-1434-4346-95b3-5463e8a4aa9b |
| Jogador 7 | 3-7 | 436 | BUY | STABILIZE | 32.0 | 7 | 28 | 2 | 32.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8057662844657898 | 0.0 | 0.0 | +78525c90-c4d2-425d-ba90-a03664c60a28 / -— |
| Jogador 7 | 3-7 | 437 | SELL | STABILIZE | 32.0 | 7 | 25 | 2 | 32.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058630768209695816 | 0.0 | 0.0 | +— / -a1aa0280-2379-4d0b-a475-143c1a2f6c25 |
| Jogador 7 | 3-7 | 438 | BUY | STABILIZE | 32.0 | 7 | 29 | 2 | 32.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8205417990684509 | 0.0 | 0.0 | +3d7ba32f-3349-479e-bb6f-9cd1f2006149 / -— |
| Jogador 7 | 3-7 | 439 | REROLL | STABILIZE | 32.0 | 7 | 26 | 2 | 32.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 440 | SELL | STABILIZE | 32.0 | 7 | 24 | 2 | 32.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03912321850657463 | 0.0 | 0.0 | +— / -42733dbd-0bc3-461b-95ab-76daf5ad6296 |
| Jogador 7 | 3-7 | 441 | BUY | STABILIZE | 32.0 | 7 | 28 | 2 | 32.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8588384389877319 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -0cf5c315-d2f3-4854-a95b-07912b83ea81,3d7ba32f-3349-479e-bb6f-9cd1f2006149 |
| Jogador 7 | 3-7 | 442 | PASS | STABILIZE | 32.0 | 7 | 25 | 2 | 26.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0690888911485672 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 452 | BUY | STABILIZE | 32.0 | 7 | 35 | 3 | 26.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11212100833654404 | 0.0 | 0.0 | +07cc291c-137e-4668-9caf-3a1fa8f09c3d / -— |
| Jogador 7 | 4-1 | 453 | MOVE_BENCH | STABILIZE | 32.0 | 7 | 30 | 3 | 26.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35513830184936523 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 454 | MOVE_BENCH | STABILIZE | 32.0 | 7 | 30 | 3 | 26.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38295212388038635 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 455 | BUY | STABILIZE | 32.0 | 7 | 30 | 3 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6219992637634277 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 7 | 4-1 | 456 | REROLL | STABILIZE | 32.0 | 7 | 28 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 457 | REROLL | STABILIZE | 32.0 | 7 | 26 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 458 | REROLL | STABILIZE | 32.0 | 7 | 24 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 459 | SELL | STABILIZE | 32.0 | 7 | 22 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8187282085418701 | 0.0 | 0.0 | +— / -1ff50c59-5133-459e-8bf1-d449c26efabf |
| Jogador 7 | 4-1 | 460 | BUY | STABILIZE | 32.0 | 7 | 23 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8615280985832214 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -78525c90-c4d2-425d-ba90-a03664c60a28,cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 4-1 | 461 | BUY | STABILIZE | 32.0 | 7 | 20 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13964325189590454 | 0.0 | 0.0 | +840740a6-45be-4107-a4b7-b10cefe1a667 / -— |
| Jogador 7 | 4-1 | 462 | PASS | STABILIZE | 32.0 | 7 | 16 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11033650487661362 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 472 | BUY | STABILIZE | 19.0 | 7 | 25 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013642845442518592 | 0.0 | 0.0 | +5b6dec85-6970-4575-b364-21c3123995a5 / -— |
| Jogador 7 | 4-2 | 473 | REROLL | STABILIZE | 19.0 | 7 | 22 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 474 | SELL | STABILIZE | 19.0 | 7 | 20 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048696547746658325 | 0.0 | 0.0 | +— / -5b6dec85-6970-4575-b364-21c3123995a5 |
| Jogador 7 | 4-2 | 475 | BUY | STABILIZE | 19.0 | 7 | 23 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013175110798329115 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 7 | 4-2 | 476 | REROLL | STABILIZE | 19.0 | 7 | 20 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 477 | SELL | STABILIZE | 19.0 | 7 | 18 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1287078708410263 | 0.0 | 0.0 | +— / -d1f19609-8b5f-489d-a2cf-d015fe7ed27e |
| Jogador 7 | 4-2 | 478 | BUY | STABILIZE | 19.0 | 7 | 21 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33602267503738403 | 0.0 | 0.0 | +7643f027-a90f-4f3a-8b4c-7be4cba17f95 / -— |
| Jogador 7 | 4-2 | 479 | REROLL | STABILIZE | 19.0 | 7 | 18 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 480 | SELL | STABILIZE | 19.0 | 7 | 16 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06865698099136353 | 0.0 | 0.0 | +— / -7643f027-a90f-4f3a-8b4c-7be4cba17f95 |
| Jogador 7 | 4-2 | 481 | BUY | STABILIZE | 19.0 | 7 | 19 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8106329441070557 | 0.0 | 0.0 | +83228c14-cadb-45b4-9893-2fb12c40f4a8 / -227dbcdb-af5c-4318-94d1-f01a7847d100,dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 7 | 4-2 | 482 | PASS | STABILIZE | 19.0 | 7 | 17 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11721375584602356 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 492 | BUY | STABILIZE | 19.0 | 7 | 24 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25800034403800964 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 7 | 4-3 | 493 | BUY | STABILIZE | 19.0 | 7 | 21 | 2 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09967517852783203 | 0.0 | 0.0 | +0435182d-aea5-44fe-ba36-601627982b66 / -— |
| Jogador 7 | 4-3 | 494 | REROLL | STABILIZE | 19.0 | 7 | 19 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 495 | SELL | STABILIZE | 19.0 | 7 | 17 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05001962557435036 | 0.0 | 0.0 | +— / -0435182d-aea5-44fe-ba36-601627982b66 |
| Jogador 7 | 4-3 | 496 | BUY | STABILIZE | 19.0 | 7 | 19 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8332383036613464 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -86c1ac55-598e-426a-86ea-64249f82b085,f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 4-3 | 497 | BUY | STABILIZE | 19.0 | 7 | 16 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4287710189819336 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -— |
| Jogador 7 | 4-3 | 498 | BUY | STABILIZE | 19.0 | 7 | 13 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25891703367233276 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 7 | 4-3 | 499 | REROLL | STABILIZE | 19.0 | 7 | 10 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 500 | SELL | STABILIZE | 19.0 | 7 | 8 | 0 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1384769231081009 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 7 | 4-3 | 501 | BUY | STABILIZE | 19.0 | 7 | 11 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3312591314315796 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -— |
| Jogador 7 | 4-3 | 502 | PASS | STABILIZE | 19.0 | 7 | 8 | 0 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 512 | SELL | ALL_IN | 5.0 | 7 | 13 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058476924896240234 | 0.0 | 0.0 | +— / -02d3d068-e592-4f9c-a574-914955401575 |
| Jogador 7 | 4-4 | 513 | BUY | ALL_IN | 5.0 | 7 | 16 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24410782754421234 | 0.0 | 0.0 | +e270a6b1-23dd-49a0-8694-ba911eae4c71 / -— |
| Jogador 7 | 4-4 | 514 | REROLL | ALL_IN | 5.0 | 7 | 13 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 515 | SELL | ALL_IN | 5.0 | 7 | 11 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.066600002348423 | 0.0 | 0.0 | +— / -e270a6b1-23dd-49a0-8694-ba911eae4c71 |
| Jogador 7 | 4-4 | 516 | BUY | ALL_IN | 5.0 | 7 | 14 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06731355935335159 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -— |
| Jogador 7 | 4-4 | 517 | REROLL | ALL_IN | 5.0 | 7 | 10 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 518 | SELL | ALL_IN | 5.0 | 7 | 8 | 0 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2392461597919464 | 0.0 | 0.0 | +— / -6eecc806-dcf8-47df-bc1d-bc5bc5f07099 |
| Jogador 7 | 4-4 | 519 | BUY | ALL_IN | 5.0 | 7 | 11 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1937779039144516 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 7 | 4-4 | 520 | REROLL | ALL_IN | 5.0 | 7 | 8 | 0 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 521 | SELL | ALL_IN | 5.0 | 7 | 6 | 0 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10740000009536743 | 0.0 | 0.0 | +— / -83228c14-cadb-45b4-9893-2fb12c40f4a8 |
| Jogador 7 | 4-4 | 522 | PASS | ALL_IN | 5.0 | 7 | 11 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 532 | BUY | ALL_IN | 5.0 | 7 | 17 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04724675416946411 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -— |
| Jogador 7 | 4-5 | 533 | SELL | ALL_IN | 5.0 | 7 | 13 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06807692348957062 | 0.0 | 0.0 | +— / -b0c1aba5-b1bd-48df-abec-19efa8e49d6d |
| Jogador 7 | 4-5 | 534 | BUY | ALL_IN | 5.0 | 7 | 16 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7804375886917114 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -— |
| Jogador 7 | 4-5 | 535 | REROLL | ALL_IN | 5.0 | 7 | 12 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 536 | SELL | ALL_IN | 5.0 | 7 | 10 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06379999965429306 | 0.0 | 0.0 | +— / -1c5a9322-14c8-4df9-937b-842dcaa1f372 |
| Jogador 7 | 4-5 | 537 | BUY | ALL_IN | 5.0 | 7 | 14 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2739327847957611 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 7 | 4-5 | 538 | REROLL | ALL_IN | 5.0 | 7 | 11 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 539 | SELL | ALL_IN | 5.0 | 7 | 9 | 0 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39976921677589417 | 0.0 | 0.0 | +— / -3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 |
| Jogador 7 | 4-5 | 540 | BUY | ALL_IN | 5.0 | 7 | 17 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25479456782341003 | 0.0 | 0.0 | +b1d58916-6d8b-4071-a37d-a478395e6a1e / -— |
| Jogador 7 | 4-5 | 541 | REROLL | ALL_IN | 5.0 | 7 | 14 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 542 | PASS | ALL_IN | 5.0 | 7 | 12 | 1 | 38.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.011937879957258701 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3058992028236389 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 35 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 1.0161010026931763 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8132011890411377 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5297468900680542 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.13150574266910553 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 39 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 62 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2737751305103302 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 63 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7302599549293518 | 0.0 | 0.0 | +— / -74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 1-3 | 64 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2724849581718445 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29965540766716003 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6520918011665344 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 67 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 92 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2742752134799957 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 93 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4310055077075958 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 94 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1167123317718506 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -78019889-2624-4adb-917b-619681f23053,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 1-4 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20886565744876862 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15471206605434418 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 98 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 122 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.39350399374961853 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 123 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04054325446486473 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 124 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 125 | PASS | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 148 | BUY | STABILIZE | 95.0 | 4 | 12 | 1 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03290138766169548 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 149 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5196688175201416 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 150 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 14.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12566843628883362 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 151 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41079115867614746 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 152 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05742357671260834 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 153 | BUY_XP | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 154 | PASS | STABILIZE | 95.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 172 | SELL | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037510305643081665 | 0.0 | 0.0 | +— / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02 |
| Jogador 8 | 2-3 | 173 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.006139321718364954 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 174 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5332509875297546 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 175 | SELL | STABILIZE | 95.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4197772145271301 | 0.0 | 0.0 | +— / -64f24363-3325-4538-972e-a6d8260b3787 |
| Jogador 8 | 2-3 | 176 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2724389135837555 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 177 | SELL | STABILIZE | 95.0 | 4 | 9 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32243892550468445 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-3 | 178 | BUY_XP | STABILIZE | 95.0 | 4 | 10 | 1 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.061000000685453415 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 179 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20079177618026733 | 0.0 | 0.0 | +491eb6b6-54f4-4de8-bc63-d96c6c1d9cce / -— |
| Jogador 8 | 2-3 | 180 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 181 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.578492283821106 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 182 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 201 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23616790771484375 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 202 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11008749902248383 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 203 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8478800058364868 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 204 | PASS | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 227 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 11 | 1 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4137265980243683 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 228 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 11 | 1 | 20.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1887097954750061 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 229 | SELL | STABILIZE | 95.0 | 5 | 11 | 1 | 20.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3695846199989319 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-5 | 230 | BUY | STABILIZE | 95.0 | 5 | 14 | 1 | 20.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2272193878889084 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 231 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 11 | 1 | 20.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3969563841819763 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 232 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 11 | 1 | 20.0 | Fera do Rift/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061898715794086456 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 233 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 11 | 1 | 20.0 | Fera do Rift/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2902139723300934 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 234 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 11 | 1 | 20.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4087785482406616 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 235 | PASS | STABILIZE | 95.0 | 5 | 11 | 1 | 20.0 | Fera do Rift/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 252 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 17 | 1 | 20.0 | Fera do Rift/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050306547433137894 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 253 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 17 | 1 | 20.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05896814540028572 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 254 | SELL | STABILIZE | 89.0 | 5 | 17 | 1 | 22.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00478022126480937 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-6 | 255 | BUY | STABILIZE | 89.0 | 5 | 19 | 1 | 22.0 | Fera do Rift/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3048809766769409 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 256 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 16 | 1 | 22.0 | Fera do Rift/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5083942413330078 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 257 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 16 | 1 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6374168992042542 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 258 | PASS | STABILIZE | 89.0 | 5 | 16 | 1 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020178571343421936 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 276 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 23 | 2 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2661965489387512 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 277 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 23 | 2 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041864536702632904 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 278 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 23 | 2 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6980040073394775 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 279 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 23 | 2 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05781284347176552 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 280 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 23 | 2 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2738310992717743 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 281 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 23 | 2 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3422989845275879 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 282 | PASS | STABILIZE | 83.0 | 5 | 23 | 2 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02142857201397419 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 302 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 31 | 3 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03378736600279808 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 303 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 31 | 3 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2821522057056427 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 304 | PASS | STABILIZE | 83.0 | 5 | 31 | 3 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12349999696016312 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 327 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 40 | 4 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2663520574569702 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 328 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 40 | 4 | 22.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1318671703338623 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 329 | SELL | STABILIZE | 83.0 | 5 | 40 | 4 | 26.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48184695839881897 | 0.0 | 0.0 | +— / -491eb6b6-54f4-4de8-bc63-d96c6c1d9cce |
| Jogador 8 | 3-2 | 330 | BUY | STABILIZE | 83.0 | 5 | 41 | 4 | 26.0 | Caçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03191269561648369 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 331 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 37 | 3 | 26.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46871116757392883 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 332 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 37 | 3 | 28.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30939945578575134 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 333 | PASS | STABILIZE | 83.0 | 5 | 37 | 3 | 28.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1264999955892563 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 349 | MOVE_BENCH | FAST8 | 73.0 | 6 | 45 | 4 | 28.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.469478577375412 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 350 | BUY | FAST8 | 73.0 | 6 | 45 | 4 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7211475372314453 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 351 | MOVE_BENCH | FAST8 | 73.0 | 6 | 42 | 4 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37232300639152527 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 352 | MOVE_BENCH | FAST8 | 73.0 | 6 | 42 | 4 | 32.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23865219950675964 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 353 | PASS | FAST8 | 73.0 | 6 | 42 | 4 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1289999932050705 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 371 | MOVE_BENCH | FAST8 | 73.0 | 6 | 52 | 5 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35023033618927 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 372 | BUY_XP | FAST8 | 73.0 | 6 | 52 | 5 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07455000281333923 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 373 | BUY_XP | FAST8 | 73.0 | 6 | 48 | 4 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 374 | BUY_XP | FAST8 | 73.0 | 6 | 44 | 4 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 375 | BUY_XP | FAST8 | 73.0 | 6 | 40 | 4 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 376 | BUY_XP | FAST8 | 73.0 | 6 | 36 | 3 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 377 | BUY_XP | FAST8 | 73.0 | 6 | 32 | 3 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 378 | BUY_XP | FAST8 | 73.0 | 6 | 28 | 2 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 379 | BUY_XP | FAST8 | 73.0 | 6 | 24 | 2 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 380 | BUY_XP | FAST8 | 73.0 | 6 | 20 | 2 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004100000020116568 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 381 | PASS | FAST8 | 73.0 | 7 | 16 | 1 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05649999901652336 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 392 | MOVE_BENCH | FAST8 | 73.0 | 7 | 22 | 2 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6639476418495178 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 393 | MOVE_BENCH | FAST8 | 73.0 | 7 | 22 | 2 | 32.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2595669627189636 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 394 | PASS | FAST8 | 73.0 | 7 | 22 | 2 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05950000137090683 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 410 | MOVE_BENCH | FAST8 | 73.0 | 7 | 22 | 2 | 34.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10271777212619781 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 412 | BUY | FAST8 | 73.0 | 7 | 31 | 3 | 40.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04883725568652153 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 413 | MOVE_BENCH | FAST8 | 73.0 | 7 | 27 | 2 | 40.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19549426436424255 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 414 | MOVE_BENCH | FAST8 | 73.0 | 7 | 27 | 2 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03293432667851448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 415 | BUY_XP | FAST8 | 73.0 | 7 | 27 | 2 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003275000024586916 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 416 | BUY_XP | FAST8 | 73.0 | 7 | 23 | 2 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 417 | BUY_XP | FAST8 | 73.0 | 7 | 19 | 1 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 418 | BUY_XP | FAST8 | 73.0 | 7 | 15 | 1 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 419 | BUY_XP | FAST8 | 73.0 | 7 | 11 | 1 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 420 | BUY_XP | FAST8 | 73.0 | 7 | 7 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 421 | PASS | FAST8 | 73.0 | 7 | 3 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 432 | BUY_XP | FAST8 | 73.0 | 7 | 10 | 1 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 433 | BUY_XP | FAST8 | 73.0 | 7 | 6 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 434 | PASS | FAST8 | 73.0 | 7 | 2 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 452 | CRAFT_AND_EQUIP | FAST8 | 73.0 | 7 | 8 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10616837441921234 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 453 | SELL | FAST8 | 73.0 | 7 | 8 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07730375230312347 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 4-1 | 454 | BUY | FAST8 | 73.0 | 7 | 11 | 1 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6539978981018066 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 8 | 4-1 | 455 | BUY_XP | FAST8 | 73.0 | 7 | 8 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 456 | BUY_XP | FAST8 | 73.0 | 7 | 4 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 457 | PASS | FAST8 | 73.0 | 7 | 0 | 0 | 42.0 | Caçador/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 472 | SELL | FAST8 | 73.0 | 7 | 7 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8389999866485596 | 0.0 | 0.0 | +— / -6388773b-0e99-40a9-8d68-895dcf16fce6 |
| Jogador 8 | 4-2 | 473 | BUY | FAST8 | 73.0 | 7 | 10 | 1 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.128232941031456 | 0.0 | 0.0 | +bb51728e-fcc5-4950-ad03-c864c51c2371 / -— |
| Jogador 8 | 4-2 | 474 | BUY_XP | FAST8 | 73.0 | 7 | 6 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0853937491774559 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 475 | MOVE_BENCH | WINSTREAK | 73.0 | 8 | 2 | 0 | 42.0 | Caçador/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6402223110198975 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 476 | BUY | WINSTREAK | 73.0 | 8 | 2 | 0 | 50.0 | Caçador/DA_Brambleback18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25718024373054504 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 8 | 4-2 | 477 | PASS | WINSTREAK | 73.0 | 8 | 0 | 0 | 50.0 | Caçador/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 492 | BUY | WINSTREAK | 73.0 | 8 | 8 | 0 | 50.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.061078738421201706 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 8 | 4-3 | 493 | PASS | WINSTREAK | 73.0 | 8 | 4 | 0 | 50.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 512 | PASS | WINSTREAK | 73.0 | 8 | 13 | 1 | 50.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 532 | BUY | WINSTREAK | 73.0 | 8 | 22 | 2 | 50.0 | Caçador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5159324407577515 | 0.0 | 0.0 | +bbfa514f-8d07-411b-aa19-4511ae5fb5cd / -— |
| Jogador 8 | 4-5 | 533 | PASS | WINSTREAK | 73.0 | 8 | 18 | 1 | 50.0 | Caçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08214285969734192 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 551 | BUY | WINSTREAK | 73.0 | 8 | 28 | 2 | 50.0 | Caçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16232576966285706 | 0.0 | 0.0 | +b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 / -— |
| Jogador 8 | 4-6 | 552 | PASS | WINSTREAK | 73.0 | 8 | 24 | 2 | 50.0 | Caçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08642856776714325 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 570 | BUY | WINSTREAK | 73.0 | 8 | 35 | 3 | 50.0 | Caçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21846798062324524 | 0.0 | 0.0 | +bdee88f4-e5b5-48fb-9ae5-1fd155982995 / -— |
| Jogador 8 | 4-7 | 571 | BUY | WINSTREAK | 73.0 | 8 | 31 | 3 | 50.0 | Caçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020451560616493225 | 0.0 | 0.0 | +db79d601-4b72-43c1-a8e3-4755c3442aa0 / -— |
| Jogador 8 | 4-7 | 572 | PASS | WINSTREAK | 73.0 | 8 | 27 | 2 | 50.0 | Caçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08857142925262451 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 582 | ANVIL_CHOICE | WINSTREAK | 73.0 | 8 | 37 | 3 | 50.0 | Caçador/DA_18_Soraka | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 583 | BUY | WINSTREAK | 73.0 | 8 | 37 | 3 | 50.0 | Caçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10579773038625717 | 0.0 | 0.0 | +316b1635-e9c1-41c2-a26f-e64625e1c743 / -— |
| Jogador 8 | 5-1 | 584 | BUY | WINSTREAK | 73.0 | 8 | 32 | 3 | 50.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12321341037750244 | 0.0 | 0.0 | +9658df1d-f821-4560-b2b0-79ab4e1f14d9 / -— |
| Jogador 8 | 5-1 | 585 | BUY | WINSTREAK | 73.0 | 8 | 28 | 2 | 50.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20960459113121033 | 0.0 | 0.0 | +3c65e9e8-ff81-499f-8145-953bbcd0531e / -— |
| Jogador 8 | 5-1 | 586 | PASS | WINSTREAK | 73.0 | 8 | 24 | 2 | 50.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03457142785191536 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 601 | SELL | WINSTREAK | 73.0 | 8 | 35 | 3 | 50.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -db79d601-4b72-43c1-a8e3-4755c3442aa0 |
| Jogador 8 | 5-2 | 602 | BUY | WINSTREAK | 73.0 | 8 | 39 | 3 | 50.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8610045313835144 | 0.0 | 0.0 | +a920ed77-ca29-4616-afba-e4c7759b2d68 / -7915a339-3bda-4275-80ae-9941370ea609,e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 5-2 | 603 | MOVE_BENCH | WINSTREAK | 73.0 | 8 | 36 | 3 | 38.0 | Caçador/DA_18_KhaZix | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1012585237622261 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 604 | SELL | WINSTREAK | 73.0 | 8 | 36 | 3 | 40.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13272307813167572 | 0.0 | 0.0 | +— / -9658df1d-f821-4560-b2b0-79ab4e1f14d9 |
| Jogador 8 | 5-2 | 605 | BUY | WINSTREAK | 73.0 | 8 | 40 | 4 | 40.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5432805418968201 | 0.0 | 0.0 | +23181987-d0b2-4e8c-a1a7-48a1e28179f7 / -— |
| Jogador 8 | 5-2 | 606 | MOVE_BENCH | WINSTREAK | 73.0 | 8 | 36 | 3 | 40.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24261833727359772 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 607 | BUY | WINSTREAK | 73.0 | 8 | 36 | 3 | 48.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2960313558578491 | 0.0 | 0.0 | +1b5c89d2-f5ea-401f-bf8a-985023acf75c / -— |
| Jogador 8 | 5-2 | 608 | PASS | WINSTREAK | 73.0 | 8 | 33 | 3 | 48.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04164285585284233 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 612 | MOVE_BENCH | WINSTREAK | 73.0 | 8 | 33 | 3 | 48.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.594840943813324 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 619 | BUY | WINSTREAK | 73.0 | 8 | 45 | 4 | 52.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.826781690120697 | 0.0 | 0.0 | +4bc5b602-fe82-4525-b854-33dc5ab88a32 / -— |
| Jogador 8 | 5-3 | 620 | SELL | WINSTREAK | 73.0 | 8 | 42 | 4 | 52.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08226153999567032 | 0.0 | 0.0 | +— / -3c65e9e8-ff81-499f-8145-953bbcd0531e |
| Jogador 8 | 5-3 | 621 | BUY | WINSTREAK | 73.0 | 8 | 46 | 4 | 52.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9460867047309875 | 0.0 | 0.0 | +4cae9d83-6cc8-4a27-9c17-2e6f45091477 / -1b5c89d2-f5ea-401f-bf8a-985023acf75c,4bc5b602-fe82-4525-b854-33dc5ab88a32 |
| Jogador 8 | 5-3 | 622 | BUY | WINSTREAK | 73.0 | 8 | 43 | 4 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06342215836048126 | 0.0 | 0.0 | +fb7a5348-949c-42cf-9326-c4676d6b6960 / -— |
| Jogador 8 | 5-3 | 623 | BUY | WINSTREAK | 73.0 | 8 | 40 | 4 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014942487701773643 | 0.0 | 0.0 | +30d632db-738f-4a3c-84dc-ff4a4705ecdf / -— |
| Jogador 8 | 5-3 | 624 | PASS | WINSTREAK | 73.0 | 8 | 38 | 3 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045571427792310715 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 632 | SELL | WINSTREAK | 73.0 | 8 | 50 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05186966434121132 | 0.0 | 0.0 | +— / -30d632db-738f-4a3c-84dc-ff4a4705ecdf |
| Jogador 8 | 5-4 | 633 | BUY | WINSTREAK | 73.0 | 8 | 52 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3098706007003784 | 0.0 | 0.0 | +e47e9d8e-e703-4b77-8266-2f90680eb62f / -— |
| Jogador 8 | 5-4 | 634 | SELL | WINSTREAK | 73.0 | 8 | 49 | 4 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1321520358324051 | 0.0 | 0.0 | +— / -fb7a5348-949c-42cf-9326-c4676d6b6960 |
| Jogador 8 | 5-4 | 635 | BUY | WINSTREAK | 73.0 | 8 | 52 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33162829279899597 | 0.0 | 0.0 | +c7e728cc-abbd-488d-b3bb-3368e9259d0b / -— |
| Jogador 8 | 5-4 | 636 | SELL | WINSTREAK | 73.0 | 8 | 48 | 4 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.256873220205307 | 0.0 | 0.0 | +— / -bdee88f4-e5b5-48fb-9ae5-1fd155982995 |
| Jogador 8 | 5-4 | 637 | BUY | WINSTREAK | 73.0 | 8 | 52 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09704180061817169 | 0.0 | 0.0 | +74eb8880-c862-4163-afac-054a68ace2bd / -— |
| Jogador 8 | 5-4 | 638 | REROLL | WINSTREAK | 73.0 | 8 | 49 | 4 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 639 | SELL | WINSTREAK | 73.0 | 8 | 47 | 4 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14803488552570343 | 0.0 | 0.0 | +— / -23181987-d0b2-4e8c-a1a7-48a1e28179f7 |
| Jogador 8 | 5-4 | 640 | BUY | WINSTREAK | 73.0 | 8 | 51 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7881102561950684 | 0.0 | 0.0 | +89cc418a-8b13-4a3c-8f62-de886873b56c / -— |
| Jogador 8 | 5-4 | 641 | SELL | WINSTREAK | 73.0 | 8 | 49 | 4 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10017500072717667 | 0.0 | 0.0 | +— / -74eb8880-c862-4163-afac-054a68ace2bd |
| Jogador 8 | 5-4 | 642 | PASS | WINSTREAK | 73.0 | 8 | 52 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24311579763889313 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 651 | BUY | WINSTREAK | 73.0 | 8 | 65 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20404359698295593 | 0.0 | 0.0 | +877a1ed4-302c-493b-a973-ac9ca3d3e6a4 / -— |
| Jogador 8 | 5-5 | 652 | SELL | WINSTREAK | 73.0 | 8 | 61 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07426153868436813 | 0.0 | 0.0 | +— / -877a1ed4-302c-493b-a973-ac9ca3d3e6a4 |
| Jogador 8 | 5-5 | 653 | BUY | WINSTREAK | 73.0 | 8 | 65 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020659970119595528 | 0.0 | 0.0 | +769abba3-083d-4c19-b123-0eca59c90bb3 / -— |
| Jogador 8 | 5-5 | 654 | SELL | WINSTREAK | 73.0 | 8 | 62 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032538462430238724 | 0.0 | 0.0 | +— / -769abba3-083d-4c19-b123-0eca59c90bb3 |
| Jogador 8 | 5-5 | 655 | BUY | WINSTREAK | 73.0 | 8 | 65 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09049028158187866 | 0.0 | 0.0 | +98785f85-6099-44a3-ae6c-ce3126135f45 / -— |
| Jogador 8 | 5-5 | 656 | REROLL | WINSTREAK | 73.0 | 8 | 63 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 657 | SELL | WINSTREAK | 73.0 | 8 | 61 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035861536860466 | 0.0 | 0.0 | +— / -98785f85-6099-44a3-ae6c-ce3126135f45 |
| Jogador 8 | 5-5 | 658 | BUY | WINSTREAK | 73.0 | 8 | 63 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5783390402793884 | 0.0 | 0.0 | +ae36e82c-bcac-4ad8-b7b1-063966ecc411 / -— |
| Jogador 8 | 5-5 | 659 | SELL | WINSTREAK | 73.0 | 8 | 60 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34261399507522583 | 0.0 | 0.0 | +— / -ae36e82c-bcac-4ad8-b7b1-063966ecc411 |
| Jogador 8 | 5-5 | 660 | BUY | WINSTREAK | 73.0 | 8 | 63 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5786932706832886 | 0.0 | 0.0 | +8ef30c1a-60fd-4a11-bee3-08c3aa7baa32 / -— |
| Jogador 8 | 5-5 | 661 | PASS | WINSTREAK | 73.0 | 8 | 60 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09455320984125137 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 669 | SELL | WINSTREAK | 73.0 | 8 | 74 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3425622582435608 | 0.0 | 0.0 | +— / -8ef30c1a-60fd-4a11-bee3-08c3aa7baa32 |
| Jogador 8 | 5-6 | 670 | BUY | WINSTREAK | 73.0 | 8 | 77 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9492145776748657 | 0.0 | 0.0 | +233643ca-941f-4ffe-8d9a-f1ff0f64d1d2 / -— |
| Jogador 8 | 5-6 | 671 | SELL | WINSTREAK | 73.0 | 8 | 74 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.330046147108078 | 0.0 | 0.0 | +— / -18e21ac6-f873-4310-95c8-bd8e62612479 |
| Jogador 8 | 5-6 | 672 | BUY | WINSTREAK | 73.0 | 8 | 78 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.892059326171875 | 0.0 | 0.0 | +8b7968ee-f664-4b2a-b9e8-9b0ad6e81d79 / -— |
| Jogador 8 | 5-6 | 673 | SELL | WINSTREAK | 73.0 | 8 | 74 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -bbfa514f-8d07-411b-aa19-4511ae5fb5cd |
| Jogador 8 | 5-6 | 674 | BUY | WINSTREAK | 73.0 | 8 | 78 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15137194097042084 | 0.0 | 0.0 | +d6d15e43-3f39-40c6-8a07-a05854ef835d / -— |
| Jogador 8 | 5-6 | 675 | REROLL | WINSTREAK | 73.0 | 8 | 74 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 676 | SELL | WINSTREAK | 73.0 | 8 | 72 | 5 | 52.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -d6d15e43-3f39-40c6-8a07-a05854ef835d |
| Jogador 8 | 5-6 | 677 | BUY | WINSTREAK | 73.0 | 8 | 76 | 5 | 52.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9999939203262329 | 0.0 | 0.0 | +087138e8-3632-4703-b838-e0047a0e80c3 / -233643ca-941f-4ffe-8d9a-f1ff0f64d1d2,87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 5-6 | 678 | BUY | WINSTREAK | 73.0 | 8 | 73 | 5 | 46.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1768583357334137 | 0.0 | 0.0 | +68251e71-5657-42da-9181-7351627204f6 / -— |
| Jogador 8 | 5-6 | 679 | PASS | WINSTREAK | 73.0 | 8 | 71 | 5 | 46.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10282160341739655 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 682 | SELL | ECON | 56.0 | 8 | 81 | 5 | 46.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035861536860466 | 0.0 | 0.0 | +— / -68251e71-5657-42da-9181-7351627204f6 |
| Jogador 8 | 5-7 | 683 | BUY | ECON | 56.0 | 8 | 83 | 5 | 46.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8370668888092041 | 0.0 | 0.0 | +8c28b034-ea67-4700-84c5-5dbd3059cbdb / -b0f8dc80-dd2b-4dde-87a9-b855a1c13da5,c7e728cc-abbd-488d-b3bb-3368e9259d0b |
| Jogador 8 | 5-7 | 684 | BUY | ECON | 56.0 | 8 | 79 | 5 | 46.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3928973078727722 | 0.0 | 0.0 | +c4b17c0a-50ed-4a1f-92c1-71a683f7256f / -— |
| Jogador 8 | 5-7 | 685 | BUY | ECON | 56.0 | 8 | 78 | 5 | 46.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17387895286083221 | 0.0 | 0.0 | +71a71643-507c-4266-9f74-1fd7802fe094 / -— |
| Jogador 8 | 5-7 | 686 | REROLL | ECON | 56.0 | 8 | 74 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 687 | SELL | ECON | 56.0 | 8 | 72 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600000016391277 | 0.0 | 0.0 | +— / -a920ed77-ca29-4616-afba-e4c7759b2d68 |
| Jogador 8 | 5-7 | 688 | BUY | ECON | 56.0 | 8 | 80 | 5 | 46.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42110008001327515 | 0.0 | 0.0 | +b82a1a05-d852-47d3-a875-b96f21139f69 / -— |
| Jogador 8 | 5-7 | 689 | SELL | ECON | 56.0 | 8 | 77 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07426153868436813 | 0.0 | 0.0 | +— / -71a71643-507c-4266-9f74-1fd7802fe094 |
| Jogador 8 | 5-7 | 690 | BUY | ECON | 56.0 | 8 | 81 | 5 | 46.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007681308779865503 | 0.0 | 0.0 | +c6cfacad-08af-4690-9ef3-7751f1aa7a30 / -— |
| Jogador 8 | 5-7 | 691 | REROLL | ECON | 56.0 | 8 | 77 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 692 | PASS | ECON | 56.0 | 8 | 75 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.105955109000206 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 697 | ANVIL_CHOICE | ECON | 56.0 | 8 | 85 | 5 | 46.0 | Caçador/DA_Amumu18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 698 | EQUIP_FROM_INVENTORY | ECON | 56.0 | 8 | 85 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08955872058868408 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 699 | SELL | ECON | 56.0 | 8 | 85 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -c6cfacad-08af-4690-9ef3-7751f1aa7a30 |
| Jogador 8 | 6-1 | 700 | BUY | ECON | 56.0 | 8 | 89 | 5 | 46.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1556423306465149 | 0.0 | 0.0 | +0805d2e7-a19e-4760-b726-78436ad911b1 / -— |
| Jogador 8 | 6-1 | 701 | REROLL | ECON | 56.0 | 8 | 86 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 702 | SELL | ECON | 56.0 | 8 | 84 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03168705105781555 | 0.0 | 0.0 | +— / -0805d2e7-a19e-4760-b726-78436ad911b1 |
| Jogador 8 | 6-1 | 703 | BUY | ECON | 56.0 | 8 | 87 | 5 | 46.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24260853230953217 | 0.0 | 0.0 | +9061935a-18ba-4903-a48c-8ff90432875e / -— |
| Jogador 8 | 6-1 | 704 | SELL | ECON | 56.0 | 8 | 83 | 5 | 46.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31194987893104553 | 0.0 | 0.0 | +— / -b82a1a05-d852-47d3-a875-b96f21139f69 |
| Jogador 8 | 6-1 | 705 | BUY | ECON | 56.0 | 8 | 86 | 5 | 46.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0489283800125122 | 0.0 | 0.0 | +048822a2-1cc9-493f-b924-bbba636f19f1 / -17170204-1921-4cf1-b92b-cc73bb0701ea,89cc418a-8b13-4a3c-8f62-de886873b56c |
| Jogador 8 | 6-1 | 706 | BUY | ECON | 56.0 | 8 | 84 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011829297058284283 | 0.0 | 0.0 | +4d7ec7ee-5678-4796-a6e4-43af72c50bc3 / -— |
| Jogador 8 | 6-1 | 707 | PASS | ECON | 56.0 | 8 | 80 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11993733793497086 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 712 | SELL | STABILIZE | 37.0 | 8 | 91 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4236887991428375 | 0.0 | 0.0 | +— / -048822a2-1cc9-493f-b924-bbba636f19f1 |
| Jogador 8 | 6-2 | 713 | BUY | STABILIZE | 37.0 | 8 | 96 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2102493792772293 | 0.0 | 0.0 | +15804d76-ee44-4abc-8233-4b68bb7ae1f1 / -— |
| Jogador 8 | 6-2 | 714 | SELL | STABILIZE | 37.0 | 8 | 93 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017825210466980934 | 0.0 | 0.0 | +— / -15804d76-ee44-4abc-8233-4b68bb7ae1f1 |
| Jogador 8 | 6-2 | 715 | BUY | STABILIZE | 37.0 | 8 | 96 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2105807512998581 | 0.0 | 0.0 | +da4921b5-0ae7-4339-b38b-6ebce7412120 / -— |
| Jogador 8 | 6-2 | 716 | REROLL | STABILIZE | 37.0 | 8 | 93 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 717 | SELL | STABILIZE | 37.0 | 8 | 91 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01739216409623623 | 0.0 | 0.0 | +— / -da4921b5-0ae7-4339-b38b-6ebce7412120 |
| Jogador 8 | 6-2 | 718 | BUY | STABILIZE | 37.0 | 8 | 94 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9187800884246826 | 0.0 | 0.0 | +b92739a6-903f-4298-b146-b370a8adcc29 / -— |
| Jogador 8 | 6-2 | 719 | SELL | STABILIZE | 37.0 | 8 | 90 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -4d7ec7ee-5678-4796-a6e4-43af72c50bc3 |
| Jogador 8 | 6-2 | 720 | BUY | STABILIZE | 37.0 | 8 | 94 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13095435500144958 | 0.0 | 0.0 | +fdc17360-8d79-44b4-8b7e-4fc1f86a76b7 / -— |
| Jogador 8 | 6-2 | 721 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 90 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3890856206417084 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 722 | PASS | STABILIZE | 37.0 | 8 | 90 | 5 | 48.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31391462683677673 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 728 | BUY | STABILIZE | 19.0 | 8 | 101 | 5 | 48.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014323529787361622 | 0.0 | 0.0 | +2ea16654-a3ca-4b16-a4cd-989264343b5c / -— |
| Jogador 8 | 6-3 | 729 | SELL | STABILIZE | 19.0 | 8 | 97 | 5 | 48.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -2ea16654-a3ca-4b16-a4cd-989264343b5c |
| Jogador 8 | 6-3 | 730 | BUY | STABILIZE | 19.0 | 8 | 101 | 5 | 48.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4233553409576416 | 0.0 | 0.0 | +272b6a08-78d0-41af-bb2b-9d85eba7a082 / -— |
| Jogador 8 | 6-3 | 731 | REROLL | STABILIZE | 19.0 | 8 | 99 | 5 | 48.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 732 | REROLL | STABILIZE | 19.0 | 8 | 97 | 5 | 48.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 733 | REROLL | STABILIZE | 19.0 | 8 | 95 | 5 | 48.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 734 | SELL | STABILIZE | 19.0 | 8 | 93 | 5 | 48.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -fdc17360-8d79-44b4-8b7e-4fc1f86a76b7 |
| Jogador 8 | 6-3 | 735 | BUY | STABILIZE | 19.0 | 8 | 97 | 5 | 48.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.011580467224121 | 0.0 | 0.0 | +663c9fe5-55b8-4c50-b544-aba5b6e02070 / -— |
| Jogador 8 | 6-3 | 736 | REROLL | STABILIZE | 19.0 | 8 | 94 | 5 | 48.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 737 | SELL | STABILIZE | 19.0 | 8 | 92 | 5 | 48.0 | Caçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48516014218330383 | 0.0 | 0.0 | +— / -4cae9d83-6cc8-4a27-9c17-2e6f45091477 |
| Jogador 8 | 6-3 | 738 | PASS | STABILIZE | 19.0 | 8 | 100 | 5 | 48.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3614531457424164 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 742 | BUY | ALL_IN | 1.0 | 8 | 111 | 5 | 48.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0695981979370117 | 0.0 | 0.0 | +864500c7-31dd-4a7f-a5ab-8645f49d4e8a / -663c9fe5-55b8-4c50-b544-aba5b6e02070,e47e9d8e-e703-4b77-8266-2f90680eb62f |
| Jogador 8 | 6-4 | 743 | BUY | ALL_IN | 1.0 | 8 | 108 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7753496766090393 | 0.0 | 0.0 | +358601f9-8e68-4107-8719-8fdaee776f87 / -— |
| Jogador 8 | 6-4 | 744 | SELL | ALL_IN | 1.0 | 8 | 104 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4640282392501831 | 0.0 | 0.0 | +— / -864500c7-31dd-4a7f-a5ab-8645f49d4e8a |
| Jogador 8 | 6-4 | 745 | BUY | ALL_IN | 1.0 | 8 | 112 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9588554501533508 | 0.0 | 0.0 | +c83e0903-8994-4014-b0d6-76d9c26e4b22 / -— |
| Jogador 8 | 6-4 | 746 | REROLL | ALL_IN | 1.0 | 8 | 111 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 747 | SELL | ALL_IN | 1.0 | 8 | 109 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5049999952316284 | 0.0 | 0.0 | +— / -087138e8-3632-4703-b838-e0047a0e80c3 |
| Jogador 8 | 6-4 | 748 | BUY | ALL_IN | 1.0 | 8 | 117 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044370703399181366 | 0.0 | 0.0 | +d8e2c6ca-7b96-4e5a-afb4-85d5f2d9058e / -— |
| Jogador 8 | 6-4 | 749 | SELL | ALL_IN | 1.0 | 8 | 113 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -d8e2c6ca-7b96-4e5a-afb4-85d5f2d9058e |
| Jogador 8 | 6-4 | 750 | BUY | ALL_IN | 1.0 | 8 | 117 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18472754955291748 | 0.0 | 0.0 | +9bad8fab-03a2-4e1e-822b-963b09bcc62a / -— |
| Jogador 8 | 6-4 | 751 | REROLL | ALL_IN | 1.0 | 8 | 114 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 752 | PASS | ALL_IN | 1.0 | 8 | 112 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2930619716644287 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 759 | SELL | ALL_IN | 1.0 | 8 | 123 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01772216521203518 | 0.0 | 0.0 | +— / -9bad8fab-03a2-4e1e-822b-963b09bcc62a |
| Jogador 8 | 6-5 | 760 | BUY | ALL_IN | 1.0 | 8 | 126 | 5 | 42.0 | Caçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04805278778076172 | 0.0 | 0.0 | +5a9bb50e-c400-49f0-96bf-35de23a5e388 / -— |
| Jogador 8 | 6-5 | 761 | SELL | ALL_IN | 1.0 | 8 | 121 | 5 | 42.0 | Caçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3742923140525818 | 0.0 | 0.0 | +— / -8c28b034-ea67-4700-84c5-5dbd3059cbdb |
| Jogador 8 | 6-5 | 762 | BUY | ALL_IN | 1.0 | 8 | 132 | 5 | 42.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04239427298307419 | 0.0 | 0.0 | +6f557758-bcc6-4354-9119-c86fc5dde945 / -— |
| Jogador 8 | 6-5 | 763 | SELL | ALL_IN | 1.0 | 8 | 127 | 5 | 42.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -9061935a-18ba-4903-a48c-8ff90432875e |
| Jogador 8 | 6-5 | 764 | BUY | ALL_IN | 1.0 | 8 | 131 | 5 | 42.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12082566320896149 | 0.0 | 0.0 | +ce444b53-573e-4e50-b9a7-cc3cfb087b69 / -— |
| Jogador 8 | 6-5 | 765 | REROLL | ALL_IN | 1.0 | 8 | 127 | 5 | 42.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 766 | SELL | ALL_IN | 1.0 | 8 | 125 | 5 | 42.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -ce444b53-573e-4e50-b9a7-cc3cfb087b69 |
| Jogador 8 | 6-5 | 767 | MOVE_BENCH | ALL_IN | 1.0 | 8 | 129 | 5 | 42.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30687400698661804 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 768 | BUY | ALL_IN | 1.0 | 8 | 129 | 5 | 44.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23183831572532654 | 0.0 | 0.0 | +a2c0ba94-962f-447b-953b-a27f25ced40c / -— |
| Jogador 8 | 6-5 | 769 | PASS | ALL_IN | 1.0 | 8 | 126 | 5 | 44.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47441503405570984 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 772 | BUY | ALL_IN | 1.0 | 8 | 137 | 5 | 44.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39478376507759094 | 0.0 | 0.0 | +ef39d938-bee9-4290-95a4-da8a51088653 / -— |
| Jogador 8 | 6-6 | 773 | SELL | ALL_IN | 1.0 | 8 | 134 | 5 | 44.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -a2c0ba94-962f-447b-953b-a27f25ced40c |
| Jogador 8 | 6-6 | 774 | BUY | ALL_IN | 1.0 | 8 | 137 | 5 | 44.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06806446611881256 | 0.0 | 0.0 | +bed1d4a1-8791-49c9-b881-a91b3a35bad3 / -— |
| Jogador 8 | 6-6 | 775 | REROLL | ALL_IN | 1.0 | 8 | 133 | 5 | 44.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 776 | SELL | ALL_IN | 1.0 | 8 | 131 | 5 | 44.0 | Caçador/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -bed1d4a1-8791-49c9-b881-a91b3a35bad3 |
| Jogador 8 | 6-6 | 777 | BUY | ALL_IN | 1.0 | 8 | 135 | 5 | 44.0 | Caçador/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0699259042739868 | 0.0 | 0.0 | +105550a2-b9bd-4b92-98d8-49d95050f3e1 / -8b7968ee-f664-4b2a-b9e8-9b0ad6e81d79,bb51728e-fcc5-4950-ad03-c864c51c2371 |
| Jogador 8 | 6-6 | 778 | BUY | ALL_IN | 1.0 | 8 | 131 | 5 | 36.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0694602727890015 | 0.0 | 0.0 | +a0f77ac2-10b9-4e83-a9da-54bf70c1f177 / -4ac49c80-f0c3-47ae-a031-96928d244e13,b92739a6-903f-4298-b146-b370a8adcc29 |
| Jogador 8 | 6-6 | 779 | BUY | ALL_IN | 1.0 | 8 | 127 | 5 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35821980237960815 | 0.0 | 0.0 | +feb29e3c-5554-410e-a677-8c3e335a4531 / -— |
| Jogador 8 | 6-6 | 780 | MOVE_BENCH | ALL_IN | 1.0 | 8 | 125 | 5 | 28.0 | Caçador/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19595269858837128 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 781 | MOVE_BENCH | ALL_IN | 1.0 | 8 | 125 | 5 | 22.0 | Caçador/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09076005220413208 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 782 | PASS | ALL_IN | 1.0 | 8 | 125 | 5 | 32.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47345247864723206 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 193 | 222 | 50 | 15 | 13 | 2 | 20 | 5 | 0 | 56.0 |
- Jogador 1 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 118g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 40g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 4g, stage 2: 19g, stage 3: 80g, stage 4: 104g, stage 5: 15g
| Jogador 2 | 243 | 318 | 135 | 12 | 23 | 0 | 7 | 1 | 80 | 54.0 |
- Jogador 2 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 204g, BUY_XP: 100g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 14g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 5g, stage 2: 47g, stage 3: 53g, stage 4: 48g, stage 5: 78g, stage 6: 87g
| Jogador 3 | 162 | 205 | 2 | 10 | 32 | 2 | 0 | 0 | 0 | 40.0 |
- Jogador 3 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 57g, BUY_XP: 148g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 9g, stage 3: 59g, stage 4: 110g, stage 5: 20g
| Jogador 4 | 192 | 204 | 50 | 11 | 12 | 1 | 13 | 1 | 0 | 38.0 |
- Jogador 4 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 122g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 26g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 5g, stage 2: 29g, stage 3: 72g, stage 4: 92g, stage 5: 6g
| Jogador 5 | 186 | 238 | 80 | 18 | 18 | 1 | 12 | 2 | 11 | 42.0 |
- Jogador 5 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 134g, BUY_XP: 80g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 24g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 6g, stage 2: 22g, stage 3: 77g, stage 4: 60g, stage 5: 73g
| Jogador 6 | 190 | 233 | 54 | 15 | 12 | 1 | 27 | 5 | 1 | 50.0 |
- Jogador 6 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 119g, BUY_XP: 60g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 54g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 19g, stage 3: 95g, stage 4: 95g, stage 5: 17g
| Jogador 7 | 155 | 206 | 59 | 15 | 9 | 1 | 21 | 2 | 12 | 38.0 |
- Jogador 7 — gasto por ação: BUY: 124g, BUY_XP: 40g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 42g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 7g, stage 2: 13g, stage 3: 92g, stage 4: 94g
| Jogador 8 | 266 | 365 | 178 | 24 | 20 | 1 | 15 | 2 | 125 | 32.0 |
- Jogador 8 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 243g, BUY_XP: 92g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 30g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 5g, stage 2: 32g, stage 3: 79g, stage 4: 41g, stage 5: 103g, stage 6: 105g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 16 | 20 |
- Jogador 1 · 2-2 · step 150: PASS com 7g, HP 100, nível 4/8 (STABILIZE).
- Jogador 1 · 3-5 · step 402: PASS com 42g, HP 80, nível 6/8 (FAST8).
- Jogador 1 · 3-6 · step 422: PASS com 41g, HP 70, nível 7/8 (FAST8).
- Jogador 1 · 3-7 · step 442: PASS com 20g, HP 59, nível 7/8 (FAST8).
- Jogador 1 · 4-1 · step 458: PASS com 13g, HP 59, nível 7/8 (FAST8).
- Jogador 1 · 4-2 · step 473: REROLL com 19g, HP 59, nível 7/8 (FAST8).
- Jogador 1 · 4-2 · step 474: REROLL com 17g, HP 59, nível 7/8 (FAST8).
- Jogador 1 · 4-2 · step 479: REROLL com 9g, HP 59, nível 7/8 (FAST8).
- Jogador 1 · 4-2 · step 482: PASS com 6g, HP 59, nível 7/8 (FAST8).
- Jogador 1 · 4-3 · step 492: REROLL com 11g, HP 47, nível 7/8 (FAST8).
- Jogador 1 · 4-3 · step 495: REROLL com 9g, HP 47, nível 7/8 (FAST8).
- Jogador 1 · 4-4 · step 514: REROLL com 5g, HP 36, nível 7/8 (STABILIZE).
- Jogador 1 · 4-5 · step 532: REROLL com 6g, HP 36, nível 7/8 (STABILIZE).
- Jogador 1 · 4-5 · step 533: REROLL com 4g, HP 36, nível 7/8 (STABILIZE).
- Jogador 1 · 4-5 · step 537: REROLL com 6g, HP 36, nível 7/8 (STABILIZE).
- Jogador 1 · 4-5 · step 541: REROLL com 5g, HP 36, nível 7/8 (STABILIZE).
- Jogador 1 · 5-1 · step 583: REROLL com 7g, HP 11, nível 7/8 (ALL_IN).
- Jogador 1 · 5-1 · step 584: REROLL com 5g, HP 11, nível 7/8 (ALL_IN).
- Jogador 1 · 5-2 · step 601: REROLL com 6g, HP 11, nível 7/8 (ALL_IN).
- Jogador 1 · 5-2 · step 602: REROLL com 4g, HP 11, nível 7/8 (ALL_IN).
| Jogador 2 | 25 | 1 |
- Jogador 2 · 3-4 · step 377: PASS com 7g, HP 94, nível 7/8 (FAST8).
| Jogador 3 | 37 | 4 |
- Jogador 3 · 2-2 · step 152: PASS com 5g, HP 95, nível 4/8 (STABILIZE).
- Jogador 3 · 2-3 · step 174: PASS com 11g, HP 90, nível 4/8 (STABILIZE).
- Jogador 3 · 3-7 · step 442: PASS com 52g, HP 64, nível 7/8 (FAST8).
- Jogador 3 · 4-1 · step 462: PASS com 28g, HP 64, nível 7/8 (FAST8).
| Jogador 4 | 14 | 16 |
- Jogador 4 · 2-1 · step 129: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 4 · 2-2 · step 151: PASS com 9g, HP 94, nível 4/8 (STABILIZE).
- Jogador 4 · 2-3 · step 174: PASS com 15g, HP 88, nível 4/8 (STABILIZE).
- Jogador 4 · 2-5 · step 230: PASS com 30g, HP 82, nível 4/8 (STABILIZE).
- Jogador 4 · 3-3 · step 359: PASS com 12g, HP 61, nível 7/8 (FAST8).
- Jogador 4 · 4-3 · step 495: REROLL com 4g, HP 38, nível 7/8 (STABILIZE).
- Jogador 4 · 4-3 · step 502: PASS com 4g, HP 38, nível 7/8 (STABILIZE).
- Jogador 4 · 4-4 · step 513: REROLL com 8g, HP 38, nível 7/8 (STABILIZE).
- Jogador 4 · 4-5 · step 536: REROLL com 6g, HP 38, nível 7/8 (STABILIZE).
- Jogador 4 · 4-5 · step 541: PASS com 4g, HP 38, nível 7/8 (STABILIZE).
- Jogador 4 · 4-6 · step 553: REROLL com 10g, HP 27, nível 7/8 (STABILIZE).
- Jogador 4 · 4-6 · step 557: REROLL com 5g, HP 27, nível 7/8 (STABILIZE).
- Jogador 4 · 4-7 · step 572: REROLL com 9g, HP 13, nível 7/8 (ALL_IN).
- Jogador 4 · 4-7 · step 575: REROLL com 5g, HP 13, nível 7/8 (ALL_IN).
- Jogador 4 · 5-1 · step 583: REROLL com 6g, HP 13, nível 7/8 (ALL_IN).
- Jogador 4 · 5-1 · step 584: REROLL com 4g, HP 13, nível 7/8 (ALL_IN).
| Jogador 5 | 20 | 14 |
- Jogador 5 · 2-2 · step 153: PASS com 7g, HP 95, nível 4/8 (STABILIZE).
- Jogador 5 · 2-4 · step 205: PASS com 5g, HP 90, nível 5/8 (STABILIZE).
- Jogador 5 · 2-5 · step 231: PASS com 10g, HP 90, nível 5/8 (STABILIZE).
- Jogador 5 · 2-6 · step 254: PASS com 16g, HP 84, nível 5/8 (STABILIZE).
- Jogador 5 · 2-7 · step 280: PASS com 23g, HP 84, nível 5/8 (STABILIZE).
- Jogador 5 · 3-1 · step 305: PASS com 30g, HP 84, nível 5/8 (STABILIZE).
- Jogador 5 · 3-2 · step 330: PASS com 38g, HP 75, nível 5/8 (STABILIZE).
- Jogador 5 · 3-3 · step 352: PASS com 47g, HP 66, nível 6/8 (STABILIZE).
- Jogador 5 · 3-4 · step 381: PASS com 19g, HP 66, nível 7/8 (STABILIZE).
- Jogador 5 · 4-4 · step 514: REROLL com 6g, HP 53, nível 7/8 (FAST8).
- Jogador 5 · 4-5 · step 533: REROLL com 5g, HP 53, nível 7/8 (FAST8).
- Jogador 5 · 4-6 · step 553: REROLL com 11g, HP 53, nível 7/8 (FAST8).
- Jogador 5 · 4-6 · step 558: PASS com 5g, HP 53, nível 7/8 (FAST8).
- Jogador 5 · 4-7 · step 576: REROLL com 4g, HP 39, nível 7/8 (FAST8).
| Jogador 6 | 15 | 32 |
- Jogador 6 · 2-2 · step 150: PASS com 8g, HP 100, nível 4/8 (STABILIZE).
- Jogador 6 · 2-3 · step 174: PASS com 15g, HP 100, nível 4/8 (STABILIZE).
- Jogador 6 · 2-4 · step 203: PASS com 23g, HP 100, nível 4/8 (STABILIZE).
- Jogador 6 · 2-5 · step 237: PASS com 23g, HP 100, nível 5/8 (STABILIZE).
- Jogador 6 · 3-2 · step 331: PASS com 47g, HP 89, nível 6/8 (FAST8).
- Jogador 6 · 3-3 · step 352: PASS com 54g, HP 89, nível 6/8 (FAST8).
- Jogador 6 · 3-5 · step 402: PASS com 43g, HP 79, nível 6/8 (FAST8).
- Jogador 6 · 3-6 · step 422: PASS com 26g, HP 69, nível 7/8 (FAST8).
- Jogador 6 · 3-7 · step 437: REROLL com 20g, HP 60, nível 7/8 (FAST8).
- Jogador 6 · 3-7 · step 440: REROLL com 12g, HP 60, nível 7/8 (FAST8).
- Jogador 6 · 3-7 · step 442: PASS com 11g, HP 60, nível 7/8 (FAST8).
- Jogador 6 · 4-1 · step 453: REROLL com 14g, HP 60, nível 7/8 (FAST8).
- Jogador 6 · 4-1 · step 456: REROLL com 13g, HP 60, nível 7/8 (FAST8).
- Jogador 6 · 4-1 · step 461: REROLL com 12g, HP 60, nível 7/8 (FAST8).
- Jogador 6 · 4-1 · step 462: PASS com 10g, HP 60, nível 7/8 (FAST8).
- Jogador 6 · 4-2 · step 476: REROLL com 13g, HP 46, nível 7/8 (FAST8).
- Jogador 6 · 4-2 · step 479: REROLL com 11g, HP 46, nível 7/8 (FAST8).
- Jogador 6 · 4-2 · step 482: PASS com 10g, HP 46, nível 7/8 (FAST8).
- Jogador 6 · 4-3 · step 496: REROLL com 9g, HP 34, nível 7/8 (STABILIZE).
- Jogador 6 · 4-4 · step 514: REROLL com 9g, HP 34, nível 7/8 (STABILIZE).
- Jogador 6 · 4-4 · step 517: REROLL com 7g, HP 34, nível 7/8 (STABILIZE).
- Jogador 6 · 4-4 · step 518: REROLL com 5g, HP 34, nível 7/8 (STABILIZE).
- Jogador 6 · 4-5 · step 532: REROLL com 6g, HP 34, nível 7/8 (STABILIZE).
- Jogador 6 · 4-5 · step 533: REROLL com 4g, HP 34, nível 7/8 (STABILIZE).
- Jogador 6 · 4-6 · step 553: REROLL com 6g, HP 22, nível 7/8 (STABILIZE).
- Jogador 6 · 4-6 · step 556: REROLL com 6g, HP 22, nível 7/8 (STABILIZE).
- Jogador 6 · 4-6 · step 557: REROLL com 4g, HP 22, nível 7/8 (STABILIZE).
- Jogador 6 · 4-7 · step 572: REROLL com 7g, HP 22, nível 7/8 (STABILIZE).
- Jogador 6 · 4-7 · step 573: REROLL com 5g, HP 22, nível 7/8 (STABILIZE).
- Jogador 6 · 5-1 · step 585: REROLL com 8g, HP 22, nível 7/8 (STABILIZE).
- Jogador 6 · 5-1 · step 586: REROLL com 6g, HP 22, nível 7/8 (STABILIZE).
- Jogador 6 · 5-1 · step 587: REROLL com 4g, HP 22, nível 7/8 (STABILIZE).
| Jogador 7 | 10 | 26 |
- Jogador 7 · 2-2 · step 152: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 7 · 2-3 · step 174: PASS com 11g, HP 100, nível 4/8 (STABILIZE).
- Jogador 7 · 3-5 · step 402: PASS com 32g, HP 55, nível 6/8 (FAST8).
- Jogador 7 · 3-6 · step 414: REROLL com 35g, HP 44, nível 6/8 (FAST8).
- Jogador 7 · 3-7 · step 434: REROLL com 28g, HP 32, nível 7/8 (STABILIZE).
- Jogador 7 · 3-7 · step 439: REROLL com 26g, HP 32, nível 7/8 (STABILIZE).
- Jogador 7 · 3-7 · step 442: PASS com 25g, HP 32, nível 7/8 (STABILIZE).
- Jogador 7 · 4-1 · step 456: REROLL com 28g, HP 32, nível 7/8 (STABILIZE).
- Jogador 7 · 4-1 · step 457: REROLL com 26g, HP 32, nível 7/8 (STABILIZE).
- Jogador 7 · 4-1 · step 458: REROLL com 24g, HP 32, nível 7/8 (STABILIZE).
- Jogador 7 · 4-1 · step 462: PASS com 16g, HP 32, nível 7/8 (STABILIZE).
- Jogador 7 · 4-2 · step 473: REROLL com 22g, HP 19, nível 7/8 (STABILIZE).
- Jogador 7 · 4-2 · step 476: REROLL com 20g, HP 19, nível 7/8 (STABILIZE).
- Jogador 7 · 4-2 · step 479: REROLL com 18g, HP 19, nível 7/8 (STABILIZE).
- Jogador 7 · 4-2 · step 482: PASS com 17g, HP 19, nível 7/8 (STABILIZE).
- Jogador 7 · 4-3 · step 494: REROLL com 19g, HP 19, nível 7/8 (STABILIZE).
- Jogador 7 · 4-3 · step 499: REROLL com 10g, HP 19, nível 7/8 (STABILIZE).
- Jogador 7 · 4-3 · step 502: PASS com 8g, HP 19, nível 7/8 (STABILIZE).
- Jogador 7 · 4-4 · step 514: REROLL com 13g, HP 5, nível 7/8 (ALL_IN).
- Jogador 7 · 4-4 · step 517: REROLL com 10g, HP 5, nível 7/8 (ALL_IN).
- Jogador 7 · 4-4 · step 520: REROLL com 8g, HP 5, nível 7/8 (ALL_IN).
- Jogador 7 · 4-4 · step 522: PASS com 11g, HP 5, nível 7/8 (ALL_IN).
- Jogador 7 · 4-5 · step 535: REROLL com 12g, HP 5, nível 7/8 (ALL_IN).
- Jogador 7 · 4-5 · step 538: REROLL com 11g, HP 5, nível 7/8 (ALL_IN).
- Jogador 7 · 4-5 · step 541: REROLL com 14g, HP 5, nível 7/8 (ALL_IN).
- Jogador 7 · 4-5 · step 542: PASS com 12g, HP 5, nível 7/8 (ALL_IN).
| Jogador 8 | 23 | 11 |
- Jogador 8 · 1-4 · step 98: PASS com 4g, HP 100, nível 3/8 (STABILIZE).
- Jogador 8 · 2-1 · step 125: PASS com 7g, HP 100, nível 4/8 (STABILIZE).
- Jogador 8 · 2-4 · step 204: PASS com 5g, HP 95, nível 5/8 (STABILIZE).
- Jogador 8 · 2-5 · step 235: PASS com 11g, HP 95, nível 5/8 (STABILIZE).
- Jogador 8 · 2-6 · step 258: PASS com 16g, HP 89, nível 5/8 (STABILIZE).
- Jogador 8 · 2-7 · step 282: PASS com 23g, HP 83, nível 5/8 (STABILIZE).
- Jogador 8 · 3-1 · step 304: PASS com 31g, HP 83, nível 5/8 (STABILIZE).
- Jogador 8 · 3-2 · step 333: PASS com 37g, HP 83, nível 5/8 (STABILIZE).
- Jogador 8 · 3-3 · step 353: PASS com 42g, HP 73, nível 6/8 (FAST8).
- Jogador 8 · 3-4 · step 381: PASS com 16g, HP 73, nível 7/8 (FAST8).
- Jogador 8 · 3-5 · step 394: PASS com 22g, HP 73, nível 7/8 (FAST8).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 3 | 3 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 2 | 2 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 193 | 28 | 27 | 138 | -0.0034 | -0.6377 | -0.0057 | 0.4479 | 0.0023 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0216 (43 ações), BUY_XP: Δ 0.0000 (16 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0053 (60 ações), MOVE_BOARD: Δ -0.0359 (8 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0000 (20 ações), SELL: Δ 0.0150 (16 ações)
| Jogador 2 | 243 | 28 | 26 | 189 | 0.0001 | -0.0119 | -0.0026 | 0.5241 | 0.0026 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (2 ações), BUY: Δ -0.0181 (70 ações), BUY_XP: Δ 0.0000 (25 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0176 (56 ações), MOVE_BOARD: Δ -0.0321 (2 ações), PASS: Δ 0.0000 (38 ações), REROLL: Δ 0.0000 (7 ações), SELL: Δ 0.0088 (41 ações)
| Jogador 3 | 162 | 20 | 20 | 122 | 0.0027 | -0.0447 | -0.0001 | 0.4936 | 0.0028 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0029 (21 ações), BUY_XP: Δ 0.0000 (37 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0098 (70 ações), MOVE_BOARD: Δ -0.0938 (2 ações), PASS: Δ 0.0000 (28 ações), SELL: Δ 0.0000 (2 ações)
| Jogador 4 | 192 | 35 | 37 | 120 | -0.0040 | -0.8320 | -0.0063 | 0.3993 | 0.0023 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0227 (47 ações), BUY_XP: Δ 0.0000 (14 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0013 (66 ações), MOVE_BOARD: Δ 0.0119 (8 ações), PASS: Δ 0.0000 (26 ações), REROLL: Δ 0.0000 (13 ações), SELL: Δ 0.0075 (16 ações)
| Jogador 5 | 186 | 24 | 26 | 136 | 0.0027 | -0.1895 | 0.0009 | 0.4499 | 0.0019 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0148 (48 ações), BUY_XP: Δ 0.0000 (20 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0192 (44 ações), MOVE_BOARD: Δ 0.0120 (6 ações), PASS: Δ 0.0000 (30 ações), REROLL: Δ 0.0000 (12 ações), SELL: Δ 0.0125 (24 ações)
| Jogador 6 | 190 | 24 | 27 | 139 | -0.0032 | -0.5973 | -0.0050 | 0.3869 | 0.0017 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0235 (46 ações), BUY_XP: Δ 0.0000 (15 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0008 (50 ações), MOVE_BOARD: Δ 0.1853 (2 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0000 (27 ações), SELL: Δ 0.0029 (21 ações)
| Jogador 7 | 155 | 21 | 22 | 112 | 0.0007 | -0.2556 | -0.0025 | 0.5013 | 0.0031 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0240 (44 ações), BUY_XP: Δ 0.0000 (10 ações), MOVE_BENCH: Δ 0.0187 (35 ações), MOVE_BOARD: Δ -0.0460 (2 ações), PASS: Δ 0.0000 (23 ações), REROLL: Δ 0.0000 (21 ações), SELL: Δ 0.0300 (20 ações)
| Jogador 8 | 266 | 30 | 34 | 202 | -0.0022 | -0.2115 | -0.0037 | 0.4669 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (2 ações), BUY: Δ -0.0151 (79 ações), BUY_XP: Δ 0.0000 (23 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0030 (54 ações), MOVE_BOARD: Δ -0.0047 (5 ações), PASS: Δ 0.0000 (38 ações), REROLL: Δ 0.0000 (15 ações), SELL: Δ 0.0100 (48 ações)
- Jogador 1 — rounds avaliados: 27; correlação estrutural/combate: 0.390; posicional/combate: 0.089.
- Jogador 1 — combate positive: score estrutural prévio -0.336
  score posicional prévio 0.481
- Jogador 1 — combate negative: score estrutural prévio -0.768
  score posicional prévio 0.451
- Jogador 2 — rounds avaliados: 38; correlação estrutural/combate: 0.133; posicional/combate: 0.102.
- Jogador 2 — combate positive: score estrutural prévio 0.008
  score posicional prévio 0.534
- Jogador 2 — combate negative: score estrutural prévio -0.081
  score posicional prévio 0.536
- Jogador 3 — rounds avaliados: 28; correlação estrutural/combate: -0.112; posicional/combate: 0.081.
- Jogador 3 — combate positive: score estrutural prévio -0.042
  score posicional prévio 0.506
- Jogador 3 — combate negative: score estrutural prévio -0.020
  score posicional prévio 0.491
- Jogador 4 — rounds avaliados: 26; correlação estrutural/combate: 0.380; posicional/combate: 0.365.
- Jogador 4 — combate positive: score estrutural prévio -0.683
  score posicional prévio 0.438
- Jogador 4 — combate negative: score estrutural prévio -0.990
  score posicional prévio 0.349
- Jogador 5 — rounds avaliados: 30; correlação estrutural/combate: 0.131; posicional/combate: 0.225.
- Jogador 5 — combate positive: score estrutural prévio -0.080
  score posicional prévio 0.491
- Jogador 5 — combate negative: score estrutural prévio -0.208
  score posicional prévio 0.449
- Jogador 6 — rounds avaliados: 27; correlação estrutural/combate: 0.074; posicional/combate: 0.483.
- Jogador 6 — combate positive: score estrutural prévio -0.491
  score posicional prévio 0.490
- Jogador 6 — combate negative: score estrutural prévio -0.603
  score posicional prévio 0.371
- Jogador 7 — rounds avaliados: 23; correlação estrutural/combate: 0.298; posicional/combate: 0.098.
- Jogador 7 — combate positive: score estrutural prévio -0.095
  score posicional prévio 0.539
- Jogador 7 — combate negative: score estrutural prévio -0.230
  score posicional prévio 0.519
- Jogador 8 — rounds avaliados: 38; correlação estrutural/combate: 0.426; posicional/combate: 0.245.
- Jogador 8 — combate positive: score estrutural prévio -0.042
  score posicional prévio 0.488
- Jogador 8 — combate negative: score estrutural prévio -0.465
  score posicional prévio 0.444

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 219 | OK (219) | 0 | 1 | 0 | 1 | 1 | 1 |
- Jogador 1 — IDs equipados observados: TFT_Item_IonicSpark; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 1 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow.
- Jogador 1 — bigorna 5-1 step 582: seleção TFT_Item_RecurveBow entre TFT_Item_RecurveBow, TFT_Item_BFSword, TFT_Item_Spatula; consistente: True; fit 0.0.
| Jogador 2 | 281 | OK (281) | 0 | 2 | 0 | 1 | 2 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_BlueBuff, TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 2, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 2 — bigornas: 2 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_Spatula, TFT_Item_TearOfTheGoddess.
- Jogador 2 — bigorna 5-1 step 582: seleção TFT_Item_TearOfTheGoddess entre TFT_Item_TearOfTheGoddess, TFT_Item_ChainVest, TFT_Item_FryingPan; consistente: True; fit 0.0.
- Jogador 2 — bigorna 6-1 step 697: seleção TFT_Item_IonicSpark entre TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_InfinityEdge, DA_18_EmblemBlossom; consistente: True; fit 0.0.
| Jogador 3 | 189 | OK (189) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 3 — IDs equipados observados: TFT_Item_JeweledGauntlet; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 3 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_NeedlesslyLargeRod, TFT_Item_Spatula.
- Jogador 3 — bigorna 5-1 step 582: seleção TFT_Item_SparringGloves entre TFT_Item_SparringGloves, TFT_Item_FryingPan, TFT_Item_Spatula; consistente: True; fit 0.0.
| Jogador 4 | 217 | OK (217) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 4 — IDs equipados observados: TFT_Item_Redemption; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 4 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_GiantsBelt, TFT_Item_TearOfTheGoddess.
- Jogador 4 — bigorna 5-1 step 582: seleção TFT_Item_BFSword entre TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak; consistente: True; fit 0.0.
| Jogador 5 | 215 | OK (215) | 0 | 0 | 1 | 1 | 1 | 1 |
- Jogador 5 — IDs equipados observados: TFT_Item_TitansResolve; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 5 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_FryingPan, TFT_Item_RecurveBow.
- Jogador 5 — bigorna 5-1 step 582: seleção TFT_Item_RecurveBow entre TFT_Item_RecurveBow, TFT_Item_FryingPan, TFT_Item_GiantsBelt; consistente: True; fit 0.0.
| Jogador 6 | 216 | OK (216) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 6 — IDs equipados observados: TFT_Item_Quicksilver; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 6 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_SparringGloves, TFT_Item_Spatula.
- Jogador 6 — bigorna 5-1 step 582: seleção TFT_Item_NegatronCloak entre TFT_Item_NegatronCloak, TFT_Item_GiantsBelt, TFT_Item_BFSword; consistente: True; fit 0.0.
| Jogador 7 | 177 | OK (177) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 7 — IDs equipados observados: nenhum observado; eventos: COMPONENT_LOOT_GRANTED: 16.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 0 (conversões observadas: 0); componentes persistentes entre rounds: TFT_Item_SparringGloves, TFT_Item_Spatula.
- Jogador 7 — revisão de conversão: componentes foram observados, mas nenhuma ação de craft/equip foi registrada; isso não prova receita viável.
| Jogador 8 | 303 | OK (303) | 2 | 0 | 0 | 1 | 2 | 1 |
- Jogador 8 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_LastWhisper; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 2, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 8 — bigornas: 2 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_NegatronCloak.
- Jogador 8 — bigorna 5-1 step 582: seleção TFT_Item_NegatronCloak entre TFT_Item_NegatronCloak, TFT_Item_Spatula, TFT_Item_RecurveBow; consistente: True; fit 0.0.
- Jogador 8 — bigorna 6-1 step 697: seleção TFT_Item_LastWhisper entre TFT_Item_LastWhisper, TFT_Item_SpearOfShojin, TFT_Item_SpectralGauntlet, TFT_Item_ArchangelsStaff; consistente: True; fit 0.0.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 1 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.016 | 0.000 |
| Jogador 1 | 1-3 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.110 | 0.000 |
| Jogador 1 | 1-4 | 4 | -2.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 4 → 7 | 1 | 3 → 4 | 0.188 | 0.000 |
| Jogador 1 | 2-1 | 9 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 7 → 7 | 6 | 4 → 4 | -0.004 | 0.293 |
| Jogador 1 | 2-2 | 4 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 7 → 12 | 0 | 4 → 4 | -0.173 | -0.593 |
| Jogador 1 | 2-3 | 12 | 4.000 | 0.000 | 0 → 0 | 1 → 2 | 14% → 18% | 12 → 12 | 8 | 4 → 5 | 0.076 | 0.216 |
| Jogador 1 | 2-4 | 6 | 2.000 | 2.000 | 0 → 0 | 2 → 1 | 18% → 18% | 12 → 16 | 3 | 5 → 5 | -0.125 | 0.000 |
| Jogador 1 | 2-5 | 8 | -2.000 | 0.000 | 0 → 0 | 1 → 2 | 18% → 18% | 16 → 23 | 2 | 5 → 5 | 0.094 | -0.290 |
| Jogador 1 | 2-6 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 23 → 31 | 0 | 5 → 5 | 0.000 | 0.377 |
| Jogador 1 | 2-7 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 31 → 39 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 1 | 3-1 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 39 → 50 | 0 | 5 → 5 | 0.000 | 0.460 |
| Jogador 1 | 3-2 | 9 | 6.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 50 → 56 | 4 | 5 → 5 | -0.079 | -0.293 |
| Jogador 1 | 3-3 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 56 → 67 | 0 | 5 → 5 | 0.006 | 0.552 |
| Jogador 1 | 3-4 | 12 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 21% | 67 → 72 | 5 | 5 → 6 | -0.013 | 0.000 |
| Jogador 1 | 3-5 | 12 | 2.000 | -2.000 | 0 → 1 | 2 → 1 | 21% → 18% | 72 → 51 | 30 | 6 → 6 | 0.033 | -0.224 |
| Jogador 1 | 3-6 | 12 | 4.000 | 4.000 | 1 → 2 | 1 → 1 | 18% → 18% | 51 → 51 | 10 | 6 → 7 | 0.018 | -0.231 |
| Jogador 1 | 3-7 | 12 | 16.000 | 6.000 | 2 → 2 | 1 → 1 | 18% → 25% | 51 → 28 | 31 | 7 → 7 | -0.057 | 0.000 |
| Jogador 1 | 4-1 | 8 | 0.000 | 30.000 | 2 → 2 | 1 → 2 | 25% → 25% | 28 → 20 | 15 | 7 → 7 | 0.000 | 0.379 |
| Jogador 1 | 4-2 | 12 | 0.000 | 10.000 | 2 → 2 | 2 → 4 | 25% → 25% | 20 → 11 | 20 | 7 → 7 | -0.005 | -0.235 |
| Jogador 1 | 4-3 | 10 | 0.000 | 8.000 | 2 → 2 | 4 → 3 | 25% → 25% | 11 → 6 | 17 | 7 → 7 | -0.006 | -0.268 |
| Jogador 1 | 4-4 | 11 | -4.000 | 4.000 | 2 → 2 | 3 → 2 | 25% → 21% | 6 → 6 | 17 | 7 → 7 | -0.019 | 0.000 |
| Jogador 1 | 4-5 | 12 | 0.000 | -8.000 | 2 → 2 | 2 → 3 | 21% → 21% | 6 → 9 | 16 | 7 → 7 | 0.010 | -0.233 |
| Jogador 1 | 4-6 | 11 | 14.000 | -6.000 | 2 → 3 | 3 → 3 | 21% → 25% | 9 → 6 | 14 | 7 → 7 | 0.002 | -0.251 |
| Jogador 1 | 4-7 | 4 | 0.000 | 6.000 | 3 → 3 | 3 → 3 | 25% → 25% | 6 → 7 | 5 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 8 | 0.000 | 2.000 | 3 → 3 | 3 → 4 | 25% → 25% | 7 → 6 | 9 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-2 | 5 | -56.000 | -58.000 | 3 → 0 | 4 → 0 | 25% → 0% | 6 → 0 | 6 | 7 → 7 | 0.131 | -0.580 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 16, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 29 ações e piorou em 27.
- Jogador 1 — estado final: ouro 0, nível 7, vida 11.0, colocação 6.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 2 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.014 | 0.000 |
| Jogador 2 | 1-3 | 4 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.022 | 0.000 |
| Jogador 2 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 2 | 2-1 | 8 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 7 → 8 | 5 | 4 → 4 | 0.001 | 0.320 |
| Jogador 2 | 2-2 | 7 | 4.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 18% | 8 → 9 | 6 | 4 → 5 | -0.013 | 0.359 |
| Jogador 2 | 2-3 | 4 | -2.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 18% | 9 → 14 | 0 | 5 → 5 | -0.014 | -0.607 |
| Jogador 2 | 2-4 | 4 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 18% → 18% | 14 → 20 | 0 | 5 → 5 | 0.014 | 0.000 |
| Jogador 2 | 2-5 | 4 | -2.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 18% | 20 → 28 | 0 | 5 → 5 | -0.003 | 0.647 |
| Jogador 2 | 2-6 | 12 | 6.000 | -2.000 | 0 → 0 | 2 → 3 | 18% → 21% | 28 → 18 | 18 | 5 → 6 | 0.002 | 0.235 |
| Jogador 2 | 2-7 | 12 | 6.000 | 2.000 | 0 → 0 | 3 → 2 | 21% → 21% | 18 → 8 | 18 | 6 → 6 | 0.003 | 0.000 |
| Jogador 2 | 3-1 | 7 | 4.000 | -2.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 10 | 7 | 6 → 6 | 0.016 | 0.421 |
| Jogador 2 | 3-2 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 1 | 21% → 21% | 10 → 9 | 9 | 6 → 7 | 0.000 | 0.469 |
| Jogador 2 | 3-3 | 6 | 8.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 25% | 9 → 9 | 8 | 7 → 7 | -0.005 | 0.492 |
| Jogador 2 | 3-4 | 8 | -2.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 14 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 3-5 | 8 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 25% → 25% | 14 → 7 | 12 | 7 → 7 | 0.000 | -0.334 |
| Jogador 2 | 3-6 | 9 | 8.000 | -4.000 | 0 → 1 | 1 → 0 | 25% → 25% | 7 → 9 | 6 | 7 → 7 | -0.081 | 0.332 |
| Jogador 2 | 3-7 | 5 | 2.000 | 6.000 | 1 → 1 | 0 → 1 | 25% → 25% | 9 → 6 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 6 | -2.000 | 2.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 9 | 8 | 7 → 7 | 0.098 | 0.494 |
| Jogador 2 | 4-2 | 7 | 0.000 | -6.000 | 1 → 1 | 1 → 2 | 25% → 25% | 9 → 5 | 13 | 7 → 7 | 0.009 | -0.388 |
| Jogador 2 | 4-3 | 3 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 5 → 7 | 4 | 7 → 8 | 0.000 | -0.905 |
| Jogador 2 | 4-4 | 5 | 2.000 | 10.000 | 1 → 1 | 2 → 3 | 25% → 29% | 7 → 7 | 6 | 8 → 8 | -0.023 | 0.000 |
| Jogador 2 | 4-5 | 4 | 0.000 | 12.000 | 1 → 1 | 3 → 3 | 29% → 29% | 7 → 7 | 6 | 8 → 8 | -0.015 | 0.740 |
| Jogador 2 | 4-6 | 7 | 10.000 | -10.000 | 1 → 1 | 3 → 2 | 29% → 29% | 7 → 9 | 5 | 8 → 8 | 0.054 | 0.419 |
| Jogador 2 | 4-7 | 4 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 29% → 29% | 9 → 9 | 6 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 6 | 0.000 | 10.000 | 1 → 1 | 2 → 2 | 29% → 29% | 9 → 7 | 9 | 8 → 8 | 0.000 | 0.523 |
| Jogador 2 | 5-2 | 4 | 0.000 | 14.000 | 1 → 1 | 2 → 3 | 29% → 29% | 7 → 7 | 7 | 8 → 8 | 0.000 | 0.746 |
| Jogador 2 | 5-3 | 6 | 0.000 | 12.000 | 1 → 1 | 3 → 4 | 29% → 29% | 7 → 9 | 9 | 8 → 8 | 0.000 | 0.498 |
| Jogador 2 | 5-4 | 11 | 0.000 | 10.000 | 1 → 1 | 4 → 3 | 29% → 29% | 9 → 9 | 12 | 8 → 8 | -0.003 | 0.000 |
| Jogador 2 | 5-5 | 8 | 0.000 | 0.000 | 1 → 1 | 3 → 2 | 29% → 29% | 9 → 15 | 13 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-6 | 8 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 29% → 29% | 15 → 25 | 11 | 8 → 8 | 0.000 | 0.367 |
| Jogador 2 | 5-7 | 12 | 0.000 | -4.000 | 1 → 1 | 3 → 2 | 29% → 29% | 25 → 35 | 17 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 12 | 0.000 | 8.000 | 1 → 1 | 2 → 3 | 29% → 29% | 35 → 41 | 14 | 8 → 8 | 0.000 | 0.251 |
| Jogador 2 | 6-2 | 12 | 0.000 | -8.000 | 1 → 1 | 3 → 2 | 29% → 29% | 41 → 56 | 18 | 8 → 8 | 0.000 | 0.250 |
| Jogador 2 | 6-3 | 12 | 0.000 | -6.000 | 1 → 1 | 2 → 3 | 29% → 29% | 56 → 71 | 16 | 8 → 8 | 0.000 | 0.250 |
| Jogador 2 | 6-4 | 12 | -10.000 | 12.000 | 1 → 1 | 3 → 3 | 29% → 25% | 71 → 77 | 13 | 8 → 8 | -0.044 | 0.000 |
| Jogador 2 | 6-5 | 12 | -6.000 | -6.000 | 1 → 1 | 3 → 3 | 25% → 21% | 77 → 90 | 12 | 8 → 8 | 0.002 | -0.242 |
| Jogador 2 | 6-6 | 12 | 12.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 25% | 90 → 81 | 14 | 8 → 8 | -0.015 | 0.250 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 21, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 28 ações e piorou em 26.
- Jogador 2 — estado final: ouro 81, nível 8, vida 42.0, colocação 1.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.014 | 0.000 |
| Jogador 3 | 1-3 | 6 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 4 | 1 | 3 → 3 | 0.000 | 0.000 |
| Jogador 3 | 1-4 | 6 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 11% → 14% | 4 → 4 | 4 | 3 → 4 | -0.011 | 0.000 |
| Jogador 3 | 2-1 | 7 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 4 → 6 | 4 | 4 → 4 | 0.017 | -0.346 |
| Jogador 3 | 2-2 | 6 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 11 | 2 | 4 → 4 | 0.000 | -0.387 |
| Jogador 3 | 2-3 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 14% | 11 → 18 | 0 | 4 → 5 | 0.000 | -0.646 |
| Jogador 3 | 2-4 | 7 | 6.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 18% | 18 → 22 | 3 | 5 → 5 | 0.010 | 0.000 |
| Jogador 3 | 2-5 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 22 → 30 | 0 | 5 → 5 | 0.000 | 0.527 |
| Jogador 3 | 2-6 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 30 → 38 | 0 | 5 → 5 | 0.000 | -0.659 |
| Jogador 3 | 2-7 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 38 → 46 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 3-1 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 46 → 56 | 0 | 5 → 5 | 0.000 | 0.553 |
| Jogador 3 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 56 → 68 | 0 | 5 → 5 | 0.000 | 0.703 |
| Jogador 3 | 3-3 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 68 → 78 | 0 | 5 → 5 | -0.003 | -0.555 |
| Jogador 3 | 3-4 | 12 | 4.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 21% | 78 → 62 | 26 | 5 → 6 | -0.005 | 0.000 |
| Jogador 3 | 3-5 | 6 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 21% → 21% | 62 → 73 | 0 | 6 → 6 | 0.000 | 0.475 |
| Jogador 3 | 3-6 | 9 | 2.000 | -2.000 | 0 → 1 | 2 → 1 | 21% → 21% | 73 → 83 | 2 | 6 → 6 | -0.014 | 0.302 |
| Jogador 3 | 3-7 | 12 | 4.000 | 2.000 | 1 → 1 | 1 → 1 | 21% → 21% | 83 → 63 | 31 | 6 → 7 | 0.003 | 0.000 |
| Jogador 3 | 4-1 | 12 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 21% → 21% | 63 → 35 | 35 | 7 → 7 | 0.000 | -0.233 |
| Jogador 3 | 4-2 | 8 | 0.000 | 0.000 | 1 → 0 | 2 → 2 | 21% → 25% | 35 → 40 | 4 | 7 → 8 | -0.016 | -0.352 |
| Jogador 3 | 4-3 | 12 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 40 → 45 | 4 | 8 → 8 | 0.000 | -0.226 |
| Jogador 3 | 4-4 | 6 | 8.000 | -8.000 | 0 → 0 | 2 → 2 | 25% → 29% | 45 → 55 | 0 | 8 → 8 | -0.007 | 0.000 |
| Jogador 3 | 4-5 | 12 | 0.000 | 16.000 | 0 → 0 | 2 → 2 | 29% → 29% | 55 → 22 | 40 | 8 → 8 | 0.000 | 0.233 |
| Jogador 3 | 4-6 | 7 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 29% → 29% | 22 → 9 | 20 | 8 → 8 | 0.000 | 0.419 |
| Jogador 3 | 4-7 | 4 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 29% → 29% | 9 → 8 | 7 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 5-1 | 8 | 2.000 | 6.000 | 0 → 0 | 2 → 2 | 29% → 32% | 8 → 7 | 8 | 8 → 9 | 0.021 | 0.367 |
| Jogador 3 | 5-2 | 4 | 0.000 | 14.000 | 0 → 0 | 2 → 2 | 32% → 32% | 7 → 5 | 7 | 9 → 9 | 0.000 | -0.700 |
| Jogador 3 | 5-3 | 3 | -40.000 | -58.000 | 0 → 0 | 2 → 0 | 32% → 0% | 5 → 0 | 5 | 9 → 9 | -0.145 | -0.933 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 10, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 4; mudanças de composição: 0; posicionamento melhorou em 20 ações e piorou em 21.
- Jogador 3 — estado final: ouro 0, nível 9, vida 10.0, colocação 4.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 4 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.002 | 0.000 |
| Jogador 4 | 1-3 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.126 | 0.000 |
| Jogador 4 | 1-4 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 6 | 2 | 3 → 4 | -0.066 | 0.000 |
| Jogador 4 | 2-1 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 6 → 9 | 2 | 4 → 4 | -0.042 | -0.276 |
| Jogador 4 | 2-2 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 15 | 0 | 4 → 4 | 0.000 | -0.516 |
| Jogador 4 | 2-3 | 4 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 15 → 22 | 0 | 4 → 4 | 0.200 | -0.645 |
| Jogador 4 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 22 → 30 | 0 | 4 → 4 | -0.010 | 0.000 |
| Jogador 4 | 2-5 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 30 → 39 | 0 | 4 → 5 | 0.068 | -0.496 |
| Jogador 4 | 2-6 | 8 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 39 → 46 | 3 | 5 → 5 | -0.087 | -0.310 |
| Jogador 4 | 2-7 | 12 | 6.000 | 2.000 | 0 → 0 | 1 → 2 | 18% → 21% | 46 → 31 | 24 | 5 → 6 | 0.041 | 0.000 |
| Jogador 4 | 3-1 | 6 | -2.000 | 2.000 | 0 → 1 | 2 → 1 | 21% → 18% | 31 → 39 | 2 | 6 → 6 | -0.023 | -0.431 |
| Jogador 4 | 3-2 | 6 | 4.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 21% | 39 → 46 | 2 | 6 → 6 | -0.064 | 0.461 |
| Jogador 4 | 3-3 | 12 | 0.000 | 12.000 | 1 → 1 | 1 → 1 | 21% → 21% | 46 → 18 | 34 | 6 → 7 | 0.037 | -0.231 |
| Jogador 4 | 3-4 | 9 | 6.000 | 12.000 | 1 → 1 | 1 → 3 | 21% → 25% | 18 → 6 | 17 | 7 → 7 | 0.003 | 0.000 |
| Jogador 4 | 3-5 | 9 | 6.000 | -6.000 | 1 → 2 | 3 → 1 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | 0.012 | 0.318 |
| Jogador 4 | 3-6 | 12 | 0.000 | 10.000 | 2 → 2 | 1 → 1 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | -0.014 | -0.230 |
| Jogador 4 | 3-7 | 8 | 2.000 | 4.000 | 2 → 2 | 1 → 0 | 25% → 25% | 5 → 5 | 5 | 7 → 7 | -0.015 | 0.000 |
| Jogador 4 | 4-1 | 11 | -4.000 | 14.000 | 2 → 1 | 0 → 0 | 25% → 25% | 5 → 6 | 5 | 7 → 7 | 0.041 | 0.269 |
| Jogador 4 | 4-2 | 12 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 25% → 25% | 6 → 7 | 16 | 7 → 7 | 0.005 | 0.249 |
| Jogador 4 | 4-3 | 12 | 0.000 | -2.000 | 1 → 1 | 1 → 2 | 25% → 25% | 7 → 11 | 17 | 7 → 7 | 0.000 | 0.238 |
| Jogador 4 | 4-4 | 12 | -6.000 | 12.000 | 1 → 1 | 2 → 2 | 25% → 21% | 11 → 9 | 14 | 7 → 7 | -0.006 | 0.000 |
| Jogador 4 | 4-5 | 11 | 12.000 | -6.000 | 1 → 2 | 2 → 2 | 21% → 25% | 9 → 9 | 8 | 7 → 7 | -0.056 | -0.239 |
| Jogador 4 | 4-6 | 12 | -12.000 | 12.000 | 2 → 1 | 2 → 1 | 25% → 21% | 9 → 9 | 17 | 7 → 7 | 0.007 | -0.244 |
| Jogador 4 | 4-7 | 12 | 8.000 | -4.000 | 1 → 2 | 1 → 1 | 21% → 25% | 9 → 6 | 15 | 7 → 7 | -0.012 | 0.000 |
| Jogador 4 | 5-1 | 6 | -38.000 | -72.000 | 2 → 0 | 1 → 0 | 25% → 0% | 6 → 0 | 6 | 7 → 7 | 0.128 | -0.492 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 10; mudanças de composição: 3; posicionamento melhorou em 36 ações e piorou em 37.
- Jogador 4 — estado final: ouro 0, nível 7, vida 13.0, colocação 7.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 5 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.022 | 0.000 |
| Jogador 5 | 1-3 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.106 | 0.000 |
| Jogador 5 | 1-4 | 5 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.105 | 0.000 |
| Jogador 5 | 2-1 | 7 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 7 | 3 | 4 → 4 | -0.152 | -0.346 |
| Jogador 5 | 2-2 | 7 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 7 → 13 | 3 | 4 → 4 | 0.181 | -0.332 |
| Jogador 5 | 2-3 | 9 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 13 → 6 | 13 | 4 → 5 | -0.016 | 0.306 |
| Jogador 5 | 2-4 | 6 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 10 | 3 | 5 → 5 | -0.115 | 0.000 |
| Jogador 5 | 2-5 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 10 → 16 | 0 | 5 → 5 | 0.005 | -0.405 |
| Jogador 5 | 2-6 | 4 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 16 → 23 | 0 | 5 → 5 | 0.165 | 0.647 |
| Jogador 5 | 2-7 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 23 → 30 | 0 | 5 → 5 | -0.103 | 0.000 |
| Jogador 5 | 3-1 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 30 → 38 | 0 | 5 → 5 | 0.123 | -0.507 |
| Jogador 5 | 3-2 | 5 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 38 → 47 | 0 | 5 → 6 | -0.124 | -0.517 |
| Jogador 5 | 3-3 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 21% | 47 → 57 | 0 | 6 → 6 | -0.018 | 0.492 |
| Jogador 5 | 3-4 | 12 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 57 → 25 | 38 | 6 → 7 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 11 | 2.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 25 → 8 | 24 | 7 → 7 | 0.054 | 0.251 |
| Jogador 5 | 3-6 | 6 | 4.000 | 4.000 | 0 → 0 | 0 → 1 | 21% → 25% | 8 → 7 | 8 | 7 → 7 | 0.057 | 0.492 |
| Jogador 5 | 3-7 | 4 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 4 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | 0.000 | -0.687 |
| Jogador 5 | 4-2 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 25% | 5 → 7 | 4 | 7 → 7 | 0.000 | 0.961 |
| Jogador 5 | 4-3 | 5 | 0.000 | 12.000 | 0 → 0 | 1 → 3 | 25% → 25% | 7 → 8 | 6 | 7 → 7 | 0.000 | 0.577 |
| Jogador 5 | 4-4 | 9 | 2.000 | 0.000 | 0 → 0 | 3 → 2 | 25% → 25% | 8 → 9 | 9 | 7 → 7 | -0.032 | 0.000 |
| Jogador 5 | 4-5 | 7 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 9 → 8 | 10 | 7 → 7 | 0.000 | 0.416 |
| Jogador 5 | 4-6 | 9 | 0.000 | -2.000 | 0 → 0 | 2 → 3 | 25% → 25% | 8 → 10 | 12 | 7 → 7 | 0.000 | -0.309 |
| Jogador 5 | 4-7 | 10 | 6.000 | 0.000 | 0 → 1 | 3 → 3 | 25% → 25% | 10 → 5 | 13 | 7 → 8 | 0.023 | 0.000 |
| Jogador 5 | 5-1 | 8 | 10.000 | -12.000 | 1 → 1 | 3 → 3 | 25% → 29% | 5 → 12 | 2 | 8 → 8 | -0.010 | -0.344 |
| Jogador 5 | 5-2 | 12 | 0.000 | 8.000 | 1 → 1 | 3 → 3 | 29% → 29% | 12 → 12 | 21 | 8 → 8 | 0.005 | 0.240 |
| Jogador 5 | 5-3 | 12 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 29% → 29% | 12 → 8 | 18 | 8 → 8 | -0.005 | -0.228 |
| Jogador 5 | 5-4 | 12 | -6.000 | 10.000 | 1 → 1 | 3 → 2 | 29% → 25% | 8 → 6 | 16 | 8 → 8 | -0.009 | 0.000 |
| Jogador 5 | 5-5 | 12 | -42.000 | -62.000 | 1 → 0 | 2 → 0 | 25% → 0% | 6 → 11 | 16 | 8 → 8 | -0.032 | -0.237 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 24 ações e piorou em 27.
- Jogador 5 — estado final: ouro 11, nível 8, vida 8.0, colocação 3.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 6 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.171 | 0.000 |
| Jogador 6 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | 0.019 | 0.000 |
| Jogador 6 | 1-4 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.008 | 0.000 |
| Jogador 6 | 2-1 | 7 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.003 | 0.366 |
| Jogador 6 | 2-2 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 8 → 15 | 0 | 4 → 4 | -0.002 | 0.684 |
| Jogador 6 | 2-3 | 4 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 15 → 23 | 0 | 4 → 4 | 0.212 | 0.647 |
| Jogador 6 | 2-4 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 23 → 31 | 0 | 4 → 4 | -0.218 | 0.000 |
| Jogador 6 | 2-5 | 12 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 31 → 32 | 10 | 4 → 5 | 0.077 | 0.205 |
| Jogador 6 | 2-6 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 18% → 18% | 32 → 41 | 3 | 5 → 5 | 0.009 | 0.431 |
| Jogador 6 | 2-7 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 41 → 49 | 3 | 5 → 5 | -0.145 | 0.000 |
| Jogador 6 | 3-1 | 12 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 18% → 18% | 49 → 47 | 10 | 5 → 6 | 0.078 | -0.231 |
| Jogador 6 | 3-2 | 6 | 8.000 | -8.000 | 0 → 0 | 2 → 2 | 18% → 21% | 47 → 57 | 0 | 6 → 6 | -0.146 | 0.492 |
| Jogador 6 | 3-3 | 6 | -2.000 | 2.000 | 0 → 1 | 2 → 1 | 21% → 18% | 57 → 64 | 3 | 6 → 6 | -0.042 | -0.430 |
| Jogador 6 | 3-4 | 7 | 4.000 | -4.000 | 1 → 2 | 1 → 0 | 18% → 18% | 64 → 72 | 2 | 6 → 6 | -0.039 | 0.000 |
| Jogador 6 | 3-5 | 12 | 6.000 | 4.000 | 2 → 2 | 0 → 1 | 18% → 21% | 72 → 53 | 29 | 6 → 6 | 0.082 | -0.215 |
| Jogador 6 | 3-6 | 12 | 4.000 | 6.000 | 2 → 3 | 1 → 0 | 21% → 21% | 53 → 34 | 27 | 6 → 7 | -0.051 | -0.211 |
| Jogador 6 | 3-7 | 12 | 0.000 | 38.000 | 3 → 3 | 0 → 2 | 21% → 21% | 34 → 18 | 24 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 12 | 0.000 | 4.000 | 3 → 3 | 2 → 3 | 21% → 21% | 18 → 17 | 16 | 7 → 7 | 0.000 | -0.240 |
| Jogador 6 | 4-2 | 12 | -6.000 | 2.000 | 3 → 2 | 3 → 2 | 21% → 18% | 17 → 18 | 15 | 7 → 7 | 0.039 | -0.230 |
| Jogador 6 | 4-3 | 12 | 14.000 | 12.000 | 2 → 3 | 2 → 3 | 18% → 25% | 18 → 9 | 18 | 7 → 7 | -0.065 | 0.240 |
| Jogador 6 | 4-4 | 12 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 25% → 25% | 9 → 6 | 17 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 7 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 25% → 25% | 6 → 5 | 9 | 7 → 7 | 0.000 | -0.395 |
| Jogador 6 | 4-6 | 10 | 0.000 | -6.000 | 3 → 3 | 3 → 2 | 25% → 25% | 5 → 5 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-7 | 7 | 0.000 | -4.000 | 3 → 3 | 2 → 3 | 25% → 25% | 5 → 6 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 10 | 0.000 | -2.000 | 3 → 3 | 3 → 4 | 25% → 25% | 6 → 6 | 11 | 7 → 7 | 0.006 | -0.285 |
| Jogador 6 | 5-2 | 5 | -50.000 | -54.000 | 3 → 0 | 4 → 0 | 25% → 0% | 6 → 1 | 6 | 7 → 7 | 0.123 | -0.546 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 25 ações e piorou em 27.
- Jogador 6 — estado final: ouro 1, nível 7, vida 7.0, colocação 5.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 7 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.014 | 0.000 |
| Jogador 7 | 1-3 | 4 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.023 | 0.000 |
| Jogador 7 | 1-4 | 7 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 6 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 7 | 2-1 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 6 → 6 | 6 | 4 → 4 | -0.010 | 0.352 |
| Jogador 7 | 2-2 | 6 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 6 → 11 | 3 | 4 → 4 | 0.000 | 0.410 |
| Jogador 7 | 2-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 11 → 17 | 0 | 4 → 5 | 0.000 | -0.607 |
| Jogador 7 | 2-4 | 7 | 8.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 17 → 19 | 4 | 5 → 5 | -0.014 | 0.000 |
| Jogador 7 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 19 → 27 | 0 | 5 → 5 | 0.000 | 0.659 |
| Jogador 7 | 2-6 | 4 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 27 → 34 | 0 | 5 → 5 | 0.000 | -0.607 |
| Jogador 7 | 2-7 | 4 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 34 → 42 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 7 | 3-1 | 4 | -4.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 42 → 52 | 0 | 5 → 5 | 0.000 | -0.646 |
| Jogador 7 | 3-2 | 4 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 52 → 63 | 0 | 5 → 5 | 0.000 | -0.694 |
| Jogador 7 | 3-3 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 63 → 71 | 3 | 5 → 5 | 0.000 | -0.573 |
| Jogador 7 | 3-4 | 10 | 2.000 | 12.000 | 0 → 0 | 1 → 2 | 18% → 21% | 71 → 67 | 15 | 5 → 6 | -0.016 | 0.000 |
| Jogador 7 | 3-5 | 12 | 0.000 | 14.000 | 0 → 0 | 2 → 4 | 21% → 21% | 67 → 42 | 35 | 6 → 6 | -0.005 | -0.223 |
| Jogador 7 | 3-6 | 12 | -6.000 | 20.000 | 0 → 0 | 4 → 4 | 21% → 18% | 42 → 32 | 22 | 6 → 7 | -0.025 | -0.235 |
| Jogador 7 | 3-7 | 12 | 6.000 | -6.000 | 0 → 1 | 4 → 4 | 18% → 18% | 32 → 35 | 17 | 7 → 7 | 0.013 | 0.000 |
| Jogador 7 | 4-1 | 12 | 12.000 | 8.000 | 1 → 2 | 4 → 3 | 18% → 21% | 35 → 25 | 20 | 7 → 7 | -0.007 | -0.233 |
| Jogador 7 | 4-2 | 12 | 0.000 | 0.000 | 2 → 2 | 3 → 2 | 21% → 21% | 25 → 24 | 17 | 7 → 7 | 0.005 | 0.244 |
| Jogador 7 | 4-3 | 12 | 0.000 | 18.000 | 2 → 2 | 2 → 2 | 21% → 21% | 24 → 13 | 21 | 7 → 7 | -0.015 | -0.240 |
| Jogador 7 | 4-4 | 12 | 0.000 | -6.000 | 2 → 2 | 2 → 1 | 21% → 21% | 13 → 17 | 16 | 7 → 7 | 0.005 | 0.000 |
| Jogador 7 | 4-5 | 12 | -38.000 | -70.000 | 2 → 0 | 1 → 0 | 21% → 0% | 17 → 12 | 20 | 7 → 7 | 0.001 | -0.229 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 21 ações e piorou em 23.
- Jogador 7 — estado final: ouro 12, nível 7, vida 5.0, colocação 8.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.010 | 0.000 |
| Jogador 8 | 1-3 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 4 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 8 | 0.000 | -2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 4 → 8 | 1 | 3 → 4 | -0.023 | 0.000 |
| Jogador 8 | 2-1 | 5 | 2.000 | 0.000 | 1 → 1 | 0 → 0 | 7% → 11% | 8 → 12 | 1 | 4 → 4 | -0.004 | -0.464 |
| Jogador 8 | 2-2 | 8 | 8.000 | 2.000 | 1 → 1 | 0 → 0 | 11% → 14% | 12 → 9 | 9 | 4 → 4 | 0.019 | 0.308 |
| Jogador 8 | 2-3 | 12 | 4.000 | -2.000 | 1 → 0 | 0 → 0 | 14% → 18% | 9 → 8 | 13 | 4 → 5 | -0.051 | 0.228 |
| Jogador 8 | 2-4 | 5 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 11 | 3 | 5 → 5 | 0.151 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 11 → 17 | 3 | 5 → 5 | 0.017 | -0.248 |
| Jogador 8 | 2-6 | 8 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 17 → 23 | 3 | 5 → 5 | -0.111 | -0.304 |
| Jogador 8 | 2-7 | 8 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 23 → 31 | 0 | 5 → 5 | 0.111 | 0.000 |
| Jogador 8 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 31 → 40 | 0 | 5 → 5 | -0.199 | 0.679 |
| Jogador 8 | 3-2 | 8 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 40 → 45 | 4 | 5 → 6 | 0.105 | -0.329 |
| Jogador 8 | 3-3 | 6 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 18% → 21% | 45 → 52 | 3 | 6 → 6 | -0.002 | 0.506 |
| Jogador 8 | 3-4 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 52 → 22 | 36 | 6 → 7 | 0.004 | 0.000 |
| Jogador 8 | 3-5 | 5 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 25% | 22 → 31 | 0 | 7 → 7 | -0.026 | 0.570 |
| Jogador 8 | 3-6 | 11 | 2.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 31 → 10 | 28 | 7 → 7 | 0.004 | 0.267 |
| Jogador 8 | 3-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 10 → 8 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 2 | 25% → 25% | 8 → 7 | 11 | 7 → 7 | 0.000 | 0.416 |
| Jogador 8 | 4-2 | 7 | 8.000 | -2.000 | 0 → 0 | 2 → 1 | 25% → 29% | 7 → 8 | 10 | 7 → 8 | -0.005 | 0.426 |
| Jogador 8 | 4-3 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 29% → 29% | 8 → 13 | 4 | 8 → 8 | 0.000 | 1.012 |
| Jogador 8 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 13 → 22 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 2 | 29% → 29% | 22 → 28 | 4 | 8 → 8 | 0.000 | 0.978 |
| Jogador 8 | 4-6 | 3 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 29% → 29% | 28 → 35 | 4 | 8 → 8 | 0.000 | 1.028 |
| Jogador 8 | 4-7 | 4 | 0.000 | 16.000 | 0 → 0 | 2 → 2 | 29% → 29% | 35 → 37 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 6 | 0.000 | 26.000 | 0 → 0 | 2 → 2 | 29% → 29% | 37 → 35 | 13 | 8 → 8 | 0.000 | 0.501 |
| Jogador 8 | 5-2 | 10 | 2.000 | -4.000 | 0 → 0 | 2 → 2 | 29% → 29% | 35 → 45 | 10 | 8 → 8 | -0.029 | 0.307 |
| Jogador 8 | 5-3 | 7 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 29% → 29% | 45 → 50 | 11 | 8 → 8 | -0.009 | 0.412 |
| Jogador 8 | 5-4 | 12 | 0.000 | -8.000 | 0 → 0 | 2 → 3 | 29% → 29% | 50 → 65 | 14 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 12 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 29% → 29% | 65 → 74 | 17 | 8 → 8 | 0.000 | 0.253 |
| Jogador 8 | 5-6 | 12 | -6.000 | 2.000 | 0 → 0 | 4 → 3 | 29% → 25% | 74 → 81 | 18 | 8 → 8 | -0.053 | -0.229 |
| Jogador 8 | 5-7 | 12 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 81 → 85 | 20 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 12 | -4.000 | 6.000 | 0 → 0 | 3 → 1 | 25% → 21% | 85 → 91 | 15 | 8 → 8 | 0.000 | -0.233 |
| Jogador 8 | 6-2 | 12 | 6.000 | -6.000 | 0 → 0 | 1 → 2 | 21% → 25% | 91 → 101 | 16 | 8 → 8 | 0.000 | -0.233 |
| Jogador 8 | 6-3 | 12 | 0.000 | -10.000 | 0 → 0 | 2 → 3 | 25% → 25% | 101 → 111 | 17 | 8 → 8 | 0.005 | -0.233 |
| Jogador 8 | 6-4 | 12 | -6.000 | -2.000 | 0 → 0 | 3 → 4 | 25% → 21% | 111 → 123 | 19 | 8 → 8 | 0.010 | 0.000 |
| Jogador 8 | 6-5 | 12 | 2.000 | -6.000 | 0 → 0 | 4 → 4 | 21% → 25% | 123 → 137 | 19 | 8 → 8 | -0.008 | 0.257 |
| Jogador 8 | 6-6 | 12 | -44.000 | -56.000 | 0 → 0 | 4 → 0 | 25% → 0% | 137 → 125 | 19 | 8 → 8 | 0.019 | -0.233 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 30, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 18; mudanças de composição: 1; posicionamento melhorou em 31 ações e piorou em 34.
- Jogador 8 — estado final: ouro 125, nível 8, vida 1.0, colocação 2.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 43 | 16 | 0 | 0 | 0 | 0 | 6 | 4 | 4.474 |
| Jogador 2 | 70 | 41 | 0 | 0 | 2 | 0 | 7 | 8 | 2.9912 |
| Jogador 3 | 21 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 2.5919 |
| Jogador 4 | 47 | 16 | 0 | 0 | 0 | 0 | 8 | 0 | 4.5483 |
| Jogador 5 | 48 | 24 | 0 | 0 | 0 | 0 | 5 | 3 | 3.7775 |
| Jogador 6 | 46 | 21 | 0 | 0 | 1 | 0 | 5 | 3 | 4.1505 |
| Jogador 7 | 44 | 20 | 0 | 0 | 0 | 0 | 5 | 3 | 3.0415 |
| Jogador 8 | 79 | 48 | 2 | 2 | 2 | 0 | 9 | 7 | 2.1287 |
- Jogador 1 — venda DA_KogMaw18_AD (2-5, step 228): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Azir (4-3, step 493): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Tristana (4-5, step 535): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Shen (4-5, step 538): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Yorick (2-7, step 283): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (3-2, step 327): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Ahri (5-5, step 651): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_MasterYi_AD (5-5, step 653): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Ahri (5-7, step 684): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Hecarim (5-7, step 691): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Ahri (6-2, step 712): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Fiddlesticks18 (6-2, step 721): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_CrimsonRaptor18 (6-5, step 761): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Fiddlesticks18 (6-5, step 764): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_Fiddlesticks18 (4-4, step 516): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Diana (5-1, step 583): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_KogMaw18_AD (5-2, step 605): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yorick (5-2, step 610): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Diana (5-3, step 621): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_MasterYi_AD (5-5, step 660): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_CrimsonRaptor18 (4-3, step 497): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Zyra (4-6, step 554): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Caitlyn (5-1, step 583): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Camille (5-2, step 601): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Alistar (3-7, step 435): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rakan (4-1, step 459): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_CrimsonRaptor18 (4-4, step 518): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Diana (4-5, step 539): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Cassiopeia (2-5, step 229): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (4-2, step 472): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_18_Ezreal (5-4, step 636): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rammus (5-5, step 659): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rammus (5-6, step 669): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Soraka (5-6, step 671): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rammus (6-1, step 704): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Diana (6-4, step 744): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (6-4, step 747): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **7**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente. Ganhos nas três ações seguintes do mesmo round podem compensar uma venda; falta de ganho imediato isoladamente não gera penalidade.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 2-5 | 228 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-3 | 493 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Azir' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 4-5 | 535 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-5 | 538 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 5-2 | 2958 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-2 | 2959 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 2-2 | 520 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 3-3 | 1308 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-1 | 1992 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-1 | 2004 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-1 | 2068 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-2 | 2141 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-2 | 2177 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-7 | 283 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-1 | 302 | PURCHASE_REVERSED | Compra de DA_18_Kayle desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-2 | 327 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-2 | 472 | PURCHASE_REVERSED | Compra de DA_18_Ezreal desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 5-5 | 651 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ahri' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-7 | 684 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ahri' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-7 | 691 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-2 | 712 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ahri' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-2 | 721 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Fiddlesticks18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 6-5 | 761 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 164 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-4 | 258 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-1 | 364 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-2 | 458 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-3 | 517 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-4 | 576 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-5 | 635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-6 | 787 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-1 | 376 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 672 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 683 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 694 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 753 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-6 | 824 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-6 | 835 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-6 | 846 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-5 | 2005 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-6 | 2075 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-7 | 2160 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 3 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-2 | 139 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-3 | 222 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 5-3 | 2558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-3 | 2559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 2-2 | 519 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1087 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1098 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1133 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1144 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1155 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1166 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-1 | 1710 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-2 | 1937 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-3 | 2008 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-4 | 2168 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 4 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 5-1 | 2925 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-1 | 2926 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-2 | 519 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-4 | 649 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-6 | 842 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-6 | 853 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-6 | 864 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-6 | 875 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-6 | 886 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 5 | 5-2 | 605 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-2 | 610 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 5-5 | 660 | SOLD_CORE_UNIT | Venda de 'DA_18_MasterYi_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 1-2 | 115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 5-5 | 2935 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-5 | 2936 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 2-4 | 721 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-5 | 780 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-6 | 863 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-7 | 934 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-1 | 1005 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-2 | 1076 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-3 | 1235 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-3 | 1754 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-4 | 1863 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-4 | 1899 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-5 | 1970 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-6 | 2138 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-6 | 2150 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-6 | 252 | PURCHASE_REVERSED | Compra de DA_18_Varus desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-6 | 554 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Zyra' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 5-1 | 583 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 5-2 | 601 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 139 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-2 | 2915 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-2 | 2916 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 2-2 | 471 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-3 | 530 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 684 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-7 | 935 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-7 | 946 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-6 | 1668 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-6 | 1704 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-7 | 1775 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-7 | 1811 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-7 | 1872 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-1 | 1968 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-1 | 2005 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-7 | 435 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-4 | 518 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-5 | 539 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 1-3 | 222 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 1-4 | 318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 4-5 | 2410 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-5 | 2411 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 2-2 | 531 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-3 | 1064 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-3 | 1075 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-5 | 1332 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-6 | 1590 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-7 | 1747 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-1 | 1906 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 1-3 | 63 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-3 | 177 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 2-5 | 229 | SOLD_CORE_UNIT | Venda de 'DA_18_Cassiopeia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-4 | 636 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ezreal' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-5 | 659 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-6 | 669 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-6 | 671 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Soraka' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 6-4 | 744 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 6-4 | 747 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 151 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-3 | 246 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 6-6 | 4105 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-6 | 4106 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 2-4 | 862 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-5 | 969 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-6 | 1076 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-7 | 1135 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-1 | 1242 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 6-1 | 3443 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 6-2 | 3603 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
\n\n---\n\n## Evidências resumidas dos achados\n\nO relatório apresenta métricas agregadas e a timeline em tabelas. Esta seção complementa apenas os achados com o contexto mínimo da decisão; snapshots, máscaras brutas e diagnósticos completos não são duplicados em Markdown.\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 2-5 · step 228\n\nVenda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia SLOWROLL · motivo SLOWROLL: composição tem alvo de 3 estrelas\n- Estado: HP 95.0, nível 5, ouro 16, força 16.0\n- Composição: Inferno / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4923838973045349, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 1 · 4-3 · step 493\n\nVenda de 'DA_18_Azir' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 47.0, nível 7, ouro 9, força 46.0\n- Composição: Inferno / DA_18_Tristana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.26878461241722107, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Azir, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 4-5 · step 535\n\nVenda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 36.0, nível 7, ouro 0, força 42.0\n- Composição: Inferno / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4221692383289337, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Tristana, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 1 · 4-5 · step 538\n\nVenda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 36.0, nível 7, ouro 4, força 42.0\n- Composição: Inferno / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8550000190734863, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Shen, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 5-2 · step 2958\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 5-2 · step 2959\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_1_log.tft\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 1 · 2-2 · step 520\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=8, comp_direction=—, comp_focus=DA_18_Sejuani, reward=-0.06, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 1 · 3-3 · step 1308\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=62, comp_direction=Inferno, comp_focus=DA_18_Ezreal, reward=0.22, raw_action=BUY XP\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 1 · 4-1 · step 1992\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=17, comp_direction=Inferno, comp_focus=DA_18_Shen, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 1 · 4-1 · step 2004\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=15, comp_direction=Inferno, comp_focus=DA_18_Shen, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 1 · 4-1 · step 2068\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=7, comp_direction=Inferno, comp_focus=DA_18_Tristana, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 1 · 4-2 · step 2141\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=9, comp_direction=Inferno, comp_focus=DA_18_Tristana, reward=-0.24, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 1 · 4-2 · step 2177\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=7, comp_direction=Inferno, comp_focus=DA_18_Tristana, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 2-7 · step 283\n\nVenda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia SLOWROLL · motivo SLOWROLL: composição tem alvo de 3 estrelas\n- Estado: HP 94.0, nível 6, ouro 2, força 24.0\n- Composição: Colosso / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8520264625549316, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yorick, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 3-1 · step 302\n\nCompra de DA_18_Kayle desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia SLOWROLL · motivo SLOWROLL: composição tem alvo de 3 estrelas\n- Estado: HP 94.0, nível 6, ouro 8, força 24.0\n- Composição: Colosso / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3388069272041321, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=285, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 3-2 · step 327\n\nVenda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 94.0, nível 6, ouro 10, força 28.0\n- Composição: Colosso / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8921291828155518, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Rakan, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 4-2 · step 472\n\nCompra de DA_18_Ezreal desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 83.0, nível 7, ouro 9, força 46.0\n- Composição: Colosso / DA_18_Sejuani\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação 0.1013842225074768, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=454, cost=4, sale_gold_delta=4, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 5-5 · step 651\n\nVenda de 'DA_18_Ahri' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 9, força 58.0\n- Composição: Colosso / DA_18_Alune\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.252888560295105, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ahri, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 5-7 · step 684\n\nVenda de 'DA_18_Ahri' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 23, força 58.0\n- Composição: Colosso / DA_CrimsonRaptor18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3187280297279358, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ahri, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 5-7 · step 691\n\nVenda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 22, força 58.0\n- Composição: Colosso / DA_CrimsonRaptor18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.30373847484588623, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Hecarim, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 6-2 · step 712\n\nVenda de 'DA_18_Ahri' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 41, força 58.0\n- Composição: Colosso / DA_CrimsonRaptor18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3187251091003418, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ahri, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 6-2 · step 721\n\nVenda de 'DA_Fiddlesticks18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 40, força 58.0\n- Composição: Colosso / DA_CrimsonRaptor18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3870784640312195, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Fiddlesticks18, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 6-5 · step 761\n\nVenda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 59.0, nível 8, ouro 79, força 48.0\n- Composição: Colosso / DA_18_Lillia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4307846128940582, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_CrimsonRaptor18, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-2 · step 164\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-3 · step 223\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-4 · step 258\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-1 · step 364\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-2 · step 458\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-3 · step 517\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-4 · step 576\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-5 · step 635\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-6 · step 787\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_2_log.tft\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-1 · step 376\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=4, comp_direction=—, comp_focus=DA_18_Yorick, reward=0.04, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-5 · step 672\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=22, comp_direction=Colosso, comp_focus=DA_18_Sejuani, reward=-0.06, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-5 · step 683\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=18, comp_direction=Colosso, comp_focus=DA_18_Sejuani, reward=-0.14, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-5 · step 694\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=14, comp_direction=Colosso, comp_focus=DA_18_Sejuani, reward=0.01, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-5 · step 753\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=10, comp_direction=Colosso, comp_focus=DA_18_Sejuani, reward=-0.06, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-6 · step 824\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=10, comp_direction=Colosso, comp_focus=DA_18_Lillia, reward=-0.06, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-6 · step 835\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=6, comp_direction=Colosso, comp_focus=DA_18_Lillia, reward=-0.14, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 2 · 2-6 · step 846\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=2, comp_direction=Colosso, comp_focus=DA_18_Lillia, reward=-0.06, raw_action=BUY XP\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 2 · 4-5 · step 2005\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=2, comp_direction=Colosso, comp_focus=DA_18_Sejuani, reward=-0.03, raw_action=BUY XP\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 2 · 4-6 · step 2075\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=3, comp_direction=Colosso, comp_focus=DA_18_Sejuani, reward=-0.01, raw_action=BUY XP\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 2 · 4-7 · step 2160\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=0, comp_direction=Colosso, comp_focus=DA_18_Lux_Sunbeam, reward=-0.01, raw_action=BUY XP\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-2 · step 139\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-3 · step 222\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-3 · step 2558\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-3 · step 2559\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_3_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 3 · 2-2 · step 519\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=11, comp_direction=—, comp_focus=DA_Scuttlecrab18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 3-3 · step 1087\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=74, comp_direction=Inferno, comp_focus=DA_18_Rengar, reward=0.0, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 3-3 · step 1098\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=70, comp_direction=Inferno, comp_focus=DA_18_Rengar, reward=0.34, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 3-3 · step 1133\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=64, comp_direction=Inferno, comp_focus=DA_18_Rengar, reward=0.0, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 3-3 · step 1144\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=60, comp_direction=Inferno, comp_focus=DA_18_Rengar, reward=0.0, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 3-3 · step 1155\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=56, comp_direction=Inferno, comp_focus=DA_18_Rengar, reward=0.0, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 3 · 3-3 · step 1166\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=52, comp_direction=Inferno, comp_focus=DA_18_Rengar, reward=0.0, raw_action=BUY XP\n\n### MEDIUM · ECON_NON_UNIT_SPEND_BELOW_50_REVIEW · Jogador 3 · 4-1 · step 1710\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=ECON, strategy_reason=ECON: acumular até o limite de juros de 50, gold_after=31, comp_direction=Inferno, comp_focus=DA_Scuttlecrab18, reward=0.08, raw_action=BUY XP\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 3 · 4-2 · step 1937\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=36, comp_direction=Inferno, comp_focus=DA_Scuttlecrab18, reward=-0.16, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 3 · 4-3 · step 2008\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=45, comp_direction=Inferno, comp_focus=DA_Scuttlecrab18, reward=-0.19, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 3 · 4-4 · step 2168\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=15, comp_direction=Inferno, comp_focus=DA_Scuttlecrab18, reward=-0.09, raw_action=PASSOU TURNO\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 1-2 · step 127\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 5-1 · step 2925\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 5-1 · step 2926\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_4_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 4 · 2-2 · step 519\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=15, comp_direction=—, comp_focus=DA_Gromp18_AP, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 4 · 2-4 · step 649\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=30, comp_direction=Colosso, comp_focus=DA_Gromp18_AP, reward=-0.04, raw_action=PASSOU TURNO\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 4 · 2-6 · step 842\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=38, comp_direction=Fera do Rift, comp_focus=DA_CrimsonRaptor18, reward=-0.14, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 4 · 2-6 · step 853\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=34, comp_direction=Fera do Rift, comp_focus=DA_CrimsonRaptor18, reward=-0.06, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 4 · 2-6 · step 864\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=30, comp_direction=Fera do Rift, comp_focus=DA_CrimsonRaptor18, reward=-0.06, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 4 · 2-6 · step 875\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=26, comp_direction=Fera do Rift, comp_focus=DA_CrimsonRaptor18, reward=-0.14, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 4 · 2-6 · step 886\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=22, comp_direction=Fera do Rift, comp_focus=DA_CrimsonRaptor18, reward=0.05, raw_action=BUY XP\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 5-2 · step 605\n\nVenda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 22.0, nível 8, ouro 4, força 48.0\n- Composição: Colosso / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3933858275413513, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 5-2 · step 610\n\nVenda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 22.0, nível 8, ouro 5, força 48.0\n- Composição: Colosso / DA_Vi18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8365190625190735, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yorick, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 5-5 · step 660\n\nVenda de 'DA_18_MasterYi_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 8.0, nível 8, ouro 3, força 42.0\n- Composição: Colosso / DA_Vi18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2833857238292694, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_MasterYi_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-2 · step 115\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 5-5 · step 2935\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 5-5 · step 2936\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_5_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 2-4 · step 721\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=10, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 2-5 · step 780\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=16, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 2-6 · step 863\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=23, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 2-7 · step 934\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=30, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=-0.12, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 3-1 · step 1005\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=38, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=-0.13, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 3-2 · step 1076\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=47, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=-0.13, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 3-3 · step 1235\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=19, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=-0.06, raw_action=PASSOU TURNO\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 5 · 4-3 · step 1754\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=4, comp_direction=Colosso, comp_focus=DA_18_Morgana, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 5 · 4-4 · step 1863\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=3, comp_direction=Colosso, comp_focus=DA_Sentinel18, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 5 · 4-4 · step 1899\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=1, comp_direction=Colosso, comp_focus=DA_18_Sejuani, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 5 · 4-5 · step 1970\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=9, comp_direction=Colosso, comp_focus=DA_18_Sejuani, reward=-0.24, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 5 · 4-6 · step 2138\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=2, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=-0.09, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 5 · 4-6 · step 2150\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=0, comp_direction=Colosso, comp_focus=DA_KogMaw18_AD, reward=-0.09, raw_action=REROLL\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 6 · 2-6 · step 252\n\nCompra de DA_18_Varus desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 5, ouro 32, força 18.0\n- Composição: Devastador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.41924068331718445, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=235, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=0.0438\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 6 · 4-6 · step 554\n\nVenda de 'DA_18_Zyra' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 22.0, nível 7, ouro 4, força 50.0\n- Composição: Devastador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3405076861381531, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Zyra, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 6 · 5-1 · step 583\n\nVenda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 22.0, nível 7, ouro 6, força 50.0\n- Composição: Devastador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7519506812095642, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Caitlyn, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 6 · 5-2 · step 601\n\nVenda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 7.0, nível 7, ouro 6, força 50.0\n- Composição: Devastador / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7972040176391602, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Camille, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 1-2 · step 139\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-2 · step 2915\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-2 · step 2916\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_6_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 2-2 · step 471\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=15, comp_direction=—, comp_focus=DA_18_Rammus, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 2-3 · step 530\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=23, comp_direction=—, comp_focus=DA_18_Rammus, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 2-4 · step 684\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=23, comp_direction=Devastador, comp_focus=DA_18_Rammus, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 6 · 2-7 · step 935\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=43, comp_direction=Devastador, comp_focus=DA_KogMaw18_AD, reward=-0.03, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 6 · 2-7 · step 946\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=39, comp_direction=Devastador, comp_focus=DA_KogMaw18_AD, reward=-0.02, raw_action=BUY XP\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 6 · 3-6 · step 1668\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=18, comp_direction=Devastador, comp_focus=DA_18_Rammus, reward=-0.24, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 6 · 3-6 · step 1704\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=10, comp_direction=Devastador, comp_focus=DA_18_Rammus, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 6 · 3-7 · step 1775\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=12, comp_direction=Devastador, comp_focus=DA_18_Rammus, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 6 · 3-7 · step 1811\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=11, comp_direction=Devastador, comp_focus=DA_18_Rammus, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 6 · 3-7 · step 1872\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=10, comp_direction=Devastador, comp_focus=DA_18_Rammus, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 6 · 4-1 · step 1968\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=11, comp_direction=Devastador, comp_focus=DA_18_Rammus, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 6 · 4-1 · step 2005\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=9, comp_direction=Devastador, comp_focus=DA_18_Rammus, reward=-0.24, raw_action=REROLL\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 7 · 3-7 · step 435\n\nVenda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 32.0, nível 7, ouro 26, força 32.0\n- Composição: Vanguarda / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.35448169708251953, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Alistar, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 7 · 4-4 · step 518\n\nVenda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 5.0, nível 7, ouro 8, força 38.0\n- Composição: Vanguarda / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2392461597919464, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_CrimsonRaptor18, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 7 · 4-5 · step 539\n\nVenda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 5.0, nível 7, ouro 9, força 38.0\n- Composição: Vanguarda / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.39976921677589417, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-1 · step 68\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-2 · step 163\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-3 · step 222\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-4 · step 318\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-5 · step 2410\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-5 · step 2411\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_7_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 2-2 · step 531\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=11, comp_direction=—, comp_focus=DA_18_Hecarim, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 3-3 · step 1064\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=60, comp_direction=Vanguarda, comp_focus=DA_Sentinel18, reward=0.0, raw_action=BUY XP\n\n### MEDIUM · SLOWROLL_BUY_XP_REVIEW · Jogador 7 · 3-3 · step 1075\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=BUY_XP, strategy=SLOWROLL, strategy_reason=SLOWROLL: composição tem alvo de 3 estrelas, gold_after=56, comp_direction=Vanguarda, comp_focus=DA_Sentinel18, reward=0.46, raw_action=BUY XP\n\n### MEDIUM · FAST8_REROLL_REVIEW · Jogador 7 · 3-5 · step 1332\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=REROLL, strategy=FAST8, strategy_reason=FAST8: composição planejada exige nível 8, gold_after=33, comp_direction=Vanguarda, comp_focus=DA_Sentinel18, reward=-0.16, raw_action=REROLL\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-6 · step 1590\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=25, comp_direction=Vanguarda, comp_focus=DA_Fiddlesticks18, reward=-0.07, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-7 · step 1747\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=16, comp_direction=Vanguarda, comp_focus=DA_Fiddlesticks18, reward=-0.11, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 4-1 · step 1906\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=17, comp_direction=Vanguarda, comp_focus=DA_Fiddlesticks18, reward=-0.12, raw_action=PASSOU TURNO\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 8 · 1-3 · step 63\n\nCompra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 1, força 6.0\n- Composição: — / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7302599549293518, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=62, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=1.6945\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 8 · 2-3 · step 177\n\nCompra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 95.0, nível 4, ouro 9, força 18.0\n- Composição: — / DA_18_Cassiopeia\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.32243892550468445, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=176, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 2-5 · step 229\n\nVenda de 'DA_18_Cassiopeia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 95.0, nível 5, ouro 11, força 20.0\n- Composição: Fera do Rift / DA_Krug18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3695846199989319, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Cassiopeia, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 8 · 5-4 · step 636\n\nVenda de 'DA_18_Ezreal' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 73.0, nível 8, ouro 48, força 52.0\n- Composição: Caçador / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.256873220205307, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ezreal, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 8 · 5-5 · step 659\n\nVenda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 73.0, nível 8, ouro 60, força 52.0\n- Composição: Caçador / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.34261399507522583, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Rammus, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 8 · 5-6 · step 669\n\nVenda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 73.0, nível 8, ouro 74, força 52.0\n- Composição: Caçador / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3425622582435608, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Rammus, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 8 · 5-6 · step 671\n\nVenda de 'DA_18_Soraka' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 73.0, nível 8, ouro 74, força 52.0\n- Composição: Caçador / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.330046147108078, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Soraka, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 6-4 · step 744\n\nVenda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 1.0, nível 8, ouro 104, força 42.0\n- Composição: Caçador / DA_Amumu18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4640282392501831, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 6-4 · step 747\n\nVenda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 1.0, nível 8, ouro 109, força 42.0\n- Composição: Caçador / DA_Amumu18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5049999952316284, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Tristana, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-2 · step 151\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-3 · step 246\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 6-6 · step 4105\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 6-6 · step 4106\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261102-183512-a1bb6636\player_8_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 2-4 · step 862\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=11, comp_direction=Fera do Rift, comp_focus=DA_18_Rammus, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 2-5 · step 969\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=16, comp_direction=Caçador, comp_focus=DA_18_Tristana, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 2-6 · step 1076\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=23, comp_direction=Caçador, comp_focus=DA_18_Tristana, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 2-7 · step 1135\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=31, comp_direction=Caçador, comp_focus=DA_18_Tristana, reward=-0.12, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 3-1 · step 1242\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=37, comp_direction=Caçador, comp_focus=DA_Brambleback18, reward=-0.13, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 6-1 · step 3443\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=90, comp_direction=Caçador, comp_focus=DA_Amumu18, reward=-0.31, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 6-2 · step 3603\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=100, comp_direction=Caçador, comp_focus=DA_Amumu18, reward=-0.36, raw_action=PASSOU TURNO\n\n## Arquivos e rastreabilidade\n\n- Jogadores analisados: 8\n- Entradas analisadas: 4861\n- Decisões únicas estruturadas: 1587\n- Reconstruções textuais corroborativas (não somadas): 1587\n- Achados: 149\n- Os arquivos estruturados de origem permanecem separados deste relatório.\n- Campos ausentes são exibidos como “—”; não são inferidos como zero.\n